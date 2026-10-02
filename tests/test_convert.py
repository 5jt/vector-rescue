from pathlib import Path

from vecrescue.convert import convert_article
from vecrescue.inventory import read_index

FIX = Path(__file__).parent / "fixtures"
SRC = FIX / "src"


def record(vid):
    return next(r for r in read_index(SRC) if r["id"] == vid)


def test_sample_article_matches_golden_file():
    md = convert_article(SRC, record("10500650"))
    assert md == (FIX / "expected" / "10500650.md").read_text(encoding="utf-8")


def test_unknown_elements_pass_through_as_raw_html():
    md = convert_article(SRC, record("10500650"))
    assert "<blink>Unknown &amp; kept</blink>" in md
