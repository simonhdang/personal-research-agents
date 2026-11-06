---
name: manuscript-versioning
description: Make any change to a manuscript as a new dated version with Word tracked changes and a comment explaining each edit, never touching the existing file. Use whenever editing a manuscript or applying revisions.
---

# Manuscript versioning

## Rule
Existing manuscript files are never edited (the guard hook blocks it). Every change produces `manuscript_v{N+1}_mmddyyyy.docx` in the project's `manuscript/` folder.

## How
1. Write the planned edits to `projects/<name>/manuscript/edits_<mmddyyyy>.json`:
```json
{"author": "Claude (personal-research-agents)",
 "edits": [
   {"find": "exact old words", "replace": "new words", "comment": "R2.3: softer causal claim"},
   {"insert_after": "exact anchor words", "text": " (alpha = .89)", "comment": "Report reliability (lessons.md: Measurement)"},
   {"find": "words to delete", "replace": "", "comment": "R1.4: remove redundancy"},
   {"find": "repeated phrase", "replace": "new", "nth": 2, "comment": "second occurrence only"}
 ]}
```
   - `find`/`insert_after` text must match the document exactly, within one paragraph or table cell.
   - Every edit gets a comment naming its reason (reviewer comment id, lesson, or the researcher's instruction).
2. Run:
```
python3 .claude/scripts/docx_tracked.py projects/<name>/manuscript projects/<name>/manuscript/edits_<mmddyyyy>.json
```
   It copies the latest version to the next number with today's date and applies the edits as tracked changes with comments. It reports edits it could not find; fix those anchors and rerun on a fresh version, or list them for the researcher.
3. New paragraphs or whole sections: write them to `manuscript/drafts/<section>_<mmddyyyy>.md` and tell the researcher where they go (the script edits inline text only).
4. Log the new version in the project log with the number of edits applied.

## Non-Word manuscripts
For LaTeX or Markdown: copy to the next version name and edit the copy; produce a diff summary in the project log.

Requires `python-docx>=1.2` and `lxml` (`.claude/scripts/requirements.txt`; /setup installs them after asking).
