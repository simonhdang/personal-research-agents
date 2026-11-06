---
name: reference-library
description: Read the researcher's reference manager (EndNote, Zotero or Mendeley), enforce the suggested, acquired, verified, citable pipeline, prepare records for import, and check citations in drafts. Use whenever finding, adding, citing or verifying references.
---

# Reference library

The manager in use is set in `config.md` > Reference manager. Always check the library first before searching elsewhere.

## Reading the library
| Manager | How to read | Full text visible? |
|---|---|---|
| EndNote | The XML export named in config.md (File > Export > XML). Ask the researcher to refresh it when it is older than the current task, or read a read-only copy of the `.enl` library's `.Data` folder for attached PDFs | Yes: `internal-pdf://` attachments |
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
