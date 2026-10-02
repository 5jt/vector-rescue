"""Issue #4: block and inline elements."""

import lxml.html
import pytest

from vecrescue.convert import body_blocks
from vecrescue.markdown import inline


def frag(html):
    return lxml.html.fragment_fromstring(html)


def blocks(html):
    notes = []
    md = "\n\n".join(body_blocks(frag(f"<div>{html}</div>"), notes))
    return md, notes


def md(html):
    return blocks(html)[0]


# inline ----------------------------------------------------------------------

@pytest.mark.parametrize("html, out", [
    ("<p>a <em>b</em> c</p>", "a *b* c"),
    ("<p>a <i>b</i> <cite>Vector</cite> <dfn>raze</dfn> <var>x</var></p>", "a *b* *Vector* *raze* *x*"),
    ("<p><strong>s</strong> <b>t</b></p>", "**s** **t**"),
    ("<p>x<em> y </em>z</p>", "x *y* z"),
    ("<p>a<em></em>b</p>", "ab"),
    ("<p><strong>a <em>b</em></strong></p>", "**a *b***"),
    ("<p><tt>⍳10</tt></p>", "`⍳10`"),
    ("<p>x<sup>2</sup> H<sub>2</sub>O <q>q</q></p>", "x<sup>2</sup> H<sub>2</sub>O <q>q</q>"),
    ("<p><span class='nowrap'>a<sup>2</sup></span></p>", "a<sup>2</sup>"),
    ("<p><span class='italic'>it</span></p>", "*it*"),
    ("<p>line one<br/>line two</p>", "line one  \nline two"),
])
def test_inline(html, out):
    assert inline(frag(html)) == out


@pytest.mark.parametrize("html, out", [
    ('<p><a href="http://x.org/a">site</a></p>', "[site](http://x.org/a)"),
    ('<p><a href="http://x.org" title="T">s</a></p>', '[s](http://x.org "T")'),
    ('<p><a href="#ref2">[2]</a></p>', "[\\[2\\]](#ref2)"),
    ('<p><a href="http://x.org/a b">s</a></p>', '<a href="http://x.org/a%20b">s</a>'),
    ('<p><a href="x" title=\'say "hi"\'>s</a></p>', '<a href="x" title=\'say "hi"\'>s</a>'),
    ('<p><a name="ref1"> </a>Text</p>', '<a id="ref1"></a>Text'),
])
def test_links(html, out):
    assert inline(frag(html)) == out


@pytest.mark.parametrize("text, out", [
    ("2*3 a_b `x` [n] \\", "2\\*3 a\\_b \\`x\\` \\[n\\] \\\\"),
    ("a &lt;b&gt;", "a &lt;b>"),
    ("AT&amp;T &amp;lt;", "AT&T &amp;lt;"),
])
def test_text_is_escaped(text, out):
    assert inline(frag(f"<p>{text}</p>")) == out


@pytest.mark.parametrize("text, out", [
    ("# not heading", "\\# not heading"),
    ("1. not a list", "1\\. not a list"),
    ("- not a list", "\\- not a list"),
    ("+ x", "\\+ x"),
    ("> not quote", "\\> not quote"),
    ("=====", "\\====="),
])
def test_block_start_is_escaped(text, out):
    assert md(f"<p>{text}</p>") == out


# blocks ----------------------------------------------------------------------

def test_headings():
    assert md("<h2>Two</h2><h3>Three <em>x</em></h3><h4>4</h4><h5>5</h5>") == \
        "## Two\n\n### Three *x*\n\n#### 4\n\n##### 5"


def test_heading_id_and_break():
    assert md('<h2 id="Prelim">A<br/>B</h2>') == "## A B { #Prelim }"


def test_lists():
    assert md("<ul><li>a</li><li>b <em>c</em></li></ul><ol><li>x</li><li>y</li></ol>") == \
        "- a\n- b *c*\n\n1. x\n2. y"


def test_ordered_list_start():
    assert md('<ol start="0"><li>z</li><li>o</li></ol>') == "0. z\n1. o"


def test_nested_list():
    assert md("<ul><li>a<ul><li>b</li></ul></li><li>c</li></ul>") == \
        "- a\n    - b\n- c"


def test_list_item_with_blocks_makes_a_loose_list():
    assert md("<ul><li><p>p1</p><pre>\ncode</pre></li><li>t</li></ul>") == \
        "- p1\n\n    ```\n    code\n    ```\n\n- t"


def test_list_with_unmarkdownable_numbering_stays_raw():
    out, notes = blocks('<ol class="alpha"><li>a</li></ol>')
    assert out.startswith('<ol class="alpha">')
    assert notes == [{"kind": "raw-html", "tag": "ol", "reason": "numbering"}]


def test_blockquote():
    assert md("<blockquote><p>a</p><p>b</p></blockquote>") == "> a\n>\n> b"


def test_blockquote_with_code_and_nesting():
    assert md("<blockquote><pre>\n  x</pre><blockquote><p>in</p></blockquote></blockquote>") == \
        "> ```\n>   x\n> ```\n>\n> > in"


def test_blockquote_bare_text():
    assert md("<blockquote>said <em>so</em></blockquote>") == "> said *so*"


def test_definition_list():
    assert md("<dl><dt>Term <em>t</em></dt><dd>Def</dd><dt>T2</dt>"
              "<dd><p>p</p><pre>\nc</pre></dd></dl>") == \
        "Term *t*\n:   Def\n\nT2\n:   p\n\n    ```\n    c\n    ```"


def test_hr():
    assert md("<p>a</p><hr/><p>b</p>") == "a\n\n***\n\nb"


def test_plain_div_is_transparent():
    assert md("<div><p>a</p><div class='clear'></div></div>") == "a"


def test_paragraph_classes_with_meaning_are_kept_and_layout_dropped():
    out, notes = blocks('<p class="ednote">e</p><p class="center">x</p>')
    assert out == 'e\n{ .ednote }\n\nx'


def test_paragraph_with_block_content_stays_raw():
    out, _ = blocks('<p>See <svg:svg><svg:text>x</svg:text></svg:svg></p>')
    assert out.startswith("<p>See <svg:svg")


def test_empty_paragraph_is_dropped():
    assert md('<p class="pagebreak"><br/><br/></p><p>x</p>') == "x"


def test_whitespace_between_inline_elements_in_a_container_is_kept():
    assert md("<ul><li>is <code>v1</code>\n   <em>necessarily</em> so</li></ul>") == \
        "- is `v1` *necessarily* so"


def test_link_text_edge_spaces_move_outside_the_link():
    assert inline(frag('<p>see<a href="http://x.org"> x.org </a>.</p>')) == \
        "see [x.org](http://x.org) ."


def test_emphasis_of_punctuation_alone_stays_raw():
    assert inline(frag("<p>0-xFFFF<strong>,</strong> except</p>")) == \
        "0-xFFFF<strong>,</strong> except"


def test_markdown_characters_inside_inline_raw_html_are_escaped():
    assert inline(frag('<p><code>GetFiles("*.*",<br/>x)</code></p>')) == \
        '<code>GetFiles("\\*.\\*",<br>x)</code>'


def test_list_item_starting_with_code_puts_the_fence_on_its_own_line():
    assert md("<ul><li><pre>\ncode</pre><p>after</p></li><li>x</li></ul>") == \
        "- \n    ```\n    code\n    ```\n\n    after\n\n- x"


def test_definition_starting_with_code_puts_the_fence_on_its_own_line():
    assert md("<dl><dt>T</dt><dd><pre>\ncode</pre><p>after</p></dd></dl>") == \
        "T\n:   \n    ```\n    code\n    ```\n\n    after"


def test_container_holding_raw_html_says_so():
    _, notes = blocks("<blockquote><table><tr><td>1</td></tr></table></blockquote>")
    assert notes[-1] == {"kind": "raw-html", "tag": "blockquote", "reason": "contains-raw-html"}
