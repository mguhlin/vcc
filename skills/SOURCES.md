# Reusable skills: sources and adaptations

## Audiobook Maker

**Original workflow: Lance Eaton. VCC adaptation: Miguel Guhlin.** [Audiobook Maker](audiobook-maker/SKILL.md) adapts Eaton's **Book to Audio Edition** prompts from [leaton79/book-to-audiobook](https://github.com/leaton79/book-to-audiobook), linked in his blog post [AI Audiobooks: An Update](https://aiedusimplified.substack.com/p/ai-audiobooks-an-update). Eaton developed the original workflow with Claude. This is an attributed adaptation, not a claim of endorsement or VCC authorship of the original method.

The repository explicitly licenses code **and documentation** under MIT. The full `Copyright (c) 2026 Lance Eaton` notice travels inside the maintained skill, agent export, and downloadable copies. The blog identifies its own CC BY-SA 4.0 terms; VCC links to the post and adapts the separately MIT-licensed repository prompts rather than reproducing the blog. No blog imagery, book text, upstream scripts, dependencies, or voice models are redistributed.

Source identities from the GitHub connector:

| Repository file | Git blob |
| --- | --- |
| `prompts/chat-only-prompt.md` | `37751f4c753b33e3a8eabd2a2038c76bafff7431` |
| `prompts/code-assistant-prompt.md` | `f760aaac0abdd1403bacf51a7abd90f4d32af069` |
| `README.md` | `58fea1f3fb11409399c587f800f365f66bc28ba3` |
| `LICENSE` | `ab7d1eced19bb5e2fbe9c37616c4e1a2ded5bece` |

VCC renames and reformats the workflow, separates text preparation from optional audio synthesis, and adds explicit chat/file capability boundaries, permitted processing destinations, a representative pilot, conservative handling of unique sidebars and citations, traceable note relocation, uncertain OCR handling, source-block reconciliation, interruption recovery, and final text re-extraction. It avoids treating matching endpoints, OCR word-frequency scores, or extraction ratios as proof that nothing was lost. Required notices remain in the delivered package even when excluded from narration.

The separately authored [project prompt](audiobook-maker/PROJECT_PROMPT.md), concept sketch, and [free local audio reference](audiobook-maker/references/free-local-audio.md) follow VCC's CC BY 4.0 terms. The reference cites official Piper, Kokoro, Balabolka, and FFmpeg documentation and distinguishes engine/model licenses from book rights. The complete skill folder ZIP and both collection ZIPs include the project prompt and local audio reference. These are instructions, not a completed converter or claims of tested speech quality on a full book.

## Supplied collection

Miguel Guhlin supplied the full text of SIFT Approach, PRISM Thinking Coach, Outline Helper, Quadrant Note-Taking, AI Citation Assistant, Vocabulary Enhancement, and Freewriting Coach. Their Markdown instructions are preserved as supplied; the Freewriting description is quoted so its colon parses correctly as YAML. These seven files follow VCC's CC BY 4.0 educational-prose terms; attribute Miguel Guhlin and link to VCC. SIFT's underlying framework is credited to Mike Caulfield in the skill. No ownership of that framework is claimed.

The project prompts and original SVG concept sketches are VCC additions. They illustrate potential browser-local projects; they are not screenshots, evaluated learning products, or claims of automatic AI functionality. No upstream image assets or external fonts are used.

## Repository adaptations

Public repository discovery covered mguhlin/creations and mglearn repositories. The two additions selected for this collection come from mguhlin/creations; no mglearn material is redistributed.

- [Compare options source](https://github.com/mguhlin/creations/blob/main/architect/skills/packages/compare-options-skill/SKILL.md), source blob `1ad4c49537011deb77d10b88d08f5885498ef9f7`, by Miguel Guhlin, CC0-1.0.
- [Source integrity source](https://github.com/mguhlin/creations/blob/main/architect/skills/packages/source-integrity-skill/SKILL.md), source blob `4e38e1a93798072fe39328751281bdbbca92a16e`, by Miguel Guhlin, CC0-1.0.

Both source files were read through the GitHub connector. Adaptations shorten their instructions into standalone workflows, add output structures and classroom examples, preserve evidence and uncertainty safeguards, and remove references to upstream `eval.md` practice files. The adaptations retain CC0-1.0. No upstream scripts, dependencies, practice files, or images are bundled. Upstream licenses were identified from each file's explicit frontmatter.

## Boundaries

These files instruct an assistant; they are not installed into a visitor's account. Project prompts ask for manual evidence entry and scaffolded practice first. Citation templates require official style verification before use; source-evaluation tools must not claim to have fetched or verified a source without doing so. The library does not make new legal or citation-style determinations.

## Creator adaptations

Miguel Guhlin supplied additional instructional specifications and three local source files. Fourteen standalone skills adapt those materials. The educational instructions and project prompts follow VCC's CC BY 4.0 terms, except the MIT-adapted ClearCopy skill body. Named frameworks retain their attribution; no ownership of their underlying methods is claimed.

| Supplied material | VCC skill | Adaptation |
| --- | --- | --- |
| Four-framework skeptical evaluator | Signal Scout | Verified framework definitions, explicit unknown ratings, transparent scoring, and one-step Socratic mode. |
| ETHICAL decision guidance | Northstar Decisions | Seven supplied stages, facts versus values, stakeholder perspectives, and a human authorization boundary. |
| District technology plan analyzer | District Systems Compass | Evidence-linked rubrics, KPIs, lifecycle planning, and qualified standards alignment. |
| Workshop designer | Workshop Foundry | Timed activities, facilitator notes, realistic practice, and accessible alternatives. |
| School AI policy development | Policy Forge | Context, gap analysis, policy drafting, stakeholder review, and rollout. |
| School AI policy consultant | Policy Lens | Existing-policy review, privacy, equity, inspectability, human oversight, and accountability. |
| Conference proposal evaluator | Session Lens | Preserved 20/20/20/40 rubric; an optional three-point bonus requires an explicit low-score cutoff and is shown separately from raw scoring. |
| Excellent session proposal guidance | Proposal Spark | Specific takeaways, realistic scope, practical examples, and a proposal-readiness review. |
| Instructional design synthesis | Learning Loom | Workshop, one-pager, and coaching modes; effect sizes only from a supplied `CheckEffectSizes.md`. |
| Madlib story and image instructions | Wonder Weave | One choice at a time, scene before image, unambiguous style choices, and honest image-tool capability checks. |
| Professional learning strategy partner | Strategy Studio | Goal-driven strategy planning and reflection; unavailable source files and research figures are identified rather than invented. |
| `flipbook_calendar.md` | Daylight Pages | Portable build guidance, consistent calendar arithmetic, local preferences, keyboard navigation, projection, printing, and truthful teacher-note privacy. |
| `vimeo_download_skill.txt` | Archive Harbor | Authorized supported downloads, complete inventory checks, dialog identity checks, and honest completion verification. |
| `watermarks-remover-main.zip` | ClearCopy | Inspect-first text and format-aware metadata hygiene; attribution and required disclosures preserved. |

Organization-specific branding, subscription/account requirements, obsolete assistant roles, and a recurring feedback-form request were removed. New titles and 14 original generated hero illustrations accompany the adaptations. The original nine SVG interface sketches remain. `assets/skills/heroes/PROMPTS.json` preserves the image-generation prompts; WebP images are optimized distribution assets. These are conceptual visuals, not application screenshots.

Missing knowledge files (`CheckEffectSizes.md`, `p8.txt`, `p6.txt`, `prism.txt`, `PRISM_Science.md`, and `exemplars.md`) are not bundled or claimed as consulted. Research numbers, local standards mappings, legal conclusions, and example district case details are not invented. Legal and current technical references must be verified for the user's context when applying a skill. The supplied proposal examples are used for principles rather than copied quotations or historic legal deadlines.

Framework references include [Melanie Trecek-King's FLOATER](https://thinkingispower.com/floater-a-tool-kit-for-evaluating-claims/), [Wayne R. Bartz's original CRITIC publication](https://skepticalinquirer.org/2002/09/teaching-skepticism-via-the-critic-acronym-and-the-skeptical-inquirer/), [Gil Duran's Orwell Test](https://www.theframelab.org/the-orwell-test/), and [Mike Caulfield's SIFT](https://hapgood.us/2019/06/19/sift-the-four-moves/). The Orwell Test is Facts/Source/Method, not a fabricated letter expansion. Signal Scout's scores are instructional judgments, not calibrated truth probabilities. Conference scoring expresses a suggested evaluation, not an official event decision.

### Local source identity

The supplied files remain outside the public repository. Their content identities are recorded for provenance:

| Source | SHA-256 |
| --- | --- |
| `flipbook_calendar.md` | `7d257b3bcd7443adc301dc5dba1f15ddd00348d5941a56cd1aee658a8a762b0f` |
| `vimeo_download_skill.txt` | `7492d971c37f7560220d53dc9f64921c01572b28d4be7a5854b4af07e14fcfa7` |
| `watermarks-remover-main.zip` | `2ece1888289281285484eef25432725084424f599e182506181877d7ec4d42ad` |

The archive identifies [watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) as its upstream. Its README, two skill files, and MIT notice were inspected. No executable, HTTP service, Docker setup, model weights, or optional watermark-removal backends were run or redistributed. The adapted skill retains the full MIT notice from the archive. Optional dependencies require their own separate license and capability review before any future installation. Source skill hashes: `clean-user-facing-text/SKILL.md` is `2787e78b8332502d93519c57e087e10d9e09d6a5fe9867f15c0b11ced462618c`; `remove-ai-marks/SKILL.md` is `3f128e0cbd77ad170ac2be639ebe881afe4e02417ea8a7846b53b440e77c6495`.

Archive Harbor does not infer successful downloads from button clicks or identical file sizes. It checks files only when an authorized filesystem capability exists. Daylight Pages treats collapsed teacher notes as present in the public document, not access-controlled. ClearCopy preserves multilingual controls, code, citations, and provenance unless a specific authorized change is justified; it makes no guarantee about undetectability or removal of hidden media marks.


## Build Texas Classroom Crosswalk

The user supplied `build-texas-classroom-crosswalk.zip` for VCC. Its skill instructions, framework reference with citations, icon, and agent metadata are preserved. The archive included no separate license notice. VCC’s project prompt and concept sketch follow its CC BY 4.0 terms.


## Go App Builder

Go App Builder is original VCC educational guidance by Miguel Guhlin, offered under CC BY 4.0. It synthesizes reusable implementation and testing patterns with primary documentation from Go, desktop and mobile framework maintainers, Microsoft, Apple, Android, browser-platform documentation, W3C, and OWASP. [Its source guide](go-app-builder/references/sources.md) maps references to the decisions they support and the facts an assistant must recheck for a selected version and deployment.

The skill does not copy an individual application's identity, source code, credentials, binaries, or development-specific file paths. Platform references, the project prompt, and agent metadata travel in its complete folder ZIP and both skill collection downloads. The original code-drawn concept sketch accompanies the reading page, reusable-skills ZIP, and complete VCC bundle. No SDK, runtime installer, framework code, or build dependency is installed or redistributed just by reading or saving this skill. The four VCC guides are linked companion reviews, not claims of security, accessibility, legal certification, or institutional approval.

## WebDecks

Web Deck v5 is by Miguel Guhlin, published at [mguhlin/webdecks](https://github.com/mguhlin/webdecks) under MIT. VCC includes distribution snapshots of `webdeck_spec_v5.md`, `webdeck_v5_standalone.md`, `assets/deck-framework.css`, `assets/deck-framework.js`, and `decks/template-deck.html`, plus the original license. The template is renamed to `assets/template-deck.html.txt` for an inert download; its contents are unchanged. The VCC skill and project prompt adapt the workflow for portable folders, existing project authorization, privacy, and honest verification, under the same MIT terms. The original copyright and full MIT notice remain in the skill, agent export, and downloadable folder. The WebDecks repository remains the maintained source for framework changes. The VCC concept sketch is original educational artwork under CC BY 4.0. Linked example decks and remote font files are not bundled.
