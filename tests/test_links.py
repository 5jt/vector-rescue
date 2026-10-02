"""Issue #8: links to the old site."""

import lxml.html
import pytest

from vecrescue.links import LinkIndex, localise_links

INDEX = LinkIndex(
    pages={"10500090", "10500650"},
    ids={"10500090", "10500650", "10009840", "10003610"},
    by_source={"trad/v234/jot50.htm": "10009840", "trad/v151/bob151_97.htm": "10003610",
               "trad/v151/bob.htm": "10003610"},
)


@pytest.fixture
def root(tmp_path):
    (tmp_path / "content/printed/251/sykes").mkdir(parents=True)
    (tmp_path / "content/printed/251/sykes/oostats.zip").write_bytes(b"z")
    (tmp_path / "resource").mkdir()
    (tmp_path / "resource/apl385.ttf").write_bytes(b"f")
    (tmp_path / "trad/v234b").mkdir(parents=True)
    (tmp_path / "trad/v234b/d25.pdf").write_bytes(b"p")
    return tmp_path


def run(root, href):
    doc = lxml.html.fromstring(f'<html><body><a href="{href}">x</a></body></html>')
    notes = []
    assets = localise_links(doc, root, "content/printed/251/sykes/sykes.htm", INDEX, notes)
    return next(doc.iter("a")).get("href"), assets, notes


@pytest.mark.parametrize("href, out", [
    ("http://archive.vector.org.uk/art10500090", "../art10500090/"),
    ("http://www.vector.org.uk/art10500090", "../art10500090/"),
    ("http://vector.org.uk/art10500090#ref2", "../art10500090/#ref2"),
    ("https://vector.johnbutlerassociates.co.uk/art10500090", "../art10500090/"),
    ("/art10500650", "../art10500650/"),
    ("http://www.vector.org.uk/archive/v234/jot50.htm", "../art10009840/"),
    ("archive/v234/jot50.htm", "../art10009840/"),
    ("http://www.vector.org.uk/?vol=15&amp;no=1&amp;art=bob", "../art10003610/"),
    ("http:/vector.org.uk/?vol=23&amp;no=4&amp;art=jot50", "../art10009840/"),
    ("?vol=23&amp;no=4&amp;art=jot50", "../art10009840/"),
    ("http://archive.vector.org.uk/24/1", "../24/1/"),
])
def test_old_site_links_are_rewritten(root, href, out):
    assert run(root, href)[0] == out


def test_link_to_an_article_not_converted_yet_is_noted(root):
    _, _, notes = run(root, "http://archive.vector.org.uk/art10009840")
    assert notes == [{"kind": "link-to-unconverted", "id": "10009840"}]


def test_link_to_an_issue_page_is_noted(root):
    _, _, notes = run(root, "/24/1")
    assert notes == [{"kind": "link-to-issue", "volume": "24", "issue": "1"}]


@pytest.mark.parametrize("href, out, asset", [
    ("oostats.zip", "oostats.zip", "content/printed/251/sykes/oostats.zip"),
    ("../../../../resource/apl385.ttf", "resource/apl385.ttf", "resource/apl385.ttf"),
    ("http://www.vector.org.uk/archive/v234b/d25.pdf", "trad/v234b/d25.pdf", "trad/v234b/d25.pdf"),
])
def test_linked_files_are_copied(root, href, out, asset):
    new, assets, notes = run(root, href)
    assert new == out
    assert assets == {out: root / asset}
    assert notes == []


@pytest.mark.parametrize("href", ["?area=about", "ref4", "http://archive.vector.org.uk/art99999999"])
def test_unresolvable_links_are_left_and_noted(root, href):
    new, _, notes = run(root, href.replace("&", "&amp;"))
    assert new == href
    assert notes == [{"kind": "link-unresolved", "href": href}]


@pytest.mark.parametrize("href", ["http://elsewhere.org/x", "#ref1", "mailto:a@b.c", "ftp://x.org/f"])
def test_other_links_are_left_alone(root, href):
    assert run(root, href)[:3:2] == (href, [])


# repairs ---------------------------------------------------------------------

REPAIR_INDEX = LinkIndex(
    pages={"10500200", "10500320", "10500390"},
    ids={"10500200", "10500320", "10500390"},
    by_source={},
    articles=[("10500200", "24", "2", "hui"), ("10500390", "24", "4", "hui"),
              ("10500320", "24", "2", "holmesfc3")],
)


@pytest.mark.parametrize("href, out", [
    ("?vol=24&amp;no=3&amp;art=hui", "../art10500200/"),       # 24:3 was printed with 24:2
    ("http:/vector.org.uk/?vol=24&amp;no=2&amp;art=holmes", "../art10500320/"),
])
def test_query_links_fall_back_to_the_printed_article(root, href, out):
    doc = lxml.html.fromstring(f'<html><body><a href="{href}">x</a></body></html>')
    notes = []
    localise_links(doc, root, "content/printed/244/x.htm", REPAIR_INDEX, notes)
    assert next(doc.iter("a")).get("href") == out
    assert notes[0]["kind"] == "link-repaired"


def test_query_link_with_several_candidates_is_not_guessed(root):
    doc = lxml.html.fromstring('<html><body><a href="?vol=24&amp;no=4&amp;art=h">x</a></body></html>')
    idx = LinkIndex(pages={"1", "2"}, ids={"1", "2"},
                    articles=[("1", "24", "4", "hui"), ("2", "24", "4", "holmes")])
    notes = []
    localise_links(doc, root, "content/printed/244/x.htm", idx, notes)
    assert notes == [{"kind": "link-unresolved", "href": "?vol=24&no=4&art=h"}]


def test_missing_file_found_in_the_article_folder(root):
    (root / "content/printed/251/sykes/fig01.png").write_bytes(b"i")
    new, assets, notes = run(root, "reiter/fig01.png")
    assert new == "fig01.png"
    assert assets == {"fig01.png": root / "content/printed/251/sykes/fig01.png"}
    assert notes == [{"kind": "link-repaired", "href": "reiter/fig01.png", "to": "fig01.png"}]


def test_missing_file_found_from_the_tree_root(root):
    new, _, notes = run(root, "../../resource/apl385.ttf")
    assert new == "resource/apl385.ttf"
    assert notes[0]["kind"] == "link-repaired"


@pytest.mark.parametrize("href, out", [
    ("chenriod@vtx.ch", "mailto:chenriod@vtx.ch"),
    ("http://www.vector.org.uk", "../"),
    ("/", "../"),
    ("/21", "../"),
    ("http://www.vector.org.uk/v234/jot50.htm", "../art10009840/"),
])
def test_more_old_site_forms_are_repaired(root, href, out):
    new, _, notes = run(root, href)
    assert new == out
    assert notes[-1]["kind"] == "link-repaired"


def test_percent_encoded_file_names_are_found(root):
    (root / "content/printed/251/sykes/Example of X.htm").write_text("x")
    new, assets, _ = run(root, "Example%20of%20X.htm")
    assert new == "Example%20of%20X.htm"
    assert assets == {"Example of X.htm": root / "content/printed/251/sykes/Example of X.htm"}


def test_downloads_are_found_in_the_old_sites_resource_folder(root):
    (root / "resource/apl2741.zip").write_bytes(b"z")
    new, assets, notes = run(root, "../apl2741.zip")
    assert new == "resource/apl2741.zip"
    assert assets == {"resource/apl2741.zip": root / "resource/apl2741.zip"}
    assert notes[-1]["kind"] == "link-repaired"


@pytest.mark.parametrize("href, out", [
    ("www.milinta.com/english", "http://www.milinta.com/english"),
    ("en.wikipedia.org/wiki/Duck_typing", "http://en.wikipedia.org/wiki/Duck_typing"),
])
def test_web_addresses_without_a_scheme(root, href, out):
    new, _, notes = run(root, href)
    assert new == out and notes[-1]["kind"] == "link-repaired"
