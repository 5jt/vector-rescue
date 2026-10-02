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


def decode(data):
    """Text of a legacy source, and how it was decoded: 'utf-8'; 'cp1252'
    (Windows-1252, as lib/present.php assumed); or 'mixed', where valid UTF-8
    is kept and only the bytes that are not valid UTF-8 are read as
    Windows-1252. Bytes Windows-1252 leaves undefined become U+FFFD."""
    try:
        return data.decode("utf-8"), "utf-8"
    except UnicodeDecodeError:
        pass
    out, utf8_seen, i = [], False, 0
    while i < len(data):
        try:
            chunk = data[i:].decode("utf-8")
            out.append(chunk)
            utf8_seen |= any(ord(c) > 0x7F for c in chunk)
            break
        except UnicodeDecodeError as e:
            good = data[i:i + e.start].decode("utf-8")
            out.append(good)
            utf8_seen |= any(ord(c) > 0x7F for c in good)
            bad = data[i + e.start:i + e.start + 1]
            try:
                out.append(bad.decode("cp1252"))
            except UnicodeDecodeError:
                out.append("\ufffd")
            i += e.start + 1
    return "".join(out), "mixed" if utf8_seen else "cp1252"


def fix_comments(text):
    """Jake's 'extended' comments, <!------- … ------->, as present.php did."""
    return re.sub(r"-{3,}>", "-->", re.sub(r"<!-{3,}", "<!--", text))


def mapped_apl(text, path, listed, unicode=False):
    """Why this source may hold character-mapped APL, or None.

    The suspect heuristic applies only to files that were not valid UTF-8
    (UNICODE false): accented letters in Unicode-era code are real (French
    identifiers, for instance), while mapped APL is a pre-Unicode practice.
    """
    if path in listed:
        return "codingprobs"
    if APL_FONT.search(text):
        return "apl-font"
    if "\ufffd" in text:  # bytes undefined in Windows-1252: an APL font's mapping
        return "undefined-bytes"
    if not unicode and (MAPPED_PROSE.search(text) or MAPPED_CODE.search(_code_text(text))):
        return "mapped-apl-suspect"
    return None


# Telltales of APL typed in an APL font that maps glyphs onto Latin-1
# characters: Œ before a system name (⎕io, ⎕WC), É as assignment between word
# characters (V←V+1), or Latin letters inside code, where real APL has none.
# ¨ ¯ × ÷ are genuine APL and are not counted.
MAPPED_PROSE = re.compile(r"\u0152[A-Za-z]{2}|\w\u00c9\w")
MAPPED_CODE = re.compile("[\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u00ff\u0152\u0153\u0160\u0161"
                         "\u0178\u017d\u017e\u0192\u02c6\u02dc\u2030\u2039\u203a]")


def _code_text(text):
    import lxml.html
    try:
        doc = lxml.html.fromstring(text)
    except Exception:
        return ""
    return "".join(e.text_content() for e in doc.iter("pre", "code", "tt"))


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
