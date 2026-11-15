---
name: daylight-pages
description: "Use for daily learning calendars. Build an accessible one-page-per-day learning calendar with reliable date mapping, navigation, and classroom projection."
license: CC-BY-4.0
---

# Daylight Pages

## Purpose and decisions

Build or adapt a static daily-opener flipbook calendar. Establish five decisions: calendar-date versus numbered school-day mapping; audience bands; authored versus template-generated content; approximate daily activity length; and whether each day needs an image. Preserve an existing site's style and constraints. Use the calendar metaphor only where it supports the task.

## Content and data

Keep authored content in validated JSON or another simple maintained source, then generate the shipped HTML. Give each entry a stable ID, date/day mapping, title, learning prompt, audience variants, optional teacher notes/answer, related resource IDs, image scene direction, and alt text. Keep variants together so they stay aligned. Validate required fields, duplicate IDs, enums, link targets, source coverage, and translation placeholders. Do not ship unfinished or fabricated standards entries.

Use actual authored scenarios where specificity is essential. Template-based patterns can be useful for a short sequence; vary them and explain their limits. Do not invent claims about production cost or prior deployment results. A weekly rhythm can support planning, but define what happens to skipped weekday activities.

## Date correctness

Use a consistent UTC date plus UTC formatting strategy, or local calendar dates throughout. Do not mix them. Never derive local calendar dates with an accidental UTC shift. Test at least two materially different time zones, daylight-saving boundaries, month/year boundaries, weekends, holidays, and start/end conditions where relevant.

Make the school start and exclusions editable when school-day mapping is needed. Explain the difference between numbered school days and weekday-preserving weeks. Outside the covered dates, show the nearest available real page with a plain explanation. Functional calendar dates are substantive content; omit maintenance timestamps and dated status badges.

## Interface and accessibility

Provide labeled Previous, Next, Today, and month-jump controls; accessible audience/language choices; shareable date/day fragments; and browser-history behavior that matches the chosen navigation design. Keyboard navigation must not hijack typing or controls. Support swipe only as an optional alternative to buttons. Announce the new date and title politely.

Use a native accessible modal or inline month panel with predictable dismissal/focus. Projection should enlarge the learner task and hide teacher notes, with a working exit/fullscreen-state handler. Collapsed answers in shipped HTML are not confidential; private answer keys need a separate protected route. Offer print and text-only views. Reduced motion should remove the flip animation rather than require another distracting transition.

## Images, languages, storage, and checks

Keep essential instructional text as real HTML. Images need accurate alt text, source/creation credit, optimized dimensions, and a text-first missing-image state. Generate or license actual assets only when needed and authorized. Validate translated text, accents, placeholders, standard IDs, and word-game adaptations with appropriate human review.

If preferences persist locally, explain shared-device behavior and provide scoped reset with storage-failure handling. Do not claim offline/PWA support from static hosting alone. Use existing authorized build/browser tools to verify dates, month jump, Today, history, keyboard, reflow, language toggles, reset, print, and image failures. Preserve working content, links, and user work during repairs.

## VCC source and reuse

Maintained source: https://mguhlin.github.io/vcc/skills/daylight-pages/SKILL.md

Readable guide: https://mguhlin.github.io/vcc/guides/skills.html#daylight-pages

VCC educational prose is CC BY 4.0. Attribute Miguel Guhlin and link to VCC; cited third-party material retains its own terms.

Credits and terms: https://mguhlin.github.io/vcc/CREDITS.md
