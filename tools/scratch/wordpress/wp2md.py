"""Convert a WordPress post (Gutenberg blocks or classic HTML) to Markdown.

usage: wp2md.py POST.html OUT.md IMGDIR NAME
Converts the HTML as rendered, not the Markdown source some Jetpack blocks
keep (it can be stale). Raw HTML blocks are kept, without style and class.
Code blocks: fenced, verbatim. Embeds: links. Everything else: pandoc HTML ->
markdown_strict (4-space list indentation, as Python-Markdown needs).
Images under wp-content/uploads are fetched from vector.org.uk into IMGDIR
and linked as NAME/<file>."""
import html, json, re, subprocess, sys, urllib.request
from pathlib import Path

src, out, imgdir, name = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3]), sys.argv[4]
text = open(src, encoding="utf-8").read()
OPEN = re.compile(r"<!-- (/?)wp:([\w/-]+)(?: (\{.*?\}))? (/?)-->", re.S)


def blocks(s):
    """Top-level (name, attrs, inner) blocks; text outside blocks as ('html', {}, text)."""
    out, depth, start, cur, pos = [], 0, 0, None, 0
    for m in OPEN.finditer(s):
        closing, bname, attrs, selfclose = m.group(1), m.group(2), m.group(3), m.group(4)
        if depth == 0 and not closing:
            gap = s[pos:m.start()]
            if gap.strip():
                out.append(("classic", {}, gap))
            if selfclose:
                out.append((bname, json.loads(attrs) if attrs else {}, ""))
                pos = m.end()
                continue
            cur, start, depth = (bname, json.loads(attrs) if attrs else {}), m.end(), 1
        elif not closing and not selfclose:
            depth += 1
        elif closing:
            depth -= 1
            if depth == 0:
                out.append((cur[0], cur[1], s[start:m.start()]))
                pos = m.end()
    if s[pos:].strip():
        out.append(("classic", {}, s[pos:]))
    return out


def pandoc(h):
    h = re.sub(r"\[caption[^\]]*\](.*?)\[/caption\]", r"<figure>\1</figure>", h, flags=re.S)
    r = subprocess.run(["pandoc", "-f", "html", "-t", "markdown_strict+pipe_tables+backtick_code_blocks+fenced_code_attributes-raw_html", "--wrap=none"],
                       input=h, capture_output=True, text=True, check=True)
    return r.stdout.strip()


def code(inner):
    m = re.search(r"<pre[^>]*>(.*?)</pre>", inner, re.S)
    body = html.unescape(re.sub(r"<[^>]+>", "", m.group(1) if m else inner))
    return "```\n" + body.strip("\n") + "\n```"


parts = []
for bname, attrs, inner in blocks(text):
    if bname in ("spacer", "separator") or not (inner.strip() or attrs):
        continue
    if bname == "html":  # a raw HTML block: kept as HTML, without inline styles
        parts.append(re.sub(r'\s(?:style|class)="[^"]*"', "", inner).strip())
    elif bname in ("codemirror-blocks/code-block", "code"):
        parts.append(code(inner))
    elif bname.startswith("core-embed/") or bname == "embed":
        url = attrs.get("url") or re.search(r"https?://\S+", inner).group(0)
        parts.append(f"[Video]({url.strip()})")
    else:
        md = pandoc(inner)
        if md:
            parts.append(md)
md = "\n\n".join(p for p in parts if p)
md = re.sub(r"^```[ {]*[^`\n]*$", "```", md, flags=re.M)          # bare fences, as in the other transcriptions
def prose(t):
    t = re.sub(r"\\\n", "  \n", t)                         # hard line breaks: two spaces (Python-Markdown)
    return re.sub(r"^(\[?!\[[^\]]*\]\([^)]*\)(?:\]\([^)]*\))?) +(\S.*)$", r"\1\n\n*\2*", t, flags=re.M)  # caption under its figure


chunks = re.split(r"(^```\n.*?^```$)", md, flags=re.M | re.S)   # odd chunks are code
def unescape_code(c):  # WordPress double-escaped some code: &amp;lt; for <
    return html.unescape(c)


def inline(t):
    return re.sub(r"`[^`\n]+`", lambda m: unescape_code(m.group(0)), t)


md = "".join(unescape_code(c) if i % 2 else inline(prose(c)) for i, c in enumerate(chunks))
md = re.sub(r"\[(!\[[^\]]*\]\(([^)]*)\))\]\(\2\)", r"\1", md)  # an image linked to itself

imgdir.mkdir(parents=True, exist_ok=True)


def fetch(m):
    url = m.group(0)
    live = re.sub(r"^https?://[^/]+", "https://vector.org.uk", url)
    fn = url.rsplit("/", 1)[1]
    dest = imgdir / fn
    if not dest.exists():
        try:
            dest.write_bytes(urllib.request.urlopen(live, timeout=30).read())
        except Exception as e:
            print("MISSING", live, e, file=sys.stderr)
            return url
    return f"{name}/{fn}"


md = re.sub(r"https?://[^\s)\"']*/wp-content/uploads/[^\s)\"']+\.(?:png|jpe?g|gif|svg|webp)", fetch, md, flags=re.I)
out.write_text(md + "\n", encoding="utf-8")
print(out, len(md))
