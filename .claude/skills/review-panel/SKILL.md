---
name: review-panel
description: Simulate a pre-submission peer review of a manuscript for a named journal with an editor, three independent reviewers and a devil's advocate, seeded from the researcher's own review history. Use for /review or when asked how a journal's reviewers will react.
---

# Review panel

Simulates the review a manuscript would get at one named journal, using what this researcher's past reviewers actually asked for.

## Inputs (read before reviewing)
1. Latest manuscript version in `projects/<name>/manuscript/` (read-only).
2. `vault/journals/<journal>.md`: scope, what reviewers there ask for, desk-reject triggers.
3. `vault/reviews/lessons.md`: the general sections plus the journal-specific section. This is the checklist.
4. `vault/reviews/ledger.csv` rows for this journal (if any).
5. `projects/<name>/CLAUDE.md` for the model, constructs and target journal.

## Panel (run the four reviewers in parallel and independently; none sees another's report)
| Seat | Agent | Focus |
|---|---|---|
| Editor | panel-editor | Desk screen first (fit, contribution, scope); later synthesizes all reports into a decision letter |
| Reviewer 1 | panel-reviewer, persona "methodology" | Design, sampling, measurement, PLS-SEM / experiment / PROCESS reporting, common method bias, endogeneity |
| Reviewer 2 | panel-reviewer, persona "domain" | Theory, hypotheses logic, literature positioning in the journal's field |
| Reviewer 3 | panel-reviewer, persona "perspective" | Contribution, managerial and policy implications, adjacent-discipline view |
| Devil's advocate | panel-devils-advocate | The strongest honest case for rejection |

## Each reviewer's procedure
1. Go through every lesson in `lessons.md` that applies; mark each comment it triggers as `history: <lesson title>`.
2. Apply `references/review_criteria_framework.md`, `references/quality_rubrics.md` and, for statistics, `references/statistical_reporting_standards.md`.
3. Write comments as a real reviewer would: specific, located (section/page), actionable.
4. Tag each comment: `severity` (major | minor), `category` (theory-contribution | measurement-validity | design-sampling | analysis-reporting | writing-framing | journal-fit).
5. Literature suggestions name a topic or a library record, never an invented citation.

## Outputs: `projects/<name>/reviews/simulated/<YYYY-MM-DD>_<journal>/`
- `reviewer-1.md`, `reviewer-2.md`, `reviewer-3.md`, `devils-advocate.md` (format: `references/peer_review_report_template.md`)
- `editor-decision.md` (format: `references/editorial_decision_template.md`): decision, top 5 issues, prioritized revision roadmap
- `predictions.csv`: one row per comment (`seat,category,severity,history_lesson,summary`) so /retro can later compare with real reviews

## Limits
- Read-only on the manuscript; no web access; never uploads anything.
- This panel is not calibrated. Say so in the decision letter. /retro measures how well its predictions matched real reviews over time.
- Background on the original design: `references/ars-agents/` (ARS v3.24.2, CC BY-NC; see NOTICE.md).
