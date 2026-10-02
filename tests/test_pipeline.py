import json
from pathlib import Path

from vecrescue.pipeline import run_convert, run_inventory

SRC = Path(__file__).parent / "fixtures" / "src"


def test_inventory_then_convert(tmp_path):
    inv = run_inventory(SRC, tmp_path)
    assert json.loads(inv.read_text())[0]["id"] == "10500650"
    written = run_convert(SRC, tmp_path)
    # sources that exist, are XHTML or UTF-8 HTML, and have an ID are converted
    assert [str(p.relative_to(tmp_path)) for p in written] == [
        "docs/art10500650/index.md", "docs/art10014170/index.md"]
    assert (tmp_path / "docs" / "art10500650" / "fig1.png").read_bytes().startswith(b"\x89PNG")


def test_convert_writes_notes_per_article(tmp_path):
    run_inventory(SRC, tmp_path)
    run_convert(SRC, tmp_path)
    notes = json.loads((tmp_path / "notes.json").read_text())
    assert notes["10500650"] == [{"kind": "raw-html", "tag": "blink", "reason": "no-rule"}]


def test_convert_starts_from_an_empty_docs_folder(tmp_path):
    run_inventory(SRC, tmp_path)
    stale = tmp_path / "docs" / "art999.md"
    stale.parent.mkdir(parents=True)
    stale.write_text("old")
    run_convert(SRC, tmp_path)
    assert not stale.exists()


def test_legacy_html_article_is_converted(tmp_path):
    run_inventory(SRC, tmp_path)
    run_convert(SRC, tmp_path)
    md = (tmp_path / "docs" / "art10014170" / "index.md").read_text(encoding="utf-8")
    assert "byline: Dyalog Ltd" in md
    assert md.rstrip().endswith("Dyalog released version 10.")
    assert "vector.org.uk" not in md.split("---", 2)[2]
    notes = json.loads((tmp_path / "notes.json").read_text())
    assert {"kind": "breadcrumbs-dropped", "count": 2} in notes["10014170"]
