#!/usr/bin/env python3
"""Create the next manuscript version and apply edits as Word tracked changes with comments.

Usage:
  python3 .claude/scripts/docx_tracked.py <manuscript_folder> <edits.json> [--base manuscript] [--source FILE]

edits.json:
  {"author": "Claude (personal-research-agents)",
   "edits": [
     {"find": "old words", "replace": "new words", "comment": "why", "nth": 1},
     {"insert_after": "anchor words", "text": " added words", "comment": "why"},
     {"find": "words to delete", "replace": "", "comment": "why"}
   ]}

The latest manuscript_v{N}_mmddyyyy.docx (or --source) is copied to manuscript_v{N+1}_{today}.docx and
edited there; the original is never touched. Prints a JSON summary; exit code 1 if any edit was not found.
Requires: python-docx >= 1.2, lxml.
"""
import sys, os, re, json, glob, shutil, copy, datetime, argparse
from docx import Document
from docx.oxml.ns import qn
from docx.text.run import Run

W_ID = [9000]
def nid():
    W_ID[0] += 1
    return str(W_ID[0])

def find_versions(folder, base):
    out = []
    for f in glob.glob(os.path.join(folder, f"{base}_v*_*.docx")):
        m = re.search(r"_v(\d+)_", os.path.basename(f))
        if m and not os.path.basename(f).startswith("~$"):
            out.append((int(m.group(1)), f))
    return sorted(out)

def next_path(folder, base, n):
    d = datetime.date.today().strftime("%m%d%Y")
    p = os.path.join(folder, f"{base}_v{n}_{d}.docx")
    if os.path.exists(p):
        raise SystemExit(f"{p} already exists; not overwriting.")
    return p

def runs_of(p):
    return [r for r in p.findall(qn("w:r")) if r.find(qn("w:t")) is not None]

def rtext(r):
    return "".join(t.text or "" for t in r.findall(qn("w:t")))

def set_text(r, text):
    ts = r.findall(qn("w:t"))
    for t in ts[1:]:
        r.remove(t)
    ts[0].text = text
    ts[0].set("{http://www.w3.org/XML/1998/namespace}space", "preserve")

def split_run(r, off):
    """Split run r at char offset; return (left, right). Either may be None if empty."""
    t = rtext(r)
    if off <= 0: return None, r
    if off >= len(t): return r, None
    right = copy.deepcopy(r)
    set_text(r, t[:off]); set_text(right, t[off:])
    r.addnext(right)
    return r, right

def locate(p, needle, nth):
    """Return list of run elements exactly covering the nth occurrence of needle, splitting runs as needed."""
    runs = runs_of(p)
    full = "".join(rtext(r) for r in runs)
    idx, start = -1, 0
    for _ in range(nth):
        idx = full.find(needle, start)
        if idx < 0: return None
        start = idx + 1
    end = idx + len(needle)
    pos, covered = 0, []
    for r in runs:
        t = rtext(r); a, b = pos, pos + len(t); pos = b
        if b <= idx or a >= end: continue
        cur = r
        if a < idx:
            _, cur = split_run(cur, idx - a); a = idx
        if b > end:
            cur, _ = split_run(cur, end - a)
        covered.append(cur)
    return covered

def make_ins(template_run, text, author, date):
    ins = template_run.makeelement(qn("w:ins"), {qn("w:id"): nid(), qn("w:author"): author, qn("w:date"): date})
    r = copy.deepcopy(template_run)
    for child in list(r):
        if child.tag != qn("w:rPr"): r.remove(child)
    t = r.makeelement(qn("w:t"), {}); t.text = text
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    r.append(t); ins.append(r)
    return ins, r

def wrap_del(runs, author, date):
    d = runs[0].makeelement(qn("w:del"), {qn("w:id"): nid(), qn("w:author"): author, qn("w:date"): date})
    runs[0].addprevious(d)
    for r in runs:
        for t in r.findall(qn("w:t")):
            t.tag = qn("w:delText")
        d.append(r)
    return d

def apply(doc, edit, author, initials, date):
    nth = int(edit.get("nth", 1))
    anchor = edit.get("find") if "find" in edit else edit.get("insert_after")
    if not anchor: return False
    seen = 0
    for p_el in doc.element.body.iter(qn("w:p")):
        full = "".join(rtext(r) for r in runs_of(p_el))
        c = full.count(anchor)
        if seen + c < nth:
            seen += c; continue
        covered = locate(p_el, anchor, nth - seen)
        if not covered: return False
        para = None
        comment_runs = []
        if "find" in edit:
            d = wrap_del(covered, author, date)
            new = edit.get("replace", "")
            if new:
                ins, r = make_ins(covered[0], new, author, date)
                d.addnext(ins); comment_runs = [r]
            else:
                comment_runs = covered
        else:
            ins, r = make_ins(covered[-1], edit.get("text", ""), author, date)
            covered[-1].addnext(ins); comment_runs = [r]
        if edit.get("comment"):
            from docx.text.paragraph import Paragraph
            para = Paragraph(p_el, doc._body)
            doc.add_comment([Run(x, para) for x in comment_runs], text=edit["comment"], author=author, initials=initials)
        return True
    return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder"); ap.add_argument("edits")
    ap.add_argument("--base", default="manuscript"); ap.add_argument("--source")
    a = ap.parse_args()
    spec = json.load(open(a.edits))
    author = spec.get("author", "Claude (personal-research-agents)")
    initials = spec.get("initials", "AI")
    versions = find_versions(a.folder, a.base)
    if a.source:
        src = a.source; n = (versions[-1][0] if versions else 0) + 1
    else:
        if not versions: raise SystemExit(f"No {a.base}_v*_*.docx in {a.folder}")
        src = versions[-1][1]; n = versions[-1][0] + 1
    dst = next_path(a.folder, a.base, n)
    shutil.copy2(src, dst)
    doc = Document(dst)
    date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    done, missing = 0, []
    for e in spec.get("edits", []):
        if apply(doc, e, author, initials, date): done += 1
        else: missing.append(e.get("find") or e.get("insert_after"))
    doc.save(dst)
    print(json.dumps({"source": src, "new_version": dst, "applied": done, "not_found": missing}, indent=2))
    sys.exit(1 if missing else 0)

if __name__ == "__main__":
    main()
