# Maintaining and recovering VCC

VCC is a public static library. Its visitor workflow is browse → read → copy or download. It has no backend, visitor accounts, student uploads, or external AI calls. A skill is documentation for an assistant; installing or applying it is a separate user task. Preserve alphabetical sidebar order, the independently scrolling desktop list, the narrow-screen picker, fragment links, clipboard fallback, no-JavaScript reading route, and relative downloads.

## Recreate the build

Use Python 3.10 or newer and Git. The build dependencies are pinned in `requirements.txt`. Browser verification additionally needs Node.js 20 or newer, npm, the development dependencies in `package-lock.json`, and a Playwright-compatible Chromium browser. Local verification has used Python 3.13 and Node.js 20; CI performs source, build, and package verification on Ubuntu. CI does not currently run the browser suite.

Create an isolated Python environment, then install the documented build requirements:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/build.py
.venv/bin/python scripts/validate.py
.venv/bin/python scripts/package.py
.venv/bin/python scripts/verify_package.py
```

A normal checkout includes the published ZIPs and manifest. For a source-only copy that omits those outputs, run packaging once after the build and before link validation so download targets exist. Then run the full validation and package-verification sequence.

For browser checks, install the pinned development dependencies with `npm ci` and obtain a Chromium browser with `npx playwright install chromium`. In one terminal, serve the project:

```sh
python3 -m http.server 4186 --bind 127.0.0.1
```

In another terminal, run `npm test`. The default target is `http://127.0.0.1:4186/`. `VCC_URL` selects an authorized alternate target; `VCC_CHROME` selects an existing Chrome executable. `VCC_SCREENSHOTS=1` writes verification screenshots outside the project. Do not use real student or private district data in tests.

## Edit the maintained source

| Change | Maintained source | Generated distribution |
| --- | --- | --- |
| Featured guides | `WEB_DESIGN.md`, `EDU_COMPLIANCE.md`, `securevcc/securevcc.md`, `rescue/VIBE_CODE_RESCUE.md` | `guides/design.html`, `education.html`, `security.html`, `rescue.html` |
| Reusable skill | `skills/<slug>/SKILL.md`, `PROJECT_PROMPT.md`, `skills/catalog.json` | Sidebar workspace, agent exports, skill ZIPs |
| Skill introduction | `supplementals/REUSABLE_SKILLS.md` | `guides/skills.html` |
| Agent setup/use directions | `AGENT_GUIDE.md`, `agent-resources/featured.json`, `HOME_PROMPT.md` | `agent-skills/`, `agent-skills.json`, `llms.txt`, visible page sections |
| Supplemental resource | Its Markdown plus `supplementals/RESOURCE_LIBRARY.json` | Readable guide and resource catalog |
| Navigation/page template | `scripts/build.py` | Homepage navigation and guide shells |
| Layout and interactions | `assets/site.css`, `site.js`, `skills.js` | Served directly |
| Image artwork | Optimized assets, `assets/ARTWORK_PROMPTS.json`, skill hero `PROMPTS.json` | Served directly and bundled |
| Complete download | `scripts/package.py`, shared `project_files.py` | `downloads/vcc-complete.zip`, `SHA256SUMS.txt` |

Do not maintain generated Markdown exports or guide HTML independently. The homepage is authored HTML except for build-owned navigation. Keep its download inventory aligned with the catalog. The old creations/SecureVCC site is a migration redirect, not another maintained copy.

When adding a skill, give it a unique folder and matching catalog slug, a useful description, complete standalone instructions, a project prompt, category, group, provenance, and license. Optional `hero` and `hero_alt` fields refer to an optimized image and meaningful text description; record its dimensions and generation prompt in the hero metadata. Preserve third-party notices. Never imply that absent knowledge files, external services, research figures, or generated outputs are available.

## Diagnose failures without losing work

1. Inspect `git status --short` and the diff. Preserve unrelated changes. Identify the failing visitor task or build command and reproduce the smallest case.
2. If a guide differs from its source, rerun the build rather than patching generated HTML. If the source changes unexpectedly during a rebuild, inspect the relevant generator.
3. A missing link/anchor or image label fails `scripts/validate.py`. Catalog/source mismatches and stale skill ZIP content also fail there. Fix the maintained source and rebuild.
4. Clipboard denial should select the complete source and explain manual copying. It must never announce success when copying failed. The browser suite exercises this failure and the neighboring successful-copy path.
5. A stale checksum or complete ZIP fails `scripts/verify_package.py`. Run packaging after all source, image, test, and documentation changes; rerun verification afterward.
6. Repeated build drift is a reproducibility defect. Compare outputs in a separate clean checkout or temporary copy. Do not keep committing regenerated differences without locating the cause.

The package inventory excludes Git metadata, Python/Node environments, caches, bytecode, local `.env` files, and its own output archive. Dummy `.env.example` and `.env.sample` files may be shipped if needed; VCC currently requires no environment secrets. Public file symlinks are rejected. Review new files before committing: inventory exclusions do not establish that arbitrary document or asset content is safe to publish.

## Release and recovery

Run build, source validation, relevant browser checks, packaging, and complete-package verification. Review the diff and ensure no public maintenance timestamps were added. Commit the maintained sources and generated outputs together. Push under the owner's existing publication instructions, inspect the validation and Pages results, then verify meaningful live content and affected downloads. A passing local build is not evidence of a live deployment.

For a bad release, preserve the current diff and identify a known working revision. Revert the offending commit through normal Git history, rebuild and repackage if later source changes need to remain, run the checks, and publish the corrective commit. Do not use a destructive reset or overwrite a checkout containing unsaved work. A downloaded bundle can be inspected in a separate directory and its checksum manifest verified before using its files for recovery.

The automated suite covers sampled keyboard flows, mobile reflow, copy/download parity, all reusable-skill states, and automated accessibility scans. It does not establish full WCAG conformance, assistive-technology compatibility, legal compliance, or school approval. There is no server/database authorization flow to test in the current static site; reassess that boundary before adding accounts, uploads, analytics, or an AI service.
