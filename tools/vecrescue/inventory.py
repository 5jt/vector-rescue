"""Read the PHP site's master index (index.xml) into plain records."""

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
    """(format, path) of the source to convert: XHTML if present, else
    HTML that is valid UTF-8; None if neither."""
    for s in record["sources"]:
        if s["fmt"] == "XHTML" and s["exists"]:
            return "XHTML", s["path"]
    for s in record["sources"]:
        if s["fmt"] == "HTML" and s["exists"] and s["utf8"]:
            return "HTML", s["path"]
    return None


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
        issues.append({
            "volume": el.get("volume"), "issue": el.get("issue"),
            "year": el.get("year"), "month": el.get("month"),
            "title": el.get("title"), "span": int(el.get("span") or 1),
            "pdf": files.get("PDF"), "doc": files.get("DOC"),
        })
    return issues
