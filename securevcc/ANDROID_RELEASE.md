# Installed Android release checks

Use this worksheet with SecureVCC MOBILE-01 through MOBILE-04. An APK check is evidence for specific properties, not store approval, legal compliance or proof of complete security. The app-store playbook reference is https://github.com/mjmirza/app-store-compliance ; VCC does not install its hooks or redistribute its rule pack.

## Inspect final bytes

Run Python 3 with official Android build-tools and Java installed:

```sh
python3 scripts/check_android_release.py path/to/final.apk --build-tools /path/to/android/build-tools --minimum-target YOUR_VERIFIED_API_FLOOR --output /tmp/apk-preflight.json
```

Supply the policy floor required for your actual distribution channel after reading the current official Play target API policy. The script has no fixed forever-current target threshold, uploads nothing and writes only the specified report. It inspects packaged release flags, cleartext/backup settings, permissions, exposed components, ZIP paths, native ELF alignment, recognized private-material filenames, signatures and package alignment. Extra permissions/components require app-specific review; this conservative baseline can flag legitimate features. Missing tools or parsing errors return NOT_CHECKED and a failing exit status. PASS_SCOPED means only the named checks passed. It is not a complete secrets or dependency scan.

## Complete the evidence

| Evidence | Record |
| --- | --- |
| Identity | Source revision, final artifact SHA-256, package/version, publisher certificate, toolchain |
| Essential task | Install final signed bytes; import, process, save, reopen; valid and rejected synthetic data |
| Lifecycle | Cancellation, revoked provider access, partial output, disk failure, rotation, process death and restart |
| Accessibility | Named OS/device, TalkBack, keyboard, large text, target sizes, landscape/resize, RTL and long translations |
| Privacy | Real recipients/SDKs, offline behavior, backup/transfer, deletion including derived copies, exported-copy limits |
| Store readiness | Applicable Data Safety/privacy declarations, review access, payments/account deletion/AI rules, publisher account/listing |
| Delivery | Final signed download digest equals tested artifact; recovery and private signing-key custody |

Mark every row PASS, FAIL, NOT RUN or N/A with a reason. A source-only pass cannot replace installed behavior. A preview may disclose unresolved platform qualification; do not present it as store-ready. Block an affected release when there is a critical boundary failure, essential task/data-loss failure or material false claim.

Revalidate official sources: [permissions](https://developer.android.com/privacy-and-security/permissions), [WebView bridges](https://developer.android.com/privacy-and-security/risks/insecure-webview-native-bridges), [backup](https://developer.android.com/identity/data/autobackup), [signing](https://developer.android.com/studio/publish/app-signing), [page sizes](https://developer.android.com/guide/practices/page-sizes), [target policy](https://developer.android.com/google/play/requirements/target-sdk).

Original VCC educational guidance by Miguel Guhlin, CC BY 4.0. Upstream references retain their own terms.

## Permission, update and warning decisions

Use the [Android Release Audit skill](../skills/android-release-audit/SKILL.md) and its primary policy references for the ten-domain release gate. Play APK self-updates cannot be excused by a baseline exception. Direct APK and Play routes have different delivery rules; neither a valid signature nor a local preflight establishes Play Protect approval. Keep protection enabled and hold promotion for an unresolved harmful-app warning.

Test that cache-cleanup failure cannot skip sync disconnection, revocation or cancellation during local erase. Repeat the actual confirmation flow and check protected state before and after, including failure/restart. Record missing Console declarations, physical-device checks and real-provider evidence explicitly.
