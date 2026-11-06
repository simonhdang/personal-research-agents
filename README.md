# personal-research-agents

A Claude Code template that gives one researcher a personal team of AI research agents.

- You talk to one **Orchestrator**; it assigns work to specialist agents and runs independent jobs in parallel.
- The system **learns from your past peer reviews**: every reviewer comment you add updates `vault/reviews/lessons.md`, which all agents consult before drafting, simulating reviews, or writing response letters.
- Agents **cite only records in your reference manager** (EndNote, Zotero, or Mendeley) that have the full text attached.
- **You own the rules.** `soul.md` and everything in `vault/owner/` are yours; agents can only suggest changes in `vault/suggestions.md`.
- `/update` takes anything new and files it where it belongs; `/close-project` harvests a finished project into reusable knowledge.
- Every project gets its **own folder and CLAUDE.md**, mirrored to **Notion** (portfolio and per-project trackers).

Start with `GETTING-STARTED.md`. A 25-slide training deck with speaker notes is in `docs/personal-research-agents_seminar.pptx`.

## What's inside

| Part | Count | Where |
|---|---|---|
| Agents | 13 (Orchestrator is the main session) | `.claude/agents/` |
| Commands | 12 | `.claude/commands/` |
| Skills | 14 (9 adapted, 5 new) | `.claude/skills/` |
| Safety hooks | Guard (blocks edits to originals, deletions, sending; asks before changing your own files) and session start | `.claude/hooks/` |
| Helper scripts | Citation check, tracked-change versioning, file fingerprints | `.claude/scripts/` |

Third-party material and licenses: `THIRD_PARTY.md`.

## Map

```
personal-research-agents/
├── CLAUDE.md          global orchestrator instructions (short)
├── soul.md            researcher profile (yours; filled by /setup)
├── config.md          reference manager, accounts, Notion IDs (filled by /setup)
├── GETTING-STARTED.md
├── inbox/             drop anything new here, then /update
├── vault/             cross-project knowledge
│   ├── index.md         map of everything + collaborator table
│   ├── log.md           append-only history
│   ├── suggestions.md   agents propose changes to anything you own
│   ├── owner/           YOURS: no-go rules, research profile, style profile (agents read only)
│   ├── publications.md  facts from ORCID and decision letters
│   ├── reviews/         lessons.md + ledger.csv (learning from reviews)
│   ├── journals/        one file per journal
│   ├── people/          one file per coauthor
│   ├── knowledge/       reusable assets: measures, methods, datasets, constructs, passages, ideas
│   └── sources/         untouched originals + manifest
├── projects/          one folder per study (from projects/_template-project)
├── .backups/          dated backups of vault files (no git needed)
└── .claude/           agents, commands, skills, permission settings
```

Folders appear only when needed: if `vault/knowledge/` passes about 30 files, the Archivist suggests splitting it by type.
