"""Issue #6: images and figures.

localise_images runs on the whole source document before conversion, so
images inside raw HTML (tables, lists) are copied and rewritten too.
"""

import copy
import os
import re
from pathlib import Path

from .markdown import INLINE_RULES, escape, escape_line_starts, inline, raw_html, raw_inline

OLD_SITE = re.compile(
    r"^https?://(?:(?:www|archive|linux)\.)?vector\.org\.uk/|"
    r"^https?://vector\.johnbutlerassociates\.co\.uk/")
EXT_TYPE = {".jpg": "jpeg", ".jpeg": "jpeg", ".png": "png", ".gif": "gif", ".bmp": "bmp"}
MAGIC = ((b"\x89PNG", "png"), (b"\xff\xd8\xff", "jpeg"), (b"GIF8", "gif"), (b"BM", "bmp"))


def sniff(data):
    """The image type DATA looks like, or None."""
    for magic, kind in MAGIC:
        if data.startswith(magic):
            return kind
    return None


def localise_images(doc, root, source, notes):
    """Rewrite <img src> to paths inside the article's output folder.

    Returns {src: source file} for the files to copy beside the page.
    Relative srcs are kept; images on the old site are copied from the
    recovered tree when present. Missing files and files whose content
    does not match their extension are noted.
    """
    root = Path(root)
    base = Path(source).parent
    assets = {}
    for img in doc.iter("img"):
        src = (img.get("src") or "").strip()
        if not src:
            continue
        if OLD_SITE.match(src):
            rel = OLD_SITE.sub("", src)
            path = root / rel
        elif re.match(r"^[a-z]+:", src, re.I) or src.startswith("/"):
            continue  # another site: leave it
        else:
            rel = src
            path = root / os.path.normpath(base / src)
        if not path.is_file():
            notes.append({"kind": "image-missing", "src": src})
            continue
        img.set("src", rel)
        assets[rel] = path
        expected = EXT_TYPE.get(path.suffix.lower())
        actual = sniff(path.read_bytes()[:16])
        if expected and actual != expected:
            notes.append({"kind": "image-format-mismatch", "src": rel, "actual": actual})
    return assets


# inline <img> -----------------------------------------------------------------

def image(el):
    src, alt, title = el.get("src"), el.get("alt") or "", el.get("title")
    attrs = [(k, el.get(k)) for k in ("width", "height", "style") if el.get(k)]
    if (not src or re.search(r"[\s()<>]", src) or (title and '"' in title)
            or any('"' in v for _, v in attrs)):
        return raw_inline(el)
    title = f' "{title}"' if title else ""
    attr_list = " ".join(f'{k}="{v}"' for k, v in attrs)
    return f"![{escape(alt)}]({src}{title})" + (f"{{ {attr_list} }}" if attrs else "")


INLINE_RULES["img"] = image


# p.caption → <figure> --------------------------------------------------------

def _float(classes):
    if classes & {"fright", "right"}:
        return "right"
    if classes & {"fleft", "left"}:
        return "left"
    return None


def figure(el, ctx):
    """A caption paragraph: a figure if it holds one image, else a caption."""
    imgs = el.findall(".//img")
    if not imgs:
        md = escape_line_starts(inline(el))
        return f"{md}\n{{ .caption }}" if md else ""
    children = [k for k in el if isinstance(k.tag, str)]
    media = children[0]
    reason = None
    if len(imgs) > 1:
        reason = "several-images"
    elif (el.text or "").strip() or not (media.tag == "img" or media.find(".//img") is not None):
        reason = "text-before-image"
    if reason:
        ctx["raw"] = True
        ctx["notes"].append({"kind": "figure-raw", "reason": reason})
        return raw_html(el)

    holder = el.makeelement("p", {})
    item = copy.deepcopy(media)
    item.tail = None
    holder.append(item)
    media_md = inline(holder)

    caption = el.makeelement("p", {})
    caption.text = media.tail
    for k in media.itersiblings():
        caption.append(copy.deepcopy(k))
    if not (caption.text or "").strip() and len(caption) and caption[0].tag == "br":
        first = caption[0]
        caption.text = first.tail
        caption.remove(first)
    caption_md = inline(caption).replace("  \n", "<br>")

    cls = _float(set((el.get("class") or "").split()))
    lines = [f'<figure class="{cls}" markdown="1">' if cls else '<figure markdown="1">', media_md]
    if caption_md:
        lines.append(f'<figcaption markdown="span">{caption_md}</figcaption>')
    lines.append("</figure>")
    ctx["raw"] = True  # an HTML block: a list or quote holding it must be raw
    return "\n".join(lines)
