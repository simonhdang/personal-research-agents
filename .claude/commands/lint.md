---
description: Vault health check: broken links, orphan pages, stale project status, contradictions, and growth that suggests reorganizing.
argument-hint: [--fix]
---

# /lint

Delegate to the **archivist**.

Checks:
1. Broken `[[links]]` and links to missing files.
2. Orphan pages (nothing links to them; not in `vault/index.md`).
3. Stale projects (no log entry for 30+ days while not Archived).
4. Contradictions: the same fact stated differently across pages (affiliations, journal word limits, deadlines).
5. Index drift: pages missing from `vault/index.md`.
6. Growth: `vault/knowledge/` past about 30 files (suggest a split by type); any new top-level vault folder (needs the researcher's approval).
7. Ledger rows without a matching lesson after 2+ occurrences.

Report all findings. `--fix` applies only safe fixes (index entries, missing links to existing pages); everything else waits for the researcher.
