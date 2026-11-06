---
name: literature-review
description: Search, screen and synthesize literature for a project, checking the researcher's reference library first and moving papers through the suggested, acquired, verified, citable pipeline. Use for literature reviews, finding papers, evidence matrices, systematic reviews, or literature watches.
---

# Literature review

## Search order
1. **The researcher's library first** (see `config.md` and the reference-library skill). Report what is already there.
2. **Scholarly connectors**: OpenAlex and Consensus (load via ToolSearch), then Semantic Scholar/Crossref per `references/openalex_api_protocol.md` and `references/crossref_api_protocol.md`.
3. **Web search** only for gray literature or very recent work.

Judge sources with `references/source_quality_hierarchy.md` (peer-reviewed journals in the field first; check journal standing in `vault/journals/` when present).

## Pipeline (never skip a stage)
| Stage | Meaning | Where recorded |
|---|---|---|
| suggested | Found and relevant; not in library | `refs.md` > Suggested, with a one-line reason |
| acquired | Record + full text now in library | stage column updated |
| verified | The PDF was read and the claim it will support was confirmed | stage column + the claim |
| citable | May be used by the Writer | stage column |

- If OpenAlex reports a legal open-access PDF, download it to `projects/<name>/to-import/` with a matching `.ris` record (EndNote/Mendeley) or add via the Zotero API after approval (see reference-library skill).
- Otherwise add the paper to `refs.md` > To download for the researcher.
- Never put a suggested or acquired paper into a manuscript.

## Synthesis
- Build an evidence matrix (`references/literature_matrix_template.md`): construct, theory, context, method, finding, record number.
- Group by theme; name gaps and contradictions explicitly (`references/argumentation_reasoning_framework.md`).
- Save to `projects/<name>/analysis/literature-matrix.md` and, for reusable theory notes, propose `vault/knowledge/` entries (type: construct).

## Systematic reviews
Follow `references/systematic_review_protocol.md` and `references/systematic_review_toolkit.md` (PRISMA 2020 flow, preregistration via `references/preregistration_template.md`).

Reference files: ARS v3.24.2 (CC BY-NC; see NOTICE.md).
