# Survey: the hand-coded XHTML and the Markdown target

Executes `plans/xhtml-target-survey.md`. Surveyed by Claude on 2026-10-02. All work was done on copies or in memory; `sources/` was not modified. Scripts lived in a scratch directory and are not yet in the repo (see "Next steps").

## Short answers

1. **The XHTML is small and regular.** 148 indexed XHTML articles (all under `content/`), 5,986 paragraphs, 1,859 `<pre>` blocks, 98 tables. Its vocabulary is modest: a handful of semantic classes carry nearly all the meaning.
2. **Most of it converts to Markdown cleanly, but not by pandoc out of the box.** Three things need rules: the **title/author/metadata block**, **`<pre>` blocks** (pandoc 3.11 mangles a bare `<pre>`), and a small set of **classes and layout tables** that Markdown has no syntax for.
3. **Zensical works as a renderer for this content.** In a trial it built the page, passed raw HTML and MathML through, supported footnotes, definition lists, `attr_list`, `md_in_html`, admonitions and APL code highlighting out of the box, and built ~1,500 pages in 55 s. It can emit `/art<ID>/index.html` or `/art<ID>.html`, **but not an extensionless `/art<ID>` file** (see "Renderer trial").
4. **Valid UTF-8 does not mean correct APL.** Of the 295 valid-UTF-8 `trad/` HTML files, 23 still use font-mapped APL (APL2741, APLX, APLNet). The first slice should therefore be XHTML, then the UTF-8 `trad/` files with a font check.

## 1. The XHTML set

Indexed `vec:source fmt="XHTML"` files: **148**, all present. 100 parse as well-formed XML; the other 48 fail only because they use HTML entities XML does not define (`&nbsp;` 19 files, `&ldquo;`/`&lsquo;`/`&rsquo;` 8, 8 and 7, `&ndash;` 4, `&times;` 1, `&sup2;` 1). So the set is XHTML in intent, not always in fact. Parse it as HTML (or define the entities).

### Element counts (files containing)

| Element | Count | Files | Notes |
|---|---:|---:|---|
| `p` | 5,986 | 148 | 403 have a `class` |
| `code` | 4,596 | 109 | Inline code, including APL |
| `pre` | 1,859 | 98 | Code and listings; **only 1 is wrapped in `<code>`** |
| `a` | 1,324 | 147 | 943 `href`, 311 `name`, 73 `id` |
| `td`/`tr`/`table` | 2,944 / 687 / 98 | 30 | Tables in only 30 files |
| `li` | 1,239 | 126 | `ul` 213 (105 files), `ol` 113 (87) |
| `em` / `strong` | 945 / 217 | 86 / 27 | |
| `h2` / `h3` / `h4` | 676 / 357 / 48 | 118 / 45 / 6 | |
| `br` | 638 | 91 | |
| `img` | 338 | 65 | 233 png, 73 jpg, 34 gif, 14 jpeg |
| `cite` | 261 | 65 | Titles of works |
| `dfn` | 92 | 24 | Defined terms |
| `blockquote` | 88 | 28 | |
| `dl`/`dt`/`dd` | 35 / 98 / 124 | 19 | |
| `sup` / `sub` | 114 / 84 | 18 / 13 | |
| `math` (MathML) | 13 | 2 | `nflpasser.htm`, `jot57.htm` |
| `svg` | 7 | 1 | `jot57.xhtml` (SVGMath output) |
| `object`/`embed`/`param` | 1/1/3 | 1 | A YouTube embed in `unicode.htm` |
| `style` | 7 | 7 | Inline style blocks |

### Meta tags

Every file has `<meta>` fields (1,506 in all). Names found: `author` 159, `volume`/`issue`/`page`/`vid` 146 each, `description` 143, `online` 120, `received` 100, `editor` 73, `keywords` 21, `status` 6, `generator` 4, `reviewer` 1. `vid` is the `art` ID. These are the article metadata and should become front matter, cross-checked against `index.xml`.

### The head-of-article pattern

Most files start with a fixed block, not ordinary headings:

```html
<h1 class="prefix">No Stinking Loops</h1>      <!-- series/column name (24 files) -->
<h1 id="title">Tables with calculated columns</h1>   <!-- 142 files -->
<h1 class="subtitle">…</h1>                    <!-- 10 files -->
<h1 id="author">by Stevan Apter</h1>           <!-- 127 files; p#author in 14 more -->
<p id="abstract">…</p>                        <!-- 66 files -->
```

Plus, at the foot or head, editorial/workflow furniture to **drop**: `<ul id="publication"><li id="status"/><li id="version"/>` (83 files, "Ready to post", "Proof for author"), and `<p id="validation">` (142 files, a W3C validator link wrapping `&#160;`). Pandoc turns these into three H1s and a junk link (see the trial).

Bylines often include **email addresses** ("Adrian Smith (adrian@apl385.com)", "John Jacob (editor@vector.org.uk)"). That's author personal data in a public archive: decide whether to keep it (see questions).

### Classes that carry meaning

Class frequencies (count, files). Presentation-only classes are marked "(layout)".

| Class | Count | Meaning | Markdown handling |
|---|---:|---|---|
| `p.caption` | 230 (48 files) | Figure caption, usually with an `<img>` in the same `<p>` | `<figure>`/`<figcaption>` (raw HTML or `md_in_html`) |
| `p.center`, `p.centred`, `img.center`, `table.center` | ~230 | Centring (layout) | Drop, or CSS class via `attr_list` |
| `td.left`, `table.left`, `p.left`, `p.right` | ~140 | Alignment (layout) | Table alignment row, else drop |
| `td.code`, `col.code`, `table.code`, `dt.code`, `dd.code` | ~110 | Cell/column content is code | Backticks inside cells |
| `img.bdr`, `img.pad`, `img.border`, `img.full`, `img.right`, `img.left` | ~170 | Image border/float/width (layout) | `attr_list` (`{ width=… }`), or drop |
| `p.pagebreak` | 33 (16 files) | `<br/><br/>` spacers for print | Drop |
| `p.fright`, `p.fleft` | 43 | Floats, e.g. equation numbers "(1)" | Raw HTML or drop |
| `h1.prefix`, `h1.subtitle` | 36 | Part of the title block | Front matter |
| `p.ednote` | 19 (19 files) | **Editor's note**, real content | `<p class="ednote">` via `md_in_html`, or an admonition |
| `p.math`, `span.infin` | 26 | Maths layout | See mathematics |
| `span.nowrap` | 19 | Keep an expression on one line | Plain text |
| `ol.references`, `div.references` | 9 (+5) | Numbered references with `<a name="refN">` anchors | Footnotes (`[^n]`) or an ordered list with anchors |
| `pre.tight`, `.listing`, `.shaded`, `.spice` | ~40 | Code styling variants | Fenced code, drop style |

### Inline and block structures worth special attention

- **`<pre>` and `<code>` with APL, J, K, q.** 1,859 `<pre>` blocks; 4,596 `<code>` spans. 71 files contain APL/symbol characters; 69 distinct such characters occur in the XHTML (e.g. `← ⎕ ⍵ ⍝ ⍺ → ⍴ ∘ ⍳ ∇ ⋄ ↓ ⊂ ↑ ⊢ ⍨ ⌽ ⍉ ≡ ⍒ ⍋ ⍣ ≠ ⌊ ≢ ⍬ ⌈ ⊣ ⊖ ○ ≤`). `<strong>`, `<em>` and `<span>` also occur **inside** `<pre>` (about 30 occurrences in 3–4 files) and would be lost in a fenced block. Whitespace must be preserved exactly (APL output is columnar).
- **Tables (98).** Both data and layout. 30 files. `td` styles (`style="text-align:left"` etc.) and `<col style=…>` shading appear; `<table>` inside `<table>` occurs in one file (23 times); 26 `<pre>` and 12 `<img>` appear **inside table cells**, which GFM tables cannot hold. Only 127 `<th>`; many tables have no header row, so GFM would need an empty header (pandoc did exactly that: `|  |  |`).
- **Block content inside list items and blockquotes.** 32 `<p>`, 9 nested `<ul>`, 4 `<pre>` in `<li>`; blockquotes contain 221 `<p>` and 30 `<pre>`. The blockquotes are mostly interview transcripts and quotations (multiple speaker paragraphs), which Markdown `>` handles.
- **Definition and term markup:** `<dl>` (19 files) and `<dfn>` (92, 24 files). Python Markdown's definition lists work. `<dfn>` has no Markdown form; keep as raw inline HTML or convert to emphasis.
- **Mathematics.** Two files embed MathML (13 `<math>` elements, using `mfrac`, `mfenced`, `msup`, `msqrt`…); one has SVG built from MathML (SVGMath metrics). Seven further XHTML fragments under `content/printed/` aren't indexed. Most other maths is written with `<sup>`, `<sub>` and `span.nowrap`.
- **Anchors and links.** 943 `href`: 412 in-page `#` anchors (references, footnotes), 447 external, 44 relative, 17 pointing at vector.org.uk, 4 `mailto:`. Anchors are mostly `<a name="refN">` (311) and `li id`. The 17 internal-site links need rewriting: `archive.vector.org.uk/artN` (10), `?vol=&no=&art=` (2), `www.vector.org.uk/archive/v234/…` (3), and **issue-page URLs such as `archive.vector.org.uk/24/1`**. Issue-page URLs are a further URL form the new site should support.
- **Entities.** The common set is `gt lt quot amp nbsp rsquo lsquo rdquo ldquo ndash`, plus rare `lambda sup2 eacute times`. Straight text conversion handles them; keep `nbsp` out of code blocks.
- **Images.** 338 `<img>` with `alt` in 336 cases (good). Directories hold the files; 26 `.jpg` files elsewhere contain BMP data (from the filetree survey) and need checking per article. A YouTube `<object>` in `unicode.htm` has no static equivalent.
- **Stylesheet links.** All 148 `<link>` to `proof.css` or `pdf.css` and a favicon, on `www.`, `archive.` and `linux.` vector.org.uk hosts. They are chrome and can be dropped.

## 2. Pandoc trial (`art10500650`)

Command: `pandoc -f html -t gfm --wrap=none` (pandoc 3.11).

| Observation | Detail |
|---|---|
| **Bare `<pre>` is mangled** | Pandoc reads `<pre>…</pre>` (no `<code>` child) as a paragraph with `\` hard line breaks and non-breaking spaces. APL/q code would be destroyed. Only 1 of 1,859 `<pre>` has a `<code>` child, so this affects nearly everything. **Workaround that works:** wrap each `<pre>` content in `<code>` before conversion; the output is then an indented code block with whitespace preserved. |
| Title block | Three H1s: "No Stinking Loops", the title, and "by Stevan Apter". Metadata isn't separated. |
| Abstract | Becomes an ordinary paragraph. |
| Tables | Converted to a GFM table, with an **empty header row** (`\|  \|  \|`) because the source has no `<th>`. |
| `<dfn>` | `<span class="dfn">raze</span>` leaks into the Markdown. |
| Validator link | Becomes `[ ](http://validator.w3.org/…)`: noise. |
| Code | Inline code is fine; fenced/indented code is fine after the `<pre>` fix. |

**Conclusion:** use pandoc's reader only after pre-processing, or write the converter ourselves on a parsed tree (e.g. Python with `html5lib`, `lxml` or BeautifulSoup) so that each rule in section 1 is explicit and testable. A custom converter is probably better, since rules for head block, `pre`, classes, tables and anchors are all needed anyway. This needs a decision.

## 3. Renderer trial: Zensical 0.0.67

Installed with `pip install zensical` into a scratch venv (Python 3.14). Config is `zensical.toml`; content is `docs/*.md`.

| Question | Result |
|---|---|
| Builds the converted article? | **Yes.** Output page `art10500650/index.html` (default). |
| Exact `/art<ID>` path? | `use_directory_urls = true` gives `/art10500650/` (a directory with `index.html`); `false` gives `/art10500650.html`. **Neither gives an extensionless `/art10500650`.** GitHub Pages would redirect `/art10500650` to `/art10500650/`. Whether Pages can serve an extensionless file with `text/html` was not tested. |
| Raw HTML passthrough | **Yes**: `<table class="bdr"><tr><td><pre>…` unchanged. |
| `md_in_html` (`markdown="1"`) | **Yes**: `<figure markdown="1">` and `<p class="ednote" markdown="1">` rendered Markdown inside HTML. |
| `attr_list` | **Yes**: `![alt](x.png){ width="200" }` produced `width="200"`. |
| Footnotes, definition lists, admonitions | **Yes**, all rendered. |
| MathML | **Passed through unchanged**; browsers render it (not visually checked here). |
| APL in code | Inline `⍴⍵←⍳10` kept. A fenced block labelled `apl` was syntax-highlighted. Fonts for APL glyphs are a styling task. |
| Front matter (`title:`) | Honoured. |
| Heading anchors | `h1 id="…"` with permalink pilcrow, so internal `#` links need slug compatibility with our anchors. |
| Scale | 1,500 copies of a 31 KB page built in **55 s** (0.3 s for one). Output 613 MB, mostly `search.json` (27 MB) plus per-page chrome; the real corpus will differ. |
| Maturity | Version 0.0.x; it is from the Material for MkDocs team and Dyalog uses it. Expect change. |

Not tested: `serve`, GitHub Pages deployment, navigation for ~100 issues, custom templates, search quality with APL characters, extensionless file serving.

## 4. What the `trad/` HTML needs (for the second slice)

Not part of the XHTML set, but sized now because "UTF-8 first" includes it.

- 458 indexed HTML files exist: **295 are valid UTF-8, 163 are not** (agrees with the Codex survey). 231 of the 295 are pure ASCII (entities for everything else).
- It is old-style HTML: `<font>` (1,060 uses in 220 files), `<center>`, `<tt>` (1,774), `<i>`/`<b>`, `<acronym>`, layout tables, `<hr>`, Word-export classes (`Section1`, `Bodytext`), `p.crumb` navigation, `p.author`.
- **Pre-Unicode APL is present even in valid-UTF-8 files.** `<font face="APL2741">` / `APLX Upright` / `APLNet` occur in **23** of the 295; `class="aplu"` (a style hook) in 99; entities such as `&larr;` (1,329), `&nabla;`, `&macr;` stand for APL glyphs. Only 37 files contain APL characters as literal Unicode, but entities are not counted in that figure, so the true number is higher. A file that is valid UTF-8 can still hold glyph-mapped text. These 23 should be classified with the non-UTF-8 problem files, not as "done".
- 164 of the 295 contain `<pre>`, so the `<pre>` fix applies here too.
- Volumes with the most UTF-8 HTML: v22 (69), v23 (49), v10 (36), v11 (35), v21 (24), v15 (20).

## 5. Target Markdown: the proposal

**Flavour:** Python Markdown with the extensions that Zensical already provides (`tables`, `footnotes`, `def_list`, `attr_list`, `md_in_html`, `admonition`, fenced code), **plus raw HTML where no syntax exists**. Not GFM-only: GFM lacks footnotes (in the Python Markdown sense), definition lists, attribute lists and Markdown-in-HTML.

**Per-article file**: `docs/art<ID>.md` with YAML front matter:

```yaml
---
title: Tables with calculated columns
authors: [Stevan Apter]
prefix: No Stinking Loops          # series, if any
subtitle:
volume: 25
issue: 1
page: 74
received: 2011-02-05
online: 2011-05-07
editor: Stephen Taylor
vid: 10500650                      # = art ID
description: …
source: content/printed/251/apter.htm   # provenance
converted: …                       # tool and version
---
```

Rules (draft, to become issues):

1. Head block → front matter. Drop `ul#publication` and `p#validation`. `#abstract` → a leading paragraph (or an `abstract` front-matter field plus a lead paragraph).
2. Headings: the article's `h2/h3/h4` become `##/###/####` (no H1 in the body).
3. `<pre>` → fenced code (` ``` `), whitespace exact; if it holds `<em>`/`<strong>`/`<span>`, keep it as raw `<pre>` HTML.
4. Inline `<code>` → backticks.
5. Tables → Markdown tables only when every cell is plain inline text; otherwise raw HTML `<table>` passthrough.
6. `p.caption` with `<img>` → `<figure markdown="1">` with `<figcaption>`.
7. `p.ednote` → `<p class="ednote" markdown="1">` (keep the class; style it).
8. `dl` → definition list; `cite` → `*italics*`; `dfn` → `*italics*` (not code: see the `<dfn>` finding in "Decisions").
9. References: `ol.references` + `a name="refN"` → keep as an HTML ordered list with `id`s so links like `#ref7` still work. Footnote syntax is an option.
10. MathML and SVG → raw passthrough.
11. Layout-only classes and `p.pagebreak` → dropped.
12. Links: rewrite vector.org.uk links to the new `art<ID>` URLs; keep other external links as they are.
13. Images: keep relative paths; copy images next to the page (or into a folder named by ID).

## 6. Decisions (Stephen Taylor, 2026-10-02)

1. **Converter:** custom, tree-based; pandoc at most as a cross-check.
2. **Bylines with emails:** keep. All were previously published; some will be stale.
3. **Raw HTML in the Markdown:** yes, provisionally; review after we see how much is needed.
4. **`<dfn>`:** your hypothesis was that it marks function names, so `<dfn>raze</dfn>` would become `` `raze` ``. I checked all 92 uses (24 files) and **it does not**. `<dfn>` marks the **first, defining use of a term**, and most are ordinary English or domain words, not APL names:
   - "structure-preserving", "records", "transpose", "flip" (Apter, 24:4)
   - "plaintext", "ciphertext", "cipher", "key" (Baronet, 25:1)
   - "harmonic series", "overround", "real probabilities", "magic value", "co-operators"
   - "partition", "inverted table", "triangle", "accident year", "ultimate loss", "reserving actuary"
   - "in-play", "degree of match", "CEP"
   - Some are not definitions of a term at all: "Cannon's Canon" (a citation), "Lemma 3.1", "Isomorphic vectors" (a labelled item in a proof).

   The APL/J/K/q names that do appear (`raze`, `adverb`, `conjunction`, `trains`, `Atop`, `Fork`, `fork`, `namespace`, `Isolates`, `Futures`) are *also* being defined as terms in running prose; the authors write them in prose, and put actual code in `<code>`. Backticks would make "plaintext", "partition" or "ultimate loss" look like code. None of the 92 contain `<code>`, and no `<code>` contains a `<dfn>`.

   **Rule adopted:** `<dfn>term</dfn>` → `*term*` (italics, which is the browser default rendering of `<dfn>`). Where we want to preserve the semantic, `<dfn>` can be left as raw inline HTML instead; say if you'd prefer that. If a `<dfn>` content is itself a function name, the author already wrapped it in `<code>`; there were none.
5. **`/art<ID>/` URLs during development:** accepted.

## Next steps

1. ~~Decide the questions above.~~ Done; see "Decisions".
2. Put the inventory scripts in the repo (suggest `tools/`) on a branch with an issue.
3. Write the converter for the 148 XHTML files, with a test per rule, and a report listing every article that needed raw HTML.
4. Round-trip check a pilot (25:1): text equality, link and image counts, visual comparison.
5. Check the UTF-8 `trad/` files for font-mapped APL before converting.
6. Test extensionless-file serving on GitHub Pages, and pilot Zensical on a development Pages site.
