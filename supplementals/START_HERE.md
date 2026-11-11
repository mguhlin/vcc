# From idea to first review

Start with one useful task, invented examples, and a person responsible for release decisions. Use this page alongside the three core guides.

## Describe one useful learning task

For example: “A teacher can create a printable vocabulary activity without signing in or entering student names.” Set the audience, the data boundaries, and the evidence you want before asking for code.

## What is PROJECT_BRIEF.md?

`PROJECT_BRIEF.md` is **your project's plan**, separate from the three instruction files. It records what you want to build, who it serves, what information it needs, and how you will know it works. `WEB_DESIGN.md` tells the assistant how to approach design; the brief tells it what this particular project needs.

1. [Download the project brief template](../templates/PROJECT_BRIEF.md).
2. Save it in your project's main folder as `PROJECT_BRIEF.md`.
3. Replace its questions with your decisions. Mark unknowns clearly and keep student information out of it.

[Read the project brief guide](../guides/project-brief.html) for the full template and its questions.

## Put the instructions in your project

Download these files into the same main folder:

- [WEB_DESIGN.md](../WEB_DESIGN.md): design, structure, and interaction guidance.
- [EDU_COMPLIANCE.md](../EDU_COMPLIANCE.md): education privacy, accessibility, and school-review guidance.
- [securevcc.md](../securevcc/securevcc.md): security review guidance. Save this file as `securevcc.md` at the project root.

Your folder should contain:

```text
your-project/
  PROJECT_BRIEF.md      Your completed project plan
  WEB_DESIGN.md         Design instructions
  EDU_COMPLIANCE.md     Education privacy instructions
  securevcc.md          Security instructions
```

Attach the files to your AI conversation if your assistant cannot read local files. A filename alone does not activate a guide.

## Ask the assistant to read and apply them

Complete the brief first, then copy this prompt. For ongoing work, add the pointer from [AGENTS.example.md](../templates/AGENTS.example.md) or [CLAUDE.example.md](../templates/CLAUDE.example.md) to your existing project instructions.

### A starting prompt you can reuse

> Read my completed PROJECT_BRIEF.md (the project plan), WEB_DESIGN.md (design instructions), EDU_COMPLIANCE.md (education privacy instructions), and securevcc.md (security instructions) before changing this project. If the brief is missing, help me create it from VCC's project brief template before writing code. Start with the educational purpose, audience, and actual data flows. Choose a layout that fits the task. Build with invented sample data and privacy-protective defaults. Test the main journey, keyboard access, mobile reflow, and relevant security controls. Report evidence, unresolved questions, and checks you could not run. Do not claim school approval or compliance without proof.

[Open the full prompt pack](../guides/prompts.html) for redesign, accessibility, security, and release prompts.

## Test, document, and get the right approval

Try the actual educator or learner task. Ask for evidence of security and accessibility checks. If student records or sensitive features are involved, resolve school and vendor requirements before use.

Use [Before you share with a class](../guides/before-sharing.html) for quick reminders and [the launch review](../guides/launch.html) to record evidence and unresolved decisions.
