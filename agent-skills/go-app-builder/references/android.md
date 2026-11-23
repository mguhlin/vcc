# Android delivery with a shared Go core

Use this reference for an installed Android app or Android browser/PWA support. These are different deliverables; choosing one does not establish the other's capabilities.

## Select and prove the integration route

A native Kotlin/Compose or Views app can call a narrow Go facade packaged by `gomobile bind` as an AAR containing Java bindings and native libraries. Keep the facade binding-compatible: supported scalar/byte types and restricted interfaces differ from arbitrary Go APIs. Handle failures within the boundary; panics/exceptions crossing it can terminate the application. Establish a build spike and actual task before committing to a large port. ([gomobile](https://pkg.go.dev/golang.org/x/mobile/cmd/gomobile), [gobind types](https://pkg.go.dev/golang.org/x/mobile/cmd/gobind#hdr-Type_restrictions))

Fyne/Gio document Android packaging; Wails documents an experimental Android host with a native Go library and WebView. Official Wails material distinguishes stable desktop from experimental mobile and documents mobile limitations, including file-dialog and window differences. Check exact pinned-release source/support rather than assuming no mobile route or complete desktop parity. A browser/PWA wrapper without Go integration cannot be described as a native shared-Go engine. ([Fyne Android](https://docs.fyne.io/started/mobile/), [Gio Android](https://gioui.org/doc/install/android), [Wails status](https://wails.io/status/), [Wails Android](https://wails.io/guides/mobile/android/))

Pin the compatible Go/x-mobile/SDK/NDK/JDK/Gradle/Android Gradle Plugin inputs actually used. Resolve contradictory prerequisites against the selected release and actual build; do not copy old framework template values as current store policy. Native UI + AAR is a useful default when direct Android accessibility, provider and lifecycle integration matter, but it remains a design choice requiring evidence.

## Treat documents as capabilities

Use the Storage Access Framework for user-selected document/tree access. A `content:` URI identifies a provider resource, not an ordinary path. Use `ContentResolver` streams/descriptors and the granted operation; do not manufacture a path from the URI. `ACTION_CREATE_DOCUMENT` creates a new document rather than overwriting by name. Directory access restrictions and provider semantics apply. Size metadata can be unknown and grants can fail after moves, deletion or revocation. ([SAF document access](https://developer.android.com/training/data-storage/shared/documents-files))

If an engine needs a seekable file, make a bounded private temporary copy and account for disk full, sensitive contents, deletion and interruption. A cloud provider can fetch/synchronize independently of application networking. Distinguish permission to read a selected input from permission to create, replace, delete or share output. Retain persistable permissions only for a justified feature and test revocation after reopening.

Use operation IDs and generation guards around picker and provider callbacks. A cancelled or stale picker must not create authority or restore cleared work. Test local/cloud providers, unknown sizes, nonseekable streams, empty/binary/large input, lost grants and failed output. Report partially written provider documents accurately; do not promise filesystem atomic rename or universal rollback. Preserve recoverable processed results for an explicit retry when safe.

## Design lifecycle and background behavior

Android controls process lifetime; cached processes can die and `onDestroy()` is not guaranteed. A ViewModel helps configuration changes, but process death needs deliberate saved-state/persistence design. Decide whether operations are foreground-only, restartable, or resumable. Preserve only necessary non-secret UI metadata by default and explain when interrupted work must restart. ([Process lifecycle](https://developer.android.com/guide/components/activities/process-lifecycle), [saved state](https://developer.android.com/topic/libraries/architecture/saving-states))

For justified persistent work, use the appropriate platform scheduler and an idempotent restart strategy. WorkManager can stop work after cancellation, constraint changes or replacement; cooperate with stop signals and prevent a late result from reporting success. Long-running workers and foreground services have version-specific quotas, start restrictions, permission/type requirements and user expectations. A Go goroutine does not bypass these rules. Re-read the policy for the actual target OS rather than promising unlimited background processing. ([Manage WorkManager](https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/manage-work), [long-running work](https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/long-running), [foreground restrictions](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start))

Propagate cancellation from UI/worker through the Go operation registry and I/O loops. Reset revokes capabilities and generations first. Exercise rotation, resize, background/foreground, Back/cancelled Back gesture, close during commit, process death and reopen. Reconcile uncertain output before retry; do not silently repeat provider writes.

## Constrain a WebView host

Prefer packaged content loaded through `WebViewAssetLoader` and a deliberate origin policy. Unmatched asset requests can fall through to networking, so local assets alone do not prove no uploads/egress. Avoid permissive `file://` access. Inventory origins, frames, navigation, popups, mixed content and resource fallbacks; disable unnecessary debug facilities in release. ([Local WebView content](https://developer.android.com/develop/ui/views/layout/webapps/load-local-content))

An `addJavascriptInterface` object is exposed to all frames and does not provide calling-frame origin verification. Web-message bridges need origin/source restrictions too. Keep untrusted previews away from privileged bridges. Expose only bounded operations with native-established capabilities; never arbitrary paths, URLs, commands or evaluation. An allowlisted top-level page alone does not prove every caller is trusted. ([Android bridge risks](https://developer.android.com/privacy-and-security/risks/insecure-webview-native-bridges))

Omit INTERNET when the application has no networking need, while describing independent provider/OS behavior honestly. Test release network behavior and actual installed WebView engine/version. Chunk/binary transport can reduce full-file base64/JSON costs, but measure Go/native/JS copies and backpressure rather than assuming zero copy.

## Keep keys, backup and portable recovery distinct

Android Keystore supports non-exportable keys and usage restrictions. Hardware backing depends on device capability and must be inspected. Device-bound wrapping/authentication is different from a portable cross-platform file/password format; design explicit user-approved export/recovery rather than expecting Keystore keys to travel to other platforms. ([Keystore](https://developer.android.com/privacy-and-security/keystore))

Private storage can enter Auto Backup. Review cloud and device-transfer rules, cache/no-backup placement, sensitive temporary files and replacement-device behavior; `allowBackup=false` is not a universal manufacturer-independent transfer guarantee. Test backup/restore assumptions and make exclusions intentional. Do not promise forensic erasure or that no device/provider data ever leaves the phone. ([Auto Backup](https://developer.android.com/identity/data/autobackup))

## Inspect the delivered native artifact

Record `minSdk`, compile SDK, `targetSdk`, native ABI, package ID/version, WebView requirement and distribution channel separately. Map Go `arm64` to Android `arm64-v8a` and Go `amd64` to `x86_64`; select supported physical/emulator targets deliberately. Inspect the packaged libraries, not just build configuration. ([Android ABIs](https://developer.android.com/ndk/guides/abis), [APK Analyzer](https://developer.android.com/tools/apkanalyzer))

Verify 16 KB native page compatibility at ELF, package-alignment, dependency and runtime levels. A framework template, recent NDK or successful Go build does not independently certify the Go runtime and every bundled/prebuilt library. Read the current native-page and Play target requirements at release time; store thresholds must not be hardcoded as forever-current constants in this skill. ([16 KB guidance](https://developer.android.com/guide/practices/page-sizes), [Play target policy](https://developer.android.com/google/play/requirements/target-sdk))

Signed APKs install; an AAB is a publishing format from which a distribution channel or `bundletool` produces device APKs. Verify the actual signed APK or generated split set and install that artifact. Align before APK signing, verify afterward and do not modify signed bytes. `apksigner` does not sign an AAB. Keep app/upload signing identities, key custody, backups and update continuity explicit and private. ([Signing](https://developer.android.com/studio/publish/app-signing), [App Bundles](https://developer.android.com/guide/app-bundle), [bundletool](https://developer.android.com/tools/bundletool), [apksigner](https://developer.android.com/tools/apksigner))

Qualify the essential task on declared minimum/target OS, representative physical arm64 and emulator x86_64 where supported, 16 KB runtime, provider and WebView combinations. Test touch, keyboard/IME, TalkBack, large text, orientation/window changes, Back, offline packaged launch, revoked permissions, disk full and cancellation races. Browser viewport emulation is not installed-device evidence. Android recommends combining manual accessibility-service tests, analysis tools and automation. Store acceptance, institutional approval and legal conformance remain separate determinations. ([Accessibility testing](https://developer.android.com/guide/topics/ui/accessibility/testing), [adaptive apps](https://developer.android.com/develop/ui/compose/layouts/adaptive/get-started-with-adaptive-apps), [Predictive Back](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture))

Original educational prose by Miguel Guhlin for [VCC](https://mguhlin.github.io/vcc/), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Linked materials retain their own terms.
