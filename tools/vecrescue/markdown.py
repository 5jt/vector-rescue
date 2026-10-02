"""Shared Markdown helpers for the conversion rules."""

import re

import lxml.html

# HTML collapses ASCII whitespace only; a non-breaking space is content.
_WS = re.compile(r"[ \t\n\r\f]+")


def ws(s):
    return _WS.sub(" ", s or "")


def raw_html(el):
    return lxml.html.tostring(el, encoding="unicode", with_tail=False)


class Literal(str):
    """Inline Markdown that whitespace collapsing must not touch."""


INLINE_RULES = {}


def inline(el):
    """Markdown for the inline content of EL.

    Text is whitespace-collapsed as a browser would; output from inline
    rules is returned as a Literal and kept exactly.
    """
    pieces = [el.text or ""]
    for child in el:
        if not isinstance(child.tag, str):  # comment
            pass
        elif child.tag == "br":
            pieces.append(" ")
        else:
            rule = INLINE_RULES.get(child.tag)
            md = rule(child) if rule else raw_html(child)
            # whitespace-only output (e.g. an empty <code>) is just text
            pieces.append(Literal(md) if md.strip() else md)
        pieces.append(child.tail or "")
    out, text = [], []
    for p in pieces:
        if isinstance(p, Literal):
            out.append(ws("".join(text)))
            text = []
            out.append(p)
        else:
            text.append(p)
    out.append(ws("".join(text)))
    return "".join(out).strip()
