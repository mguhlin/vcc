# Sources and editorial decisions

## Core components

- `securevcc/`: migrated from Miguel Guhlin’s `mguhlin/creations` SecureVCC folder. The original security guidance, source Markdown, upstream ZIP, license, and source notes are retained. Its local landing route now points to the VCC security guide.
- `WEB_DESIGN.md`: supplied by Miguel Guhlin. Its maintenance date was removed for publication; its operational guidance is retained.
- `EDU_COMPLIANCE.md`: supplied by Miguel Guhlin. Its maintenance-date frontmatter was removed for publication; its operational guidance is retained.
- The two explanatory images were supplied with those files. The hero was generated for VCC; see `assets/hero-prompt.txt`.
- Project brief, launch review, and prompt pack extend those guides into practical educator workflows.

## Blog context

Both local authoring files were read, including their publication metadata and article bodies:

- [Securing Your Vibe-Coded Creation](https://mguhlin.org/blog/2026-11-08-securing-your-vibe-coded-creation/): use a reusable security instruction file; the article links to SecureVCC and Cloudflare’s source skill.
- [Stop Letting AI Make Every Website Look the Same](https://mguhlin.org/blog/2026-11-10-stop-letting-ai-make-every-website-look-the-same/): match structure to function, provide design references, and build accessibility and privacy into the workflow. VCC links to the companion article from its supplemental blog page and does not reproduce the full essay.

The article names and dates in their URLs are stable content identifiers, not VCC maintenance timestamps.

## Illustrated walkthroughs

Miguel Guhlin supplied `cartoon_github.png`, `cartoon_netlify.png`, and `Vibe-Coding Center_ Three Essential Checks.png`. VCC preserves the originals in `assets/cartoons/` and uses WebP copies for page display. The classroom-sharing guide shows the Four Checks remake and links to the original Three Essential Checks cartoon; the publishing walkthroughs pair the other cartoons with text versions and current official GitHub Pages and Netlify documentation. Cloudflare is identified as optional, and the Netlify action links to the service's actual Drop page rather than relying on the address drawn in the cartoon.

## Supplemental resources

Miguel Guhlin supplied the [Vibe-Coded Apps Flipboard ezine](https://flipboard.com/@mguhlin/vibe-coded-apps-ai-free-dnmobc4ny) as an optional resource readers can follow for new apps, AI tools, and free resources. VCC links to the magazine and shows the supplied Flipboard cover screenshot on the homepage. The screenshot retains the photo credit shown by Flipboard. [Flipboard’s help center](https://flipboard.helpshift.com/hc/en/1-flipboard/faq/990-organize-my-top-home-carousel-1671584878/) documents the magazine follow control; subscription is managed on Flipboard.

The supplied `AI_Git_Hub.csv` contained 16 bookmarks. Tracking parameters and exported bookmark metadata are excluded from VCC’s public recommendations. Every bookmark has a decision in [RESOURCE_REVIEW.md](RESOURCE_REVIEW.md), with additional primary design and test references. The Helpful GitHubs shelf is narrower than that historical ledger; its optional additions are Gitleaks, ZAP, and Accessibility Insights for Web, each explicitly distinguished from references already named in the core instructions. Repository metadata and READMEs were read through GitHub; no recommended software was installed or executed for vetting.

## Official guidance consulted

These are reference points, not endorsements or compliance certifications. The full education guide has the broader source list. Recheck applicability and current text for each actual project.

- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/): testable accessibility criteria, with manual testing still necessary.
- [U.S. Department of Education: FERPA school-official exception](https://studentprivacy.ed.gov/faq/who-school-official-under-ferpa): outsourcing education-record services involves specific conditions, not a generic software approval.
- [FTC COPPA FAQs](https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions): follow the FTC’s linked revised Rule for current requirements. A school context does not remove all operator responsibilities.
- [Official GDPR text](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng): the primary legal source is linked, but automated retrieval encountered a browser verification challenge. VCC does not make a new legal interpretation from an unread page.

## Reusable skills

The seven supplied Markdown files are preserved under `skills/`. Two additional standalone adaptations—Compare Options and Source Integrity—come from explicit CC0-1.0 files read through GitHub in mguhlin/creations. Discovery also covered public mglearn repositories; no mglearn material is redistributed. [Detailed provenance](skills/SOURCES.md) records source links, blob identifiers, and adaptation boundaries. VCC's prompts and original vector concept sketches translate each workflow into a possible project; they do not claim that these applications have been built or evaluated.

## Rescue and security repair workflows

The creator-supplied `vibe-code-rescue-skill.zip` was inspected as a one-file Markdown archive. VCC adapts its broader setup/diagnostics/maintainability workflow into `rescue/VIBE_CODE_RESCUE.md` and integrates its security repair baseline into the maintained SecureVCC source. [Detailed provenance](rescue/SOURCES.md) records source hashes, supplied attribution, scope, and editorial changes. OWASP authorization and logging guidance and GitHub's sensitive-data removal guidance were read for technical support. The linked MakeUseOf article could not be retrieved; attribution is preserved as stated in the supplied skill without treating the article as independently verified evidence.

## Agent-facing installation and use directions

[Unslop's README](https://github.com/heydamir/unslop/blob/main/README.md), by Damir Sokolovsky, was read through GitHub for its explicit install/use pattern. VCC provides its own directions and source-derived exports; upstream installation commands and skill code are not redistributed. [OpenAI's skill documentation](https://developers.openai.com/codex/skills/) supports the local `.agents/skills` locations, `SKILL.md` metadata, explicit invocation, and discovery guidance. The local Codex CLI README was inspected first but did not document these skill locations. Guidance remains subject to the actual assistant and environment.

`AGENT_GUIDE.md` and per-page prompts distinguish skill creation, workflow use, and task authorization. The exported files preserve maintained source bodies and notices, with normalized frontmatter and a source/reuse footer. `llms.txt` is a convenient plain-text index, not a guarantee that every assistant reads it automatically.

## Modern Web Guidance in Web Design

The creator requested [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src) for the Web Design featured item. Its README and Apache-2.0 code license were read, alongside its documentation license statement: guide content under `guides/` is CC BY 4.0. VCC paraphrases selected guidance and links the source; no executable code, demos, evaluation harness, or CLI is redistributed or executed.

Focused guide files read through GitHub:

- [Responsive design](https://github.com/GoogleChrome/modern-web-guidance-src/blob/main/guides/css/responsive-design/guide.md), source blob `7d4cb98c6e06740d34b6620142583fe167e54e69`.
- [Dialog](https://github.com/GoogleChrome/modern-web-guidance-src/blob/main/guides/ui-components/dialog/guide.md), source blob `30828a93d61a14f2c496faee2706bbe0a65dbbcf`.
- [Optimize image priority](https://github.com/GoogleChrome/modern-web-guidance-src/blob/main/guides/performance/optimize-image-priority/guide.md), source blob `7baed769516fa8d49393d615f8e7e6917f211024`.
- [Respect OS text scale](https://github.com/GoogleChrome/modern-web-guidance-src/blob/main/guides/accessibility/respect-os-text-scale/guide.md), source blob `efd816d6593151836f565b346352fd91a6d8bfcc`.

The [official overview](https://developer.chrome.com/docs/modern-web-guidance) and [modernization workflow](https://developer.chrome.com/docs/modern-web-guidance/modernization-workflow) were also read. VCC adapts their selection/verification approach without copying code, volatile feature counts, vendor evaluation results, or installation requirements. It qualifies browser availability, treats OS text-scale and other newer features as conditional, and preserves existing fallback behavior. CLI telemetry is described in the upstream README; the VCC site makes no calls to that CLI or its telemetry endpoints.

Fourteen additional creator adaptations expand the reusable collection to 23 workflows. They draw on supplied instructional specifications, the daily calendar and Vimeo workflow files, and a narrowly scoped MIT text/file-hygiene adaptation from the supplied archive. Each has a new title, authored project prompt, and generated hero illustration. [Skill provenance](skills/SOURCES.md) identifies the adaptations, retained attribution, source hashes, missing knowledge files, and excluded service dependencies. Hero prompts are preserved in `assets/skills/heroes/PROMPTS.json`.
