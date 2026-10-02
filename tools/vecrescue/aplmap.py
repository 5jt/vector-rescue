"""Issue #33: APL typed in fonts that map glyphs onto ordinary characters.

A mapping table (mappings/<name>.tsv) gives, for each byte, the APL
character the font drew there. Mapped text reaches us as Windows-1252
characters, or as their Unicode code points after an earlier conversion,
so each character is taken back to its byte and looked up. The mapping is
applied only in APL contexts (text set in an APL font, pre, tt, code, or
APL-classed elements); prose is left alone and suspicious characters there
are noted for review.
"""

import csv
import re
from functools import lru_cache
from pathlib import Path

from .legacy import PRIVATE

MAPPINGS = Path(__file__).resolve().parents[2] / "mappings"
CONTEXT_TAGS = {"pre", "tt", "code"}
APL_ATTR = re.compile(r"apl", re.I)
# characters that in prose are only ever mapped APL, never ordinary text
TELLTALE = set("„Œœ½¼¾©«»ª¬®°±²³´µº¹¦§ˆ‰‹›ƒ†‡šŠžŽŸ")


@lru_cache(maxsize=None)
def load_table(name):
    with open(MAPPINGS / f"{name}.tsv", encoding="utf-8") as f:
        return {int(r["byte"], 16): r["APL"] for r in csv.DictReader(f, delimiter="\t")}


def to_byte(ch):
    """The byte a mapped character came from, or None."""
    if PRIVATE + 0x80 <= ord(ch) <= PRIVATE + 0xFF:
        return ord(ch) - PRIVATE
    try:
        b = ch.encode("cp1252")
    except UnicodeEncodeError:
        return None
    return b[0] if len(b) == 1 and b[0] >= 0x80 else None


def _map(text, table, count):
    if not text:
        return text
    out = []
    for ch in text:
        b = to_byte(ch)
        new = table.get(b, ch) if b is not None else ch
        if new != ch:
            count[0] += 1
        out.append(new)
    return "".join(out)


def _is_context(el):
    return el.tag in CONTEXT_TAGS or any(APL_ATTR.search(el.get(a) or "")
                                         for a in ("face", "class", "style"))


def _inside_context(el):
    return any(_is_context(a) for a in el.iterancestors() if isinstance(a.tag, str))


def apply_mapping(doc, table, notes, name="apl2741"):
    body = doc.find("body") if doc.find("body") is not None else doc
    count = [0]
    roots = [el for el in body.iter() if isinstance(el.tag, str) and el is not body
             and _is_context(el) and not _inside_context(el)]
    for root in roots:
        for el in root.iter():
            if not isinstance(el.tag, str):
                continue
            el.text = _map(el.text, table, count)
            if el is not root:
                el.tail = _map(el.tail, table, count)
    for el in [e for e in body.iter("font") if APL_ATTR.search(e.get("face") or "")]:
        el.drop_tag()  # the text is Unicode now; the site's APL font shows it
    notes.append({"kind": "apl-mapped", "table": name, "characters": count[0]})
    for el in body.iter():
        if not isinstance(el.tag, str) or _is_context(el) or _inside_context(el):
            continue
        own = (el.text or "") + "".join(c.tail or "" for c in el)
        if TELLTALE & set(own):
            notes.append({"kind": "apl-residue-in-prose", "sample": " ".join(el.text_content().split())[:80]})
            break
    return doc


# VARCH's J boxes (issue #33) ---------------------------------------------------

# J has no ⍲, ⍒ or Å: in VARCH's conversions of J output they can only be
# box-drawing (J used the DOS code page's line characters).
J_BOX = {"⍲": "─", "⍒": "┘", "Å": "┼"}


def repair_varch_boxes(text):
    """Repair box drawings in J output as Ian Clark's VARCH converted them.

    VARCH wrote J's horizontal line as ⍲, right corners as ? and ⍒, the
    cross as Å, and vertical bars as ?. Every box, at any depth, is found
    from its ┌: its top edge runs to the right corner, its left side down to
    its └. A ? becomes │ only in that box's corner and join columns (a ? in
    a cell is J's roll, and is kept); a ? closing a top edge becomes ┐, and
    one closing a separator row ┤.
    """
    grid = [[J_BOX.get(c, c) for c in line] for line in text.split("\n")]

    def at(r, c):
        return grid[r][c] if 0 <= r < len(grid) and 0 <= c < len(grid[r]) else ""

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch != "┌":
                continue
            k = c + 1
            while at(r, k) in ("─", "┬"):
                k += 1
            if at(r, k) not in ("?", "┐") or k == c + 1:
                continue
            row[k] = "┐"
            joins = [c] + [x for x in range(c + 1, k) if row[x] == "┬"] + [k]
            bottom = next((rr for rr in range(r + 1, len(grid)) if at(rr, c) == "└"), None)
            if bottom is None:
                continue
            if at(bottom, k) == "?":
                grid[bottom][k] = "┘"
            for rr in range(r + 1, bottom):
                if at(rr, c) == "├":
                    if at(rr, k) == "?":
                        grid[rr][k] = "┤"
                    continue
                for x in joins:
                    if at(rr, x) == "?":
                        grid[rr][x] = "│"
    return "\n".join("".join(row) for row in grid)
