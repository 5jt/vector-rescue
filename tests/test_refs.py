"""Issue #7: references, anchors, editor's notes, mathematics."""

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


# anchors ---------------------------------------------------------------------

@pytest.mark.parametrize("html, out", [
    ('<p><a name="ref1"> </a>Bell, <cite>Men</cite></p>', '<a id="ref1"></a>Bell, *Men*'),
    ('<p><a id="fn2"></a>x</p>', '<a id="fn2"></a>x'),
    ('<p><a name="n3">Note <em>3</em></a></p>', '<a id="n3"></a>Note *3*'),
    ('<p><a name="r" href="http://x.org">X</a></p>', '<a id="r"></a>[X](http://x.org)'),
])
def test_anchors_become_ids(html, out):
    assert inline(frag(html)) == out


def test_reference_list_becomes_a_markdown_list_with_anchors():
    assert md('<ol class="references"><li><a name="ref1"> </a>One</li>'
              '<li><a name="ref2"> </a>Two</li></ol>') == \
        '1. <a id="ref1"></a>One\n2. <a id="ref2"></a>Two'


def test_div_with_an_id_keeps_the_id_as_an_anchor():
    assert md('<div id="references"><h2>References</h2><ol><li>A</li></ol></div>') == \
        '<a id="references"></a>\n\n## References\n\n1. A'


# classed paragraphs ------------------------------------------------------------

@pytest.mark.parametrize("cls, out", [
    ("ednote", "{ .ednote }"), ("center math", "{ .math }"),
    ("fright", "{ .right }"), ("fleft", "{ .left }"), ("math fright", "{ .math .right }"),
])
def test_classed_paragraphs_keep_their_meaning(cls, out):
    assert md(f'<p class="{cls}">x<sub>2</sub> <em>Ed.</em><!-- c --></p>') == \
        f"x<sub>2</sub> *Ed.*\n{out}"


def test_ednote_inside_a_list_stays_markdown():
    assert md('<ul><li><p class="ednote">n</p></li></ul>') == "- n\n    { .ednote }"


# divs ------------------------------------------------------------------------

def test_layout_only_divs_are_transparent():
    assert md('<div class="center pad"><p>a</p></div><div class="clear"><p>b</p></div>') == "a\n\nb"


def test_panel_div_becomes_a_markdown_div():
    assert md('<div class="fright panel plain small" style="width: 18em">'
              '<h3 class="center">Strange</h3><p>t</p></div>') == \
        '<div class="panel right" markdown="1">\n\n### Strange\n\nt\n\n</div>'


# maths and embeds ---------------------------------------------------------------

def test_inline_mathml_stays_in_the_paragraph():
    out = md('<p>so <math><mi>a</mi><mo>=</mo><mn>5</mn></math> here</p>')
    assert out == "so <math><mi>a</mi><mo>=</mo><mn>5</mn></math> here"


def test_block_mathml_passes_through_and_is_noted():
    out, notes = blocks('<math display="block"><mi>a</mi></math>')
    assert out == '<math display="block"><mi>a</mi></math>'
    assert notes == [{"kind": "mathml"}]


def test_embedded_video_becomes_a_link():
    out, notes = blocks('<p>See it.<br/><object width="2"><param name="movie" '
                        'value="http://www.youtube.com/v/Gd&amp;hl=en"/>'
                        '<embed src="http://www.youtube.com/v/Gd&amp;hl=en"/></object></p>')
    assert out == "See it.  \n[Video: http://www.youtube.com/v/Gd&hl=en](http://www.youtube.com/v/Gd&hl=en)"
    assert notes == [{"kind": "embed-replaced", "url": "http://www.youtube.com/v/Gd&hl=en"}]


def test_classed_paragraph_starting_with_raw_html_becomes_an_html_paragraph():
    out, _ = blocks('<p class="center math"><math><mi>a</mi></math> = <em>b</em></p>')
    assert out == '<p class="math" markdown="span"><math><mi>a</mi></math> = *b*</p>'
