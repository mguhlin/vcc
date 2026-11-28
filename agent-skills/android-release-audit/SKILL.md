---
name: android-release-audit
description: "Use for security & delivery. Review Android permissions, updates, privacy recovery and final signed artifacts before release; investigate Play Protect warnings with evidence."
license: CC-BY-4.0
---

# Android Release Audit

Decide what can be released, to which channel, on the evidence available. Use this for an Android pre-submission review, a significant permission/data/update change, or a reported Play Protect warning. It does not install scanners, submit an app, create accounts or authorize publication. Preserve existing project instructions and publication authorization; an audit alone authorizes review, not unrelated changes.

## Establish the channel and identity

Record source revision and dirty files, final artifact SHA-256, package/version code/name, signing certificate digest, target/minimum API, native ABI inventory, supported devices, intended audience, distribution channel, test environment and exclusions. Preserve user data and unrelated work. Use synthetic fixtures on disposable local/emulated devices; do not probe production, upload APKs or contact Google/vendors without the relevant authorization. Inspect project-controlled setup/tests before execution. Never expose signing keys or credentials.

Distinguish these routes:

- **Google Play:** assess Play developer/content/data/permission rules, submission artifact, Play App Signing/update continuity, listing and account prerequisites. An APK alone is not a new Play submission package. Verify current channel exceptions rather than assuming one package rule for every distribution.
- **Direct APK distribution:** valid APK signatures and transparent OS-consented installation remain necessary. Play Protect may evaluate sideloaded apps. Play-specific restrictions are not evidence that every sideloaded feature is malware, and sideloading does not exempt an app from unwanted-software principles.
- **Google OAuth verification:** applies to direct Google API authorization/scopes where required. A desktop synced folder or Android document-provider grant is not, by itself, direct app OAuth access.
- **Google Workspace Marketplace:** a separate review of Workspace integrations/listings. Approval there does not clear an Android warning or provide Play approval.

Read the current primary documents in [policy sources](references/policy-sources.md) for the applicable route. Do not treat a dated guide, remembered API floor, a third-party rubric or this skill as current Google policy.

## Investigate a warning before changing code

Obtain the exact warning title and all explanatory text, APK version/source, installation route and scan result if available. Separate an unknown-app scan prompt, unrecognized-developer warning, sensitive-permission block, old-target warning and specific harmful-app finding. One generic sentence cannot identify the cause. Hash the public APK and compare it with the tested artifact and expected certificate; a matching hash establishes identity, not safety.

Keep Play Protect enabled. Do not instruct users to bypass an unresolved warning. If Google offers a scan, allow that platform assessment; a local checker cannot substitute for it. If a reviewed app appears misclassified, prepare the official appeal facts: package/version, APK URL/digest, certificate digest, complete warning, behavior/permissions, reproduction and actual remediation. Submission requires the owner's authorization and any required account/contact information. Do not claim an appeal was submitted or accepted without evidence.

Do not rename packages, rotate signing identities, pack/obfuscate code or alter bytes merely to evade classification. Preserve legitimate update/data continuity and fix the underlying behavior. Do not promise that removing a permission will remove a warning unless independently established.

## Trace source to protected operations

Start with credentials in current source, relevant Git history and shipped bytes. Report locations and masked classifications, not secret values. Inventory entrypoints, imports, network destinations, exported components, URI grants, bridges, background work, storage/caches/logs/backups, exports and deletion.

Follow each lower-trust input through validation to the final authority. Examples include feed HTML to native/web rendering; release metadata to any installer; a document grant to a shared-file write; and Erase to revocation, database deletion and cache cleanup. A picker grants access to one resource, not arbitrary paths. Validate size, count, nesting, integer ranges, URLs and actual content before replacing valid work. Confirm rejection preserves protected state.

For optional sync, test off/disconnect, revoked provider access, malformed/unrelated files, partial writes, independent offline edits, concurrent changes, restart and lost permission. Explain shared fields and external copies. Keep optional connections optional; do not add OAuth or a backend simply to satisfy a checklist.

**Deletion order matters:** invalidate pending work and revoke/disconnect remote access before erasing records. A failed image/media/cache deletion must not skip sync revocation or silently reconnect old state. Attempt independent cleanup independently, report remaining copies truthfully, and test failure/reopen/late-completion paths. Exports and provider backups need separate retention explanations.

## Apply the ten-domain rubric

This is an operational VCC gate adapted from the creator's rubric, not Google's published scoring algorithm. Classify each domain for the stated channel with a source path, artifact identity, method, actual result and remaining evidence. Use **Pass**, **Conditional**, **Fail**, or **N/A with reason**. Unknown/unexecuted controls are Conditional, not automatic passes. A known policy violation or established required-invariant failure is Fail; it does not automatically establish malware or a particular Google enforcement outcome.

| Domain | Evidence needed for Pass | Conditional or Fail triggers to investigate |
| --- | --- | --- |
| Malware/device abuse | Scoped source/artifact/dependency review finds no malicious behavior; required platform tests identified | Unresolved payloads/packers or runtime evidence are Conditional; demonstrated spyware, hidden execution, exploit/abuse behavior is Fail. Never assert proof of zero malware. |
| Deception/MUwS | Identity, icon, behavior, disclosures and normal install/uninstall accurately match | Misleading identity/system-update UI, hiding, coercion or interfering with uninstall is Fail when established; ambiguous flows need resolution. |
| Permissions/APIs | Minimum effective permissions mapped to real core features; denial/revocation and scoped pickers tested | Non-core restricted permissions or missing required declarations are Fail for the affected channel. Sensitive permission presence alone does not prove abuse. |
| Data/privacy | Implemented recipients/SDKs/storage/retention match in-app notice and required listing/Data Safety declarations; deletion tested | Missing Console evidence is Conditional; undisclosed collection or proven broken required deletion is Fail. Account-deletion obligations apply when app accounts exist. |
| Dynamic code/updates | Release code/update path meets the channel policy; no untrusted executable loader | Play-delivered apps must use Play-managed updates, including supported Play update APIs. An external self-APK updater is a Play release blocker even if signed and user-confirmed. Distinguish direct APK distribution and applicable interpreter exceptions. |
| Network/cryptography | Intended TLS validation, scoped destinations, bounded I/O, maintained crypto and appropriate secret storage | Trust-all TLS or sensitive cleartext disclosure is Fail; unresolved DNS/redirect/cancellation boundaries are Conditional. Keystore is needed for appropriate device secrets, not a requirement to invent keys. |
| Third-party SDKs | Exact SDKs/versions/recipients inventoried, applicable advisories and policies checked | Known covert collection/abuse is Fail. Unknown dependencies or relevant unfixed advisories remain Conditional. There is no universal Play certification for every library; an app with no ad SDK needs no ad certification. |
| API/platform integrity | Current verified API floor met by packaged target; lifecycle/background/service behavior tested appropriately | Outdated target blocks the affected submission. Bypass/interference is Fail when established. Unsupported physical/minimum-OS behavior remains Conditional. |
| Monetization/ads | Actual billing, pricing, renewals, cancellation and ads meet applicable policies | Evaluate current regional/program exceptions. Deceptive billing/ads or prohibited payment routing is Fail; no monetization is N/A with source evidence. |
| Content/safety/IP | Appropriate content/audience rating, rights, reporting/moderation and Families/AI requirements where triggered | Missing required rating/reviewer evidence is Conditional; established prohibited content/IP violations are Fail. Externally reading user-selected feeds is different from hosting a public social network or generating AI content. |

Do not total or average scores to override a Fail. One material Fail blocks that release route. Conditional requires named prerequisites, impact and a resolving check; some uncertainties, including an unresolved harmful-app warning, should hold Android promotion. N/A needs architectural evidence. Zero identified Fails is necessary under this local rubric but does not guarantee any Google scan, review, account outcome or continuing compliance.

## Exercise the final installed artifact

Use existing reviewed tools where available. Optional VCC APK preflight: [check_android_release.py](https://mguhlin.github.io/vcc/scripts/check_android_release.py) with official build-tools, an explicitly verified API floor and scratch output. It uploads nothing. It checks named static properties only; extra permissions require app-specific analysis and an unsupported tool/parser result is unverified. Do not rewrite FAIL to PASS by adding an exception unless the underlying policy actually permits that channel/use.

Test legitimate and denied cases on final signed bytes: install, import/open, read/process, export, independently reopen, offline use, share/provider grants, Back/cancel, rotation, background/foreground, process restart and signed upgrades retaining state. Exercise malformed input, wrong/expired grant, wrong signing identity/version, storage failure, denied cleanup and late callbacks. Test TalkBack, large text and supported providers on named targets or retain explicit gaps. An emulator without Google services cannot reproduce a real Play Protect verdict. A successful signature or emulator install is not a Play scan.

Bind build inputs → signed/package bytes → extracted inventory → installed identity → any published bytes with hashes and methods. Rebuilds create new candidates. Keep app data, test fixtures/APKs and signing material out of downloads. Record SBOM/provenance availability honestly. Verify the normal task and former failure after authorized fixes, with a nearby regression. Preserve earlier evidence rather than pretending an old result covers changed bytes.

## Report and decide

Use chat unless the owner requested a file. Include scope/channel/revision, a ten-row ledger, prioritized confirmed findings, separate hypotheses/design observations, fixes/tests, unresolved provider/account facts, artifact identity and **Release / Conditional / Hold** with reasons. Examples:

- A Play build with an external APK installer: **Fail; Hold for Play**, regardless of local signature checks.
- A scoped direct APK with permission checks but no physical-device or Play Protect evidence: **Conditional**, not Play-approved.
- An unresolved reported harmful-app warning: **Hold promotion pending characterization/review**, not “probably safe, install anyway.”
- A cache-error test leaves sync connected after Erase: **Fail for deletion invariant**; disconnect first, retest the actual UI and independent cleanup failures.
- A local public reader with no accounts, billing, ads, AI or hosted UGC: record those absent features as N/A instead of adding them.

Publication follows existing authorization only after applicable blockers are resolved. Record the separate Google/owner decisions still required. Readiness does not authorize contacting a third party, changing credentials, uploading private material or creating a developer account.

Original VCC guidance by Miguel Guhlin, CC BY 4.0. Adapted from the creator's Android audit rubric and lessons from permission, updater and deletion reviews. Primary-source links are references, not reproduced Google policy text or endorsements.

## VCC source and reuse

Maintained source: https://mguhlin.github.io/vcc/skills/android-release-audit/SKILL.md

Readable guide: https://mguhlin.github.io/vcc/guides/skills.html#android-release-audit

VCC educational prose is CC BY 4.0. Attribute Miguel Guhlin and link to VCC; cited third-party material retains its own terms.

[references/policy-sources.md](https://mguhlin.github.io/vcc/agent-skills/android-release-audit/references/policy-sources.md)

Credits and terms: https://mguhlin.github.io/vcc/CREDITS.md
