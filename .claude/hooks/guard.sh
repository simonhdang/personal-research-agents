#!/bin/bash
# PreToolUse guard for personal-research-agents.
# - Hard-blocks: changes to originals (inbox/, vault/sources/ except manifest.md, data/raw/), existing manuscript
#   versions, deletions, git push.
# - Asks the researcher: any change to soul.md or vault/owner/ (owner-only files).
# Exit 2 = block (stderr goes to Claude). JSON with permissionDecision "ask" = prompt the researcher.
INPUT="$(cat)"
ROOT="${CLAUDE_PROJECT_DIR:-$(pwd)}"
TOOL="$(printf '%s' "$INPUT" | grep -o '"tool_name"[[:space:]]*:[[:space:]]*"[^"]*"' | head -1 | sed 's/.*"\([^"]*\)"$/\1/')"

block() { echo "BLOCKED by personal-research-agents guard: $1" >&2; exit 2; }
ask() {
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"%s"}}\n' "$1"
  exit 0
}

check_path() {   # $1 = absolute or relative path being written
  local p="$1"
  case "$p" in /*) ;; *) p="$ROOT/$p" ;; esac
  local rel="${p#$ROOT/}"
  case "$rel" in
    soul.md|vault/owner/*)
      ask "This changes a file only the researcher owns ($rel). Approve only if you asked for this exact change." ;;
    vault/sources/manifest.md) ;;
    vault/sources/*) block "vault/sources/ holds untouched originals; copy files in with cp instead of editing." ;;
    inbox/*) block "inbox/ files are originals; never edit them." ;;
    projects/*/data/raw/*) block "data/raw/ is read-only; write cleaned data to data/clean/." ;;
    projects/*/library/*) block "library/ holds the researcher's reference library and its export; agents may read it but never change it." ;;
    projects/*/manuscript/*)
      if [ -e "$p" ]; then block "Never edit an existing manuscript version; create manuscript_v{N+1}_mmddyyyy.docx with .claude/scripts/docx_tracked.py."; fi ;;
  esac
}

case "$TOOL" in
  Edit|Write|MultiEdit|NotebookEdit)
    FP="$(printf '%s' "$INPUT" | grep -o '"\(file_path\|notebook_path\)"[[:space:]]*:[[:space:]]*"[^"]*"' | head -1 | sed 's/.*"\([^"]*\)"$/\1/')"
    [ -n "$FP" ] && check_path "$FP"
    ;;
  Bash)
    CMD="$(printf '%s' "$INPUT" | grep -o '"command"[[:space:]]*:[[:space:]]*"\([^"\\]\|\\.\)*"' | head -1 | sed 's/^"command"[[:space:]]*:[[:space:]]*"//; s/"$//')"
    if printf '%s' "$CMD" | grep -Eq '(^|[;&|[:space:]])(rm|rmdir|unlink|shred)([[:space:]]|$)'; then
      block "Deleting is not allowed. Move unwanted files to an _archive/ folder instead."
    fi
    if printf '%s' "$CMD" | grep -Eq 'git[[:space:]]+push|--dangerously'; then block "Not allowed: $CMD"; fi
    if printf '%s' "$CMD" | grep -Eq '(^|[;&|[:space:]])(mv|cp)[[:space:]].*projects/[^[:space:]]+/library/[^[:space:]]*[[:space:]]*$'; then
      block "Agents may not move or copy files into or out of a project's library/; the researcher manages the reference library."
    fi
    if printf '%s' "$CMD" | grep -Eq '(sed[[:space:]]+-i|tee[[:space:]]|truncate|>[^&]|perl[[:space:]]+-pi)'; then
      if printf '%s' "$CMD" | grep -Eq '(vault/sources/[^m ]|inbox/|data/raw/|/library/)'; then block "Shell write to a protected original (inbox/, vault/sources/, data/raw/, library/)."; fi
      if printf '%s' "$CMD" | grep -Eq '(soul\.md|vault/owner/)'; then ask "Shell command changes an owner-only file (soul.md or vault/owner/). Approve only if you asked for it."; fi
    fi
    ;;
  mcp__*)
    if printf '%s' "$TOOL" | grep -Eiq '(send|reply|forward|trash|delete|spam|share|publish|purge|remove|cancel)'; then
      block "Connector action not allowed ($TOOL). Agents may read and create drafts only; the researcher sends, deletes and shares."
    fi
    ;;
esac
exit 0
