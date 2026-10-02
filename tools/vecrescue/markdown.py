"""Shared Markdown helpers: escaping, raw HTML and inline conversion."""

import copy
import re

import lxml.html

# HTML collapses ASCII whitespace only; a non-breaking space is content.
_WS = re.compile(r"[ \t\n\r\f]+")
_BR = "\x00"  # placeholder for <br>, resolved after whitespace collapsing

INLINE_TAGS = {
    "a", "abbr", "acronym", "b", "big", "br", "cite", "code", "dfn", "em",
    "font", "i", "img", "kbd", "q", "s", "samp", "small", "span", "strike",
    "strong", "sub", "sup", "tt", "u", "var",
}


def ws(s):
    return _WS.sub(" ", s or "")


def raw_html(el):
    return lxml.html.tostring(el, encoding="unicode", with_tail=False)


def raw_inline(el):
    """Raw HTML for an inline element.

    Python-Markdown still applies inline Markdown to text inside inline
    HTML, so Markdown characters in that text are escaped.
    """
    el = copy.deepcopy(el)
    el.tail = None
    for node in el.iter():
        if node.text and isinstance(node.tag, str):
            node.text = _MD_CHARS.sub(r"\\\1", node.text)
        if node is not el and node.tail:
            node.tail = _MD_CHARS.sub(r"\\\1", node.tail)
    return raw_html(el)


_MD_CHARS = re.compile(r"([\\`*_\[\]])")


def escape(text):
    """Escape characters Markdown would otherwise interpret."""
    text = re.sub(r"([\\`*_\[\]])", r"\\\1", text)
    text = re.sub(r"&(?=#?\w+;)", "&amp;", text)
    return text.replace("<", "&lt;")


def escape_line_starts(md):
    """Escape characters that would start a heading, list, quote or rule."""
    def fix(line):
        line = re.sub(r"^(\s*)([#>+=-])", r"\1\\\2", line)
        return re.sub(r"^(\s*\d+)([.)])(?=\s|$)", r"\1\\\2", line)
    return "\n".join(fix(line) for line in md.split("\n"))


class Literal(str):
    """Inline Markdown that whitespace collapsing must not touch."""


INLINE_RULES = {}


def inline(el):
    """Markdown for the inline content of EL.

    Text is whitespace-collapsed as a browser would and escaped; output
    from inline rules is kept exactly. <br> becomes a hard line break.
    """
    pieces = [el.text or ""]
    for child in el:
        if not isinstance(child.tag, str):  # comment
            pass
        elif child.tag == "br":
            pieces.append(Literal(_BR))
        else:
            rule = INLINE_RULES.get(child.tag)
            md = rule(child) if rule else raw_inline(child)
            # whitespace-only output (e.g. an empty <code>) is just text
            pieces.append(Literal(md) if md.strip() else md)
        pieces.append(child.tail or "")
    out, text = [], []
    for p in pieces:
        if isinstance(p, Literal):
            out.append(escape(ws("".join(text))))
            text = []
            out.append(p)
        else:
            text.append(p)
    out.append(escape(ws("".join(text))))
    md = "".join(out).strip(" ")
    md = re.sub(f" *{_BR}+ *", lambda m: "  \n" * 1, md)
    return md.strip(" \n")


def inline_flat(el):
    """Inline Markdown on one line (headings, terms): breaks become spaces."""
    return re.sub(r" *\n *", " ", inline(el).replace("  \n", " "))


# inline rules ----------------------------------------------------------------

def _edges(el):
    t = el.text_content()
    return (" " if t[:1].isspace() else ""), (" " if t[-1:].isspace() else "")


def _wrap(mark):
    def rule(el):
        body = inline(el)
        if not body:
            return ""
        if not re.search(r"\w", body):  # *,* or **.** would not parse
            return raw_inline(el)
        lead, trail = _edges(el)
        return f"{lead}{mark}{body}{mark}{trail}"
    return rule


def span(el):
    cls = (el.get("class") or "").split()
    if "italic" in cls:
        return _wrap("*")(el)
    if "nowrap" in cls:
        return inline(el)
    return raw_inline(el)


def link(el):
    href, title = el.get("href"), el.get("title")
    text = inline(el)
    unsafe = (href is None or el.get("name") or el.get("id") or not text
              or re.search(r"[\s<>]", href) or href.count("(") != href.count(")")
              or (title and '"' in title))
    if unsafe:
        return raw_inline(el)
    title = f' "{title}"' if title else ""
    lead, trail = _edges(el)
    return f"{lead}[{text}]({href}{title}){trail}"


for tag in ("em", "i", "cite", "dfn", "var"):
    INLINE_RULES[tag] = _wrap("*")
for tag in ("strong", "b"):
    INLINE_RULES[tag] = _wrap("**")
INLINE_RULES["span"] = span
INLINE_RULES["a"] = link
