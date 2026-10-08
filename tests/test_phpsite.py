"""Issue #104: fetching from the restored PHP site."""

import json

from vecrescue import phpsite

INDEX = """<vec:index>
<vec:source fmt="xhtml">content/printed/263/old.htm</vec:source>
<vec:source fmt="xhtml">content/printed/264/new.htm</vec:source>
<vec:source fmt="pdf">http://example.com/x.pdf</vec:source>
<vec:source fmt="xhtml">content/printed/264/new.htm</vec:source>
</vec:index>"""

NEW = b'<p><img src="fig1.png"/><a href="other.htm">x</a><img src="../shared/logo.gif"/>' \
      b'<a href="http://example.com/y.png">y</a><img src="/abs.png"/></p>'


def fake_site(pages):
    calls = []

    def get(url):
        calls.append(url)
        rel = url.removeprefix(phpsite.BASE)
        if rel not in pages:
            raise OSError("404")
        return pages[rel]
    return get, calls


def test_missing_sources_skips_held_urls_and_duplicates(tmp_path):
    (tmp_path / "content/printed/263").mkdir(parents=True)
    (tmp_path / "content/printed/263/old.htm").write_text("x")
    assert phpsite.missing_sources(INDEX, tmp_path) == ["content/printed/264/new.htm"]


def test_assets_resolve_relative_files_only():
    assert phpsite.assets(NEW, "content/printed/264/new.htm") == [
        "content/printed/264/fig1.png", "content/printed/shared/logo.gif"]


def test_sources_fetch_what_the_tree_lacks(tmp_path):
    tree = tmp_path / "tree"
    (tree / "content/printed/263").mkdir(parents=True)
    (tree / "content/printed/263/old.htm").write_text("x")
    (tree / "content/printed/shared").mkdir(parents=True)
    (tree / "content/printed/shared/logo.gif").write_text("x")
    get, calls = fake_site({"index.xml": INDEX.encode(), "issues/index.xml": b"<i/>",
                            "content/printed/264/new.htm": NEW,
                            "content/printed/264/fig1.png": b"PNG"})
    f = phpsite.Fetcher(tmp_path / "out", get=get, pause=0)
    assert f.sources(tree) == ["content/printed/264/new.htm"]
    assert (tmp_path / "out/content/printed/264/fig1.png").read_bytes() == b"PNG"
    assert not any("logo.gif" in c for c in calls)
    manifest = json.loads((tmp_path / "out/manifest.json").read_text())
    assert manifest["content/printed/264/new.htm"]["size"] == len(NEW)
    assert f.failed == {}
    # Resumable: a second run fetches only the indexes again
    calls.clear()
    phpsite.Fetcher(tmp_path / "out", get=get, pause=0).sources(tree)
    assert calls == [phpsite.BASE + "index.xml", phpsite.BASE + "issues/index.xml"]


def test_renderings_saved_by_article(tmp_path):
    get, _ = fake_site({"index": b'<a href="art10000010">a</a> <a href="/art10000020">b</a>'
                                 b' <a href="art10000010">again</a>',
                        "art10000010": b"<html>one</html>"})
    f = phpsite.Fetcher(tmp_path, get=get, pause=0)
    assert f.renderings() == ["art10000010", "art10000020"]
    assert (tmp_path / "rendered/art10000010.html").read_bytes() == b"<html>one</html>"
    assert "rendered/art10000020.html" in f.failed
