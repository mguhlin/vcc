# Vibe-Coding Center (VCC)

Practical, educator-friendly guidance for creating websites with AI: purposeful design, safer code, student privacy, accessibility, and evidence before release.

**[Open VCC](https://mguhlin.github.io/vcc/)** · **[Complete download](https://mguhlin.github.io/vcc/downloads/vcc-complete.zip)**

## Start with your project

1. Read the educator introductions and open **Supplementals → Start here** on the site.
2. Download `WEB_DESIGN.md`, `EDU_COMPLIANCE.md`, and `securevcc/securevcc.md` into your project root. The last file should be named `securevcc.md` there.
3. Copy `templates/PROJECT_BRIEF.md` into your project root and complete it without student information.
4. Explicitly ask your coding assistant to read and apply all three instruction files. If it cannot access files, attach or paste them. Presence alone is not activation.
5. Use `templates/PROMPTS.md` and `templates/LAUNCH_REVIEW.md` to gather evidence and unresolved decisions. Engineering checks do not replace school authorization or legal review.

## What is included

- Four featured Markdown guides: Web Design, Security, Education Privacy, and Vibe-Code Rescue
- 24 reusable skills with full Markdown, project prompts, concept images, and a sidebar browser
- 28 agent-ready skill exports with individual setup and use prompts
- All SecureVCC reference and provenance materials, including its original upstream archive
- Project brief, prompt pack, launch review, and instruction-pointer examples
- Four-checks cartoon hero and a coordinated series of four featured-guide illustrations
- Classroom-sharing and publishing cartoons with text walkthroughs, optimized web images, and PNG downloads
- A focused GitHub shelf with optional additions labeled by instruction-file coverage
- Supplemental resource library, start, classroom-sharing, and blog pages in a shared navigation dropdown
- An About page linked from every site footer
- Resource notes preserving the decisions for the original supplied bookmarks
- Static HTML/CSS/JS, Markdown sources, rebuild and packaging scripts

Third-party recommended repositories are linked, not installed or redistributed. See [CREDITS.md](CREDITS.md) for reuse details and [RESOURCE_REVIEW.md](RESOURCE_REVIEW.md) for review scope.

## Open or host the center

Unzip the complete bundle and open `index.html`. The guides, relative links, search, and reminders work directly as local files; clipboard copying may require a secure hosted context. External references require internet access. No service worker or installable PWA is provided.

To preview with HTTP, run `python3 -m http.server 4186 --bind 127.0.0.1` from this folder. Host the folder as static files; GitHub Pages publishes this repository’s main branch root. The `.nojekyll` file preserves static file paths.

## Rebuild

Python 3.10 or newer and `markdown-it-py` (see `requirements.txt`) are needed to refresh the readable guides. They are build tools, not visitor dependencies.

```sh
python3 -m pip install -r requirements.txt
python3 scripts/build.py
python3 scripts/validate.py
python3 scripts/package.py
python3 scripts/verify_package.py
```

Optional browser verification: install the development dependencies with `npm install`, install a Playwright Chromium browser with `npx playwright install chromium`, serve the site locally, and run `npm test`. Set `VCC_URL` to the local or authorized live site. `VCC_CHROME` can point to an existing Chrome executable. The browser checks cover primary interactions, a sampled keyboard flow, mobile/reflow, and automated axe scans; they do not replace assistive-technology or full WCAG review.

Packaging puts every public project component except Git metadata, caches, local environment files, Python/Node environments, and the output archive itself into `downloads/vcc-complete.zip`, with a SHA-256 manifest. Do not include credentials or private project data.

## AI agent setup and use

The [VCC agent directions page](https://mguhlin.github.io/vcc/guides/ai-agent.html) links to `AGENT_GUIDE.md`, generated `llms.txt`, and `agent-skills.json`. The four featured guides and each of the 24 reusable skills include a visible agent section with a direct `SKILL.md` download and separate copyable setup/use prompts. These prompts create local skill files only when requested and apply workflows within existing project instructions and user authorization.

Edit `AGENT_GUIDE.md`, `agent-resources/featured.json`, `agent-resources/HOME_PROMPT.md`, the original guide Markdown, and `skills/catalog.json` as appropriate. `scripts/agent_resources.py` generates all 28 `agent-skills/<name>/SKILL.md` exports, normalizing frontmatter and adding source/reuse footers. The original bodies and attribution are retained. Exported Web Design receives skill metadata; the Education report template uses a project revision field. The generated files are distribution copies, not independently maintained sources or skills installed in this checkout. Rebuild with `scripts/build.py` before validating and packaging.

`downloads/vcc-agent-skills.zip` contains all 28 exported skill folders, an agent readme, and the directory. The existing 24-skill project-starter ZIP remains available. The complete VCC bundle and SHA-256 manifest include both collections and the machine-readable entry points. Codex project/personal scope and invocation guidance cites OpenAI's documentation; other hosts should use their supported locations. No installer, dependency, backend, or external AI connection is added.

## Vibe-Code Rescue

[Vibe-Code Rescue](https://mguhlin.github.io/vcc/guides/rescue.html) is the fourth front-page guide. Its maintained source is `rescue/VIBE_CODE_RESCUE.md`, adapted from the supplied ZIP; provenance and changes are in `rescue/SOURCES.md`. It focuses on reproducible setup, useful diagnostics, focused repairs, and repair/rebuild/retire decisions. The security-specific baseline and new `SUPPLY-03` / `OPS-04` checks are integrated into `securevcc/securevcc.md`, which generates the existing security page. Both guides link to each other and remain usable as standalone Markdown. The complete VCC ZIP and checksum manifest include the maintained files and original rescue illustration. The 24 reusable skills remain in their sidebar collection.

## Reusable skills

Open [Reusable skills](https://mguhlin.github.io/vcc/guides/skills.html). The seven original supplied files, two CC0 repository adaptations, 14 creator adaptations, and the supplied Build Texas Classroom Crosswalk skill live under `skills/<name>/SKILL.md`. Each folder includes an authored `PROJECT_PROMPT.md`. The catalog lives in `skills/catalog.json`; the introduction is `supplementals/REUSABLE_SKILLS.md`. Edit these Markdown and catalog sources before rebuilding. `scripts/skills_library.py` renders the workspace and original SVG wireframes, includes the new WebP hero artwork, and creates a deterministic `downloads/reusable-skills.zip`. The complete archive includes all of them. Attribution and adaptation notes are in `skills/SOURCES.md`.

The skills workspace lists titles alphabetically. On desktop, the reading rail keeps search and downloads in view while the title list scrolls. On phones and narrow windows, open the skill picker and scroll the page to browse. Selecting a skill closes the picker, and Browse skills opens it again. Copy buttons preserve the complete source; the fallback selects text for manual copying. Direct fragment links, browser history, search, individual downloads, and a no-JavaScript reading route keep the collection usable. Navy text, silver surfaces, and a blue selection marker carry through the shared theme and skill concept sketches. Alternatives considered were an accordion and a sequential wizard; the sidebar supports repeated browsing and copying with fewer steps. Ten entries use vector interface plans. The 14 creator adaptations use editorial hero artwork with descriptive alternatives. Neither represents a working application. Hero generation prompts are preserved in `assets/skills/heroes/PROMPTS.json`. The library remains public/static (Tier 0); filter state stays in memory, and clipboard writes occur only on request. The proposed projects default to local manual scaffolds and require separate review before external AI integration.

## Add a resource

Add its Markdown source, introduction, and build mapping in `scripts/build.py`. Supplemental pages use `supplementals/` for Markdown and `guides/` for rendered HTML; add their links to `SUPPLEMENTALS` in the build script to update navigation everywhere. Add a catalog entry in `supplementals/RESOURCE_LIBRARY.json` with a category and download link; paths are relative to the project root. Document sources, licensing, the intended audience, and testing limits. Rebuild, validate, and package so online and downloaded copies agree. Keep public material free of maintenance timestamps and dated status labels.

VCC is a public/static resource library. It uses no visitor account, uploads, analytics, remote fonts, or application backend. GitHub Pages receives hosting requests. Search and reminder values remain in page memory. External services receive requests only when their links are followed.

## Design decision

VCC’s primary job is helping an educator find a useful guide or download in under a minute. A searchable field-guide library was chosen over a step-by-step wizard or a promotional landing page: visitors can enter at the task they already have, keep the full reference nearby, and download immediately. This is a design goal, not a measured user-study result.

The character is practical, warm, and deliberate. The interface uses white pages, a dark blue header with silver text, and blue and silver accents, with readable system text and serif headings. The Four Checks Before You Share cartoon introduces the four featured guides in a navy-and-silver two-by-two comic. It displays beside the hero text with full-size and text-version links. The original Three Essential Checks image is retained in the classroom-sharing guide. The GitHub and Netlify cartoons share a supplemental publishing page with text walkthroughs and original downloads. Four instruction-guide cards pair titles and short descriptions with matching navy-and-silver workbench illustrations. The same artwork appears in the guides. Each complete card links to its explanation page; on mobile, the cards stack for readable images. The reusable-skills introduction and download section follow the cards. The searchable eight-resource catalog lives under Supplementals → Resource library, with numbered entries and direct file downloads. Supplemental workflows live on their own reading pages, reached through a native disclosure dropdown shared by the homepage and all guides. The homepage keeps the three core guides, companion rescue guide, download, and Flipboard preview easy to scan. The Supplemental menu links to the repository shelf, agent directions, and About. Spacing follows a 4-pixel scale, controls share clear focus states, and motion is unnecessary. Mobile stacks the same content in reading order. English is the authored interface language. The engineering accessibility target is WCAG 2.2 AA, without a conformance claim. The site is public/static (Tier 0) and has no student-data collection workflow.

The rescue addition extends the established guide layout and palette. The primary educator tasks are choosing audit versus repair, downloading the workflow, and reaching detailed security checks. The existing reading rail, native links, and a copyable audit prompt support those tasks without new dependencies, accounts, or data collection. Verification covers the fourth card, linked guides and downloads, copy action, keyboard access, narrow-screen reflow, and automated accessibility checks.

The Web Design featured guide incorporates a focused Modern Web Guidance adaptation in `WEB_DESIGN.md` and an educator explanation in `supplementals/MODERN_WEB_GUIDANCE.md`. It covers platform features, browser targets, fallbacks, text scaling, and measured loading/interaction improvements. The same source flows into `agent-skills/vcc-web-design/SKILL.md` and the all-skills bundle. Upstream code and CLI packages are linked resources, not runtime dependencies.

The Reusable Skills introduction pairs its explanation with compact toolbox artwork, capped at 320 CSS pixels on desktop and 280 on stacked layouts. It uses the open space beside the copy without enlarging the page hero.

See [MAINTAINING.md](MAINTAINING.md) for isolated setup, maintained-versus-generated file boundaries, diagnostics, complete-archive verification, publishing checks, and recovery without discarding work.
