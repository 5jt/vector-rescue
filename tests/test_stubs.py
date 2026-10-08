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
    assert not (docs / "art2").exists()          # no PDF, no transcription: the stale stub goes (#63)
    assert results["2"]["page"] is False


def test_article_with_no_source_gets_no_page(tmp_path):
    from vecrescue.pipeline import write_stub_pages
    results = write_stub_pages([RECORD], [], {}, tmp_path)
    assert results["10001000"] == {"pdf": None, "match": None, "transcribed": None, "own_pdf": None, "page": False}
    assert not (tmp_path / "docs" / "art10001000").exists()


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


def test_reviewed_transcription_names_its_reviewer(tmp_path):
    from vecrescue.stubs import write_transcribed
    path = _transcription(tmp_path, "reviewed\nreviewed_by: Jane Doe\nreviewed_on: '2026-10-06'")
    text = write_transcribed(RECORD, tmp_path / "docs", path, pdf=None).read_text()
    assert "not yet reviewed" not in text
    assert "*Transcribed from the printed issue. Reviewed by Jane Doe on 2026-10-06.*" in text


def test_doubtful_transcription_has_a_warning(tmp_path):
    from vecrescue.stubs import write_transcribed
    path = _transcription(tmp_path, "draft\nwarning: Two pages are\n  illegible.")
    text = write_transcribed(RECORD, tmp_path / "docs", path, pdf=None).read_text()
    head, body = text.split("---", 2)[1:]
    assert "warning: Two pages are illegible." in head
    assert '!!! warning "Doubtful transcription"\n\n    Two pages are illegible.\n' in body
    assert body.index("not yet reviewed") < body.index("!!! warning") < body.index("Some text.")


def test_transcription_without_text_keeps_the_stub(tmp_path):
    from vecrescue.pipeline import write_stub_pages
    path = _transcription(tmp_path, "draft\nwarning: Needs a human transcriber.")
    path.write_text(path.read_text().split("---\n\n")[0] + "---\n", encoding="utf-8")
    results = write_stub_pages([RECORD], [], {}, tmp_path, transcriptions=tmp_path / "transcriptions")
    assert results["10001000"]["transcribed"] == "failed"
    text = (tmp_path / "docs" / "art10001000" / "index.md").read_text()
    assert "status: not online" in text and "warning: Needs a human transcriber." in text
    assert '!!! warning "Not transcribed"\n\n    Needs a human transcriber.' in text and "The text of this article is not yet online." in text


def test_stub_pages_use_transcriptions(tmp_path):
    from vecrescue.pipeline import write_stub_pages
    _transcription(tmp_path)
    results = write_stub_pages([RECORD], [], {}, tmp_path, transcriptions=tmp_path / "transcriptions")
    assert results["10001000"]["transcribed"] == "draft"
    assert "Some text." in (tmp_path / "docs" / "art10001000" / "index.md").read_text()


def test_stub_includes_the_ocr_block(tmp_path):
    text = write_stub(RECORD, tmp_path, pdf="1/1/x.pdf#page=67", ocr="<details>…</details>").read_text()
    assert text.rstrip().endswith("<details>…</details>")


def _damaged_pdf(path, printed):
    """A PDF cut off after its pages' content streams (#81): one stream per
    page, each word placed by Tm and shown in UTF-16BE by Tj, as a scanner
    writes its invisible OCR layer; no page tree, no %%EOF."""
    import zlib

    def word(x, y, w):
        return f"1 0 0 1 {x} {y} Tm\n(".encode() + w.encode("utf-16-be") + b")Tj\n"   # () balanced, unescaped
    data = b"%PDF-1.4\n"
    for i, n in enumerate(printed):
        body = b"BT\n3 Tr\n" + word(10, 590, "VECTOR") + word(200, 590.4, str(n))
        body += word(10, 560, f"Words of page {n},") + word(80, 560.6, "skewed (a little)")
        body += word(10, 550, "and their next line.") + word(10, 520, "A new paragraph.") + b"ET\n"
        stream = zlib.compress(body)
        data += f"{i + 5} 0 obj\n<</Length {len(stream)}/Filter /FlateDecode>>\nstream\n".encode() + stream
        data += b"\nendstream\nendobj\n"
    path.write_bytes(data + b"99 0 obj\n<</Length 4000/Filter /FlateDecode>>\nstream\nx\x9c")   # cut mid-stream
    return path


def test_ocr_text_is_recovered_from_a_truncated_pdf(tmp_path):
    from vecrescue.stubs import recovered_pages
    pages = recovered_pages(_damaged_pdf(tmp_path / "VOL.1-NO.1-MAY-1984.pdf", [63, 64]))
    assert pages == ["VECTOR 63\n\nWords of page 63, skewed (a little)\nand their next line.\n\nA new paragraph.",
                     "VECTOR 64\n\nWords of page 64, skewed (a little)\nand their next line.\n\nA new paragraph."]


def test_article_in_a_damaged_issue_shows_its_recovered_text(tmp_path):
    from vecrescue.pipeline import write_stub_pages
    pdf = _damaged_pdf(tmp_path / "VOL.1-NO.1-MAY-1984.pdf", [2, 3, 4, 5])   # printed page = PDF page + 1
    results = write_stub_pages([dict(RECORD, page="4")], [], {}, tmp_path, damaged={("1", "1"): pdf})
    assert results["10001000"]["page"] is True and results["10001000"]["pdf"] is None
    text = (tmp_path / "docs" / "art10001000" / "index.md").read_text()
    assert "The only copy found, on vector.org.uk, is damaged" in text
    assert "Read it in the PDF" not in text
    assert "<summary>Unedited OCR text, machine-read from a scan now lost" in text
    assert "<p>Words of page 4, skewed (a little) and their next line.</p>" in text
    assert "page 3," not in text


def test_article_pdf_published_and_linked(tmp_path):
    """#111: the article's own PDF goes beside its page, linked; with no issue
    scan it still gives the article a page."""
    from vecrescue.pipeline import write_stub_pages
    src = tmp_path / "src"
    (src / "trad/v112").mkdir(parents=True)
    (src / "trad/v112/langlet.pdf").write_bytes(b"%PDF-1.4")
    record = dict(RECORD, sources=[{"fmt": "PDF", "path": "trad/v112/langlet.pdf"}])
    results = write_stub_pages([record], [], {}, tmp_path, src=src)
    page = tmp_path / "docs/art10001000"
    assert (page / "langlet.pdf").read_bytes() == b"%PDF-1.4"
    assert "[Read it in the article’s own PDF](langlet.pdf)" in (page / "index.md").read_text(encoding="utf-8")
    assert results["10001000"]["page"] is True and results["10001000"]["own_pdf"] == "langlet.pdf"


def test_transcribed_page_links_article_pdf(tmp_path):
    from vecrescue.stubs import write_transcribed
    t = tmp_path / "art10001000.md"
    t.write_text("---\nvid: '10001000'\ntitle: Why APL?\nreview: draft\n---\nText.\n", encoding="utf-8")
    text = write_transcribed(RECORD, tmp_path / "docs", t, "1/1/x.pdf#page=67", own="a.pdf").read_text(encoding="utf-8")
    assert "[Read it in the article’s own PDF](a.pdf) [Read it in the PDF of the issue, page 65]" in text
