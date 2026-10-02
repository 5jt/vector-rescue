from vecrescue.pipeline import write_home_page


def test_home_page_lists_articles_by_volume_and_issue(tmp_path):
    inv = [
        {"id": "2", "title": "Second", "volume": "25", "issue": "1"},
        {"id": "1", "title": "First", "volume": "24", "issue": "4"},
        {"id": "3", "title": "Online", "volume": None, "issue": None},
    ]
    docs = tmp_path / "docs"
    docs.mkdir()
    for i in ("1", "2", "3"):
        (docs / f"art{i}.md").write_text("x")
    text = write_home_page(inv, docs).read_text(encoding="utf-8")
    assert text.index("24:4") < text.index("25:1") < text.index("Online only")
    assert "[First](art1/)" in text
