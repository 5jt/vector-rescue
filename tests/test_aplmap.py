"""Issue #33: converting APL typed in mapped fonts."""

import lxml.html
import pytest

from vecrescue.aplmap import apply_mapping, load_table, to_byte
from vecrescue.legacy import decode


def test_table_loads_from_the_repo():
    t = load_table("apl2741")
    assert t[0x84] == "←" and t[0x8C] == "⎕" and t[0xBD] == "⍴" and t[0x81] == "⊣"
    assert 0x41 not in t                       # ASCII is untouched


def test_undefined_windows_1252_bytes_keep_their_identity():
    text, how = decode(b"a\x81b", keep_undefined=True)
    assert to_byte(text[1]) == 0x81 and how == "cp1252"


@pytest.mark.parametrize("ch, byte", [("„", 0x84), ("Œ", 0x8C), ("½", 0xBD), ("a", None), ("⍴", None)])
def test_to_byte(ch, byte):
    assert to_byte(ch) == byte


def doc(html):
    return lxml.html.fromstring(f"<html><body>{html}</body></html>")


def body(d):
    return lxml.html.tostring(d.find("body"), encoding="unicode")[6:-7]


def test_mapping_applies_in_apl_contexts_only_and_unwraps_apl_fonts():
    d = doc('<p>Café Œ prose</p><pre>vv„?365½12</pre>'
            '<p>Use <font face="APL2741">Œio„0</font> and <tt>¼10</tt>.</p>')
    notes = []
    apply_mapping(d, load_table("apl2741"), notes)
    assert body(d) == ('<p>Café Œ prose</p><pre>vv←?365⍴12</pre>'
                       '<p>Use ⎕io←0 and <tt>⍳10</tt>.</p>')
    assert notes == [{"kind": "apl-mapped", "table": "apl2741", "characters": 5},
                     {"kind": "apl-residue-in-prose", "sample": "Café Œ prose"}]


def test_mapping_is_idempotent_on_unicode_apl():
    d = doc("<pre>x←⍳ 10 × 2 ÷ ¯1</pre>")
    apply_mapping(d, load_table("apl2741"), [])
    assert body(d) == "<pre>x←⍳ 10 × 2 ÷ ¯1</pre>"


def test_varch_j_boxes_are_repaired_by_column():
    from vecrescue.aplmap import repair_varch_boxes
    before = ("      sum\n"
              "┌⍲┬⍲?\n"
              "?+?/?\n"
              "└⍲┴⍲⍒\n"
              "   ?2 3   NB. a real ? (deal) outside a box\n"
              "┌⍲⍲⍲┬⍲?\n"
              "?1 ??x?\n"
              "└⍲⍲⍲┴⍲⍒")
    after = ("      sum\n"
             "┌─┬─┐\n"
             "│+│/│\n"
             "└─┴─┘\n"
             "   ?2 3   NB. a real ? (deal) outside a box\n"
             "┌───┬─┐\n"
             "│1 ?│x│\n"      # ? inside a cell is J's roll, kept
             "└───┴─┘")
    assert repair_varch_boxes(before) == after


def test_varch_j_nested_boxes_and_trees():
    from vecrescue.aplmap import repair_varch_boxes
    before = ("┌⍲┬⍲⍲⍲⍲⍲⍲⍲?\n"
              "?f?┌⍲┬⍲?  ?\n"
              "? ??+?/?  ?\n"
              "? ?└⍲┴⍲⍒  ?\n"
              "└⍲┴⍲⍲⍲⍲⍲⍲⍲⍒\n"
              "⍲⍲Å⍲ %")
    after = ("┌─┬───────┐\n"
             "│f│┌─┬─┐  │\n"
             "│ ││+│/│  │\n"
             "│ │└─┴─┘  │\n"
             "└─┴───────┘\n"
             "──┼─ %")
    assert repair_varch_boxes(before) == after
