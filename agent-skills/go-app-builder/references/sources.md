# Sources, scope, and revalidation

This skill synthesizes primary platform documentation, standards and VCC's four evidence-oriented guides. Tables say what each source supports and what remains a project decision. Implementation recommendations, manifests, state/evidence schemas and acceptance recipes are original synthesis, not upstream standards. Documentation proves a mechanism or support policy; it does not prove that an arbitrary app has passed tests.

The desktop, mobile/browser and crosscutting research notes were source/documentation research. They included read-only implementation observations generalized here without identifying individual developments or reproducing their source paths. No app, native gesture, device, installer, signature, offline workflow, legal conformance or live deployment was verified by that research. The skill itself requires these distinctions in subsequent work.

Reopen material version-sensitive sources when choosing/upgrading dependencies and before release. Pin resolved versions in project records. Do not treat source publication history, a framework template or this guide's wording as evidence of current SDK/store requirements. Record unresolved facts as `UNKNOWN` or `NOT_RUN` as appropriate; avoid maintenance timestamps and dated status labels in authored public material.

## Architecture and framework contracts

| Primary source | Supports | Recheck / does not establish |
| --- | --- | --- |
| [Go cgo](https://pkg.go.dev/cmd/cgo) | CGO build constraints and target compiler requirements | Selected cross-toolchain and native dependency closure |
| [Wails FAQ](https://wails.io/faq/) | Go/webview architecture and cross-build considerations | Pinned-release feature behavior and actual accessibility |
| [Wails status](https://wails.io/status/) | Desktop/mobile maturity and platform/GUI support contract | Exact selected version, deprecations and native dependencies |
| [Wails v2 installation](https://v2.wails.io/docs/gettingstarted/installation/) and [Linux support](https://v2.wails.io/docs/guides/linux-distro-support/) | Version-specific desktop prerequisites and WebKit ABI distinctions | Do not mix v2 instructions with v3 flags/requirements |
| [Wails Android](https://wails.io/guides/mobile/android/) | Experimental host architecture, API differences and template configuration | Actual Go/SDK/NDK compatibility, store policy and provider behavior |
| [Fyne cross-builds](https://docs.fyne.io/started/cross-compiling/), [mobile](https://docs.fyne.io/started/mobile/) and [web](https://docs.fyne.io/started/webapp/) | Documented toolchain/packaging routes and web limitations | Selected-release file dialogs, AT, graphics and target usability |
| [Gio installation](https://gioui.org/doc/install), [Android](https://gioui.org/doc/install/android) and [wasm](https://gioui.org/doc/install/wasm) | Native dependency and platform build/serve routes | Compatible tool versions and actual input/AT/runtime task |
| [gomobile](https://pkg.go.dev/golang.org/x/mobile/cmd/gomobile) and [gobind](https://pkg.go.dev/golang.org/x/mobile/cmd/gobind#hdr-Type_restrictions) | AAR/library generation and restricted foreign-language facade | Pinned x/mobile build, supported exported API and native library runtime |
| [Go WebAssembly](https://go.dev/wiki/WebAssembly) | Browser target, helper pairing, serving/testing and WASI distinction | Exact compiler/helper/assets and browser dependency compatibility |

## Desktop authority and distribution

| Primary source | Supports | Recheck / does not establish |
| --- | --- | --- |
| [Wails v3.1.0 runtime drop method](https://github.com/wailsapp/wails/blob/v3.1.0/v3/internal/runtime/desktop/@wailsio/runtime/src/window.ts#L638-L672), [backend request decoder](https://github.com/wailsapp/wails/blob/v3.1.0/v3/pkg/application/messageprocessor_window.go#L369-L400) and [window dispatch](https://github.com/wailsapp/wails/blob/v3.1.0/v3/pkg/application/webview_window.go#L1669-L1685) | Specific source path from renderer-provided filenames to event dispatch | Trace selected version/OS and app authority issuance; source finding is not an executed exploit or universal framework claim |
| [Go root-relative API guidance](https://go.dev/blog/osroot) and [Rename](https://pkg.go.dev/os#Rename) | Traversal/TOCTOU distinctions and OS-dependent replacement semantics | Actual API/platform limits, links, overwrite policy and crash durability |
| [CommandContext](https://pkg.go.dev/os/exec#CommandContext), [Cmd](https://pkg.go.dev/os/exec#Cmd) and [Process.Kill](https://pkg.go.dev/os#Process.Kill) | Cancellation defaults, wait controls and descendant/wait limitations | Per-OS process-tree ownership, abrupt parent-death and pipe cleanup |
| [Microsoft WebView2 distribution](https://learn.microsoft.com/en-us/microsoft-edge/webview2/concepts/distribution) | Bootstrapper/full standalone/Fixed Version distinction and runtime detection | Selected architecture, servicing, installer identity and independent absent-runtime/offline app proofs |
| [SignTool signing guide](https://learn.microsoft.com/en-gb/windows/win32/seccrypto/using-signtool-to-sign-a-file) and [reference](https://learn.microsoft.com/en-us/windows/win32/seccrypto/signtool) | Authenticode signing/verification procedure | Actual final publisher trust, channel and signed artifact identity |
| [Apple notarization](https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution) and [custom workflow](https://developer.apple.com/documentation/security/customizing-the-notarization-workflow) | Signing/notarization requirements, tickets and stapling | Extracted bundle fidelity, quarantine/Gatekeeper, every CPU slice and offline launch |
| [Debian dependency relationships](https://www.debian.org/doc/debian-policy/ch-relationships.html) | Package dependency declarations and configuration relationships | Distribution-compatible dependency closure and air-gapped installation |
| [Wails frontend runtime](https://wails.io/reference/frontend-runtime/) | Framework native printing API and browser-print caveat | Actual printer/export/webview/media behavior per target |

## Android documents, lifecycle, security and releases

| Primary source | Supports | Recheck / does not establish |
| --- | --- | --- |
| [SAF documents](https://developer.android.com/training/data-storage/shared/documents-files) | URI grants, provider streams, create/open/tree semantics and restrictions | Provider seek/size/offline behavior, revocation and partial-output recovery |
| [Process lifecycle](https://developer.android.com/guide/components/activities/process-lifecycle) and [saved state](https://developer.android.com/topic/libraries/architecture/saving-states) | Process death and configuration/state distinctions | Actual restart policy, sensitive-state retention and idempotent recovery |
| [WorkManager management](https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/manage-work), [long-running work](https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/long-running) and [foreground restrictions](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start) | Cooperative stop, scheduling and background restrictions | Current OS/target quota, permissions, task types and runtime behavior |
| [Local WebView content](https://developer.android.com/develop/ui/views/layout/webapps/load-local-content) and [bridge risks](https://developer.android.com/privacy-and-security/risks/insecure-webview-native-bridges) | AssetLoader origin model, fallback requests and frame/bridge hazards | Actual origin/source enforcement, navigation, release flags and denied requests |
| [Keystore](https://developer.android.com/privacy-and-security/keystore) and [Auto Backup](https://developer.android.com/identity/data/autobackup) | Key restrictions/hardware distinctions and backup/transfer rules | Device hardware support, manufacturer behavior, exclusions and replacement-device recovery |
| [NDK ABIs](https://developer.android.com/ndk/guides/abis) | Android native architecture names/contracts | Every packaged library's architecture and physical device evidence |
| [16 KB page sizes](https://developer.android.com/guide/practices/page-sizes) | ELF/package alignment, dependency and runtime test requirements | Final Go/prebuilt native libraries, runtime behavior and channel applicability |
| [Play target requirement](https://developer.android.com/google/play/requirements/target-sdk) | Authoritative publishing target policy | Current channel/category rules; template defaults are insufficient |
| [App signing](https://developer.android.com/studio/publish/app-signing), [App Bundles](https://developer.android.com/guide/app-bundle) and [bundletool](https://developer.android.com/tools/bundletool) | Signing identities, AAB distribution and generated APK sets | Actual key custody/update continuity and device-specific installed artifact |
| [APK Analyzer](https://developer.android.com/tools/apkanalyzer) and [apksigner](https://developer.android.com/tools/apksigner) | Packaged metadata and APK signature inspection | Final permissions/SDK/debuggability, package alignment and actual install/task |
| [Adaptive apps](https://developer.android.com/develop/ui/compose/layouts/adaptive/get-started-with-adaptive-apps), [Predictive Back](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture) and [accessibility tests](https://developer.android.com/guide/topics/ui/accessibility/testing) | Window-aware layouts, platform Back and combined AT/tool testing | Actual touch/keyboard/TalkBack/large-text task; no automatic accessibility conformance |

## Browser runtime, storage and security

| Primary source | Supports | Recheck / does not establish |
| --- | --- | --- |
| [syscall/js](https://pkg.go.dev/syscall/js) and [FuncOf](https://pkg.go.dev/syscall/js#FuncOf) | Callback event-loop behavior, lifetime and byte-copy interfaces | Wrapper lifetime, cancellation and actual Go/JS memory cost |
| [File API](https://developer.mozilla.org/en-US/docs/Web/API/File_API), [file-system capability guide](https://developer.chrome.com/docs/capabilities/web-apis/file-system-access) and [directory picker](https://developer.mozilla.org/en-US/docs/Web/API/Window/showDirectoryPicker) | File/Blob baseline, enhancement and activation/permission constraints | Actual browser/provider support, directory fidelity and persisted save result |
| [Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers), [wasm streaming](https://developer.mozilla.org/en-US/docs/WebAssembly/Reference/JavaScript_interface/instantiateStreaming_static) and [buffer encryption](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/encrypt) | Off-thread messaging/transfers, MIME requirements and buffer-based crypto | Actual end-to-end streaming, peak memory, UI responsiveness and cancellation |
| [PWA installation](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable) | Browser-dependent installation requirements | Installation icon does not prove offline processing or persisted cache |
| [Service workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers), [storage eviction](https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria) and [background operation](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Offline_and_background_operation) | Secure-context lifecycle, replacement/cache concepts, eviction and bounded background execution | Complete asset readiness, interrupted/mixed-version update, offline restart and recovery |
| [CSP script-src](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/script-src) and [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS) | Browser execution/fetch policies | Effective deployed headers/engine support; neither substitutes for authorization or zero-egress evidence |
| [Web Crypto security](https://www.w3.org/TR/webcrypto/#security-considerations) and [extractable keys](https://developer.mozilla.org/en-US/docs/Web/API/CryptoKey/extractable) | API assurance limits, origin/script trust and export restriction | No universal hardware backing, portability, zeroization or injected-script protection |

## Crosscutting verification and VCC provenance

| Primary source | Supports | Recheck / does not establish |
| --- | --- | --- |
| [Race detector](https://go.dev/doc/articles/race_detector) and [fuzzing](https://go.dev/doc/security/fuzz/) | Executed-path race detection and deterministic bounded fuzz methodology | Supported target/instrumentation, meaningful workload and untouched paths |
| [govulncheck](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck), [modules](https://go.dev/ref/mod) and [toolchains](https://go.dev/doc/toolchain) | Advisory/build configuration, dependency integrity and toolchain selection | Actual nested/native/frontend coverage, reachability, network downloads and fixes |
| [Build information](https://pkg.go.dev/runtime/debug#ReadBuildInfo) | Embedded module/build identification | Does not authenticate publisher or prove source-to-binary integrity |
| [AEAD](https://pkg.go.dev/crypto/cipher#AEAD) and [RFC 9106](https://www.rfc-editor.org/rfc/rfc9106.html) | Authenticated-encryption nonce rules and Argon2 profiles/test vectors | Product format correctness, hostile parameter limits, device benchmarks and independent review |
| [OWASP DOM guidance](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html) and [logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) | Safe rendering and proportionate redacted/robust diagnostics | Actual sink policy, reachable consequence and logging-failure behavior |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) and [W3C evaluation](https://www.w3.org/WAI/test-evaluate/) | Web accessibility criteria and need for human evaluation | Selected task/browser/AT conformance, native toolkit access and legal applicability |
| [GitHub attestations](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations) and [offline attestation verification](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/verify-attestations-offline) | Artifact/provenance/SBOM predicates and offline verification prerequisites | Expected publisher/workflow identity, later revocations and full component inventory |
| [VCC design](https://mguhlin.github.io/vcc/WEB_DESIGN.md), [education/privacy](https://mguhlin.github.io/vcc/EDU_COMPLIANCE.md), [security](https://mguhlin.github.io/vcc/securevcc/securevcc.md) and [rescue](https://mguhlin.github.io/vcc/rescue/VIBE_CODE_RESCUE.md) | Four independent principles distilled into this skill | Full guides are optional depth; claim only material actually read, and verify project evidence separately |

## Reuse

Original educational prose by **Miguel Guhlin** for [VCC](https://mguhlin.github.io/vcc/), licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Retain attribution, the license link and a notice of adaptations. This file cites and paraphrases mechanisms rather than copying manuals, software or substantial checklist text. Linked upstream works retain their own licenses. Format/source versions identify substantive technical evidence, not maintenance status.
