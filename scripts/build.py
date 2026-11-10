#!/usr/bin/env python3
"""Render trusted, repository-owned Markdown as accessible static VCC guides."""
import html,re
from pathlib import Path
from markdown_it import MarkdownIt
ROOT=Path(__file__).resolve().parents[1]
md=MarkdownIt('commonmark',{'html':False}).enable('table')
GUIDES=[
('design','Make the design fit the job','WEB_DESIGN.md','Design starts with the task. Tell your assistant who will use the site, what they need to do, and what would make that task easier. Then choose a structure and test it.','design-playbook.webp','AI Design Playbook for Education Websites: function-first structure, purposeful style, accessibility, privacy, and evaluation'),
('security','Look beyond “it works”','securevcc/securevcc.md','SecureVCC is the security component of VCC. Ask for source evidence and safe synthetic tests. A hidden button, a working login, or a clean scanner report does not establish that private information is protected.','securevcc/assets/securevcc-workstation.webp','Illustrated workstation for the SecureVCC security review'),
('education','Put students’ needs first','EDU_COMPLIANCE.md','Begin by asking what information the educational task actually needs. Avoid collecting student information when the activity works without it. The guide separates engineering safeguards from legal review and school authorization.','education-compliance.webp','Education compliance guide: privacy, security, accessibility, student safety, and documentation'),
('project-brief','Write a better starting brief','templates/PROJECT_BRIEF.md','Define one observable learning task, the intended audience, and the information the tool needs. Copy the template into your project and replace the questions with real decisions.','',''),
('launch','Gather evidence before sharing','templates/LAUNCH_REVIEW.md','Keep a record of the actual journeys you tried, the results, and the decisions a school or project owner still needs to make. Unknowns stay visible.','',''),
('prompts','Keep the AI focused','templates/PROMPTS.md','Use these prompts with your project and the three instruction files. Adapt them to the task, use invented data, and ask for evidence rather than reassurance.','',''),
('resource-vetting','A selective shelf, an honest review','RESOURCE_REVIEW.md','This ledger explains every supplied bookmark, the additional references, and the limits of this review. Recommendations are reference choices, not security endorsements.','','')]
EXPLAINERS={
'design': ('Use this when the layout feels generic—or before a first build', 'WEB_DESIGN.md asks your assistant to decide the audience, the main task, and the page structure before choosing colors and components. A lesson library should make browsing easy; a classroom game should get learners into the activity.', ['Write a small design brief with observable success criteria.', 'Compare different structures, then choose a consistent visual direction.', 'Check keyboard use, readability, reflow, data flows, and working behavior.'], 'Read WEB_DESIGN.md. Inspect this project and explain who it serves, what the visitor must accomplish, and which page structure best supports that task. Preserve working features and show how you will test the result.'),
'security': ('Use this before release, and whenever a feature changes the risk', 'SecureVCC helps a coding assistant investigate what the application actually permits. For a static resource page, the review is small. Accounts, shared files, payments, or student records call for deeper checks appropriate to those features.', ['Start with private credentials, trust boundaries, and actual data access.', 'Validate suspected problems using safe, invented examples.', 'Separate confirmed vulnerabilities from suggestions and tests not run.'], 'Read securevcc.md. Review this project within the authorized scope. Inspect source and use safe local synthetic tests. Report evidence for confirmed findings, fix what you can safely fix, and identify checks that remain unverified.'),
'education': ('Use this before a school or student is asked to trust the tool', 'EDU_COMPLIANCE.md brings education-specific questions into the build: ages, information collected, accessibility, vendors, retention, sharing, and who can authorize student use. It helps prepare for institutional review; it does not grant that approval.', ['Map information in forms, device storage, URLs, logs, and external services.', 'Identify applicable school, contract, privacy, and accessibility questions.', 'Document safeguards and unresolved decisions without inventing compliance claims.'], 'Read EDU_COMPLIANCE.md. Inspect what this project actually collects, stores, shares, and deletes. Classify its education and data risks. Prefer a prototype with invented data until required safeguards and school decisions are resolved. Report evidence and unknowns.')}
HEADER='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} — Vibe-Coding Center</title><meta name="description" content="{desc}"><meta name="referrer" content="strict-origin-when-cross-origin"><meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'"><link rel="canonical" href="https://mguhlin.github.io/vcc/guides/{slug}.html"><link rel="stylesheet" href="../assets/site.css?v=blue-silver-compact"><link rel="icon" href="../assets/favicon.svg" type="image/svg+xml"></head><body><a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="wrap header-inner"><a class="brand" href="../"><span>VCC</span> Vibe-Coding Center</a><nav aria-label="Main"><a href="../#library">Resource library</a><a href="../#start">Start here</a><a href="../#tools">Helpful GitHubs</a><a href="../#download">Download</a></nav></div></header>'''
for slug,title,source,intro,image,alt in GUIDES:
 raw=(ROOT/source).read_text()
 if raw.startswith('---\n'):raw=raw.split('---\n',2)[-1]
 body=md.render(raw)
 # Guides are nested one directory below project-root downloads.
 if slug=='resource-vetting':body=body.replace('href="RESOURCE_REVIEW.md"','href="../RESOURCE_REVIEW.md"')
 body=re.sub(r'<(/?)h([1-6])>',lambda m:'<'+m[1]+'h'+str(min(6,int(m[2])+1))+'>',body)
 toc=[];ids={}
 def heading(m):
  level,text=m.groups();label=re.sub('<[^>]+>','',text);base=re.sub(r'[^a-z0-9]+','-',html.unescape(label).lower()).strip('-') or 'section'
  ids[base]=ids.get(base,0)+1;ident=base+('-'+str(ids[base]) if ids[base]>1 else '')
  if level=='3':toc.append((ident,html.unescape(label)))
  return f'<h{level} id="{ident}">{text}</h{level}>'
 body=re.sub(r'<h([2-6])>(.*?)</h\1>',heading,body,flags=re.S)
 body=body.replace('<table>','<div class="table-scroll" tabindex="0" role="region" aria-label="Reference table"><table>').replace('</table>','</table></div>')
 rail='<aside class="guide-rail" aria-label="Guide navigation"><div><a href="../#library">← All resources</a><p><strong>In this guide</strong></p><a href="#overview">Overview</a>' + ''.join(f'<a href="#{i}">{html.escape(t)}</a>' for i,t in toc)+'</div></aside>'
 visual=''
 if image:
  image_path='../'+image if image.startswith('securevcc/') else '../assets/'+image
  visual=f'<figure><a href="{image_path}"><img src="{image_path}" alt="{html.escape(alt)}" width="1600" height="900" loading="lazy"></a><figcaption class="meta">Visual overview; the full text instructions below provide the detail. <a href="{image_path}" download>Download image</a></figcaption></figure>'
 explanation=''
 if slug in EXPLAINERS:
  sub,meaning,points,prompt=EXPLAINERS[slug]
  explanation='<section class="guide-explainer"><h2>'+html.escape(sub)+'</h2><p>'+html.escape(meaning)+'</p><h3>What the guide helps you do</h3><ul>'+''.join('<li>'+html.escape(point)+'</li>' for point in points)+'</ul><h3>Try this with your coding assistant</h3><blockquote>'+html.escape(prompt)+'</blockquote><p class="meta">Download the instruction file and explicitly ask your assistant to read it. Keep real student information out of sample prompts and public test records.</p></section>'
 extra='<p class="note">For the combined VCC starter prompt, save this download as <code>securevcc.md</code> in your project root. <a href="../securevcc/SOURCES.md">Security sources</a> · <a href="../securevcc/README.md">Additional security usage notes</a></p>' if slug=='security' else ''
 page=HEADER.format(title=html.escape(title),desc=html.escape(intro),slug=slug)+f'<main class="wrap guide-layout" id="main">{rail}<article class="guide-content"><p class="eyebrow">Vibe-Coding Center / Field guide</p><h1 id="overview">{title}</h1><p>{html.escape(intro)}</p><p><a class="button" href="../{source}" download>Download {Path(source).name}</a></p>{extra}{visual}{explanation}<h2>Full reference</h2>{body}</article></main><footer class="site-footer"><div class="wrap footer-inner"><p>Vibe-Coding Center · <a href="https://mguhlin.org/">Miguel Guhlin</a></p><p><a href="../CREDITS.md">Credits &amp; reuse</a> · <a href="../SOURCES.md">Sources</a><br>Design refinement: <a href="https://github.com/heydamir/unslop">unslop by Damir Sokolovsky</a> (CC BY 4.0).</p></div></footer></body></html>'
 (ROOT/'guides'/f'{slug}.html').write_text(page)
print(f'Rendered {len(GUIDES)} guides')
