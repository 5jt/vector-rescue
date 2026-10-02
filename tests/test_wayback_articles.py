"""Issue #25: articles recovered from the Wayback Machine."""

import json
from pathlib import Path

from vecrescue.inventory import article_source, merge_wayback, read_index
from vecrescue.pipeline import run_convert, run_inventory

SRC = Path(__file__).parent / "fixtures" / "src"
WAYBACK = Path(__file__).parent / "fixtures" / "wayback"


def merged():
    return {r["id"]: r for r in merge_wayback(read_index(SRC), WAYBACK, SRC) if r["id"]}


def test_online_only_article_gets_its_issue_from_the_2021_index():
    r = merged()["10501610"]
    assert (r["volume"], r["issue"], r["page"]) == ("26", "4", "40")
    assert r["metadata"] == "index-2021"
    assert [s["fmt"] for s in r["sources"]] == ["XHTML"]   # our own source, no captured page added


def test_new_indexed_article_uses_its_captured_page():
    r = merged()["10501700"]
    assert r["title"] == "Taming statistics" and r["authors"] == ["Stephen Mansour"]
    assert r["in_press"] is True
    assert article_source(r) == ("WAYBACK", "../wayback/archive.vector.org.uk/art10501700.html")


def test_captured_page_with_no_index_record_becomes_a_record():
    r = merged()["10501760"]
    assert r["title"] == "Larger than life automata"
    assert r["authors"] == ["Cliff Reiter"]
    assert r["in_press"] is True and r["volume"] is None
    assert r["metadata"] == "page"


def test_recovered_article_converts(tmp_path):
    run_inventory(SRC, tmp_path, wayback=WAYBACK)
    run_convert(SRC, tmp_path)
    md = (tmp_path / "docs" / "art10501760" / "index.md").read_text(encoding="utf-8")
    assert "title: Larger than life automata" in md
    assert "wayback: https://web.archive.org/web/20201001000000id_/http://archive.vector.org.uk/art10501760" in md
    assert "[the code](https://github.com/x/y)" in md
    assert "[a video](https://www.youtube.com/watch?v=1)" in md
    assert "![Fig 1](content/printed/271/ltl/fig01.png)" in md
    assert (tmp_path / "docs/art10501760/content/printed/271/ltl/fig01.png").exists()
    assert "validator" not in md
