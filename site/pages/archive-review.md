---
title: Comparison with the archive
---

*Written 11 October 2026, comparing [archive.vector.org.uk](https://archive.vector.org.uk/) with this development build.*

[archive.vector.org.uk](https://archive.vector.org.uk/) is the restored PHP site that served *Vector* online until 2016: the editors’ index, and the articles published as web pages. This build starts from the same index and the same web pages, and adds the printed issues. This page reviews what differs between the two, article by article.

## In short

- **Coverage.** The archive shows text for 630 of the 1,499 records in its index; this site has text for 1,430 of its 1,503. The archive’s own full index links only 661 articles; the other 838 records have an empty page there. This site gives every record a page, and lists everything on every issue’s Contents page (2,553 items), not only what the editors indexed.
- **Where both have text** (620 articles), the words agree exactly in 460. Most of the rest are APL characters: in 89 articles the archive shows the bytes of a pre-Unicode APL font (`©` for `⍝`, `„` for `←`), where this site shows the APL.
- **The archive is better** in no respect now found: the one line of code our converter had damaged is mended (below).
- **Scans.** The archive offers the PDFs of 12 issues (21:4, 23:4, the Dyalog at 25 supplement and Volumes 24–26) and 24 articles’ own PDFs. This site links a scan of 97 issues (all but 2:2, of which no copy has been found, and 3:4, 7:4 and 16:4, whose only copies are damaged) and the same 24 article PDFs, each Contents line to its page.

## The index

Both sites use the editors’ index (`index.xml`). The archive has 1,499 records; this site has 1,503, adding the four articles published online in 2016–17 after the archive was last updated ([Conquering recursion](../art10501740/), [Dyalog ’16 – an insider’s view](../art10501750/), [Larger than life automata](../art10501760/), [Minutes of the BAA AGM 2017](../art10501770/)).

The index was compiled by hand. This site corrects it from the printed Contents pages: 84 corrections to 76 records (pages, issues, authors and titles), each listed in the build report. Four records index an article a second time; on this site the second address leads to the first (for example [10013600](../art10013600/), indexed as “Review of Pocket APL”, is the APL2002 conference report [10000300](../art10000300/)). One, [10012820](../art10012820/), indexed as the 11:1 APL94 Abstracts, is the Update on APL94 printed in 10:4, and is filed there.

## What each site shows

For every record in the index, what a reader finds at `/art<ID>` on each site:

| archive.vector.org.uk | this site | articles |
|---|---|--:|
| text | text, converted from the same web page | 620 |
| text | transcribed from the scan | 5 |
| text | redirect to its twin (indexed twice) | 3 |
| text: a placeholder (“This is a dummy stub…”, “[File to do…]”) | link to the scan, with its machine-read text | 2 |
| the article’s own PDF, in a frame | transcribed from the scan (and the same PDF linked) | 24 |
| an empty page, though linked from its index | transcribed from the scan | 6 |
| an empty page, though linked from its index | machine-read text (damaged scan) | 1 |
| an empty page, not linked from its index | transcribed from the scan | 771 |
| an empty page, not linked from its index | machine-read text (damaged scans of 3:4, 7:4, 16:4) | 30 |
| an empty page, not linked from its index | link to the scan, with its machine-read text | 26 |
| an empty page, not linked from its index | known only from the index (2:2, no copy found) | 9 |
| an empty page, not linked from its index | transcription abandoned, link to the scan | 1 |
| an empty page, not linked from its index | redirect to its twin | 1 |
| not in its index | text | 4 |

The five where the archive has text and this site transcribed from the scan instead: in four the archive’s text is in a pre-Unicode APL font or the wrong encoding, and shows as `�` or stray characters ([10003000](https://archive.vector.org.uk/art10003000), [10004430](https://archive.vector.org.uk/art10004430), [10004770](https://archive.vector.org.uk/art10004770), [10008510](https://archive.vector.org.uk/art10008510)); in the fifth, [news from Kx](https://archive.vector.org.uk/art10011390) (22:4), the archive shows another article, the Kx Users’ Meeting report.

Six articles linked from the archive’s index have an empty page there, and are transcribed here: [First Quarter](../art10013780/) (Dyalog at 25), [A very simple structure compiler for J](../art10006140/), [Sending MIDI messages to a sound-card with J](../art10006150/), [How to write computer programs](../art10007810/), [An Implementation of A](../art10008920/) and [Getting started with A](../art10008930/).

## Where both have text

The 620 articles converted from the same web pages were compared word for word with the archive’s rendering of them (1,085,526 words), leaving aside headings, bylines and this site’s subject tags.

| difference | articles | words |
|---|--:|--:|
| none | 460 | |
| APL in a pre-Unicode font: the archive shows the font’s bytes | 89 | 3,606 |
| a web page shared by several articles: the archive shows the whole page | 12 | 10,949 |
| text in angle brackets, lost at the archive | 13 | 105 |
| web addresses rewritten | 10 | 281 |
| other (mostly mis-decoded quotes, and wording around headings) | 75 | 754 |

**APL characters.** Before Unicode, *Vector*’s web pages set APL in fonts that put APL symbols at the codes of ordinary characters. The archive shows those codes as they are, under a warning that “this article might contain pre-Unicode character-mapped APL code”: in [10000730](https://archive.vector.org.uk/art10000730) `headings„'Region'` is `headings←'Region'` and every `∇` is `’`; elsewhere `©` stands for `⍝`, `›` for `⊂`, `‡` for `↓`, `ª` for `⋄`. This site maps each font back to Unicode ([10000730](../art10000730/)), with per-article corrections where a mapping alone was not enough.

**Shared pages.** The letters of 22:2 and 22:4 and the Sustaining Members’ news of 23:1 were each published as one web page, which the index gives to several records. The archive shows the whole page under each title; this site shows each record its own part ([10011240](../art10011240/), Kenecdotes, against [the archive’s page](https://archive.vector.org.uk/art10011240), which begins with another letter).

**Angle brackets.** Text such as `<wsid>`, `<ctrl+break>` or `<function 1>` is read by the archive as an HTML tag and disappears: “loadws=” at the archive is “loadws=`<wsid>`” here ([10001980](../art10001980/)).

**Encoding.** Where a web page’s encoding was mis-declared, the archive shows `�` for curly quotes and accented letters (“Let�s”, [10004060](https://archive.vector.org.uk/art10004060)); this site decodes them.

**Stray markup.** In four articles the archive shows fragments of the web page’s own header as text: `ml version="1.0" encoding="utf-8"?> Sustaining Members' News | Vector 21.2 body {max-width:40em}` ([10014210](https://archive.vector.org.uk/art10014210)) or `YPE HTML PUBLIC "-//W3C//DTD HTML 3.2//EN">` ([10003640](https://archive.vector.org.uk/art10003640)).

**Web addresses.** Links that *Vector* printed to `archive.vector.org.uk` appear at the archive rewritten to `britishaplassociation.co.uk`; this site keeps them as published, and serves the old `/art<ID>` addresses itself.

**Where the archive was right and this site wrong.** One line of code in the report of the [San Quirico Moot](../art10011760/) (23:3): the source has `⍝  <-----3----->`, the archive shows it so, and our converter dropped three hyphens, taking them for the end of an HTML comment. Mended ([#283](https://github.com/5jt/vector-rescue/issues/283)).

## Other differences

| | archive.vector.org.uk | this site |
|---|---|---|
| Issue pages | the index records, in page order | the printed Contents page, with sections and unindexed items |
| Scans | 12 issue PDFs, 24 article PDFs | 97 issue scans, 24 article PDFs, each Contents line linked to its page |
| Machine-read text of the scans | — | under each untranscribed article, for searching |
| Quality of the text | — | marked for every item in the [full index](../full-index/) |
| Subjects | — | [tags](../tags/) on every article with text |
| Search | site search box | search of all pages |
| Old addresses | `/art<ID>` | `/art<ID>` |

## Method

The archive’s full index and its page for each of the 661 articles it links were fetched on 8 October 2026 (`sources/php-site/`); on 11 October the live index was checked and links the same 661 articles, and pages for a sample of unlinked records were fetched and found empty. The comparison of words uses the build’s check (`vecrescue fetch-php --check`), extended to list every difference rather than a sample, and leaves out headings, bylines, subject tags and the archive’s hidden debug log. Counts of articles in the table of differences overlap where an article has differences of more than one kind.
