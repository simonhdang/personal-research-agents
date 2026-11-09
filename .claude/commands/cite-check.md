---
description: Check every citation in a draft or manuscript against your reference library and PDFs, and report anything missing, ambiguous or without full text.
argument-hint: <project> [file]
---

# /cite-check

Arguments: `$ARGUMENTS`.

1. Find the library export: the project's `CLAUDE.md` > Reference library (usually `library/<name>.xml`), or `config.md` for a shared library. If the export is older than the draft, ask the researcher to re-export it (EndNote: select all > File > Export > XML).
2. Run `python3 .claude/scripts/cite_check.py --library <export> --draft <file>` (default file: latest manuscript version).
3. Show the problems first, with the fix for each (import the record, attach the PDF, add a record number).
4. Record the result in the project's `refs.md` > Citation check.
