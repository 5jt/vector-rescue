from vecrescue.review import apply, mark_reviewed, ticked

TRANSCRIPTION = """---
vid: '10007700'
title: Operators & Nested Arrays
review: draft
warning: >-
  Two lines of code
  are doubtful.
queries:
- "A slip, transcribed as printed."
---

Some text.
"""

URL = "https://github.com/5jt/vector-rescue/blob/main/transcriptions"
CHECKLIST = f"""# Checklist

- [x] **Operators & Nested Arrays**, John Scholes · [transcription]({URL}/art10007700.md) · [PDF](x.pdf#page=119) — Jane Doe
- [x] **Guide**, Norman Thomson · [transcription]({URL}/art10009930.md) · [PDF](x.pdf#page=110)
- [ ] **Tree-processing**, Anne Wilson · [transcription]({URL}/art10010930.md) — Jane Doe
- [x] **Meeting**, Adrian Smith · [transcription]({URL}/unindexed/v1n1-p41-x.md) — Joe Bloggs, 2026-10-01
"""


def _setup(tmp_path):
    t = tmp_path / "transcriptions"
    (t / "unindexed").mkdir(parents=True)
    (t / "art10007700.md").write_text(TRANSCRIPTION, encoding="utf-8")
    (t / "art10009930.md").write_text(TRANSCRIPTION, encoding="utf-8")
    (t / "unindexed" / "v1n1-p41-x.md").write_text(TRANSCRIPTION, encoding="utf-8")
    c = tmp_path / "checklist.md"
    c.write_text(CHECKLIST, encoding="utf-8")
    return c, t


def test_ticked_lines_are_read_with_their_signatures(tmp_path):
    c, _ = _setup(tmp_path)
    assert [x[:3] for x in ticked(c)] == [("art10007700.md", "Jane Doe", None),
                                          ("art10009930.md", None, None),
                                          ("unindexed/v1n1-p41-x.md", "Joe Bloggs", "2026-10-01")]


def test_mark_reviewed_keeps_the_rest_of_the_front_matter():
    text = mark_reviewed(TRANSCRIPTION, "Jane Doe", "2026-10-06")
    assert text == """---
vid: '10007700'
title: Operators & Nested Arrays
queries:
- "A slip, transcribed as printed."
review: reviewed
reviewed_by: Jane Doe
reviewed_on: '2026-10-06'
---

Some text.
"""


def test_apply_marks_signed_ticks_reviewed(tmp_path):
    c, t = _setup(tmp_path)
    results = {p.name: outcome for p, outcome in apply(c, t, today="2026-10-06")}
    assert results["art10007700.md"] == "reviewed"
    assert results["art10009930.md"].startswith("ticked but not signed")
    assert results["v1n1-p41-x.md"] == "reviewed"
    assert "reviewed_on: '2026-10-06'" in (t / "art10007700.md").read_text()
    assert "reviewed_on: '2026-10-01'" in (t / "unindexed" / "v1n1-p41-x.md").read_text()
    assert "review: draft" in (t / "art10009930.md").read_text()
    again = {p.name: outcome for p, outcome in apply(c, t, today="2026-10-07")}
    assert again["art10007700.md"] == "already reviewed"
    assert "reviewed_on: '2026-10-06'" in (t / "art10007700.md").read_text()


def test_apply_refuses_a_transcription_without_text(tmp_path):
    c, t = _setup(tmp_path)
    (t / "art10007700.md").write_text(TRANSCRIPTION.split("---\n\n")[0] + "---\n", encoding="utf-8")
    results = {p.name: outcome for p, outcome in apply(c, t)}
    assert results["art10007700.md"] == "has no text to review"
