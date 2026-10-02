"""Issue #21: rule changes found by converting the trad/ articles."""

import lxml.html
import pytest

from vecrescue.convert import body_blocks, expand_pre_tabs
from vecrescue.head import extract_head
from vecrescue.markdown import inline


def frag(html):
    return lxml.html.fragment_fromstring(html)


def blocks(html):
    notes = []
    md = "\n\n".join(body_blocks(frag(f"<div>{html}</div>"), notes))
    return md, notes


def md(html):
    return blocks(html)[0]


@pytest.mark.parametrize("html, out", [
    ("<p>2<i>n</i>2</p>", "2<i>n</i>2"),                       # inside a word
    ("<p>(a/<i>n</i>)</p>", "(a/<i>n</i>)"),                   # after a symbol
    ("<p>pseudo<em>prime</em>, x</p>", "pseudo<em>prime</em>, x"),
    ("<p>a <em>b</em>, c</p>", "a *b*, c"),                    # safely bounded
    ("<p>(<em>b</em>)</p>", "(*b*)"),
    ("<p>“<b>bold</b>”</p>", "“**bold**”"),
])
def test_emphasis_is_markdown_only_when_safely_bounded(html, out):
    assert inline(frag(html)) == out


def test_emphasis_of_only_a_space_keeps_the_space():
    assert inline(frag("<p>Conference<i> </i>Proceedings</p>")) == "Conference Proceedings"


@pytest.mark.parametrize("text, out", [("=", "&#61;"), ("== x", "&#61;= x"), ("a = b", "a = b")])
def test_leading_equals_sign_is_an_entity(text, out):
    assert md(f"<p>{text}</p>") == out


def test_text_after_a_list_item_joins_that_item():
    out, notes = blocks("<ul><li>A second bit.</li> A third bit.</ul>")
    assert out == "- A second bit.\n\n    A third bit."
    assert {"kind": "list-stray-text"} in notes


def test_paragraph_holding_blocks_is_rendered_as_a_container():
    # built by hand: the parser would close the <p>, but malformed sources
    # can still leave one open over blocks
    div = frag("<div><p>Before</p></div>")
    for html in ("<hr/>", "<h1>Appendix</h1>", "<h2>Part</h2>"):
        div[0].append(frag(html))
    div[0][-1].tail = "after"
    notes = []
    out = "\n\n".join(body_blocks(div, notes))
    assert out == "Before\n\n***\n\n## Appendix\n\n## Part\n\nafter"
    assert {"kind": "p-holding-blocks"} in notes


def test_anchor_wrapping_blocks_keeps_the_anchor_and_converts_the_blocks():
    out, _ = blocks('<a name="acct"><h2>Accounts</h2><pre>\n (R&amp;P)</pre></a>')
    assert out == '<a id="acct"></a>\n\n## Accounts\n\n```\n (R&P)\n```'


def test_address_is_a_paragraph():
    assert md("<address>The Editor<br/>London</address>") == "The Editor  \nLondon"


@pytest.mark.parametrize("html, raw", [
    ('<ul type="disc"><li>a</li></ul>', False), ('<ul style="list-style: square"><li>a</li></ul>', False),
    ('<ol type="1"><li>a</li></ol>', False), ('<ol type="a"><li>a</li></ol>', True),
    ('<ol style="list-style-type: lower-roman"><li>a</li></ol>', True),
])
def test_list_bullet_styles_are_dropped_but_numbering_styles_kept_raw(html, raw):
    assert md(html).startswith("<") == raw


def test_byline_starting_with_html_becomes_an_html_paragraph():
    doc = lxml.html.fromstring('<html><body><h1>T</h1><p class="author"><sup>1</sup> me</p>'
                               '<p>b</p></body></html>')
    _, lead = extract_head(doc, {"id": "1", "title": "T", "authors": []}, [])
    assert lead == ['<p class="byline" markdown="span"><sup>1</sup> me</p>']


def test_head_elements_anywhere_in_the_body_are_removed():
    doc = lxml.html.fromstring('<html><body><div><title>T</title><link rel="x"/><meta name="a"/>'
                               '<h1>T</h1></div><p>b</p></body></html>')
    extract_head(doc, {"id": "1", "title": "T", "authors": []}, [])
    assert not doc.xpath("//body//title|//body//link|//body//meta")


def test_tabs_in_every_pre_are_expanded_before_conversion():
    doc = lxml.html.fromstring("<html><body><table><tr><td><pre>a\tb</pre></td></tr></table></body></html>")
    expand_pre_tabs(doc)
    assert doc.find(".//pre").text == "a       b"


@pytest.mark.parametrize("html, out", [
    ("<p>press <ctrl+break> now</p>", "press &lt;ctrl+break> now"),
    ("<p>Write to <acamacho@cix.compulink.co.uk></p>", "Write to &lt;acamacho@cix.compulink.co.uk>"),
])
def test_made_up_tags_are_shown_as_text(html, out):
    md_out, notes = blocks(html)
    assert md_out == out
    assert notes[0]["kind"] == "made-up-tag-as-text"


def test_unclosed_made_up_tag_wrapping_blocks_renders_them_as_blocks():
    div = frag("<div><p>so p<t>p</t></p></div>")
    t = div[0][0]
    t.append(frag("<pre>\np * q</pre>"))
    t.append(frag("<p>After</p>"))
    notes = []
    out = "\n\n".join(body_blocks(div, notes))
    assert out == "so p&lt;t>p\n\n```\np * q\n```\n\nAfter"


def test_adjacent_emphasis_falls_back_to_html():
    assert inline(frag("<p>z − <i>a</i><i>n</i> x</p>")) == "z − <i>a</i><i>n</i> x"


def test_anchor_keeps_the_space_at_the_end_of_its_text():
    assert inline(frag('<p><a name="t">the Class\n</a>Prototype</p>')) == '<a id="t"></a>the Class Prototype'


def test_template_always_shows_the_title():
    from pathlib import Path
    t = (Path(__file__).parents[1] / "site/overrides/partials/content.html").read_text()
    assert "<h1" in t and "not in page.content" not in t


def test_nested_emphasis_at_the_edge_falls_back_to_html():
    assert inline(frag("<p>so <i>z − <i>n</i></i> x</p>")) == "so <i>z − <i>n</i></i> x"
