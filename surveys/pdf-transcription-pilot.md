# Pilot: transcribing the PDF-only articles (work in progress)

Issue #40. Running log; to be written up when the pilot is complete.


Method: render pages at 220 dpi (110 too coarse for APL: ⌿ looked like / or ≠); read; zoom to 400–500 dpi on any code region with doubtful glyphs; write; cross-check OCR words (accounted for if they split into transcription words).

| id | group | pp | code lines | zooms | corrections after zoom | queries | structure judgments | OCR words unaccounted (real misses) |
|---|---|---|---|---|---|---|---|---|
| 10002820 | much | 3 | 66 | 1 | 1 (⌿ in [19],[20]; read as / at 110 dpi) | 0 | prose names in backticks; underscored Δ → ⍙ | 0 |
| 10007890 | some | 4 | 22 | 2 | 0 | 1 (W for X?) | WLINK two-column table → code block; signature → blockquote | 0 |
| 10003880 | little | 2 | 0 | 0 | 0 | 0 | starts mid-page | 0 (residue from preceding letter) |
| 10006380 | much | 3 (range said 2) | 52 | 1 | 0 | 2 (author slips: fn 62/63; DI/DX) | — | 0; CODE bytes verified against assembler |
| 10010120 | much | 2 (range said 3; ends top of p.131) | 38 | 2 | 0 | 1 (two [4] lines) | — | results verified arithmetically; UNINDEXED: "Miaou = Cat!" (Claude Henriod) p.131–132 |

Findings so far:
- Page range from the index is wrong both ways: articles end on the next article's first page (10006380), or end early with unindexed pieces following (10010120). Transcriber must find the end by reading.
- Unindexed letters/pieces exist between indexed articles.
