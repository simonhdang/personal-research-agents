---
name: reference-library
description: Read the researcher's reference manager (EndNote, Zotero or Mendeley), enforce the suggested, acquired, verified, citable pipeline, prepare records for import, and check citations in drafts. Use whenever finding, adding, citing or verifying references.
---

# Reference library

The manager in use is set in `config.md` > Reference manager. Always check the library first before searching elsewhere.

## Where the library is
- **One library per project** (recommended for EndNote): the `.enl` file, its `.Data/` folder and the XML export live in `projects/<name>/library/`, or at the path recorded in the project's `CLAUDE.md` > Reference library when the library is kept outside a cloud-synced folder.
- **One shared library**: its path and export are in `config.md`; the project's group or collection is named in the project's `CLAUDE.md`.
- `library/` is read-only for agents. Never open, save, compact or modify a `.enl` file or its `.Data` folder; read the export and the PDFs only. Ask the researcher to re-export when the export is older than the draft or task.
- Record numbers belong to one library. Never mix `#RecNum` citations from two libraries in one manuscript.

## Reading the library
| Manager | How to read | Full text visible? |
|---|---|---|
| EndNote | The XML export in the project's `library/` (or named in config.md for a shared library), made with File > Export > XML. Attached PDFs are read from the library's `.Data/PDF/` folder, read-only | Yes: `internal-pdf://` attachments |
| Zotero | Zotero 7 local API (`http://localhost:23119/api/users/0/items`, enabled in Zotero Settings > Advanced) or the Better BibTeX auto-export `.bib` | Yes: attachment items / `file` field |
| Mendeley | BibTeX or RIS export named in config.md | Partly: `file` field if exported |

## Pipeline
`suggested -> acquired -> verified -> citable` (see literature-review skill). Only **citable** records may appear in text.

## Adding records
- **EndNote / Mendeley**: agents cannot write to the library. Put a `.ris` file and the legal open-access PDF (same base name) in `projects/<name>/to-import/`, then ask the researcher to import them (EndNote: File > Import; attach the PDF). Example RIS:
```
TY  - JOUR
AU  - Lastname, First
PY  - 2024
TI  - Title
T2  - Journal
DO  - 10.xxxx/xxxxx
ER  -
```
- **Zotero**: with the researcher's approval each time, add via the Zotero web API using the key stored outside the repo (never in config.md); attach the PDF.
- Papers without a legal open-access copy go to `refs.md` > To download.

## Citing in drafts
| Manager | In-text form the Writer uses | Formatted by |
|---|---|---|
| EndNote | `{Dang, 2024 #312}` (record number required) | Cite While You Write > Update Citations |
| Zotero | `[@citekey]` (Better BibTeX) or `{Dang, 2024}` RTF-scan form | Zotero RTF/ODF Scan or Pandoc |
| Mendeley | `{Dang, 2024}` | Mendeley Cite (manual) |

## Checking
```
python3 .claude/scripts/cite_check.py --library <export> --draft <file.docx|file.md> [--out report.md]
```
Passes only if every citation exists in the library and has full text attached.
