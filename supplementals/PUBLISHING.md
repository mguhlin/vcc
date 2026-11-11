# Publishing walkthroughs

Follow an exit-ticket project from an AI prompt to a link you can open in a browser. Choose GitHub Pages for a repository-based workflow or Netlify Drop for a manual upload of site files.

Open either cartoon at full size to read its panels. The text walkthroughs below describe the same sequence. Use invented answers while testing; leave out the illustrated name field when the activity works without it.

## GitHub Pages

[![Five-panel cartoon of a teacher prompting an AI, generating an exit ticket, uploading its files to GitHub, enabling GitHub Pages, and optionally adding a Cloudflare-managed custom domain.](../assets/cartoons/github-pages.webp)](../assets/cartoons/github-pages.png)

[Open full-size GitHub cartoon](../assets/cartoons/github-pages.png) · [Download original GitHub PNG](../assets/cartoons/github-pages.png)

### The GitHub cartoon in text

1. **Ask an AI for help.** A teacher describes a simple, privacy-conscious exit ticket for a class.
2. **Generate the tool.** The assistant produces HTML, CSS, and JavaScript. The teacher saves an `index.html` entry file and its supporting files.
3. **Put the files on GitHub.** Upload the site files to a repository and commit the change.
4. **Turn on GitHub Pages.** In the repository's Pages settings, choose the publishing source that contains the entry file. Open the resulting site URL and test it.
5. **Optionally add a custom domain.** The cartoon uses Cloudflare for this step. A custom domain and Cloudflare are optional; GitHub Pages already supports HTTPS. Review the classroom journey before sharing the link.

For the service's current controls, use [GitHub's Pages setup instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site) and [HTTPS guidance](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https).

## Netlify Drop

[![Five-panel cartoon of a teacher prompting an AI for an exit ticket, generating HTML, CSS, and JavaScript, saving the files together, dropping the site folder into Netlify, and opening the shared link.](../assets/cartoons/netlify.webp)](../assets/cartoons/netlify.png)

[Open full-size Netlify cartoon](../assets/cartoons/netlify.png) · [Download original Netlify PNG](../assets/cartoons/netlify.png)

### The Netlify cartoon in text

1. **Describe the activity.** Ask the assistant for an exit ticket with a clear learning task.
2. **Generate and test the tool.** Review the HTML, CSS, and JavaScript with invented answers.
3. **Save the project files together.** A simple static site can contain `index.html`, `style.css`, and `script.js`. For a project with a build step, build locally and use the finished output folder.
4. **Upload the site folder.** Open [Netlify Drop](https://app.netlify.com/drop) and drag the folder containing the deployable site files into its upload area. The cartoon's browser labels are illustrative; use this link to reach the service.
5. **Open and review the site.** Test the resulting URL on the devices your learners will use before sharing it. For later changes, upload the updated output folder through the existing site's Deploys page.

Manual uploads do not run a build command for you. See [Netlify's deployment instructions](https://docs.netlify.com/deploy/create-deploys/#drag-and-drop) for its current workflow.

## Check before sharing

Use [Three checks before you share](../guides/before-sharing.html#three-checks-before-you-share) to review education privacy, security, and design for function. Keep your evidence in [the launch review](../guides/launch.html).
