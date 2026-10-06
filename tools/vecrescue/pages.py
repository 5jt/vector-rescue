"""The home page and one page per volume (#9, #54, #68).

A volume page at /<vol>/ shows each issue as a tab listing every indexed
article in page order: those converted are linked, the others shown as
not yet online. Whole-issue PDFs are kept at /<vol>/<issue>/.
"""

import html
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path

import yaml

from . import stubs
from .markdown import escape
from .stubs import DAMAGED
from .wayback import is_complete_pdf

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


NO_SCAN = ("No complete scan of this issue has been found, so articles listed without a link "
           "are known only from the index ([help find one](https://github.com/5jt/vector-rescue/issues/62)).")
DOUBTFUL = "The transcription is doubtful or missing; its page says why"


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


def damaged_issue_pdfs(wayback_root):
    """{(volume, issue): path} of the truncated captures of whole-issue PDFs,
    from which only the OCR text can be recovered (#81)."""
    found = {}
    uploads = Path(wayback_root) / "vector.org.uk" / "wp-content" / "uploads"
    for path in sorted(uploads.rglob("*.pdf")) if uploads.is_dir() else []:
        for pattern in PDF_NAMES:
            m = pattern.match(path.name)
            if m and not is_complete_pdf(path.read_bytes()):
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


def _issue_name(issue):
    """“N°1, May 1984”: the tab heading of an issue on its volume page."""
    return f"N°{_label(issue)}" + (f", {_date(issue)}" if _date(issue) else "")


def tab_id(issue):
    """The anchor of an issue's tab on its volume page, as pymdownx.tabbed
    makes it from the tab heading (its slugify is set in zensical.toml)."""
    from pymdownx.slugs import slugify
    return slugify(case="lower")(_issue_name(issue), "-")


def thumbnail(thumbs, vol, no):
    """The issue's 32×45 colour cover thumbnail in THUMBS (images/covers/32x45
    in the source tree: v0101.jpg for 1:1), or None (#68)."""
    if not thumbs or not (vol.isdigit() and no.isdigit()):
        return None
    path = Path(thumbs) / f"v{int(vol):02d}{int(no):02d}.jpg"
    return path if path.is_file() else None


def _thumb(thumbs, docs, key, prefix, label=None):
    """Markdown for an issue's thumbnail, copied to DOCS/covers/, with its
    path from the page prefixed by PREFIX; "" if there is none."""
    src = thumbnail(thumbs, *key)
    if not src:
        return ""
    (Path(docs) / "covers").mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, Path(docs) / "covers" / src.name)
    return f"![Vector {key[0]}:{label or key[1]} cover]({prefix}covers/{src.name})"


def _issue_contents(docs, issue, rows, root, more_pdfs, vol, no):
    """Lines for one issue's tab: its contents table, notes, and the links to
    the whole-issue PDF or Word document, which are copied to DOCS/<vol>/<no>/."""
    folder = docs / vol / no
    folder.mkdir(parents=True, exist_ok=True)
    files = []
    for kind, text in (("pdf", "PDF"), ("doc", "Word document")):
        name = issue.get(kind)
        if name and (Path(root) / "issues" / name).is_file():
            shutil.copyfile(Path(root) / "issues" / name, folder / name)
            files.append((kind, f"[{text} of the whole issue]({no}/{name})"))
    if not any(kind == "pdf" for kind, _ in files):  # the copy published on vector.org.uk, if captured
        for n in issue.get("numbers") or [no]:
            pdf = (more_pdfs or {}).get((vol, n))
            if pdf:
                shutil.copyfile(pdf, folder / pdf.name)
                files.append(("pdf", f"[PDF of the whole issue]({no}/{pdf.name})"))
                break
    have_pdf = any(kind == "pdf" for kind, _ in files)
    lines = []
    if rows and not have_pdf and any(not r.get("href") and not r.get("section") for r in rows):
        lines += [NO_SCAN, ""]
    if rows:
        lines += ["| Page | Article | Author |", "| ---: | --- | --- |"]
        for r in rows:
            title = _row_md(r, "../")
            lines.append(f"| {r.get('page') or ''} | {title} | {_cell(r.get('author'))} |")
        if any(r.get("doubtful") for r in rows):
            lines += ["", f"⚠ {DOUBTFUL}."]
    else:
        lines.append("No articles are indexed for this issue.")
    for _, link in files:  # below the table (#68)
        lines += ["", link]
    return lines


def mark_issue_tabs(inventory, issues, docs):
    """Write `issue_tab:` into the front matter of each article page with a
    volume, the anchor of its issue's tab on the volume page, so that the
    article's “Vector 2:3, page 60” line links there (#68); and point links
    in the text to the old issue pages at the same tabs."""
    docs = Path(docs)
    catalogue, alias = _catalogue(issues)

    def tab(vol, no):
        key = alias.get((vol, no), (vol, no))
        return tab_id(catalogue.get(key, {"volume": key[0], "issue": key[1]}))

    def relink(m):  # a link in the text to an old issue page (links.py)
        return f"](../{m.group(1)}/#{tab(m.group(1), m.group(2))})"

    count = 0
    for r in inventory:
        page = docs / f"art{r.get('id')}" / "index.md"
        if not page.is_file():
            continue
        text = page.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        head, rest = text[4:].split("\n---", 1)
        rest = re.sub(r"\]\(\.\./(\d+)/(\d+)/\)", relink, rest)
        head = re.sub(r"^issue_tab: .*\n?", "", head, flags=re.M).rstrip("\n")
        if r.get("volume"):
            head += f"\nissue_tab: {tab(r['volume'], r['issue'])}"
            count += 1
        page.write_text(f"---\n{head}\n---{rest}", encoding="utf-8")
    for page in sorted(docs.glob("v*n*-p*/index.md")):  # pieces with no index entry (#93)
        text = page.read_text(encoding="utf-8")
        head, rest = text[4:].split("\n---", 1)
        fm = yaml.safe_load(head) or {}
        if fm.get("volume") and "\nissue_tab:" not in "\n" + head:
            page.write_text(f"---\n{head}\nissue_tab: {tab(str(fm['volume']), str(fm['issue']))}\n---{rest}", encoding="utf-8")
            count += 1
    return count


def _volume_title(vol, span):
    return f"Volume {vol}" + (f", {span}" if span else "")


def read_contents(folder):
    """{(volume, issue): contents} from the transcribed Contents pages in
    FOLDER (transcriptions/contents/v<V>n<N>.yaml, #93)."""
    out = {}
    for path in sorted(Path(folder).glob("v*.yaml")) if folder and Path(folder).is_dir() else []:
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        out[(str(doc["volume"]), str(doc["issue"]))] = doc
    return out


def _as_list(x):
    return [] if x is None else x if isinstance(x, list) else [x]


def piece_name(file):
    """The page folder of a piece with no index entry: its file’s stem."""
    return Path(file).stem


def publish_unindexed(transcriptions, docs, pdf_links=None):
    """A page docs/<stem>/ for each transcription of a printed piece with no
    index entry (transcriptions/unindexed/, #93), linked to its issue PDF."""
    written = []
    folder = Path(transcriptions or "") / "unindexed"
    for path in sorted(folder.glob("v*.md")) if transcriptions and folder.is_dir() else []:
        fm, _ = stubs.read_transcription(path)
        key = (str(fm.get("volume")), str(fm.get("issue")))
        link = None
        if key in (pdf_links or {}) and str(fm.get("page") or "").isdigit():
            rel, offset = pdf_links[key]
            link = f"../{rel}#page={int(fm['page']) + offset}"
        record = {"id": None, "page": fm.get("page")}
        written.append(stubs.write_transcribed(record, docs, path, link and link[3:], name=path.stem))
    return written


def issue_rows(docs, contents, index_rows, pdf_link=None):
    """The rows of an issue’s table (#93): from its transcribed Contents page
    if there is one, else from its index records in page order. Each row is
    a dict: section, indent, page, title, author, href (from the site root,
    or None), q (quality) and doubtful. A line links to its article page (an
    index record or a piece with no index entry), else to the issue PDF at
    its page (PDF_LINK: (path, offset)), else to nothing."""
    docs = Path(docs)
    titles = {r["id"]: r for r in index_rows}

    def article(vid, indent, page=None, title=None, author=None):
        r = titles.get(vid, {})
        q, doubtful = quality(docs, vid)
        doubtful = doubtful or q == "failed"
        return {"indent": indent, "page": page if page is not None else r.get("page"),
                "title": title or r.get("title"), "author": author if author is not None else ", ".join(r.get("authors") or []),
                "href": f"art{vid}/" if _converted(docs, vid) else None, "q": q, "doubtful": doubtful, "vid": vid}

    def pdf_href(page):
        if pdf_link and str(page or "").isdigit():
            return f"{pdf_link[0]}#page={int(page) + pdf_link[1]}"
        return None

    rows = []
    if not contents:
        for r in sorted(index_rows, key=lambda r: (_num(r.get("page")), r.get("title") or "")):
            rows.append(article(r["id"], 0))
        return rows
    for item in contents.get("items", []):
        files, vids = _as_list(item.get("file")), _as_list(item.get("vid"))
        indent = item.get("indent", 0)
        if "section" in item:
            row = {"section": True, "indent": 0, "page": item.get("page"), "title": item["section"],
                   "author": "", "href": None, "q": None, "doubtful": False}
            if files and (docs / piece_name(files[0]) / "index.md").exists():
                row["href"] = piece_name(files[0]) + "/"
            rows.append(row)
            continue
        title, author, page = item.get("title"), item.get("author") or "", item.get("page")
        files = [f for f in files if (docs / piece_name(f) / "index.md").exists()]  # published
        if files:
            q, doubtful = quality(docs, name=piece_name(files[0]))
            rows.append({"indent": indent, "page": page, "title": title, "author": author,
                         "href": piece_name(files[0]) + "/", "q": q, "doubtful": doubtful})
            for f in files[1:]:
                page_md = docs / piece_name(f) / "index.md"
                fm = stubs.read_transcription(page_md)[0] if page_md.exists() else {}
                q, doubtful = quality(docs, name=piece_name(f))
                rows.append({"indent": indent + 1, "page": fm.get("page"), "title": fm.get("title") or piece_name(f),
                             "author": ", ".join(fm.get("authors") or []), "href": piece_name(f) + "/", "q": q, "doubtful": doubtful})
            rows += [article(v, indent + 1) for v in vids]
        elif len(vids) == 1:
            rows.append(article(vids[0], indent, page, title, author))
        else:
            href = pdf_href(page)
            rows.append({"indent": indent, "page": page, "title": title, "author": author, "href": href,
                         "q": "PDF" if href else "missing", "doubtful": False, "pdf": bool(href)})
            rows += [article(v, indent + 1) for v in vids]
    return rows


def _row_md(row, prefix):
    """A table row’s article cell: the title, linked from a page PREFIX
    levels below the site root, and indented."""
    title = _cell(row["title"])
    if row.get("section"):
        title = f"**{title}**"
    if row.get("href"):
        title = f"[{title}]({prefix}{row['href']})"
    if row.get("pdf"):
        title += " (PDF)"
    if row.get("vid") and row.get("href"):  # a stub for an index record
        title += {"PDF": " (PDF only)", "failed": " (PDF only)", "OCR": " (not online)"}.get(row["q"], "")
    if row.get("doubtful"):
        title += f' <span class="doubtful" title="{DOUBTFUL}">⚠</span>'
    return "&emsp;" * row.get("indent", 0) + title


def write_volume_pages(inventory, issues, root, docs, more_pdfs=None, thumbs=None, contents=None, pdf_links=None):
    """A page /<vol>/ for each volume (#68): its issues as tabs, each headed
    by the issue's colour thumbnail, number and date, and holding the
    issue's contents in page order (converted articles linked, the others
    shown as not yet online) with the whole-issue PDF linked below. A
    combined issue (e.g. 24:2&3) is one tab."""
    docs = Path(docs)
    catalogue, alias = _catalogue(issues)
    articles = defaultdict(list)
    for r in inventory:
        if r.get("volume"):
            key = (r["volume"], r["issue"])
            articles[alias.get(key, key)].append(r)
    written = []
    for vol, keys, span in volumes(inventory, issues):
        lines = ["---", f"title: {_volume_title(vol, span)}",
                 "hide: [toc]",  # the tabs are the navigation; a toc would point into hidden tabs
                 "---", "", ""]
        for key in keys:
            issue = catalogue.get(key, {"volume": vol, "issue": key[1]})
            rows = issue_rows(docs, (contents or {}).get(key), articles.get(key, []), (pdf_links or {}).get(key))
            thumb = _thumb(thumbs, docs, key, "../", _label(issue))
            lines += [f'=== "{(thumb + " ") if thumb else ""}{_issue_name(issue)}"', "",
                      # the tab label is not salient enough (#79); the heading's own id
                      # leaves the tab its anchor (pymdownx would otherwise suffix it)
                      f"    ## {_issue_name(issue)} {{ #contents-{tab_id(issue)} }}", ""]
            lines += [("    " + x) if x else "" for x in
                      _issue_contents(docs, issue, rows, root, more_pdfs, vol, key[1])]
            lines.append("")
        path = docs / vol / "index.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines), encoding="utf-8")
        written.append(path)
    return written


def nav_toml(inventory, issues):
    """The Zensical nav: Home, the full index (#79), then the volumes under
    “Volumes” (#68)."""
    entries = [f'{{ "{_volume_title(vol, span)}" = "{vol}/index.md" }}'
               for vol, _, span in volumes(inventory, issues)]
    return ('nav = [\n  { "Home" = "index.md" },\n  { "Project status" = "status/index.md" },\n'
            '  { "Full index" = "full-index/index.md" },\n  { "Tags" = "tags/index.md" },\n'
            '  { "Volumes" = [\n    '
            + ",\n    ".join(entries) + ",\n  ] },\n]")


QUALITY = (  # worst to best (#83)
    ("missing", "known only from the index: no scan has been found"),
    ("OCR", "only machine-read text survives, from a damaged copy without page images"),
    ("PDF", "the scan is linked, with its machine-read text folded away"),
    ("failed", "transcription was attempted and abandoned; the scan is linked"),
    ("draft", "transcribed from the scan, not yet reviewed"),
    ("reviewed", "transcribed from the scan and reviewed"),
    ("text", "converted from the text published online"),
)


def quality(docs, vid=None, name=None):
    """The state of an article's text, one of QUALITY, read from its page
    (art<VID>, or NAME for a piece with no index entry); and whether its
    transcription is doubtful (#83)."""
    path = Path(docs) / (name or f"art{vid}") / "index.md"
    if not (vid or name) or not path.exists():
        return "missing", False
    page = path.read_text(encoding="utf-8")
    head = (page.split("---", 2) + ["", ""])[1]
    warned = "\nwarning: " in head
    if "\nstatus: transcribed" in head:
        return ("reviewed" if "\nreview: reviewed" in head else "draft"), warned
    if "\nstatus: not online" in head:
        return ("failed" if warned else "OCR" if DAMAGED in page else "PDF"), False
    return "text", False


def _badge(q):
    return f'<span class="quality q-{q.lower()}" title="{dict(QUALITY)[q]}">{q}</span>'


def write_index_page(inventory, issues, docs, contents=None, pdf_links=None):
    """The full index on a page of its own (#79), so a reader can search just
    the index with the browser: every line of every issue’s Contents page
    (#93; the index records, for an issue whose Contents page is not
    transcribed), in order, linked as on the volume pages; then the
    articles published online only. With the quality of each one’s text,
    and their totals, to gauge progress (#83)."""
    docs = Path(docs)
    catalogue, alias = _catalogue(issues)
    articles = defaultdict(list)
    for r in inventory:
        if r.get("volume"):
            key = (r["volume"], r["issue"])
            articles[alias.get(key, key)].append(r)
    lines, totals = [], Counter()

    def add(vol, no, r):
        q = r["q"] or "missing"
        totals[q] += 1
        lines.append(f"| {vol} | {no} | {r.get('page') or ''} | {_badge(q)} | {_row_md(r, '../')} | {_cell(r.get('author'))} |")

    for vol, keys, _ in volumes(inventory, issues):
        for key in keys:
            issue = catalogue.get(key, {"volume": vol, "issue": key[1]})
            v, n = f"[{vol}](../{vol}/)", f"[{_label(issue)}](../{vol}/#{tab_id(issue)})"
            link = (pdf_links or {}).get(key)
            for r in issue_rows(docs, (contents or {}).get(key), articles.get(key, []), link):
                heading = link and not r.get("page") and not r.get("href")  # a group heading on the Contents page
                if not r.get("section") and not heading:
                    add(v, n, r)
    online = [r for r in inventory if r.get("id") and not r.get("volume") and _converted(docs, r["id"])]
    for r in sorted(online, key=lambda r: (r.get("online") or "9999", r["id"])):
        q, doubtful = quality(docs, r["id"])
        add("", "", {"title": r.get("title"), "author": ", ".join(r.get("authors") or []), "href": f"art{r['id']}/",
                     "q": q, "doubtful": doubtful, "indent": 0})
    head = [_front("Full index"),
            "Every item on the Contents page of every issue of *Vector*, in the order printed, linked to its "
            "text where we have it, else to its page in the issue PDF; then the articles published online only. "
            "Use your browser’s Find to search it.", "",
            "Quality of the text: " + " · ".join(f"{_badge(q)} {totals[q]}" for q, _ in QUALITY)
            + f" (of {sum(totals.values())})", "",
            "| volume | issue | page | quality | article | author |", "|:---:|:---:|---:|:---:|---|---|"]
    path = docs / "full-index" / "index.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(head + lines) + "\n", encoding="utf-8")
    return path


def tag_id(label):
    """The anchor of a tag on the Tags page (as the article template writes it)."""
    return "tag-" + label.replace(" ", "-")


def write_tags_page(vocabulary, docs):
    """The Tags page (#95): each tag of VOCABULARY (transcriptions/tags.yaml)
    with the article pages in DOCS that carry it, in printed order. Returns
    the path, and the tags found on pages but not in the vocabulary."""
    docs = Path(docs)
    tags = yaml.safe_load(Path(vocabulary).read_text(encoding="utf-8"))["tags"] if vocabulary and Path(vocabulary).is_file() else []
    known = [t["label"] for t in tags]
    pages = defaultdict(list)
    for page in sorted(docs.glob("*/index.md")):
        text = page.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        fm = yaml.safe_load(text.split("---", 2)[1]) or {}
        for t in fm.get("tags") or []:
            pages[t].append(fm)
            pages[t][-1] = dict(fm, _href=page.parent.name)
    unknown = sorted(set(pages) - set(known))
    lines = [_front("Tags"),
             "The transcribed articles by subject. An article may carry more than one tag. "
             "Tagging follows the transcription, volume by volume.", ""]
    lines += [" · ".join(f"[{t}](#{tag_id(t)}) ({len(pages[t])})" for t in known if pages[t]), ""]
    for t in tags:
        items = pages.get(t["label"])
        if not items:
            continue
        lines += [f"## {t['label']} {{ #{tag_id(t['label'])} }}", "", f"*{t['about']}*", ""]
        for fm in sorted(items, key=lambda f: (_num(f.get("volume")), _num(f.get("issue")), _num(f.get("page")), f.get("title") or "")):
            where = f"{fm['volume']}:{fm['issue']}" if fm.get("volume") else "online"
            who = ", ".join(fm.get("authors") or [])
            lines.append(f"- {where} [{_cell(fm.get('title'))}](../{fm['_href']}/)" + (f", {escape(who)}" if who else ""))
        lines.append("")
    path = docs / "tags" / "index.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    return path, unknown


LOGO = "assets/images/vector-logo.png"  # vector.org.uk’s, white and yellow


def write_home_page(inventory, issues, docs, thumbs=None):
    """The home page (#68): the Vector logo, an introduction, and a table of
    the volumes with their issues’ colour thumbnails, each linked to the
    issue’s tab on its volume page; then the articles never printed."""
    docs = Path(docs)
    catalogue, alias = _catalogue(issues)
    lines = [_front("The Vector Archive"),
             f'<div class="masthead" markdown="0"><img src="{LOGO}" alt="Vector, journal of the BAA"></div>', "",
             "# The Vector Archive", "",
             "The [British APL Association](https://britishaplassociation.org) published its journal "
             "*Vector* in print and online between 1984 and 2022.", "",
             "The complete archive is here recovered from multiple sources and published online in a form "
             "legible to search engines and AI agents, most of it for the first time.", "",
             "| volume | years | N°1 | N°2 | N°3 | N°4 |",
             "|:------:|:-----:|:---:|:---:|:---:|:---:|"]
    for vol, keys, span in volumes(inventory, issues):
        cells = [[] for _ in range(4)]
        for key in keys:
            issue = catalogue.get(key, {"volume": vol, "issue": key[1]})
            face = _thumb(thumbs, docs, key, "", _label(issue)) or f"{vol}:{_label(issue)}"
            link = f"[{face}]({vol}/#{tab_id(issue)})"
            numbers = [n for n in (issue.get("numbers") or [key[1]])]
            cols = [int(n) - 1 for n in numbers if n.isdigit() and 1 <= int(n) <= 4]
            if not cols:  # a supplement such as 23:4.1 goes with its issue
                cols = [min(3, max(0, int(_num(key[1])) - 1))] if _num(key[1]) != float("inf") else [3]
            for c in cols:
                cells[c].append(link)
        lines.append(f"| [{vol}]({vol}/) | {span} | " + " | ".join(" ".join(c) for c in cells) + " |")
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
