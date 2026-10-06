"""Issues #9, #68, #79: volume pages, the home page and the full index."""

from pathlib import Path

import pytest

from vecrescue.inventory import read_issues
from vecrescue.pages import write_home_page, write_index_page, write_volume_pages
from vecrescue.stubs import DAMAGED

SRC = Path(__file__).parent / "fixtures" / "src"

INVENTORY = [
    {"id": "3", "title": "Second | piece", "authors": ["B. B"], "volume": "25", "issue": "1", "page": "74"},
    {"id": "1", "title": "First *thing*", "authors": ["A. A", "C. C"], "volume": "25", "issue": "1", "page": "9"},
    {"id": "2", "title": "Not online", "authors": [], "volume": "25", "issue": "1", "page": "30"},
    {"id": "4", "title": "In the combined issue", "authors": [], "volume": "24", "issue": "3", "page": "5"},
    {"id": "5", "title": "Online only", "authors": ["D. D"], "volume": None, "issue": None, "page": None,
     "online": "2016-01-22"},
]
CONVERTED = {"1", "3", "5"}


def test_read_issues():
    by = {(i["volume"], i["issue"]): i for i in read_issues(SRC)}
    assert by[("25", "1")] == {"volume": "25", "issue": "1", "year": "2011", "month": "06",
                               "title": None, "span": 1, "numbers": ["1"],
                               "pdf": "v251.pdf", "doc": None}
    assert by[("24", "2")]["span"] == 2 and by[("24", "2")]["title"] == "Nos.2&3"
    assert by[("1", "1")]["pdf"] is None


def pages(tmp_path):
    docs = tmp_path / "docs"
    for i in CONVERTED:
        (docs / f"art{i}").mkdir(parents=True)
        (docs / f"art{i}" / "index.md").write_text("x")
    written = write_volume_pages(INVENTORY, read_issues(SRC), SRC, docs)
    return docs, written


def tab(text, label):
    """The indented body of the tab whose heading contains LABEL."""
    head = next(l for l in text.splitlines() if l.startswith('=== "') and label in l)
    body = text.split(head, 1)[1].split('\n=== "', 1)[0]
    return "\n".join(l[4:] for l in body.splitlines())


def test_volume_page_has_a_tab_per_issue_listing_articles_in_page_order(tmp_path):
    docs, _ = pages(tmp_path)
    text = (docs / "25" / "index.md").read_text(encoding="utf-8")
    assert "title: Volume 25, 2011–2012" in text
    assert '=== "N°1, June 2011"' in text
    assert tab(text, "N°1,").lstrip("\n").startswith("## N°1, June 2011 { #contents-n1-june-2011 }\n")    # a heading in the tab (#79)
    rows = [line for line in tab(text, "N°1,").splitlines() if line.startswith("| ") and "---" not in line][1:]
    assert rows == [
        "| 9 | [First \\*thing\\*](../art1/) | A. A, C. C |",
        "| 30 | Not online |  |",
        "| 74 | [Second \\| piece](../art3/) | B. B |",
    ]
    assert not (docs / "25" / "1" / "index.md").exists()    # no issue pages (#68)


def test_issue_pdf_is_copied_and_linked_below_the_table(tmp_path):
    docs, _ = pages(tmp_path)
    assert (docs / "25" / "1" / "v251.pdf").read_bytes().startswith(b"%PDF")
    body = tab((docs / "25" / "index.md").read_text(), "N°1,")
    assert body.index("| Page |") < body.index("[PDF of the whole issue](1/v251.pdf)")


def test_combined_issue_is_one_tab(tmp_path):
    docs, _ = pages(tmp_path)
    text = (docs / "24" / "index.md").read_text(encoding="utf-8")
    assert text.count('=== "N°2&3') == 1 and '=== "N°3' not in text
    assert "In the combined issue" in tab(text, "N°2&3")          # catalogued as 24:3


def test_issue_with_no_articles_still_has_a_tab(tmp_path):
    docs, _ = pages(tmp_path)
    assert "No articles are indexed" in tab((docs / "1" / "index.md").read_text(), "N°1")


def test_tabs_are_headed_by_colour_thumbnails(tmp_path):
    thumbs = tmp_path / "thumbs"
    thumbs.mkdir()
    (thumbs / "v2501.jpg").write_bytes(b"jpg")
    docs = tmp_path / "docs"
    write_volume_pages(INVENTORY, read_issues(SRC), SRC, docs, thumbs=thumbs)
    text = (docs / "25" / "index.md").read_text(encoding="utf-8")
    assert '=== "![Vector 25:1 cover](../covers/v2501.jpg) N°1, June 2011"' in text
    assert (docs / "covers" / "v2501.jpg").read_bytes() == b"jpg"


def test_home_page_tables_the_volumes_and_lists_online_only(tmp_path):
    from vecrescue.pages import tab_id
    docs, _ = pages(tmp_path)
    text = write_home_page(INVENTORY, read_issues(SRC), docs).read_text(encoding="utf-8")
    assert "# The Vector Archive" in text and 'class="masthead"' in text
    assert "| volume | years | N°1 | N°2 | N°3 | N°4 |" in text
    by = {(i["volume"], i["issue"]): i for i in read_issues(SRC)}
    row = next(l for l in text.splitlines() if l.startswith("| [24](24/)"))
    assert row.count(f"[24:2&3](24/#{tab_id(by[('24', '2')])})") == 2    # under N°2 and N°3
    assert f"[25:1](25/#{tab_id(by[('25', '1')])})" in text
    assert text.index("| [1](1/)") < text.index("| [24](24/)") < text.index("| [25](25/)")
    assert "## Published online only" in text
    assert "[Online only](art5/)" in text


def test_home_page_separates_in_press_articles(tmp_path):
    inv = INVENTORY + [{"id": "6", "title": "Never printed", "authors": [], "volume": None,
                        "issue": None, "page": None, "online": "2016-09-01", "in_press": True}]
    docs = tmp_path / "docs"
    for i in ("5", "6"):
        (docs / f"art{i}").mkdir(parents=True)
        (docs / f"art{i}" / "index.md").write_text("x")
    text = write_home_page(inv, read_issues(SRC), docs).read_text(encoding="utf-8")
    assert text.index("## Published online only") < text.index("[Online only]")
    assert text.index("## In press, never printed") < text.index("[Never printed]")


def test_combined_issue_numbers_come_from_the_title():
    by = {(i["volume"], i["issue"]): i for i in read_issues(SRC)}
    assert by[("25", "3")]["numbers"] == ["2", "3"]     # filed under its last number
    assert by[("24", "2")]["numbers"] == ["2", "3"]     # filed under its first
    assert by[("25", "4")]["numbers"] == ["4"]


def test_articles_link_to_their_issue_tab(tmp_path):
    from vecrescue.pages import mark_issue_tabs, tab_id
    docs = tmp_path / "docs"
    (docs / "art4").mkdir(parents=True)
    (docs / "art4" / "index.md").write_text("---\nvid: '4'\n---\n\nSee [21:2](../24/3/).\n")
    assert mark_issue_tabs(INVENTORY, read_issues(SRC), docs) == 1
    text = (docs / "art4" / "index.md").read_text()
    t = tab_id({i["issue"]: i for i in read_issues(SRC) if i["volume"] == "24"}["2"])
    assert f"\nissue_tab: {t}\n---" in text and f"](../24/#{t})" in text
    mark_issue_tabs(INVENTORY, read_issues(SRC), docs)                 # idempotent
    assert (docs / "art4" / "index.md").read_text() == text


import pytest
from vecrescue.pages import wayback_issue_pdfs


@pytest.mark.parametrize("name, key", [
    ("VOL.1-NO.1-MAY-1984.pdf", ("1", "1")),
    ("VOL.17-NO.4.pdf", ("17", "4")),
    ("VOL.23-NO.1-AND-2-JANUARY-2008.pdf", ("23", "1")),
    ("v241-1.pdf", ("24", "1")),          # -1: WordPress's duplicate-name suffix
    ("v252-3.pdf", ("25", "2")),          # Nos. 2&3
    ("Vector264.pdf", ("26", "4")),
])
def test_wayback_issue_pdf_names(tmp_path, name, key):
    d = tmp_path / "vector.org.uk/wp-content/uploads/2022/07"
    d.mkdir(parents=True)
    (d / name).write_bytes(b"%PDF-1.4\n%%EOF\n")
    assert wayback_issue_pdfs(tmp_path) == {key: d / name}


def test_issue_page_uses_a_wayback_pdf_when_the_tree_has_none(tmp_path):
    w = tmp_path / "wayback/vector.org.uk/wp-content/uploads/2022/07"
    w.mkdir(parents=True)
    (w / "VOL.1-NO.1-MAY-1984.pdf").write_bytes(b"%PDF 1984\n%%EOF")
    (w / "v251.pdf").write_bytes(b"%PDF other copy\n%%EOF")
    docs = tmp_path / "docs"
    write_volume_pages(INVENTORY, read_issues(SRC), SRC, docs, wayback_issue_pdfs(tmp_path / "wayback"))
    assert (docs / "1/1/VOL.1-NO.1-MAY-1984.pdf").read_bytes() == b"%PDF 1984\n%%EOF"
    assert "[PDF of the whole issue](1/VOL.1-NO.1-MAY-1984.pdf)" in (docs / "1/index.md").read_text()
    assert (docs / "25/1/v251.pdf").read_bytes().startswith(b"%PDF-1.4 fixture")   # ours preferred


def test_truncated_wayback_pdfs_are_not_used(tmp_path):
    d = tmp_path / "vector.org.uk/wp-content/uploads/2022/07"
    d.mkdir(parents=True)
    (d / "VOL.3-NO.4-APRIL-1987.pdf").write_bytes(b"%PDF-1.3\n" + b"0" * 100)        # no %%EOF
    (d / "VOL.3-NO.3-JANUARY-1987.pdf").write_bytes(b"%PDF-1.3\n...\n%%EOF\n")
    assert list(wayback_issue_pdfs(tmp_path)) == [("3", "3")]


def test_issue_page_marks_articles_only_in_the_pdf(tmp_path):
    from vecrescue.stubs import write_stub
    docs = tmp_path / "docs"
    for i in CONVERTED:
        (docs / f"art{i}").mkdir(parents=True)
        (docs / f"art{i}" / "index.md").write_text("x")
    write_stub(INVENTORY[2], docs, "25/1/v251.pdf#page=32")
    write_volume_pages(INVENTORY, read_issues(SRC), SRC, docs)
    text = tab((docs / "25" / "index.md").read_text(encoding="utf-8"), "N°1,")
    assert "| 30 | [Not online](../art2/) (PDF only) |  |" in text
    assert "⚠" not in text


def test_issue_without_a_scan_lists_sourceless_articles_unlinked(tmp_path):
    from vecrescue.pages import NO_SCAN
    docs = tmp_path / "docs"
    for i in CONVERTED:
        (docs / f"art{i}").mkdir(parents=True)
        (docs / f"art{i}" / "index.md").write_text("x")
    write_volume_pages(INVENTORY, read_issues(SRC), SRC, docs)
    text = tab((docs / "25" / "index.md").read_text(encoding="utf-8"), "N°1,")
    assert "| 30 | Not online |  |" in text and "art2" not in text
    assert ("PDF" in text) != (NO_SCAN in text)   # the note only where the issue has no PDF


def test_issue_page_marks_doubtful_transcriptions(tmp_path):
    from vecrescue.stubs import write_stub
    docs = tmp_path / "docs"
    for i in CONVERTED:
        (docs / f"art{i}").mkdir(parents=True)
        (docs / f"art{i}" / "index.md").write_text("x")
    write_stub(INVENTORY[2], docs, "25/1/v251.pdf#page=32", warning="Could not be transcribed.")
    write_volume_pages(INVENTORY, read_issues(SRC), SRC, docs)
    text = tab((docs / "25" / "index.md").read_text(encoding="utf-8"), "N°1,")
    assert '[Not online](../art2/) (PDF only) <span class="doubtful"' in text
    assert "\n⚠ The transcription is doubtful or missing; its page says why.\n" in text


def test_volumes_have_year_spans(tmp_path):
    from vecrescue.pages import volumes
    by = {v: (keys, span) for v, keys, span in volumes(INVENTORY, read_issues(SRC))}
    assert by["25"] == ([("25", "1"), ("25", "3"), ("25", "4")], "2011–2012")
    assert ("24", "2") in by["24"][0] and ("24", "3") not in by["24"][0]   # combined issue filed at 2


def test_nav_lists_home_full_index_and_volumes():
    from vecrescue.pages import nav_toml
    nav = nav_toml(INVENTORY, read_issues(SRC))
    assert nav.startswith('nav = [\n  { "Home" = "index.md" },\n  { "Project status" = "status/index.md" },\n'
                          '  { "Full index" = "full-index/index.md" },\n  { "Volumes" = [')
    assert '{ "Volume 25, 2011–2012" = "25/index.md" }' in nav
    assert nav.index('"Volume 1') < nav.index('"Volume 24') < nav.index('"Volume 25')


def test_full_index_tables_every_article_in_printed_order(tmp_path):
    from vecrescue.pages import _badge, tab_id
    docs, _ = pages(tmp_path)
    (docs / "art3" / "index.md").write_text("---\nstatus: transcribed\nreview: draft\nwarning: unsure\n---\n\nText")
    text = write_index_page(INVENTORY, read_issues(SRC), docs).read_text(encoding="utf-8")
    assert "# Full index" not in text            # the page title is the heading
    assert "| volume | issue | page | quality | article | author |" in text
    assert (f"Quality of the text: {_badge('missing')} 2 · {_badge('OCR')} 0 · {_badge('PDF')} 0 · "
            f"{_badge('failed')} 0 · {_badge('draft')} 1 · {_badge('reviewed')} 0 · {_badge('text')} 2 (of 5)") in text
    by = {(i["volume"], i["issue"]): i for i in read_issues(SRC)}
    t24, t25 = f"(../24/#{tab_id(by[('24', '2')])})", f"(../25/#{tab_id(by[('25', '1')])})"
    rows = [l for l in text.splitlines() if l.startswith("| ") and "---" not in l][1:]
    assert rows == [
        f"| [24](../24/) | [2&3]{t24} | 5 | {_badge('missing')} | In the combined issue |  |",
        f"| [25](../25/) | [1]{t25} | 9 | {_badge('text')} | [First \\*thing\\*](../art1/) | A. A, C. C |",
        f"| [25](../25/) | [1]{t25} | 30 | {_badge('missing')} | Not online |  |",
        f"| [25](../25/) | [1]{t25} | 74 | {_badge('draft')} | [Second \\| piece](../art3/) <span class=\"doubtful\" "
        f"title=\"The transcription is doubtful or missing; its page says why\">⚠</span> | B. B |",
        f"|  |  |  | {_badge('text')} | [Online only](../art5/) | D. D |",
    ]


@pytest.mark.parametrize("page, expected", [
    (None, ("missing", False)),
    ("Converted text", ("text", False)),
    ("---\ntitle: T\n---\n\nConverted text", ("text", False)),
    ("---\nstatus: not online\n---\n\n[Read it in the PDF](../1/1/x.pdf#page=3)", ("PDF", False)),
    ("---\nstatus: not online\nwarning: XPL\n---\n\n[Read it in the PDF](../1/1/x.pdf#page=3)", ("failed", False)),
    ("---\nstatus: transcribed\nreview: draft\n---\n\nText", ("draft", False)),
    ("---\nstatus: transcribed\nreview: reviewed\n---\n\nText", ("reviewed", False)),
    ("---\nstatus: transcribed\nreview: reviewed\nwarning: unsure\n---\n\nText", ("reviewed", True)),
])
def test_quality_of_an_articles_text(tmp_path, page, expected):
    from vecrescue.pages import quality
    if page is not None:
        (tmp_path / "art7").mkdir()
        (tmp_path / "art7" / "index.md").write_text(page)
    assert quality(tmp_path, "7") == expected


def test_quality_of_text_from_a_damaged_copy(tmp_path):
    from vecrescue.pages import quality
    from vecrescue.stubs import write_stub
    write_stub({"id": "7", "title": "T"}, tmp_path, ocr="<details>…</details>", note=DAMAGED)
    assert quality(tmp_path, "7") == ("OCR", False)


CONTENTS = {("25", "1"): {"volume": "25", "issue": "1", "items": [
    {"title": "EDITORIAL: A view", "author": "E. Ditor", "page": 3},
    {"section": "RECENT MEETINGS", "page": 7, "file": "unindexed/v25n1-p7-meetings.md"},
    {"title": "A meeting", "author": "A. A", "page": 9, "vid": ["1", "2"]},
    {"title": "Second piece", "page": 74, "vid": "3"},
]}}


def test_issue_table_follows_the_contents_page(tmp_path):
    from vecrescue.pages import issue_rows
    docs, _ = pages(tmp_path)
    (docs / "v25n1-p7-meetings").mkdir()
    (docs / "v25n1-p7-meetings" / "index.md").write_text("---\nstatus: transcribed\nreview: draft\n---\n\nText")
    rows = issue_rows(docs, CONTENTS[("25", "1")], INVENTORY[:3], ("25/1/v251.pdf", 2))
    assert [(r.get("section", False), r["indent"], r["title"], r["href"], r["q"]) for r in rows] == [
        (False, 0, "EDITORIAL: A view", "25/1/v251.pdf#page=5", "PDF"),      # front section: its PDF page
        (True, 0, "RECENT MEETINGS", "v25n1-p7-meetings/", None),           # section: its introduction
        (False, 0, "A meeting", "25/1/v251.pdf#page=11", "PDF"),            # a line holding two index records
        (False, 1, "First *thing*", "art1/", "text"),
        (False, 1, "Not online", None, "missing"),
        (False, 0, "Second piece", "art3/", "text"),                         # Contents title, index record’s page
    ]


def test_issue_table_without_a_scan_links_nothing_to_a_pdf(tmp_path):
    from vecrescue.pages import issue_rows
    docs, _ = pages(tmp_path)
    rows = issue_rows(docs, CONTENTS[("25", "1")], INVENTORY[:3], None)
    assert rows[0]["href"] is None and rows[0]["q"] == "missing"


def test_volume_page_and_full_index_use_the_contents(tmp_path):
    docs, _ = pages(tmp_path)
    write_volume_pages(INVENTORY, read_issues(SRC), SRC, docs, contents=CONTENTS, pdf_links={("25", "1"): ("25/1/v251.pdf", 2)})
    text = tab((docs / "25" / "index.md").read_text(encoding="utf-8"), "N°1,")
    assert "| 3 | [EDITORIAL: A view](../25/1/v251.pdf#page=5) (PDF) | E. Ditor |" in text
    assert "| 7 | **RECENT MEETINGS** |  |" in text                 # its introduction is not published here
    assert "| 9 | &emsp;[First \\*thing\\*](../art1/) | A. A, C. C |" in text
    full = write_index_page(INVENTORY, read_issues(SRC), docs, CONTENTS, {("25", "1"): ("25/1/v251.pdf", 2)}).read_text()
    assert "[EDITORIAL: A view](../25/1/v251.pdf#page=5) (PDF)" in full and "RECENT MEETINGS" not in full


def test_unindexed_pieces_are_published(tmp_path):
    from vecrescue.pages import publish_unindexed, quality
    t = tmp_path / "transcriptions" / "unindexed"
    t.mkdir(parents=True)
    (t / "v25n1-p7-meetings.md").write_text("---\ntitle: Meetings\nvolume: '25'\nissue: '1'\npage: '7'\n"
                                           "unindexed: true\nreview: draft\n---\n\nSome text.\n\n![F](v25n1-p7-meetings/f.png)\n")
    (t / "v25n1-p7-meetings").mkdir()
    (t / "v25n1-p7-meetings" / "f.png").write_bytes(b"png")
    docs = tmp_path / "docs"
    [page] = publish_unindexed(tmp_path / "transcriptions", docs, {("25", "1"): ("25/1/v251.pdf", 2)})
    text = page.read_text()
    assert page == docs / "v25n1-p7-meetings" / "index.md"
    assert "Some text." in text and "](f.png)" in text and (docs / "v25n1-p7-meetings" / "f.png").exists()
    assert "](../25/1/v251.pdf#page=9)" in text
    assert quality(docs, name="v25n1-p7-meetings") == ("draft", False)


def test_contents_files_parse_and_link_existing_records():
    import json
    from vecrescue.pages import _as_list, read_contents
    contents = read_contents(Path(__file__).parents[1] / "transcriptions" / "contents")
    assert ("4", "4") in contents
    for key, doc in contents.items():
        for item in doc["items"]:
            assert ("section" in item) != ("title" in item), (key, item)
            for f in _as_list(item.get("file")):
                assert (Path(__file__).parents[1] / "transcriptions" / f).is_file(), (key, f)
