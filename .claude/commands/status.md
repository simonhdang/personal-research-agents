---
description: Snapshot across all projects: recent runs, deadlines, what's waiting on coauthors, references to download, and pending suggestions. Use --brief for the Monday research brief.
argument-hint: [--brief | project]
---

# /status

1. Read-back from Notion first (deadline, priority, blocked) per the notion-sync skill.
2. For each active project (`projects/*/status.md`, excluding `_template-project` and `_archive`): stage, next action, deadline, blocked, last activity.
3. Show:
   - Due in the next 14 days (sorted by date)
   - Under review / R&R and days since submission
   - Waiting on coauthors
   - References to download (count per project, from refs.md)
   - Files waiting in inbox/ or _drop/
   - Pending items in `vault/suggestions.md` (each mentioned once; do not nag)
   - Last 5 entries of `vault/log.md`
4. `--brief`: the same as a one-page Monday brief. Shown in chat; when run as a scheduled task, also posted as a page under the Notion parent page (no new vault files).
5. If a project name is given, show only that project in more detail.
Keep it short. No changes are made except the Notion read-back.
