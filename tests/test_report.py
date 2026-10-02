"""Issue #10: the run report."""

import json

import lxml.html

from vecrescue.report import code_check, text_check, run_report, render_markdown

SOURCE = """<html><body>
<ul id="publication"><li>Draft</li></ul>
<h1 class="prefix">Series</h1>
<h1 id="title">Page title</h1>
<h1 id="author">by A. Author</h1>
<p>One<br/>two <em>three</em>.</p>
<table><tr><td>Cell</td><td>Next</td></tr></table>
<pre>
  x←⍳10
\ty</pre>
<p id="validation"><a href="v">&#160;</a></p>
</body></html>"""

RENDERED = """<html><body><article>
<h1 id="__skip">Index title<a class="headerlink" href="#x">¶</a></h1>
<p class="byline">by A. Author</p>
<p>One<br>two <em>three</em>.</p>
<table><tr><td>Cell</td>\n<td>Next</td></tr></table>
<div class="highlight"><pre><span></span><code><span><a id="l1"></a>  x←⍳10
</span><span><a id="l2"></a>        y
</span></code></pre></div>
</article></body></html>"""

RECORD = {"id": "1", "title": "Index title", "authors": [], "volume": None,
          "issue": None, "page": None, "received": None, "online": None}


def doc(html):
    return lxml.html.fromstring(html)


def test_text_check_ignores_title_prefix_furniture_breaks_and_cells():
    r = text_check(doc(SOURCE), doc(RENDERED), RECORD)
    assert r["differing"] == 0
    assert r["source_words"] == r["rendered_words"] == 10


def test_text_check_reports_lost_and_added_words():
    rendered = RENDERED.replace("two <em>three</em>", "two <em>four</em> extra")
    r = text_check(doc(SOURCE), doc(rendered), RECORD)
    assert r["differing"] == 2
    assert r["samples"] == [{"source": "three.", "rendered": "four extra."}]


def test_code_check_matches_after_normalisation():
    r = code_check(doc(SOURCE), doc(RENDERED))
    assert r == {"source_blocks": 1, "rendered_blocks": 1, "mismatched": 0, "samples": []}


def test_code_check_reports_a_changed_block():
    r = code_check(doc(SOURCE), doc(RENDERED.replace("x←⍳10", "x←⍳11")))
    assert r["mismatched"] == 1
    assert r["samples"][0]["source"].startswith("  x←⍳10")


def _setup(tmp_path, notes):
    src = tmp_path / "src"
    (src / "a").mkdir(parents=True)
    (src / "a" / "x.htm").write_text(SOURCE, encoding="utf-8")
    out = tmp_path / "build"
    (out / "site" / "art1").mkdir(parents=True)
    (out / "site" / "art1" / "index.html").write_text(RENDERED, encoding="utf-8")
    rec = dict(RECORD, sources=[{"fmt": "XHTML", "path": "a/x.htm", "exists": True, "utf8": True}])
    (out / "inventory.json").write_text(json.dumps([rec]))
    (out / "notes.json").write_text(json.dumps({"1": notes}))
    return src, out


def test_run_report_totals_and_previous_run(tmp_path):
    src, out = _setup(tmp_path, [{"kind": "raw-html", "tag": "ol"},
                                 {"kind": "table-raw", "reason": "caption"}])
    first = run_report(src, out)
    assert first["totals"]["articles"] == 1
    assert first["totals"]["raw_html"] == {"ol": 1}
    assert first["totals"]["table_raw"] == {"caption": 1}
    assert first["totals"]["text_differing_words"] == 0
    assert first["totals"]["code_mismatched"] == 0
    (out / "notes.json").write_text(json.dumps({"1": []}))
    second = run_report(src, out)
    assert second["previous"]["raw_html"] == {"ol": 1}
    assert (out / "report.prev.json").exists()
    assert "raw HTML" in (out / "report.md").read_text()


def test_markdown_report_shows_deltas():
    md = render_markdown({
        "totals": {"articles": 2, "raw_html": {"p": 3}, "table_raw": {}, "notes": {"x": 1},
                   "text_differing_words": 5, "code_mismatched": 0},
        "previous": {"articles": 2, "raw_html": {"p": 5}, "table_raw": {}, "notes": {},
                     "text_differing_words": 9, "code_mismatched": 0},
        "articles": {}})
    assert "| p | 3 | −2 |" in md
    assert "| Differing words | 5 | −4 |" in md


def test_image_check(tmp_path):
    from vecrescue.report import image_check
    (tmp_path / "a.png").write_bytes(b"x")
    rendered = doc('<html><body><article><img src="a.png"/><img src="gone.png"/>'
                   '<img src="http://x.org/y.png"/></article></body></html>')
    source = doc('<html><body><img src="a.png"/><img src="gone.png"/>'
                 '<img src="http://x.org/y.png"/><img src="dropped.png"/></body></html>')
    r = image_check(source, rendered, tmp_path)
    assert r == {"source_images": 4, "rendered_images": 3, "external": 1, "broken": ["gone.png"]}


def test_anchor_check_lists_in_page_links_with_no_target():
    from vecrescue.report import anchor_check
    rendered = doc('<html><body><article><a id="ref1"></a><h2 id="intro">I</h2>'
                   '<a href="#ref1">1</a><a href="#ref2">2</a><a href="#intro">i</a>'
                   '<a name="old"></a><a href="#old">o</a><a href="#">top</a></article></body></html>')
    assert anchor_check(rendered) == {"links": 4, "missing": ["#ref2"]}


def test_link_check(tmp_path):
    from vecrescue.report import link_check
    site = tmp_path / "site"
    (site / "art1").mkdir(parents=True)
    (site / "art2").mkdir()
    (site / "art2" / "index.html").write_text("x")
    (site / "art1" / "f.zip").write_bytes(b"z")
    rendered = doc('<html><body><article><a href="../art2/">ok</a><a href="../art2/#r">ok</a>'
                   '<a href="../art3/">no</a><a href="f.zip">ok</a><a href="../24/1/">no</a>'
                   '<a href="http://x.org">ext</a><a href="#r">in-page</a></article></body></html>')
    assert link_check(rendered, site / "art1", site) == {
        "links": 5, "broken": ["../art3/", "../24/1/"]}


def test_text_check_ignores_the_article_header_from_the_template():
    rendered = RENDERED.replace('<h1 id="__skip">', '<p class="prefix">Series</p><h1 id="__skip">').replace(
        '<p class="byline">', '<p class="printed"><a href="../25/1/">Vector 25:1</a>, page 74</p><p class="byline">')
    assert text_check(doc(SOURCE), doc(rendered), RECORD)["differing"] == 0


def test_block_boundaries_separate_words():
    from vecrescue.report import _words
    assert _words(doc("<div><p>one.</p><p>Two</p><li>three</li><h2>Four</h2></div>")) == \
        ["one.", "Two", "three", "Four"]


def test_image_check_ignores_the_dropped_validator_badge(tmp_path):
    from vecrescue.report import image_check
    (tmp_path / "a.png").write_bytes(b"x")
    source = doc('<html><body><img src="a.png"/><p id="validation"><a href="v">'
                 '<img src="http://www.w3.org/Icons/valid-html401"/></a></p></body></html>')
    rendered = doc('<html><body><article><img src="a.png"/></article></body></html>')
    assert image_check(source, rendered, tmp_path)["source_images"] == 1


def test_capture_check_compares_with_the_old_sites_rendering():
    from vecrescue.report import capture_check
    captured = doc('<html><body><div id="article"><h1>T</h1><p>It’s here – now.</p></div></body></html>')
    ours = doc('<html><body><article><h1>T</h1><p>It’s here – now.</p></article></body></html>')
    assert capture_check(captured, ours)["differing"] == 0
    ours = doc('<html><body><article><h1>T</h1><p>Itâ€™s here now.</p></article></body></html>')
    r = capture_check(captured, ours)
    assert r["differing"] == 2


def test_stub_pages_are_counted_not_checked(tmp_path):
    src, out = _setup(tmp_path, [])
    (out / "stubs.json").write_text(json.dumps({
        "1": {"pdf": "1/1/a.pdf#page=3", "match": "page"},
        "2": {"pdf": "1/1/a.pdf#page=9", "match": "not found"},
        "3": {"pdf": None, "match": None}}))
    r = run_report(src, out)
    assert r["totals"]["articles"] == 0                       # art1 is a stub, not checked
    assert r["totals"]["stubs"] == {"pages": 3, "with_pdf": 2, "title_not_found": 1}
    assert "## Pages without text" in (out / "report.md").read_text()
