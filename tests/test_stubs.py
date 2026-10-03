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


def test_ocr_text_is_folded_away_and_escaped(tmp_path):
    from vecrescue.stubs import ocr_block
    pages = ["  VECTOR      Vol.10 No.1\n\nThisis the ratio   that matters\nnot so muchthefact.\n\n   3°20 FYAIL F  <b>\n", "Next page."]
    block = ocr_block(pages)
    assert block.startswith('<details class="ocr">\n<summary>Unedited OCR text')
    assert "<p>Thisis the ratio that matters not so muchthefact.</p>" in block
    assert "<p>3°20 FYAIL F &lt;b&gt;</p>" in block and "<p>Next page.</p>" in block
    assert block.endswith("</details>")


TRANSCRIPTION = """---
vid: '10001000'
title: Why APL?
authors:
- A. Writer
volume: '1'
issue: '1'
page: '65'
transcribed: from page images of VOL.1-NO.1-MAY-1984.pdf, pages 67–68; Claude, 2026-10-03
review: draft
queries:
- "A slip, transcribed as printed."
---

by A. Writer
{ .byline }

Some text.

![A graph](art10001000/graph.png)
"""


def _transcription(tmp_path, review="draft"):
    folder = tmp_path / "transcriptions"
    (folder / "art10001000").mkdir(parents=True)
    (folder / "art10001000" / "graph.png").write_bytes(b"png")
    path = folder / "art10001000.md"
    path.write_text(TRANSCRIPTION.replace("review: draft", f"review: {review}"), encoding="utf-8")
    return path


def test_transcription_replaces_the_stub(tmp_path):
    from vecrescue.stubs import write_transcribed
    docs = tmp_path / "docs"
    path = write_transcribed(RECORD, docs, _transcription(tmp_path), pdf="1/1/x.pdf#page=67")
    text = path.read_text(encoding="utf-8")
    fm, body = text.split("---", 2)[1:]
    assert "status: transcribed" in fm and "review: draft" in fm and "not online" not in fm
    assert "Transcribed from the printed issue; not yet reviewed." in body
    assert "[Read it in the PDF of the issue, page 65](../1/1/x.pdf#page=67)" in body
    assert "Some text." in body and "<details" not in body


def test_transcription_figures_are_copied_and_relinked(tmp_path):
    from vecrescue.stubs import write_transcribed
    docs = tmp_path / "docs"
    text = write_transcribed(RECORD, docs, _transcription(tmp_path), pdf=None).read_text(encoding="utf-8")
    assert "![A graph](graph.png)" in text
    assert (docs / "art10001000" / "graph.png").read_bytes() == b"png"


def test_approved_transcription_has_no_review_note(tmp_path):
    from vecrescue.stubs import write_transcribed
    text = write_transcribed(RECORD, tmp_path / "docs", _transcription(tmp_path, "approved"), pdf=None).read_text()
    assert "not yet reviewed" not in text and "Transcribed from the printed issue." in text


def test_stub_pages_use_transcriptions(tmp_path):
    from vecrescue.pipeline import write_stub_pages
    _transcription(tmp_path)
    results = write_stub_pages([RECORD], [], {}, tmp_path, transcriptions=tmp_path / "transcriptions")
    assert results["10001000"]["transcribed"] == "draft"
    assert "Some text." in (tmp_path / "docs" / "art10001000" / "index.md").read_text()


def test_stub_includes_the_ocr_block(tmp_path):
    text = write_stub(RECORD, tmp_path, pdf="1/1/x.pdf#page=67", ocr="<details>…</details>").read_text()
    assert text.rstrip().endswith("<details>…</details>")
