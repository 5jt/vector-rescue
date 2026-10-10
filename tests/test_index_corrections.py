"""Issue #211: index records corrected from the Contents pages and corrections.yaml."""

import json

import pytest

from vecrescue.corrections import CorrectionError, Corrections
from vecrescue.inventory import correct_from_contents
from vecrescue.report import index_corrections_md


def rec(vid, vol, no, page, title="T", authors=("A",)):
    return {"id": vid, "title": title, "authors": list(authors), "volume": vol, "issue": no, "page": page}


def contents(vol, no, *items):
    return {(vol, no): {"volume": vol, "issue": no, "items": list(items)}}


def test_a_line_with_one_record_gives_it_its_page_and_issue():
    records = [rec("1", "5", "3", "61"), rec("2", "5", "2", "70")]
    log = correct_from_contents(records, contents("5", "2",
        {"title": "Short", "author": "Someone Else", "page": 60, "vid": "1"},
        {"title": "Same", "page": 70, "vid": "2"}))
    assert records[0] == rec("1", "5", "2", "60")  # title and author untouched
    assert records[1] == rec("2", "5", "2", "70")
    assert log == [{"id": "1", "field": "issue", "old": "3", "new": "2", "by": "Contents v5n2"},
                   {"id": "1", "field": "page", "old": "61", "new": "60", "by": "Contents v5n2"}]


def test_a_p999_twin_takes_the_line_but_other_records_on_it_do_not():
    records = [rec("1", "20", "2", "136"), rec("2", "21", "1", "999"),
               rec("3", "23", "4", "17"), rec("4", "23", "4", "19")]
    c = {**contents("20", "2", {"title": "R.net", "page": 136, "vid": ["1", "2"]}),
         **contents("23", "4", {"title": "Industry news", "page": 17, "vid": ["3", "4"]})}
    log = correct_from_contents(records, c)
    assert records[1] == rec("2", "20", "2", "136")
    assert records[3]["page"] == "19"
    assert [(e["id"], e["field"]) for e in log] == [("2", "volume"), ("2", "issue"), ("2", "page")]


def test_lines_that_correct_nothing():
    records = [rec("1", "7", "3", "123"), rec("2", "11", "4", "12"), rec("3", "16", "4", "95"),
               rec("4", "10", "2", "999")]
    log = correct_from_contents(records, {
        **contents("7", "3", {"title": "Held over", "vid": "1"}),  # no page
        **contents("11", "4", {"title": "Letter", "page": 7, "vid": "2",
                               "note": "not on the Contents page; within Correspondence"}),
        **contents("16", "4", {"title": "Hacker", "page": 95, "vid": "3", "note": "95 from the index"},
                   {"section": "NEWS", "page": 5}),
        **contents("10", "2", {"title": "Twin", "page": 19, "vid": ["9", "4"]})})  # no twin at p.19
    assert log == []
    assert [r["page"] for r in records] == ["123", "12", "95", "999"]


def test_records_in_corrections_yaml_are_applied_and_logged():
    c = Corrections.from_text("""
records:
  "1":
    title: How to Rig an Election
    authors: [Richard Smith, Adrian Smith]
    page: 127
    why: printed so
    decided: Claude (evidence)
  "9":
    page: 3
    why: gone
    decided: Claude (evidence)
""")
    records = [rec("1", "21", "3", "12", "How to Win an Election", ["Adrian Smith", "Adrian Richard"])]
    log = c.apply_records(records)
    assert records[0] == rec("1", "21", "3", "127", "How to Rig an Election", ["Richard Smith", "Adrian Smith"])
    assert [(e["id"], e["field"]) for e in log] == [("1", "title"), ("1", "authors"), ("1", "page"), ("9", None)]
    assert log[0]["by"] == "corrections.yaml: printed so"


@pytest.mark.parametrize("entry", ["{title: X, decided: me}", "{title: X, why: because}", "{why: because, decided: me}"])
def test_a_record_correction_needs_why_decided_and_a_field(entry):
    with pytest.raises(CorrectionError):
        Corrections.from_text(f'records:\n  "1": {entry}\n')


def test_the_report_lists_every_correction():
    log = [{"id": "1", "field": "page", "old": "61", "new": "60", "by": "Contents v5n1"},
           {"id": "2", "field": "authors", "old": ["A|B"], "new": ["C"], "by": "corrections.yaml: why"}]
    md = "\n".join(index_corrections_md(log))
    assert "## Index records corrected" in md
    assert "2 records of index.xml corrected (authors 1, page 1)" in md
    assert "| art1 | page | 61 | 60 | Contents v5n1 |" in md
    assert "| art2 | authors | A\\|B | C | corrections.yaml: why |" in md
    assert index_corrections_md([]) == []


def test_the_inventory_step_writes_the_log(tmp_path):
    from pathlib import Path
    from vecrescue.pipeline import run_inventory
    src = Path(__file__).parent / "fixtures" / "src"
    first = json.loads(run_inventory(src, tmp_path / "a").read_text())[0]
    folder = tmp_path / "t" / "contents"
    folder.mkdir(parents=True)
    (folder / "v1n1.yaml").write_text(
        f"volume: '{first['volume']}'\nissue: '{first['issue']}'\n"
        f"items:\n- title: X\n  page: 4321\n  vid: '{first['id']}'\n", encoding="utf-8")
    inv = json.loads(run_inventory(src, tmp_path / "b", transcriptions=tmp_path / "t").read_text())
    assert inv[0]["page"] == "4321"
    log = json.loads((tmp_path / "b" / "index-corrections.json").read_text())
    assert log == [{"id": first["id"], "field": "page", "old": first["page"], "new": "4321",
                    "by": f"Contents v{first['volume']}n{first['issue']}"}]
