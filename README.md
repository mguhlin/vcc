# Vibe-Coding Center (VCC)

Practical, educator-friendly guidance for creating websites with AI: purposeful design, safer code, student privacy, accessibility, and evidence before release.

**[Open VCC](https://mguhlin.github.io/vcc/)** · **[Complete download](https://mguhlin.github.io/vcc/downloads/vcc-complete.zip)**

## Start with your project

1. Read the educator introductions on the site.
2. Download `WEB_DESIGN.md`, `EDU_COMPLIANCE.md`, and `securevcc/securevcc.md` into your project root. The last file should be named `securevcc.md` there.
3. Copy `templates/PROJECT_BRIEF.md` into your project root and complete it without student information.
4. Explicitly ask your coding assistant to read and apply all three instruction files. If it cannot access files, attach or paste them. Presence alone is not activation.
5. Use `templates/PROMPTS.md` and `templates/LAUNCH_REVIEW.md` to gather evidence and unresolved decisions. Engineering checks do not replace school authorization or legal review.

## What is included

- Three core instruction files and readable HTML guides
- All SecureVCC reference and provenance materials, including its original upstream archive
- Project brief, prompt pack, launch review, and instruction-pointer examples
- Hero illustration, design playbook, and education compliance visual
- Supplemental repository recommendations and a decision for every supplied bookmark
- Static HTML/CSS/JS, Markdown sources, rebuild and packaging scripts

Third-party recommended repositories are linked, not installed or redistributed. See [CREDITS.md](CREDITS.md) for reuse details and [RESOURCE_REVIEW.md](RESOURCE_REVIEW.md) for review scope.

## Open or host the center

Unzip the complete bundle and open `index.html`. The guides, relative links, search, and reminders work directly as local files; clipboard copying may require a secure hosted context. External references require internet access. No service worker or installable PWA is provided.

To preview with HTTP, run `python3 -m http.server 4186 --bind 127.0.0.1` from this folder. Host the folder as static files; GitHub Pages publishes this repository’s main branch root. The `.nojekyll` file preserves static file paths.

## Rebuild

Python 3 and `markdown-it-py` (see `requirements.txt`) are needed to refresh the readable guides. They are build tools, not visitor dependencies.

```sh
python3 -m pip install -r requirements.txt
python3 scripts/build.py
python3 scripts/validate.py
python3 scripts/package.py
```

Optional browser verification: install the development dependencies with `npm install`, install a Playwright Chromium browser with `npx playwright install chromium`, serve the site locally, and run `npm test`. Set `VCC_URL` to the local or authorized live site. `VCC_CHROME` can point to an existing Chrome executable. The browser checks cover primary interactions, a sampled keyboard flow, mobile/reflow, and automated axe scans; they do not replace assistive-technology or full WCAG review.

Packaging puts every project component except Git metadata, caches, development-only browser dependencies, and the output archive itself into `downloads/vcc-complete.zip`, with a SHA-256 manifest. Do not include credentials or private project data.

## Add a resource

Add its Markdown source, introduction, and build mapping in `scripts/build.py`. Add a library entry in `index.html` with a category and download link. Document sources, licensing, the intended audience, and testing limits. Rebuild, validate, and package so online and downloaded copies agree. Keep public material free of maintenance timestamps and dated status labels.

VCC is a public/static resource library. It uses no visitor account, uploads, analytics, remote fonts, or application backend. GitHub Pages receives hosting requests. Search and reminder values remain in page memory. External services receive requests only when their links are followed.

## Design decision

VCC’s primary job is helping an educator find a useful guide or download in under a minute. A searchable field-guide library was chosen over a step-by-step wizard or a promotional landing page: visitors can enter at the task they already have, keep the full reference nearby, and download immediately. This is a design goal, not a measured user-study result.

The character is practical, warm, and deliberate. The visual world is an educator’s workbench; one illustrated scene carries the richness while the interface uses silver-white, navy and denim blue, readable system text, and serif headings. Three original instruction-file artworks form a visual gateway to distinct explanation pages; numbered field-guide entries organize the broader library. Spacing follows a 4-pixel scale, controls share clear focus states, and motion is unnecessary. Mobile stacks the same content in reading order. English is the authored interface language. The engineering accessibility target is WCAG 2.2 AA, without a conformance claim. The site is public/static (Tier 0) and has no student-data collection workflow.
