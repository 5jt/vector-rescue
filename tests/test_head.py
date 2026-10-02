"""Issue #2: the article head block becomes front matter."""

import lxml.html
import pytest

from vecrescue.head import extract_head

RECORD = {"id": "1", "title": "Index title", "authors": ["A. Author"],
          "volume": "25", "issue": "1", "page": "7",
          "received": None, "online": None}


def run(body_html, meta="", record=RECORD):
    doc = lxml.html.fromstring(
        f"<html><head>{meta}</head><body>{body_html}<p>Body.</p></body></html>")
    notes = []
    fm, lead = extract_head(doc, record, notes)
    rest = [el.tag for el in doc.find("body")]
    return fm, lead, rest, notes


def test_title_comes_from_index_and_head_h1s_are_removed():
    fm, lead, rest, _ = run('<h1 id="title">Index title</h1><h1 id="author">by A</h1>')
    assert fm["title"] == "Index title"
    assert rest == ["p"]


@pytest.mark.parametrize("html", [
    '<h1 class="subtitle">Sub</h1>', '<h1 id="subtitle">Sub</h1>'])
def test_subtitle_variants(html):
    fm, lead, _, _ = run('<h1 id="title">T</h1>' + html)
    assert fm["subtitle"] == "Sub"
    assert lead[0] == "Sub\n{ .subtitle }"


def test_unmarked_h1_right_after_title_is_a_subtitle():
    fm, _, _, notes = run('<h1 id="title">T</h1><h1>4: The Year 1998</h1>')
    assert fm["subtitle"] == "4: The Year 1998"
    assert "unmarked-h1-as-subtitle" in [n["kind"] for n in notes]


def test_unmarked_h1_after_body_starts_is_left_for_the_body():
    _, _, rest, _ = run('<h1 id="title">T</h1><p>x</p><h1>Addendum</h1>')
    assert rest == ["p", "h1", "p"]


def test_h1_class_title_is_the_title():
    _, _, rest, _ = run('<h1 class="title">T</h1>')
    assert rest == ["p"]


@pytest.mark.parametrize("html", [
    '<p id="abstract">Ab <code>x</code></p>', '<p class="abstract">Ab <code>x</code></p>',
    '<div id="abstract"><p>Ab <code>x</code></p></div>'])
def test_abstract_variants(html):
    fm, lead, rest, _ = run(html)
    assert fm["abstract"] == "Ab x"
    assert lead == ["Ab `x`\n{ .abstract }"]
    assert rest == ["p"]


def test_byline_from_p_author_keeps_email():
    fm, lead, _, _ = run('<p id="author">by Chris (c@x.com)</p>')
    assert fm["byline"] == "by Chris (c@x.com)"
    assert lead == ["by Chris (c@x.com)\n{ .byline }"]


def test_publication_and_validation_are_dropped_wherever_they_are():
    _, _, rest, _ = run('<ul id="publication"><li>x</li></ul>'
                        '<div><p id="validation"><a href="v">&#160;</a></p></div>')
    assert rest == ["div", "p"]


def test_meta_fields():
    fm, _, _, _ = run("", '<meta name="editor" content="Ed"/>'
                          '<meta name="keywords" content="a, b,,c,"/>'
                          '<meta name="received" content="2011-02-05"/>')
    assert fm["editor"] == "Ed"
    assert fm["keywords"] == ["a", "b", "c"]
    assert fm["received"] == "2011-02-05"


def test_index_dates_win_over_meta():
    rec = dict(RECORD, online="2011-05-07")
    fm, _, _, _ = run("", '<meta name="online" content="1999-01-01"/>', rec)
    assert fm["online"] == "2011-05-07"


def test_meta_disagreeing_with_index_is_noted():
    _, _, _, notes = run("", '<meta name="page" content="8"/><meta name="vid" content="1"/>')
    assert notes == [{"kind": "meta-disagrees", "field": "page",
                      "meta": "8", "index": "7"}]


def test_page_title_not_in_index_title_is_noted():
    _, _, _, notes = run('<h1 id="title">Something else</h1>')
    assert [n["kind"] for n in notes] == ["title-differs"]


def test_decorations_inside_the_head_block_are_skipped_and_kept():
    fm, _, rest, _ = run('<div class="panel">from: x</div><h1 id="title">T</h1>'
                         '<div style="x"><code>y</code></div><h1 id="author">by A</h1>')
    assert fm["byline"] == "by A"
    assert rest == ["div", "div", "p"]


def test_unmarked_h1_before_any_title_is_the_title():
    fm, _, rest, notes = run('<h1>BAA London</h1><h1 id="author">Phil</h1>')
    assert rest == ["p"] and fm["byline"] == "Phil"
    assert "unmarked-h1-as-title" in [n["kind"] for n in notes]


def test_head_elements_misplaced_in_body_are_removed_and_noted():
    doc = lxml.html.fromstring(
        "<html><body><meta name='issue' content=''/><title>T</title>"
        "<h1 id='title'>T</h1><p>Body.</p></body></html>")
    notes = []
    extract_head(doc, RECORD, notes)
    assert [el.tag for el in doc.find("body")] == ["p"]
    assert {"kind": "head-element-in-body", "tag": "title"} in notes


def test_two_subtitles_are_both_kept():
    fm, lead, rest, _ = run('<h1 id="title">T</h1><h1 class="subtitle">One</h1>'
                            '<h1 class="subtitle"><em>or</em> Two</h1><h1 id="author">A</h1>')
    assert fm["subtitle"] == "One / or Two"
    assert lead[:2] == ["One\n{ .subtitle }", "*or* Two\n{ .subtitle }"]
    assert fm["byline"] == "A" and rest == ["p"]


def test_empty_byline_and_abstract_leave_no_lead_paragraph():
    fm, lead, _, _ = run('<h1 id="title">T</h1><h1 id="author"> </h1><p id="abstract"> </p>')
    assert lead == []
    assert "byline" not in fm and "abstract" not in fm


def test_consecutive_abstract_paragraphs_are_all_abstract():
    fm, lead, rest, _ = run('<h1 id="title">T</h1><p class="abstract">One.</p>'
                            '<p class="abstract">Two.</p>')
    assert fm["abstract"] == "One. Two."
    assert lead == ["One.\n{ .abstract }", "Two.\n{ .abstract }"]
    assert rest == ["p"]


def test_removed_lists_exactly_what_was_taken_out():
    doc = lxml.html.fromstring('<html><body><h1 id="title">T</h1><h1 id="author">A</h1>'
                               '<h1 id="author">B</h1><p>x</p></body></html>')
    removed = []
    extract_head(doc, RECORD, [], removed)
    assert [k for k, _ in removed] == ["title", "byline"]
    assert [el.tag for el in doc.find("body")] == ["h1", "p"]
