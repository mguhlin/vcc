# Architecture, contracts, and honest sharing

Use this reference when selecting a stack, porting a working product, or changing a format/engine boundary. The recommendations below are engineering synthesis; a source describing a tool does not qualify an arbitrary application.

## Inspect before choosing

Read the actual platform entry points, nested `go.mod` files, `go.work`, frontend/native locks, build tags and packaging inputs. Identify filesystem, process, networking, CGO/unsafe, GPU, UI-thread and third-party engine assumptions. Preserve known-good output and error behavior as fixtures before modifying the boundary. Run a small build-and-task spike for each proposed target; compilation alone cannot establish runtime integration.

Go's cross-compilation does not automatically bring native dependencies: CGO normally needs a suitable target compiler and is disabled by default for cross-builds. Conversely, a package that avoids CGO can still load embedded native libraries or require a GUI stack. Record actual dependencies rather than equating a compiler flag with self-containment. ([cgo](https://pkg.go.dev/cmd/cgo), [Gio platform dependencies](https://gioui.org/doc/install), [Fyne cross-compilation](https://docs.fyne.io/started/cross-compiling/))

## Compare viable architectures

| Shape | What can share | Decisive prototype / maintenance question |
| --- | --- | --- |
| Portable Go core, native desktop/Android views, browser DOM + wasm | Domain implementation and format; UI/adapters differ | Can the selected packages compile and perform the bounded operation through every facade? Does each UI expose the essential task accessibly? |
| Go desktop webview shell and web UI | Browser assets and bridge contract; engine only if actually integrated | Which webview codecs/APIs/dialogs work, and where is native authority enforced? |
| Fyne/Gio UI across selected targets | More view code plus Go behavior | Test actual input, rendering, accessibility and file integration; packaging support alone does not prove feature parity. |
| Go shell with bundled interpreter/native/JS engine | Existing engine and stable format/API | Are all target binaries, native modules, models, licenses and process-lifecycle controls packaged and verified? |
| Independent Go and JavaScript implementations | Format and observable behavior | Can both implementations read the other's output and reject the same malformed/resource-hostile cases? |
| Remote processing service | Protocol, perhaps core implementation | Explicitly disclose uploads, server authority, retention, operating cost and outage behavior. This is a product/data-flow decision. |

Wails uses native webviews with web UI and Go logic. Its official status page distinguishes stable v3 desktop from experimental mobile; v2 and v3 have different installation and Linux dependency contracts. Do not encode “Wails v3 is always prerelease” or “Wails has no Android route.” Resolve the selected release's source, support policy and platform gaps before using its commands. Fyne and Gio document mobile/web packaging, with different capabilities and native requirements. ([Wails FAQ](https://wails.io/faq/), [Wails status](https://wails.io/status/), [Wails v2 installation](https://v2.wails.io/docs/gettingstarted/installation/), [Fyne mobile](https://docs.fyne.io/started/mobile/), [Fyne web](https://docs.fyne.io/started/webapp/), [Gio Android](https://gioui.org/doc/install/android), [Gio wasm](https://gioui.org/doc/install/wasm))

A sound default is `core` for pure behavior, platform facades for translation and operation lifecycle, and adapters for native I/O and permissions. This is a proposed boundary, not a mandatory directory layout. Keep contexts/channels/UI objects internal where a foreign-language binding cannot export them. `gomobile bind` emits an Android AAR; `gobind` has restricted exported types and specific error shapes. A generated AAR is not a generated Android interface. ([gomobile](https://pkg.go.dev/golang.org/x/mobile/cmd/gomobile), [gobind restrictions](https://pkg.go.dev/golang.org/x/mobile/cmd/gobind#hdr-Type_restrictions))

Keep a decision record explaining the primary task, existing code preserved, selected engine/UI/adapters, rejected alternatives, release support contract, unresolved experiments and migration/recovery path. Preserve a proven engine until a replacement passes its compatibility corpus. Label a shell as a shell; embedding web assets does not establish that Go performs the processing.

## Define feature parity by outcomes

Use one row per material feature and one target record per actually promised configuration. A useful feature record is:

```yaml
feature: export_document
semantics: "Create a new document; preserve current work on refusal"
format: document/v1
platforms:
  desktop: {adapter: native_save, support: UNKNOWN, evidence: []}
  android: {adapter: saf_create, support: UNKNOWN, evidence: []}
  browser: {adapter: blob_download, support: DEGRADED, evidence: []}
fallback: "Retain result and offer another explicit save attempt"
limits: {input_bytes: TO_DEFINE, output_bytes: TO_DEFINE}
completion: "Adapter-specific evidence; download click is not persisted-file proof"
```

Support labels describe intended or documented capability; `PASS/FAIL/NOT_RUN/NA` describe checks. Do not turn a fallback into hidden behavior loss. Document folder fidelity, metadata, printing/media, permissions, cancellation, offline conditions and output location where they differ. Independently reopen produced files in an appropriate consumer.

## Keep format rules above adapters

Define magic/version and supported migration paths; text encoding and invalid-text behavior; endianness and length units; integer and floating-point ranges; time zone/offset/precision; empty/null/absent fields; canonical ordering if required; duplicate fields/IDs; checksums/authenticated metadata; and forward-compatibility policy. Document whether filenames preserve Unicode spelling or normalize, and handle normalization/case collisions without silently overwriting. Portable archive names also need explicit handling of Windows reserved names, trailing dots/spaces, drive-qualified paths and links.

Golden fixtures should cover exact byte preservation, empty files/directories, binary bytes, non-BMP and combining text, mixed newlines, long labels, range limits, offset timestamps, malformed/truncated input, unknown versions, duplicate/colliding names and one-over-limit work. For two engines, exercise writer A → reader B and writer B → reader A; a self-round-trip can preserve the same bug twice. Use independently produced fixtures where possible and distinguish conformance-to-format from platform UI behavior.

For required encryption, define algorithm identifiers, salt/nonce sizes, authenticated headers, KDF profile/units, chunk ordering/finalization and accepted resource ceilings. Nonce uniqueness is an AEAD requirement; do not weaken protection silently to fit a device. Treat untrusted KDF parameters as resource requests and reject oversized profiles before allocation. RFC 9106 offers Argon2 profiles and vectors, not universal device suitability or a product certification. Benchmark chosen profiles on the supported low-memory target and test wrong credentials, tampering, reordering and resource rejection across implementations. ([Go AEAD](https://pkg.go.dev/crypto/cipher#AEAD), [RFC 9106](https://www.rfc-editor.org/rfc/rfc9106.html))

## Minimal application manifest

This proposed schema is a map to evidence, not a certificate. Replace symbolic values with project facts; omit irrelevant features rather than adding infrastructure to fill fields.

```yaml
schema: go-app-manifest/v1
product_id: example.tool
primary_task: "Transform a user-selected local document"
audience: "Declared users and accessibility/localization needs"
source: {revision: UNKNOWN, dirty_summary: UNKNOWN}
targets:
  - os: TARGET
    arch: TARGET
    minimum_os: UNKNOWN
    ui_runtime: PINNED_OR_UNKNOWN
    native_abi: UNKNOWN_OR_NA
entrypoints: [ui]
engines:
  - {role: transformation, implementation: GO_OR_BUNDLED, revision: PINNED}
permissions:
  files: "Native-selected resources, action-specific rights"
  network: "Enumerated destinations or none in declared mode"
data:
  - {class: workspace, stores: [memory], recipients: [], clear: "Invalidate work first"}
formats: [document/v1]
limits: {input_bytes: TO_DEFINE, expanded_bytes: TO_DEFINE, jobs: TO_DEFINE}
inputs: {go: PINNED, native_dependencies: [], frontend_locks: []}
journeys: [open_process_save, cancel, failed_write, clear_late_callback]
```

Maintain source revisions and protocol versions without public maintenance timestamps. Protocol-required signing metadata and substantive data timestamps are separate concerns. Use [validation-release.md](validation-release.md) for evidence linking the manifest to actual deliverables.

Original educational prose by Miguel Guhlin for [VCC](https://mguhlin.github.io/vcc/), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Linked materials retain their own terms.
