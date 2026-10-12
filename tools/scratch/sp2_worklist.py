"""Second Pass work list (#305): Contents lines with no text. Run from the repo root with S=<scratchpad>; writes $S/sp2/work.json. Then sp2_kids.py adds the items beneath each line and the page-unknown lines."""
import json, re, sys, os, collections
from pathlib import Path
sys.path.insert(0, "tools")
from vecrescue.pages import issue_pdfs, wayback_issue_pdfs, read_contents
from vecrescue.pipeline import pdf_links, read_issues
from vecrescue.corrections import Corrections
src, wb = Path("sources/sjt/Vector"), Path("sources/wayback")
issues = Corrections.load(Path("corrections.yaml")).apply_catalogue(read_issues(Path("sources/php-site") if (Path("sources/php-site")/"issues"/"index.xml").is_file() else src))
pdfs = issue_pdfs(issues, src, wayback_issue_pdfs(wb))
links = pdf_links(pdfs, Path("build"))
contents = read_contents(Path("transcriptions/contents"))
SKIP = re.compile(r'advertis|form\b|forms\b|subscri|membership renewal|registration form|submission details', re.I)
DAMAGED = {("3","4"),("7","4"),("16","4"),("2","2")}
work, nopdf, nopage, skipped = [], [], [], collections.Counter()
for key, doc in sorted(contents.items(), key=lambda kv:(float(kv[0][0]), kv[0][1])):
    if key in DAMAGED: continue
    items = doc["items"]
    pages = sorted({int(i["page"]) for i in items if str(i.get("page","")).isdigit()})
    for idx, it in enumerate(items):
        if "title" not in it or it.get("file") or it.get("vid"): continue
        if SKIP.search(it["title"]): skipped[it["title"]] += 1; continue
        rec = dict(issue=f"{key[0]}:{key[1]}", stem=f"v{key[0]}n{key[1]}", idx=idx, title=it["title"], author=it.get("author"), page=it.get("page"), note=it.get("note"))
        if key not in pdfs or key not in links: nopdf.append(rec); continue
        rec["pdf"] = str(pdfs[key]); rec["offset"] = links[key][1]
        p = it.get("page")
        if not str(p).isdigit(): nopage.append(rec); continue
        later = [q for q in pages if q > int(p)]
        rec["next_page"] = later[0] if later else None
        work.append(rec)
print("work", len(work), "nopdf", len(nopdf), "nopage", len(nopage), "skipped", sum(skipped.values()))
print(collections.Counter(r["issue"] for r in nopdf))
for r in nopage[:15]: print("NOPAGE", r["issue"], r["title"])
json.dump(dict(work=work, nopdf=nopdf, nopage=nopage), open(os.environ["S"]+"/sp2/work.json","w"), ensure_ascii=False, indent=1)
print(skipped.most_common(12))
