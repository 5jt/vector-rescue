"""Issue #23: curated corrections for source defects."""

import pytest

from vecrescue.corrections import Corrections, CorrectionError

YAML = """
articles:
  "10500140":
    - find: '<a name="ref1"> </a>Second'
      replace: '<a name="ref2"> </a>Second'
      why: ref1 defined twice; the second is ref2
      decided: Stephen Taylor
  "10003000":
    - encoding: cp850
      why: DOS code page
      decided: Stephen Taylor
  "10011350":
    - release: true
      why: ø is a Danish name in a string, not mapped APL
      decided: Stephen Taylor
  "10000001":
    - hold: true
      why: garbled beyond repair
      decided: Stephen Taylor
catalogue:
  "26:2":
    title: Nos.2&3
    why: v262.pdf is headed Vol.26 No.2&3
    decided: Stephen Taylor
  "26:4":
    year: "2016"
    month: "03"
    why: date of the issue
    decided: Stephen Taylor
"""


@pytest.fixture
def c():
    return Corrections.from_text(YAML)


def test_text_correction_is_applied_and_noted(c):
    notes = []
    out = c.apply_text("10500140", '<a name="ref1"> </a>First <a name="ref1"> </a>Second', notes)
    assert out == '<a name="ref1"> </a>First <a name="ref2"> </a>Second'
    assert notes == [{"kind": "corrected", "why": "ref1 defined twice; the second is ref2",
                      "decided": "Stephen Taylor"}]


def test_stale_correction_is_reported(c):
    notes = []
    assert c.apply_text("10500140", "nothing to find", notes) == "nothing to find"
    assert notes == [{"kind": "correction-stale", "find": '<a name="ref1"> </a>Second'}]


def test_articles_without_corrections_are_untouched(c):
    notes = []
    assert c.apply_text("99999999", "text", notes) == "text" and notes == []


def test_encoding_hold_and_release(c):
    assert c.encoding("10003000") == "cp850" and c.encoding("10500140") is None
    assert c.released("10011350") and not c.released("10500140")
    assert c.held("10000001") == "garbled beyond repair" and c.held("10500140") is None


def test_catalogue_corrections(c):
    issues = [{"volume": "26", "issue": "2", "year": "2014", "month": "09", "title": None,
               "span": 1, "numbers": ["2"], "pdf": "v262.pdf", "doc": None}]
    out = c.apply_catalogue(issues)
    assert out[0]["numbers"] == ["2", "3"] and out[0]["title"] == "Nos.2&3"
    new = [i for i in out if i["issue"] == "4"][0]
    assert (new["volume"], new["year"], new["month"], new["numbers"]) == ("26", "2016", "03", ["4"])


def test_every_entry_needs_why_and_decided():
    with pytest.raises(CorrectionError):
        Corrections.from_text('articles:\n  "1":\n    - find: a\n      replace: b\n')


def test_nth_occurrence_only():
    c = Corrections.from_text("""
articles:
  "1":
    - find: <a name="ref1"> </a>
      replace: <a name="ref2"> </a>
      nth: 2
      why: w
      decided: d
""")
    notes = []
    assert c.apply_text("1", 'A<a name="ref1"> </a>B<a name="ref1"> </a>C', notes) == \
        'A<a name="ref1"> </a>B<a name="ref2"> </a>C'
    assert notes[0]["kind"] == "corrected"
    assert c.apply_text("1", 'A<a name="ref1"> </a>B', []) == 'A<a name="ref1"> </a>B'


def test_apl_mapping_entry_also_releases():
    c = Corrections.from_text("""
articles:
  "1":
    - apl: apl2741
      why: w
      decided: d
""")
    assert c.apl("1") == "apl2741" and c.released("1") and c.apl("2") is None


def test_boxes_entry():
    c = Corrections.from_text('articles:\n  "1":\n    - boxes: varch-j\n      why: w\n      decided: d\n')
    assert c.boxes("1") == "varch-j" and c.boxes("2") is None
