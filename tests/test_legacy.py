"""Issue #21: normalising legacy trad/ HTML."""

import lxml.html
import pytest

from vecrescue.legacy import fix_comments, mapped_apl, normalise


def body(html):
    doc = lxml.html.fromstring(f"<html><body>{html}</body></html>")
    notes = []
    normalise(doc, notes)
    return lxml.html.tostring(doc.find("body"), encoding="unicode")[6:-7].strip(), notes


CRUMB_TABLE = ('<table width="100%"><tr><td><font size="-1"><a href="http://www.vector.org.uk">'
               '<img src="../../icons/iconnavy.gif"></a> <a href="../../?area=vect&amp;page=content/archive">'
               'back issues</a> &gt; <a href="index.htm">contents of Vector 22.3</a></font></td></tr></table>')
CRUMB_P = ('<p style="font-size:80%"><a href="http://www.vector.org.uk">www.vector.org.uk</a> &gt; '
           '<a href="../../?area=vect&amp;page=content/archive">back issues</a></p>')


def test_breadcrumbs_and_their_rule_are_dropped():
    out, notes = body(f'{CRUMB_TABLE}<div class="Section1"><h1>T</h1><p>Text</p></div>'
                      f'<hr noshade><p class="crumb">{CRUMB_P[3:-4]}</p>')
    assert out == "<h1>T</h1><p>Text</p>"
    assert notes == [{"kind": "breadcrumbs-dropped", "count": 2}]


def test_breadcrumb_paragraph_and_crumbs_class():
    out, _ = body(f'{CRUMB_P}<h1>T</h1><p>x</p><hr><p class="crumbs cbtm">'
                  '<a href="../display.htm">Problems?</a></p>')
    assert out == "<h1>T</h1><p>x</p>"


def test_a_paragraph_that_mentions_the_site_inside_text_is_kept():
    out, _ = body('<p>See <a href="http://www.vector.org.uk">the website</a> for more, '
                  'and <p>nested</p></p>')
    assert "the website" in out


@pytest.mark.parametrize("html, out", [
    ('<font face="Book Antiqua"><p>a</p></font>', "<p>a</p>"),
    ('<p><font size="-1">small</font> text</p>', "<p>small text</p>"),
    ('<center><h1>T</h1></center>', "<h1>T</h1>"),
    ('<div align="center"><h1>T</h1><p>b</p></div>', "<h1>T</h1><p>b</p>"),
    ('<div id="wrapper"><div class="liner"><div id="pageblock"><p>a</p></div></div></div>', "<p>a</p>"),
    ('<p><span style="font-size:10pt" lang="EN-GB">x</span><o:p></o:p></p>', "<p>x</p>"),
    ('<p class="MsoNormal"><span class="MsoHyperlink">x</span></p>', '<p class="MsoNormal">x</p>'),
])
def test_presentational_wrappers_are_unwrapped(html, out):
    assert body(html)[0] == out


def test_meaningful_spans_and_fonts_are_kept():
    out, _ = body('<p><span class="APLU">⍴⍵</span> <font face="APL2741">r</font></p>')
    assert out == '<p><span class="APLU">⍴⍵</span> <font face="APL2741">r</font></p>'


def test_fix_comments():
    assert fix_comments("a<!------------- x --------------->b") == "a<!-- x -->b"


@pytest.mark.parametrize("text, listed, reason", [
    ('<pre>x</pre>', False, None),
    ('<pre>x</pre>', True, "codingprobs"),
    ('<font face="APL2741">r</font>', False, "apl-font"),
    ("<font face='APLX Upright'>r</font>", False, "apl-font"),
    ('<span style="font-family:APLNet">r</span>', False, "apl-font"),
])
def test_mapped_apl(text, listed, reason):
    assert mapped_apl(text, "trad/v101/x.htm", {"trad/v101/x.htm"} if listed else set()) == reason
