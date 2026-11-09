# library/

This project's reference library. Agents may **read** it but never change it (the guard blocks any write here).

## EndNote (one library per project)
1. Close EndNote.
2. Copy **both** the library file and its data folder here, keeping the same name:
   - `<name>.enl`
   - `<name>.Data/` (holds the attached PDFs; without it the references have no full text)
   A compressed library (`<name>.enlx`) also works: copy it here and open it once in EndNote to unpack.
3. From now on, open the library **from this folder** and stop using the old location for this project, so there is only one copy.
4. Export it for the agents: select all references > File > Export > Save as type: **XML** > save as `<name>.xml` in this folder. Re-export whenever you add references.
5. Record the paths in the project's `CLAUDE.md` > Reference library.

**If a draft already has EndNote citations** from a larger master library, copy that whole library instead of building a new one from a group: a new library renumbers records, so existing `{Author, Year #RecNum}` citations would point to the wrong references.

**Cloud sync:** EndNote warns against keeping libraries in iCloud, Dropbox, or OneDrive folders. If this folder is synced (on a Mac, Documents often is), keep the library in a non-synced folder such as `~/EndNote/` and put only its path in the project's `CLAUDE.md`.

## Zotero or Mendeley
Nothing needs to be copied. Put the project's export here (Better BibTeX `.bib` with Keep updated, or a Mendeley `.bib`/`.ris`) and record the collection name in `CLAUDE.md`.

New references flow the other way: the Librarian prepares them in `../to-import/` for you to import.
