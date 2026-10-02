# Survey of the PHP filetree (`sources/sjt/Vector`)

Surveyed by Claude. Read-only: nothing under `sources/` was modified. Counts come from scripts that parsed `index.xml` and walked the tree; where I only inferred something, it is marked **(inferred)**.

## Short answers

**When does the archive finish?**

| Measure | Answer |
|---|---|
| Last printed issue | **Vol. 26 Nos. 2&3**, catalogued as 26:2, September 2014. `issues/index.xml` says 26:2, but the masthead of `issues/v262.pdf` reads "Vol.26 No.2&3" (corrected after Codex's review; verified with `pdftotext`). The PDF is dated 1 Mar 2015 on disk. |
| Last article put online | **22 Jan 2016**: John Earnest, "A graphical sandbox for K" (`art10501610`). This is the maximum `vec:online` date in `index.xml` (105 entries carry one). My first draft said 22 Mar 2016, which was only the file mtime of `taylor.htm` (a re-edit of an older article, ID `10500550`); corrected after Codex's review. Eleven online-only articles were published Apr 2015 – Jan 2016, with IDs up to `10501610`. |
| Last change to the tree | `index.xml` on 2 Jun 2016. `events.log` ends 29 May 2016. Draft files in `content/edit/` are dated up to Mar 2016. |
| Draft material | `content/edit/` and `content/held/`, with files dated up to Feb 2016. Not in the index. |

Nothing after mid-2016 is in this tree. The README says the latest issue is dated 2022, so the 2014–2022 gap has to come from the WordPress export, or from PDFs not in the PHP tree. I found no issue after 26.2 anywhere in the PHP tree.

**What was lost, and what survives?** The index lists **1,485 articles** (1,484 with an ID). Only **629 of the 1,474 with volume/issue data have a source file** that exists on disk. The rest are metadata only. Coverage is uneven:

| Volumes | Online text |
|---|---|
| 1–9 (1984–1994, **inferred** from issue dates) | Almost none: 14 of 333 entries. |
| 10–11 | 60/81 and 45/93. |
| 12–14 | 13/75, 4/69, 6/65. |
| 15–21 | 20–60% (26/65, 34/61, 31/60, 25/60, 21/60, 27/62, 40/64). |
| 22–23 | 77/81, 70/76. |
| 24–26 | **100%** (51/51, 41/41, 43/43). |

Full per-issue PDFs exist for only 12 of the 100 issues listed in `issues/index.xml`: 21.4, 23.1 (a `.doc`), 23.4, the 23.4 Dyalog@25 supplement, 24.1, 24.2, 24.4, 25.1, 25.3, 25.4, 26.1 and 26.2. All of these are 2005 or later. **Issues 1.1 to 21.3 (1984–2005) survive only as the article-level HTML in `trad/`, and often not even that.** Possible further sources for them are the old Word files and the Wayback Machine.

## Layout

Total: 3,377 files, about 338 MB.

| Path | Files | Size | What it is |
|---|---|---|---|
| `index.php`, `redirector.php`, `lib/`, `members/`, `tools/`, `scrap/`, `sandbox/` | 33 PHP files | small | The application. See "How URLs worked". |
| `index.xml` | 1 | 650 KB | **The master index.** RDF/XML, 1,485 `rdf:Description` elements. Last written 2 Jun 2016. |
| `static_index*.xml` | 8 variants | ~580 KB | Older snapshots, 2010–2015 (dated 24 Dec 2010 to 19 Mar 2015). Useful for history and diffs. |
| `issues/` | 14 | 48 MB | Issue PDFs, one `.doc` and `issues/index.xml` (100 issues, 1984-05 to 2014-09). |
| `trad/` | 1,821 | 140 MB | **"Traditional" articles**: 95 `vNNN` directories from `v011` (Vol. 1 No. 1) to `v234`, HTML plus images. |
| `tradarch/` | 9 | 144 KB | Small leftover archive of six issues' folders: `v101 v154 v163 v184 v212 v221`. |
| `content/printed/` | — | — | XHTML article folders for printed issues 24.1–26.2: `241 242 244 251 253 254 261 262`. |
| `content/published/` | — | — | 11 online-only articles, 2015–16. |
| `content/edit/`, `content/held/`, `content/rejected/` | — | — | Drafts, held and rejected submissions. Not in the index. `rejected/` holds submissions that were never published. |
| `content/` total | 709 | 61 MB | |
| `varch/` | 4 | 8.6 MB | Three `VARCH*.w3` files from Nov 2010, apparently Vector archive dumps **(inferred; not opened)**. |
| `aflat/` | 105 | 3.3 MB | A separate sub-site for A♭ (an APL-like language) with docs, downloads and manuals. |
| `resource/` | 83 | 5.5 MB | Fonts and downloads: APL385, apl2741, `aplcode.zip`. |
| `css/`, `images/`, `icons/` | 276 | 23 MB | Site chrome. |
| `events.log`, `events.20121125.log` | 2 | 38 MB | **Web server request logs**, in XML. These are useful: they list which old URLs people actually requested (including 404s). |
| `cgi-bin/`, `devt/` | 0 | 0 | Empty. |

By file type: 954 `.htm`, 831 `.jpg`, 591 `.gif`, 461 `.png`, 141 `.js`, 65 `.css`, 52 `.xml`, 43 `.zip`, 40 `.pdf`, 33 `.php`, 32 `.wmz`, 26 `.txt`, 25 `.db` (probably `Thumbs.db`), 8 `.xhtml`.

## How URLs worked

I read `index.php` and `redirector.php`.

1. **`/artNNNNNNNN` requests.** `index.php` reads `?id=NNNNNNNN`. It looks up `dc:identifier == id` in `index.xml`, picks the best source by preference XHTML, HTML, HTTP, PDF, and then:
   - XHTML: transforms it with `lib/article.xsl`.
   - HTML: wraps it in chrome via `presentArticle()`.
   - PDF: serves it in an iframe.
   - HTTP: redirects to the external URL.
   - No source: shows "Sorry, we don't have this article online".
2. **Legacy `?vol=&no=&art=` URLs** go to `redirector.php`. It matches `trad/vVVNN/ART.htm` or `.pdf` against `vec:source`, then sends a **Location: `/artNNNNNNNN`** redirect. If there is no match it serves the file directly, or returns a 404.
3. **Not in the tree: the rewrite rule that turns `/artNNN` into `index.php?id=NNN`.** I found no `.htaccess` or Apache config. The code only comments on `art…` links in `lib/present.php:48`. **We need that rule from the old server (or to infer it).** Without it, we can only say that `/art<ID>` is the URL form and that `<ID>` is `dc:identifier`.

**The `art` URL space is therefore the 1,484 IDs in `index.xml`.** Two of the three namespaces are visible in the IDs:

| ID prefix | Count |
|---|---|
| `1000…` | 997 |
| `1001…` | 342 |
| `1050…` | 145 |

The highest ID is `10501610`. The example from the README, `art10500650`, falls in the `1050` group, which is the 2008–2016 era, so it has a source file. **I have confirmed it: `art10500650` is Stevan Apter's "Tables with calculated columns" (25:1, p.74), source `content/printed/251/apter.htm`.** Entries also carry `vec:received` and `vec:online` dates, which should help to date the online-only articles. The string `art10500650` does not appear in `events.log`.

## Findings and problems

- **One entry has an empty identifier:** `content/printed/244/peelle.htm`, "Backgammon Tools in J: 2. Wastage" (`<dc:identifier />`). It has no `art` URL and needs one, or a manual lookup in `static_index*.xml`.
- **10 `vec:source` paths in `index.xml` don't exist on disk**, including `trad/v222/gitte222.htm` and `trad/v151/bob.htm` (plus one blank path). Six sources are external `http://` links (e.g. `juggle.gaertner.de/bnp/…`), which have probably rotted.
- **Online-only articles have no `vec:published` element** (11 entries), so they don't belong to an issue. They would need an issue-less home or a date.
- **Orphans: 218 files have no `index.xml` entry.** 25 `.htm` and 7 `.xhtml` under `content/`, and 182 `.htm`, 4 `.doc` and 3 `.pdf` under `trad/`. Some are probably image pages or alternates, but some may be unindexed articles. They need checking.
- **Issue numbering oddities:** `23:4.1` (the Dyalog@25 supplement) is a string, not an integer. The issues 23:1&2, 24:2&3, 25:2&3 and 26:2&3 are combined issues. This will matter for URL and issue-page generation.
- **Mixed encodings in `trad/`.** Of the `.htm` files there, **327 declare UTF-8, 25 declare windows-1252 or ISO-8859-1, and 71 declare no charset at all.** The no-charset files need testing. This is the main character-encoding risk, in addition to the Word-era APL font problem.
- **Five `.doc` files** are in the tree: `issues/v231.doc` (listed in `issues/index.xml`), `trad/v231/v231.doc`, `trad/v213/lescasse_213.doc`, `trad/v214/lescasse214.doc` and `trad/v181/ed2.doc`. Four of them are among the orphans (the `trad/` ones, which the earlier count shows as 4 unreferenced `.doc`). These may use the pre-Unicode APL fonts mentioned in the README. **I did not open them.** Ian Clark's converted Unicode versions are not obviously present.
- **32 `.wmz` files** (compressed Windows metafiles) are in the images. Browsers can't display them. They need conversion.
- **Fonts:** `Apl385.ttf`, `apl385.eot`, `apl2741*.ttf` in `resource/`. Useful for rendering and for mapping old encodings.
- **Privacy:** `members/register.php` and the logs contain IP addresses and user agents. Request logs total about 55.8 MB: `events.log`, `events.20121125.log` **and a third one, `icons/events.log` (17 MB, Dec 2013), which I missed and Codex found**. None should be published as it stands. It is also a useful source of lost-link data.
- **Duplicates:** `tools/dupvids.php` suggests duplicate IDs were a known problem. In `index.xml` all 1,484 IDs are unique.

## Cross-check with Codex

`reviews/filetree-survey-codex.md` is an independent survey of the same tree. It agrees with my totals (3,377 files, 1,485 records, 838 with no source, 1,484 unique IDs, one empty ID, the 100-issue catalogue, no rewrite config). Differences, and what I did about them:

- Last printed issue and last online date: Codex was right on both; corrected above.
- `icons/events.log`: Codex found a third log; added above.
- Source files missing from disk: Codex shows that three of them are just aliases for files that exist (`trad/v222/gitte222.htm` is at `trad/v223/`, `trad/v151/bob.htm` is `bob151_97.htm`, `trad/v212/rowan.htm` is `rowan2.htm`).
- Encodings: my 327/25/71 counts only what the files *declare*. Codex strictly decoded the 606 indexed text files: **443 are valid UTF-8 and 163 are not**. Use Codex's figure.
- Unindexed files: my 218 and Codex's 189 (trad) + 9 + 8 + others differ in what they count; Codex excludes nothing but notes that 92 of the `trad/` ones are `index.htm`. Treat both as candidates, not article counts.
- Codex also found: `ed2.doc` is HTML, not Word; the two `v231.doc` copies are identical; 26 `.jpg` files hold BMP data; some JPEGs have no valid signature; two zero-byte files; case-mismatched image directories (a problem on case-sensitive hosting); `issues/v253.pdf` is an unreferenced 2-page file; `redirector.php` doesn't send a 301.

## Not yet checked

- Whether the other README URLs resolve through `index.xml` (`art10500650` does).
- Contents of `varch/*.w3`, `scrap/` indexes (`arcindex.xml`, `flagged_index.xml`) and `tools/` scripts, which may hold clean-up notes.
- The 838 entries with no source: which issues they belong to, and whether PDFs of those issues could stand in.
- Whether `trad/` HTML includes whole-issue pages as well as articles.
- The `.doc` files' fonts, and whether their text duplicates `trad/` HTML.
- Differences between `index.xml` and the `static_index*.xml` snapshots (articles removed or renumbered).
- File dates: I took the preserved file mtimes at face value; they look genuine (2010–2016), not copy dates.

## Suggested next steps

1. Recover or reconstruct the web server rewrite rule for `/art<ID>`.
2. Extract a CSV from `index.xml`: ID, title, authors, volume, issue, page, source, format, exists. Make it the canonical inventory.
3. Validate every `art` URL in the README and in `events.log` against that table to find which old requests the new site must satisfy.
4. Check the orphan files and the 838 metadata-only entries.
5. Sample the three `trad/` encoding groups.
6. Try the `.doc` files.
7. Compare with the WordPress export when it arrives, to see what covers 2014–2022.
