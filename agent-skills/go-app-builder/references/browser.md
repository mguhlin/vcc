# Browser Go, capabilities, and offline behavior

Use this reference for browser/installed-PWA delivery, including browser engines on Android. A native Android WebView host additionally needs [android.md](android.md).

## Pair Go and its runtime deliberately

Browser Go targets `GOOS=js GOARCH=wasm`, with a JavaScript host and browser adapters. Ship `wasm_exec.js` from the exact pinned Go toolchain with the wasm binary; Go documents matching the compiler/helper major release and exact pairing avoids avoidable drift. Locate the helper from that toolchain rather than copying an arbitrary old example. WASI is a distinct execution target, not a substitute for browser JavaScript/DOM integration. ([Go WebAssembly](https://go.dev/wiki/WebAssembly))

Keep browser APIs behind a narrow wrapper. A `syscall/js.FuncOf` callback blocks the JavaScript event loop until it returns; blocking on asynchronous JS from that callback can deadlock. Use a nonblocking operation entry point, managed callback lifetimes and `Func.Release` at the correct teardown point. A goroutine is not itself an independent browser UI thread. ([syscall/js](https://pkg.go.dev/syscall/js#FuncOf))

Run expensive wasm work in a dedicated worker when appropriate, with versioned messages, operation IDs, progress and cancellation. Transferable ArrayBuffers avoid certain structured-clone copies by transferring ownership and detaching the sender's buffer; Go linear-memory transfers can still copy. Bound active jobs, time, bytes and retained results; terminate a worker only with an explicit partial-output and cleanup policy. ([Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers), [Go byte-copy APIs](https://pkg.go.dev/syscall/js))

Serve wasm with correct MIME for streaming instantiation and provide a deliberate fallback/error where needed. Streaming module compilation says nothing about application input/output buffering. Include JS source buffers, Go copies, compression/KDF working memory, base64 expansion and result retention in peak-memory measurements. Buffer-based crypto APIs can still require whole-file memory. ([instantiateStreaming](https://developer.mozilla.org/en-US/docs/WebAssembly/Reference/JavaScript_interface/instantiateStreaming_static), [SubtleCrypto.encrypt](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/encrypt))

## Start with a usable file baseline

Use `<input type="file">` or actual user-selected File objects for import and an explicit Blob download/save action for output. Release Blob URLs when no longer needed. Enhance with native-style file/directory access only after capability detection. Secure contexts, user activation, permissions and browser availability apply. Obtain a save handle during a suitable user gesture if later processing would lose activation; defer the write until the validated result is ready. ([File API](https://developer.mozilla.org/en-US/docs/Web/API/File_API), [file-system guidance](https://developer.chrome.com/docs/capabilities/web-apis/file-system-access), [directory picker](https://developer.mozilla.org/en-US/docs/Web/API/Window/showDirectoryPicker))

Fallbacks should be product behavior: retain a result for explicit download retry, offer ZIP or individual-file output when directory writing is unavailable, and explain lost folder metadata/fidelity. Selected File objects are not arbitrary OS path authority. Browser download initiation is not confirmation that the OS persisted bytes successfully. Do not promise overwrite/shredding of originals, unrestricted folder access or preservation of empty directories without target evidence.

Validate browser drops, clipboard, URL and `postMessage` inputs with the same schema/resource/generation rules as primary imports. Wrong-origin or wrong-source messages must not gain authority. Bound actual reads and expansion even when size metadata is present. Reset/cancel invalidates pending reads, workers, handles and callbacks before removing state; late completions must not resurrect cleared records.

## Define four different offline claims

| Claim | Decisive condition |
| --- | --- |
| Local processing | Source and observed request boundaries show processing stays in the declared client mode. Hosting requests remain distinct. |
| First-ever hosted visit offline | Assets cannot arrive from an unavailable host without prior delivery; provide a qualified package instead of a false promise. |
| Cached PWA offline relaunch | Complete assets are installed; controlled clients/cache lifecycle and a network-disabled restart are tested. |
| Offline source build | Toolchains, modules, frontend/native inputs and build assets are locally provisioned, then the build is tested without network. |

Installability is browser/platform dependent and does not itself require a service worker or prove offline readiness. Service workers require a secure context, with HTTPS/development-localhost rules and origin/scope constraints. Copying a folder or opening `file://` is not automatically a supported wasm/worker/offline distribution. ([PWA installation](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable), [service workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers), [Gio wasm serving](https://gioui.org/doc/install/wasm))

Treat an update as a coherent versioned asset set: HTML, CSS, scripts, wasm, matching runtime helper, worker scripts, fonts/icons and required engines/help. Prepare the replacement cache fully before marking ready; retain the known-good set until activation safely completes. Keep in-flight work on one version, offer updates when idle and avoid forcing `skipWaiting()` into unfinished operations. Test interrupted installation, stale tabs, mixed-version assets, missing resources and rollback. This is an application consistency design built on the worker lifecycle, not a universal transaction supplied by CacheStorage. ([Worker lifecycle](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers))

Storage can be evicted or user-cleared, and private/managed environments differ. Request persistent storage only with a product reason and handle refusal. Workers can be stopped; service-worker events and background sync do not guarantee indefinite processing or resume at the interruption point. Model long work and recovery honestly. ([Storage eviction](https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria), [background operation](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Offline_and_background_operation))

## Constrain content and network boundaries

Use safe text/DOM sinks for plain imported content, and a deliberate sanitizer/isolated sandbox for active formats. A sandbox preview should have only the capabilities its task requires and no unintended route to the privileged application origin/bridge. Constrain navigation, frames, popup/openers, downloads, external resources and message origins/sources independently. Rendering, sanitization and network policy are distinct controls. ([OWASP DOM guidance](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html))

Test CSP against the actual bootstrap, workers and exports. Allow only required script/wasm execution and asset fetches; `wasm-unsafe-eval` is narrower than broad `unsafe-eval` where supported. A blanket `connect-src 'none'` can block the app's own wasm fetch. CORS needs server cooperation for cross-origin fetches and is not authorization. A public server/proxy fallback must disclose what file/content/metadata goes where, retention, access and failure behavior, then remain within user authorization. ([CSP script-src](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/script-src), [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS))

Keep secrets out of URLs, analytics, logs, persistent caches and localStorage by default. Origin storage is not isolated merely by URL path. A non-extractable CryptoKey restricts export operations but does not prove hardware backing, resistance to injected script using the key, or memory zeroization. Minimize lifetimes and references without promising forensic erasure of managed memory, downloads, clipboard or OS backups. ([Web Crypto security considerations](https://www.w3.org/TR/webcrypto/#security-considerations), [CryptoKey.extractable](https://developer.mozilla.org/en-US/docs/Web/API/CryptoKey/extractable))

## Qualify the complete task

Use accessible semantic DOM controls where they fit. Test keyboard focus/dialog behavior, screen-reader names/status/errors, touch and drag alternatives, browser zoom/reflow, Android large text and keyboard, long translations, contrast and reduced motion. A rendered canvas needs an effective accessible route for essential work. W3C cautions that tools alone do not establish conformance. ([WCAG 2.2](https://www.w3.org/TR/WCAG22/), [W3C evaluation](https://www.w3.org/WAI/test-evaluate/))

Run actual declared Chromium/Firefox/WebKit-family and relevant Android browser/PWA/WebView combinations. Node-executed wasm tests are different evidence from browser tests. Exercise baseline/fallback branches, activation timing, denied permissions, worker crash/cancel, hostile bounds, offline restart, eviction, interrupted updates and CSP/CORS errors. Observe intended requests using synthetic files. Record exact engine, target and artifact; do not turn viewport emulation, an install icon or one successful browser into universal compatibility. ([Go wasm testing](https://go.dev/wiki/WebAssembly))

Original educational prose by Miguel Guhlin for [VCC](https://mguhlin.github.io/vcc/), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Linked materials retain their own terms.
