"""Issue #38: a page for every indexed article.

An index record with no text still has an old `art` URL. It gets a page
with what the index knows, and a link that opens the issue's PDF at the
article's first page. The PDFs are scans with OCR text; the offset between
PDF page and printed page is found from the page numbers in the OCR, and
the title is looked for on the computed page as a check.
"""

import re
import subprocess
from collections import Counter
from pathlib import Path

import yaml

from .markdown import escape

NUMBER = re.compile(r"(?:^|\s)(\d{1,3})(?=\s|$)")


def pdf_pages(pdf):
    """The OCR text of each page of PDF."""
    out = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
    return out.split("\f")


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


def write_stub(record, docs, pdf=None):
    """docs/art<ID>/index.md for a record with no text. PDF is the issue PDF's
    path from the site root, with #page=N."""
    fm = {"vid": record["id"], "title": record["title"] or f"Article {record['id']}"}
    if record.get("authors"):
        fm["authors"] = record["authors"]
    for k in ("volume", "issue", "page", "online"):
        if record.get(k):
            fm[k] = record[k]
    fm["status"] = "not online"
    lines = ["---", yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000).rstrip(), "---", ""]
    if record.get("authors"):
        lines += [escape(", ".join(record["authors"])) + "\n{ .byline }", ""]
    lines.append("The text of this article is not yet online.")
    if pdf:
        page = f", page {record['page']}" if record.get("page") else ""
        lines += ["", f"[Read it in the PDF of the issue{page}](../{pdf})"]
    path = Path(docs) / f"art{record['id']}" / "index.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path
