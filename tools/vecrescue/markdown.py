"""Shared Markdown helpers for the conversion rules."""

import re

import lxml.html


def ws(s):
    return re.sub(r"\s+", " ", s or "")


def raw_html(el):
    return lxml.html.tostring(el, encoding="unicode", with_tail=False)


INLINE_RULES = {}


def inline(el):
    """Markdown for the inline content of EL, whitespace collapsed."""
    out = [ws(el.text)]
    for child in el:
        if child.tag == "br":
            out.append(" ")
        else:
            rule = INLINE_RULES.get(child.tag)
            out.append(rule(child) if rule else raw_html(child))
        out.append(ws(child.tail))
    return re.sub(r" {2,}", " ", "".join(out)).strip()
