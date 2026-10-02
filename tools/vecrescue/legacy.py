"""Issue #21: normalise legacy trad/ HTML into the shape the converter handles.

The old site presented these pages with lib/present.php, which dropped the
breadcrumb navigation at top and bottom. This module does the same and also
unwraps the presentational markup of the era (font, center, Word export
divs, style-only spans), so the XHTML rules apply unchanged.
"""

import re

APL_FONT = re.compile(r"(?:face\s*=\s*[\"']?|font-family\s*:\s*[\"']?)(?:apl2741|aplx upright|aplnet)", re.I)
HOME = re.compile(r"^https?://www\.vector\.org\.uk/?$|^(?:\.\./)?index\.htm$", re.I)
NAV = re.compile(r"\?area=vect|(?:^|/)index\.htm$|display\.htm$", re.I)
UNWRAP_DIV_IDS = {"wrapper", "pageblock"}
UNWRAP_DIV_CLASSES = {"section1", "liner", "wordsection1"}


def fix_comments(text):
    """Jake's 'extended' comments, <!------- … ------->, as present.php did."""
    return re.sub(r"-{3,}>", "-->", re.sub(r"<!-{3,}", "<!--", text))


def mapped_apl(text, path, listed):
    """Why this source may hold character-mapped APL, or None."""
    if path in listed:
        return "codingprobs"
    if APL_FONT.search(text):
        return "apl-font"
    return None


def read_codingprobs(root):
    """Paths listed in the old site's tools/codingprobs.txt (mapped APL)."""
    path = root / "tools" / "codingprobs.txt"
    prefix = "http://archive.vector.org.uk/"
    if not path.is_file():
        return set()
    return {line.strip()[len(prefix):] for line in path.read_text(encoding="utf-8").splitlines()
            if line.startswith(prefix)}


def _classes(el):
    return {c.lower() for c in (el.get("class") or "").split()}


def _is_crumb(el):
    if {"crumb", "crumbs"} & _classes(el):
        return True
    if el.xpath(".//p|.//table"):
        return False
    hrefs = [a.get("href") or "" for a in el.iter("a")]
    return any(HOME.match(h) for h in hrefs) and any(NAV.search(h) for h in hrefs)


def _unwrap(el):
    tag, cls = el.tag, _classes(el)
    if tag in ("center", "o:p"):
        return True
    if tag == "font":
        return not APL_FONT.search(f'face="{el.get("face") or ""}"')
    if tag == "div":
        return (el.get("id") in UNWRAP_DIV_IDS or cls & UNWRAP_DIV_CLASSES
                or (el.get("align") and not cls and not el.get("id")))
    if tag == "span":
        return not cls or all(c.startswith("mso") for c in cls)
    return False


def normalise(doc, notes):
    body = doc.find("body")
    if body is None:
        body = doc
    crumbs = [el for el in body.iter("p", "table") if _is_crumb(el)]
    for el in crumbs:
        prev = el.getprevious()
        if prev is not None and prev.tag == "hr":
            prev.drop_tree()
        el.drop_tree()
    if crumbs:
        notes.append({"kind": "breadcrumbs-dropped", "count": len(crumbs)})
    for el in [e for e in body.iter() if isinstance(e.tag, str) and e is not body and _unwrap(e)]:
        el.drop_tag()
    return doc
