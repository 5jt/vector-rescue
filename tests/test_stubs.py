"""Issue #38: a page for every indexed article."""

import pytest

from vecrescue.stubs import page_offset, title_on_page, write_stub


def test_page_offset_is_the_commonest_difference():
    pages = ["Cover", "Contents 3", "VECTOR Vol.10 No.1\ntext\n1", "text\n2", "Vol.10 No.1\n3", "no number"]
    assert page_offset(pages) == 2


def test_page_offset_none_when_no_numbers():
    assert page_offset(["a", "b"]) is None


@pytest.mark.parametrize("title, text, found", [
    ("The Chosen 36 APL Characters", "VECTOR Vol.5 No.2 The Chosen 36 APL Characters The symbols", True),
    ("Seize the Time: The APL Programmer's Toolkit", "Seize the Time The APL Programmers Toolkit", True),
    ("Mandelbrot Sets", "Hackers Corner", False),
])
def test_title_on_page(title, text, found):
    assert title_on_page(title, text) == found


RECORD = {"id": "10001000", "title": "Why APL?", "authors": ["A. Writer"], "volume": "1",
          "issue": "1", "page": "65", "online": None}


def test_stub_with_pdf_link(tmp_path):
    path = write_stub(RECORD, tmp_path, pdf="1/1/VOL.1-NO.1-MAY-1984.pdf#page=67")
    text = path.read_text(encoding="utf-8")
    assert path == tmp_path / "art10001000" / "index.md"
    assert "title: Why APL?" in text and "vid: '10001000'" in text and "status: not online" in text
    assert "[Read it in the PDF of the issue, page 65](../1/1/VOL.1-NO.1-MAY-1984.pdf#page=67)" in text


def test_stub_without_pdf(tmp_path):
    text = write_stub(RECORD, tmp_path, pdf=None).read_text(encoding="utf-8")
    assert "not yet online" in text and "PDF" not in text.split("---", 2)[2]


def test_stub_pages_are_rewritten_on_every_site_run(tmp_path):
    import json
    from vecrescue.pipeline import write_stub_pages
    docs = tmp_path / "docs"
    (docs / "art1").mkdir(parents=True)
    (docs / "art1" / "index.md").write_text("converted")
    (docs / "art2").mkdir()
    (docs / "art2" / "index.md").write_text("a stub from the last run")
    (tmp_path / "notes.json").write_text(json.dumps({"1": []}))          # only art1 was converted
    inv = [dict(RECORD, id="1"), dict(RECORD, id="2")]
    results = write_stub_pages(inv, [], {}, tmp_path)
    assert list(results) == ["2"]
    assert (docs / "art1" / "index.md").read_text() == "converted"
    assert "not yet online" in (docs / "art2" / "index.md").read_text()
