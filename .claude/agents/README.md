# Agents

The Orchestrator is the main session (root CLAUDE.md). These are its subagents.

| Agent | Tools | Connectors |
|---|---|---|
| archivist | Read, Glob, Grep, Write, Edit, Bash | none |
| librarian | all (inherits) | OpenAlex, Consensus (search/read) |
| theorist | Read, Glob, Grep, Write, Edit | none |
| methodologist | Read, Glob, Grep, Write, Edit, Bash | none |
| analyst | Read, Glob, Grep, Write, Edit, Bash | none (local only) |
| writer | Read, Glob, Grep, Write, Edit, Bash | none |
| panel-editor, panel-reviewer, panel-devils-advocate | Read, Glob, Grep, Write | none |
| rr-strategist | Read, Glob, Grep, Write, Edit, Bash | none |
| integrity-checker | Read, Glob, Grep, Write, Bash, WebSearch, WebFetch | none |
| liaison | all (inherits) | Gmail (read, drafts), Calendar (read), OpenAlex |
| scout | all (inherits) | Gmail (read), OpenAlex, Notion |

Agents that inherit all tools are still bound by the guard hook, which blocks sending, replying, forwarding, deleting, trashing and sharing through any connector.
