"""Issue #2: turn the article head block into front matter.

The hand-coded articles open with a run of title elements (prefix, title,
subtitle, byline, abstract) and carry workflow furniture (publication
status, validator link). extract_head removes them from the document and
returns front-matter fields plus the lead blocks to show above the body.
"""

import re

from .markdown import inline

DROP = ('//ul[@id="publication"]', '//p[@id="validation"]')
META = ("received", "online", "editor", "description", "keywords")
CHECK = ("vid", "volume", "issue", "page")
HEAD_ONLY = ("meta", "title", "link")  # belong in <head>; stray markup can push them into <body>
BODY_START = ("p", "h2", "h3", "h4", "h5", "h6", "pre", "ul", "ol", "dl",
              "table", "blockquote", "figure")


def _text(el):
    return " ".join(el.text_content().split())


def _classes(el):
    return (el.get("class") or "").split()


def _kind(el):
    """Which part of the head block EL is, or None if the body has begun."""
    tag, id_, cls = el.tag, el.get("id"), _classes(el)
    if tag == "h1":
        if "prefix" in cls:
            return "prefix"
        if id_ == "title" or "title" in cls:
            return "title"
        if id_ == "subtitle" or "subtitle" in cls:
            return "subtitle"
        if id_ == "author":
            return "byline"
        return "h1"
    if tag == "p" and id_ == "author":
        return "byline"
    if tag in ("p", "div") and (id_ == "abstract" or "abstract" in cls):
        return "abstract"
    return None


def _meta(doc):
    return {m.get("name"): " ".join((m.get("content") or "").split())
            for m in doc.iter("meta") if m.get("name")}


def extract_head(doc, record, notes):
    for xpath in DROP:
        for el in doc.xpath(xpath):
            el.getparent().remove(el)
    body = doc.find("body")
    meta = _meta(doc)
    for el in list(body):
        if el.tag in HEAD_ONLY:
            notes.append({"kind": "head-element-in-body", "tag": el.tag})
            body.remove(el)
    found = {}
    for el in list(body):
        if not isinstance(el.tag, str):
            continue
        kind = _kind(el)
        if kind is None:
            if el.tag in BODY_START:
                break
            continue  # decoration inside the head block: leave it in place
        if kind == "h1":
            if "title" not in found:
                kind = "title"
            elif "subtitle" not in found and "byline" not in found:
                kind = "subtitle"
            else:
                break
            notes.append({"kind": f"unmarked-h1-as-{kind}", "text": _text(el)})
        if kind == "subtitle":
            found.setdefault(kind, []).append(el)
        elif kind in found:
            break
        else:
            found[kind] = el
        body.remove(el)

    fm = {"vid": record["id"], "title": record["title"]}
    lead = []
    if "prefix" in found:
        fm["prefix"] = _text(found["prefix"])
    if "subtitle" in found:
        fm["subtitle"] = " / ".join(_text(el) for el in found["subtitle"])
    if record.get("authors"):
        fm["authors"] = record["authors"]
    if "byline" in found and _text(found["byline"]):
        fm["byline"] = _text(found["byline"])
    for k in ("volume", "issue", "page"):
        if record.get(k) is not None:
            fm[k] = record[k]
    for k in META:
        value = record.get(k) or meta.get(k)
        if k == "keywords" and value:
            value = [w.strip() for w in value.split(",") if w.strip()]
        if value:
            fm[k] = value
    if "abstract" in found and _text(found["abstract"]):
        fm["abstract"] = _text(found["abstract"])

    def lead_para(el, cls):
        md = inline(el)
        if md:
            lead.append(f"{md}\n{{ .{cls} }}")

    for el in found.get("subtitle", []):
        lead_para(el, "subtitle")
    if "byline" in found:
        lead_para(found["byline"], "byline")
    if "abstract" in found:
        el = found["abstract"]
        for p in (el.findall("p") if el.tag == "div" else [el]):
            lead_para(p, "abstract")

    for k in CHECK:
        index = record["id"] if k == "vid" else record.get(k)
        if meta.get(k) and index is not None and meta[k] != index:
            notes.append({"kind": "meta-disagrees", "field": k,
                          "meta": meta[k], "index": index})
    if "title" in found and record.get("title"):
        page = _text(found["title"])
        if _norm(page) not in _norm(record["title"]):
            notes.append({"kind": "title-differs", "page": page,
                          "index": record["title"]})
    return fm, lead


def _norm(s):
    return re.sub(r"\W+", " ", s).strip().lower()
