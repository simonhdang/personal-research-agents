---
description: Create a new research project folder from the template, with its own CLAUDE.md, reference group and Notion tracker.
argument-hint: [short project name]
---

# /new-project

1. Ask (skip what `$ARGUMENTS` or context already gives): working title, research question, design (experiment / survey / PLS-SEM / mixed), target journal and backups, coauthors, start date, deadline if any.
2. Slug: `<YYYY>-<2-4 word kebab-case>`. Copy `projects/_template-project/` to `projects/<slug>/` (cp -R).
3. Fill `projects/<slug>/CLAUDE.md` and `status.md` (stage: Idea or Design).
4. Set up the reference library (see `projects/<slug>/library/README.md`):
   - **One library per project (EndNote):** ask whether to bring an existing library or start a new one. Walk the researcher through closing EndNote, copying both `<name>.enl` and `<name>.Data/` into `projects/<slug>/library/` (or keeping it in a non-synced folder if Documents is cloud-synced), opening it from there from now on, and exporting XML into `library/`. If a draft already cites a master library, advise copying that whole library so record numbers stay valid.
   - **Shared library:** ask them to create a group or collection named `<slug>`.
   - Record the manager, library path, export path and export date in the project's `CLAUDE.md` > Reference library, then test-read the export with `python3 .claude/scripts/cite_check.py --library <export> --draft projects/<slug>/refs.md`.
5. If an idea card in `vault/knowledge/` (type: idea) started this project, link it and set the card's status.
6. Create the Projects row in Notion (notion-sync skill) and initial Tasks.
7. Log in the project log and `vault/log.md`; add the project to `vault/index.md`.
8. Suggest the next step (literature review, theory, or design).
