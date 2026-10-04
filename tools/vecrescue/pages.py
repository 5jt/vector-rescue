"""Issue #9: the home page and one page per issue.

Issue pages live at /<vol>/<issue>/, the old site's URL form, and list
every indexed article in page order: those converted are linked, the
others shown as not yet online. A combined issue (e.g. 24:2&3) also has
a page at its second number, pointing to the first.
"""

import html
import re
import shutil
import subprocess
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
    """{(volume, issue): path} of whole-issue PDFs published on vector.org.uk
    (uploaded to its WordPress site in 2022 and 2024; some, like 26:4, were
    made in the PHP era), as captured by the Wayback Machine."""
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


def issue_pdfs(issues, root, more_pdfs=None):
    """{(vol, issue): source PDF} for each catalogued issue: the PHP tree's
    copy where the catalogue names one, else one published on vector.org.uk."""
    out = {}
    for i in issues:
        key = (i["volume"], i["issue"])
        if i.get("pdf") and (Path(root) / "issues" / i["pdf"]).is_file():
            out[key] = Path(root) / "issues" / i["pdf"]
            continue
        for n in i.get("numbers") or [i["issue"]]:
            pdf = (more_pdfs or {}).get((i["volume"], n))
            if pdf:
                out[key] = pdf
                break
    return out


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
        if not have_pdf:  # the copy published on vector.org.uk, if captured
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
                    page_md = (docs / f"art{r['id']}" / "index.md").read_text(encoding="utf-8")
                    if "\nstatus: not online\n" in page_md:
                        title += " (PDF only)" if "](../" in page_md.split("---", 2)[2] else " (not online)"
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


def volumes(inventory, issues):
    """[(volume, [issue keys in order], year span)] in volume order; the span
    is "1984–1985", a single year, or "" if no year is known."""
    catalogue, alias = _catalogue(issues)
    keys = set(catalogue) | {(r["volume"], r["issue"]) for r in inventory if r.get("volume")}
    keys = {alias.get(k, k) for k in keys}
    by = defaultdict(list)
    for key in keys:
        by[key[0]].append(key)
    out = []
    for vol in sorted(by, key=_num):
        ordered = sorted(by[vol], key=lambda k: _num(k[1]))
        ys = sorted(y for y in (catalogue.get(k, {}).get("year") for k in ordered) if y)
        span = "" if not ys else ys[0] if ys[0] == ys[-1] else f"{ys[0]}–{ys[-1]}"
        out.append((vol, ordered, span))
    return out


def _cover(pdf, target, cache):
    """Render page 1 of PDF as a PNG at TARGET, via a cache of renders keyed
    by the PDF's name and size; False if it cannot be rendered."""
    cache = Path(cache)
    cache.mkdir(parents=True, exist_ok=True)
    cached = cache / f"{pdf.name}-{pdf.stat().st_size}.png"
    if not cached.exists():
        stem = cache / "render"
        done = subprocess.run(["pdftoppm", "-png", "-f", "1", "-l", "1", "-scale-to", str(COVER_PX),
                               "-singlefile", str(pdf), str(stem)], capture_output=True)
        if done.returncode or not stem.with_suffix(".png").exists():
            return False
        stem.with_suffix(".png").rename(cached)
    shutil.copyfile(cached, target)
    return True


COVER_PX = 360  # longer side of a rendered cover


def write_volume_pages(inventory, issues, docs, pdfs, cache):
    """A landing page /<vol>/ for each volume: the front cover of each issue
    (page 1 of its PDF), linked to the issue page; an issue without a PDF
    gets a captioned placeholder."""
    docs = Path(docs)
    catalogue, _ = _catalogue(issues)
    written = []
    for vol, keys, span in volumes(inventory, issues):
        title = f"Volume {vol}" + (f" ({span})" if span else "")
        cards = []
        for key in keys:
            issue = catalogue.get(key, {"volume": key[0], "issue": key[1]})
            no = key[1]
            caption = html.escape(f"No. {_label(issue)}" + (f" · {_date(issue)}" if _date(issue) else ""))
            alt = html.escape(f"Front cover of Vector {vol}:{_label(issue)}")
            pdf = pdfs.get(key)
            if pdf and _cover(pdf, docs / vol / no / "cover.png", cache):
                face = f'<img src="{no}/cover.png" alt="{alt}" loading="lazy">'
            else:
                face = '<span class="nocover">No cover image</span>'
            cards.append(f'<a class="cover" href="{no}/">{face}<span class="caption">{caption}</span></a>')
        lines = [_front(title), f"*Vector* volume {vol}" + (f", {span}" if span else "") + ".", "",
                 '<div class="covers" markdown="0">', *cards, "</div>"]
        path = docs / vol / "index.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        written.append(path)
    return written


def nav_toml(inventory, issues):
    """The Zensical nav: Home, then every volume with its year span."""
    entries = ['{ "Home" = "index.md" }']
    for vol, _, span in volumes(inventory, issues):
        label = f"Volume {vol}" + (f" ({span})" if span else "")
        entries.append(f'{{ "{label}" = "{vol}/index.md" }}')
    return "nav = [\n  " + ",\n  ".join(entries) + ",\n]"


def write_home_page(inventory, issues, docs):
    docs = Path(docs)
    catalogue, _ = _catalogue(issues)
    lines = [_front("Vector archive"),
             "*Vector*, the journal of the British APL Association: the archive "
             "recovered from the PHP site, converted for review.", ""]
    for vol, keys, span in volumes(inventory, issues):
        links = []
        for key in keys:
            issue = catalogue.get(key, {"volume": key[0], "issue": key[1]})
            links.append(f"[{_label(issue)}]({key[0]}/{key[1]}/)")
        lines.append(f"- [Volume {vol}]({vol}/)" + (f" ({span})" if span else "") + ": " + " · ".join(links))
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
