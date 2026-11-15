"""Build the skills reading workspace and original vector concept sketches."""
import html
import json
import zipfile
from pathlib import Path
from agent_resources import render_agent_instructions

ROOT = Path(__file__).resolve().parents[1]


def concept_image(item):
    """Original, code-native wireframes; all meaningful content has a text caption."""
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="960" height="520" viewBox="0 0 960 520" role="img" aria-labelledby="title desc">',
             f'<title id="title">{html.escape(item["project"])}</title><desc id="desc">{html.escape(item["concept"])}</desc>',
             '<rect width="960" height="520" fill="#e2e7ed"/>',
             '<path d="M24 68H936V496H24Z" fill="#fff" stroke="#8b9daf" stroke-width="2"/>']

    def text(x, y, value, size=22, color='#182e46', serif=False):
        parts.append(f'<text x="{x}" y="{y}" font-family="{ "Georgia,serif" if serif else "system-ui,sans-serif"}" font-size="{size}" fill="{color}">{html.escape(value)}</text>')

    def line(x, y, end, color='#ced7e0'):
        parts.append(f'<path d="M{x} {y}H{end}" stroke="{color}" stroke-width="2"/>')

    def box(x, y, w, h, fill='#f1f3f5'):
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="#8b9daf"/>')

    def writing(x, y, w, label, hint):
        text(x, y, label, 23)
        text(x, y+36, hint, 19, '#445b70')
        line(x, y+64, x+w)
        line(x, y+93, x+w-35)

    text(24, 44, item['project'], 30, serif=True)
    slug=item['slug']
    if slug == 'sift-approach':
        box(24,68,230,428,'#f1f3f5')
        for i,s in enumerate(['Stop','Investigate','Find coverage','Trace']):
            if i==0:box(24,88,230,60,'#e2e7ed')
            text(48,128+i*76,f'{i+1}. {s}',23)
        writing(294,122,594,'What claim are you checking?','Write the exact claim here.')
        writing(294,290,594,'Pause before deciding','What was your first reaction?')
        text(294,465,'Keep notes     /     Continue to Investigate',20,'#214f7f')
    elif slug == 'prism-thinking':
        for i,s in enumerate(['Patterns','Reasoning','Ideas','Situation','Methods']):
            text(47+i*178,112,s,22,'#214f7f')
        line(48,136,912,'#8b9daf')
        writing(60,186,820,'Your observation','What do you notice?')
        writing(60,350,820,'Go a little deeper','What evidence supports your explanation?')
    elif slug == 'outline-helper':
        parts.append('<path d="M470 92V398" stroke="#8b9daf" stroke-width="2"/>')
        writing(52,122,378,'Source notes','Paste nonconfidential sample notes.')
        text(510,122,'Traditional outline',24)
        for i,(x,s) in enumerate([(510,'I. Meeting context'),(540,'A. Purpose'),(510,'II. Discussion'),(540,'A. Key topic'),(570,'1. Supporting detail')]):text(x,174+i*42,s,22)
        line(52,410,908)
        text(52,450,'Next steps',23)
        text(258,450,'Owner: Unassigned     /     Deadline: Not specified',20,'#445b70')
    elif slug == 'quadrant-notes':
        parts.append('<path d="M480 92V460M48 280H912" stroke="#8b9daf" stroke-width="2"/>')
        for x,y,label,hint in [(56,122,'Main ideas','Which ideas matter most?'),(510,122,'Supporting details','What evidence supports them?'),(56,322,'Personal connections','This reminds me of…'),(510,322,'Summary and synthesis','How do the ideas fit together?')]:writing(x,y,375,label,hint)
    elif slug == 'ai-citation-assistant':
        box(24,68,390,428,'#f1f3f5')
        text(52,120,'Source details',24)
        for i,s in enumerate(['Source type','Author or organization','Title','Style and edition','DOI or stable URL']):
            text(52,165+i*60,s,20);line(52,181+i*60,378)
        writing(454,122,430,'Citation draft','Verify style rules before formatting.')
        writing(454,300,430,'AI-use disclosure','Include only actions that occurred.')
        text(454,465,'Missing details stay visible.',20,'#214f7f')
    elif slug == 'vocabulary-enhancement':
        text(54,120,'Word + intended meaning',25)
        line(54,150,902)
        for i,s in enumerate(['Introduce','Show meaning','Use in context','New application']):
            x=54+i*216
            box(x,190,198,150,'#f1f3f5')
            text(x+12,223,str(i+1),24,'#214f7f')
            text(x+12,313,s,18)
        text(54,390,'Explain it without your notes.',25)
        text(54,435,'Retrieval exit ticket + teacher preparation notes',21,'#445b70')
    elif slug == 'freewriting-coach':
        text(56,120,'FLOW',26,'#214f7f')
        text(635,120,'05:00    Pause    Finish',23)
        line(56,148,900)
        text(56,193,'The door opened and…',28,serif=True)
        for y,end in [(250,870),(292,900),(334,740)]:line(56,y,end)
        parts.append('<path d="M56 367V399" stroke="#214f7f" stroke-width="3"/>')
        text(56,455,'Keep ideas moving. Reflect when you choose to finish.',22,'#445b70')
    elif slug == 'compare-options':
        text(52,120,'What must this option do?',24)
        text(52,160,'Must-haves first. Preferences next.',21,'#445b70')
        for i,row in enumerate([['Criterion','Option A','Option B'],['Time available','Evidence needed','Evidence needed'],['Device access','Unknown','Unknown'],['Small trial','Plan a test','Plan a test']]):
            y=218+i*56
            for j,value in enumerate(row):text(52+j*290,y,value,21,'#214f7f' if i==0 else '#182e46')
            line(52,y+18,908)
        text(52,465,'What unknown could change your choice?',23)
    else:
        text(52,122,'Keep the claim beside its evidence.',26)
        rows=[['Original claim','Source + location','Finding'],['Claim one','Add evidence','Unresolved'],['Claim two','Add evidence','Unresolved']]
        for i,row in enumerate(rows):
            y=194+i*65
            for j,value in enumerate(row):text(52+j*290,y,value,22,'#214f7f' if i==0 else '#182e46')
            line(52,y+22,908)
        writing(52,402,830,'Next verification action','What would resolve the uncertainty?')
    parts.append('</svg>')
    path=ROOT/'assets/skills'/f'{slug}.svg'
    path.write_text('\n'.join(parts)+'\n')


def render_skills(md):
    items=json.loads((ROOT/'skills/catalog.json').read_text())
    intro=(ROOT/'supplementals/REUSABLE_SKILLS.md').read_text().split('\n',1)[1]
    intro,howto=intro.split('## From instructions to a working tool',1)
    opening=md.render(intro)
    help_text=md.render('## From instructions to a working tool'+howto)
    links=[];panels=[]
    for item in items:
        slug=item['slug'];e=lambda value:html.escape(value,quote=True)
        concept_image(item)
        raw=(ROOT/'skills'/slug/'SKILL.md').read_text()
        prompt=(ROOT/'skills'/slug/'PROJECT_PROMPT.md').read_text()
        links.append(f'<li data-skill-entry><a href="#{slug}" data-skill-link="{slug}"><span>{e(item["title"])}</span><small>{e(item["category"])}</small></a></li>')
        origin=f'{e(item["origin"])} · <a href="../skills/SOURCES.md">Sources &amp; reuse</a>'
        if item.get('source'):origin+=f' · <a href="{e(item["source"])}">Upstream skill (CC0)</a>'
        panels.append(f'''<article class="skill-panel" id="{slug}" data-skill-panel>
<h2 class="skill-title" id="{slug}-title" tabindex="-1">{e(item['title'])}</h2>
<p class="skill-summary">{e(item['summary'])}</p><p class="meta">{origin}</p>
<div class="skill-actions"><button type="button" class="button" data-skill-copy="{slug}-raw" data-copy-label="Skill">Copy skill</button><a href="../skills/{slug}/SKILL.md" download>Download SKILL.md</a><a href="#{slug}-file">Read full skill</a><span class="skill-status" role="status"></span></div>
{render_agent_instructions(slug,level=3)}
<figure class="skill-concept"><a href="../assets/skills/{slug}.svg"><img src="../assets/skills/{slug}.svg" alt="{e(item['concept'])}" width="960" height="520" loading="lazy"></a><figcaption><strong>Concept sketch: {e(item['project'])}.</strong> A possible interface, not a working app.</figcaption></figure>
<section class="skill-prompt" aria-labelledby="{slug}-project"><h3 id="{slug}-project">Turn this skill into a project</h3>
<p>Copy this prompt with the skill and VCC’s three instruction files. Adapt the audience and subject before building.</p>
<label for="{slug}-prompt">Project prompt</label><textarea id="{slug}-prompt" readonly rows="12" spellcheck="false">{e(prompt)}</textarea>
<pre class="skill-print-source">{e(prompt)}</pre><div class="skill-actions"><button type="button" class="button secondary" data-skill-copy="{slug}-prompt" data-copy-label="Project prompt">Copy project prompt</button><a href="../skills/{slug}/PROJECT_PROMPT.md" download>Download prompt</a><span class="skill-status" role="status"></span></div></section>
<section class="skill-source" aria-labelledby="{slug}-file"><h3 id="{slug}-file">Full skill file</h3><label for="{slug}-raw">{slug}/SKILL.md</label><textarea id="{slug}-raw" readonly rows="18" spellcheck="false">{e(raw)}</textarea><pre class="skill-print-source">{e(raw)}</pre><p class="meta">Read or select the full Markdown here. The Copy skill button copies the entire file.</p></section>
</article>''')
    content=f'''<main class="wrap skills-page" id="main"><header class="skills-intro"><h1>Reusable skills</h1>{opening}
<details class="skills-help"><summary>How to use these skills and prompts</summary>{help_text}</details></header>
<div class="skills-layout" data-skills><aside class="skills-sidebar" aria-label="Skill browser"><div class="skills-sidebar-inner">
<div class="skill-filter" hidden><label for="skill-search">Find a skill</label><input id="skill-search" type="search" placeholder="Try writing or evidence" autocomplete="off"><button class="skill-clear" type="button">Clear search</button><p class="meta" id="skill-count" role="status">{len(items)} skills</p></div>
<nav aria-label="Reusable skills"><ul>{''.join(links[:7])}<li class="skill-group">Adapted from repositories</li>{''.join(links[7:])}</ul></nav><p class="skill-empty" hidden>No matching skills. Clear the search to see all nine.</p>
<p><a href="../downloads/reusable-skills.zip" download>Download all nine skills</a></p></div></aside>
<div class="skills-workspace">{''.join(panels)}</div></div></main>'''
    paths=sorted((ROOT/'skills').rglob('*'))+sorted((ROOT/'assets/skills').glob('*.svg'))+[ROOT/'supplementals/REUSABLE_SKILLS.md']
    with zipfile.ZipFile(ROOT/'downloads/reusable-skills.zip','w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
        for path in paths:
            if not path.is_file():continue
            info=zipfile.ZipInfo('vcc/'+path.relative_to(ROOT).as_posix(),date_time=(1980,1,1,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16
            archive.writestr(info,path.read_bytes())
    return content
