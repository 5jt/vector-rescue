"""Issue #38: a page for every indexed article.

An index record with no text still has an old `art` URL. It gets a page
with what the index knows, and a link that opens the issue's PDF at the
article's first page. The PDFs are scans with OCR text; the offset between
PDF page and printed page is found from the page numbers in the OCR, and
the title is looked for on the computed page as a check.
"""

import html
import re
import shutil
import subprocess
import zlib
from collections import Counter
from pathlib import Path

import yaml

from .markdown import escape

NUMBER = re.compile(r"(?:^|\s)(\d{1,3})(?=\s|$)")


def pdf_pages(pdf):
    """The OCR text of each page of PDF."""
    out = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
    return out.split("\f")


CONTENT = re.compile(rb"\d+ 0 obj\s*<<[^>]*?/FlateDecode[^>]*>>\s*stream\r?\n")
TM = re.compile(rb"(-?[\d.]+) (-?[\d.]+) Tm\s*$")
TJ = re.compile(rb"\(((?:[^()\\]|\\.|\((?:[^()\\]|\\.)*\))*)\)\s*Tj", re.S)  # balanced () may go unescaped


def _pdf_string(raw):
    """A PDF literal string as text: its escapes undone, and decoded as the
    UTF-16BE of a scanner's OCR layer (else Latin-1)."""
    raw = re.sub(rb"\\([nrtbf()\\]|[0-7]{1,3})", lambda m: (
        bytes([int(m.group(1), 8)]) if m.group(1)[:1].isdigit() else
        {b"n": b"\n", b"r": b"\r", b"t": b"\t", b"b": b"\b", b"f": b"\f"}.get(m.group(1), m.group(1))), raw)
    if len(raw) % 2 == 0 and raw[:1] == b"\0":
        return raw.decode("utf-16-be", "replace")
    return raw.decode("latin-1")


def recovered_pages(pdf):
    """The OCR text of each page of a truncated PDF (#81), recovered from the
    page content streams that survive before the cut, where page tree, fonts
    and images are lost. Each word is placed by its text matrix: words are
    taken in the stream's order, which is reading order; a line ends where
    x goes back or y jumps, and a wide gap between lines starts a paragraph. Streams are taken in file order, which is
    page order in the scanner's PDFs; a stream with no text is a blank page."""
    data = Path(pdf).read_bytes()
    pages = []
    for m in CONTENT.finditer(data):
        end = data.find(b"endstream", m.end())
        if end < 0:  # the stream the cut went through
            break
        try:
            stream = zlib.decompressobj().decompress(data[m.end():end])
        except zlib.error:
            continue
        words, x, y = [], 0.0, 0.0
        for line in stream.splitlines():
            t = TM.search(line)
            if t:
                x, y = float(t.group(1)), float(t.group(2))
            for raw in TJ.findall(line):
                text = _pdf_string(raw).strip()
                if text:
                    words.append((y, x, text))
        lines = []  # [(y, [words])] in reading order: a new line where x goes back or y jumps
        last_x = last_y = 0.0
        for y, x, w in words:
            if lines and x > last_x and abs(last_y - y) < 4:  # the word before: scans are skewed
                lines[-1][1].append(w)
            else:
                lines.append((y, [w]))
            last_x, last_y = x, y
        gaps = sorted(a[0] - b[0] for a, b in zip(lines, lines[1:]) if a[0] > b[0])
        step = gaps[len(gaps) // 4] if gaps else 0  # most gaps are the line spacing
        out = []
        for i, (y, ws) in enumerate(lines):
            if i and step and lines[i - 1][0] - y > 1.6 * step:
                out.append("")
            out.append(" ".join(ws))
        pages.append("\n".join(out))
    return pages


def page_offset(pages):
    """The commonest difference between PDF page and the page number printed
    in the first or last lines of the page; None if no numbers are found."""
    diffs = Counter()
    for i, text in enumerate(pages, start=1):
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        for line in lines[:2] + lines[-2:]:
            for n in NUMBER.findall(" " + line + " "):
                d = i - int(n)
                if -5 <= d <= 12:
                    diffs[d] += 1
    return diffs.most_common(1)[0][0] if diffs else None


def _norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def title_on_page(title, text):
    """Whether most of the title's longer words appear on the page (OCR
    runs words together, so spaces are ignored)."""
    words = [w for w in re.findall(r"[a-z0-9]+", (title or "").lower()) if len(w) > 3][:4]
    if not words:
        return False
    page = _norm(text)
    return sum(1 for w in words if w in page) >= max(1, len(words) // 2 + (len(words) > 2))


CHECK_RULE = "v2"  # change when title_on_page changes, to discard cached results


OCR_SUMMARY = ("Unedited OCR text, machine-read from the scan: it contains errors, "
               "and its APL is wrong. Shown for searching; read the PDF.")


DAMAGED_SUMMARY = ("Unedited OCR text, machine-read from a scan now lost: it contains errors, "
                   "and its APL is wrong. Shown for searching.")
DAMAGED = ("No complete scan of this issue has been found. The only copy found, on vector.org.uk, is damaged: "
           "its page images are lost, but the text machine-read from them survives, shown below "
           "([help find a scan](https://github.com/5jt/vector-rescue/issues/62)).")


def ocr_block(pages, summary=OCR_SUMMARY):
    """The OCR text of PAGES, folded away in a closed <details> section:
    one <p> per paragraph, column spacing collapsed, HTML escaped."""
    paras = []
    for page in pages:
        for chunk in re.split(r"\n\s*\n", page):
            text = " ".join(" ".join(line.split()) for line in chunk.splitlines() if line.strip())
            if text:
                paras.append(f"<p>{html.escape(text, quote=False)}</p>")
    return "\n".join([f'<details class="ocr">\n<summary>{summary}</summary>', *paras, "</details>"])


def warning_block(text, title="Doubtful transcription"):
    """An admonition for the head of a page whose transcription is doubtful
    or missing (issue #58): the `warning:` of its front matter."""
    return [f'!!! warning "{title}"', "", "    " + " ".join(str(text).split()), ""]


def review_note(fm):
    """The note heading a transcribed page: who reviewed it and when, or that
    it is not yet reviewed (issue #58)."""
    note = "Transcribed from the printed issue"
    if fm.get("review") == "reviewed":
        by, on = fm.get("reviewed_by"), fm.get("reviewed_on")
        return note + "." + (f" Reviewed by {by}" if by else " Reviewed") + (f" on {on}." if on else ".")
    return note + "; not yet reviewed."


OWN_PDF = "Read it in the article’s own PDF"


def write_stub(record, docs, pdf=None, ocr=None, warning=None, note=None, own=None):
    """docs/art<ID>/index.md for a record with no text. PDF is the issue PDF's
    path from the site root, with #page=N; OWN, the file name of the
    article's own PDF, published beside the page (#111). WARNING, from a transcription with
    no text, heads the page and marks it in the issue index. NOTE follows the
    statement that the text is not online (the damaged scan of #81)."""
    fm = {"vid": record["id"], "title": record["title"] or f"Article {record['id']}"}
    if record.get("authors"):
        fm["authors"] = record["authors"]
    for k in ("volume", "issue", "page", "online"):
        if record.get(k):
            fm[k] = record[k]
    fm["status"] = "not online"
    if warning:
        fm["warning"] = warning
    lines = ["---", yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000).rstrip(), "---", ""]
    if warning:
        lines += warning_block(warning, "Not transcribed")
    if record.get("authors"):
        lines += [escape(", ".join(record["authors"])) + "\n{ .byline }", ""]
    lines.append("The text of this article is not yet online." + (f" {note}" if note else ""))
    if own:
        lines += ["", f"[{OWN_PDF}]({own})"]
    if pdf:
        page = f", page {record['page']}" if record.get("page") else ""
        lines += ["", f"[Read it in the PDF of the issue{page}](../{pdf})"]
    if ocr:
        lines += ["", ocr]
    path = Path(docs) / f"art{record['id']}" / "index.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def read_transcription(path):
    """The front matter (a dict) and Markdown body of a transcription."""
    _, head, body = Path(path).read_text(encoding="utf-8").split("---", 2)
    return yaml.safe_load(head), body


def write_transcribed(record, docs, transcription, pdf=None, name=None, own=None):
    """docs/art<ID>/index.md from TRANSCRIPTION (transcriptions/art<ID>.md,
    issue #40), in place of the stub: its text, a note of its review state,
    the PDF link, and its figures from transcriptions/art<ID>/. NAME, for a
    piece with no index entry, is its page folder and figure folder (#93)."""
    transcription = Path(transcription)
    fm, body = read_transcription(transcription)
    fm["status"] = "transcribed"
    note = review_note(fm)
    if own:
        note += f" [{OWN_PDF}]({own})"
    if pdf:
        page = f", page {record['page']}" if record.get("page") else ""
        note += f" [Read it in the PDF of the issue{page}](../{pdf})"
    name = name or f"art{record['id']}"
    folder = Path(docs) / name
    figures = transcription.with_suffix("")
    if figures.is_dir():
        shutil.copytree(figures, folder, dirs_exist_ok=True)
    body = body.strip("\n").replace(f"]({name}/", "](")
    lines = ["---", yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000).rstrip(), "---", "",
             f"*{note}*", "{ .transcribed }", ""] + (warning_block(fm["warning"]) if fm.get("warning") else []) + [body]
    path = folder / "index.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path
