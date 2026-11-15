"""Generate instruction-only skill exports and visible, copyable agent directions."""
import html
import json
import re
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE='https://mguhlin.github.io/vcc/'


def skill_entries():
    featured=json.loads((ROOT/'agent-resources/featured.json').read_text())
    entries=[]
    for entry in featured:
        entries.append(dict(entry))
    for item in json.loads((ROOT/'skills/catalog.json').read_text()):
        entries.append(dict(name=item['slug'],key=item['slug'],title=item['title'],source=f"skills/{item['slug']}/SKILL.md",guide=f"guides/skills.html#{item['slug']}",description=f"Use for {item['category'].lower()}. {item['summary']}",license='CC0-1.0' if item.get('source') else 'CC-BY-4.0',use=f"Use {item['title']} for the task and material I supply in this conversation. Follow its workflow and safeguards, ask for essential missing inputs, and distinguish verified evidence from examples or uncertainty. If I ask for a vibe-coded application, use the matching project prompt from VCC and the project's existing design, education, and security instructions."))
    for entry in entries:
        entry['skill_path']=f"agent-skills/{entry['name']}/SKILL.md"
        entry['skill_url']=BASE+entry['skill_path']
        entry['guide_url']=BASE+entry['guide']
        entry['source_url']=BASE+entry['source']
    if len({e['name'] for e in entries})!=len(entries):raise ValueError('Duplicate agent skill name')
    return entries


def source_body(raw):
    if raw.startswith('---\n'):
        _,_,tail=raw.partition('---\n')
        _,separator,body=tail.partition('---\n')
        if not separator:raise ValueError('Unclosed source frontmatter')
        return body.lstrip('\n')
    return raw


def skill_export(entry):
    body=source_body((ROOT/entry['source']).read_text())
    front=f"---\nname: {entry['name']}\ndescription: {json.dumps(entry['description'],ensure_ascii=False)}\n"
    if entry['license']!='SEE-SOURCE':front+=f"license: {entry['license']}\n"
    front+='---\n\n'
    if entry['license']=='MIT':
        terms='The MIT notice in the source body remains part of this skill.'
    elif entry['license']=='CC0-1.0':
        terms='This adaptation retains CC0-1.0. Preserve its source attribution when useful.'
    elif entry['license']=='SEE-SOURCE':
        terms='VCC additions follow CC BY 4.0; the supplied source has no separate license notice. See the source and VCC credits for adaptation boundaries.'
    else:
        terms='VCC educational prose is CC BY 4.0. Attribute Miguel Guhlin and link to VCC; cited third-party material retains its own terms.'
    return front+body.rstrip()+f"\n\n## VCC source and reuse\n\nMaintained source: {entry['source_url']}\n\nReadable guide: {entry['guide_url']}\n\n{terms}\n\nCredits and terms: {BASE}CREDITS.md\n"


def setup_prompt(entry):
    name=entry['name']
    return f"Read {BASE}AGENT_GUIDE.md and create the {name} skill from {entry['skill_url']}. Read the entire SKILL.md. Use this project's .agents/skills/{name}/SKILL.md for Codex project scope, or the current host's supported project skill location. Inspect any existing same-name skill first, reuse an identical copy, and preserve customized content until any needed merge/replace decision is resolved. Preserve the complete instructions, source attribution, and license notices. Validate the name, description, and saved content against the downloaded file. Report the actual file path and validation result. This request creates the skill files; I will specify the project or learning task separately."


def use_prompt(entry):
    return f"Read {entry['skill_url']} in full and apply the {entry['name']} workflow to my requested task. {entry['use']} Respect my project instructions, existing authorization, and tool permissions. Report what you actually read, changed, or tested and what remains unverified. Persistent installation is optional for this use request."


def render_agent_instructions(key,level=2,prefix='../'):
    entry=next(e for e in skill_entries() if e['key']==key)
    name=entry['name'];ident='ai-agent-instructions' if level==2 else f'{name}-agent-instructions'
    setup_id=f'agent-{name}-setup';use_id=f'agent-{name}-use'
    esc=html.escape
    return f'''<section class="agent-instructions" id="{ident}" aria-labelledby="{ident}-title">
<h{level} id="{ident}-title">Use with an AI agent</h{level}>
<p>Ask your agent to read this skill and use it on your own project or learning task. The Markdown contains instructions to follow; the webpage is a readable guide.</p>
<p class="agent-links"><a href="{prefix}{entry['skill_path']}" download>Download agent-ready SKILL.md</a> · <a href="{prefix}AGENT_GUIDE.md">AI agent directions</a> · <a href="{prefix}llms.txt">All 13 skills</a></p>
<details class="agent-prompts"><summary>Create this skill or use it now</summary>
<p><strong>Skill name:</strong> <code>{name}</code></p><p><strong>Create it for this project.</strong> Copy this prompt to save a reusable skill. Your agent checks existing files before writing.</p>
<pre id="{setup_id}"><code>{esc(setup_prompt(entry))}</code></pre><div class="agent-copy"><button type="button" class="button secondary copy-button" data-copy="{setup_id}" data-copy-label="Setup prompt">Copy skill setup prompt</button><span class="copy-status" role="status"></span></div>
<p><strong>Use it on the current task.</strong> This prompt reads the skill and follows it with your supplied project or material.</p>
<pre id="{use_id}"><code>{esc(use_prompt(entry))}</code></pre><div class="agent-copy"><button type="button" class="button secondary copy-button" data-copy="{use_id}" data-copy-label="Use prompt">Copy skill use prompt</button><span class="copy-status" role="status"></span></div>
<p class="meta">Codex project location: <code>.agents/skills/{name}/SKILL.md</code>. For personal scope, request <code>$HOME/.agents/skills/{name}/SKILL.md</code>. Mention <code>${name}</code> in Codex CLI/IDE or use the host's skill picker. <a href="https://developers.openai.com/codex/skills/">OpenAI skill documentation</a>.</p>
</details></section>'''


def write_agent_resources():
    entries=skill_entries()
    manifest={'title':'VCC agent skill directory','instructions_url':BASE+'AGENT_GUIDE.md','bundle_url':BASE+'downloads/vcc-agent-skills.zip','skills':[]}
    paths=[]
    for entry in entries:
        path=ROOT/entry['skill_path'];path.parent.mkdir(parents=True,exist_ok=True);path.write_text(skill_export(entry));paths.append(path)
        manifest['skills'].append({k:entry[k] for k in ['name','title','description','source_url','guide_url','skill_url','license']})
    (ROOT/'agent-skills.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
    index='# Vibe-Coding Center\n\n> Thirteen instruction-only skills: four featured guides and nine learning/productivity workflows.\n\nRead AGENT_GUIDE.md when the user asks to create or use a VCC skill. Select the skill matching the task. Follow the user\'s project instructions and existing authorization.\n\n## Agent entry points\n\n'
    index+=f'- [Agent directions]({BASE}AGENT_GUIDE.md): selection, creation, validation, and use.\n- [Structured directory]({BASE}agent-skills.json): names, descriptions, sources, guides, and skill URLs.\n- [All skill files]({BASE}downloads/vcc-agent-skills.zip): thirteen local skill folders; no executable installer.\n\n## Featured guides\n\n'
    for i,entry in enumerate(entries):
        if i==4:index+='\n## Learning and productivity\n\n'
        index+=f"- [{entry['title']}]({entry['skill_url']}): `{entry['name']}`. [Readable guide]({entry['guide_url']}).\n"
    (ROOT/'llms.txt').write_text(index)
    with zipfile.ZipFile(ROOT/'downloads/vcc-agent-skills.zip','w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
        files=[(f"vcc-agent-skills/{p.parent.name}/SKILL.md",p.read_bytes()) for p in paths]
        files += [('vcc-agent-skills/README.md',(ROOT/'AGENT_GUIDE.md').read_bytes()),('vcc-agent-skills/agent-skills.json',(ROOT/'agent-skills.json').read_bytes())]
        for name,data in files:
            info=zipfile.ZipInfo(name,date_time=(1980,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16;archive.writestr(info,data)
    return entries


def render_home_agent_instructions():
    prompt=html.escape((ROOT/'agent-resources/HOME_PROMPT.md').read_text().strip())
    return f'''<section id="ai-agent-instructions" class="section agent-instructions" aria-labelledby="home-agent-title"><h2 id="home-agent-title">Give VCC to your AI agent</h2><p class="section-intro">Send your coding assistant here to choose and read a skill for your task. All four featured guides and nine reusable skills have agent-ready files and their own setup and use prompts.</p><div class="agent-links"><a href="AGENT_GUIDE.md">AI agent directions</a> · <a href="llms.txt">Plain-text skill index</a> · <a href="agent-skills.json">Structured directory</a> · <a href="downloads/vcc-agent-skills.zip" download>Download all 13 agent skills</a></div><details class="agent-prompts"><summary>Copy a prompt for your agent</summary><pre id="vcc-agent-entry-prompt"><code>{prompt}</code></pre><div class="agent-copy"><button type="button" class="button secondary copy-button" data-copy="vcc-agent-entry-prompt" data-copy-label="VCC agent prompt">Copy VCC agent prompt</button><span class="copy-status" role="status"></span></div></details></section>'''
