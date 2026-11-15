---
name: clearcopy
description: "Use for text & file hygiene. Inspect and clean authorized text or file metadata while preserving meaning, multilingual text, attribution, and required disclosures."
license: MIT
---

# ClearCopy

## Purpose and scope

Help a user inspect and clean content they own or are authorized to process. Separate text quality, invisible Unicode, ordinary metadata, and media-provenance marks. The supplied archive includes a separate HTTP service and optional heavy backends; this portable skill does not bundle or start them. Inspect available tools and their capabilities before promising any operation.

## Workflow

1. Identify the actual file type, the requested change, permitted output, and information that must remain. Prefer a new cleaned sibling file; preserve the original unless in-place editing is explicitly requested.
2. Inspect before changing. Explain which suspicious characters or metadata fields were actually found and distinguish them from harmless or necessary formatting. Do not infer AI authorship from unusual spaces, prose style, or a detector score.
3. Protect code, formulas, citations, quotations, exact values, links, identifiers, required disclosures, and attribution. For mixed Markdown/HTML, act only on authorized prose segments; whole-file normalization can change code, attributes, or behavior.
4. For text, preserve language, accents, no-break space semantics, emoji joiners, and writing-direction controls unless a specific inspected change is requested and justified. Avoid aggressive homoglyph replacement or Unicode normalization by default. Never decode a PDF, DOCX, or image as ordinary text and overwrite its binary structure.
5. For prose improvement, remove filler and improve clarity while preserving every factual claim, number, name, citation, and requested tone. Do not add claims or rewrite quotations inside quotation marks. Provide a diff or explanation when requested.
6. For file metadata, use a supported format-aware tool only within the authorized scope. Preserve required authorship, licensing, content credentials, and disclosures as applicable; do not silently strip all fields. Check service endpoint ownership, local/remote data flows, and upload authorization before using any external service.
7. Re-inspect the output, verify readability/structure and protected spans, and report exactly what changed. If the required tool or service is unavailable, give a plan and mark the operation not performed.

## Reporting and boundaries

Distinguish verified character/field changes from best-effort prose edits and unverified detection claims. Do not promise human authorship, undetectability, removal of secret-key marks, or complete removal of pixel/audio/video watermarks. Editing can invalidate signed provenance or alter appearance; keep the original and disclose material limits. Do not falsely claim an inspection service, image edit, or export ran.

The source archive's generalized anti-detection, compulsory multi-pass rewriting, and blanket metadata stripping are not adopted. This adaptation focuses on inspectable privacy and text/file hygiene while preserving attribution and required disclosures. Any use of upstream software is a separate, authorized setup with its own dependencies and licenses; no upstream scripts are run by the VCC page.

## Source and license

Adapted from the creator-supplied archive of [watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover), particularly its text-hygiene workflow. Its source contains the following notice, retained here for the adapted material. VCC's educational explanations and artwork have their separately stated terms.

MIT License

Copyright (c) 2026 watermarks-remover contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## VCC source and reuse

Maintained source: https://mguhlin.github.io/vcc/skills/clearcopy/SKILL.md

Readable guide: https://mguhlin.github.io/vcc/guides/skills.html#clearcopy

The MIT notice in the source body remains part of this skill.

Credits and terms: https://mguhlin.github.io/vcc/CREDITS.md
