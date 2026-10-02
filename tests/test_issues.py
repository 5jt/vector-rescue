"""Issue #9: issue pages and the home page."""

from pathlib import Path

from vecrescue.inventory import read_issues
from vecrescue.pages import write_home_page, write_issue_pages

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
    written = write_issue_pages(INVENTORY, read_issues(SRC), SRC, docs)
    return docs, written


def test_issue_page_lists_articles_in_page_order(tmp_path):
    docs, _ = pages(tmp_path)
    text = (docs / "25" / "1" / "index.md").read_text(encoding="utf-8")
    assert "title: Vector 25:1" in text
    assert "June 2011" in text
    rows = [line for line in text.splitlines() if line.startswith("| ") and "---" not in line][1:]
    assert rows == [
        "| 9 | [First \\*thing\\*](../../art1/) | A. A, C. C |",
        "| 30 | Not online |  |",
        "| 74 | [Second \\| piece](../../art3/) | B. B |",
    ]


def test_issue_pdf_is_copied_and_linked(tmp_path):
    docs, _ = pages(tmp_path)
    assert (docs / "25" / "1" / "v251.pdf").read_bytes().startswith(b"%PDF")
    assert "[PDF of the whole issue](v251.pdf)" in (docs / "25" / "1" / "index.md").read_text()


def test_combined_issue_has_a_page_at_both_numbers(tmp_path):
    docs, _ = pages(tmp_path)
    main = (docs / "24" / "2" / "index.md").read_text(encoding="utf-8")
    assert "title: Vector 24:2&3" in main
    assert "In the combined issue" in main          # catalogued as 24:3
    alias = (docs / "24" / "3" / "index.md").read_text(encoding="utf-8")
    assert "[Vector 24:2&3](../2/)" in alias


def test_issue_with_no_articles_still_has_a_page(tmp_path):
    docs, _ = pages(tmp_path)
    assert "No articles are indexed" in (docs / "1" / "1" / "index.md").read_text()


def test_home_page_lists_volumes_issues_and_online_only(tmp_path):
    docs, _ = pages(tmp_path)
    text = write_home_page(INVENTORY, read_issues(SRC), docs).read_text(encoding="utf-8")
    assert text.index("Volume 1") < text.index("Volume 24") < text.index("Volume 25")
    assert "[2&3](24/2/)" in text and "[1](25/1/)" in text
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


def test_an_alias_never_replaces_a_real_issue_page(tmp_path):
    docs, _ = pages(tmp_path)
    assert "title: Vector 25:4" in (docs / "25" / "4" / "index.md").read_text()
    assert "Printed with" not in (docs / "25" / "4" / "index.md").read_text()
    assert "title: Vector 25:2&3" in (docs / "25" / "3" / "index.md").read_text()
    assert "[Vector 25:2&3](../3/)" in (docs / "25" / "2" / "index.md").read_text()


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
    write_issue_pages(INVENTORY, read_issues(SRC), SRC, docs, wayback_issue_pdfs(tmp_path / "wayback"))
    assert (docs / "1/1/VOL.1-NO.1-MAY-1984.pdf").read_bytes() == b"%PDF 1984\n%%EOF"
    assert "[PDF of the whole issue](VOL.1-NO.1-MAY-1984.pdf)" in (docs / "1/1/index.md").read_text()
    assert (docs / "25/1/v251.pdf").read_bytes().startswith(b"%PDF-1.4 fixture")   # ours preferred


def test_truncated_wayback_pdfs_are_not_used(tmp_path):
    d = tmp_path / "vector.org.uk/wp-content/uploads/2022/07"
    d.mkdir(parents=True)
    (d / "VOL.3-NO.4-APRIL-1987.pdf").write_bytes(b"%PDF-1.3\n" + b"0" * 100)        # no %%EOF
    (d / "VOL.3-NO.3-JANUARY-1987.pdf").write_bytes(b"%PDF-1.3\n...\n%%EOF\n")
    assert list(wayback_issue_pdfs(tmp_path)) == [("3", "3")]
