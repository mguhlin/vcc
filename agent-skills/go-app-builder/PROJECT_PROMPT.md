# Start a Go App Builder project

Read and apply [Go App Builder](SKILL.md). If working in an ordinary chatbot, use the [maintained skill](https://mguhlin.github.io/vcc/skills/go-app-builder/SKILL.md) plus the relevant linked references, or attach this complete folder. No installation is required to use the instructions.

Use the following brief immediately. Fill in what the conversation or repository establishes; proceed with clearly stated low-risk assumptions for the rest rather than starting a long questionnaire.

```text
Use Go App Builder for this project.

Product / primary user task: infer from my request and current code.
Audience and operating context: infer known needs; mark unresolved accessibility,
localization, managed-device, memory and connectivity constraints.
Current code: inspect the provided repository/files; preserve working behavior,
formats, exports, translations and unrelated changes.
Mode: infer plan, build, port, review or release from my request.
Required platforms: Windows, macOS, Linux, Android and browser unless I narrow
that list. Inventory exact OS/CPU/runtime/ABI baselines; do not invent support.
Platform constraints: use existing stack/dependency rules and distribution channels.
Offline/local processing: default new builds to independent local/offline operation
unless requested features require a disclosed network/service route. Distinguish
processing, first launch, clean installation
and source build; make no stronger claim than the evidence supports.
Data and permissions: minimize collection and native authority; do not introduce
accounts, cloud services, AI, telemetry or legal pages without a product reason.
Publication: follow permission already established in our conversation/project;
the skill itself does not authorize publishing or production testing.

Start by inspecting instructions, source, current changes, build/package scripts,
modules and existing acceptance evidence. State the primary task and low-risk
assumptions, then make a compact platform/feature matrix. Explain what actually
shares Go, what shares formats/UI, and where another engine remains. Read only
relevant platform references. Resolve a small end-to-end adapter spike before a
large port or framework rewrite. Implement within the authorized mode.

Protect native capability provenance, including forged framework drop requests;
use native picker/reconfirmation where provenance cannot be established. Keep
imports bounded, preserve originals, invalidate stale callbacks on clear/cancel,
and report partial commits truthfully. Verify portable formats with golden and
cross-implementation fixtures. Design keyboard, touch, Back/close, large text,
high DPI, localization and assistive-technology routes for the essential task.

Use the four independent VCC evidence gates. Return actual changes or a concrete
plan/review, architecture decisions, feature matrix, tests and target evidence,
unknowns and a scoped release decision. Mark unavailable native/device checks
NOT_RUN. Trace tested through packaged/signed/extracted/installed/published
artifacts. Do not claim execution, offline readiness, legal conformance,
accessibility certification or store approval without the corresponding evidence.
```

Use [architecture](references/architecture.md) for contracts, [desktop](references/desktop.md), [Android](references/android.md) or [browser](references/browser.md) for adapters, and [validation/release](references/validation-release.md) for evidence. The [sources](references/sources.md) distinguish documented mechanisms from decisions still requiring project-specific verification.

Original educational prose by Miguel Guhlin for [VCC](https://mguhlin.github.io/vcc/), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Linked materials retain their own terms.
