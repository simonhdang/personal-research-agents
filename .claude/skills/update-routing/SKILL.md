---
name: update-routing
description: Classify anything new (files in inbox/ or a project's submissions/_drop/, pasted text, links), file it where it belongs, code reviewer comments into the ledger, update review lessons, and harvest finished projects. Use for /update, /update --refresh and /close-project.
---

# Update routing

## Collect
1. List new files in `inbox/` (recursively) and every `projects/*/submissions/_drop/`, skipping README.md, .DS_Store, .gitkeep.
2. `python3 .claude/scripts/fingerprint.py <files>`: skip anything `already_processed`.
3. Add pasted text or links given with the command.

## Classify (one line each)
`type | project (or none) | journal | round | reviewer | confidence`. Types: decision-letter, reviewer-report, response-letter, manuscript-version, published-paper (own), paper (other's), cv, linkedin, bio, dataset, codebook, coauthor-correspondence, journal-guidelines, call-for-papers, slides-poster, irb, grant, notes, idea, other. Infer journal, round and reviewer from the content (headers, "Reviewer 2", manuscript IDs, dates). Ask the researcher only when confidence is low.

## Show the routing plan, then file
| Type | Destination |
|---|---|
| decision-letter, reviewer-report, response-letter | `projects/<p>/submissions/round-N/` renamed `YYYY-MM_<JOURNALABBR>_R<N>_<role>.<ext>` (roles: decision, reviewer-<k>, response, manuscript); then code comments (below) |
| manuscript-version | `projects/<p>/manuscript/` as the next `manuscript_v{N}_mmddyyyy` (copy, never overwrite) |
| own published paper, cv, linkedin, bio | facts to `vault/publications.md`; profile changes as suggestions in `vault/suggestions.md` |
| paper (other's) | library suggestion in the project's `refs.md`; a `vault/knowledge/` construct note only once the record is citable |
| dataset, codebook | `projects/<p>/data/raw/` (copy) and a `vault/knowledge/` dataset card |
| coauthor-correspondence | facts to `vault/people/<name>.md`; tasks to Notion |
| journal-guidelines, call-for-papers | `vault/journals/<j>.md`; calls to Notion |
| idea, notes | `vault/knowledge/` (type: idea) or the project log |

Past manuscripts in `inbox/manuscripts/<folder>/` become light projects in `projects/_archive/<slug>/` (submissions only).

After filing, **move the original** from `inbox/` or `_drop/` into `vault/sources/<YYYY-MM>/` (mv, unchanged) and add a row to `vault/sources/manifest.md`.

## Code reviewer comments into `vault/reviews/ledger.csv`
One row per distinct comment. `category`: theory-contribution | measurement-validity | design-sampling | analysis-reporting | writing-framing | journal-fit. `severity`: major | minor. `outcome` stays blank until the next decision. Response columns are filled only from the response letter the researcher confirms as submitted (never from an `ai-draft`).

## Update `vault/reviews/lessons.md`
1. Copy lessons.md and ledger.csv to `.backups/<YYYY-MM-DD_HHMM>/` first.
2. For each new comment, find the matching lesson (same category and issue). Extend it: update counts, journals, last seen, add the quote reference. Create a new lesson when the issue has appeared in 2+ comments or is a major comment.
3. Never change the text of a `Status: pinned` lesson; only add evidence lines under it.
4. Update the journal profile's "What reviewers here ask for".
5. Log every changed lesson title in `vault/log.md`.

## Conflicts
When new information contradicts stored information (affiliation, word limit, deadline), show both and ask; never overwrite silently.

## --refresh
Without new files: query OpenAlex for the researcher's new works and coauthors (ORCID in config.md), new works citing theirs, and check journal guideline pages in `vault/journals/` for changes. Route results as above; new citing papers go to suggestions only.

## Close-project harvest
Read the accepted (or final) version, all rounds, `analysis/`, and the project log. Write `projects/<p>/harvest-report.md` as a checklist (publication record; journal experience; outcome-confirmed lessons; measures with obtained reliability/validity; reusable scripts; dataset card; construct notes from citable records; passages; ideas from limitations and unpursued reviewer suggestions; style observations; coauthor roles; process findings). File only the items the researcher ticks, then move the project to `projects/_archive/` and update Notion.

## Finish
Update `vault/index.md`, append to `vault/log.md` and project logs, update `status.md` and Notion (notion-sync skill), and report a summary: what was filed where, what needs a decision.
