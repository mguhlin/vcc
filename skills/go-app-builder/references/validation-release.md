# Validation, four gates, and release evidence

Use this reference for acceptance design, a review, or release qualification. Keep controls proportional to actual exposure. These are proposed evidence structures, not a certification scheme or assertions that checks have run.

## Preserve four independent VCC checks

The core skill distills four complementary VCC workflows. Their full files are optional depth: [function-first design](https://mguhlin.github.io/vcc/WEB_DESIGN.md), [education/privacy applicability](https://mguhlin.github.io/vcc/EDU_COMPLIANCE.md), [security](https://mguhlin.github.io/vcc/securevcc/securevcc.md), and [rescue/delivery](https://mguhlin.github.io/vcc/rescue/VIBE_CODE_RESCUE.md). Read the relevant file before claiming it was applied. Do not require another skill or installation merely to use these controls.

| Independent gate | Establish | Decisive evidence / limits |
| --- | --- | --- |
| Task/design/accessibility | The declared audience can complete the essential task and recover from failure. | Actual UI journey; keyboard, touch, focus, text scale, localization, exports and named assistive-technology coverage. A screenshot or automated score cannot substitute. |
| Privacy/education applicability | Actual fields, recipients, retention and authority match the proposed use. | Data-flow inventory plus source and observed storage/network/export/clear/restore behavior. School, age, jurisdiction and contract decisions need appropriate responsible review when triggered. |
| Security boundaries | Lower-trust input cannot exercise unauthorized resource operations. | Allowed and denied cases at final authority, including capability issuance/provenance, stale work, safe parsing/rendering and protected state before/after. Framework labels and scanner counts are insufficient. |
| Recoverable delivery | Another maintainer can recreate, diagnose, recover and ship the actual product. | Clean setup/install; representative operational and logging failures; restoration/nearby regression; traceable artifact identity. Developer launch and source commits alone do not establish data recovery. |

Give each gate its own result. A perfect design cannot compensate for an unsafe bridge; signing cannot compensate for lost work; an institutional agreement cannot establish software behavior. `NA` needs architectural evidence, not an assumption that missing information means no risk. Do not add enterprise services, remote logging, legal pages or authentication solely to populate a checklist.

## Choose meaningful checks within available tools and permissions

Inspect project-controlled commands, setup hooks and network/install effects first. Use existing authorized workflows, synthetic fixtures and isolated environments appropriate to the trust level. Do not silently install scanners or execute downloaded scripts. Include nested Go modules, frontend and native dependencies, generators and build-tag configurations; `./...` from one module is not complete project coverage.

Possible Go checks, selected rather than blindly run, include ordinary tests, vet, supported race-instrumented tests, targeted bounded fuzzing, vulnerability analysis and binary build-info inspection:

```sh
go test ./...
go vet ./...
go test -race ./...
go test -fuzz=FuzzParser -fuzztime=30s ./specific/package
govulncheck ./...
go version -m path/to/binary
```

These are examples, not executed results or a guaranteed portable command suite. Select a real existing fuzz target and scratch-only outputs; use tiny boundary fixtures, never destructive bombs. Race detection covers executed paths and has platform/toolchain requirements. Fuzz seed tests and bounded campaigns need deterministic state and bounded resource use. `govulncheck` coverage depends on source/binary mode and build configuration and normally uses an external vulnerability database. Record its settings/network behavior. ([Race detector](https://go.dev/doc/articles/race_detector), [Go fuzzing](https://go.dev/doc/security/fuzz/), [govulncheck](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck))

Pin reviewed toolchains and dependency locks, examine authoritative advisories and update deliberately. `go mod verify` checks cached module content against cached hashes; it is not vulnerability or behavioral validation. Go toolchain auto-selection can download another toolchain. Source pinning is different from an offline/reproducible build proof. Embedded build metadata aids identification, not publisher authentication. ([Modules](https://go.dev/ref/mod), [toolchain selection](https://go.dev/doc/toolchain), [build information](https://pkg.go.dev/runtime/debug#ReadBuildInfo))

Test invariants rather than mirroring implementation: valid/invalid imports preserve state; byte-exact or specified semantic round trips; rejection preserves outside-tree files; native capabilities cannot be minted through forged framework drops; reset/cancel cannot revive old work; write failure preserves originals; timeout-after-commit reconciles; helper shutdown leaves no unintended descendants; limits reject before expensive allocation. Retain legitimate workflows beside negative cases.

## Keep evidence types separate

| Kind | What it can establish | What remains separate |
| --- | --- | --- |
| `SOURCE_REVIEW` | Reachable implementation/configuration properties | Actual runtime attachment, gestures and deployment |
| `SYNTHETIC_UNIT` | Pure logic, validators and in-process invariants | Native mediation, framework transport, provider behavior |
| `SYNTHETIC_INTEGRATION` | Controlled app/bridge/worker and reordered callbacks | Actual OS drops, providers, real service policy |
| `AUTOMATED_UI` | Named driver/engine UI behavior and layout | Native dialogs and human assistive-technology experience |
| `NATIVE_GESTURE` | Actual picker/drop/save/share/Back path on installed target | Other OS/device/runtime combinations |
| `ASSISTIVE_TECH` | Named technology completing the selected task | Untested tasks/technologies and full conformance |
| `CLEAN_INSTALL_OFFLINE` | Intended artifact works without developer state/network under stated prerequisites | Offline source build, other targets and optional online paths |
| `LIVE_DEPLOYMENT` | Actual hosted/downloaded identity and meaningful changed behavior | Complete security or unrelated production operations |

Record result, revision/artifact, exact OS/CPU/runtime/ABI, method, expected versus observed outcome, evidence location and limitations. Use `PASS`, `FAIL`, `NOT_RUN`, `NA`; use a separate confidence label for findings such as confirmed, needs validation, design observation or rejected. Do not downgrade an unverified serious hypothesis into a confirmed minor issue. Distinguish a source-confirmed design property from an executed-test failure: a supplied description alone is unverified, inspection can confirm the source property, and runtime consequences need their own evidence. Prioritize critical boundary blockers, then essential-task qualification, then additional target expansion.

Real native acceptance includes arbitrary-path rejection, forged framework requests, actual external drop, picker cancel, source replacement, denied write, disk full, close/restart and save reconciliation. Automated injection is valuable but is not an OS gesture. Test final installed packages rather than substituting a developer binary. No physical-device claim follows from a build runner or emulated viewport.

## Test inclusive tasks and diagnosis

Choose combinations from the audience and platform matrix: keyboard-only open/use/save/cancel/retry/clear, logical focus and dialog return, touch target/drag alternatives, platform Back and unsaved-work decisions, desktop DPI/multiwindow, browser text zoom/reflow, native large type, long/RTL translations and input methods where supported. Inspect names, roles, errors and progress with the actual target assistive technology. Verify contrast and non-color meaning, reduced-motion behavior and accessible print/export if promised.

W3C describes tools as assistance rather than conformance determination. Android likewise combines manual accessibility-service testing with tools and automation. WCAG 2.2 is a web reference; native platform units and semantics need their own evaluation. Legal applicability and institutional acceptance are independent from engineering targets. ([W3C evaluation](https://www.w3.org/WAI/test-evaluate/), [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [Android testing](https://developer.android.com/guide/topics/ui/accessibility/testing))

Diagnostics should explain operation, state, stable error code, retryability and completed/failed items without passwords, tokens, private content or unnecessary full paths. Prefer bounded local logging when sufficient; remote crash reports are a separate data-flow decision. Exercise an operational failure and a diagnostic-sink failure. Logging must not leak, grant authority, corrupt work, or replace an actionable error with false success. ([OWASP logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html))

## Trace one release candidate through transformations

Track source revision and dirty state → pinned build/dependency inputs → tested binary and embedded assets → signed/packaged output → extracted/mounted contents → installed identity/runtime → published/downloaded artifact. Signing/stapling/packaging alter bytes legitimately: retain input/output digests and verification evidence, not an impossible identical-hash requirement across transformations. Rebuilds create new candidates. Test promotion candidates without silently rebuilding after qualification.

Inventory everything shipped: native libraries, bundled interpreters, JS/wasm, models, fonts, runtime installers, licenses/notices and required corresponding source. Record an SBOM and provenance appropriate to the channel, or explicitly state absence. Hashes identify bytes; code signatures support publisher trust; notarization supplies platform review/ticket evidence; SBOMs inventory components; attestations connect artifacts to claimed build identities. None proves absence of vulnerabilities. Verify expected product/publisher/repository/workflow/channel rather than accepting any valid signature. Offline attestation verification requires provisioned trust material and cannot learn later revocations. ([GitHub attestations](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations), [offline verification](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/verify-attestations-offline))

Keep signing secrets outside source, logs and packages. Fail a trusted channel when required signing/verification fails; label unsigned/debug evaluation packages clearly with their unqualified targets and trust limits. Never recommend globally disabling operating-system protections. Generate final download hashes after signing/stapling. Inspect extracted bundle modes/symlinks and signatures, final runtime dependencies and permissions; archive creation success alone is insufficient.

On a clean ordinary-user machine/profile without source checkout or developer configuration, install/extract the intended candidate and complete a fictional open/create → process/edit → save/export → close/reopen journey. Reopen output independently. Test declared offline conditions, upgrade/cancel/error/uninstall and data retention. Verify published bytes/download and actual changed behavior when publication is authorized; HTTP success alone is not deployment verification.

## Compact release record

Use this proposed schema or the project's equivalent. Do not add maintenance timestamps or dated status labels; immutable identifiers and substantive format/signing fields suffice.

```yaml
schema: go-app-release/v1
release_id: IMMUTABLE_IDENTIFIER
source: {revision: COMMIT_OR_UNKNOWN, dirty: false}
target: {os: TARGET, arch: TARGET, runtime: EXACT, abi: EXACT_OR_NA}
inputs: {go: PINNED, flags: [], dependency_digest: SHA256}
artifacts:
  tested: {sha256: DIGEST, assets: DIGEST}
  package: {sha256: DIGEST, derived_from: DIGEST, publisher_evidence: PATH_OR_UNKNOWN}
  extracted: {inventory: PATH, verification: PATH_OR_NOT_RUN}
  installed: {identity: ID_OR_UNKNOWN, runtime_revision: REV_OR_UNKNOWN, evidence: PATH}
  published: {location: URL_OR_NA, sha256: DIGEST_OR_UNKNOWN, evidence: PATH}
checks:
  - id: clear_then_late_result
    kind: SYNTHETIC_INTEGRATION
    result: NOT_RUN
    evidence: NONE
    limits: "Execution not available"
  - {id: real_drop, kind: NATIVE_GESTURE, result: NOT_RUN, reason: TARGET_UNAVAILABLE}
gates:
  task_design_accessibility: {result: RESULT, evidence: PATH}
  privacy_education_applicability: {result: RESULT, evidence: PATH}
  security_boundaries: {result: RESULT, evidence: PATH}
  recoverable_delivery: {result: RESULT, evidence: PATH}
supply_chain: {notices: PATH, sbom: PATH_OR_ABSENT, provenance: PATH_OR_ABSENT}
decision: {status: GO_OR_CONDITIONAL_OR_NO_GO, scope: TEXT, unresolved: []}
authorization: "Existing instruction for publication, or outside current scope"
```

`GO` concerns only the tested scope. Use `CONDITIONAL` for explicit prerequisites before exposure and `NO_GO` for established critical boundaries, essential-task failures/data loss, severe inaccessible required tasks, or unsupported material safety/privacy claims. An unavailable essential qualification can block that target while allowing a synthetic-data prototype or narrower release. Report the limitation without pretending all targets passed. Readiness does not grant deployment permission, legal conformance, school approval or store acceptance.

Original educational prose by Miguel Guhlin for [VCC](https://mguhlin.github.io/vcc/), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Linked materials retain their own terms.
