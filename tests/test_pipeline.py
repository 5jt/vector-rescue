import json
from pathlib import Path

from vecrescue.pipeline import run_convert, run_inventory

SRC = Path(__file__).parent / "fixtures" / "src"


def test_inventory_then_convert(tmp_path):
    inv = run_inventory(SRC, tmp_path)
    assert json.loads(inv.read_text())[0]["id"] == "10500650"
    written = run_convert(SRC, tmp_path)
    # only XHTML sources that exist and have an ID are converted
    assert [str(p.relative_to(tmp_path)) for p in written] == ["docs/art10500650/index.md"]
    assert (tmp_path / "docs" / "art10500650" / "fig1.png").read_bytes().startswith(b"\x89PNG")


def test_convert_writes_notes_per_article(tmp_path):
    run_inventory(SRC, tmp_path)
    run_convert(SRC, tmp_path)
    notes = json.loads((tmp_path / "notes.json").read_text())
    assert notes["10500650"] == [{"kind": "raw-html", "tag": "blink"}]


def test_convert_starts_from_an_empty_docs_folder(tmp_path):
    run_inventory(SRC, tmp_path)
    stale = tmp_path / "docs" / "art999.md"
    stale.parent.mkdir(parents=True)
    stale.write_text("old")
    run_convert(SRC, tmp_path)
    assert not stale.exists()
