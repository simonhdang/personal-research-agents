---
name: integrity-check
description: Final gate before any manuscript or response letter is called done; verifies every citation against the library and PDFs, every number against analysis output, and common AI-research failure modes. Use for /cite-check, before submission, and after every draft.
---

# Integrity check

Nothing is "done" until this check passes. Output: `projects/<name>/reviews/integrity-report_<YYYY-MM-DD>.md` with PASS or FAIL per section.

## 1. Citations (always)
Run:
```
python3 .claude/scripts/cite_check.py --library <export from the project's CLAUDE.md > Reference library, or config.md> --draft <manuscript or draft> --out projects/<name>/refs-check.tmp.md
```
Copy the summary into `refs.md` > Citation check. Any NOT IN LIBRARY, NO FULL TEXT or AMBIGUOUS result is a FAIL.

## 2. Claims
For each citation supporting a substantive claim (all of them for key claims; a sample of at least 20 for routine ones), open the PDF and confirm the source says what the sentence says. Follow `references/claim_verification_protocol.md`. Record mismatches with page numbers.

## 3. Numbers
Every statistic, sample size and coefficient in the text and tables must match a file in `analysis/`. List each number with its source file; mismatches are a FAIL.

## 4. Failure modes
Check `references/ai_research_failure_modes.md` (fabricated or misattributed references, overstated claims, methods that do not match what was run, results reported that were never computed) and `references/integrity_review_protocol.md`.

## 5. Reproducibility (before submission)
`references/reproducibility_audit.md`: seeds set, scripts run from raw to results, data and code availability statement drafted.

## Rules
Read-only on the manuscript. Web access only to confirm that a reference exists. Report problems; do not fix them (the Writer does).

Reference files: ARS v3.24.2 (CC BY-NC; see NOTICE.md).
