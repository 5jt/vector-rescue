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
    issues = read_issues(SRC)
    assert issues[0] == {"volume": "25", "issue": "1", "year": "2011", "month": "06",
                         "title": None, "span": 1, "pdf": "v251.pdf", "doc": None}
    assert issues[1]["span"] == 2 and issues[1]["title"] == "Nos.2&3"
    assert issues[2]["pdf"] is None


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
