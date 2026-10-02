"""Issue #5: tables."""

import lxml.html
import pytest

from vecrescue.convert import body_blocks


def blocks(html):
    notes = []
    md = "\n\n".join(body_blocks(lxml.html.fragment_fromstring(f"<div>{html}</div>"), notes))
    return md, notes


SIMPLE = ("<table class='left'><tr><th>Op</th><th>Meaning</th></tr>"
          "<tr><td><code>⍴</code></td><td>shape <em>of</em> x</td></tr>"
          "<tr><td>a|b</td><td></td></tr></table>")


def test_simple_table_with_header_row_becomes_markdown():
    md, notes = blocks(SIMPLE)
    assert md == ("| Op | Meaning |\n| --- | --- |\n"
                  "| `⍴` | shape *of* x |\n| a\\|b |   |")
    assert notes == []


def test_thead_and_tbody_are_read():
    md, _ = blocks("<table><thead><tr><th>A</th></tr></thead>"
                   "<tbody><tr><td>1</td></tr></tbody></table>")
    assert md == "| A |\n| --- |\n| 1 |"


def test_pipe_inside_code_is_left_alone():
    md, _ = blocks("<table><tr><th>q</th></tr><tr><td><code>x|y</code> or a|b</td></tr></table>")
    assert md.endswith("| `x|y` or a\\|b |")


def test_line_break_in_a_cell_becomes_br():
    md, _ = blocks("<table><tr><th>A</th></tr><tr><td>one<br/>two</td></tr></table>")
    assert md.endswith("| one<br>two |")


@pytest.mark.parametrize("reason, html", [
    ("no-header-row", "<table><tr><td>1</td></tr><tr><td>2</td></tr></table>"),
    ("span", "<table><tr><th colspan='2'>A</th></tr><tr><td>1</td><td>2</td></tr></table>"),
    ("ragged", "<table><tr><th>A</th><th>B</th></tr><tr><td>1</td></tr></table>"),
    ("block-content", "<table><tr><th>A</th></tr><tr><td><pre>x</pre></td></tr></table>"),
    ("caption", "<table><caption>C</caption><tr><th>A</th></tr><tr><td>1</td></tr></table>"),
    ("column-styling", "<table><col style='background:#DDD'/><tr><th>A</th></tr><tr><td>1</td></tr></table>"),
    ("code-or-math-table", "<table class='center code left'><tr><th>A</th></tr><tr><td>1</td></tr></table>"),
    ("nested-table", "<table><tr><th>A</th></tr><tr><td><table><tr><td>x</td></tr></table></td></tr></table>"),
    ("header-cell-in-body", "<table><tr><th>A</th><th>B</th></tr><tr><th>1</th><td>2</td></tr></table>"),
])
def test_tables_markdown_cannot_express_stay_raw_with_a_reason(reason, html):
    md, notes = blocks(html)
    assert md.startswith("<table")
    assert notes == [{"kind": "table-raw", "reason": reason}]


def test_raw_table_inside_a_list_makes_the_list_raw():
    md, _ = blocks("<ul><li>x<table><tr><td>1</td></tr></table></li></ul>")
    assert md.startswith("<ul>")
