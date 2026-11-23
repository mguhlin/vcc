---
name: go-app-builder
description: Plan, build, port, review, or prepare releases of shared Go applications for Windows, macOS, Linux, Android, and browsers, with explicit platform adapters, interoperability, accessible tasks, security boundaries, and target-specific evidence.
---

# Go App Builder

Build the smallest maintainable solution that completes the user's task on its declared platforms. Share domain behavior deliberately; prove platform integration separately. A Go binary, native window, browser app, offline package, and trusted release are different deliverables.

This is standalone guidance for coding agents and ordinary chatbots. Read this file, then only the references needed for the job. No installation, companion skill, paid service, or particular tool is required. Without repository or execution access, produce a concrete design, patch proposal, or review with unknowns marked; never imply that proposed work ran.

Maintained entry point: [VCC Go App Builder](https://mguhlin.github.io/vcc/skills/go-app-builder/SKILL.md). Relative references work in the complete folder. If unavailable, fetch the matching file beneath `https://mguhlin.github.io/vcc/skills/go-app-builder/`, download [the complete skill folder](https://mguhlin.github.io/vcc/downloads/go-app-builder.zip), or obtain [the complete VCC bundle](https://mguhlin.github.io/vcc/downloads/vcc-complete.zip) and open `skills/go-app-builder/`. Ask for only a missing reference that materially blocks the task. [PROJECT_PROMPT.md](PROJECT_PROMPT.md) supplies an immediate project brief.

## Use with an AI agent

Give the assistant the [agent-ready file](https://mguhlin.github.io/vcc/agent-skills/go-app-builder/SKILL.md) or this source plus relevant references. For optional setup, say: “Save the complete Go App Builder folder in this agent’s supported project skill location; preserve references and metadata.” For immediate use, say: “Read Go App Builder and use it to plan/build/port/review my application; inspect the current code and report platform evidence.” Use [PROJECT_PROMPT.md](PROJECT_PROMPT.md) for the fuller brief. Reading or applying the skill needs no installer.

## Select the authorized job

Infer the mode from the request: **plan** produces decisions and acceptance criteria; **build** implements a requested solution; **port** preserves existing behavior through new adapters; **review** reports findings without silently changing code; **release** qualifies and packages a stated candidate. Combine modes only when authorized. Preserve prior permission for routine development, commits, publication, or deployment; this skill supplies no universal publication grant. A readiness verdict does not create one.

Inspect project instructions, the current diff, README, entry points, module/workspace files, frontend locks, build tags, native dependencies, packaging and CI before edits or execution. Discover nested modules. Preserve unrelated work, supported formats, accessibility routes, translations, exports, and working workflows. Characterize one known-good task and the requested failure or change. A source commit does not back up persisted user data; establish appropriate recovery before a risky migration.

Proceed with stated, low-risk assumptions when facts are absent. Ask only for decisions that block dependent work or materially affect cost, privacy, destructive behavior, or release identity. Inspect scripts before running them. Use synthetic fixtures and authorized environments; isolate untrusted code from host credentials and production connections. Existing development permission does not authorize production probing, credential rotation, messages, purchases, or unrelated infrastructure changes.

## Define the product and platform contract

Record the primary task, audience, current code, required targets, offline meaning, data sensitivity, accessibility/localization needs, allowed dependencies, and acceptance criteria. For a new build, default to independent local/offline processing unless the user requests network/service features; a first hosted browser visit still requires asset delivery. Do not expand a local utility into SaaS, accounts, AI, telemetry, or legal pages without a product requirement.

Create a compact feature matrix: feature/task; input/output semantics; target adapter; native permission/runtime; fallback; limits; cancellation/recovery; evidence. Mark `SUPPORTED`, `DEGRADED`, `UNSUPPORTED`, or `UNKNOWN` separately from test results. Compare successful outcomes, not similarly named buttons. Record exact OS/architecture/minimum OS and runtime coordinates; Android SDK/ABI and Linux libc/GUI ABI need their own fields. A cross-build is not physical-device qualification.

Use [architecture.md](references/architecture.md) for decision records, portable format contracts, and a minimal application manifest. Keep these records small enough to maintain with the implementation.

## Choose what actually shares

Prefer a UI-independent Go core for validation, transformations, and stable format semantics, with adapters for files, permissions, storage, clipboard, printing, navigation, lifecycle and UI. Core APIs take bounded bytes/streams or already-authorized resources, not renderer paths or framework windows. Give asynchronous operations stable IDs, typed errors, progress and cancellation semantics.

Evaluate alternatives against the existing product. A desktop webview can reuse a proven web interface; a native Go toolkit can suit a simpler task; native Android UI can call a narrow Go AAR facade; a browser wrapper can run the core as `js/wasm`. Fyne, Gio, Wails, and native hosts have different native dependencies and accessibility behavior. Verify exact pinned-release capabilities through primary documentation and a small end-to-end spike before committing to a stack.

Do not repeat obsolete blanket framework assumptions: official Wails guidance distinguishes stable v3 desktop from experimental mobile. Recheck the selected version's compatibility contract, SDK and GUI requirements. Experimental Android support does not imply desktop dialog, window or filesystem parity. Toolkit documentation is evidence of a supported route, not proof that this application's dependencies or essential task work.

Preserve a mature JavaScript, WASM, or bundled interpreter engine when replacement would sacrifice compatibility. State honestly whether Go performs the processing, hosts another engine, or shares only a format contract. Separate implementations need independent interoperability and security evidence. Pin bundled snapshots/components with source revisions and hashes; avoid runtime executable downloads or dependence on another checkout. Include their maintenance and redistribution obligations.

## Preserve portable data semantics

Specify format versions, encodings, byte order, numeric ranges, timestamps/time zones, null/empty distinctions, ordering, path/name rules, and migration/rejection behavior. JavaScript number precision, Unicode normalization, filesystem case collisions, reserved names, and differing newline conventions can break apparently successful ports. Preserve original bytes when the contract requires it; do not normalize silently.

Keep golden fixtures and cross-implementation round trips in both directions. Include empty/binary input, non-ASCII and combining characters, boundary numbers, timestamp offsets, malformed/truncated input, duplicate names and unsupported versions. Randomized output should be compared by verified decoded semantics, not ordinary byte equality.

Only introduce cryptography when required. Define authenticated metadata, algorithm/KDF identifiers and units, nonce rules, chunk finalization and accepted resource profiles. Bound hostile KDF parameters before work; benchmark accepted profiles on the weakest supported device. Use known-answer and independent cross-implementation fixtures. Do not invent algorithms, silently reduce protection, or describe successful round trips as a cryptographic audit.

## Keep native authority outside the renderer

Treat imported content, JavaScript, bridge calls, messages, CLI/config input, and framework event payloads as untrusted at their authority boundary. Enforce action-specific rights where reads, writes, deletes, execution or network transfers actually occur. Avoid generic privileged `ReadFile(path)` or `Run(command)` bindings.

Native-issued capabilities must derive from a verified OS-selected resource. Bind them to resource, permitted operation, window/session, generation, lifetime and consumption/replay policy; revoke on reset, cancel and close. A token scoped correctly can still launder an attacker-chosen path if its issuer trusts a forged event.

**Test forged framework drop events as well as arbitrary direct bridge arguments.** Trace OS interaction through framework dispatch, public runtime methods, message buses and backend handlers. A callback named “native drop,” a nonce, hidden endpoint, or frontend `isTrusted` check does not establish provenance. If renderer code can supply paths that become native authority, require trustworthy backend registration or native picker/reconfirmation. Leave unverifiable provenance unresolved; disabling privileged drop while retaining a picker is a valid fallback.

Confinement and authorization are independent. Use appropriate root-relative filesystem APIs and test their documented platform limits; cleaning a path, prefix checking or checking symlinks before opening is insufficient against all races. Reject or model symlinks/hardlinks, traversal, device entries, duplicates and portable-name collisions. Restore hostile archives into newly reserved output, not an existing user tree.

Stage writes privately, check write/flush/close errors and recheck authority at commit. Use an OS/provider-specific replacement policy. Go `Rename` is not universally atomic, a sequence of replacements is not a directory transaction, and provider streams need their own partial-write recovery. State actual overwrite, metadata and durability guarantees rather than promising them globally.

## Make lifecycle and resource limits observable

Model selection, validation, running, staging, commit, cancellation, failure and recovery explicitly enough to explain the workflow. Bind callbacks and results to operation ID and workspace generation. Validate into a bounded candidate before replacing current work. Reset invalidates asynchronous work and capabilities before clearing app-owned copies. Reject late picker, worker, save and announcement callbacks; race-free memory alone does not prevent stale logical results.

Cancellation must reach readers, processing loops, native jobs and helpers where supported. Distinguish cancelled-before-commit, already-completed effects, partial output, and unknown outcome after timeout. Reconcile an ambiguous commit before retrying; do not duplicate consequential work. Preserve valid originals and offer bounded recovery.

Keep expensive processing off the required UI thread. Bound actual bytes read, decoded/expanded bytes, entries, nesting, numeric parameters, active sessions, concurrent jobs, total work and retained results. Measure peak copies across Go/JS/FFI/base64, not only nominal file size. Streaming compilation or an API named stream does not prove bounded application memory.

For bundled subprocesses, use trusted absolute executables, bounded handshakes, one shutdown owner and one wait owner. Design startup failure, crash, parent death, descendants, pipes and cancellation per OS. `CommandContext`/`Process.Kill` do not guarantee process-tree termination. A loopback service still needs appropriate peer/origin and per-session authority checks; prefer simpler IPC when it reduces exposure.

Map input through processing, storage, derived copies, recipients, deletion and restore. Include history, previews, logs, caches, exports, clipboard and OS backups. Use safe rendering, constrained previews, minimal permissions and redacted bounded diagnostics. Clear only app-owned data and report cleanup failures. Neither managed-memory cleanup nor file overwrite proves forensic zeroization; downloaded, synchronized and recipient copies have independent lifecycles.

## Design the task for each platform

Choose screen structure from the task: workspace, document flow, search, or focused operation. Preserve the established identity; do not add marketing decoration to an application. Use consistent controls, plain language and truthful empty/loading/error/completion states. Errors say what happened, whether work was saved and what to do next.

An essential task needs keyboard access, visible/logical focus, discernible labels, touch alternatives to dragging, predictable dialog dismissal and focus return. Test platform Back/close and unsaved-work behavior, large text, high DPI, resize/orientation, long translations, input methods, contrast and reduced motion. Keep progress announcements useful and free of private content. Verify print/export independently when promised.

Use semantic DOM controls for web interfaces where suitable; evaluate native toolkit semantics with actual assistive technology. Automated scans and screenshots do not establish accessibility conformance. WCAG is a web engineering reference; CSS pixel thresholds are not Android dp rules or blanket native-toolkit certification. Record the actual accessibility target and applicable institutional/legal questions separately.

## Apply platform-specific delivery rules

Read only the relevant platform references before implementing or qualifying those adapters:

- [desktop.md](references/desktop.md): native capabilities and child engines; Windows WebView2 full offline installer versus bootstrapper; macOS signing/notarization and extracted bundles; Linux GUI/libc dependencies and packaging.
- [android.md](references/android.md): Go AAR/native alternatives versus PWA; SAF URI capabilities, lifecycle/background rules, backup/Keystore, ABI/page-size and signed APK/AAB verification.
- [browser.md](references/browser.md): matching Go wasm runtime, file fallbacks, workers, secure contexts, cache/update lifecycle, CSP/CORS, sandboxing and remote-server disclosures.

Distinguish offline processing, first launch, clean installation and source build. Test each claim separately with its required caches/runtimes absent or provisioned. A PWA icon, a desktop archive or a dependency declaration does not prove offline readiness. Never substitute a remote server for local Go execution without explaining what leaves the device and obtaining authorization for the changed data flow.

## Pass four independent evidence gates

Use these distilled VCC controls even when the full guides are unavailable. Read the optional full guides for deeper relevant work, and claim only files actually read.

| Gate | Evidence needed for the stated use |
| --- | --- |
| Task/design/accessibility | Essential UI journey, failure recovery, keyboard/touch/text scaling and named assistive-technology coverage or explicit gaps. |
| Privacy/education applicability | Actual fields, recipients, storage, backup, clear/restore and observed transfers; contextual legal/institutional decisions only where triggered. |
| Security boundaries | Allowed and denied operations, trustworthy capability issuance, safe imports/rendering and lifecycle checks; protected state remains unchanged on rejection. |
| Recoverable delivery | Reproducible setup, meaningful diagnostics including logging failure, recovery, nearby regressions and identified packaged/installed artifact. |

A strong result in one gate cannot compensate for another gate's failure or missing evidence. [validation-release.md](references/validation-release.md) links the full VCC guides and supplies compact schemas, test methods and release criteria.

## Verify and hand over honestly

Pin reviewed toolchains, Go/native/frontend dependencies and build configuration. Select available, authorized tests, static analysis, vulnerability checks, race and bounded fuzz runs for actual modules and supported targets. Inspect network/install side effects first. A command from one module or host cannot establish every platform branch, FFI integration or device outcome.

Record `PASS`, `FAIL`, `NOT_RUN`, or `NA` with target, revision/artifact, method, evidence and limits. Separate source review, synthetic tests, automated UI, real native gestures, assistive technology, clean install/offline and live deployment. Mark unavailable devices and unresolved applicability honestly. Tool success is neither legal approval nor proof of complete security.

Track identity from source/build inputs through tested binary/assets, packaging, signing, extracted contents, installation and published download. Transformations change bytes: link input/output hashes and publisher evidence. Verify final hashes, licenses/notices, SBOM/provenance or explicit absences. Signing, notarization and checksums provide different evidence. Keep signing keys private; clearly constrain unsigned prereleases and never advise disabling OS protections globally.

Return implemented changes or a concrete plan/review, architecture reasons, feature matrix, four gate outcomes, checks run, unresolved decisions and a scoped `GO`, `CONDITIONAL`, or `NO_GO`. Block affected use for critical boundary failures, essential-task data loss, severe inaccessible required tasks or unsupported material claims. Continue safe prototype work where possible. Publish only within existing authorization and verify the actual live artifact when publication is in scope.

## Sources and reuse

Original educational prose by **Miguel Guhlin**, published through [VCC](https://mguhlin.github.io/vcc/), licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Preserve attribution, license link and indication of changes when adapting. Linked upstream software, documentation and standards retain their own terms; this license grants no additional software rights. [sources.md](references/sources.md) maps primary evidence and revalidation needs. This guidance provides engineering decisions and verification methods, not security, accessibility, legal or store certification.
