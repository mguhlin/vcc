#!/usr/bin/env python3
"""Validate VCC local references, document structure, and publication hygiene."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
import re,sys,json,zipfile
from project_files import LOCAL_DIRS
ROOT=Path(__file__).resolve().parents[1]
errors=[];pages={}
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=[];self.h1=0;self.lang=False;self.title=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='html':self.lang=bool(a.get('lang'))
  if tag=='title':self.title=True
  if tag=='h1':self.h1+=1
  for k in ['href','src']:
   if a.get(k):self.links.append(a[k])
  if tag=='img' and 'alt' not in a:errors.append('Image missing alt')
for path in ROOT.rglob('*.html'):
 if any(p in LOCAL_DIRS for p in path.relative_to(ROOT).parts):continue
 page=Page();page.feed(path.read_text());pages[path]=page
 if not page.lang or not page.title or page.h1!=1:errors.append(f'{path.relative_to(ROOT)}: invalid document landmarks/title/h1')
 if len(page.ids)!=len(set(page.ids)):errors.append(f'{path}: duplicate IDs')
 for link in page.links:
  parsed=urlsplit(link)
  if parsed.scheme or parsed.netloc:continue
  target=(path.parent/unquote(parsed.path)).resolve() if parsed.path else path
  if target.is_dir():target=target/'index.html'
  if not target.exists():errors.append(f'{path.relative_to(ROOT)}: missing {link}')
for path,page in pages.items():
 for link in page.links:
  parsed=urlsplit(link)
  if parsed.scheme or parsed.netloc or not parsed.fragment:continue
  target=(path.parent/unquote(parsed.path)).resolve() if parsed.path else path
  if target.is_dir():target=target/'index.html'
  if target in pages and unquote(parsed.fragment) not in pages[target].ids:errors.append(f'{path.relative_to(ROOT)}: missing anchor {link}')
pattern=re.compile(r'last[ -](?:updated|modified|reviewed)\s*[:：]|generated on\s*[:：]|(?:checked|reviewed|updated|modified)\s+(?:on\s+)?\d{4}-\d{2}-\d{2}',re.I)
for path in ROOT.rglob('*'):
 if path.suffix not in {'.md','.html','.txt','.json','.yml'} or any(p in LOCAL_DIRS for p in path.relative_to(ROOT).parts):continue
 if pattern.search(path.read_text(errors='replace')):errors.append(f'{path.relative_to(ROOT)}: public maintenance timestamp')
# The complete security checklist must survive rendering.
raw=(ROOT/'securevcc/securevcc.md').read_text();rendered=(ROOT/'guides/security.html').read_text()
checks=re.findall(r'^- \*\*([A-Z][A-Z0-9]*-\d{2}) —',raw,re.M)
if len(checks)!=len(set(checks)) or any(c not in rendered for c in checks):errors.append('Security checklist lost during rendering')
for entry in json.loads((ROOT/'agent-resources/featured.json').read_text()):
 version=entry['version'];slug=entry['key']
 label=f'<span class="guide-version" aria-label="Version {version}">v{version}</span>'
 if type(version) is not int or version<1:errors.append(f'{slug}: invalid source revision count')
 if not re.search(rf'<a class="foundation" href="guides/{slug}\.html"><strong>[^<]+ '+re.escape(label),(ROOT/'index.html').read_text()):errors.append(f'{slug}: homepage guide version is stale')
 if label not in (ROOT/'guides'/f'{slug}.html').read_text():errors.append(f'{slug}: guide version is stale')
# Catalog, distribution copies, and source files must describe the same collection.
catalog=json.loads((ROOT/'skills/catalog.json').read_text())
slugs=[item['slug'] for item in catalog]
folders={p.parent.name for p in (ROOT/'skills').glob('*/SKILL.md')}
if len(slugs)!=len(set(slugs)) or set(slugs)!=folders:errors.append('Reusable skill catalog does not match source folders')
manifest=json.loads((ROOT/'agent-skills.json').read_text())
if len(manifest['skills'])!=len(catalog)+4:errors.append('Agent directory count does not match the collection')
with zipfile.ZipFile(ROOT/'downloads/reusable-skills.zip') as bundle:
 for item in catalog:
  for name in ['SKILL.md','PROJECT_PROMPT.md',*item.get('support_files',[])]:
   path=ROOT/'skills'/item['slug']/name
   if bundle.read('vcc/'+path.relative_to(ROOT).as_posix())!=path.read_bytes():errors.append(f'Stale reusable skill bundle: {path}')
  if item.get('bundle'):
   with zipfile.ZipFile(ROOT/item['bundle']) as individual:
    expected={f'{item["slug"]}/{name}':(ROOT/'skills'/item['slug']/name).read_bytes() for name in ['SKILL.md','PROJECT_PROMPT.md',*item.get('support_files',[])]}
    if len(individual.namelist())!=len(expected) or set(individual.namelist())!=set(expected):errors.append(f'Incomplete individual skill bundle: {item["slug"]}')
    for name,data in expected.items():
     if individual.read(name)!=data:errors.append(f'Stale individual skill component: {name}')
  if item.get('hero'):
   if bundle.read('vcc/'+item['hero'])!=(ROOT/item['hero']).read_bytes():errors.append(f'Stale hero: {item["slug"]}')
   raw=(ROOT/'skills'/item['slug']/'SKILL.md').read_text()
   prompt=(ROOT/'skills'/item['slug']/'PROJECT_PROMPT.md').read_text()
   if re.search(r'\b(?:TCEA|GPTs?|bots?)\b',raw+'\n'+prompt,re.I):errors.append(f'Legacy assistant branding in {item["slug"]}')
with zipfile.ZipFile(ROOT/'downloads/vcc-agent-skills.zip') as bundle:
 for entry in manifest['skills']:
  path=ROOT/'agent-skills'/entry['name']/'SKILL.md'
  if bundle.read(f'vcc-agent-skills/{entry["name"]}/SKILL.md')!=path.read_bytes():errors.append(f'Stale agent bundle: {entry["name"]}')
  for file in entry.get('support_files',[]):
   support=path.parent/file
   source=(ROOT/'skills'/entry['name']/file).read_bytes()
   if bundle.read(f'vcc-agent-skills/{entry["name"]}/{file}')!=source or support.read_bytes()!=source:errors.append(f'Stale agent support file: {support}')
if errors:print('\n'.join(errors));sys.exit(1)
print(f'Validated {len(pages)} HTML pages, local links/anchors, image labels, document structure, timestamp hygiene, and {len(checks)} security checks')
