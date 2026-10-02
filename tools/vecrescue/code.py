"""Issue #3: <pre> blocks and inline <code>."""

import copy
import re

from .markdown import INLINE_RULES, raw_html, raw_inline, ws

TAB_WIDTH = 8  # browsers render tabs in <pre> at 8 columns


def _element_children(el):
    return sorted({k.tag for k in el.iter() if k is not el and isinstance(k.tag, str)})


def _longest_backticks(text):
    return max((len(m) for m in re.findall(r"`+", text)), default=0)


def _text_slots(el):
    """(element, "text" | "tail") pairs in document order under EL."""
    yield el, "text"
    for child in el:
        if isinstance(child.tag, str):
            yield from _text_slots(child)
        yield child, "tail"


def _expand_tabs(pre):
    """A copy of PRE with tabs expanded to TAB_WIDTH columns, counting
    columns across child elements. Python-Markdown would use 4."""
    pre = copy.deepcopy(pre)
    col = 0
    for el, slot in _text_slots(pre):
        text = getattr(el, slot)
        if not text:
            continue
        out = []
        for ch in text:
            if ch == "\t":
                n = TAB_WIDTH - col % TAB_WIDTH
                out.append(" " * n)
                col += n
            else:
                out.append(ch)
                col = 0 if ch == "\n" else col + 1
        setattr(el, slot, "".join(out))
    return pre


def pre_block(el, notes):
    tags = _element_children(el)
    if tags:
        notes.append({"kind": "pre-raw-html", "tags": tags})
        return raw_html(_expand_tabs(el))
    text = el.text_content()
    if text.startswith("\r\n"):
        text = text[2:]
    elif text.startswith("\n"):
        text = text[1:]
    lines = [line.rstrip("\r").expandtabs(TAB_WIDTH).rstrip(" ") for line in text.split("\n")]
    while lines and not lines[-1].strip(" \t"):
        lines.pop()
    blank = 0
    while lines and not lines[0].strip(" \t"):
        lines.pop(0)
        blank += 1
    if not lines:
        notes.append({"kind": "pre-empty"})
        return ""
    if blank:
        notes.append({"kind": "pre-leading-blank-lines", "count": blank})
    body = "\n".join(lines)
    fence = "`" * max(3, _longest_backticks(body) + 1)
    return f"{fence}\n{body}\n{fence}"


def inline_code(el):
    if _element_children(el):
        for c in [c for c in el if not isinstance(c.tag, str)]:
            c.getparent().remove(c)
        return raw_inline(el) if _element_children(el) else inline_code(el)
    text = ws(el.text_content())
    lead = " " if text.startswith(" ") else ""
    trail = " " if text.endswith(" ") else ""
    text = text.strip(" ")
    if not text:
        return lead or trail
    fence = "`" * (_longest_backticks(text) + 1)
    pad = " " if text.startswith("`") or text.endswith("`") else ""
    return f"{lead}{fence}{pad}{text}{pad}{fence}{trail}"


INLINE_RULES["code"] = inline_code
INLINE_RULES["tt"] = inline_code
