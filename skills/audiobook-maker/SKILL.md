---
name: audiobook-maker
description: Prepare PDF, EPUB, or supplied text for text-to-speech listening while preserving the author's prose, relocating notes, and checking for lost content. Use for listening editions and audiobook source preparation; audio synthesis is an optional separate step.
license: MIT
---

# Audiobook Maker

Prepare a faithful listening edition from a book or other authorized text. Remove reading interruptions caused by page layout while preserving the author's words, reading order, evidence, and useful navigation. The default deliverable is clean text plus a listening-ready PDF when file tools support it. Generating an audio recording is a separate, optional stage.

**Credit:** Adapted by Miguel Guhlin for [VCC](https://mguhlin.github.io/vcc/) from **Lance Eaton's Book to Audio Edition** workflow in [book-to-audiobook](https://github.com/leaton79/book-to-audiobook), introduced in [AI Audiobooks: An Update](https://aiedusimplified.substack.com/p/ai-audiobooks-an-update). The adaptation adds conservative content handling, explicit capability checks, chapter-level reconciliation, and an optional free local audio path. Retain Eaton's MIT notice below. No endorsement by Eaton is implied.

## Establish the listening edition

Use choices already supplied; ask only for missing decisions that affect content or processing:

- Identify title, author/editor, language, input files, requested output, and intended personal or authorized educational use. Work only with material the user is authorized to process. Do not bypass DRM or infer permission to publish a converted book from possession of a copy.
- Identify where processing occurs. File upload to a hosted assistant is already an external transfer; do not call it local processing. Before any further OCR, AI, or narration upload, establish that the destination is permitted. Keep student records and sensitive annotations out of unapproved services.
- Choose notes at the end grouped by chapter (recommended), after each chapter, or another requested arrangement. Preserve notes and bibliography unless the user explicitly chooses omission. Preserve in-text author–date citations by default; they carry source meaning even if awkward aloud.
- Confirm any front/back matter to omit. Distinguish optional praise, ads, index, and duplicate contents from substantive introductions, appendices, contributor names, and required rights notices. Retain required notices in the delivered package even if excluded from the narration text.
- Choose captions only or captions with spoken tables and informational figure descriptions. Preserve unique sidebar or margin content unless omission is explicitly requested.

Propose a short representative pilot before a full book or batch: include ordinary prose, a page transition, a note, and a table or figure if present. Use the user's existing choices for the pilot; resolve uncertain content decisions before repeating them across the book.

## Match the method to available tools

**Chat/text only:** process one chapter or manageable section at a time. Start small enough to reproduce the complete text without truncation, often about 1,000–2,000 words, and reduce the size if needed. Ask for readable text if extraction or image inspection is unavailable. Never imply that plain chat can OCR an unseen scan, inspect an inaccessible EPUB, or create a downloadable file without those tools.

**File/code tools:** inspect file type, PDF text-layer quality and reading order, or EPUB spine/section order. Sample opening, middle, ending, and difficult-layout pages. Check for missing pages and corrupted extraction before cleanup. For scans, use available permitted OCR and compare suspect words with page images. Work from copies in a separate output folder; never overwrite originals. For long jobs, save section outputs and a progress ledger so interruption does not require silently regenerating or skipping chapters.

Eaton's repository provides an optional extraction/rendering implementation. Its scripts, models, and dependencies are **not included** with this skill. If the user requests that route, read its README and configuration documentation and inspect the chosen revision before installation or execution; follow existing authorization and environment permissions. A word-count or extraction-ratio threshold is an alert to investigate, not proof of completeness, and English word-frequency heuristics are unreliable for other languages or specialist notation.

## Clean without rewriting

1. **Preserve prose.** Do not summarize, translate, simplify, modernize, censor, or repair the author's reasoning. Preserve quotations, names, numbers, units, meaningful punctuation, lists, equations, and deliberate typography where it affects meaning.
2. **Remove verified layout artifacts.** Remove running headers/footers, folios, repeated continuation labels, and confirmed duplicate pull quotes. Check repeated position and context; a bare number, bracketed reference, asterisk, or capitalized line is not automatically clutter. Preserve substantive list numbers, exponents, dates, and mathematical symbols.
3. **Repair mechanical breaks.** Rejoin line-wrapped paragraphs, split words, and drop caps only when the source supports the join. Keep real compound hyphens, verse line breaks, and section boundaries. Correct OCR/ligature errors only with evidence; record uncertain readings for review instead of guessing. Apply language-appropriate rules.
4. **Retain navigation.** Give parts, chapters, introductions, and appendices clear spoken headings. Preserve titles and contributor names; add a chapter label only when the structure establishes it. Retain subheadings and distinguish added navigation from the author's prose.
5. **Relocate notes with a map.** Remove only confirmed note callouts; retain a separate mapping from source page/section and callout to the destination note. Preserve note order, numbering, chapter groups, and note text, including citations and cross-references. Keep bibliography/references separate from notes. If a callout cannot be matched, retain it and flag the gap.
6. **Make visual information speakable.** Keep captions. For a table, narrate its title, row labels, column headers, values, units, missing entries, and qualifications in a consistent row-by-row order. Label this as a table narration added for listening. For charts/diagrams, add a clearly labeled image description based only on a visible source or supplied description. Distinguish author text from additions. Do not invent trends or estimates from unreadable figures. Keep a source reference and flag complex tables, equations, or diagrams needing human review; do not silently replace them with a vague summary.

## Reconcile each section before assembly

Return or save three separate components for each section:

- **Listening text:** clean author text, headings, captions, and clearly labeled authorized visual narrations.
- **Relocated notes:** original chapter/section identifiers and note numbers; say “None” only when none are present or all omissions were explicitly chosen.
- **Review ledger:** source range, first/last words, paragraph or block coverage, moved/omitted elements and reasons, OCR corrections, visual additions, unmatched notes, and unresolved readings. Keep this ledger out of the narration.

Compare the retained body and notes against the source **throughout** each section. With code, compare normalized paragraph/block sequences and investigate every unmatched span after accounting for permitted layout changes, moved notes, and labeled additions. Without code, compare smaller passages directly and describe the limited coverage. Word counts and matching endpoints cannot detect all internal omissions or substitutions. Do not claim a full reconciliation from spot checks.

If output would truncate, pause at a complete paragraph and record the last completed source location and exact continuation point. Mark the section incomplete. On continuation, check the seam for duplication and omission. Never substitute a summary for an unfinished section or label a partial book complete.

## Assemble and verify

- Assemble chapters in verified source order, followed by notes and other retained matter. Include title, author, edition/source identity when known, and a short preparation note identifying the listening adaptation and added descriptions. The skill's license does not license the source book.
- Supply clean UTF-8 text or structured Markdown as the reusable narration master. If PDF is requested and supported, use selectable text, readable 12-point serif body type, section page breaks, chapter bookmarks, and no spoken running heads or folios. Preserve language and logical reading order. A text layer and bookmarks alone do not establish an accessible PDF.
- Use a separate output name such as `Author - Short Title - Listening Edition`; avoid path/control characters and collisions. Preserve the source file and its substantive metadata. Keep the review ledger as a companion file rather than within the read-aloud stream.
- Re-extract the final PDF text when possible; compare it with the narration master for missing text, wrong ordering, duplicate headings, and encoding/ligature errors. Check chapter starts/ends, note destinations, and difficult passages. Listen to a short sample in the intended reader if available; report listening checks as untested otherwise.
- Report actual files produced, section coverage, intentional omissions, OCR use, unresolved items, and checks performed. Return drafts with visible gaps if fidelity remains unresolved. Never fabricate a download link, completed OCR run, or successful audio preview.

## Optional: make the audio locally

[PageSpindle — Spin text into listening](https://mguhlin.github.io/pagespindle/) is the companion application, maintained in its [own repository](https://github.com/mguhlin/pagespindle). Choose a Windows, macOS, or Linux installer, or open the [browser edition directly](https://mguhlin.github.io/pagespindle/browser/?v=0.3.1). Desktop editions open in their own window, install required runtime components, and automatically download verified models during first-launch setup. They work offline after setup. The browser downloads its English voice on first use; optional browser AI requires WebGPU and adequate GPU memory/storage. Paste or open text, then choose Create audiobook: local AI preparation and passage comparison are optional. PageSpindle interprets Markdown before speech, so heading hashes, emphasis asterisks and other formatting markers are silent without an AI pass. Original text and project backups retain their formatting; previously saved audio must be generated again. Source preservation, note destinations, project backups, and a copyable chatbot prompt remain available. The initial voice is English. The browser exports WAV chapters; desktop installers include FFmpeg for MP3/M4B. Check release evidence, unsigned-installer, hardware, and job-size limits. OCR, visual interpretation, listening-ready PDF production, and automatic full-book fidelity verification remain separate tasks.

When the user requests a recording, read [Free local audio path](references/free-local-audio.md). It maps clean chapter text → local speech synthesis → WAV chapter masters → MP3 chapters or an M4B with chapter metadata, without requiring a paid narration service. Verify the selected engine, voice terms, installation permissions, and a short pilot before processing the book. Keep notes as separate optional tracks. Do not upload the book, clone a person's voice, or publish the recording without the relevant authorization.

## License

This adapted skill is distributed under the upstream MIT License. VCC's separately authored project prompt and concept sketch follow VCC's CC BY 4.0 terms. Preserve this notice in standalone skill copies and adaptations:

MIT License

Copyright (c) 2026 Lance Eaton

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
