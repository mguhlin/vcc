## Modern Web Guidance

Modern Web Guidance helps an assistant choose browser features that fit the job. VCC incorporates its native-control, responsive-layout, performance, and compatibility approach into the downloadable Web Design instructions and the `vcc-web-design` skill.

Start with the browsers and devices your audience actually uses. Prefer an appropriate native control or CSS layout, check its current support, and keep the essential task usable when an enhancement is unavailable. A newer API is useful when it simplifies the task and preserves access.

- **Controls:** consider native dialogs and disclosure controls before rebuilding their behavior. Verify names, focus, dismissal, keyboard use, and unsaved-work recovery.
- **Layout and text:** use content-driven layout and relative text sizing. Consider container queries for reusable components and dynamic viewport units where browser chrome affects the available height. Try large text and narrow screens.
- **Loading and responsiveness:** reserve image space, prioritize the actual important image, defer suitable offscreen media, and investigate measured interaction delays.
- **Compatibility:** consult current Baseline and browser-support information for each chosen feature. Use feature detection and a usable fallback; preserve intentional compatibility code.

### A modernization prompt

> Use VCC's Web Design instructions and its Modern Web Guidance section to review this project's existing frontend. Identify the intended browser/device range, then find a small number of changes that could simplify controls, improve responsive layout, or address a measured loading or interaction problem. Consult the relevant current upstream guides and verify compatibility. Preserve deliberate fallbacks and working interactions. Apply only the modernization work I have requested, use the existing authorized tools, and verify the main task, keyboard behavior, text scaling, narrow-screen layout, and relevant performance evidence. Report any checks not run.

VCC's practical selection and testing workflow paraphrases guidance from the [Modern Web Guidance contributors](https://github.com/GoogleChrome/modern-web-guidance-src), whose guide documentation is [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Read the [official documentation](https://developer.chrome.com/docs/modern-web-guidance) and [modernization workflow](https://developer.chrome.com/docs/modern-web-guidance/modernization-workflow). The [distribution repository](https://github.com/GoogleChrome/modern-web-guidance) provides the upstream installation options; the source repository contains authoring templates. VCC includes its own adaptation and source links. No upstream executable code, installer, or CLI is bundled or run by this page.

If you separately choose the upstream CLI, review its installation and [telemetry documentation](https://github.com/GoogleChrome/modern-web-guidance-src#telemetry--privacy). Its README describes `DISABLE_TELEMETRY=1`; private project or student content should stay out of external tool queries. Reading the linked guides does not require installing that CLI.
