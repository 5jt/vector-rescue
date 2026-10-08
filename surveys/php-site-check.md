# The restored PHP site against our build

Issue #104, 2026-10-08. Claude, for Stephen Taylor.

The PHP site was restored at https://archive.vector.org.uk. `make fetch-php` saved its indexes, the sources our tree lacks, and its own page for each of the 661 articles its full index links (`sources/php-site/`, with a manifest). `vecrescue fetch-php --check` compares those pages with `build/site` and writes `build/php-check.json`. The word check is the one the run report uses for Wayback captures (`report.capture_check`).

## What was fetched

- `index.xml` (1,499 records) and `issues/index.xml` (with 26:4).
- All 29 source files our tree lacks: `content/printed/264/`, `content/printed/271/`, `trad/v143/odbc143.htm`, and their images.
- Eight files failed with 404. They are missing on the server too: three `pdf.css` stylesheets, a favicon, and four "alt" figures that `content/printed/264/ike/` links but does not hold.
- All 661 article pages (23 MB in all).

## The pages, by kind

| PHP site | Our build | Pages |
|---|---|---:|
| Text | Article page | 626 |
| Text | Held back (#34: Dueren, De Kerf, two with mapped APL) | 4 |
| Per-article PDF in a frame | Stub with a page link | 24 |
| No article (external links: juggle.gaertner.de, dyalog.com, …) | Stub | 7 |

Every article the PHP site shows as text, we show as text, except the four held back.

## Word check on the 626

1,096,082 words; 5,191 differ (0.5%). Sorted by hand-checked kinds:

| Kind | Words | Articles |
|---|---:|---:|
| The PHP site shows mapped APL as Windows-1252 (`Œio„0` for `⎕io←0`, `‡` for `↓`, `½` for `⍴`) or U+FFFD, where we decode it | ~3,900 | ~100 |
| Subtitles and lead lines: shown on one side only, or in a different place | ~400 | ~75 |
| Made-up tags (`<condition>`, `<wsid>`, `<esc>`): the PHP site drops them as HTML; we show them as text | ~150 | ~10 |
| The PHP site shows stray HTML and CSS as text (`<!-- body {font-family…`, a DOCTYPE) | ~200 | 5 |
| Figure captions in a different order | ~50 | 3 |
| Words run together on the PHP site (`applications.Even`) | ~30 | 1 |
| Email addresses differ | 5 | 5 |

### Faults on our side

- **10003100, Eastwood, The Toronto Toolkit (10:4).** Five characters in a second code page are left unmapped: `à` (→), `1Ê2` (probably 1÷2), `1îA[ôA]` (1↑A[⍒A]), and `ŒMONITOR` and `ŒFI` (⎕). The PHP site garbles them too. `corrections.yaml` released the article as "already Unicode APL; nothing left to map", which is wrong. It needs a correction entry.
- **Source chrome kept** in three articles: breadcrumbs (`www.vector.org.uk > archive > Vol.21 > No.1`, 10003740) and VARCH footers ("webpage generated: 18 October 2006 … VARCH43", 10001530 and 10002310).

### Differences to rule on

- **Email addresses.** Phil Last (10501450): the PHP site has phil.last@4xtra.com; our source has phil.g.last@gmail.com. Editorial (10500550): editor@vector.org.uk against sjt@5jt.com. The restored site renders from its own cache, and `content/published/` is not served, so its source cannot be compared. Three more differences come from the PHP site treating `<address>` as a tag.

## Conclusions

- Our build is at least as faithful as the PHP site for every article both show as text, apart from the faults above. Against the original, the restored site mostly loses: mapped APL, encodings, made-up tags, and its debug trace (#105).
- **Nothing in the restored site's renderings needs to come into ours**, beyond the 29 sources (#104) and the 15 newer records they carry.
- The 24 framed per-article PDFs are better scans (300 dpi colour) than the issue scans (200 dpi 1-bit). Our tree holds them too, but our stubs link only the issue scan. Linking them is cheap.
