"""Issue #3: <pre> and <code>."""

import lxml.html
import pytest

from vecrescue.code import pre_block
from vecrescue.markdown import inline


def frag(html):
    return lxml.html.fragment_fromstring(html)


def pre(html):
    notes = []
    return pre_block(frag(html), notes), notes


# <pre> ---------------------------------------------------------------------

def test_pre_becomes_fenced_code_without_the_leading_newline():
    md, notes = pre("<pre>\n  t.f:10 20 30\n  t g:40\n</pre>")
    assert md == "```\n  t.f:10 20 30\n  t g:40\n```"
    assert notes == []


def test_entities_are_decoded():
    md, _ = pre("<pre>a&lt;b &amp; &quot;c&quot;</pre>")
    assert md == '```\na<b & "c"\n```'


def test_tabs_expand_to_eight_columns_as_browsers_show_them():
    md, _ = pre("<pre>\tX\nab\tY</pre>")
    assert md == "```\n        X\nab      Y\n```"


def test_fence_is_longer_than_any_backtick_run_inside():
    md, _ = pre("<pre>s:```a`b</pre>")
    assert md == "````\ns:```a`b\n````"


def test_trailing_whitespace_lines_are_removed():
    md, _ = pre("<pre>\nx\n   \n\t</pre>")
    assert md == "```\nx\n```"


def test_non_breaking_spaces_are_kept():
    md, _ = pre("<pre>a b</pre>")
    assert md == "```\na b\n```"


def test_leading_blank_lines_are_dropped_and_noted():
    md, notes = pre("<pre>\n\n\nx</pre>")
    assert md == "```\nx\n```"
    assert notes == [{"kind": "pre-leading-blank-lines", "count": 2}]


def test_pre_with_markup_inside_stays_raw_html():
    md, notes = pre("<pre>\nr<em>x</em></pre>")
    assert md == "<pre>\nr<em>x</em></pre>"
    assert notes == [{"kind": "pre-raw-html", "tags": ["em"]}]


def test_comments_inside_pre_do_not_force_raw_html():
    md, _ = pre("<pre>a<!-- c -->b</pre>")
    assert md == "```\nab\n```"


def test_empty_pre_is_dropped_and_noted():
    md, notes = pre("<pre>\n  \n</pre>")
    assert md == ""
    assert notes == [{"kind": "pre-empty"}]


# inline <code> -------------------------------------------------------------

@pytest.mark.parametrize("html, md", [
    ("<p>use <code>⍴⍵</code> here</p>", "use `⍴⍵` here"),
    ("<p>q <code>A=`a</code></p>", "q ``A=`a``"),
    ("<p>q <code>`A</code></p>", "q `` `A ``"),
    ("<p>q <code>a`</code></p>", "q `` a` ``"),
    ("<p>x<code> y </code>z</p>", "x `y` z"),
    ("<p><code>a\n\t  b</code></p>", "`a b`"),
    ("<p><code>&lt;tag&gt; &amp;</code></p>", "`<tag> &`"),
    ("<p><code>≅<!--approx =--></code>.</p>", "`≅`."),
    ("<p>a <code> </code> b</p>", "a b"),
])
def test_inline_code(html, md):
    assert inline(frag(html)) == md


def test_inline_code_with_line_breaks_stays_raw_html():
    assert inline(frag("<p><code>a<br/>b</code></p>")) == "<code>a<br>b</code>"


def test_spaces_inside_inline_code_are_not_collapsed_by_paragraph_rules():
    assert inline(frag("<p>a  <code>x  y</code>  b</p>")) == "a `x  y` b"


def test_trailing_spaces_on_lines_are_removed():
    md, _ = pre("<pre>a  \nb\t\nc\u00a0</pre>")
    assert md == "```\na\nb\nc\u00a0\n```"


def test_tabs_in_a_raw_pre_are_expanded_to_eight_columns():
    md, _ = pre("<pre>\n\t∇ r<b>x</b>\tz\n</pre>")
    assert md == "<pre>\n        ∇ r<b>x</b>    z\n</pre>"


def test_text_after_a_comment_in_inline_code_is_kept():
    assert inline(frag("<p><code>a<!-- note -->b<br/>c</code></p>")) == "<code>ab<br>c</code>"


def test_adjacent_code_elements_are_merged():
    assert inline(frag("<p>use <code>f</code><code>⍤</code> and <tt>a</tt><code>b</code>.</p>")) == \
        "use `f⍤` and `ab`."
