"""Set each article's byline under its title in the built site (#285).

The one step after the Zensical build. It uses only the standard library, so
that it can run on its own in the official repository's publishing workflow
(#341): `python lift_bylines.py SITE`."""

import re
import sys
from pathlib import Path

BYLINE = re.compile(r'<p class="byline">.*?</p>\n?', re.S)
TITLE = re.compile(r'(<h1 id="__skip">.*?</h1>\n?)', re.S)


def lift_bylines(site):
    """Set each article's byline directly under its title (#285): the first
    byline paragraph of the article text, if it opens the text (no heading or
    long paragraph before it), moves to follow the h1. A transcription's
    byline keeps the transcribed text's typeface. Returns the pages changed."""
    changed = 0
    for page in Path(site).glob("**/index.html"):
        html = page.read_text(encoding="utf-8")
        title = TITLE.search(html)
        if not title:
            continue
        by = BYLINE.search(html, title.end())
        if not by or "<h2" in html[title.end():by.start()] or len(re.sub(r"<[^>]+>", "", html[title.end():by.start()])) > 600:
            continue
        lifted = by.group(0).rstrip("\n")
        if '<div class="transcribed-text">' in html[title.end():by.start()]:
            lifted = lifted.replace('<p class="byline">', '<p class="byline transcribed-text">', 1)
        html = html[:by.start()] + html[by.end():]
        html = html[:title.end()] + lifted + "\n" + html[title.end():]
        page.write_text(html, encoding="utf-8")
        changed += 1
    return changed


if __name__ == "__main__":
    print(f"Bylines lifted on {lift_bylines(sys.argv[1])} pages")
