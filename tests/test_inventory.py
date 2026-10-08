from pathlib import Path

from vecrescue.inventory import read_index

SRC = Path(__file__).parent / "fixtures" / "src"


def records():
    return {r["title"]: r for r in read_index(SRC)}


def test_reads_every_description():
    assert len(read_index(SRC)) == 7


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


INDEX = """<?xml version="1.0"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/"
         xmlns:vec="http://www.vector.org.uk/archive-schema">
<rdf:Description><dc:identifier>1</dc:identifier><dc:title>Old</dc:title>
  <vec:source fmt="XHTML">content/a/a.htm</vec:source></rdf:Description>
<rdf:Description><dc:identifier>2</dc:identifier><dc:title>New</dc:title>
  <vec:source fmt="XHTML">content/b/b.htm</vec:source></rdf:Description>
</rdf:RDF>"""


def test_restored_index_takes_its_own_sources_first(tmp_path):
    """#113: an index from the restored site; sources from its copy, else the tree."""
    from vecrescue.inventory import php_renderings
    src, php = tmp_path / "sjt/Vector", tmp_path / "php-site"
    (src / "content/a").mkdir(parents=True)
    (src / "content/a/a.htm").write_text("<p/>")
    (php / "content/b").mkdir(parents=True)
    (php / "content/b/b.htm").write_text("<p/>")
    (php / "index.xml").write_text(INDEX)
    (php / "rendered").mkdir()
    (php / "rendered/art2.html").write_text("<html/>")
    recs = {r["id"]: r for r in read_index(php, src)}
    assert recs["1"]["sources"][0] == {"fmt": "XHTML", "path": "content/a/a.htm", "exists": True, "utf8": True}
    assert recs["2"]["sources"][0]["path"] == "../../php-site/content/b/b.htm"
    assert (src / recs["2"]["sources"][0]["path"]).is_file()
    recs = {r["id"]: r for r in php_renderings(list(recs.values()), php, src)}
    assert recs["2"]["captured"] == "../../php-site/rendered/art2.html"
    assert "captured" not in recs["1"]
