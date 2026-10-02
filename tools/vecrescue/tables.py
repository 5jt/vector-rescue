"""Issue #5: tables.

A table becomes a Markdown table only when Markdown can say everything it
says: a header row of <th>, rectangular, no spans, inline-only cells, no
caption or column styling. Anything else stays raw HTML, with the reason
in the notes, so the reasons can be reviewed and the rule revised.
"""

import re

from .markdown import INLINE_TAGS, inline, raw_html

STYLED_CLASSES = {"code", "math"}


def _rows(table):
    return table.xpath("./tr|./thead/tr|./tbody/tr|./tfoot/tr")


def _cells(row):
    return row.xpath("./th|./td")


def _why_raw(table):
    """The reason TABLE can't be a Markdown table, or None if it can."""
    if table.xpath(".//table"):
        return "nested-table"
    if table.find("caption") is not None:
        return "caption"
    if table.xpath("./col|./colgroup"):
        return "column-styling"
    if STYLED_CLASSES & set((table.get("class") or "").split()):
        return "code-or-math-table"
    rows = [_cells(r) for r in _rows(table)]
    if not rows or not all(c.tag == "th" for c in rows[0]):
        return "no-header-row"
    if any(c.get("colspan") or c.get("rowspan") for r in rows for c in r):
        return "span"
    if len({len(r) for r in rows}) > 1:
        return "ragged"
    if any(c.tag == "th" for r in rows[1:] for c in r):
        return "header-cell-in-body"
    for r in rows:
        for c in r:
            if any(isinstance(k.tag, str) and k.tag not in INLINE_TAGS
                   for k in c.iter() if k is not c):
                return "block-content"
    return None


_CODE_SPAN = re.compile(r"(`+).+?\1")


def _escape_pipes(md):
    """Escape | outside code spans (the table extension respects those)."""
    out, pos = [], 0
    for m in _CODE_SPAN.finditer(md):
        out.append(md[pos:m.start()].replace("|", "\\|"))
        out.append(m.group(0))
        pos = m.end()
    out.append(md[pos:].replace("|", "\\|"))
    return "".join(out)


def _cell(c):
    md = _escape_pipes(inline(c).replace("  \n", "<br>"))
    return md or " "


def table(el, ctx):
    reason = _why_raw(el)
    if reason:
        ctx["raw"] = True
        ctx["notes"].append({"kind": "table-raw", "reason": reason})
        return raw_html(el)
    rows = [[_cell(c) for c in _cells(r)] for r in _rows(el)]
    lines = ["| " + " | ".join(r) + " |" for r in rows]
    lines.insert(1, "| " + " | ".join("---" for _ in rows[0]) + " |")
    return "\n".join(lines)
