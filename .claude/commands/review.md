---
description: Simulated pre-submission review of a project's manuscript for a named journal: desk screen, three independent reviewers and a devil's advocate in parallel, then an editor's decision letter.
argument-hint: <project> <journal>
---

# /review

Arguments: `$ARGUMENTS` (project and journal; ask if missing).

1. Confirm the manuscript version to review (latest in `manuscript/`) and that `vault/journals/<journal>.md` exists (create from the template if not, with a note that it is thin).
2. **panel-editor**: desk screen. If no-go, report and ask whether to continue.
3. In parallel, independent: **panel-reviewer** (persona methodology), **panel-reviewer** (persona domain), **panel-reviewer** (persona perspective), **panel-devils-advocate**. Each gets the journal name and the review-panel skill.
4. **panel-editor**: synthesis into `editor-decision.md` and `predictions.csv`.
5. Summarize for the researcher: decision, top 5 issues, which ones match past lessons, and the roadmap. Offer to create Tasks in Notion from the roadmap.
6. Log the run.
