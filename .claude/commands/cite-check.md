---
description: Check every citation in a draft or manuscript against your reference library and PDFs, and report anything missing, ambiguous or without full text.
argument-hint: <project> [file]
---

# /cite-check

Arguments: `$ARGUMENTS`.

1. Find the library export path in `config.md` (ask the researcher to refresh the export if it is older than the draft).
2. Run `python3 .claude/scripts/cite_check.py --library <export> --draft <file>` (default file: latest manuscript version).
3. Show the problems first, with the fix for each (import the record, attach the PDF, add a record number).
4. Record the result in the project's `refs.md` > Citation check.
