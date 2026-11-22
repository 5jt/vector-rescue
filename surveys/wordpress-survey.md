WordPress database survey
=========================

Survey of the vector.org.uk WordPress database (#316), from a phpMyAdmin SQL dump sent by Jake Jacob (generated 2026-11-17; MariaDB 10.11). It resolves blocker B1 in `plans/master.md`.

The dump is **not held in this repository**. Besides the content it holds user accounts, password hashes, two-factor secrets, private messages, Wordfence logs and mailing-list subscribers. Only the content tables (`wp_posts`, `wp_postmeta`, `wp_terms`, `wp_term_taxonomy`, `wp_term_relationships`) were read for this survey.

Jake also sent `htdocs.zip`: byte-identical to the htdocs copy of the PHP site compared on 2026-10-12, and it holds none of the articles below.

Not in the dump: the uploaded files (`wp-content/uploads/`). The database lists them as 502 attachments (112 PDFs, the rest images).

## Summary

| Kind | Count | |
|---|---:|---|
| Issue pages, category *Journal* | 101 | One per issue, Volume 1 No. 1 to Volume 26 No. 4 (posted 2024): contents list and PDF link |
| Articles already held | 32 | Including 3 duplicate posts; matched by body text |
| **Articles not held** | **11** | 10 published 2019–2022, plus a short notice |
| Video posts | 8 | Seven talks at the BAA meeting of 20 May 2016 (one posted twice); a short abstract and a YouTube video each |
| Unpublished | 3 | A draft article, a pending test post, a styling sample |
| Pages | 13 | Site furniture (About Us, Past Publications, member pages) |

Matching was by body text: the share of each post's five-word sequences found in a held text (`build/docs`, `transcriptions/`). Titles alone mislead: several posts carry different titles from the index (e.g. *Letting data tell a story with kdb+* is 10501600, *What makes a good tennis match?*), and several title matches were false.

## Articles not held

None of these is in the PHP index or the Wayback captures. Authors as recorded on the posts (Co-Authors Plus terms); some posts carry extra author terms that look like editors or plugin defaults, so check the bylines in the text.

| Post | Posted | Category | Title | Author | Media |
|---:|---|---|---|---|---|
| 763 | 2019-04-12 | In Press | Finding text in files | Dan Baronet | video |
| 965 | 2019-05-29 | In Press | Reflections on Langlet’s APL Theory of Human Vision | Stuart Smith | 23 |
| 1458 | 2019-05-30 | In Press | Making images and videos of the Buddhabrot | Nicholas Delcros | 4, video |
| 1496 | 2019-05-30 | In Press | APLX is out, long live APL | Dan Baronet | |
| 1966 | 2019-07-05 | In Press | TAO Axioms | Adám Brudzewsky, Jay Foad, Roger Hui (byline in text) | |
| 2041 | 2020-02-02 | 27:1 | The doctor and the doc | Stephen Taylor | |
| 2240 | 2020-09-10 | 27:1 | Powerful CSV processing with kdb+ | Ferenc Bodon | 8 |
| 2293 | 2020-11-09 | 27:1 | Book review — Fun Q: A Functional Introduction to Machine Learning in Q | Daniel Krizian (author term; the book is by Nick Psaris) | |
| 2473 | 2022-06-16 | 27:1 | A Vendor-Agnostic Logo for APL | Adám Brudzewsky | 7 |
| 2666 | 2022-10-31 | 27:1 | Hacker’s Corner: JPEG Comments | Nicholas Small | |
| 170 | 2018-10-14 | In Press | APL Germany Autumn Meeting (a two-line notice) | Stephen Taylor | 1 |

The media column counts images and files under `wp-content/uploads/` referenced by the post. Of the 43, 41 are still served by vector.org.uk; two return 404 (`2019/04/figure1.png`, `2020/09/pivotWithTotal.png`).

27:1 is the issue that never appeared in print. The PHP index already holds seven 27:1 or in-press articles (10501680–10501770); these eleven complete it, as far as WordPress records.

## Art IDs for the additions

All twelve are published (2026-11-19, #316): `transcriptions/art10501780.md`–`art10501890.md`, converted from the posts’ HTML (not the Markdown some posts keep, which in one case is out of date). Losses in WordPress are recorded in each file’s queries: APL characters stored as “?” in 10501800 (mostly restored), two images.

**Decided by Stephen Taylor, 2026-11-19:** the additions continue the PHP index's numbering, in steps of 10 from 10501780, in order of WordPress post date. The draft (2075) and test posts get none.

| ID | Post | Posted | Title |
|---|---:|---|---|
| 10501780 | 8 video posts | 2016-05-20 | BAA meeting, 20 May 2016: talks (`transcriptions/art10501780.md`) |
| 10501790 | 170 | 2018-10-14 | APL Germany Autumn Meeting |
| 10501800 | 763 | 2019-04-12 | Finding text in files |
| 10501810 | 965 | 2019-05-29 | Reflections on Langlet’s APL Theory of Human Vision |
| 10501820 | 1458 | 2019-05-30 | Making images and videos of the Buddhabrot |
| 10501830 | 1496 | 2019-05-30 | APLX is out, long live APL |
| 10501840 | 1966 | 2019-07-05 | TAO Axioms |
| 10501850 | 2041 | 2020-02-02 | The doctor and the doc |
| 10501860 | 2240 | 2020-09-10 | Powerful CSV processing with kdb+ |
| 10501870 | 2293 | 2020-11-09 | Book review — Fun Q |
| 10501880 | 2473 | 2022-06-16 | A Vendor-Agnostic Logo for APL |
| 10501890 | 2666 | 2022-10-31 | Hacker’s Corner: JPEG Comments |

## Articles already held

All 32 are 25:2/3, 26:2, 26:4, 27:1 or in-press articles. Scores corrected 2026-11-22 (#328): the first scoring stripped everything between `<` and `>` from the held texts as if it were HTML, which in APL and J code ate whole passages. That is why twelve posts first scored below 0.85; all but one now score 0.90 or more.

**Compared, 2026-11-22 (#328; README decision 5):** the twelve were diffed word by word against the held texts. **None has been revised; the held texts stand.** The differences are:

- in the held texts only: bylines, link URLs, figure captions (10501760), reference links;
- in the posts only: the Divi page builder's shortcodes (`[et_pb_section …]`, 10501640, hence its 0.82), and in *Co-operators* (10500740) one paragraph posted twice;
- the rest is alignment noise around code.

**Better sources:** none needed. 10501740, 10501750 and 10501760 are held only as Wayback renderings; their words and APL glyphs match the posts exactly.

| Post | Title | Held as | Score |
|---:|---|---|---:|
| 1645 | Co-operators | 10500740 | 1.00 |
| 1641 | Sharing code – the APLTree project | 10500730 | 0.99 |
| 1623 | What is an Array? | 10500690 | 0.95 |
| 300 | Minnowbrook conference review | 10501310 | 0.99 |
| 288 | One reason that APL is so cool | 10501270 | 0.99 |
| 318 | Squares, neighbours, probability, and J | 10501300 | 0.99 |
| 315 | Writing a simple Japanese dentist office system in APL2 | 10501350 | 0.98 |
| 320 | A tool of thought | 10501380 | 0.99 |
| 290 | A letter from Dijkstra on APL | 10501260 | 0.95 |
| 354 | Searching for the state in which Wonderful Things are inevitable | 10501360 | 1.00 |
| 292 | Impending kOS | 10501320 | 0.98 |
| 285 | All integer partitions: J programs compared | 10501280 | 0.94 |
| 306 | Notation as a tool of proof | 10501240 | 0.99 |
| 304 | Table Diff | 10501400 | 0.99 |
| 225, 2210 | A Notation for APL array Embedding and Serialization (two posts) | 10501450 | 1.00 |
| 204, 1693 | Using J for Actuarial Applications Part 1 (two posts) | 10501580 | 0.93, 0.94 |
| 235 | Pi, Pin and Ping | 10501470 | 0.99 |
| 239 | Reading New Code | 10501520 | 1.00 |
| 195 | APL and partitioned data | 10501640 | 0.82 |
| 1800 | J-ottings 58 | 10501460 | 0.98 |
| 749 | Second Childhood | 10500550 | 0.97 |
| 1723 | Book review — Q Tips | 10501500 | 1.00 |
| 1156 | Letting data tell a story with kdb+ | 10501600 | 0.98 |
| 1404 | Sixteen APL Amuse-Bouches | 10501480 | 0.90 |
| 1705 | A graphical sandbox for K | 10501610 | 0.96 |
| 102 | Minutes of Annual General Meeting 2016 | 10501690 | 0.99 |
| 1383 | Writing a Utility function | 10501710 | 0.98 |
| 136 | Dyalog ’16 – an insider’s view | 10501750 | 0.99 |
| 1390 | A modern APL system | 10501730 | 0.99 |
| 1396 | Conquering recursion | 10501740 | 0.98 |
| 1417 | Taming statistics with limited-domain operators | 10501700 | 1.00 |
| 1426 | J-ottings 59 Love Actuarily | 10501720 | 0.98 |
| 1432 | Larger than life automata | 10501760 | 0.99 |

Held but not on WordPress: 10501680 (Optima welcomes James Heslip) and 10501770 (Minutes of the BAA AGM 2017).

## Video posts

Seven talks at the BAA meeting of 20 May 2016, in eight posts, each a short abstract (mostly the programme blurb) and a video: *File functions in Dyalog 15* (Richard Smith), *A Memo Operator* (Roger Hui), *About PresentAPL* and *Markdown & MarkAPL* (Kai Jaeger), *XAML and APL on the Web* (Michael Hughes; posted twice, 1157 and 1878), *Git in the APL Room* (Stephen Taylor), *Pi for Brains* (Romilly Cocking). All seven videos are live on the British APL Association’s YouTube channel (checked 2026-11-19). The category’s other two members are page-builder layouts.

**Ruling (Stephen Taylor, 2026-11-19):** one page for the meeting’s talks, with speakers, abstracts and video links, filed beside the 2016 AGM minutes (10501690). Drafted as `transcriptions/art10501780.md`; its ID is 10501780 (below).

## Unpublished

- 2075, draft, 2021-01-21: *The Derivative Revisited* (Richard Park). A full article never published; needs the author’s or editor’s consent.
- 2182, pending: *A test post as author*. Not content.
- 2007: *Swatch sample for styling*. Not content.

## Issue pages and PDFs

The 101 *Journal* posts list each issue’s contents (with author searches on the PHP site) and link the issue PDF. Issue 2:2 has a page but no PDF; 7:2 has neither a PDF attachment nor a link. Neither was ever uploaded, so #62 stands for those two.

**The truncated scans can be replaced.** The Wayback copies of 3:4, 7:4, 16:4 and 21:4 in `sources/wayback/` stop at exactly 1 MiB and do not open. vector.org.uk still serves all four complete (checked 2026-11-19: 148 pages each, 3.7–5.4 MB, first pages are the right covers).

## Pages

About Us (with an embedded video), Past Publications, Home, Authors, test front pages, and the member pages (Log In, Sign Up, Reset Password, My Account, My Profile, Member Directory). None holds journal content.
