---
name: rr-response
description: Handle a revise-and-resubmit: parse the decision letter and real reviews, plan responses using what worked before, draft the response letter and a comment-by-comment traceability matrix, and prepare manuscript edits. Use for /respond or when reviews arrive.
---

# R&R response

## 1. Parse
Follow `references/external_review_protocol.md`. Turn the decision letter into a table: `id (R1.1, R1.2, ...) | reviewer | type (major/minor/editorial/positive) | category | request in one line | quote | section`. Categories match the ledger (theory-contribution, measurement-validity, design-sampling, analysis-reporting, writing-framing, journal-fit). Make sure /update has added these comments to `vault/reviews/ledger.csv`.

## 2. Plan
For each comment:
- Look up `vault/reviews/lessons.md` for the matching lesson and its "What worked".
- Recommend one of: **accept**, **partially accept**, **respectfully disagree** (with the evidence). The researcher decides.
- Note required new analysis (hand to the Analyst) or literature (hand to the Librarian).
- Flag conflicts between reviewers and propose how to satisfy both or which to follow.
Save as `submissions/round-N/response-plan.md` and stop for the researcher's decisions.

## 3. Draft (after decisions)
- Response letter: `references/revision_response_template.md`. Polite, specific, each reply quotes the change and gives its page/line.
- Traceability matrix: `references/revision_tracking_template.md` (comment, decision, change made, location, verified?).
- Manuscript edits: an edits.json for the manuscript-versioning skill (one comment per change, naming the reviewer comment id).
- Save the letter as `submissions/round-N/response-letter_ai-draft_<mmddyyyy>.docx` or `.md`.

## 4. Learning hand-off
AI drafts are records only. Ask the researcher to confirm the final submitted response letter; only that version is added to the ledger (my_response_summary, addressed_how). The outcome is attached when the next decision arrives.

Reference files: ARS v3.24.2 (CC BY-NC; see NOTICE.md).
