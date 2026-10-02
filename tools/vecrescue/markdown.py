"""Shared Markdown helpers: escaping, raw HTML and inline conversion."""

import copy
import html
import re
from contextvars import ContextVar

import lxml.html
from lxml.html import defs

# HTML collapses ASCII whitespace only; a non-breaking space is content.
_WS = re.compile(r"[ \t\n\r\f]+")
_BR = "\x00"  # placeholder for <br>, resolved after whitespace collapsing

_NOTES = ContextVar("notes", default=None)


def collecting(notes):
    """Context for rules to add notes: `with collecting(notes): ...`."""
    class _Ctx:
        def __enter__(self):
            self.token = _NOTES.set(notes)

        def __exit__(self, *exc):
            _NOTES.reset(self.token)
    return _Ctx()


def note(n):
    notes = _NOTES.get()
    if notes is not None:
        notes.append(n)


INLINE_TAGS = {
    "a", "abbr", "acronym", "b", "big", "br", "cite", "code", "dfn", "em",
    "font", "i", "img", "kbd", "q", "s", "samp", "small", "span", "strike",
    "strong", "sub", "sup", "tt", "u", "var",
}


def made_up(tag):
    """A tag that is not HTML: usually an author's literal <…> that the parser
    took for markup (e.g. <ctrl+break>, an email address in angle brackets)."""
    return isinstance(tag, str) and ":" not in tag and tag not in defs.tags


def made_up_as_text(el):
    attrs = "".join(f" {k}" + (f'="{v}"' if v else "") for k, v in el.attrib.items())
    note({"kind": "made-up-tag-as-text", "tag": el.tag})
    return escape(f"<{el.tag}{attrs}>")


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


_MD_CHARS = re.compile(r"([\\`*_\[\]{}])")


def escape(text):
    """Escape characters Markdown would otherwise interpret."""
    text = re.sub(r"([\\`*_\[\]{}])", r"\\\1", text)  # { } would be attribute lists
    text = re.sub(r"&(?=#?\w+;)", "&amp;", text)
    return text.replace("<", "&lt;")


def escape_line_starts(md):
    """Escape characters that would start a heading, list, quote or rule.

    Python-Markdown has no backslash escape for =, so it becomes an entity.
    """
    def fix(line):
        line = re.sub(r"^(\s*)=", r"\1&#61;", line)
        line = re.sub(r"^(\s*)([#>+-])", r"\1\\\2", line)
        return re.sub(r"^(\s*\d+)([.)])(?=\s|$)", r"\1\\\2", line)
    return "\n".join(fix(line) for line in md.split("\n"))


class Literal(str):
    """Inline Markdown that whitespace collapsing must not touch."""


class Emphasis(Literal):
    """Markdown emphasis, with the raw HTML to use if its neighbours would
    stop Markdown recognising it (e.g. inside a word: 2<i>n</i>2)."""

    def __new__(cls, md, raw):
        obj = super().__new__(cls, md)
        obj.raw = raw
        return obj


OPENERS = "([{“‘\"'"
CLOSERS = ".,;:!?)]}”’\"'"


def _safe(prev, nxt, md):
    if "*" in (prev, nxt):  # **…*** next to another emphasis will not parse
        return False
    before = md[:1].isspace() or prev == "" or prev.isspace() or prev in OPENERS
    after = md[-1:].isspace() or nxt == "" or nxt.isspace() or nxt in CLOSERS
    return before and after


INLINE_RULES = {}


def inline(el):
    """Markdown for the inline content of EL.

    Text is whitespace-collapsed as a browser would and escaped; output
    from inline rules is kept exactly. <br> becomes a hard line break.
    """
    _merge_adjacent_code(el)
    pieces = [el.text or ""]
    for child in el:
        if not isinstance(child.tag, str):  # comment
            pass
        elif child.tag == "br":
            pieces.append(Literal(_BR))
        elif made_up(child.tag):
            pieces.append(Literal(made_up_as_text(child)))
            pieces.append(" " if (child.text or "")[:1].isspace() else "")
            inner = inline(child)
            pieces.append(Literal(inner) if inner else "")
        else:
            rule = INLINE_RULES.get(child.tag)
            md = rule(child) if rule else raw_inline(child)
            # whitespace-only output (e.g. an empty <code>) is just text
            pieces.append(md if isinstance(md, Literal) or not md.strip() else Literal(md))
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
    for i, piece in enumerate(out):
        if isinstance(piece, Emphasis):
            prev, nxt = "".join(out[:i])[-1:], "".join(out[i + 1:])[:1]
            if not _safe(prev, nxt, piece):
                out[i] = piece.raw
    md = "".join(out).strip(" ")
    md = re.sub(f" *{_BR}+ *", lambda m: "  \n" * 1, md)
    return md.strip(" \n")


CODE_TAGS = ("code", "tt")


def _merge_adjacent_code(el):
    """Join code elements with nothing between them (`f` `⍤` would
    otherwise become f``⍤, which Markdown misreads)."""
    for child in list(el):
        nxt = child.getnext()
        while (child.tag in CODE_TAGS and nxt is not None and nxt.tag in CODE_TAGS
               and not child.tail and not len(child) and not len(nxt)):
            child.text = (child.text or "") + (nxt.text or "")
            child.tail = nxt.tail
            el.remove(nxt)
            nxt = child.getnext()


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
        if not body:  # keep a space that was only emphasised
            return " " if el.text_content()[:1].isspace() else ""
        if not re.search(r"\w", body) or body[:1] == "*" or body[-1:] == "*":
            return raw_inline(el)  # *,* or **.** or *a *n** would not parse
        lead, trail = _edges(el)
        return Emphasis(f"{lead}{mark}{body}{mark}{trail}", lead + raw_inline(el) + trail)
    return rule


def span(el):
    cls = (el.get("class") or "").split()
    if "italic" in cls:
        return _wrap("*")(el)
    if "nowrap" in cls:
        return inline(el)
    return raw_inline(el)


def classed(md, classes):
    """A paragraph of inline Markdown MD with CSS CLASSES."""
    if md.startswith("<"):  # a line opening with HTML takes no { .class }
        return f'<p class="{" ".join(classes)}" markdown="span">{md}</p>'
    return md + "\n{ " + " ".join("." + c for c in classes) + " }"


def anchor_html(name):
    return f'<a id="{html.escape(name, quote=True)}"></a>'


def link(el):
    href, title = el.get("href"), el.get("title")
    name = el.get("name") or el.get("id")
    if name:  # a link target: an empty anchor, then the content
        el = copy.deepcopy(el)
        for k in ("name", "id"):
            el.attrib.pop(k, None)
        rest = link(el).strip(" ") if href else inline(el)
        if not rest:  # an empty target, e.g. <a name="ref1"> </a>
            return anchor_html(name)
        lead, trail = _edges(el)
        return lead + anchor_html(name) + rest + trail
    text = inline(el)
    unsafe = (href is None or not text
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
def embedded(el):
    """<object>/<embed> (e.g. a video): a link to what it shows."""
    url = el.get("data") or el.get("src")
    for p in el.iter("param"):
        if (p.get("name") or "").lower() in ("movie", "src"):
            url = url or p.get("value")
    for e in el.iter("embed"):
        url = url or e.get("src")
    if not url:
        return raw_inline(el)
    note({"kind": "embed-replaced", "url": url})
    return f"[Video: {escape(url)}]({url})"


INLINE_RULES["span"] = span
INLINE_RULES["object"] = embedded
INLINE_RULES["embed"] = embedded
INLINE_RULES["math"] = raw_inline
INLINE_RULES["a"] = link
