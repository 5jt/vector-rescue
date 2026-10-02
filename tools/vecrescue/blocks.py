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
from .images import figure
from .tables import table
from .markdown import (INLINE_TAGS, anchor_html, escape_line_starts, inline,
                       inline_flat, note, raw_html)

# paragraph classes that carry meaning, and the class they become
P_CLASSES = {"ednote": "ednote", "math": "math", "fright": "right", "fleft": "left"}
LAYOUT_DIV = {"clear", "center", "centred", "pad", "plain", "small"}
PANEL_DIV = {"panel", "fright", "fleft"}
PLAIN_LIST_CLASSES = {None, "", "bullet", "references"}
PHRASING = INLINE_TAGS | {"math", "object", "embed", "param"}
OPAQUE = {"math", "object"}  # their insides are not examined


def _inside_opaque(k, top):
    for a in k.iterancestors():
        if a is top:
            return False
        if a.tag in OPAQUE:
            return True
    return False


def _has_block_content(el):
    """Whether EL holds anything a Markdown paragraph cannot."""
    return any(isinstance(k.tag, str) and k.tag not in PHRASING and not _inside_opaque(k, el)
               for k in el.iterdescendants())


def _raw(el, ctx, reason="no-rule"):
    ctx["raw"] = True
    ctx["notes"].append({"kind": "raw-html", "tag": el.tag, "reason": reason})
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
    cls = (el.get("class") or "").split()
    if "caption" in cls:
        return figure(el, ctx)
    if _has_block_content(el):
        return _raw(el, ctx, "block-content")
    md = escape_line_starts(inline(el))
    keep = [P_CLASSES[c] for c in cls if c in P_CLASSES]
    if md and keep:
        if md.startswith("<"):  # a line opening with HTML takes no { .class }
            ctx["raw"] = True
            return f'<p class="{" ".join(keep)}" markdown="span">{md}</p>'
        md += "\n{ " + " ".join("." + c for c in keep) + " }"
    return md


def heading(el, ctx):
    level = int(el.tag[1])
    text = inline_flat(el)
    anchor = f" {{ #{el.get('id')} }}" if el.get("id") else ""
    return f"{'#' * level} {text}{anchor}" if text else ""


def stray_h1(el, ctx):
    """An H1 left after the head block; the page title is the only H1."""
    ctx["notes"].append({"kind": "h1-demoted", "text": " ".join(el.text_content().split())})
    return f"## {inline_flat(el)}"


def _attach(marker, block):
    """BLOCK after a list or definition MARKER, continuation lines indented 4.

    A code fence is not recognised on the marker line, so it starts on the
    next line instead.
    """
    if block.startswith("```"):
        return marker + "\n" + _indent(block)
    first, _, rest = block.partition("\n")
    return marker + first + ("\n" + _indent(rest) if rest else "")


def _item(marker, blocks):
    """A list item: marker on the first line, the rest indented 4."""
    out = []
    for i, block in enumerate(blocks):
        if i == 0:
            out.append(_attach(marker, block))
        else:
            sep = "\n" if _is_list(block) and i == 1 else "\n\n"
            out.append(sep + _indent(block))
    return "".join(out)


def _is_list(md):
    return bool(re.match(r"(- |\d+\. )", md))


def a_list(el, ctx):
    if (el.get("class") or None) not in PLAIN_LIST_CLASSES or el.get("style") \
            or el.get("type"):
        return _raw(el, ctx, "numbering")
    items = []
    n = int(el.get("start") or 1) if el.tag == "ol" else None
    for li in el:
        if not isinstance(li.tag, str):
            continue
        if li.tag != "li":
            return _raw(el, ctx, "not-a-list-item")
        blocks = _inner(li, ctx)
        if blocks is None:
            return _raw(el, ctx, "contains-raw-html")
        marker = "- " if n is None else f"{n}. "
        if n is not None:
            n += 1
        items.append(_item(marker, blocks or [""]))
    loose = any("\n\n" in item for item in items)
    return ("\n\n" if loose else "\n").join(items)


def blockquote(el, ctx):
    blocks = _inner(el, ctx)
    if blocks is None:
        return _raw(el, ctx, "contains-raw-html")
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
                return _raw(el, ctx, "contains-raw-html" if blocks is None else "dd-without-dt")
            current.append(_attach(":   ", "\n\n".join(blocks)))
        else:
            return _raw(el, ctx, "not-a-definition")
    if current:
        groups.append("\n".join(current))
    return "\n\n".join(groups)


def div(el, ctx):
    cls = set((el.get("class") or "").split())
    if cls & PANEL_DIV:  # a sidebar: a Markdown div keeping the float
        side = "right" if "fright" in cls else "left" if "fleft" in cls else None
        classes = " ".join(["panel"] + ([side] if side else []))
        inner = "\n\n".join(render_blocks(el, ctx))
        ctx["raw"] = True
        return f'<div class="{classes}" markdown="1">\n\n{inner}\n\n</div>'
    if cls - LAYOUT_DIV or el.get("style"):
        return _raw(el, ctx, "styled")
    blocks = render_blocks(el, ctx)
    if el.get("id"):
        blocks.insert(0, anchor_html(el.get("id")))
    return "\n\n".join(blocks)


def math(el, ctx):
    note({"kind": "mathml"})
    ctx["raw"] = True
    return raw_html(el)


def pre(el, ctx):
    md = pre_block(el, ctx["notes"])
    if md.startswith("<pre"):
        ctx["raw"] = True
    return md


BLOCK_RULES = {
    "p": para, "h1": stray_h1, "pre": pre, "blockquote": blockquote,
    "ul": a_list, "ol": a_list, "dl": dlist, "div": div,
    "hr": lambda el, ctx: "***", "table": table, "math": math,
    **{f"h{n}": heading for n in range(2, 7)},
}
