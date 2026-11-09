---
description: First-run onboarding: builds your researcher profile, picks your reference manager and email, creates Notion trackers, and processes past manuscripts. Re-run one part with /setup references | soul | accounts | notion | journals.
argument-hint: [part]
---

# /setup

Guide the researcher one step at a time. Wait for answers. If `$ARGUMENTS` names a part (references, soul, accounts, notion, journals, tools), run only that step.

Tell the researcher at the start: everything is drafted first and saved only after their approval; nothing is sent or deleted.

## Step 1: Tools check
- Check `python3`, the python packages in `.claude/scripts/requirements.txt`, `R`/`Rscript` and `quarto` (use `which` and a version call).
- For anything missing, explain in one line what it is for and ask before installing (pip packages; R packages later on first use). For R and Quarto, give the download pages (https://cran.r-project.org and https://quarto.org) since they use normal installers.
- Check which connectors are available (ToolSearch for notion, gmail, calendar, openalex, consensus) and report what is and isn't connected. Missing connectors don't stop setup.

## Step 2: Accounts
Ask, then write `config.md` > Accounts:
1. Which email account holds publication and coauthor correspondence? (Search only that account.)
2. What may agents search for in it? Propose a scope (journal names, editorial-system senders such as ScholarOne and Editorial Manager, coauthor names, "manuscript", "reviewer") and let the researcher edit it.
3. ORCID iD, faculty page, personal website, Google Scholar link.

## Step 3: Reference manager
Explain the three options in one table, then ask which one they use:

| | EndNote | Zotero | Mendeley |
|---|---|---|---|
| How agents read it | An XML export you refresh (File > Export > XML) | Zotero 7 local API or a Better BibTeX auto-export | A BibTeX/RIS export |
| Can agents add records? | No: they prepare a .ris + PDF in `to-import/`, you import | Yes, with your approval each time | No: you import |
| Citations in Word | `{Author, Year #RecNum}`, formatted by Cite While You Write | `[@key]` or `{Author, Year}` | `{Author, Year}` |
| Setup effort | Low | Medium (install Better BibTeX) | Low |

Then ask how libraries are organized:
- **One library per project** (good for EndNote): each project keeps its `.enl` + `.Data/` folder and XML export in `projects/<name>/library/`; /new-project sets it up.
- **One shared library**: one export recorded in `config.md`; each project uses a group or collection.
Mention the cloud-sync caution: EndNote libraries should not live in iCloud, Dropbox or OneDrive folders.

Write the choice, library layout, export path (shared library only) and citation format to `config.md` > Reference manager. Run `python3 .claude/scripts/cite_check.py --library <export> --draft <any small .md with one citation>` to confirm the export can be read.

## Step 4: Gather and extract
1. Read everything in `inbox/` (not `inbox/manuscripts/` yet): CV, LinkedIn export, own papers, slides, IRB, grants.
2. Pull the publication list and coauthors from OpenAlex using the ORCID iD.
3. Fetch the faculty page and website.
4. With explicit permission, search the publications email within the agreed scope for submission history and active coauthors, and the calendar for recurring coauthor meetings. Never store private or family content.
5. Show a short list of what was read.

## Step 5: Draft the profile
Draft, with a source tag on each line (e.g. `[CV]`, `[OpenAlex]`, `[paper: 2024 JRCS]`):
- `soul.md` (all 9 sections, about one page),
- `vault/owner/research-profile.md`, `vault/owner/style-profile.md` (measured from 3+ own papers per `.claude/skills/paper-writing/references/style_calibration_protocol.md`),
- `vault/publications.md`, coauthor pages in `vault/people/` and the collaborator table in `vault/index.md`.
Then interview only for what documents cannot show (3-6 questions): theories they avoid, what counts as a contribution, how much autonomy agents get and what they must always ask about, output preferences.
Show the drafts. Save soul.md and `vault/owner/` only after explicit approval (the guard will ask the researcher to confirm each write).

## Step 6: No-go rules
Offer the starter rules in `vault/owner/no-go.md` one by one (accept / edit / drop) and ask for any others. Save after approval.

## Step 7: Journals
Ask which journals they target. Create `vault/journals/<slug>.md` from the template for each (scope, tier, word limit, reference style from the journal's guide for authors, with the source URL). Remove example stubs they don't want by moving them to `vault/journals/_archive/`.

## Step 8: Past manuscripts
If `inbox/manuscripts/` has folders, run the /update procedure on them (update-routing skill): archive projects, ledger, first version of `vault/reviews/lessons.md`. Report the top lessons found.

## Step 9: Notion
Follow `.claude/skills/notion-sync/SKILL.md` > Bootstrap. Save IDs to `config.md` > Notion. Add rows for archived manuscripts to Submissions.

## Step 10: Scheduled automations (optional)
Offer the three v1 automations: daily decision-email watcher, Monday research brief, weekly literature watch. If accepted, explain they run as Claude scheduled tasks that only read and draft, and set them up with the scheduling tools available in this session (or give the researcher the prompts to schedule: "Run /status --brief", "Run the scout decision-email watcher", "Run the scout literature watch").

## Finish
Log `## [YYYY-MM-DD HH:MM] setup | completed` in `vault/log.md`. Summarize what was created and the next step (`/new-project` or `/update`).
