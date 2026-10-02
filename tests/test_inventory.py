from pathlib import Path

from vecrescue.inventory import read_index

SRC = Path(__file__).parent / "fixtures" / "src"


def records():
    return {r["title"]: r for r in read_index(SRC)}


def test_reads_every_description():
    assert len(read_index(SRC)) == 6


def test_identifier_and_publication():
    r = records()["Tables with calculated columns"]
    assert r["id"] == "10500650"
    assert (r["volume"], r["issue"], r["page"]) == ("25", "1", "74")
    assert r["received"] == "2011-02-05"
    assert r["online"] == "2011-05-07"
    assert r["authors"] == ["Stevan Apter"]


def test_sources_with_format_and_existence():
    r = records()["Tables with calculated columns"]
    assert r["sources"] == [
        {"fmt": "XHTML", "path": "content/printed/251/sample.htm",
         "exists": True, "utf8": True}
    ]
    legacy = records()["News from Sustaining Members"]["sources"][0]
    assert legacy["exists"] is True and legacy["utf8"] is True


def test_corporate_creator():
    assert records()["News from Sustaining Members"]["authors"] == ["Dyalog Ltd"]


def test_metadata_only_and_empty_id():
    assert records()["Metadata only"]["sources"] == []
    assert records()["No identifier"]["id"] is None


def test_online_only_has_no_issue():
    r = records()["Online only"]
    assert r["volume"] is None and r["online"] == "2016-01-22"


def test_article_source_prefers_xhtml_then_utf8_html():
    from vecrescue.inventory import article_source
    rec = {"sources": [{"fmt": "HTML", "path": "a.htm", "exists": True, "utf8": True},
                       {"fmt": "XHTML", "path": "b.htm", "exists": True, "utf8": True}]}
    assert article_source(rec) == ("XHTML", "b.htm")
    rec["sources"][1]["exists"] = False
    assert article_source(rec) == ("HTML", "a.htm")
    rec["sources"][0]["utf8"] = False      # decoded as Windows-1252 (#27)
    assert article_source(rec) == ("HTML", "a.htm")
    rec["sources"][0]["exists"] = False
    assert article_source(rec) is None
