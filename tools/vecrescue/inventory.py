"""Read the PHP site's master index (index.xml) into plain records."""

import os
import re
from pathlib import Path
import xml.etree.ElementTree as ET

VEC = "{http://www.vector.org.uk/archive-schema}"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
DC = "{http://purl.org/dc/elements/1.1/}"
FOAF = "{http://xmlns.com/foaf/0.1/}"


def _text(el):
    return (el.text or "").strip() or None if el is not None else None


def _author(creator):
    name = creator.find(FOAF + "name")
    if name is None:
        return " ".join((creator.text or "").split()) or None
    parts = [_text(name.find(FOAF + k)) for k in ("givenName", "familyName")]
    return " ".join(p for p in parts if p) or None


def _source(root, el):
    path = _text(el)
    rec = {"fmt": el.get("fmt"), "path": path, "exists": False, "utf8": None}
    if path and not path.startswith("http"):
        f = root / path
        if f.is_file():
            rec["exists"] = True
            try:
                f.read_bytes().decode("utf-8")
                rec["utf8"] = True
            except UnicodeDecodeError:
                rec["utf8"] = False
    return rec


def _date(el):
    return el.get("date") if el is not None else None


def read_index(root):
    """Return one record per rdf:Description in ROOT/index.xml, in file order."""
    root = Path(root)
    records = []
    for d in ET.parse(root / "index.xml").iter(RDF + "Description"):
        pub = d.find(VEC + "published")
        records.append({
            "id": _text(d.find(DC + "identifier")),
            "title": " ".join((_text(d.find(DC + "title")) or "").split()) or None,
            "authors": [a for a in map(_author, d.findall(DC + "creator")) if a],
            "volume": pub.get("volume") if pub is not None else None,
            "issue": pub.get("issue") if pub is not None else None,
            "page": pub.get("page") if pub is not None else None,
            "received": _date(d.find(VEC + "received")),
            "online": _date(d.find(VEC + "online")),
            "sources": [_source(root, s) for s in d.findall(VEC + "source")],
        })
    return records


def article_source(record):
    """(format, path) of the source to convert: XHTML if present, else HTML
    (decoded by legacy.decode), else a page captured by the Wayback Machine;
    None if none of these."""
    for fmt in ("XHTML", "HTML", "WAYBACK"):
        for s in record["sources"]:
            if s["fmt"] == fmt and s["exists"]:
                return fmt, s["path"]
    return None


# Wayback Machine (issue #25) -------------------------------------------------

def _page_record(vid, page):
    """A record for a captured art page that no captured index lists."""
    import lxml.html
    doc = lxml.html.fromstring(page.read_bytes())
    art = doc.xpath('//div[@id="article"]')[0]
    title = art.xpath('.//*[@id="title"]') or art.findall(".//h1")
    author = art.xpath('.//*[@id="author"]')
    byline = " ".join(author[0].text_content().split()) if author else ""
    byline = re.sub(r"\s*\([^)]*\)", "", re.sub(r"^(?:by|from)\s+", "", byline, flags=re.I))
    return {"id": vid, "title": " ".join(title[0].text_content().split()) if title else None,
            "authors": [a.strip() for a in re.split(r"\s*(?:,|&| and )\s*", byline) if a.strip()],
            "volume": None, "issue": None, "page": None, "received": None, "online": None,
            "metadata": "page", "in_press": _in_press(doc)}


def _in_press(doc):
    crumb = doc.xpath('//div[@id="result"]/*[1]')
    return bool(crumb) and "in press" in crumb[0].text_content().lower()


def merge_wayback(records, wayback_root, src_root):
    """Records from the PHP tree, updated and extended from the Wayback
    Machine: the 2021 index (issue assignments, new articles) and captured
    art pages for articles no captured index lists."""
    site = Path(wayback_root) / "archive.vector.org.uk"
    if not (site / "index.xml").is_file():
        return records
    by_id = {r["id"]: r for r in records if r["id"]}

    def source(vid):
        page = site / f"art{vid}.html"
        if not page.is_file():
            return []
        return [{"fmt": "WAYBACK", "path": os.path.relpath(page, src_root), "exists": True, "utf8": True}]

    for o in read_index(site):
        r = by_id.get(o["id"])
        if r is None and o["id"]:
            new = dict(o, sources=source(o["id"]), metadata="index-2021", in_press=o["volume"] is None)
            records.append(new)
            by_id[o["id"]] = new
        elif r is not None and r["volume"] is None and o["volume"]:
            r.update(volume=o["volume"], issue=o["issue"], page=o["page"], metadata="index-2021")
    for r in records:  # the old site's own rendering, for the report to check against
        page = site / f"art{r['id']}.html"
        if r["id"] and page.is_file() and not any(s["fmt"] == "WAYBACK" for s in r["sources"]):
            r["captured"] = os.path.relpath(page, src_root)
    for page in sorted(site.glob("art*.html")):
        vid = page.stem[3:]
        if re.fullmatch(r"\d{8}", vid) and vid not in by_id:
            rec = _page_record(vid, page)
            rec["sources"] = source(vid)
            records.append(rec)
            by_id[vid] = rec
    return records


def xhtml_source(record):
    """The existing XHTML source path of RECORD, or None."""
    for s in record["sources"]:
        if s["fmt"] == "XHTML" and s["exists"]:
            return s["path"]
    return None


def read_issues(root):
    """The issue catalogue, ROOT/issues/index.xml, in file order."""
    issues = []
    for el in ET.parse(Path(root) / "issues" / "index.xml").iter("issue"):
        files = {s.get("fmt"): (s.text or "").strip().strip('"') or None for s in el.findall("source")}
        span = int(el.get("span") or 1)
        named = re.findall(r"\d+", el.get("title") or "") if re.match(r"Nos?\.", el.get("title") or "") else []
        numbers = named or [str(int(el.get("issue")) + k) for k in range(span)] \
            if (el.get("issue") or "").isdigit() else [el.get("issue")]
        issues.append({
            "volume": el.get("volume"), "issue": el.get("issue"),
            "year": el.get("year"), "month": el.get("month"),
            "title": el.get("title"), "span": span, "numbers": numbers,
            "pdf": files.get("PDF"), "doc": files.get("DOC"),
        })
    return issues
