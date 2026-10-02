**Independent survey of `sources/sjt/Vector/`**

Read `README.md`, `AGENTS.md` and `project-rules.md`. No files were written; neither `plans/` nor `reviews/` was read. Paths below are relative to `sources/sjt/Vector/`.

This is a substantial but incomplete archive: **1,485 indexed article records, of which 616 have indexed HTML/XHTML text on disk**. Its latest printed material is **Volume 26, Nos.2&3**, catalogued as September 2014; its latest recorded online article is dated **22 January 2016**. These are this copy’s endpoints, not evidence that the journal ended then.

**1. Tree and organisation**

A recursive Python `os.walk("sources/sjt/Vector")`, summing `os.path.getsize()` for each file, found **3,377 files, 399 subdirectories and 346,659,999 bytes**. Sizes below are decimal MB, rounded.

| Location | Files | MB | Purpose |
|---|---:|---:|---|
| `trad/` | 1,821 | 142.972 | Legacy articles, issue contents, images and downloads |
| `content/` | 709 | 62.282 | Newer articles and editorial workflow |
| `issues/` | 14 | 50.707 | Whole-issue downloads and issue catalogue |
| Root files | 33 | 45.004 | PHP entry points, indexes, backups, fonts and logs |
| `icons/` | 30 | 17.263 | Icons **and a large request log** |
| `varch/` | 4 | 9.005 | Binary `.w3` files and stylesheet |
| `images/` | 214 | 5.969 | Covers, faces and icons |
| `resource/` | 83 | 5.628 | Fonts, software and supplementary downloads |
| `aflat/` | 105 | 3.221 | Separate Aflat website/tutorial and downloads |
| `sandbox/` | 281 | 1.823 | Editing experiments, including TinyMCE |
| `scrap/` | 16 | 1.773 | Earlier indexes and development scripts |
| `tools/` | 13 | 0.652 | Index maintenance and diagnostic utilities |
| `css/` | 32 | 0.130 | Styles and associated assets |
| `tradarch/` | 9 | 0.128 | Alternative legacy article versions |
| `members/` | 5 | 0.050 | Membership registration application |
| `lib/` | 7 | 0.048 | PHP libraries, JavaScript and article XSLT |
| `docs/` | 1 | 0.005 | Supporting documentation |

`cgi-bin/` and `devt/` are empty.

The same inventory, grouping case-insensitive extensions, found **955 `.htm`, 5 `.html`, 8 `.xhtml`, 52 `.xml`, 40 `.pdf`, 5 `.doc`, 43 `.zip`, 33 `.php`, 141 `.js`, 65 `.css`, 846 JPEG, 591 GIF, 462 PNG and 32 WMZ files**. These are file counts, not article counts; ZIP contents are additional.

`content/printed/` groups articles by issue, usually in folders containing an eponymous `.htm` and its assets. `content/published/` holds online articles awaiting print assignment. `edit/`, `held/` and `rejected/` preserve editorial material.

**2. How article URLs worked**

The recovered code establishes this intended path:

```text
/art10500650
    → server rewrite to index.php?id=10500650
    → index.xml: dc:identifier lookup
    → selected vec:source
    → article body wrapped in site navigation and styling
```

For example, `10500650` resolves to Stevan Apter’s *Tables with calculated columns*, at `content/printed/251/apter.htm`. The source exists. Evidence: [index.xml](/Users/sjt/Projects/vec-rescue/sources/sjt/Vector/index.xml:446).

[index.php](/Users/sjt/Projects/vec-rescue/sources/sjt/Vector/index.php) requires exactly one matching identifier and prefers sources in this order: XHTML, HTML, HTTP, PDF, then an unspecified fallback.

- XHTML passes through `lib/article.xsl`, extracting the body and adjusting relative URLs.
- HTML passes through `lib/present.php`, which converts presumed Windows-1252 text, removes legacy navigation and adjusts links.
- HTTP sources redirect elsewhere; PDFs appear in an iframe.
- The compiled index combines metadata from `content/printed/` and `content/published/` with `static_index.xml`. **`NOCACHE=true` causes regeneration and writes `index.xml` on every request.** Evidence: `lib/initialise.php`, `lib/indexwrite.php`.

For legacy `?vol=…&no=…&art=…` URLs, [redirector.php](/Users/sjt/Projects/vec-rescue/sources/sjt/Vector/redirector.php) constructs `trad/v{vol}{no}/{art}.htm` and `.pdf`, looks for those source strings in the index, then redirects to `/art{id}`. Otherwise it attempts to serve the file directly.

**Missing or needing repair:**

- No `.htaccess`, `httpd.conf`, `nginx.conf`, `web.config` or `.conf` file exists in this tree. The rewrite above is an **inference from the generated URLs and PHP inputs**. The original routing of legacy queries is likewise absent.
- Routing must also cover generated `/volume/issue`, `/index` and `/inpress` links.
- Despite its “permanent move” comment, `redirector.php` does not explicitly send a 301 or terminate after its redirect. Its direct-PDF branch lacks a PDF content-type header.
- Hardcoded HTTP domains and the `<base>` URL need attention. Both URL-adjustment implementations fail to recognise some modern absolute URL forms, including HTTPS.
- Restoring the PHP requires compatibility work and DOM/XSL/mbstring support. Static generation could preserve the URLs without executing this application.

**3. Coverage**

Counts below come from direct `rdf:Description` records in [index.xml](/Users/sjt/Projects/vec-rescue/sources/sjt/Vector/index.xml), grouped by `vec:published/@volume,@issue`. “Text” means an existing local source explicitly marked `HTML` or `XHTML`; it does **not** establish completeness or correct rendering.

| Indexed-record category | Count |
|---|---:|
| Existing HTML/XHTML text | **616** |
| Existing local PDF, without HTML/XHTML | **24** |
| HTTP sources only | **6** |
| Empty source only | **1** |
| No source element | **838** |
| **Total** | **1,485** |

The text records reference **606 distinct existing files: 458 HTML and 148 XHTML**. Shared bodies and alternative sources explain why file and article counts differ.

Each table cell is **indexed records / records with text**.

| Volume | Issue 1 | Issue 2 | Issue 3 | Issue 4 |
|---|---:|---:|---:|---:|
| 1 | 13/1 | 11/0 | 8/0 | 10/0 |
| 2 | 6/0 | 9/0 | 6/0 | 4/0 |
| 3 | 10/0 | 8/0 | 4/0 | 11/0 |
| 4 | 12/0 | 7/0 | 10/0 | 3/0 |
| 5 | 12/0 | 3/0 | 11/0 | 5/0 |
| 6 | 10/0 | 7/1 | 10/0 | 11/0 |
| 7 | 9/0 | 9/0 | 12/0 | 16/2 |
| 8 | 13/0 | 18/1 | 13/0 | 10/1 |
| 9 | 16/1 | 12/1 | 21/2 | 17/1 |
| 10 | 15/13 | 19/16 | 24/19 | 23/12 |
| 11 | 25/19 | 27/12 | 19/12 | 22/2 |
| 12 | 22/6 | 19/2 | 15/3 | 19/2 |
| 13 | 17/1 | 17/1 | 17/1 | 18/1 |
| 14 | 14/1 | 17/1 | 17/1 | 17/3 |
| 15 | 21/6 | 14/6 | 13/5 | 17/9 |
| 16 | 17/8 | 14/5 | 15/11 | 15/10 |
| 17 | 15/6 | 15/9 | 15/9 | 15/7 |
| 18 | 14/6 | 16/6 | 14/7 | 16/5 |
| 19 | 14/2 | 15/7 | 14/7 | 17/5 |
| 20 | 19/11 | 15/8 | 13/3 | 15/2 |
| 21 | 17/4 | 18/8 | 15/13 | 14/13 |
| 22 | 23/21 | 16/15 | 23/23 | 19/18 |
| 23 | 27/27 | Combined with 1 | 21/18 | 21/6 |
| 24 | 14/14 | 18/18 | Combined with 2 | 19/19 |
| 25 | 12/12 | Combined with 3 | 14/14 | 15/15 |
| 26 | 22/22 | 21/21 | Combined in PDF with 2 | Absent |

Additionally, the Dyalog supplement **23:4.1 has 7/5**, and articles without print assignment have **11/11**.

[issues/index.xml](/Users/sjt/Projects/vec-rescue/sources/sjt/Vector/issues/index.xml) contains **100 issue records**, including combined issues and the supplement.

- **Whole-issue PDFs:** 21:4; 23:4 and its supplement; 24:1, 24:2&3, 24:4; 25:1, 25:2&3, 25:4; 26:1, 26:2&3.
- **Whole-issue Word document:** 23:1&2, `issues/v231.doc`; article HTML also exists.
- **Only PDF article material survives for 4:2 and 7:1**, with one indexed article PDF each; these are not complete issues.
- **Catalogue entries but no identified article bodies or issue downloads:** 1:2–4; all of volumes 2, 3 and 5; 4:1,3,4; 6:1,3,4; 7:2,3; 8:1,3. These are **25 issue groups**, obtained by testing indexed local sources and inspecting their legacy folders.
- No complete issue is exclusively PDF/DOC: every complete issue download listed above also has some article text.

There is also an unreferenced `issues/v253.pdf`. `pdfinfo` reports **two pages**, and `pdftotext` extracts no text; it should not be assumed to be another complete issue.

**4. Where this recovered archive finishes**

**Printed endpoint: Volume 26, Nos.2&3.** The catalogue calls it 26:2, September 2014, but the PDF itself repeatedly says **“Vol.26 No.2&3”**. Verify with:

```sh
pdftotext -f 1 -l 3 -layout sources/sjt/Vector/issues/v262.pdf -
```

Its editorial discusses the next issue, so this is not a declaration that publication ended. Article metadata also records online publication after the catalogue’s issue date.

**Online endpoint: 22 January 2016**, John Earnest, *A graphical sandbox for K*, `/art10501610`. This is the maximum `vec:online` timestamp in `index.xml`, independently matching `meta name="online"` in [ike.htm](/Users/sjt/Projects/vec-rescue/sources/sjt/Vector/content/published/ike/ike.htm:20).

The project README says the latest journal issue is dated 2022. This PHP copy cannot establish the journal’s actual final print issue or final online article; that requires the later archive.

**5. Defects and publication exclusions**

**Identifiers and sources**

- **One empty ID:** *Backgammon Tools in J: 2. Wastage*, `content/printed/244/peelle.htm`. Its text exists, but its article permalink is unusable.
- **No duplicate nonempty IDs:** all **1,484** nonempty identifiers are distinct eight-digit strings. This does not imply distinct article bodies.
- **Seven source paths are shared by multiple records**, including combined company news and letters pages. Preserve these relationships rather than treating them automatically as accidental duplication.
- **One empty source:** `10013780`, *First Quarter*. The similarly named `trad/v234b/firstquarter.htm` is an unindexed draft with different authorship, so it is not a verified replacement.
- **Three missing named source paths are aliases**, not missing preferred bodies:

| ID | Missing alias | Existing preferred source |
|---|---|---|
| `10002270` | `trad/v222/gitte222.htm` | `trad/v223/gitte222.htm` |
| `10003610` | `trad/v151/bob.htm` | `trad/v151/bob151_97.htm` |
| `10009240` | `trad/v212/rowan.htm` | `trad/v212/rowan2.htm` |

The redirector can still recognise these aliases through the index. Another Rowan version exists in `tradarch/`.

The issue catalogue’s `v234.pdf"` has a stray trailing quote; `issues/v234.pdf` exists. Evidence for all these findings: index XML parsed against local file existence.

**Unindexed files**

Comparing `.htm/.html/.xhtml/.pdf/.doc` paths against all article `vec:source` values found:

| Area | Unindexed candidate files | Qualification |
|---|---:|---|
| `trad/` | 189 | Includes 92 `index.htm` files; remaining files include articles, drafts, supplements and alternatives |
| `tradarch/` | 9 | Alternative legacy versions |
| `content/printed/` | 8 | Seven mathematical XHTML fragments and `242/karman/makeham.htm` |
| `content/published/` | 0 | All article text files indexed |
| `content/edit/`, `held/`, `rejected/` | 15, 5, 2 | Editorial material, not established publications |

These are **candidate files, not additional article counts**. Examples worth examining include crosswords, `trad/v234/boss.htm`, and the alternative versions under `tradarch/`.

**Encodings, Word and APL**

Strict UTF-8 decoding of the **606 indexed text files** succeeds for **443** and fails for **163**. This test does not establish the failing files’ actual encoding. `lib/present.php` assumes Windows-1252 for non-UTF-8 input.

`tools/codingprobs.txt` already records suspected character-mapped APL. Actual font-dependent examples occur in `trad/v151/susnews.htm` using `APL2741`; `css/article.css` also references `APLSans`. Byte conversion alone cannot recover the intended APL glyphs.

Of the **five loose `.doc` files**, the two `v231.doc` copies have identical SHA-256 hashes; `file` identifies `trad/v181/ed2.doc` as HTML, not Word. The remaining Word material includes the Lescasse articles. ZIP inspection additionally finds `HJV171.DOC` and the `VEC97.DOC` style document. This is not a comprehensive original-Word archive.

**Images and assets**

- Missing article images include `content/printed/262/minnowbrook/minnowbrook2013-groupphoto.jpg` and figures referenced by `trad/v104/smith104_64.htm`.
- Case mismatches exist: `appleton112_109.htm` references `appleton4_files`, while the directory is `APPLETON4_files`; this matters on case-sensitive hosting.
- The **32 WMZ files** are Office metafile assets, unsuitable as ordinary browser images. Some have GIF fallbacks: `trad/v193/langlet193_93.htm` explicitly supplies one.
- Header inspection found **26 `.jpg` files containing BMP data**, under the Ian Clark directories.
- `file` identifies `trad/v193/fig04.jpg` and `trad/v201/Sun.jpg` merely as `data`; their JPEG signatures are missing. Treat them as suspect.
- **Two files are empty:** `aflat/download/aplus-fsf-4.18.zip` and `aflat/ico/more.gif`.

**Exclude from publication**

- `events.log`, `events.20121125.log` and `icons/events.log`: **55,801,256 bytes** altogether, containing request URLs, queries, user agents and remote IP addresses. Confirmed by file sizes and log field inspection.
- `members/`: registration code processes names, addresses, email and payment choices, writes outside the web root and sends mail. No registration-record files were found inside this tree.
- Editorial `edit/`, `held/`, `rejected/` material, development tools, sandbox, backups and `info.php` should not be included in a public archive by copying the tree wholesale.

**6. Surprises and limits**

The most consequential surprises are the combined **26:2&3** issue miscatalogued as 26:2, recoverable material outside the index, shared bodies behind different article IDs, and the request log hidden in `icons/`.

Two HTTP-only index entries point to Aflat pages whose files are actually present locally. Thus “HTTP-only” does not always mean the content must be recovered elsewhere.

I did not run the PHP, verify external links, exhaustively compare alternative article versions, render every article/PDF, decode the `.w3` binaries, or establish original APL character mappings. File existence establishes recoverability, not fidelity; unindexed files require editorial identification before they can increase the coverage figures.