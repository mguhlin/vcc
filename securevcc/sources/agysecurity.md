# Universal Security & Privacy Audit Framework for Vibe-Coded Applications

> **Purpose:** This document is a comprehensive, reusable security and privacy audit methodology designed for **any "vibe-coded" (AI-generated or AI-assisted) application**—from zero-dependency single-file HTML/JS tools to full-stack web apps, BaaS-backed portals (Firebase/Supabase), and AI-integrated workflows.
>
> You can use this file in two ways:
> 1. **As an Auditor Reference & Checklist** when reviewing a codebase manually.
> 2. **As a Direct Prompt / Rubric for an AI Coding Agent** (e.g., *"Read `~/Desktop/agysecurity.md` and perform a full security audit and remediation of this project"*).

---

## Table of Contents

1. [Why Vibe-Coded Solutions Have Unique Security Blind Spots](#1-why-vibe-coded-solutions-have-unique-security-blind-spots)
2. [Audit Execution Workflow (5-Phase Methodology)](#2-audit-execution-workflow-5-phase-methodology)
3. [Exhaustive 12-Domain Security Audit Matrix](#3-exhaustive-12-domain-security-audit-matrix)
   - [Domain 1: DOM Safety, XSS & Client-Side Injection](#domain-1-dom-safety-xss--client-side-injection)
   - [Domain 2: Schema Validation, State Synchronization & Self-DoS](#domain-2-schema-validation-state-synchronization--self-dos)
   - [Domain 3: File Imports, Parsers & Accidental PII Ingestion](#domain-3-file-imports-parsers--accidental-pii-ingestion)
   - [Domain 4: Data Exports, CSV Formula Injection & Download Safety](#domain-4-data-exports-csv-formula-injection--download-safety)
   - [Domain 5: Privacy Modes, Anonymization & Residual State Leaks](#domain-5-privacy-modes-anonymization--residual-state-leaks)
   - [Domain 6: Client Storage (`localStorage`, `sessionStorage`, `IndexedDB`)](#domain-6-client-storage-localstorage-sessionstorage-indexeddb)
   - [Domain 7: Untrusted Browser Event Boundaries (Drag & Drop, `postMessage`, URLs)](#domain-7-untrusted-browser-event-boundaries-drag--drop-postmessage-urls)
   - [Domain 8: Content Security Policy (CSP), Network Egress & Supply Chain](#domain-8-content-security-policy-csp-network-egress--supply-chain)
   - [Domain 9: Cryptography, Randomness (CSPRNG) & ID Generation](#domain-9-cryptography-randomness-csprng--id-generation)
   - [Domain 10: Resource Exhaustion, Algorithmic Complexity & Main-Thread DoS](#domain-10-resource-exhaustion-algorithmic-complexity--main-thread-dos)
   - [Domain 11: Full-Stack, API, Auth & BaaS Security (When Applicable)](#domain-11-full-stack-api-auth--baas-security-when-applicable)
   - [Domain 12: AI / LLM Integration & Prompt Injection (When Applicable)](#domain-12-ai--llm-integration--prompt-injection-when-applicable)
4. [Severity Rating Rubric](#4-severity-rating-rubric)
5. [Standardized Audit Report Template](#5-standardized-audit-report-template)
6. [Copy-Paste Master Prompt for Future Vibe-Coding Audits](#6-copy-paste-master-prompt-for-future-vibe-coding-audits)

---

## 1. Why Vibe-Coded Solutions Have Unique Security Blind Spots

AI-generated applications often look polished on the surface and may even include explicit security helpers (such as a custom DOM builder or a schema validator). However, because code is generated across iterative prompts, vibe-coded projects consistently exhibit specific structural vulnerabilities:

1. **Validator vs. Runtime Desynchronization (Self-Denial-of-Service):**
   An AI adds a strict schema validator for loading saved data (e.g., rejecting strings > 500 chars or arrays > 100 items), but forgets to enforce those same limits in `window.prompt()`, `<input>`, or editing handlers added in another prompt. A user enters 501 characters during normal use, the app saves to `localStorage` or exports a JSON backup, and on the next reload the app's own validator rejects the entire workspace.
2. **Naive "Happy-Path" File Parsers (Multi-Column PII Leakage):**
   When asked to support `.txt` and `.csv` imports, AI often writes `line.split(",")` and imports *every* token. When a real user imports a multi-column CSV from an enterprise system or Student Information System (`Name,ID,Medical/IEP Note,Email`), confidential columns are imported and rendered on screen as primary entities.
3. **Incomplete Privacy / Anonymization Modes:**
   When a "Hide Names", "IDs Only", or "Presentation Mode" toggle is added, the AI updates primary cards/tables to mask PII, but leaves real PII exposed in:
   - Cached validation/error banners generated *before* the toggle was flipped
   - Sequential `.split(name).join(id)` scrubbers that break when a record is renamed/deleted or when a short name is a substring of the replacement token
   - Screen-reader `aria-live` regions, `window.confirm()` dialogs, Undo/Redo stacks, or full JSON backups
4. **Unvalidated Secondary Event Channels:**
   Primary file inputs might be validated, while secondary browser inputs—such as HTML5 Drag-and-Drop (`e.dataTransfer.getData`), `window.postMessage`, `location.hash` / query parameters, or clipboard pastes—are parsed with `JSON.parse()` and used as array indices or object keys without bounds checking, corrupting state or polluting the Undo stack.
5. **Missing Browser-Level Defense-in-Depth:**
   Apps advertised as "100% offline / zero network egress" rarely include a `<meta http-equiv="Content-Security-Policy">` tag with `default-src 'none'; connect-src 'none'` to enforce that guarantee at the browser engine level.

---

## 2. Audit Execution Workflow (5-Phase Methodology)

When auditing any vibe-coded project, execute these five phases in order:

### Phase 1: Architecture & Trust-Boundary Mapping
- Identify all **entry points** (text inputs, `window.prompt`, file uploads, drag-and-drop, URL params, `localStorage`, `IndexedDB`, `postMessage`, API responses, WebSockets).
- Identify all **exit points / sinks** (DOM rendering, `localStorage` writes, CSV/JSON/PDF downloads, clipboard writes, `window.print()`, external `fetch`/`XHR`, database writes).
- Identify all **security & privacy claims** made in the UI/documentation (e.g., *"Offline"*, *"No tracking"*, *"Sensitive tags are never saved"*, *"Anonymous mode hides real names"*) and treat every claim as a testable invariant.

### Phase 2: Automated Static Pattern Scan
Search the codebase for high-risk sinks and anti-patterns:
- **DOM Sinks:** `innerHTML`, `outerHTML`, `insertAdjacentHTML`, `document.write`, `eval(`, `new Function(`, `setTimeout("`, `setInterval("`, `srcdoc`, `.href =`, `.src =`, `style.cssText`
- **Selector Injection:** `querySelector(` or `querySelectorAll(` with string concatenation/interpolation
- **Deserialization & Prototype Pollution:** `JSON.parse(`, `Object.assign(`, spread `{ ...untrusted }`, dynamic bracket assignment `obj[untrustedKey] = ...`
- **Randomness:** `Math.random()`
- **Storage & Egress:** `localStorage`, `sessionStorage`, `indexedDB`, `fetch(`, `XMLHttpRequest`, `navigator.sendBeacon`, `WebSocket`, external `<script src=`, `<link href=`, `@import`

### Phase 3: Schema vs. Runtime Consistency Audit
Compare every constraint enforced on **load/import** (types, string lengths, array sizes, numeric ranges, regexes, uniqueness, invariants like *"disabled seats cannot have an occupant"*) against **every interactive mutation handler** in the UI.

### Phase 4: Privacy, Lifecycle & Edge-Case Tracing
Trace sensitive data from creation -> display -> edit -> anonymization -> undo/redo -> persistence -> export -> deletion ("Clear My Data") to verify zero residual leakage.

### Phase 5: Remediation & Regression Verification
Apply fixes and verify syntax, schema round-tripping, and boundary conditions.

---

## 3. Exhaustive 12-Domain Security Audit Matrix

### Domain 1: DOM Safety, XSS & Client-Side Injection

#### Checklist
- [ ] **Zero unsafe HTML sinks with untrusted data:** Never pass user-controlled, imported, or stored strings into `innerHTML`, `outerHTML`, `insertAdjacentHTML`, or `document.write`.
- [ ] **Safe DOM creation:** Use `document.createElement()`, `node.textContent = ...`, and `document.createTextNode()`.
- [ ] **Attribute & URL scheme validation:** If setting `href`, `src`, `action`, or `formAction` dynamically, validate that the URL parses cleanly and uses an allowlisted protocol (`https:`, `http:`, `mailto:`, or `blob:` generated in-app). Reject `javascript:`, `data:`, and `vbscript:`.
- [ ] **Event handler attribute blocking:** In custom DOM factory helpers (like `el(tag, attrs, children)`), ensure `on*` attributes only attach listeners when the value is a `function`, and never allow arbitrary user-supplied attribute names or string-valued `on*` attributes via `setAttribute`.
- [ ] **CSS Selector Injection:** Never interpolate untrusted IDs or strings directly into `document.querySelector('[data-key="' + key + '"]')` without `CSS.escape(key)`, or filter DOM nodes in JS (`.find(node => node.dataset.key === key)`).
- [ ] **Dynamic Style Injection:** Avoid setting raw `element.style.cssText` or `<style>` tag contents from user input. Bind individual validated properties (`element.style.borderTopColor = ALLOWLIST[idx]`) or CSS custom properties with numeric validation (`Number(scale)`).

#### Vulnerable vs. Hardened Pattern
```javascript
// VULNERABLE: String interpolation in innerHTML and querySelector
container.innerHTML = `<div class="card" data-name="${user.name}">${user.bio}</div>`;
const el = document.querySelector(`[data-name="${user.name}"]`);

// HARDENED: Safe DOM APIs and property comparison
const card = document.createElement("div");
card.className = "card";
card.dataset.name = String(user.name);
card.textContent = String(user.bio);
container.appendChild(card);

const found = Array.from(container.querySelectorAll("[data-name]"))
  .find(node => node.dataset.name === user.name);
```

---

### Domain 2: Schema Validation, State Synchronization & Self-DoS

#### Checklist
- [ ] **Single Source of Truth for Bounds:** Define all maximum lengths and collection capacities as top-level constants (`MAX_TEXT_LEN`, `MAX_DESC_LEN`, `MAX_ITEMS`, `MAX_HISTORY`, `MAX_IMPORT_BYTES`) shared by both the validator and all UI input handlers.
- [ ] **Symmetric Validation (Load == Mutate):** Every rule checked when loading from `localStorage` or importing JSON must also be enforced when creating, editing, or renaming items via `<input>`, `<textarea>`, `window.prompt()`, or drag-and-drop.
- [ ] **HTML Input Constraints:** Add `maxlength`, `min`, and `max` attributes to all corresponding `<input>` and `<textarea>` elements in the markup and dynamic DOM builders.
- [ ] **Atomic Import / Load Validation:** Never mutate live application state while validating an imported payload. Validate into a clean new object first; only swap into live state after validation and initial render succeed, with automatic rollback on render error.
- [ ] **Prototype Pollution Guards:**
  - Validate all IDs/keys against a strict character allowlist (e.g., `/^[a-zA-Z0-9_-]{1,100}$/`) and explicitly reject `"__proto__"`, `"constructor"`, and `"prototype"`.
  - Initialize key-value lookup objects with `Object.create(null)` or use `new Map()`.
- [ ] **Referential Integrity on Load & Delete:** When validating imports or deleting an entity, strip or nullify dangling foreign-key references in groups, seating charts, constraints, and history logs.

#### Vulnerable vs. Hardened Pattern
```javascript
// VULNERABLE: Validator checks 500-char limit on load, but Edit prompt allows unlimited length
// -> App saves 600-char name to localStorage -> Next page reload crashes validateWorkspace()!
const updated = window.prompt("Rename:", item.name);
if (updated) {
  item.name = updated.trim();
  saveToLocalStorage();
}

// HARDENED: Shared constant enforced at mutation time + validator time
const MAX_TEXT_LEN = 500;
const updated = window.prompt("Rename:", item.name);
if (updated && updated.trim()) {
  const trimmed = updated.trim();
  if (trimmed.length > MAX_TEXT_LEN) {
    window.alert(`Name must be ${MAX_TEXT_LEN} characters or fewer.`);
    return;
  }
  item.name = trimmed;
  saveToLocalStorage();
}
```

---

### Domain 3: File Imports, Parsers & Accidental PII Ingestion

#### Checklist
- [ ] **File Size Cap Before Reading:** Check `file.size > MAX_IMPORT_BYTES` (e.g., 5 MB) *before* calling `FileReader.readAsText(file)`.
- [ ] **Async Race Condition Guard:** Capture a workspace generation counter and active context ID before starting `FileReader`. In `reader.onload`, abort if the user switched classes, cleared data, or imported another file while the read was in flight.
- [ ] **Reset File Input Value:** Always reset `e.target.value = ""` so re-importing the same filename triggers the `change` event and does not leave a file reference in the DOM.
- [ ] **RFC-4180 Quote-Aware CSV Parsing:** Never parse CSV lines with a naive `line.split(",")`. Handle double-quoted fields (`"Last, First"`) and escaped quotes (`""`).
- [ ] **Multi-Column CSV PII Protection:** When importing a roster/list from a `.csv` file, detect multi-column tables (via header names like `Name`, `First Name`, `Last Name`, `ID`, `Email`, `Grade`, `Notes`, `IEP`, `504`, or via column data heuristics) and extract **only** the target name column(s). Never dump every column of a multi-column CSV into the primary entity list.

#### Vulnerable vs. Hardened Pattern
```javascript
// VULNERABLE: Splits on every comma and imports confidential columns (IDs, IEP notes) as student names
lines.forEach(line => {
  line.split(",").forEach(part => results.push(part.trim()));
});

// HARDENED: Quote-aware CSV row parser + header/column extraction
// 1. Parse quoted fields properly so "Lin, Maya" stays one field.
// 2. If header row or multi-column structure is detected, extract only the Name or First+Last columns.
```

---

### Domain 4: Data Exports, CSV Formula Injection & Download Safety

#### Checklist
- [ ] **Spreadsheet / CSV Formula Injection (DDE) Escaping:** Any field exported to CSV/TSV that starts with optional whitespace/control characters followed by `=`, `+`, `-`, `@`, `|`, or tab/carriage-return/newline (`\t`, `\r`, `\n`) must be neutralized (e.g., prefixed with a single quote `'`) and wrapped in double quotes with internal `"` doubled (`""`).
- [ ] **Safe Filename Slugification:** Sanitize dynamic download filenames (`slugify(name)`) by stripping path separators (`/`, `\`), leading dots, control characters, and non-alphanumeric symbols, with a safe fallback name.
- [ ] **Blob URL Revocation:** Call `URL.revokeObjectURL(url)` after triggering the download to avoid leaking memory in long-running sessions.
- [ ] **Explicit PII Export Warnings:** When exporting a full JSON backup that bypasses UI anonymization (including real names, tags, notes, and history), display a clear `window.confirm()` warning before downloading.

#### Hardened CSV Cell Escaper
```javascript
function escapeCsvField(val) {
  let str = String(val === null || val === undefined ? "" : val);
  if (/^[\s\u0000-\u001f]*[=+@-|]/.test(str) || /^[\t\r\n]/.test(str)) {
    str = "'" + str;
  }
  if (/[",\n\r]/.test(str)) {
    return '"' + str.replace(/"/g, '""') + '"';
  }
  return str;
}
```

---

### Domain 5: Privacy Modes, Anonymization & Residual State Leaks

#### Checklist
- [ ] **Centralized Display Name Resolver:** Route all user-visible entity names (cards, dropdowns, badges, seating charts, print views, plain-text/CSV exports, and ARIA labels) through a single `getDisplayName(entity)` helper that checks `anonymousMode`.
- [ ] **Single-Pass PII Scrubbing for Dynamic Messages:** If free-text status messages or screen-reader announcements are scrubbed in anonymous mode:
  - Use a **single-pass regular expression** built from regex-escaped entity names sorted longest-first (`new RegExp(patterns.join("|"), "g")`).
  - Never use sequential `.forEach(s => text = text.split(s.name).join(s.anonymousId))`, which corrupts output whenever a short name (e.g., `"Stu"` or `"Student"`) is a substring of the replacement token (`"Student 01"`).
- [ ] **Invalidate Cached Reports on Edit/Delete:** Clear cached validation reports or conflict banners (`lastConstraintReport = null`) whenever an entity is renamed, deleted, or replaced so pre-formatted strings containing old real names cannot persist into anonymous mode.
- [ ] **Clear Transient Inputs & Live Regions on Mode Switch:** When toggling anonymous/privacy mode on, clear search filters, paste textareas, active picker displays, and pending `aria-live` timers/announcements.
- [ ] **Prevent Blind Edits in Anonymous Mode:** Block in-place renaming of real underlying names while anonymous mode is active so users do not accidentally overwrite or expose hidden real names via `window.prompt()` default values.
- [ ] **Hide Sensitive Tags/Notes in Presentation & Anonymous Modes:** Ensure instructional tags, private notes, and sensitive grouping rules are hidden in projector/presentation views and when anonymous mode is active.

---

### Domain 6: Client Storage (`localStorage`, `sessionStorage`, `IndexedDB`)

#### Checklist
- [ ] **Opt-In Persistence for Sensitive Domains:** For K–12, healthcare, financial, or shared-device tools, keep `localStorage` persistence **off by default** and require explicit user opt-in with a clear shared-computer warning.
- [ ] **Data Minimization Before Save:** Strip highly sensitive fields (e.g., instructional tags, private notes, behavioral keep-apart rules) from automatic browser saves even when persistence is enabled, leaving them only in explicit user-controlled file backups.
- [ ] **Immediate Removal on Opt-Out:** Unchecking the persistence toggle must immediately remove the key from `localStorage` (`localStorage.removeItem(STORAGE_KEY)`) and alert the user if removal fails.
- [ ] **Comprehensive "Clear My Data" / Panic Button:**
  - Increment a workspace generation counter to cancel any in-flight `FileReader` or timer callbacks.
  - Clear active intervals/Timeouts (animations, screen-reader announcements).
  - Close any open modals/fullscreen overlays and clear their DOM contents.
  - Remove `localStorage` data inside a `try/catch` and explicitly warn the user if browser storage removal threw an exception.
  - Wipe `undoStack`, `redoStack`, cached reports, and all `<input>` / `<textarea>` / `<input type="file">` values.
  - Reset application state to clean fictional defaults.
- [ ] **Graceful Quota / Storage Failure Handling:** Wrap `localStorage.setItem` and `localStorage.getItem` in `try/catch` blocks (handling `QuotaExceededError`, Safari Private Browsing, or disabled storage policies) and surface a visible status banner without crashing the app.

---

### Domain 7: Untrusted Browser Event Boundaries (Drag & Drop, `postMessage`, URLs)

#### Checklist
- [ ] **Validate Drag-and-Drop (`onDrop`) Payloads:** Never trust `e.dataTransfer.getData("text/plain")`. Even in a self-contained app, a user or external page can drag arbitrary text or JSON into a drop zone, or a grid resize can invalidate an in-flight index.
  - Wrap `JSON.parse(raw)` in `try/catch`.
  - Verify the payload is a non-null object with the expected `type` discriminator.
  - Verify indices are integers within current array bounds (`Number.isInteger(idx) && idx >= 0 && idx < arr.length`).
  - Verify business invariants (e.g., source and destination seats are not disabled, and source !== destination) **before** calling `pushUndo()` or mutating state.
- [ ] **Validate `window.postMessage` (If Used):** Verify `event.origin` against an explicit allowlist and validate `event.data` schema before processing.
- [ ] **Validate URL Parameters / Hash State (If Used):** Treat `location.search` and `location.hash` as untrusted input subject to the same schema validation as imported files.

#### Vulnerable vs. Hardened Pattern
```javascript
// VULNERABLE: Calls pushUndo() and indexes array before validating payload or seat state
onDrop: function (e) {
  const payload = JSON.parse(e.dataTransfer.getData("text/plain"));
  if (payload.type === "seat-move" && payload.fromSeatIndex !== sIdx) {
    pushUndo();
    const fromSeat = seating.seats[payload.fromSeatIndex]; // May be undefined or disabled!
    seat.studentId = fromSeat.studentId;
  }
}

// HARDENED: Full bounds and invariant check prior to pushUndo() or mutation
onDrop: function (e) {
  e.preventDefault();
  if (seat.disabled) return;
  const raw = e.dataTransfer.getData("text/plain");
  if (!raw) return;
  try {
    const payload = JSON.parse(raw);
    const fromIdx = Number(payload && payload.fromSeatIndex);
    const fromSeat = Number.isInteger(fromIdx) && fromIdx >= 0 && fromIdx < seating.seats.length
      ? seating.seats[fromIdx]
      : null;
    if (payload && payload.type === "seat-move" && fromSeat && !fromSeat.disabled && fromIdx !== sIdx) {
      pushUndo();
      const tmp = seat.studentId;
      seat.studentId = fromSeat.studentId;
      fromSeat.studentId = tmp;
      persistIfEnabled();
      renderSeatingView(cls);
    }
  } catch (err) { /* Ignore malformed drag payload */ }
}
```

---

### Domain 8: Content Security Policy (CSP), Network Egress & Supply Chain

#### Checklist
- [ ] **Enforce Offline / Zero-Egress via CSP Meta Tag:** For standalone/offline HTML apps, include a strict `<meta http-equiv="Content-Security-Policy">` tag in `<head>` that blocks all external connections, forms, plugins, and base-URI hijacking:
  ```html
  <meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; img-src data:; connect-src 'none'; form-action 'none'; base-uri 'none';" />
  ```
  *(If inline scripts/styles can be externalized or hashed, replace `'unsafe-inline'` with `'self'` or `'sha256-...'` hashes.)*
- [ ] **Zero Hidden Network Dependencies in Offline Apps:** Verify there are no external Google Fonts (`fonts.googleapis.com`), CDN scripts (`unpkg.com`, `jsdelivr.net`, `cdnjs.cloudflare.com`), external images, or analytics beacons that leak client IP/User-Agent metadata when opened.
- [ ] **Subresource Integrity (SRI) for Online Apps:** If an online app *must* load third-party CDN assets, pin exact versions and require `integrity="sha384-..."` and `crossorigin="anonymous"`.

---

### Domain 9: Cryptography, Randomness (CSPRNG) & ID Generation

#### Checklist
- [ ] **Use `crypto.getRandomValues` Instead of `Math.random()`:** Use the Web Crypto API for generating entity IDs, session tokens, and fairness-critical shuffling (such as student picking, role rotation, or randomized group assignment).
- [ ] **Eliminate Modulo Bias with Rejection Sampling:** When mapping a random `Uint32Array` value to `[0, maxExclusive)`, use rejection sampling rather than `buf[0] % maxExclusive`:
  ```javascript
  function secureRandomInt(maxExclusive) {
    if (maxExclusive <= 1) return 0;
    if (window.crypto && typeof window.crypto.getRandomValues === "function") {
      const limit = Math.floor(0xffffffff / maxExclusive) * maxExclusive;
      const buf = new Uint32Array(1);
      let val;
      do {
        window.crypto.getRandomValues(buf);
        val = buf[0];
      } while (val >= limit);
      return val % maxExclusive;
    }
    return Math.floor(Math.random() * maxExclusive);
  }
  ```
- [ ] **Unbiased Fisher–Yates Shuffle:** Never sort arrays with `.sort(() => Math.random() - 0.5)` (which is both biased and non-cryptographic). Always use Fisher–Yates with `secureRandomInt(i + 1)`.

---

### Domain 10: Resource Exhaustion, Algorithmic Complexity & Main-Thread DoS

#### Checklist
- [ ] **Bound History & Log Arrays at Runtime and Import Time:** Cap growing arrays (`undoStack`, `redoStack`, `pairingHistory`, `roleHistory`, `savedSnapshots`, audit logs) using `.shift()` or `.splice()` when pushing new entries, and enforce the same cap in the import validator.
- [ ] **Cap Synchronous DOM List Rendering:** Never synchronously render thousands of historical log entries on every `renderAll()` cycle. Slice to the most recent $N$ items (e.g., 100) with a summary indicator, or paginate/virtualize.
- [ ] **Bound Constraint / Optimization Loops:** Any randomized solver, backtracking search, or graph/clique check (e.g., pigeonhole conflict detection) must have a hard iteration budget (e.g., `trials <= 220`, `MAX_ROSTER_SIZE <= 500`) so worst-case inputs cannot hang the main UI thread.
- [ ] **Avoid ReDoS (Regular Expression Denial of Service):** Do not construct regular expressions with nested quantifiers (e.g., `(a+)+`) or unescaped user input. Always escape user strings with `str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")` before building a `RegExp`.

---

### Domain 11: Full-Stack, API, Auth & BaaS Security (When Applicable)

For vibe-coded applications that include a backend (Node/Express, Next.js, FastAPI, Go) or Backend-as-a-Service (Supabase, Firebase, Convex):

- [ ] **Never Trust Client-Side Auth Guards Alone:** UI route guards (`if (!user.isAdmin) return <Redirect />`) provide zero security unless every backend API endpoint and database query enforces authentication and authorization server-side.
- [ ] **Row-Level Security (RLS) & BOLA/IDOR Prevention:**
  - In Supabase/Postgres, verify `ENABLE ROW LEVEL SECURITY` is active on every table and policies check `auth.uid() = user_id` or tenant membership.
  - In Firebase, verify Firestore/Storage security rules reject unauthenticated or cross-tenant reads/writes (`allow read, write: if true;` is a critical vulnerability).
  - In REST/GraphQL APIs, always scope queries by the authenticated session's user/org ID (`WHERE id = $1 AND org_id = $2`), never by a client-supplied `userId` parameter alone.
- [ ] **Parameterized Queries / Injection Prevention:** Never concatenate user input into SQL, NoSQL (`$where`), shell commands (`child_process.exec`), or file paths (`path.join` without `path.resolve` prefix verification).
- [ ] **Secrets Hygiene:** Verify `.env` files are in `.gitignore`, no private API keys (`OPENAI_API_KEY`, `SUPABASE_SERVICE_ROLE_KEY`, `STRIPE_SECRET_KEY`) are bundled into client-side code (`NEXT_PUBLIC_*`, `VITE_*`, or inline `<script>`), and any key ever committed to git history is rotated.
- [ ] **Rate Limiting & CORS:** Restrict `Access-Control-Allow-Origin` to trusted origins, validate `Content-Type`, enforce request body size limits, and rate-limit authentication and expensive compute endpoints.

---

### Domain 12: AI / LLM Integration & Prompt Injection (When Applicable)

For vibe-coded apps that call LLMs or act as AI agents:

- [ ] **Indirect Prompt Injection Defense:** Treat all external content (uploaded documents, scraped web pages, database records, emails, student notes) as untrusted data. Delimit untrusted content clearly and never allow LLM output from untrusted context to trigger privileged tool calls, database mutations, or raw HTML/Markdown rendering without sanitization.
- [ ] **Structured Output Validation:** Validate all JSON returned by an LLM against a strict schema (e.g., Zod or allowlisted validator) before rendering or executing downstream logic.
- [ ] **Client-Side Proxy for LLM Keys:** Never call paid LLM APIs directly from browser JavaScript using a hardcoded bearer token; route through an authenticated backend with per-user quota caps.

---

## 4. Severity Rating Rubric

| Severity | Criteria | Examples |
| :--- | :--- | :--- |
| **Critical** | Remote Code Execution, arbitrary Cross-Site Scripting (XSS) in shared contexts, exposed secret/service-role keys, or unauthenticated access to sensitive multi-tenant data. | `innerHTML` with untrusted user input; hardcoded `SERVICE_ROLE_KEY`; Firestore `allow read, write: if true`. |
| **High** | Direct PII exposure across trust boundaries, broken authorization (IDOR/BOLA), SQL/command injection, or bypass of primary security controls. | Multi-tenant API missing ownership check; `eval()` on imported config; persistent XSS via imported file. |
| **Medium** | Self-Denial-of-Service (state corruption on save/reload), accidental confidential column ingestion during file import, or incomplete PII masking in privacy modes. | Runtime UI edits exceeding load-validator bounds; CSV importer dumping all SIS columns into public cards. |
| **Low** | Local UI crashes on malformed secondary events (drag-and-drop), minor residual PII in cached banners after edits, or UI freezes on large valid files. | Unchecked `fromSeatIndex` in `onDrop`; sequential string replacement bug in anonymous mode; rendering 10,000 history rows synchronously. |
| **Informational** | Missing defense-in-depth hardening where primary controls already exist, or minor edge-case escaping improvements. | Missing offline `<meta http-equiv="Content-Security-Policy">`; adding `\|` to CSV formula escaper. |

---

## 5. Standardized Audit Report Template

Use this structure when presenting audit results for any vibe-coded project:

```markdown
# Security & Privacy Audit Report: [Project Name]

## 1. Executive Summary
- **Application Type:** [Single-file offline HTML/JS | React SPA | Next.js Full-Stack | etc.]
- **Overall Posture:** [Summary of baseline strengths and highest-severity risks]
- **Findings Count:** [X Critical, X High, X Medium, X Low, X Informational]

## 2. Verified Positive Security Controls
- **[Control Area]:** [Brief description with file and line references]

## 3. Detailed Findings

### [Finding #1] [Severity] Title of Finding
- **Location:** `path/to/file.ext:L100-L125`
- **Vulnerability Category:** [e.g., Schema Validation Desynchronization / Self-DoS]
- **Description:** [How the code works and why the vulnerability occurs]
- **Impact:** [Concrete impact on confidentiality, integrity, availability, or privacy]
- **Remediation:**
  ```javascript
  // Recommended code fix
  ```

## 4. Verification & Regression Checklist
- [ ] Syntax and build verification passed
- [ ] Schema validator limits match all UI mutation handlers
- [ ] Untrusted file imports (CSV/JSON) tested with malformed, oversized, and multi-column payloads
- [ ] Privacy / Anonymous mode verified across edits, deletes, exports, and screen-reader announcements
```

---

## 6. Copy-Paste Master Prompt for Future Vibe-Coding Audits

Copy and paste the prompt below into your AI coding assistant whenever you want an exhaustive security audit and automated fix of any vibe-coded project:

```text
Perform an exhaustive security and privacy code audit of this project using the 12-Domain Methodology in ~/Desktop/agysecurity.md:

1. Map all trust boundaries, entry points (inputs, prompts, file imports, drag-and-drop, URL params, storage, APIs), and exit sinks (DOM, storage, CSV/JSON/print exports, network).
2. Check Domain 1 (DOM XSS, innerHTML, attribute/URL/CSS selector injection).
3. Check Domain 2 (Schema validation vs. runtime mutation synchronization: ensure every length/count/range limit checked on load or import is also enforced on interactive edits, prompts, and inputs so the user cannot trigger a self-DoS on reload or backup restore; verify prototype pollution guards).
4. Check Domain 3 (File imports & parsers: file size caps, async race guards, quote-aware CSV parsing, and multi-column CSV protection so confidential metadata columns are not imported as primary display items).
5. Check Domain 4 (Exports: CSV formula/DDE injection escaping for =, +, -, @, |, tab, CR, LF; safe filenames; PII export warnings).
6. Check Domain 5 & 6 (Privacy/Anonymous modes, single-pass PII scrubbing, invalidating cached error banners on edit/delete, opt-in localStorage minimization, and complete panic/Clear My Data cleanup).
7. Check Domain 7, 8, 9, 10 (Drag-and-drop/postMessage payload bounds checking before Undo/mutation, strict Content-Security-Policy meta tag / zero external egress, CSPRNG with rejection sampling, and history/DOM rendering caps to prevent main-thread freezes).
8. If the project has a backend, BaaS, or LLM integration, check Domains 11 & 12 (server-side authz, RLS/IDOR, secrets exposure, prompt injection).

First, present a prioritized security audit report with exact file and line references. Then, upon confirmation (or immediately if requested), remediate all findings and verify that the code parses and runs cleanly.
```
