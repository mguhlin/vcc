# Prompts for an educator’s project

Place the three core instruction files in your project root. Download `securevcc/securevcc.md` from VCC and put it there as `securevcc.md`. Attach the files instead if your assistant cannot read the project. Use invented data, and approve any external-service connection deliberately.

## First build

First, copy `templates/PROJECT_BRIEF.md` from the VCC download into your project's main folder as `PROJECT_BRIEF.md` and complete it. This is your project plan, separate from the design instructions in `WEB_DESIGN.md`.

> Read my completed PROJECT_BRIEF.md (the project plan), WEB_DESIGN.md (design instructions), EDU_COMPLIANCE.md (education privacy instructions), and securevcc.md (security instructions). If the brief is missing, help me create it from VCC's project brief template before writing code. Inspect the existing project before editing. Name the audience, educational task, and data flows. Compare three page structures and choose the one that makes the main task easiest. Build a small working version with no unnecessary accounts, trackers, or dependencies. Test the main journey and report evidence and unresolved decisions.

## Purposeful redesign

> Read WEB_DESIGN.md and inspect every existing route and important interaction. Preserve working features. Identify generic design choices that obscure the user’s task. Choose a coherent direction appropriate to the audience. Fix spacing, palette, copy, typography, layout, and interaction states. Test the same journeys before and after the change. Do not invent testimonials, usage figures, or compliance badges.

## Accessibility pass

> Apply the accessibility requirements in WEB_DESIGN.md and EDU_COMPLIANCE.md to the actual pages. Test the main task with keyboard alone, visible focus, narrow-screen reflow, enlarged text, and appropriate assistive technology where available. Use an automated tool if available, but separate its results from manual review. Fix demonstrated barriers. State exactly which checks were not run. Do not claim full WCAG conformance from an automated scan.

## Security review

> Use securevcc.md for a source review and safe local synthetic tests. Start with secrets reaching the browser, authentication and object permissions where applicable, unsafe inputs, uploads, dependency risks, and third-party data flows. Report confirmed vulnerabilities separately from hardening ideas. Ask for authorization before testing any live service unless it is already authorized. Do not send real student information or credentials to a testing service.

## Education privacy review

> Apply EDU_COMPLIANCE.md. Describe what this application actually receives, stores, shares, exports, and deletes, including hosting requests, URLs, browser storage, logs, and AI vendors. Identify the age band and applicable institutional or legal questions using current official sources. Keep unknowns unverified. Fix what can be safely fixed, document unresolved decisions, and do not claim school authorization or compliance without evidence.

## Release review

> Read all three core instruction files and complete LAUNCH_REVIEW.md with evidence. Test the actual task and relevant failure paths. Separate source review, automated tests, manual checks, and checks not run. Identify unresolved school, vendor, privacy, and accessibility decisions. Give a release decision limited to the reviewed scope. If student-data safeguards are unresolved, keep the prototype on invented data.

## Maintain an existing project

> Inspect the change and its actual effect on users, dependencies, storage, and network calls. Apply the relevant parts of WEB_DESIGN.md, EDU_COMPLIANCE.md, and securevcc.md. Preserve working behavior. Update documentation to match implemented behavior. Test the changed journey and relevant regressions. Do not add public maintenance timestamps or claim checks you did not perform.
