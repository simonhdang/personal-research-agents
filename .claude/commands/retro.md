---
description: Look back: compare simulated reviews with the real ones, see where you overrode the agents, and propose lesson updates and rule suggestions. Runs quarterly or after a decision arrives.
argument-hint: [project]
---

# /retro

Scope: `$ARGUMENTS` (a project after a decision, or everything since the last retro).

1. For each project with both `reviews/simulated/*/predictions.csv` and real reviews in the ledger: match predicted comments to real ones by category and issue. Report hits, misses (real comments not predicted) and false alarms. Append a line per project to `vault/log.md` with hit rate.
2. Misses that recur become candidate lessons (the archivist adds them with evidence).
3. Read `vault/log.md` and project logs for places where the researcher rejected or rewrote agent output; summarize patterns.
4. Write proposals to `vault/suggestions.md`: rule suggestions, style-profile changes, agent instruction changes. Never apply them.
5. List suggestions older than 90 days with no decision and ask whether to keep or drop them.
