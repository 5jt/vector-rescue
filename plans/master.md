# Master plan: Vector Rescue

Goal: recover the entire *Vector* archive and republish it, with every old `art` URL (e.g. `/art10500650`) resolving.

Revised 2026-10-02 (evening), after the Wayback survey. Earlier revisions followed the filetree and XHTML surveys (`surveys/`). Decisions by Stephen Taylor.

## Principles

- Old URLs are the top priority; every design choice is judged against them.
- Never modify originals. `sources/` is read-only (the fetch tool alone adds to `sources/wayback/`); all work is on derived copies in `build/`.
- The conversion is a rerunnable pipeline (`make all`). Rules are provisional, written test-first, tracked as GitHub issues, and measured by the run report on every run.
- Record provenance for every article: which source it came from, and any conversion applied.
- Overlaps between sources are decided by examining diffs, possibly article by article.
- Source defects that need judgement are corrected in a curated, visible corrections file (#23), never by guesswork in the converter.
- Do not publish private data: the request logs (`events*.log`, `icons/events.log`), `members/`, editorial `edit/`, `held/`, `rejected/` material, `info.php`, sandbox and tools.

## Where we are

| | Status |
|---|---|
| Pipeline | `make all`: inventory → convert → site → report. 273 tests. |
| Articles converted | 432 of 1,484 indexed: all XHTML (vols 24–26, online-only) and the valid-UTF-8 `trad/` HTML (vols 1–23). |
| Run report | 0 code mismatches, 0 images lost; 36 differing words, all explained (made-up tags shown as text, source typos, check artefacts). |
| Site | Issue pages for all 100 catalogued issues; development build at https://5jt.github.io/vector-rescue/ (`make publish`). |
| Held back | 21 `trad/` articles with mapped APL; 162 non-UTF-8 `trad/` articles; 24 PDF-only articles; 838 metadata-only records. |
| Sources | PHP tree (`sources/sjt/Vector`, to mid-2016); Wayback captures in `sources/wayback/` (#24). |

## What we know (from the surveys)

- PHP tree: 1,485 index records (1,484 IDs); 616 with HTML/XHTML text, 838 metadata only. Text complete for volumes 24–26, thin before volume 15.
- The PHP tree stops at mid-2016. The Wayback Machine has the 2021 index: Vol. 26 No. 4 (9 articles more, plus our 11 "online only" ones) and 6 in-press articles to Nov 2016; captured pages for 4 more to 2018. Index captures in 2022–2025 are unchanged.
- Whole-issue PDFs for volumes 1–23 (all but 2:2 and 7:2) and 26:4 were published on vector.org.uk (uploaded to its WordPress site in 2022 and 2024); captured by the Wayback Machine (~350 MB). Captures of 3:4, 7:4 and 16:4 are truncated.
- 443 of the 606 indexed text files are valid UTF-8; 163 are not. APL in older articles is often font-mapped (APL2741, APL385), which byte conversion alone cannot fix; the old site listed suspects in `tools/codingprobs.txt`.
- On GitHub Pages, `/art<ID>` redirects (301) to `/art<ID>/`; a file with no extension is served for download. Exact extensionless URLs need other hosting.

## Blocking issues

| # | Blocker | Blocks | Owner / action |
|---|---|---|---|
| B1 | **A copy of the WordPress database export** | Articles published on WordPress (2017–2022), and the old-versus-WP duplicate comparison | Await Paul Grosvenor; ask Jake Jacob as a second route. **Fallback:** ~229 WordPress posts and pages captured by the Wayback Machine (rendered HTML, so the export remains preferable). |
| B2 | **Use of the `archive.vector.org.uk` URL** (DNS control; today it points at WordPress) | Publishing under the original hostname | BAA (Paul). Not needed until Phase 5. |

## Phases

### 0. Retrieve sources: PHP tree done; Wayback in progress; WordPress export outstanding

- PHP filetree: `sources/sjt/Vector` (338 MB, not in git).
- Wayback Machine: fetch the 2021 index, the 19 newer articles and their images, the issue PDFs, and the captured renderings of articles we cannot convert directly (#24, `make fetch-wayback`).
- Still wanted (B1): the WordPress export.
- Decide where `sources/` is archived safely and publicly. **Before publishing, exclude the logs and `members/`.**

### 1–2. Surveys and groundwork: done

Filetree surveys, the XHTML target survey, the Zensical trial, the canonical inventory (`build/inventory.json`), the run report (#10). Wayback survey: `surveys/wayback-survey.md`.

### 3. Convert what the PHP tree holds as text: done for UTF-8; non-UTF-8 next

- Done: XHTML (#1–#8) and valid-UTF-8 `trad/` HTML (#21).
- Next: the 163 non-UTF-8 `trad/` articles, decoded as Windows-1252 and checked against the old site's own captured rendering (#27).
- Corrections file for source defects (#23).

### 4. Generate the site and review it on GitHub Pages: done, ongoing

- Zensical build with issue pages, home page, article header, APL font (#9). Development site on GitHub Pages for review only; production hosting is Phase 5.
- Still to add: whole-issue PDFs on every issue page (#26); an "In press (never printed)" section; a statement of what is missing; author pages and search tuning if cheap.

### 5. Widen the content

- **Wayback-recovered articles:** Vol. 26 No. 4, the in-press articles and the 2017–18 additions (#25), using the 2021 index for metadata.
- **WordPress content (B1, or its Wayback fallback):** 2017–2022 articles; compare duplicates with the PHP-era versions and rule article by article.
- **Mapped APL:** the 21 held-back `trad/` articles and any others found; APL2741 and APL385 mappings, with human review.
- **Volumes 1–21 from the issue PDFs:** check whether they are scans or text; if text, a source for the 838 metadata-only records; otherwise at least every issue is readable as a PDF.
- **Word documents:** the five `.doc` files (one is really HTML); any further Word issues; Ian Clark's converted versions if they can be found.
- **Unindexed material:** review the unindexed candidate files in `trad/` and `content/`.
- **Assets:** convert `.wmz` images, repair images with wrong formats, the 18 images not found.

### 6. Hosting and domain, after B2

- GitHub Pages with a custom domain: `/art<ID>` reaches the page through one redirect.
- Dyalog's Gitea, if it can serve static output.
- HTTPD on dyalog.com: full control of rewrites; exact `/art<ID>` and the old `?vol=&no=&art=` URLs. The fallback if one redirect is not acceptable.
- Redirects at the other hosts that inbound links use (`vector.org.uk/art…`, `vector.johnbutlerassociates.co.uk/art…`).

### 7. Verify and hand over

- Test every required `art` URL, plus the URLs seen in `events.log`, the README and the Wayback captures.
- Document how to rebuild the site and add future material.
- Agree long-term ownership with the BAA, and where the source archive lives.

## Open questions

- Which hosting option in the end? (Phase 6, after B2.)
- Who controls the vector.org.uk DNS and the WordPress site?
- Licensing and author permissions for republication.
- Where should `sources/` live safely, and what is stripped before it goes public?
- Are the issue PDFs from vector.org.uk scans or text? (Samples from 1984 and 1995 have a text layer.)
