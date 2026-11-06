---
description: File and learn from anything new: files in inbox/ or a project's submissions/_drop/, pasted text, or a link. Use --refresh to pull outside changes (new publications, citing papers, journal guidelines).
argument-hint: [--refresh] [file, link or text]
---

# /update

Delegate to the **archivist** agent with the update-routing skill (`.claude/skills/update-routing/SKILL.md`). Arguments: `$ARGUMENTS`.

1. Collect new items (or only the given item); skip already-processed fingerprints.
2. Classify each item and show the routing plan as a table. Ask only about low-confidence items.
3. After the researcher confirms the plan (one "ok" is enough), file everything, move originals to `vault/sources/<YYYY-MM>/`, code reviewer comments, and update lessons and journal profiles.
4. If new reviews arrived for an active project, offer /respond.
5. Response letters: add to the ledger only when the researcher confirms it is the submitted version.
6. `--refresh`: run the refresh procedure from the skill (OpenAlex works and coauthors, citing papers, journal guideline changes).
7. Update `vault/index.md`, logs, affected `status.md` files and Notion. Report what changed where, plus anything waiting for a decision.
