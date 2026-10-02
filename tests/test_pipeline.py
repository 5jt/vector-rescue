import json
from pathlib import Path

from vecrescue.pipeline import run_convert, run_inventory

SRC = Path(__file__).parent / "fixtures" / "src"


def test_inventory_then_convert(tmp_path):
    inv = run_inventory(SRC, tmp_path)
    assert json.loads(inv.read_text())[0]["id"] == "10500650"
    written = run_convert(SRC, tmp_path)
    # only XHTML sources that exist and have an ID are converted
    assert [p.name for p in written] == ["art10500650.md"]
    assert (tmp_path / "docs" / "art10500650.md").exists()


def test_convert_writes_notes_per_article(tmp_path):
    run_inventory(SRC, tmp_path)
    run_convert(SRC, tmp_path)
    notes = json.loads((tmp_path / "notes.json").read_text())
    assert notes["10500650"] == [{"kind": "raw-html", "tag": "blink"}]
