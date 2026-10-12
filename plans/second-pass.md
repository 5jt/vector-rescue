Second Pass: the remaining Contents lines (#305)
================================================

Decided 2026-10-12 (Stephen Taylor). Transcribe the Contents lines that still link only to the scan: editorials, news, reports, reviews and articles the index left out; BAA, BCS and sustaining-member news; correspondence sections; section editorials; crosswords and puzzles; Quick Reference and course diaries; APL Product Guides. Left out: Index to Advertisers and the order, subscription, submission and registration forms; 2:2 (no scan) and the damaged 3:4, 7:4 and 16:4; section headings with no text of their own.

Conventions
-----------

- One file per Contents line in `transcriptions/unindexed/` (`unindexed: true`, `review: draft`), linked by `file:` on the existing line; README row "Contents line (#305)".
- A section line whose pieces already have files gets only its own text; with none left, `note: heading only; its pieces are listed below`. A piece not printed in the issue gets a note saying so.
- Diaries and guides as Markdown pipe tables, a table per printed section, every entry kept. Guides may be drafted from the previous issue's file but every row is checked against the page images.
- Page numbers corrected against the print, with a note giving the Contents page's number.
- **Contact details** (decided 2026-10-12): wherever a person rather than a company is the contact, the street address, telephone and fax numbers and personal e-mail are omitted, with a query: BAA officers and editors, conference chairmen, user-group contacts, letter-writers, sole consultants, and one-person firms at a private address (Andrews, Phil Last Ltd, JAD Software, J Austria, AtomicVector, CoSy.com, Entropy Software, Lambent Technology Ltd, Acadvent Ltd, APL Consultants Japan, I-APL Ltd, Peter Cyriax Systems, IAC/Human Interfaces at Hill End). Companies', universities' and institutions' addresses, PO boxes and Brook House (APL 385, Vector Production) are kept. The 22:x guides also omit Alastair Kinloch Ltd, Dr. Nussbaum GmbH, Skelton Consulting GmbH and Orbien, which earlier guides keep: to review.

Progress
--------

- Wave 1, pilot 6:1 (#306); wave 2, Volumes 5–7 (#307); wave 3, Volumes 8–10 and the contact-details rule throughout (#308); wave 4, Volumes 11–13 and the First Pass's missed 11:1 APL94 Abstracts, now `art10000160` (#309); wave 5, Volumes 14–17 (#310); wave 6, Volumes 18–23 (this branch).
- The 13 lines of the Dyalog at 25 supplement (23:4.1) are the section headings of How we got here (10013790), held as text; noted on each line.

Remaining
---------

- Volumes 1–4: 198 lines (1:1–4:4, without 2:2 and 3:4).
- Volumes 22–25 lines with no wayback scan (30): from the typeset PDFs in `sources/sjt/Vector/issues/` (v241.pdf, v242.pdf, v244.pdf, v251.pdf, v253.pdf, v254.pdf), and 22:3 and 23:1.
- 12:2 p.113 (Adrian Smith), by hand: the content filter stops it.
- The agents' brief is `plans/second-pass-brief.md`; the work list is rebuilt (`tools/scratch/sp2_worklist.py`, then `sp2_kids.py`) from the Contents files: items with a title and page but no `file:` or `vid:`, excluding the forms and advertiser indexes, grouped by issue with the PDF and offset from `pages.issue_pdfs` and `pipeline.pdf_links`.

Printed pieces with no Contents line
------------------------------------

Noticed by the agents and not transcribed: candidates for a further sweep. Mostly section introductions.

| Issue | Printed page | Piece |
|---|---|---|
| 6:1 | 49 | Reviews Section — introduction by Adrian Smith (with Smith Benchmarks table) |
| 6:1 | 63 | GENERAL ARTICLES section introduction |
| 5:4 | 77 | RECENT MEETINGS section introduction (with contents list) |
| 5:4 | 93 | TECHNICAL SECTION introduction |
| 5:1 | 59 | RECENT MEETINGS section introduction |
| 5:1 | 65 | BAA Technical Meeting 25th March 1988 (notes by Adrian Smith) |
| 5:2 | 48 | Ziemann drawing (full page) |
| 5:2 | 55 | RECENT MEETINGS section page |
| 5:2 | 74-75 | APL*PLUS II by James Wheeler (STSC) |
| 5:2 | 76 | IBM APL2/PC notes by Adrian Smith |
| 5:2 | 79 | Technical Section introduction |
| 7:1 | 47 | Reviews Section introduction by Adrian Smith |
| 6:4 | 53 | Reviews Section introduction by Adrian Smith |
| 6:4 | 30-31 | A Selection of Affordable APL Systems; Questionnaire (Alan Sykes), in Education Vector |
| 7:3 | 32 | APL Booklist by Ed Shaw (in Education Vector contents) |
| 7:3 | 98 | General Articles section introduction |
| 5:3 | 9 | APL Training Courses (course diary, no Contents line) |
| 5:3 | 55 | RECENT MEETINGS introduction |
| 5:3 | 87 | GENERAL ARTICLES introduction |
| 6:2 | 43 | Reviews Section introduction by Adrian Smith |
| 6:2 | 113 | Technical Section introduction |
| 8:1 | 59 | Reviews and Product Announcements section heading |
| 9:2 | 95 | GENERAL ARTICLES introduction |
| 9:2 | 127 | TECHNICAL SECTION introduction |
| 8:2 | 55 | RECENT MEETINGS introduction with acknowledgements |
| 8:2 | 95 | GENERAL ARTICLES introduction |
| 10:2 | 11-12 | APL in Business flyer (EBMS/BAA Swansea) — promotional |
| 10:2 | 91-92 | Steinbrook & McDonnell From Trees into Boxes (rep. A. Camacho) |
| 10:2 | 92-93 | Bernecky Array Morphology (rep. A. Camacho) |
| 10:2 | 93-94 | Thomson Understanding ANOVA the APL Way (rep. S. Camacho) |
| 8:4 | 81 | J section introduction (with contents list) |
| 10:1 | 6-7 | BAA-GUI flyer (house advert) |
| 13:2 | 47 | RECENT MEETINGS introduction with APL96 picture credits |
| 13:2 | 87 | GENERAL ARTICLES introduction |
| 11:3 | 97 | Technical Section introduction |
| 11:4 | 159 | Submitting Material to Vector |
| 12:3 | 63 | GENERAL ARTICLES note (FTP access to J turtle graphics) |
| 16:1 | 107 | TECHNICAL SECTION introduction |
| 14:2 | 18 | British APL Association News (future issues, committee, AGM) no Contents line |
| 15:1 | 5 | Quick Puzzle from Ajay Askoolum (foot of diary page) |
| 19:3 | 5 | BAA AGM notice (Camacho) at foot of Guest Editorial |
