#!/usr/bin/env python3
"""Check every citation in a draft against the reference-library export.

Usage: python3 .claude/scripts/cite_check.py --library EXPORT --draft FILE [--draft FILE ...] [--out report.md]

Library export formats: EndNote XML (.xml), RIS (.ris), BibTeX/Better BibTeX (.bib), CSL JSON (.json).
Draft formats: .docx (temporary citations and formatted EndNote/Zotero field codes) or .md/.txt.
Citation forms recognized:
  {Dang, 2024 #312}            EndNote temporary citation (record number)
  {Dang, 2024}                 RTF-scan style (author + year)
  [@dang2024], @dang2024       Pandoc / Better BibTeX keys
  EndNote field codes          <RecNum>312</RecNum> inside ADDIN EN.CITE
A citation passes only if its record exists AND the record has full text attached.
Exit code 1 if any citation fails.
"""
import re, sys, json, argparse, zipfile, html
import xml.etree.ElementTree as ET

def norm(s): return re.sub(r"[^a-z]", "", (s or "").lower())

def load_endnote_xml(p):
    recs = []
    for r in ET.parse(p).getroot().iter("record"):
        t = lambda path: "".join(r.find(path).itertext()).strip() if r.find(path) is not None else ""
        authors = [ "".join(a.itertext()) for a in r.iter("author") ]
        urls = " ".join("".join(u.itertext()) for u in r.iter("url"))
        recs.append({"id": t("rec-number"), "key": "", "author": authors[0].split(",")[0] if authors else "",
                     "year": t("dates/year"), "title": t("titles/title"),
                     "fulltext": ("internal-pdf://" in urls) or (".pdf" in urls.lower())})
    return recs

def load_ris(p):
    recs, cur = [], {}
    for line in open(p, encoding="utf-8", errors="ignore"):
        m = re.match(r"^([A-Z][A-Z0-9])  - ?(.*)$", line.rstrip("\n"))
        if not m: continue
        k, v = m.groups()
        if k == "TY": cur = {"id": "", "key": "", "author": "", "year": "", "title": "", "fulltext": False}
        elif k == "ER": recs.append(cur); cur = {}
        elif k in ("AU", "A1") and not cur.get("author"): cur["author"] = v.split(",")[0]
        elif k in ("PY", "Y1", "DA") and not cur.get("year"): cur["year"] = v[:4]
        elif k in ("TI", "T1") and not cur.get("title"): cur["title"] = v
        elif k == "ID": cur["id"] = v.strip()
        elif k in ("L1", "L4") or (k == "UR" and v.lower().endswith(".pdf")): cur["fulltext"] = True
    return recs

def load_bib(p):
    txt = open(p, encoding="utf-8", errors="ignore").read()
    recs = []
    for m in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,(.*?)\n\}", txt, re.S):
        key, body = m.groups()
        f = lambda n: (re.search(n + r"\s*=\s*[{\"](.*?)[}\"]\s*,?\s*\n", body, re.S | re.I) or [None, ""])[1]
        recs.append({"id": "", "key": key, "author": f("author").split(",")[0].split(" and ")[0].strip("{} "),
                     "year": (f("year") or f("date"))[:4], "title": f("title"),
                     "fulltext": bool(re.search(r"\bfile\s*=", body, re.I))})
    return recs

def load_csl(p):
    recs = []
    for it in json.load(open(p)):
        a = (it.get("author") or [{}])[0]
        y = str(((it.get("issued") or {}).get("date-parts") or [[""]])[0][0])
        recs.append({"id": "", "key": it.get("id", ""), "author": a.get("family", ""), "year": y,
                     "title": it.get("title", ""), "fulltext": False})
    return recs

def load_library(p):
    pl = p.lower()
    if pl.endswith(".xml"): return load_endnote_xml(p)
    if pl.endswith(".ris"): return load_ris(p)
    if pl.endswith(".bib"): return load_bib(p)
    if pl.endswith(".json"): return load_csl(p)
    raise SystemExit("Unknown library format: " + p)

def draft_text(p):
    if p.lower().endswith(".docx"):
        with zipfile.ZipFile(p) as z:
            xml = z.read("word/document.xml").decode("utf8", "ignore")
        recnums = re.findall(r"&lt;RecNum&gt;(\d+)&lt;/RecNum&gt;|<RecNum>(\d+)</RecNum>", xml)
        text = re.sub(r"<w:p[ >]", "\n<w:p ", xml)
        text = html.unescape(re.sub(r"<[^>]+>", "", text))
        return text, [a or b for a, b in recnums]
    return open(p, encoding="utf-8", errors="ignore").read(), []

def extract(text):
    cites = []
    for grp in re.findall(r"\{([^{}]+?)\}", text):
        for part in grp.split(";"):
            part = part.strip()
            m = re.match(r"^(.+?),\s*(\d{4})[a-z]?\s*(?:#\s*(\d+))?", part)
            if m and len(m.group(1)) < 80:
                cites.append({"raw": "{" + part + "}", "author": m.group(1).split(",")[0].strip(), "year": m.group(2), "id": m.group(3) or ""})
    for k in re.findall(r"(?<![\w.])@([A-Za-z][\w:.-]*\d{4}[\w:-]*)", text):
        cites.append({"raw": "@" + k, "key": k})
    return cites

def match(c, recs):
    if c.get("key"): return [r for r in recs if r["key"] == c["key"]]
    if c.get("id"): return [r for r in recs if r["id"] == c["id"]]
    return [r for r in recs if norm(r["author"]) == norm(c["author"]) and r["year"] == c["year"]]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--library", required=True); ap.add_argument("--draft", action="append", required=True)
    ap.add_argument("--out")
    a = ap.parse_args()
    recs = load_library(a.library)
    rows, bad = [], 0
    for d in a.draft:
        text, recnums = draft_text(d)
        cites = extract(text) + [{"raw": f"EndNote field RecNum {n}", "id": n} for n in recnums]
        seen = set()
        for c in cites:
            if c["raw"] in seen: continue
            seen.add(c["raw"])
            m = match(c, recs)
            if not m: status = "NOT IN LIBRARY"
            elif len(m) > 1 and not (c.get("id") or c.get("key")): status = "AMBIGUOUS (add record number)"
            elif not m[0]["fulltext"]: status = "NO FULL TEXT"
            else: status = "OK"
            if status != "OK": bad += 1
            rows.append((d, c["raw"], (m[0]["title"][:70] if m else ""), status))
    out = ["| Draft | Citation | Matched record | Status |", "|---|---|---|---|"]
    out += [f"| {d} | {c} | {t} | {s} |" for d, c, t, s in rows]
    out.append(f"\n{len(rows)} citations checked, {bad} problem(s). Library records: {len(recs)}.")
    report = "\n".join(out)
    if a.out: open(a.out, "w").write(report)
    print(report)
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
