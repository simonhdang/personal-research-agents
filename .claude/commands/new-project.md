---
description: Create a new research project folder from the template, with its own CLAUDE.md, reference group and Notion tracker.
argument-hint: [short project name]
---

# /new-project

1. Ask (skip what `$ARGUMENTS` or context already gives): working title, research question, design (experiment / survey / PLS-SEM / mixed), target journal and backups, coauthors, start date, deadline if any.
2. Slug: `<YYYY>-<2-4 word kebab-case>`. Copy `projects/_template-project/` to `projects/<slug>/` (cp -R).
3. Fill `projects/<slug>/CLAUDE.md` and `status.md` (stage: Idea or Design).
4. Ask the researcher to create a group/collection named `<slug>` in their reference manager; record its name in the project CLAUDE.md.
5. If an idea card in `vault/knowledge/` (type: idea) started this project, link it and set the card's status.
6. Create the Projects row in Notion (notion-sync skill) and initial Tasks.
7. Log in the project log and `vault/log.md`; add the project to `vault/index.md`.
8. Suggest the next step (literature review, theory, or design).
