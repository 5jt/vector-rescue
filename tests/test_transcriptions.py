"""The committed transcriptions (issue #40): their front matter must parse,
since a broken one stops the site build (or, unindexed, goes unnoticed)."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent / "transcriptions"
FILES = sorted(p for p in ROOT.rglob("*.md") if p.name != "README.md")


@pytest.mark.parametrize("path", FILES, ids=lambda p: str(p.relative_to(ROOT)))
def test_front_matter_parses(path):
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n")
    fm = yaml.safe_load(text.split("---", 2)[1])
    assert fm.get("title") and fm.get("review") in ("draft", "reviewed")
    assert all(isinstance(q, str) for q in fm.get("queries") or [])
