---
description: Write or revise part of a manuscript in your voice for the target journal; edits become a new tracked-change version and pass the integrity check.
argument-hint: <project> <section or instruction>
---

# /draft

Arguments: `$ARGUMENTS`.

1. **writer** reads the inputs required by the paper-writing skill (voice, style profile, lessons, journal profile, citable refs, analysis outputs).
2. If citations are needed that are not citable yet, the **librarian** runs in parallel to find and stage them; the writer leaves `[CITATION NEEDED: topic]` meanwhile.
3. Revisions to the existing manuscript: new version via docx_tracked.py with a comment per change. New sections: `manuscript/drafts/`.
4. **integrity-checker** runs; report PASS/FAIL with the draft.
5. Update status and log.
