---
name: paper-writing
description: Draft or revise manuscript sections in the researcher's own voice for a target journal, citing only verified library records. Use for /draft, writing introductions, theory, methods, results, discussion, abstracts, cover letters, or AI-disclosure statements.
---

# Paper writing

## Before writing
1. Read `soul.md` (voice, contribution philosophy), `vault/owner/style-profile.md`, and `vault/owner/research-profile.md`.
2. Read `vault/reviews/lessons.md` and treat every applicable lesson as a requirement (e.g., report HTMT, address CMB, state the contribution early).
3. Read the target journal profile in `vault/journals/` (word limit, structure, reference style).
4. Read the project's `refs.md`: only references at stage **citable** may be cited.

## Writing rules
- American English unless soul.md says otherwise.
- Match the style profile: sentence length, hedging, transitions, citation integration. Follow `references/style_calibration_protocol.md` when the profile is thin.
- Structure: `references/paper_structure_patterns.md` and `templates`-style IMRaD (`references/imrad_template.md`); introductions per `references/intro_title_rhetoric_guide.md`; abstracts per `references/abstract_writing_guide.md`.
- Run `references/writing_quality_check.md` before handing back: no filler, no generic AI phrasing, no unsupported claims.
- Citations: use the format in `config.md`. For EndNote write temporary citations with record numbers, e.g. `{Dang, 2024 #312}`; for Zotero/BibTeX use keys `[@dang2024]`. Never cite anything not citable; write `[CITATION NEEDED: topic]` instead and add the need to `refs.md`.
- Numbers come only from `analysis/` outputs; quote the file they came from in a comment.
- AI-use disclosure: draft one per `references/venue_disclosure_policies.md` when submitting.

## Output
- Edits to an existing manuscript: use the manuscript-versioning skill (new version, tracked changes, a comment explaining each change).
- New sections: `projects/<name>/manuscript/drafts/<section>_<mmddyyyy>.md`, for the researcher to place.
- Then run the integrity-check skill (citations at minimum) before calling the draft done.

Reference files: ARS v3.24.2 (CC BY-NC; see NOTICE.md).
