# Plan: survey of the hand-coded XHTML (target for the Markdown)

Part of Phase 2b of `plans/master.md`.

## Why

The articles under `content/printed/` and `content/published/` were hand-coded as XHTML 1.0 Strict, and the older ones under `trad/` are looser HTML. We cannot assume that standard Markdown or GitHub-flavoured Markdown represents them. Before writing a converter we need to know what structures occur and how to represent each, so the target Markdown, and the renderer, are chosen from evidence.

## Method

1. **Inventory elements.** Parse the 148 XHTML files (and later the UTF-8 HTML files) and count every element, attribute, `class` and `id`, per file and in total. Rank by frequency and by number of files.
2. **Classify each structure** as one of:
   - plain Markdown (headings, paragraphs, lists, emphasis, links, images, simple code);
   - Markdown with common extensions (tables, footnotes, definition lists, attribute lists such as `{ #id .class }`, fenced code, admonitions);
   - needs raw HTML or Markdown-in-HTML;
   - needs a custom rule or pre-processing.
3. **Look specifically at:**
   - the heading pattern (`h1.prefix`, `h1#title`, `h1#author`, `#abstract`) which is a metadata block rather than headings;
   - `<pre>` and `<code>` blocks containing APL, J, K or q; whitespace, entities and characters that must not be reflowed;
   - tables (layout versus data), nested lists, definition lists;
   - mathematics (the seven unindexed XHTML fragments in `content/printed/`, MathML or images);
   - figures, captions, image sizing and alignment;
   - internal anchors and cross-references (`#ref3`-style), footnotes and bibliographies;
   - `<meta>` fields: author, editor, vid, received, online, volume, issue, page;
   - inline spans and classes that carry meaning (APL glyph fonts, emphasis conventions);
   - the `vector.org.uk` links inside articles that need rewriting to the new URLs.
4. **Round-trip test.** Convert a few representative articles (e.g. `art10500650`, and one with figures and one with maths), render them with each candidate (Zensical first), and compare with the original page in a browser: text, structure and link equality.
5. **Test the renderer.** Check what the renderer supports out of the box against the table of structures: required Markdown extensions, raw HTML passthrough, metadata and front matter, per-page output paths, code-block handling of APL, maths.

## Output

`plans/xhtml-target-survey-results.md` containing:

- the table of structures (frequency, files, Markdown representation, extension needed);
- the list of Markdown extensions and renderer features required;
- cases that cannot be represented and what to do (raw HTML, custom rule, manual edit);
- a recommendation on Zensical (or another renderer), with a worked example for `art10500650`;
- a draft of the converter's rules, ready to turn into issues.

## Notes

- Work only on copies; `sources/` is read-only.
- Keep scripts in the repo (suggest `tools/`) on a branch with an issue raised, per `CLAUDE.md`. The results document is a plan and may go to `main`.
- Zensical points from its documentation need confirming by trial: its Markdown support (Python Markdown, Material for MkDocs extensions) and whether it can output exact `/art<ID>` paths.
- Expected scale: the XHTML set is small (148 files for printed and published articles), so the full inventory is quick; the looser `trad/` HTML is much larger and varied and can follow.
