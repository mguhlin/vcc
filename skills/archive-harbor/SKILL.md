---
name: archive-harbor
description: "Plan and verify Vimeo library downloads through supported controls while distinguishing triggered downloads from files confirmed on disk. Use for authorized video archiving."
---

# Archive Harbor

## Scope and prerequisites

Download or organize videos only from a folder the user owns or is authorized to manage and for which downloads are permitted. Confirm the requested folder, quality, and destination using information already supplied. Prefer Original when available and requested; do not promise source-file availability. A connected authenticated browser is required for account actions. Check the tools actually available rather than hard-coding an old browser-tool name. Let the user handle sign-in or sensitive challenges.

The destination may be the browser's configured download directory. Do not claim access to the user's filesystem or move files without an actual connected file tool. Agree on a useful batch/size limit when many large files could be involved, report observed sizes as work proceeds, and preserve the user's ability to pause.

## Inventory before downloads

Read the actual folder UI and state the item count. Compare visible inventory with the folder count and account for pagination or virtualized content rather than assuming all items are loaded. Preserve each full video-management path, including unlisted privacy-path components, as its identity; do not mistake a hash for a video ID. Keep private paths in the local task context, not public reports.

Use stable accessible selectors and the current supported browser interface. Inspect changed markup; do not run a supplied script blindly or assume exact menu labels remain current. Use only the normal authorized download controls. Never extract cookies, credentials, signed download URLs, private query tokens, or bypass a disabled download option.

## Bounded download loop

1. Match one known video and verify its title/identity.
2. Open its menu and an actual current download dialog. Close or distinguish stale dialogs and verify the dialog belongs to this video; do not assume a newly created node is the only valid UI pattern.
3. Check offered quality and observed size. If the requested version is absent, report it and obtain a choice when no fallback was already authorized.
4. Trigger the download through its button and record **triggered**, not completed, until a supported download or filesystem observation confirms completion.
5. Work in small batches, report failures and cumulative known size, and retry only known misses. When an outcome is ambiguous, reconcile before triggering another download.

Identical sizes are a warning worth investigating, not proof of a duplicate: different videos can have the same size. Confirm identity and, where tools permit, filename, byte count, or hash. Do not assert that rapid-fire downloads always succeed or that a browser page reveals actual saved files.

## Ledger and verification

Track expected title/identity, quality, observed size, trigger result, completion evidence, destination status, and needed follow-up. Preserve already completed work across a retry plan. Flag possible filename suffix duplicates and ongoing large downloads before moving files. If disk observation is unavailable, provide an expected-file checklist and ask the user to compare it with the destination; do not report verified completion.

## Sources and limits

Adapted from the supplied Vimeo workflow, with corrected size/duplicate and DOM assumptions. Consult current [Vimeo library download help](https://help.vimeo.com/hc/en-us/articles/29641523095057-How-to-download-a-video-from-my-library) and [download permissions/source-file guidance](https://help.vimeo.com/hc/en-us/articles/12426502581265-How-to-download-a-video-on-Vimeo) as needed. This instruction file does not include a browser connector, account access, or a downloader service.
