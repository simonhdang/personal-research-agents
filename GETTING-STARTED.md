# Getting started

No terminal needed. Do steps 1-4, then run `/setup`.

## 1. Make your own copy
Duplicate this whole folder and keep the original as a clean template. Work only in your copy.

## 2. Drop your materials into `inbox/`
No sorting or renaming needed; the agents classify everything. Useful materials:
- Your CV
- Your LinkedIn data export (Settings > Data privacy > Get a copy of your data) or a PDF of your profile
- 3-5 papers you wrote mostly yourself (used to learn your writing style)
- Slides, posters, IRB protocols, grant proposals, codebooks

**Past manuscripts are the one exception:** put each in its own subfolder under `inbox/manuscripts/` (any name) with every version, decision letter, reviewer report and response letter for it.

## 3. Add target journals (optional)
Copy `vault/journals/_template-journal.md` for each journal, or just list journal names when /setup asks.

## 4. Check your connections
In Claude Code on your computer, enable the Notion connector (required for trackers) and, optionally, Gmail and Google Calendar.

## 5. Install the analysis tools (one time, optional until your first analysis)
- R: https://cran.r-project.org (normal installer)
- Quarto: https://quarto.org (normal installer)
/setup checks both and installs the small Python packages it needs after asking you.

## 6. Run /setup
Always open Claude Code at this top-level folder, then type `/setup`. It will:
1. Read everything in `inbox/` and your public profiles (ORCID/OpenAlex, faculty page).
2. Ask which email account and reference manager to use, explaining each option.
3. Draft `soul.md`, `vault/owner/`, coauthor pages and journal profiles, and show them before saving.
4. Process your past manuscripts and build the first `vault/reviews/lessons.md`.
5. Offer starter no-go rules (you accept, edit, or drop each).
6. Create the Notion trackers and check that R and Quarto are installed.

## Day to day
| You want to | Do this |
|---|---|
| Start a study | `/new-project` (it walks you through copying your EndNote library into the project's `library/` folder) |
| Add anything new (reviews, papers, data, notes, a link) | Drop it in `inbox/` or the project's `submissions/_drop/`, then `/update` |
| Pull in outside changes (new publications, citations, journal guidelines) | `/update --refresh` |
| Finish a project | `/close-project` |
| Anything else | Tell the Orchestrator in plain language |
