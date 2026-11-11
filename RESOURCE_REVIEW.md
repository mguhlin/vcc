# Supplemental resource review

## Current shelf

The homepage keeps unslop, UI UX Pro Max, Design Bites, axe-core, and Playwright. Gitleaks, ZAP, and Accessibility Insights for Web add focused security and accessible-interface tools that are not named in `WEB_DESIGN.md`, `securevcc/securevcc.md`, or `EDU_COMPLIANCE.md`. They are optional external resources; their software and instructions are not bundled or automatically applied.

UI UX Pro Max, Design Bites, and axe-core are already referenced in `WEB_DESIGN.md`. Unslop and Playwright are also optional resources not named in the three instruction files. The core files cover relevant practices; a tool's absence does not mean the topic is missing.

MarkItDown, Spec Kit, and Cloudflare's security-audit-skill have been removed from the homepage shelf. Cloudflare remains credited as a source of SecureVCC. Their original review entries are retained below as context.

## Review scope

The original supplied AI_Git_Hub.csv contained 16 bookmarks: thirteen GitHub repositories, one GitHub gist, and two project-directory pages. Five additional primary repositories were examined for the original design, security, and testing shelf. The three optional additions below were examined against their primary repositories and official documentation.

Repository identity, README, license signals, archive status, intended role, and setup limits inform these selections. Revision links identify inspected source without maintenance timestamps. Metadata and documentation are not an execution audit, proof of security, or classroom approval. Third-party assets and dependencies may have separate terms. Read current upstream terms before installation.

## heydamir/unslop

**Decision:** Recommended. **Source:** supplied bookmark export.

Polish a website after its purpose and structure are clear.

**License signal:** CC-BY-4.0. **Archive status:** not archived in inspected metadata.

**Use limits:** A focused design-refinement skill; requires an agent and optional browser/image tools. Inspect scripts before use; generated images may incur service costs. Retain attribution.

**Evidence:** [repository and README](https://github.com/heydamir/unslop/tree/97daa3eb365670ea3f87ed85356cbfcee18105a5) · [license and file tree](https://github.com/heydamir/unslop).

## alvinreal/awesome-opensource-ai

**Decision:** Discovery only. **Source:** supplied bookmark export.

Find broader AI projects for further investigation.

**License signal:** CC0-1.0. **Archive status:** not archived in inspected metadata.

**Use limits:** A directory, not a vetted installation set. Its CC0 license does not cover the software, model weights, or datasets it links to.

**Evidence:** [repository and README](https://github.com/alvinreal/awesome-opensource-ai/tree/51a67d5a8b432f04837262b02b280fc2852979a3) · [license and file tree](https://github.com/alvinreal/awesome-opensource-ai).

## everywall/ladder

**Decision:** Not on the starter shelf. **Source:** supplied bookmark export.

A self-hosted page proxy is outside VCC’s core website-building workflow.

**License signal:** GPL-3.0. **Archive status:** not archived in inspected metadata.

**Use limits:** Its README warns about public proxy abuse and documents optional Basic Auth and allowlists. Review access, upstream terms, and deployment exposure before any use. GPL obligations matter if redistributing.

**Evidence:** [repository and README](https://github.com/everywall/ladder/tree/d8f8ce46bee7a24adbe75b0ec97e60b1e44c09f7) · [license and file tree](https://github.com/everywall/ladder).

## elirantutia/vibeyard

**Decision:** Advanced option. **Source:** supplied bookmark export.

A desktop workspace for people already using coding-agent CLIs.

**License signal:** MIT. **Archive status:** not archived in inspected metadata.

**Use limits:** Requires a supported authenticated coding CLI. Treat terminal access, repository access, credentials, and session telemetry as privileged; provider terms and costs still apply.

**Evidence:** [repository and README](https://github.com/elirantutia/vibeyard/tree/d8689347a9579ebedb25c014bd81138d3090cb4b) · [license and file tree](https://github.com/elirantutia/vibeyard).

## microsoft/markitdown

**Decision:** Background reference; removed from the homepage shelf. **Source:** supplied bookmark export.

Convert your own lesson notes and office documents into Markdown for a project.

**License signal:** MIT. **Archive status:** not archived in inspected metadata.

**Use limits:** Local conversion is useful, but optional AI or document services can send content elsewhere. Review enabled plugins and input rights; the process can access files and URLs with its current privileges.

**Evidence:** [repository and README](https://github.com/microsoft/markitdown/tree/ed178952a6672abdfd35b5f9e76a80b6cefc086e) · [license and file tree](https://github.com/microsoft/markitdown).

## tsevis/crawl4ai-ui

**Decision:** Advanced option. **Source:** supplied bookmark export.

Collect public web references as Markdown with a local Streamlit interface.

**License signal:** MIT. **Archive status:** not archived in inspected metadata.

**Use limits:** Requires Python and browser/crawler dependencies. Limit crawl scope, honor source terms, and do not crawl private school systems or expose a local crawler publicly without review.

**Evidence:** [repository and README](https://github.com/tsevis/crawl4ai-ui/tree/d11737b1f1b480e00ff71eb426df916ce718e3b2) · [license and file tree](https://github.com/tsevis/crawl4ai-ui).

## virgiliojr94/book-to-skill

**Decision:** Conditional reference. **Source:** supplied bookmark export.

Turn your own or appropriately licensed reference materials into an agent skill.

**License signal:** MIT. **Archive status:** not archived in inspected metadata.

**Use limits:** The extractor can run locally, but text supplied to a cloud agent follows that provider’s terms. Do not redistribute copyrighted books or assume a generated skill is factually reliable.

**Evidence:** [repository and README](https://github.com/virgiliojr94/book-to-skill/tree/e7bb659d3261491c8b28793dcb9102fa64a46c22) · [license and file tree](https://github.com/virgiliojr94/book-to-skill).

## multica-ai/andrej-karpathy-skills

**Decision:** Reference only; license needs confirmation. **Source:** supplied bookmark export.

Plain-language coding discipline: state assumptions, keep changes focused, and verify outcomes.

**License signal:** Not identified in GitHub metadata. **Archive status:** not archived in inspected metadata.

**Use limits:** The README says MIT, but GitHub metadata did not identify a license. Read as guidance; confirm an actual license notice before copying or bundling. No code is included in VCC.

**Evidence:** [repository and README](https://github.com/multica-ai/andrej-karpathy-skills/tree/2c606141936f1eeef17fa3043a72095b4765b9c2) · [license and file tree](https://github.com/multica-ai/andrej-karpathy-skills).

## anthropics/claude-for-legal

**Decision:** Specialist review only. **Source:** supplied bookmark export.

Legal-workflow reference plugins, potentially relevant to institutional reviewers.

**License signal:** Apache-2.0. **Archive status:** not archived in inspected metadata.

**Use limits:** Not a substitute for counsel or school sign-off. Plugins and data connectors may access confidential material; confirm permissions, provider terms, and professional review before use.

**Evidence:** [repository and README](https://github.com/anthropics/claude-for-legal/tree/4a6c651889c97cc9140580363c73e0eb17379c2b) · [license and file tree](https://github.com/anthropics/claude-for-legal).

## github/spec-kit

**Decision:** Background reference; removed from the homepage shelf. **Source:** supplied bookmark export.

Write testable requirements and implementation plans before a larger build.

**License signal:** MIT. **Archive status:** not archived in inspected metadata.

**Use limits:** Requires a coding-agent workflow and developer setup, including Python/uv in the documented CLI path. Review templates and extensions before running; a specification is not a successful test.

**Evidence:** [repository and README](https://github.com/github/spec-kit/tree/142089067d5a66974cb215fe964c37d643020db5) · [license and file tree](https://github.com/github/spec-kit).

## NVIDIA/personaplex

**Decision:** Outside current scope. **Source:** supplied bookmark export.

A speech-to-speech research system rather than an educator website design resource.

**License signal:** MIT. **Archive status:** not archived in inspected metadata.

**Use limits:** The code is MIT, but model weights use a separate NVIDIA license. Hardware requirements and voice-data handling need a separate evaluation before any student use.

**Evidence:** [repository and README](https://github.com/NVIDIA/personaplex/tree/16419a2ef7b98611f58c9df07477d00e5ad61d5f) · [license and file tree](https://github.com/NVIDIA/personaplex).

## tirth8205/code-review-graph

**Decision:** Advanced option. **Source:** supplied bookmark export.

Provide a coding assistant with a local graph of a larger codebase.

**License signal:** MIT. **Archive status:** not archived in inspected metadata.

**Use limits:** Its installer writes MCP configuration, hooks, skills, and project instructions. The graph is local, but a connected cloud coding assistant may transmit selected code. Inspect installation changes and keep private data out.

**Evidence:** [repository and README](https://github.com/tirth8205/code-review-graph/tree/29d8bd94312a02dc85b2f4e3e6c97ebe7e768fb8) · [license and file tree](https://github.com/tirth8205/code-review-graph).

## milla-jovovich/mempalace (now MemPalace/mempalace)

**Decision:** Advanced option. **Source:** supplied bookmark export.

A memory system for sustained coding work, rather than a starter requirement.

**License signal:** MIT. **Archive status:** not archived in inspected metadata.

**Use limits:** Persistent conversation and project memory create retention and deletion questions. Review backend selection, sharing mode, installation changes, and what a connected agent receives. Do not store student records by default.

**Evidence:** [repository and README](https://github.com/milla-jovovich/mempalace/tree/927d467d72764ced1f2be900b95cbc7dae4b4581) · [license and file tree](https://github.com/milla-jovovich/mempalace).

## cloudflare/security-audit-skill

**Decision:** Background reference; removed from the homepage shelf. **Source:** additional primary reference.

Primary security-audit methodology behind SecureVCC.

**License signal:** MIT. **Archive status:** not archived in inspected metadata.

**Use limits:** A developer-facing agent skill with a multi-phase workflow. Define authorization and use synthetic tests; reading the instructions does not verify your application.

**Evidence:** [repository and README](https://github.com/cloudflare/security-audit-skill/tree/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8) · [license and file tree](https://github.com/cloudflare/security-audit-skill).

## nextlevelbuilder/ui-ux-pro-max-skill

**Decision:** Recommended. **Source:** additional primary reference.

Explore design systems, typography, and patterns that fit your users’ task.

**License signal:** MIT. **Archive status:** not archived in inspected metadata.

**Use limits:** Optional CLI and search scripts require developer setup. Treat generated suggestions as candidates to test, and review the rights of any fonts, icons, or other assets separately.

**Evidence:** [repository and README](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/6ae86f61f520d6ca229d2f40e070410638c908c5) · [license and file tree](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill).

## educlopez/design-bites

**Decision:** Recommended. **Source:** additional primary reference.

Read DESIGN.md examples to discuss visual principles with an assistant.

**License signal:** MIT. **Archive status:** not archived in inspected metadata.

**Use limits:** Use as reference, not a brand-cloning template. Its CLI documents an install telemetry ping and an opt-out; reading files directly avoids requiring that CLI. Site brands and images retain separate rights.

**Evidence:** [repository and README](https://github.com/educlopez/design-bites/tree/575bcf9887dbd9c4222db9e0335ed2f63d78521a) · [license and file tree](https://github.com/educlopez/design-bites).

## dequelabs/axe-core

**Decision:** Recommended. **Source:** additional primary reference.

Find automated accessibility issues in the actual rendered page.

**License signal:** MPL-2.0. **Archive status:** not archived in inspected metadata.

**Use limits:** MPL-2.0. Automation detects a subset of barriers; incomplete results and keyboard, screen reader, content, and journey checks need human review.

**Evidence:** [repository and README](https://github.com/dequelabs/axe-core/tree/c50bf8e8933eba8cdb7a0d8e744a6c0ec691cdd6) · [license and file tree](https://github.com/dequelabs/axe-core).

## microsoft/playwright

**Decision:** Recommended. **Source:** additional primary reference.

Make main-journey browser checks repeatable.

**License signal:** Apache-2.0. **Archive status:** not archived in inspected metadata.

**Use limits:** Requires developer setup and browser binaries. Use invented data, protect saved authentication state, and keep external email, payments, or destructive actions sandboxed.

**Evidence:** [repository and README](https://github.com/microsoft/playwright/tree/62e11d73d23ba19fc6747fa73f4f2f0f05d79183) · [license and file tree](https://github.com/microsoft/playwright).

## Karpathy gist

**Source:** supplied export. **Decision:** unverified primary content; not recommended as an installable component.

[Original gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). The direct GitHub API request returned a server error, so content, license, and applicability were not established. This is a gist rather than a repository. Do not assume that publicly readable text has a redistribution license. The separately inspected multica-ai repository is not treated as a substitute verification of the gist.

## Project-directory link: missing project

**Source:** supplied export. **Decision:** excluded; no usable primary project established.

[Directory page](https://www.opensourceprojects.dev/post/1995746679228957071) returned a “Project Not Found” title with no substantive project description. No repository, license, or behavior was established.

## Project-directory link: ebook downloader

**Source:** supplied export. **Decision:** excluded from recommendations.

[Directory page](https://www.opensourceprojects.dev/post/73425c25-9968-46aa-8f02-29b2834e314c) describes an ebook downloader and links to jbiaojerry/ebook-treasure-chest. That primary repository and its licensing were not execution-audited or established by this directory-page review. Download rights, platform terms, and the narrow fit to VCC need separate investigation; the directory’s promotional claims are not evidence of authorization or safe operation.

## gitleaks/gitleaks

**Decision:** Optional addition to the homepage shelf. **Instruction-file coverage:** Not named in `WEB_DESIGN.md`, `securevcc/securevcc.md`, or `EDU_COMPLIANCE.md`; not included as software in the VCC bundle.

Search local files and Git history for possible exposed credentials. This provides a concrete tool for secret-review work described by the core guides.

**Use limits:** Use redacted output and keep reports private. Matches need review; a clean scan is not proof that no secrets exist. Upstream describes the project as feature complete with security-patch releases. Detection does not revoke a leaked credential.

**License signal:** MIT. **Archive status:** not archived in inspected metadata.

**Evidence:** [repository and README](https://github.com/gitleaks/gitleaks/tree/5f6ec56cfa6f8c67648d863582c7ae2f206d5c1c) · [license and file tree](https://github.com/gitleaks/gitleaks).

## zaproxy/zaproxy

**Decision:** Optional addition to the homepage shelf. **Instruction-file coverage:** Not named in `WEB_DESIGN.md`, `securevcc/securevcc.md`, or `EDU_COMPLIANCE.md`; not included as software in the VCC bundle.

Inspect a running web application's requests and potential security weaknesses during development.

**Use limits:** Use a disposable local or explicitly authorized staging target, synthetic data, and a tightly defined scope. Active tests can change state. Scanner alerts need validation and do not prove complete application security. See [ZAP scope guidance](https://www.zaproxy.org/docs/desktop/start/features/scope/).

**License signal:** Apache-2.0. **Archive status:** not archived in inspected metadata.

**Evidence:** [repository and README](https://github.com/zaproxy/zaproxy/tree/a1386d3e7bd9d1c7d2fb8d2eb6fee2ef855b728d) · [license and file tree](https://github.com/zaproxy/zaproxy).

## microsoft/accessibility-insights-web

**Decision:** Optional addition to the homepage shelf. **Instruction-file coverage:** Not named in `WEB_DESIGN.md`, `securevcc/securevcc.md`, or `EDU_COMPLIANCE.md`; not included as software in the VCC bundle.

Add guided keyboard and manual accessibility checks to automated interface testing using its browser extension.

**Use limits:** Review extension permissions and telemetry settings before inspecting private school pages. The published assessment overview targets WCAG 2.1 AA; assess additional WCAG 2.2 requirements separately. Neither a scan nor the extension establishes full conformance. See [the official overview](https://accessibilityinsights.io/docs/web/overview/).

**License signal:** MIT. **Archive status:** not archived in inspected metadata.

**Evidence:** [repository and README](https://github.com/microsoft/accessibility-insights-web/tree/97ad835b33c8c15553c238da28aa3f614f12f287) · [license and file tree](https://github.com/microsoft/accessibility-insights-web).

## Before trying any linked tool

Read the current primary repository, its license, installation scripts, configuration changes, and data destinations. Choose only the tool your project needs. Pin a reviewed version, use invented data, and obtain authorization for external services or live testing. Keep credentials, private school documents, and student information out of public repositories and generated issue reports.
