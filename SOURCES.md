# Sources and editorial decisions

## Core components

- `securevcc/`: migrated from Miguel Guhlin’s `mguhlin/creations` SecureVCC folder. The original security guidance, source Markdown, upstream ZIP, license, and source notes are retained. Its local landing route now points to the VCC security guide.
- `WEB_DESIGN.md`: supplied by Miguel Guhlin. Its maintenance date was removed for publication; its operational guidance is retained.
- `EDU_COMPLIANCE.md`: supplied by Miguel Guhlin. Its maintenance-date frontmatter was removed for publication; its operational guidance is retained.
- The two explanatory images were supplied with those files. The hero was generated for VCC; see `assets/hero-prompt.txt`.
- Project brief, launch review, and prompt pack extend those guides into practical educator workflows.

## Blog context

Both local authoring files were read, including their publication metadata and article bodies:

- [Securing Your Vibe-Coded Creation](https://mguhlin.org/blog/2026-11-08-securing-your-vibe-coded-creation/): use a reusable security instruction file; the article links to SecureVCC and Cloudflare’s source skill.
- [Stop Letting AI Make Every Website Look the Same](https://mguhlin.org/blog/2026-11-10-stop-letting-ai-make-every-website-look-the-same/): match structure to function, provide design references, and build accessibility and privacy into the workflow. VCC links to the companion article from its supplemental blog page and does not reproduce the full essay.

The article names and dates in their URLs are stable content identifiers, not VCC maintenance timestamps.

## Illustrated walkthroughs

Miguel Guhlin supplied `cartoon_github.png`, `cartoon_netlify.png`, and `Vibe-Coding Center_ Three Essential Checks.png`. VCC preserves the originals in `assets/cartoons/` and uses WebP copies for page display. The classroom-sharing guide includes the three-checks cartoon; the publishing walkthroughs pair the other cartoons with text versions and current official GitHub Pages and Netlify documentation. Cloudflare is identified as optional, and the Netlify action links to the service's actual Drop page rather than relying on the address drawn in the cartoon.

## Supplemental resources

The supplied `AI_Git_Hub.csv` contained 16 bookmarks. Tracking parameters and exported bookmark metadata are excluded from VCC’s public recommendations. Every bookmark has a decision in [RESOURCE_REVIEW.md](RESOURCE_REVIEW.md), with additional primary design and test references. The homepage shelf is narrower than that historical ledger; its optional additions are Gitleaks, ZAP, and Accessibility Insights for Web, each explicitly distinguished from references already named in the core instructions. Repository metadata and READMEs were read through GitHub; no recommended software was installed or executed for vetting.

## Official guidance consulted

These are reference points, not endorsements or compliance certifications. The full education guide has the broader source list. Recheck applicability and current text for each actual project.

- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/): testable accessibility criteria, with manual testing still necessary.
- [U.S. Department of Education: FERPA school-official exception](https://studentprivacy.ed.gov/faq/who-school-official-under-ferpa): outsourcing education-record services involves specific conditions, not a generic software approval.
- [FTC COPPA FAQs](https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions): follow the FTC’s linked revised Rule for current requirements. A school context does not remove all operator responsibilities.
- [Official GDPR text](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng): the primary legal source is linked, but automated retrieval encountered a browser verification challenge. VCC does not make a new legal interpretation from an unread page.
