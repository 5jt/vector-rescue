# TODO

Expected next steps (updated 2026-10-11).

## PDF-only articles (`plans/pdf-conversion.md`)

- [x] Phase 2, Volumes 1–15: done (status page "after Volume 15").
- [x] Phase 2, Volumes 16–20: done (status page "after Volume 20").
- [x] Phase 2, Volume 21: done (status page "after Volume 21"). 21:4 was transcribed from the text layer of `sources/sjt/Vector/issues/v214.pdf`, as the wayback scan is damaged.
- [x] Sullivan (10009460): query on Series/Sequence in place.
- [ ] Add unindexed pieces found along the way to `transcriptions/unindexed/` and to #44.
- [ ] Phase 3: review checklists (`plans/pdf-review-checklist*.md`), ordered by interest; little-code articles need only their queries checked.
- [x] Report: OCR words missing from each transcription (build/report.md, last section); 63 flagged.
- [x] Triaged the 63 flagged (2026-10-11): no omitted passages; misses come from neighbouring articles on shared pages, figures and listings kept as images, and deliberate omissions under queries. Fixed: two wrong page ranges (10004320, 10010900), one missing byline (10006380). XPL (10001020) is the abandoned transcription.
## Second Pass (decided 2026-10-11, #44: unindexed pieces are worth indexing and republishing)

- [x] Pieces left out by the First Pass and noted in its queries: 26 transcribed into `transcriptions/unindexed/` and put on their issues' Contents files; three earlier pieces linked (#297).
- [x] Swept Volumes 5–21 for further unindexed pieces (#299): 226 added to the Contents files, linked to the scan, not yet transcribed. 74 finds left out (section editorials, which are their Contents line's own text; pieces already inside a held transcription; house notices, captions, parts of reports): listed in #299. Not swept: 7:4, 16:4 and 21:4 (damaged scans; 21:4 was transcribed from another copy).
- [x] Transcribed the sweep's pieces (#301): 210 files in `transcriptions/unindexed/`. 16 Contents lines removed, as their text is already published inside an indexed transcription (13:4, 14:1, 14:4, 15:2, 19:2, 7:2, 8:2).
- [ ] 12:2 p.113, “Microsoft Announces APL for the 8088 – almost 20 years late!” (Adrian Smith): blocked by the output content filter (long quotations from the book *Gates*); left linked to the scan, for transcription by hand.
- [ ] The remaining Contents lines (#305; plan, conventions and brief in `plans/second-pass.md`). Done: Volumes 5–23 (#306–#310 and wave 6), about 470 pieces, and 11:1 APL94 Abstracts (missed by the First Pass). Contact details of individuals omitted throughout (rule of 2026-10-12).
  - [ ] Volumes 1–4: 198 lines.
  - [ ] Volumes 22–25 lines with no wayback scan (30), from the typeset PDFs in `sources/sjt/Vector/issues/`.
  - [ ] Review: the 22:x guides omit four firms that earlier guides keep (Alastair Kinloch, Nussbaum, Skelton, Orbien).
  - [ ] Then update the project status page.
- [ ] A further sweep for printed pieces with no Contents line noticed during #305 (41, mostly section introductions; listed in `plans/second-pass.md`).

## Metadata

- [ ] Publish a machine-readable full index, `vector-index.json`, written by the build (#303). It also settles the index-corrections item below, as `index.xml` cannot be corrected in place.
- [ ] When the site goes public: Highwire `citation_*` tags on article pages, for Google Scholar and Zotero (#302). No Dublin Core on pages.

## Tags

- [x] Every article with text tagged (#261, #263): transcriptions carry their own tags; the converted pages' tags are in `transcriptions/article-tags.yaml`, applied by the build.
- [x] Converted pages that showed the wrong text (#265): duplicates redirect to their twins; shared sources split; placeholders held; 10012820 refiled to 10:4; two bylines corrected.

## PDF-only articles, Volumes 22–23

- [x] Transcribed the 25 indexed articles of Volumes 22–23 never online (#267: 22:1 #270, 22:2 #272, 22:4 #274, 23:3 #276, 23:4 #279, 23:4.1 #281). 23:4's Contents and PDF now follow the printed issue (issues/v234.pdf is pre-press).
- [x] Transcribed the placeholders 10009100 (20:4 K day) and 10004730 (12:1 Langlet, A Quite Different New Primitive) (#292).
- [x] PDFs with more than one page offset (#268): 8:1 (two unnumbered order-form pages after p.20), 16:3 (four after p.112), 22:2 (pp.47–50 missing); links now follow each run of pages.

## Index corrections

- [ ] Correct `index.xml` records from the scanned Contents pages (authoritative; decided by Stephen Taylor 2026-10-10: correct without review, log every correction). Discrepancies are noted on the Contents lines in `transcriptions/contents/`.

## Manual transcription

- [ ] 12:1 Adrian Smith, *Native File Functions for Dyalog APL* (10008630, printed pp.137–142): an output content filter blocked automated transcription twice; left as a PDF-linked stub for transcription by hand (#183).
- [ ] 21:2 Paul Cockshott, *Efficient Compilation of Array Expressions* (10002580, printed pp.91–100): blocked by the output content filter twice; left as a stub (#255).

## Awaiting decisions

- [ ] #44: editorial review of the unindexed pieces.
- [ ] Earlier open items: proposed corrections; #34, #35.

## Housekeeping

- [ ] Start sessions from a fresh terminal (or with `CLAUDE_CODE_FORCE_SESSION_PERSISTENCE=1`) so transcripts are saved.
- [x] Deleted `origin/42-folded-ocr` (fully merged).
- [x] Fixed the in-page anchor `#_Toc117273387` in art10013690; the build has no warnings. Two corrections that a duplicated key had silently disabled (10014110, 10003430) now apply; a test forbids duplicate keys.
