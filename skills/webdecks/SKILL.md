---
name: webdecks
description: Build or edit portable HTML slide decks using Web Deck v5, with speaker notes, a synchronized presenter view, keyboard navigation, phone reflow, and print-to-PDF. Use when the user requests this HTML deck system rather than a PowerPoint file.
---

# WebDecks

Create presentations with Miguel Guhlin's [Web Deck v5](https://mguhlin.github.io/webdecks/) system. Use the included framework rather than recreating its navigation and presenter behavior. This folder includes the specification, framework CSS and JavaScript, starter markup, and a chatbot-ready standalone reference. No package installation or build step is needed to author a deck.

Read [the complete specification](references/webdeck_spec_v5.md) before building or editing. For a chatbot returning a single HTML file, read [the standalone edition](references/webdeck_v5_standalone.md), which embeds the framework. If supporting files are unavailable, use [the complete skill ZIP](https://mguhlin.github.io/vcc/downloads/webdecks.zip) or fetch the matching paths beneath https://mguhlin.github.io/vcc/skills/webdecks/ . Do not claim to have read unavailable files. [PROJECT_PROMPT.md](PROJECT_PROMPT.md) provides an adaptable brief.

## Establish the requested deck

Inspect existing project instructions, deck files, and unsaved changes. Preserve working content and the user's chosen identity. Establish the audience, purpose, time available, source material, presenter, hub link, and output mode. Infer low-risk choices where possible. A request to plan or review does not authorize implementation or publication; preserve any publication authorization already established for the project.

Keep one idea per slide and readable projected text. Use short audience-facing phrases, at least 18 px for reading text, and real headings. Put teaching logistics and fuller explanations into first-person conversational speaker notes, about 90–130 words per slide when the material warrants it. Avoid invented facts, citations, personal anecdotes, and maintenance dates. Preserve presentation dates the user explicitly requests and substantive dates in the content.

## Build with the supplied framework

1. For a project with separate assets, copy `assets/deck-framework.css` and `assets/deck-framework.js` from this skill into the project's `assets/` folder. Copy [the starter markup](assets/template-deck.html.txt) into the project's `decks/` folder and rename it to an `.html` file. The `.txt` suffix keeps this library's download inert; the downloaded contents are HTML.
2. Replace sample content, facilitator details, and resource links. Remove any template-only examples. Point the exit control at the project's actual hub. Keep the framework attribution comment and generator metadata in the head; put the deck owner's name in visible content.
3. Customize palette and typography through deck-local CSS loaded after the framework. Prefer system font fallbacks or authorized local fonts for offline use; the reference template's Google Fonts request needs internet. Include all required media in a portable download and distinguish linked assets from a truly self-contained file.
4. Keep the 1280 × 720 slide canvas. Each slide contains `.slide-body`, a sibling `.slide-footer`, and its `.notes` block. The first slide carries `current`. Use the documented cover, divider, and content types and content blocks. Avoid shrinking text to fit dense content; split the slide instead.
5. Preserve keyboard navigation, notes toggle, fullscreen, progress, exit-to-hub, print, and presenter controls. The V key opens the synchronized presenter view, with separate current/next previews, notes, timer, and A−/A+ notes resizing. Browser pop-up and fullscreen permissions still apply. Keep the next button and preview frame IDs distinct.
6. Add deck-local grid and positioned-art selectors to `.deck.reflow` rules so phones and high zoom produce a readable stacked layout. Use meaningful image alternatives, keyboard-accessible links, sufficient contrast, and reduced-motion behavior. Speaker notes travel with public HTML; never put confidential notes or answer keys in a public deck.

For one portable HTML file, inline the supplied CSS and JavaScript using the standalone reference. Bundle or embed authorized images as required. Updating shared framework files affects linked decks; inlined decks must be rebuilt or patched separately. Do not change framework behavior to satisfy ordinary content edits. If a requested framework change is authorized, keep its specification and affected copies synchronized and test both title and content slides.

## Verify the delivered experience

Render every new or edited slide at 1280 × 720 and inspect it for clipped text, collisions, unreadable images, and footer overlap. Check phone reflow around 380 px and high zoom, including deck-local grids and images. Test keyboard next/previous, first/last, notes, help, fullscreen, and exit behavior. Verify presenter synchronization in both directions, next-slide preview, notes resizing, and close behavior. Check that the title hides the exit control and content slides show the correct destination.

Use print preview or a generated PDF when available to verify one slide per page, visible content, and hidden controls. Do not equate opening the print dialog with checking an exported PDF. Test offline only if promised, and report any remote fonts/media or browser restrictions. Automated scans and the supplied reflow behavior do not establish accessibility conformance; record assistive-technology gaps honestly.

Hand over the deck or project files, source attribution, checks performed, and material limits. Apply the project's VCC design, privacy, security, and recovery guides where relevant and available, without inventing school approval or adding student-data collection. Publish only within existing authorization, then verify the live deck.

## Source and reuse

Adapted for the VCC reusable library by Miguel Guhlin from his [mguhlin/webdecks](https://github.com/mguhlin/webdecks) repository. The bundled specification, standalone edition, framework, and starter are distribution snapshots; the WebDecks repository remains their maintained source. See [LICENSE](LICENSE). This skill and its project prompt retain the following MIT terms.

MIT License

Copyright (c) 2026 Miguel Guhlin

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
