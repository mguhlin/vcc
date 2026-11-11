#!/usr/bin/env python3
"""Validate VCC local references, document structure, and publication hygiene."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
import re,sys
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
 if any(p in {'.git','node_modules','__pycache__'} for p in path.relative_to(ROOT).parts):continue
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
 if path.suffix not in {'.md','.html','.txt','.json','.yml'} or any(p in {'.git','node_modules','__pycache__'} for p in path.relative_to(ROOT).parts):continue
 if pattern.search(path.read_text(errors='replace')):errors.append(f'{path.relative_to(ROOT)}: public maintenance timestamp')
# The complete security checklist must survive rendering.
raw=(ROOT/'securevcc/securevcc.md').read_text();rendered=(ROOT/'guides/security.html').read_text()
checks=re.findall(r'^- \*\*([A-Z][A-Z0-9]*-\d{2}) —',raw,re.M)
if len(checks)!=len(set(checks)) or any(c not in rendered for c in checks):errors.append('Security checklist lost during rendering')
if errors:print('\n'.join(errors));sys.exit(1)
print(f'Validated {len(pages)} HTML pages, local links/anchors, image labels, document structure, timestamp hygiene, and {len(checks)} security checks')
