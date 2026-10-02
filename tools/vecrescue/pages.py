"""Issue #9: the home page and one page per issue.

Issue pages live at /<vol>/<issue>/, the old site's URL form, and list
every indexed article in page order: those converted are linked, the
others shown as not yet online. A combined issue (e.g. 24:2&3) also has
a page at its second number, pointing to the first.
"""

import re
import shutil
from collections import defaultdict
from pathlib import Path

from .markdown import escape
from .wayback import is_complete_pdf

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def _num(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return float("inf")


def _cell(text):
    return escape(text or "").replace("|", "\\|")


def _converted(docs, vid):
    return vid and (Path(docs) / f"art{vid}" / "index.md").exists()


def _label(issue):
    return "&".join(issue.get("numbers") or [issue["issue"]])


def _date(issue):
    month = issue.get("month")
    month = MONTHS[int(month) - 1] if month and month.isdigit() and 1 <= int(month) <= 12 else ""
    return " ".join(x for x in (month, issue.get("year") or "") if x)


def _catalogue(issues):
    """{(vol, issue): issue} and {(vol, alias issue): (vol, issue)}."""
    catalogue, alias = {}, {}
    for i in issues:
        catalogue[(i["volume"], i["issue"])] = i
    for i in issues:  # a combined issue's other numbers point to where it is filed
        for n in i.get("numbers") or [i["issue"]]:
            if (i["volume"], n) not in catalogue:
                alias[(i["volume"], n)] = (i["volume"], i["issue"])
    return catalogue, alias


PDF_NAMES = (
    re.compile(r"^VOL\.(\d+)-NO\.(\d+)\b.*\.pdf$", re.I),   # VOL.1-NO.1-MAY-1984.pdf
    re.compile(r"^v(\d\d)(\d)(?:-\d)?\.pdf$", re.I),          # v241-1.pdf, v252-3.pdf
    re.compile(r"^Vector(\d\d)(\d)\.pdf$", re.I),             # Vector264.pdf
)


def wayback_issue_pdfs(wayback_root):
    """{(volume, issue): path} of whole-issue PDFs the WordPress site
    published, as captured by the Wayback Machine."""
    found = {}
    uploads = Path(wayback_root) / "vector.org.uk" / "wp-content" / "uploads"
    for path in sorted(uploads.rglob("*.pdf")) if uploads.is_dir() else []:
        for pattern in PDF_NAMES:
            m = pattern.match(path.name)
            if m and is_complete_pdf(path.read_bytes()):  # some captures are truncated
                found.setdefault((str(int(m.group(1))), m.group(2)), path)
                break
    return found


def _front(title):
    return f"---\ntitle: {title}\n---\n\n"


def write_issue_pages(inventory, issues, root, docs, more_pdfs=None):
    docs = Path(docs)
    catalogue, alias = _catalogue(issues)
    articles = defaultdict(list)
    for r in inventory:
        if r.get("volume"):
            key = (r["volume"], r["issue"])
            articles[alias.get(key, key)].append(r)
    keys = set(catalogue) | set(articles)
    written = []
    for key in sorted(keys, key=lambda k: (_num(k[0]), _num(k[1]))):
        vol, no = key
        issue = catalogue.get(key, {"volume": vol, "issue": no})
        label = f"{vol}:{_label(issue)}"
        folder = docs / vol / no
        folder.mkdir(parents=True, exist_ok=True)
        lines = [_front(f"Vector {label}")]
        lines.append(f"Volume {vol}, No. {_label(issue)}" +
                     (f" · {_date(issue)}" if _date(issue) else ""))
        lines.append("")
        have_pdf = False
        for kind, text in (("pdf", "PDF"), ("doc", "Word document")):
            name = issue.get(kind)
            if name and (Path(root) / "issues" / name).is_file():
                shutil.copyfile(Path(root) / "issues" / name, folder / name)
                lines += [f"[{text} of the whole issue]({name})", ""]
                have_pdf |= kind == "pdf"
        if not have_pdf:  # the copy the WordPress site published, if captured
            for n in issue.get("numbers") or [no]:
                pdf = (more_pdfs or {}).get((vol, n))
                if pdf:
                    shutil.copyfile(pdf, folder / pdf.name)
                    lines += [f"[PDF of the whole issue]({pdf.name})", ""]
                    break
        rows = sorted(articles.get(key, []), key=lambda r: (_num(r.get("page")), r.get("title") or ""))
        if rows:
            lines += ["| Page | Article | Author |", "| ---: | --- | --- |"]
            for r in rows:
                title = _cell(r.get("title"))
                if _converted(docs, r.get("id")):
                    title = f"[{title}](../../art{r['id']}/)"
                lines.append(f"| {r.get('page') or ''} | {title} | {_cell(', '.join(r.get('authors') or []))} |")
        else:
            lines.append("No articles are indexed for this issue.")
        path = folder / "index.md"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        written.append(path)
    for (vol, no), (mvol, mno) in alias.items():
        folder = docs / vol / no
        folder.mkdir(parents=True, exist_ok=True)
        main = f"Vector {mvol}:{_label(catalogue[(mvol, mno)])}"
        (folder / "index.md").write_text(
            _front(f"Vector {vol}:{no}") + f"Printed with [{main}](../{mno}/).\n", encoding="utf-8")
    return written


def write_home_page(inventory, issues, docs):
    docs = Path(docs)
    catalogue, alias = _catalogue(issues)
    keys = set(catalogue) | {(r["volume"], r["issue"]) for r in inventory if r.get("volume")}
    keys = {alias.get(k, k) for k in keys}
    volumes = defaultdict(list)
    for key in keys:
        volumes[key[0]].append(key)
    lines = [_front("Vector archive"),
             "*Vector*, the journal of the British APL Association: the archive "
             "recovered from the PHP site, converted for review.", ""]
    for vol in sorted(volumes, key=_num):
        links, years = [], set()
        for key in sorted(volumes[vol], key=lambda k: _num(k[1])):
            issue = catalogue.get(key, {"volume": key[0], "issue": key[1]})
            years.add(issue.get("year"))
            links.append(f"[{_label(issue)}]({key[0]}/{key[1]}/)")
        ys = sorted(y for y in years if y)
        span = "" if not ys else ys[0] if ys[0] == ys[-1] else f"{ys[0]}–{ys[-1]}"
        lines.append(f"- Volume {vol}" + (f" ({span})" if span else "") + ": " + " · ".join(links))
    unprinted = [r for r in inventory if r.get("id") and not r.get("volume") and _converted(docs, r["id"])]
    for heading, group in (("Published online only", [r for r in unprinted if not r.get("in_press")]),
                           ("In press, never printed", [r for r in unprinted if r.get("in_press")])):
        if not group:
            continue
        lines += ["", f"## {heading}", ""]
        for r in sorted(group, key=lambda r: (r.get("online") or "9999", r["id"])):
            who = ", ".join(r.get("authors") or [])
            lines.append(f"- [{_cell(r['title'])}](art{r['id']}/)" + (f", {escape(who)}" if who else "")
                         + (f" ({r['online']})" if r.get("online") else ""))
    path = docs / "index.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path
