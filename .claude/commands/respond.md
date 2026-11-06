---
description: Revise-and-resubmit: parse the real reviews for a project's current round, plan responses using what worked before, then draft the response letter, traceability matrix and tracked-change manuscript edits.
argument-hint: <project>
---

# /respond

Project: `$ARGUMENTS`.

1. Make sure the round's decision letter and reports are filed (if they are in `_drop/`, run /update first).
2. **rr-strategist** builds `submissions/round-N/response-plan.md`. Stop and walk the researcher through the decisions (accept / partial / disagree) comment by comment or in batches.
3. Route needed work in parallel where independent: new analyses to the **analyst**, new literature to the **librarian**, theory changes to the **theorist**.
4. **rr-strategist** drafts the response letter (`ai-draft` in the name), the traceability matrix, and edits.json; the **writer** applies edits as a new tracked-change version.
5. **integrity-checker** checks the new version and the letter.
6. Update status (stage R&R), Notion Submissions and Tasks. Remind the researcher to tell you which response letter was actually submitted, so it can enter the ledger.
