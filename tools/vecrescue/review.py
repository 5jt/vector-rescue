"""Record reviews ticked in the review checklist (issue #58).

A reviewer ticks an article's line in plans/pdf-review-checklist.md and puts
their name at the end, after an em dash, optionally with the date:

    - [x] **Title**, Author (…) · [transcription](…/transcriptions/art10007700.md) · … — Jane Doe, 2026-10-06

apply() sets the transcription's front matter to `review: reviewed`, with
`reviewed_by` and `reviewed_on` (today if no date is given), and drops any
`warning:`, since the reviewer has checked the text against the page. The
front matter is edited line by line, so the rest of it keeps its form.
"""

import datetime
import re
from pathlib import Path

import yaml

TICKED = re.compile(r"^\s*[-*] \[[xX]\] (.*)$")
LINK = re.compile(r"\]\([^)]*?transcriptions/([^)\s]+\.md)\)")
SIGNED = re.compile(r"\s+—\s+([^—]+?)(?:,\s*(\d{4}-\d{2}-\d{2}))?\s*$")


def ticked(checklist):
    """[(transcription path under transcriptions/, name or None, date or None, line)]
    for each ticked line of CHECKLIST that links to a transcription."""
    out = []
    for line in Path(checklist).read_text(encoding="utf-8").splitlines():
        m = TICKED.match(line)
        link = m and LINK.search(m.group(1))
        if link:
            signed = SIGNED.search(m.group(1)[link.end():])
            out.append((link.group(1), signed and signed.group(1).strip(), signed and signed.group(2), line))
    return out


def _scalar(key, value):
    return yaml.safe_dump({key: value}, allow_unicode=True, width=1000).rstrip()


def mark_reviewed(text, name, date):
    """TEXT (a transcription) with its front matter marked reviewed by NAME on DATE."""
    _, head, body = text.split("---", 2)
    lines, out, skipping = head.split("\n"), [], False
    for line in lines:
        if skipping and (line.startswith((" ", "\t")) or not line):
            continue  # a continued value of a dropped key
        skipping = False
        if re.match(r"(review|reviewed_by|reviewed_on|warning):", line):
            skipping = True
            continue
        out.append(line)
    while out and not out[-1]:
        out.pop()
    out += [_scalar("review", "reviewed"), _scalar("reviewed_by", name), _scalar("reviewed_on", date), ""]
    return "---" + "\n".join(out) + "---" + body


def apply(checklist, transcriptions, today=None):
    """Mark reviewed each transcription ticked and signed in CHECKLIST.
    Returns [(path, outcome)], the outcome "reviewed", "already reviewed", or
    the reason it was not."""
    today = today or datetime.date.today().isoformat()
    results = []
    for rel, name, date, _ in ticked(checklist):
        path = Path(transcriptions) / rel
        if not path.is_file():
            results.append((path, "no such transcription"))
            continue
        if not name:
            results.append((path, "ticked but not signed (add “ — Your Name” at the end of the line)"))
            continue
        text = path.read_text(encoding="utf-8")
        fm, body = yaml.safe_load(text.split("---", 2)[1]) or {}, text.split("---", 2)[2]
        if not body.strip():
            results.append((path, "has no text to review"))
        elif fm.get("review") == "reviewed" and fm.get("reviewed_by") == name:
            results.append((path, "already reviewed"))
        else:
            path.write_text(mark_reviewed(text, name, date or today), encoding="utf-8")
            results.append((path, "reviewed"))
    return results
