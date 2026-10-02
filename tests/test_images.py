"""Issue #6: figures and images."""

import lxml.html
import pytest

from vecrescue.convert import body_blocks
from vecrescue.images import localise_images, sniff
from vecrescue.markdown import inline

PNG = b"\x89PNG\r\n\x1a\n" + b"0" * 20
BMP = b"BM" + b"0" * 20


def frag(html):
    return lxml.html.fragment_fromstring(html)


def blocks(html):
    notes = []
    md = "\n\n".join(body_blocks(frag(f"<div>{html}</div>"), notes))
    return md, notes


# inline <img> -----------------------------------------------------------------

@pytest.mark.parametrize("html, out", [
    ('<p><img src="a.png" alt="A"/></p>', "![A](a.png)"),
    ('<p><img src="a.png" alt="A" title="T"/></p>', '![A](a.png "T")'),
    ('<p><img src="a.png" alt="" class="bdr center"/></p>', "![](a.png)"),
    ('<p><img src="a.png" alt="A" width="50" height="40"/></p>', '![A](a.png){ width="50" height="40" }'),
    ('<p><img src="a.png" alt="A" style="width: 200px"/></p>', '![A](a.png){ style="width: 200px" }'),
    ('<p><img src="a.png" alt="x [1]"/></p>', "![x \\[1\\]](a.png)"),
    ('<p><a href="http://x.org"><img src="a.png" alt="A"/></a></p>', "[![A](a.png)](http://x.org)"),
    ('<p><img src="a b.png" alt="A"/></p>', '<img src="a%20b.png" alt="A">'),
])
def test_inline_images(html, out):
    assert inline(frag(html)) == out


# p.caption → figure ----------------------------------------------------------

def test_caption_with_image_becomes_a_figure():
    md, _ = blocks('<p class="caption center"><img src="f.png" alt="F"/><br/>'
                   'Fig. 1. The <code>⍴</code> <em>plot</em></p>')
    assert md == ('<figure markdown="1">\n![F](f.png)\n'
                  '<figcaption markdown="span">Fig. 1. The `⍴` *plot*</figcaption>\n</figure>')


@pytest.mark.parametrize("cls, out", [("caption fright pad", "right"), ("bdr caption fleft", "left"),
                                      ("caption right", "right"), ("caption left", "left")])
def test_figure_float(cls, out):
    md, _ = blocks(f'<p class="{cls}"><img src="f.png" alt=""/></p>')
    assert md == f'<figure class="{out}" markdown="1">\n![](f.png)\n</figure>'


def test_linked_image_caption_with_line_breaks():
    md, _ = blocks('<p class="caption"><a href="big.png"><img src="f.png" alt=""/></a>'
                   '<br/>One<br/>two</p>')
    assert md == ('<figure markdown="1">\n[![](f.png)](big.png)\n'
                  '<figcaption markdown="span">One<br>two</figcaption>\n</figure>')


def test_caption_without_image_is_a_caption_paragraph():
    md, _ = blocks('<p class="caption">Table 1. Results</p>')
    assert md == "Table 1. Results\n{ .caption }"


def test_caption_with_several_images_stays_raw():
    md, notes = blocks('<p class="caption"><img src="a.png" alt=""/><br/>A'
                       '<img src="b.png" alt=""/><br/>B</p>')
    assert md.startswith('<p class="caption">')
    assert notes == [{"kind": "figure-raw", "reason": "several-images"}]


def test_figure_inside_a_list_makes_the_list_raw():
    md, _ = blocks('<ul><li><p class="caption"><img src="a.png" alt=""/></p></li></ul>')
    assert md.startswith("<ul>")


# localising image files ------------------------------------------------------

def test_sniff():
    assert sniff(PNG) == "png" and sniff(BMP) == "bmp" and sniff(b"junk") is None


def test_localise_images(tmp_path):
    root = tmp_path
    (root / "content" / "a" / "fig").mkdir(parents=True)
    (root / "content" / "a" / "fig" / "one.png").write_bytes(PNG)
    (root / "content" / "a" / "bmp.jpg").write_bytes(BMP)
    (root / "images" / "faces").mkdir(parents=True)
    (root / "images" / "faces" / "p.jpg").write_bytes(b"\xff\xd8\xff" + b"0" * 10)
    doc = lxml.html.fromstring(
        '<html><body><img src="fig/one.png"/><img src="bmp.jpg"/><img src="gone.gif"/>'
        '<img src="http://www.vector.org.uk/images/faces/p.jpg"/>'
        '<img src="http://archive.vector.org.uk/images/toons/x.png"/>'
        '<img src="http://elsewhere.org/y.png"/></body></html>')
    notes = []
    assets = localise_images(doc, root, "content/a/art.htm", notes)
    assert [i.get("src") for i in doc.iter("img")] == [
        "fig/one.png", "bmp.jpg", "gone.gif", "images/faces/p.jpg",
        "http://archive.vector.org.uk/images/toons/x.png", "http://elsewhere.org/y.png"]
    assert assets == {"fig/one.png": root / "content/a/fig/one.png",
                      "bmp.jpg": root / "content/a/bmp.jpg",
                      "images/faces/p.jpg": root / "images/faces/p.jpg"}
    assert notes == [
        {"kind": "image-format-mismatch", "src": "bmp.jpg", "actual": "bmp"},
        {"kind": "image-missing", "src": "gone.gif"},
        {"kind": "image-missing", "src": "http://archive.vector.org.uk/images/toons/x.png"},
    ]
