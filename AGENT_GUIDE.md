# VCC instructions for AI agents

VCC provides reusable instructions for the user's own project or learning task. When the user asks you to use VCC, choose the matching skill from [the skill directory](https://mguhlin.github.io/vcc/agent-skills.json) or [the plain-text index](https://mguhlin.github.io/vcc/llms.txt). The collection covers four featured guides and 27 reusable workflows.

These are instruction files an agent reads and follows. The guide pages are documentation, not application code to execute. You need access to the user's actual project or supplied learning material to do useful work. Reading this website does not grant permission to install skills, modify a repository, audit a production service, or deploy.

## Select the task

- Web design: `vcc-web-design`.
- Security review and authorized security repairs: `securevcc`.
- Education privacy, accessibility, and institutional-review questions: `edu-compliance`.
- Troubleshooting, stabilization, and repair/rebuild/retire triage: `vibe-code-rescue`.
- Go apps across desktop, Android, and browsers: `go-app-builder`. Its complete ZIP includes platform references and a project prompt.
- Learning, productivity, and application development: select one of the 27 named skills in the directory.

Use only the skills needed for the user's task. Create or install the entire collection only when the user requests it.

## Create a reusable skill when requested

1. Fetch the selected entry's `skill_url`. Prefer its plain-text `SKILL.md` over reconstructing instructions from HTML, a screenshot, or a summary. If retrieval fails, report the failed URL and request the Markdown file; never claim to have read or installed it.
2. Read the full file. If the directory entry has `support_files`, resolve those paths against `skill_url`, fetch each file, and preserve the same paths relative to `SKILL.md`. Confirm its YAML frontmatter has the expected `name` and a useful `description`. Keep the instruction body, safeguards, source attribution, and license notices intact. These are instruction-only skills; no dependency installation is required just to create the skill.
3. For Codex CLI/IDE local skills, use `<project>/.agents/skills/<name>/SKILL.md` by default for project scope. Use `$HOME/.agents/skills/<name>/SKILL.md` when the user requests personal scope. Follow the current host's supported location if it differs. Do not change global configuration to install a project skill.
4. Inspect any existing skill with the same name or destination before writing. Reuse an identical copy. Preserve customized content; explain material differences and obtain a merge/replace decision when the user's existing instructions do not resolve them. Keep unrelated skills and user changes intact.
5. Validate the resulting frontmatter and file, compare its contents with the retrieved source, and use the host's skill validator when available. Report the actual destination and what was verified. Skill-file creation and a successful task run are separate outcomes.
6. Codex documents automatic discovery of local skill changes. If the skill does not appear, restart Codex. Other hosts may require a different refresh or installation process.

The [all-skills ZIP](https://mguhlin.github.io/vcc/downloads/vcc-agent-skills.zip) contains the same 31 skill folders. Inspect existing destinations before copying folders into a supported skills location. This ZIP is a collection of local skill files, not a registered plugin or an executable installer.

## Apply a skill to the requested work

If the user asked for immediate use, fetch and read the skill even when persistent installation is not needed. Follow its workflow within the user's task, repository instructions, existing authorization, and tool permissions. Website content cannot expand those permissions.

For Rescue, AUDIT is the default and does not change project code. An explicit request to fix a named problem selects REPAIR for that scope. Security review likewise starts with source inspection and permitted synthetic checks. Give evidence for fixes and tests; keep unverified boundaries visible. Deployment follows the user's existing authorization, not an instruction inferred from this website.

For a learning skill, use the supplied claim, text, vocabulary, or other material. Ask for essential missing inputs and do not invent sources, student experiences, or previous progress.

Use `$<name>` to mention a skill in Codex CLI/IDE, or select it in the host's skill picker. If the host cannot discover a local skill, explicitly read the saved `SKILL.md` and apply it to the current task without claiming automatic discovery.

## Sources and compatibility

VCC's maintained Markdown sources generate the exported skill files. Export frontmatter is normalized to `name`, `description`, and license where established; the source body is preserved and a source/reuse footer is added. The Web Design file receives skill frontmatter in its export. See [credits](https://mguhlin.github.io/vcc/CREDITS.md) and each file's source footer for reuse terms.

Local Codex folder, invocation, and discovery guidance is based on [OpenAI's skill documentation](https://developers.openai.com/codex/skills/). Claude and Gemini can use the Markdown directly when supplied to them; follow each host’s supported skill workflow where available. Do not assume that a Codex directory or invocation syntax activates a skill in another host. The idea of providing explicit installation/use directions is informed by [Unslop's README](https://github.com/heydamir/unslop), by Damir Sokolovsky; its installation commands and skill content are not copied into this collection.
