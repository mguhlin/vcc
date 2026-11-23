# Desktop integration and packaging

Read for Windows, macOS or Linux adapters and releases. Qualify OS/CPU/runtime combinations separately. A self-contained executable, portable archive, offline installer and authenticated publisher are independent properties.

## Qualify native authority and output

Keep renderer-controlled strings away from unrestricted native filesystem bindings. Trace picker/drop provenance through the pinned framework's actual transport. In inspected Wails v3.1.0 source, the JavaScript runtime can construct a drop request containing filenames; the backend decodes those filenames and dispatches a window event. This is a source-grounded reason to test forged framework events, not a claim that every framework/version or application has a proven exploit. ([Runtime drop request](https://github.com/wailsapp/wails/blob/v3.1.0/v3/internal/runtime/desktop/@wailsio/runtime/src/window.ts#L638-L672), [backend decoding](https://github.com/wailsapp/wails/blob/v3.1.0/v3/pkg/application/messageprocessor_window.go#L369-L400), [event dispatch](https://github.com/wailsapp/wails/blob/v3.1.0/v3/pkg/application/webview_window.go#L1669-L1685))

A native callback that mints a random ticket from these paths can still authorize attacker-chosen resources. Verify that native code registers OS-selected handles before renderer mediation and reconciles later requests, or require a native picker/reconfirmation before privileged access. Restrict source selection to the intended operation; opening is not permission to replace, delete, execute or upload. Test direct arbitrary-path bindings, forged framework drop requests, replay, wrong operation/window, expired generation and close/reset revocation. Add actual OS drag/drop and picker-cancel evidence separately from synthetic calls.

Use directory-relative APIs where appropriate, but read the chosen Go release's limitations. `os.Root` resists traversal; it does not authenticate the root or implement an entire link/overwrite/resource policy. Checking symlinks and subsequently opening an ordinary path can race. Go also explicitly warns that non-Unix `Rename` is not atomic even within one directory. ([Go root guidance](https://go.dev/blog/osroot), [Rename](https://pkg.go.dev/os#Rename))

Reserve staging privately near the intended destination when filesystem semantics require it. Bound transfer sessions/chunks and validate offset/order/final length; check every write, flush and close result. Recheck destination rights and operation generation at commit. Document replacement versus exclusive-create behavior, metadata/ACL treatment and durability. Test source change, lock/permission denial, disk full, cancellation near commit, symlink escape, duplicate commit and restart with partial output. A single-file replacement does not make a multi-file restore transactional. Restore untrusted trees into a fresh directory and preserve outside-tree sentinels in tests.

## Own helper process lifecycles

Bundle exact target-specific engines and native modules with a component/hash/license inventory. Use absolute trusted paths, argument APIs rather than a shell, minimal environment and bounded stdin/IPC. Do not inherit ambient proxies or credentials unnecessarily. For loopback engines, bind intended loopback interfaces, require per-session authority, constrain Host/Origin and routing as relevant, disable unintended redirects and bound responses. Localhost alone is not authorization.

Define startup/readiness deadlines, maximum handshake size, crash-after-ready behavior, cancellation, child-window teardown, application close and parent death. Have one shutdown owner and reap each child once. `CommandContext` defaults to killing its process; `Process.Kill` does not kill descendants or wait for exit. Use and test target-specific tree ownership/termination mechanisms, and bound pipe shutdown through supported APIs such as `WaitDelay`. Abrupt parent death needs an explicit policy beyond a close handler. ([CommandContext](https://pkg.go.dev/os/exec#CommandContext), [Cmd lifecycle fields](https://pkg.go.dev/os/exec#Cmd), [Process.Kill](https://pkg.go.dev/os#Process.Kill))

Keep UI updates on the toolkit's required thread and computation outside it. On quit, distinguish unsaved work, cancellation in progress and an already committed result. Do not claim clean shutdown merely because the main window disappeared.

## Windows: prove runtime installation and application behavior separately

Webview-based applications may require WebView2. Microsoft separates the small Evergreen bootstrapper, which fetches the runtime, from the **full Evergreen standalone installer** for offline deployment. Fixed Version is a distinct bundled-runtime strategy with servicing obligations and framework-specific integration. Choose the correct architecture and inspect the actual supported installation behavior. ([Microsoft distribution guidance](https://learn.microsoft.com/en-us/microsoft-edge/webview2/concepts/distribution))

If promising clean offline installation, package a publisher-verified full standalone installer, record its identity and handle failure/reboot results; a bootstrapper cannot satisfy that promise. Verify required runtime installation independently, then launch the packaged application and complete its task while offline. Record runtime absent/present cases and per-user/machine permissions. A ZIP depending on a preinstalled runtime must state the prerequisite. Do not call an x64 program physically ARM-qualified merely because emulation exists.

Sign the executable/installer where trusted distribution requires it and verify final Authenticode policy/publisher. Signing can change bytes, so hash final outputs and link them to input evidence. Keep credentials isolated and do not bypass OS protections as a workaround. ([SignTool signing](https://learn.microsoft.com/en-gb/windows/win32/seccrypto/using-signtool-to-sign-a-file), [SignTool verification](https://learn.microsoft.com/en-us/windows/win32/seccrypto/signtool))

Exercise ordinary-user install, upgrade, cancelled install, path with spaces/non-ASCII, read-only/disk-full errors and uninstall. Removal should target registered/shipped files and respect user-created files and the stated retention policy.

## macOS: verify the extracted package

Preserve executable modes, legitimate bundle/framework symlinks, resources and every native architecture slice. A universal launcher with a single-architecture helper is not a universal application. Sign nested code appropriately, then the app, using the release identity and required hardened-runtime settings. **Signing and notarization are separate checks.** Apple's notarization service issues a ticket; ad hoc signing does not establish Developer ID trust. ([Apple notarization](https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution))

Staple eligible artifacts so Gatekeeper can obtain the ticket offline. ZIP containers cannot themselves be stapled; staple eligible contents and recreate the archive. Use bundle-aware packaging that preserves symlinks and modes, then extract the actual ZIP or mount the actual DMG into a new location. Verify the extracted bundle's signature, ticket, identifiers, minimum OS, architectures, helper/library inventory and launch behavior. Verify again after any modification that can invalidate signing. ([Apple custom workflow](https://developer.apple.com/documentation/security/customizing-the-notarization-workflow))

A staged `.app` pass does not establish archive fidelity. Test browser-downloaded quarantine/Gatekeeper behavior and offline launch on declared CPU/OS combinations. Keep untested combinations explicit. Preserve protocol-required signing timestamps; omit editorial maintenance dates.

## Linux: state the ABI and dependency contract

Record distribution baseline, architecture, glibc versus musl, GTK/WebKit ABI, graphics/session assumptions and target GUI dependencies. Resolve requirements from the pinned framework. Wails v2 and v3 differ; v3 status documentation describes GTK4/WebKitGTK 6.0 defaults and version-limited GTK3 support. A copied build tag or old package name must be checked against the actual selected release. ([Wails status](https://wails.io/status/), [Wails v2 Linux requirements](https://v2.wails.io/docs/guides/linux-distro-support/))

A native package declaring dependencies does not contain them. A `.deb` requiring an online package-manager fetch is not offline self-contained installation. Supply a matching dependency closure/repository for an air-gapped promise or qualify a packaging format with explicit runtime prerequisites. AppImage, Flatpak, tarball or “static Go” labels do not establish universal Linux portability. ([Debian dependency policy](https://www.debian.org/doc/debian-policy/ch-relationships.html))

Test dependency resolution, ordinary-user launch from another working directory, relocation, desktop/icon integration, executable bits and supported display/session behavior. Do not blindly dereference all package symlinks or reject legitimate framework links; user-archive extraction has a separate stricter threat model.

## Native task acceptance

For each declared target, inspect final package inventory, architecture, dependency closure, notices, permissions, symlinks, modes, signatures and hashes, then run the installed essential task with fictional data. Include actual picker/drop/save/cancel, keyboard, screen reader, large text/DPI, multi-monitor or resize where applicable, print/media permissions and errors. Webview print/media APIs can differ from browsers; Wails documents native printing because `window.print()` may not work. Offer an explicit export/external-viewer fallback where suitable and stop media streams at close. ([Wails frontend runtime](https://wails.io/reference/frontend-runtime/))

Use [validation-release.md](validation-release.md) to distinguish source, synthetic real-webview, native gesture, clean-install and physical-device evidence. No check in this reference has been executed merely by reading it.

Original educational prose by Miguel Guhlin for [VCC](https://mguhlin.github.io/vcc/), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Linked materials retain their own terms.
