# Survey: what the Wayback Machine holds

Surveyed by Claude on 2026-10-02 from the Wayback Machine's CDX index, which lists every captured URL. Nothing was downloaded in bulk for this survey; a few files were fetched to check them.

Queries (reproducible):

    https://web.archive.org/cdx/search/cdx?url=archive.vector.org.uk/*&output=json&fl=timestamp,original,mimetype,statuscode,digest&collapse=urlkey
    https://web.archive.org/cdx/search/cdx?url=archive.vector.org.uk/index.xml&output=json
    https://web.archive.org/cdx/search/cdx?url=vector.org.uk/wp-content/*&output=json&fl=timestamp,original,mimetype,statuscode,length&collapse=urlkey
    https://web.archive.org/cdx/search/cdx?url=vector.org.uk/*&output=json&collapse=urlkey&filter=statuscode:200&filter=mimetype:text/html&from=20170101

A capture is fetched unmodified by adding `id_` to its timestamp, e.g. `https://web.archive.org/web/20210830085903id_/http://archive.vector.org.uk/index.xml`. Some captures come back gzip-compressed.

## Short answers

1. **The archive did not stop in mid-2016.** A capture of `index.xml` (30 Aug 2021) has 1,500 records, 15 more than our copy: Vol. 26 No. 4 was assembled (9 new articles, plus the 11 we had as "online only"), and 6 "in press" articles for Vol. 27 were added May–Nov 2016. Pages for 4 more articles (IDs 10501740–10501770, 2017–2018) were captured although no captured index lists them. Captures of `index.xml` in 2022–2025 are identical to 2021's.
2. **Those 19 articles can be recovered** from their captured `art` pages, which hold the article in a clean `div#article`; most of their images were captured too. Their `.htm` sources were not.
3. **186 more captured `art` pages** are for articles we have but have not converted: 162 non-UTF-8 `trad/` articles, which the old site served transcoded to UTF-8 (a cross-check for our own conversion; mapped APL is still wrong in them), and 24 with only a PDF source.
4. **Whole-issue PDFs from 1984 onwards,** published on vector.org.uk: they were uploaded to its WordPress site under `wp-content/uploads/2022/07/` (`VOL.1-NO.1-MAY-1984.pdf` …) and `2024/06/`; 99 PDF captures, about 350 MB: every issue of volumes 1–23 except **2:2 and 7:2**, `Vector264.pdf` (Vol. 26 No. 4, missing from our tree), and copies of the 24–26 PDFs we have.
5. **WordPress posts (2017 on):** about 229 captured posts and pages (some duplicated with `-2` slugs), plus author, tag and category listings (`/category/v26no4/`, `/category/in-press/`, …). A fallback for blocker B1 if the database export never arrives.

## 1. archive.vector.org.uk

3,580 distinct URLs captured. By kind (status 200 unless noted):

| Kind | Captured |
|---|---:|
| `art` pages | 687 (plus 17 redirects, 7 not found) |
| `trad/` files | 739 (151 not found) |
| `content/` files | 428 |
| Issue pages (`/24/1` …) | 101 |
| `issues/` PDFs | 12 (v214 to v262; no v263/v264) |
| `index.xml` | 9 captures, 2021-08-30 to 2025-05-02 |

Of the 704 `art` IDs captured, 646 are in our index (432 converted, 21 held back for mapped APL, 193 not converted). The other 58 are mostly artefacts: an ID with a footnote number glued on (`art100072301`). **19 are genuine new articles:**

| ID (first capture) | Captured | Issue | Online | Title | Authors |
|---|---|---|---|---|---|
| [10501530](https://web.archive.org/web/20170826042448/http://archive.vector.org.uk/art10501530) | 20170826 | 26:4 | 2016-05-05 | 4xTra Alliance industry news | Chris Hogan |
| [10501540](https://web.archive.org/web/20160524033058/http://archive.vector.org.uk/art10501540) | 20160524 | 26:4 | 2016-05-05 | Dyalog Ltd industry news | Morten Kromberg |
| [10501570](https://web.archive.org/web/20170826042452/http://archive.vector.org.uk/art10501570) | 20170826 | 26:4 | 2016-05-05 | Chairman’s Report August 2015 | Paul Grosvenor |
| [10501620](https://web.archive.org/web/20160524034005/http://archive.vector.org.uk/art10501620) | 20160524 | 26:4 | 2016-05-05 | Kx Systems 2015 News | Abby Gruen |
| [10501630](https://web.archive.org/web/20170826042452/http://archive.vector.org.uk/art10501630) | 20170826 | 26:4 | 2016-05-05 | British APL Association AGM - Friday 29th May 2015 | Chris Hogan |
| [10501640](https://web.archive.org/web/20160921031441/http://archive.vector.org.uk/art10501640) | 20160921 | 26:4 | 2016-05-05 | APL and partitioned data | Jonathan Barman |
| [10501650](https://web.archive.org/web/20170826042450/http://archive.vector.org.uk/art10501650) | 20170826 | 26:4 | 2016-05-05 | Editorial | John Jacob |
| [10501660](https://web.archive.org/web/20170826042448/http://archive.vector.org.uk/art10501660) | 20170826 | 26:4 | 2016-05-05 | Optima Systems Ltd - Industry News | Paul Grosvenor |
| [10501670](https://web.archive.org/web/20170826042449/http://archive.vector.org.uk/art10501670) | 20170826 | 26:4 | 2015-08-05 | APL2000 Update |  |
| [10501680](https://web.archive.org/web/20160921031338/http://archive.vector.org.uk/art10501680) | 20160921 | in press | 2016-05-17 | Optima welcomes James Heslip | James Heslip |
| [10501690](https://web.archive.org/web/20170826042456/http://archive.vector.org.uk/art10501690) | 20170826 | in press | 2016-06-10 | Minutes of Annual General Meeting 2016 | Stephen Taylor |
| [10501700](https://web.archive.org/web/20160921031349/http://archive.vector.org.uk/art10501700) | 20160921 | in press | 2016-09-01 | Taming statistics with limited-domain operators | Stephen Mansour |
| [10501710](https://web.archive.org/web/20160921031448/http://archive.vector.org.uk/art10501710) | 20160921 | in press | 2016-08-30 | Writing a utility function | Dan Baronet |
| [10501720](https://web.archive.org/web/20170826042457/http://archive.vector.org.uk/art10501720) | 20170826 | in press | 2016-10-31 | J-ottings 59 Love Actuarily... | Norman Thomson |
| [10501730](https://web.archive.org/web/20170826042433/http://archive.vector.org.uk/art10501730) | 20170826 | in press | 2016-11-01 | AntLang – A modern APL system | Anthony Cipriano |
| [10501740](https://web.archive.org/web/20170826042458/http://archive.vector.org.uk/art10501740) | 20170826 | not in any captured index | | (title from the page, once fetched) | |
| [10501750](https://web.archive.org/web/20170826042458/http://archive.vector.org.uk/art10501750) | 20170826 | not in any captured index | | (title from the page, once fetched) | |
| [10501760](https://web.archive.org/web/20180620112817/http://archive.vector.org.uk/art10501760) | 20180620 | not in any captured index | | (title from the page, once fetched) | |
| [10501770](https://web.archive.org/web/20180831213927/http://archive.vector.org.uk/art10501770) | 20180831 | not in any captured index | | (title from the page, once fetched) | |

The 2021 index also moves our 11 "online only" articles into 26:4 (source paths `content/printed/264/…`), and the in-press articles' sources are in `content/printed/271/`. Captured images exist for most of them (`content/printed/264/…`, `content/printed/271/…`), including articles not yet listed (`271/dyalogum16/`, `271/ltl_automata/`).

## 2. vector.org.uk (the WordPress site, from 2017)

Two hosts were captured: `archive.vector.org.uk` served the PHP site (captured 2011–2025; everything above in §1 comes from it), and `vector.org.uk` served a Google Sites page in 2016 and the WordPress site from 2017. Only the PDFs and posts below come from `vector.org.uk`.

- Issue PDFs as above, uploaded in July 2022 (volumes 1–23) and June 2024 (24–26). Some predate their upload: `Vector264.pdf` was generated on 24 June 2016, in the PHP era; the 24–26 files are byte-identical to the PHP tree's `issues/`. Missing from the captures: Vol. 2 No. 2 and Vol. 7 No. 2; only truncated captures of 3:4, 7:4, 16:4 and 21:4 (8:1 was recovered from another capture).
- About 229 posts and pages captured between 2019 and 2026, with listings by author, tag and category; categories include `v25no3`, `v26no2`, `v26no4`, `in-press`, `journal`.
- The Google Sites period (2016) was not examined.

## Not found

- Source files (`.htm`) for anything added after mid-2016.
- An index newer than November 2016.
- PDFs of 2:2 and 7:2.
- Not yet checked: whether the issue PDFs are scans or contain text.

## Next steps (agreed 2026-10-02)

1. This survey.
2. Download the 19 newer articles' pages and images into a read-only `sources/wayback/`, and convert them.
3. Download the issue PDFs and link them from issue pages.
4. Download the 162 captured renderings of non-UTF-8 `trad/` articles, as a cross-check for their conversion.
5. Keep the WordPress captures as the fallback for B1.
