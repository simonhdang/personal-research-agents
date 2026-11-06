#!/bin/bash
# Loads the researcher profile and hard rules at the start of every session, and reports waiting files.
ROOT="${CLAUDE_PROJECT_DIR:-$(pwd)}"
cd "$ROOT" || exit 0
echo "=== soul.md (researcher profile) ==="; cat soul.md 2>/dev/null
echo; echo "=== vault/owner/no-go.md (hard rules: obey without exception) ==="; cat vault/owner/no-go.md 2>/dev/null
N=$(find inbox projects/*/submissions/_drop -type f ! -name 'README.md' ! -name '.DS_Store' ! -name '.gitkeep' 2>/dev/null | wc -l | tr -d ' ')
if [ "${N:-0}" != "0" ]; then echo; echo "=== NOTICE: $N file(s) waiting in inbox/ or a submissions/_drop/ folder. Suggest /update once. ==="; fi
if grep -q '^- Manager: *<!--' config.md 2>/dev/null || ! grep -q '^- Manager: *[A-Za-z]' config.md 2>/dev/null; then
  echo; echo "=== NOTICE: setup not finished (config.md has no reference manager). Suggest /setup. ==="
fi
exit 0
