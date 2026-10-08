# Master plan: Vector Rescue

Goal: recover the entire *Vector* archive and republish it, with every old `art` URL (e.g. `/art10500650`) resolving.

End goal (2026-10-08): the static site built here **replaces the PHP site** at archive.vector.org.uk. With publication moved to the WordPress site, there is no case for serving the archive from a dynamic site.

Revised 2026-10-08, after the PHP site was restored at archive.vector.org.uk. Revised 2026-10-02 (evening), after the Wayback survey. Earlier revisions followed the filetree and XHTML surveys (`surveys/`). Decisions by Stephen Taylor.

## Principles

- Old URLs are the top priority; every design choice is judged against them.
- Never modify originals. `sources/` is read-only (the fetch tools alone add to `sources/wayback/` and `sources/php-site/`); all work is on derived copies in `build/`.
- The conversion is a rerunnable pipeline (`make all`). Rules are provisional, written test-first, tracked as GitHub issues, and measured by the run report on every run.
- Record provenance for every article: which source it came from, and any conversion applied.
- Overlaps between sources are decided by examining diffs, possibly article by article.
- Source defects that need judgement are corrected in a curated, visible corrections file (#23), never by guesswork in the converter.
- Do not publish private data: the request logs (`events*.log`, `icons/events.log`), `members/`, editorial `edit/`, `held/`, `rejected/` material, `info.php`, sandbox and tools.

## Where we are

Updated 2026-10-02 (late).

| | Status |
|---|---|
| Pipeline | `make all`: inventory → convert → site → report. 339 tests. |
| Articles converted | 630 of 1,503 records (1,484 in the PHP index, 19 recovered from the Wayback Machine): XHTML (vols 24–26, 26:4, in press); `trad/` HTML in UTF-8, Windows-1252 and mapped APL (vols 1–23). |
| Run report | 0 code mismatches, 0 images lost; 89 differing words, all explained (made-up tags shown as text, source typos); 158 articles also checked against the old site's own rendering. |
| Site | All 100+ issue pages, 96 with whole-issue PDFs; development build at https://5jt.github.io/vector-rescue/ (`make publish`). APL in APL387 Unicode. |
| Held back | 4 articles (#34: Langlet, De Kerf, smith104; dueren113 encoding). |
| Not online | ~840 index records with no text (mostly vols 1–21): the issue PDFs are their only source. |
| Editorial review | #34 (uncertain code points, other mappings), #35 (symbol names in braces); proposed corrections in `corrections.yaml` marked "proposed by Claude". |

## What we know (from the surveys)

- PHP tree: 1,485 index records (1,484 IDs); 616 with HTML/XHTML text, 838 metadata only. Text complete for volumes 24–26, thin before volume 15.
- The PHP tree stops at mid-2016. The Wayback Machine has the 2021 index: Vol. 26 No. 4 (9 articles more, plus our 11 "online only" ones) and 6 in-press articles to Nov 2016; captured pages for 4 more to 2018. Index captures in 2022–2025 are unchanged.
- Whole-issue PDFs for volumes 1–23 (all but 2:2 and 7:2) and 26:4 were published on vector.org.uk (uploaded to its WordPress site in 2022 and 2024); captured by the Wayback Machine (~350 MB). Captures of 3:4, 7:4 and 16:4 are truncated. The 48 indexed articles of these five issues have no page; their issue pages list them without links (#63), and the search for scans is #62.
- 443 of the 606 indexed text files are valid UTF-8; 163 are not. APL in older articles is often font-mapped (APL2741, APL385), which byte conversion alone cannot fix; the old site listed suspects in `tools/codingprobs.txt`.
- **The restored PHP site** (archive.vector.org.uk, under Jake Jacob's control; restored by 2026-10-08) runs a newer copy of the tree than ours, to November 2016. Its `index.xml` has 1,499 records against our 1,484: the 15 more are 26:4 and six in-press articles, which we otherwise hold only as Wayback renderings. It serves 29 source files our tree lacks (`content/printed/264/`, `content/printed/271/`, `trad/v143/odbc143.htm`). It lacks the four 2017–18 articles we recovered from Wayback, and holds no scans for Vols 1–21. Defects (broken current-issue link, debug trace, wrong base URL) are reported in #105. `vector.org.uk/art…` still returns 404.
- Per-article PDFs in `trad/` (24 records) are 300 dpi colour scans, better than the 200 dpi 1-bit issue scans; both sides hold them.
- On GitHub Pages, `/art<ID>` redirects (301) to `/art<ID>/`; a file with no extension is served for download. Exact extensionless URLs need other hosting.

## Blocking issues

| # | Blocker | Blocks | Owner / action |
|---|---|---|---|
| B1 | **A copy of the WordPress database export** | Phase 8 only: articles published on WordPress (2017–2022) | Await Paul Grosvenor; ask Jake Jacob as a second route. **Fallback:** ~229 WordPress posts and pages captured by the Wayback Machine (rendered HTML, so the export remains preferable). |
| B2 | **Replacing the restored PHP site at `archive.vector.org.uk`** with the static build (Jake Jacob's server; relates to eventual integration with the BAA domain, #105) | Publishing under the original hostname | Jake, with the BAA (Paul). Not needed until Phase 6. |

## Phases

### 0. Retrieve sources: PHP tree done; Wayback in progress; WordPress export outstanding

- PHP filetree: `sources/sjt/Vector` (338 MB, not in git).
- Wayback Machine: fetch the 2021 index, the 19 newer articles and their images, the issue PDFs, and the captured renderings of articles we cannot convert directly (#24, `make fetch-wayback`).
- Restored PHP site: its indexes, the 29 sources our tree lacks and their images, and its rendering of each linked article (#104, `make fetch-php`, `sources/php-site/`). To do: make the inventory prefer these over the 2016 copies, so the 15 newer records convert from XHTML.
- Still wanted for Phase 8 (B1): the WordPress export.
- Decide where `sources/` is archived safely and publicly. **Before publishing, exclude the logs and `members/`.**

### 1–2. Surveys and groundwork: done

Filetree surveys, the XHTML target survey, the Zensical trial, the canonical inventory (`build/inventory.json`), the run report (#10). Wayback survey: `surveys/wayback-survey.md`.

### 3. Convert what the PHP tree holds as text: done

- XHTML (#1–#8); valid-UTF-8 `trad/` HTML (#21); non-UTF-8, decoded as Windows-1252 and checked against the old site's rendering (#27); mapped APL via `mappings/apl2741.tsv` (#33).
- Curated corrections for source defects (#23, `corrections.yaml`); editorial questions in #34, #35.

### 4. Generate the site and review it on GitHub Pages: done, ongoing

- Zensical build with issue pages, home page, article header, APL font (#9). Development site on GitHub Pages for review only; production hosting is Phase 5.
- Still to add: whole-issue PDFs on every issue page (#26); an "In press (never printed)" section; a statement of what is missing; author pages and search tuning if cheap.

### 5. Widen the content

- **Wayback-recovered articles:** done (#25): Vol. 26 No. 4, in-press articles, 2017–18 additions.
- **Mapped APL:** done (#33) apart from the articles in #34.
- **Volumes 1–21 from the issue PDFs:** check whether they are scans or text; if text, a source for the 838 metadata-only records; otherwise at least every issue is readable as a PDF.
- **Word documents:** the five `.doc` files (one is really HTML); any further Word issues; Ian Clark's converted versions if they can be found.
- **Unindexed material:** review the unindexed candidate files in `trad/` and `content/`.
- **Assets:** convert `.wmz` images, repair images with wrong formats, the 18 images not found.

### 6. Hosting and domain, after B2

The target is archive.vector.org.uk, replacing the PHP site.

- GitHub Pages with a custom domain: `/art<ID>` reaches the page through one redirect.
- Dyalog's Gitea, if it can serve static output.
- HTTPD on dyalog.com: full control of rewrites; exact `/art<ID>` and the old `?vol=&no=&art=` URLs. The fallback if one redirect is not acceptable.
- Redirects at the other hosts that inbound links use (`vector.org.uk/art…`, `vector.johnbutlerassociates.co.uk/art…`).

### 7. Verify and hand over

- Test every required `art` URL, plus the URLs seen in `events.log`, the README and the Wayback captures.
- Document how to rebuild the site and add future material.
- Agree long-term ownership with the BAA, and where the source archive lives.

### 8. Later, separate phase: WordPress content

After the archive is replaced. Publication on the WordPress site appears to have ended in 2022, so there is a case for exporting its content (B1, or its Wayback fallback) and adding it to the archive: 2017–2022 articles, with duplicates of PHP-era articles compared and ruled article by article.

## Open questions

- Which hosting option in the end? (Phase 6, after B2.)
- Who controls the vector.org.uk DNS and the WordPress site?
- Licensing and author permissions for republication.
- Where should `sources/` live safely, and what is stripped before it goes public?
- Are the issue PDFs from vector.org.uk scans or text? (Samples from 1984 and 1995 have a text layer.)
