"""Issue #4: block elements, rendered recursively.

Each rule takes (element, ctx) and returns Markdown. ctx["notes"] collects
notes; ctx["raw"] is set when a rule falls back to raw HTML, which matters
inside containers: Python-Markdown does not recognise raw HTML blocks that
are indented inside list items or quoted, so a container holding one is
passed through whole.
"""

import copy
import re

from .code import pre_block
from .tables import table
from .markdown import (INLINE_TAGS, escape_line_starts, inline, inline_flat,
                       raw_html)

PENDING_P = {"caption", "ednote", "math", "fright", "fleft"}  # issues #6, #7
TRANSPARENT_DIV = {None, "", "clear"}
PLAIN_LIST_CLASSES = {None, "", "bullet"}


def _raw(el, ctx):
    ctx["raw"] = True
    ctx["notes"].append({"kind": "raw-html", "tag": el.tag})
    return raw_html(el)


def _indent(md, prefix="    "):
    return "\n".join(prefix + line if line else "" for line in md.split("\n"))


def render_blocks(container, ctx):
    """Markdown blocks for the children of CONTAINER.

    Runs of inline content (text and inline elements) between block
    children are gathered into paragraphs.
    """
    blocks, run = [], None

    def flush():
        nonlocal run
        if run is not None:
            md = escape_line_starts(inline(run))
            if md:
                blocks.append(md)
            run = None

    def add_inline(item=None, text=None):
        nonlocal run
        if run is None:
            run = container.makeelement("p", {})
        if item is not None:
            run.append(item)
        elif text:
            if len(run):
                run[-1].tail = (run[-1].tail or "") + text
            else:
                run.text = (run.text or "") + text

    if (container.text or "").strip():
        add_inline(text=container.text)
    for el in container:
        if not isinstance(el.tag, str):
            pass
        elif el.tag in INLINE_TAGS:
            item = copy.deepcopy(el)
            item.tail = None
            add_inline(item)
        else:
            flush()
            md = render_block(el, ctx)
            if md:
                blocks.append(md)
        # inside a run of inline content, whitespace between elements matters
        if el.tail and (el.tail.strip() or run is not None):
            add_inline(text=el.tail)
    flush()
    return blocks


def render_block(el, ctx):
    rule = BLOCK_RULES.get(el.tag)
    return rule(el, ctx) if rule else _raw(el, ctx)


def _inner(el, ctx):
    """Render EL's children in a fresh context; None if any went raw."""
    sub = {"notes": [], "raw": False}
    blocks = render_blocks(el, sub)
    if sub["raw"]:
        return None
    ctx["notes"].extend(sub["notes"])
    return blocks


# rules -----------------------------------------------------------------------

def para(el, ctx):
    cls = set((el.get("class") or "").split())
    if cls & PENDING_P or any(isinstance(k.tag, str) and k.tag not in INLINE_TAGS
                              for k in el.iter() if k is not el):
        return _raw(el, ctx)
    return escape_line_starts(inline(el))


def heading(el, ctx):
    level = int(el.tag[1])
    text = inline_flat(el)
    anchor = f" {{ #{el.get('id')} }}" if el.get("id") else ""
    return f"{'#' * level} {text}{anchor}" if text else ""


def stray_h1(el, ctx):
    """An H1 left after the head block; the page title is the only H1."""
    ctx["notes"].append({"kind": "h1-demoted", "text": " ".join(el.text_content().split())})
    return f"## {inline_flat(el)}"


def _item(marker, blocks):
    """A list item: marker on the first line, the rest indented 4."""
    out = []
    for i, block in enumerate(blocks):
        if i == 0:
            first, _, rest = block.partition("\n")
            out.append(marker + first + ("\n" + _indent(rest) if rest else ""))
        else:
            sep = "\n" if _is_list(block) and i == 1 else "\n\n"
            out.append(sep + _indent(block))
    return "".join(out)


def _is_list(md):
    return bool(re.match(r"(- |\d+\. )", md))


def a_list(el, ctx):
    if (el.get("class") or None) not in PLAIN_LIST_CLASSES or el.get("style") \
            or el.get("type"):
        return _raw(el, ctx)
    items = []
    n = int(el.get("start") or 1) if el.tag == "ol" else None
    for li in el:
        if not isinstance(li.tag, str):
            continue
        if li.tag != "li":
            return _raw(el, ctx)
        blocks = _inner(li, ctx)
        if blocks is None:
            return _raw(el, ctx)
        marker = "- " if n is None else f"{n}. "
        if n is not None:
            n += 1
        items.append(_item(marker, blocks or [""]))
    loose = any("\n\n" in item for item in items)
    return ("\n\n" if loose else "\n").join(items)


def blockquote(el, ctx):
    blocks = _inner(el, ctx)
    if blocks is None:
        return _raw(el, ctx)
    md = "\n\n".join(blocks)
    return "\n".join("> " + line if line else ">" for line in md.split("\n"))


def dlist(el, ctx):
    groups, current = [], []
    for k in el:
        if not isinstance(k.tag, str):
            continue
        if k.tag == "dt":
            if current and current[-1].startswith(":"):
                groups.append("\n".join(current))
                current = []
            current.append(inline_flat(k))
        elif k.tag == "dd":
            blocks = _inner(k, ctx)
            if blocks is None or not current:
                return _raw(el, ctx)
            md = "\n\n".join(blocks)
            first, _, rest = md.partition("\n")
            current.append(":   " + first + ("\n" + _indent(rest) if rest else ""))
        else:
            return _raw(el, ctx)
    if current:
        groups.append("\n".join(current))
    return "\n\n".join(groups)


def div(el, ctx):
    if el.get("class") not in TRANSPARENT_DIV or el.get("id") or el.get("style"):
        return _raw(el, ctx)
    return "\n\n".join(render_blocks(el, ctx))


def pre(el, ctx):
    md = pre_block(el, ctx["notes"])
    if md.startswith("<pre"):
        ctx["raw"] = True
    return md


BLOCK_RULES = {
    "p": para, "h1": stray_h1, "pre": pre, "blockquote": blockquote,
    "ul": a_list, "ol": a_list, "dl": dlist, "div": div,
    "hr": lambda el, ctx: "***", "table": table,
    **{f"h{n}": heading for n in range(2, 7)},
}
