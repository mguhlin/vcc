# Vibe-Code Rescue sources and adaptation

Miguel Guhlin supplied `vibe-code-rescue-skill.zip`, containing one Markdown skill. VCC adapts its four foundations: reproducible setup, diagnosable failures, protected operations, and maintainable change boundaries. The ZIP was read as text; no code or installation steps from it were executed.

## Source identity

SHA-256 identifies the supplied bytes; it does not establish source trust or grant a license.

```text
eab27ea44bcf70729edeb0511b1cb3823f7f550aec38705dcde89f9653a6ed73  vibe-code-rescue-skill.zip
2af614db64509d4663b5bbdc690cd871a02f4e25e078598d144b647a1752d220  vibe-code-rescue/SKILL.md
```

The original archive is not a second maintained download. Its source identity is recorded here; VCC's adapted Markdown is the maintained version. No separate license notice was present in the supplied archive. VCC's original explanatory additions and vector artwork follow its educational-prose CC BY 4.0 terms. External sources retain their own rights; the article below is linked, not reproduced.

## How VCC divides the material

- [SecureVCC](../securevcc/securevcc.md) incorporates the security-repair baseline, reproducible review setup, and privacy-preserving diagnostic checks. Existing detailed permissions, exposed-credential response, synthetic validation, and realistic severity rules remain in place. SecureVCC retains its MIT notice.
- [Vibe-Code Rescue](VIBE_CODE_RESCUE.md) keeps troubleshooting, repair, release-gate, and repair/rebuild/retire triage workflows in a separate self-contained file. It includes minimum safety rules and points to SecureVCC for detailed audits.
- The adaptation respects authorization already established by the user and repository, preserves unrelated work, separates uncertainty from severity, and removes maintenance-date fields from report templates. A release verdict does not grant publication permission.
- The four-part illustration originated as VCC vector artwork and has a colorful generated revision representing a recovery workflow. It is not a screenshot or test result.

## Reference material

The supplied skill attributes its four-foundation framing to [MakeUseOf's article about recurring problems in vibe-coded apps](https://www.makeuseof.com/fix-vibe-coded-apps-for-a-living-and-these-mistakes-keep-coming-back/). Retrieval of that article was unavailable; VCC does not present it as independently verified technical evidence or reproduce its prose.

Official references read for the technical adaptation:

- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html): enforce permissions at the trusted boundary on each request and validate allowed/denied cases.
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html): exclude sensitive values, sanitize logs, and test logging failures without information disclosure.
- [GitHub: Removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository): revoke or rotate exposed credentials first; history rewriting has separate coordination risks.

The colorful workbench artwork was generated as an edit of the original VCC SVG and includes a red plus coding-repair toolkit. Pages use `assets/rescue-workbench.webp`; `assets/rescue-workbench.svg` remains a self-contained compatibility image at its stable URL. The original vector is preserved at `assets/art-source/rescue-workbench-original.svg`. Image prompts are in `assets/ARTWORK_PROMPTS.json`.
