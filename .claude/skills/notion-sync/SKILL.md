---
name: notion-sync
description: Create and keep the Notion trackers in step with local project status: a portfolio across projects plus per-project tasks and submission history. Use at the end of every command that changes status, and in /setup.
---

# Notion sync

Local `projects/<name>/status.md` is the source of truth; Notion mirrors it. Exception: **deadline, priority, blocked** are read back from Notion at the start of each session (the researcher may edit them on a phone).

Load the Notion tools with ToolSearch ("notion") before calling them. If Notion is unavailable, finish the local work and add "Notion not updated" to the summary.

## Databases (created once by /setup under a "personal-research-agents" page; IDs saved in config.md > Notion)
| Database | Properties |
|---|---|
| Projects | Name (title), Stage (select: Idea, Design, Data, Analysis, Writing, Under review, R&R, Accepted, Rejected, Archived), Target journal (text), Current round (number), Next action (text), Deadline (date), Priority (select: High, Medium, Low), Blocked (checkbox), Coauthors (text), Last agent run (date), Local folder (text) |
| Tasks | Task (title), Project (relation > Projects), Owner (select: Me, Coauthor, Agent), Due (date), Status (select: To do, In progress, Waiting, Done) |
| Submissions | Name (title, "<Journal> R<N>"), Project (relation), Journal (text), Round (number), Submitted (date), Decision (select: Pending, Desk reject, Major revision, Minor revision, Reject, Accept), Decision date (date), Comments (number) |

Views: Projects as a board by Stage, a timeline by Deadline, "Due this week", "Waiting on coauthors"; Tasks filtered by project on each project page; Submissions "Under review now".

## Bootstrap sequence (/setup)
1. Create the parent page "personal-research-agents".
2. Create each database under it; confirm it sits under the parent (move it if not).
3. Re-add select options if creation dropped them.
4. Create the views.
5. Save every ID to `config.md` > Notion.

## Sync after each command
1. Read the project's `status.md` frontmatter.
2. Update (or create) the Projects row; store its ID in `status.md` > notion_page_id.
3. Add or close Tasks the command created or finished; add or update the Submissions row when a round changes.
4. Always include readable page content (next action, recent activity), not only properties.

## Read-back at session start
For active projects, fetch Deadline, Priority and Blocked from Notion; if they differ from `status.md`, update `status.md` and log the change.
