"""Issue #27: decoding non-UTF-8 trad/ sources."""

import pytest

from vecrescue.legacy import decode, mapped_apl


@pytest.mark.parametrize("data, text, how", [
    ("café ’q’".encode("utf-8"), "café ’q’", "utf-8"),
    (b"don\x92t \x93say\x94 \x96 caf\xe9", "don’t “say” – café", "cp1252"),
    ("← x".encode("utf-8") + b" don\x92t", "← x don’t", "mixed"),
])
def test_decode(data, text, how):
    assert decode(data) == (text, how)


def test_bytes_undefined_in_cp1252_are_kept_visible():
    text, how = decode(b"a\x8db")
    assert text == "a�b" and how == "cp1252"


def test_bytes_undefined_in_cp1252_mean_mapped_apl():
    assert mapped_apl("a�b", "trad/x.htm", set()) == "undefined-bytes"


@pytest.mark.parametrize("html, reason", [
    ("<p>execute (with ŒioÉ1) the line</p>", "mapped-apl-suspect"),   # ⎕io←1
    ("<p>assign VÉV+1</p>", "mapped-apl-suspect"),                      # V←V+1
    ("<pre>Z←-ëRECT N</pre>", "mapped-apl-suspect"),               # letter in code
    ("<pre>+¨ ¯1 2×3÷4</pre>", None),                   # ¨ ¯ × ÷ are APL
    ("<p>Gérard Langlet and Dürer</p>", None),                      # accents in prose
    ("<p>£ price; ½ off</p>", None),
])
def test_mapped_apl_suspects(html, reason):
    assert mapped_apl(html, "trad/x.htm", set()) == reason


def test_suspect_heuristic_applies_only_to_pre_unicode_files():
    html = "<pre>RÉC ← 'café'</pre>"     # French identifiers in Unicode APL
    assert mapped_apl(html, "trad/x.htm", set(), unicode=True) is None
    assert mapped_apl(html, "trad/x.htm", set()) == "mapped-apl-suspect"
