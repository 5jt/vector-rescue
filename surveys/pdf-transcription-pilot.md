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
| 10007070 | much | 4 | 95 (incl. results) | 4 | 0 | 2 (printed title/author; "APROXIMATIONS") | ÷ drawn like ‡; ⌿ ⍀ as slash/backslash with bar | 0; results verified (row/col sums) |
| 10003240 | much | 3 (range said 4; then advert) | 45 | 0 (300 dpi enough) | 0 | 2 (no ⍝ on [20]; comment column narrowed) | — | 0 |
| 10001690 | much | 5 | 57 | 0 (300 dpi enough) | 0 | 2 ("reult"; comments cut off at margin) | rules as numbered bullets kept; 2 figures cropped to 1-bit PNG | 0 (residue is code OCR noise and the graph's axis label) |
| 10005920 | much | 5 (range said 7; pp.30–31 are an unindexed piece) | 225 (incl. output) | 5 | 0 | 3 (printed title; A one element short, NOS 4–9 shifted; label-string spacing) | Instructions / Example Game as code blocks | 0; Example Game verified against Instructions; UNINDEXED: "Two Mathematical Functions" (C.E. Williams) pp.30–31, CHAR4 and ROMB results verified |
| 10008760 | much | 9 | 150 (APL and HTML) | 6 | 0 | 3 (Winword ☞ bullet; APL-font • and © glyphs; ⍕ read from context) | 4 screenshots cropped to 16-grey PNG; prose HTML tags in backticks | 0 (residue is OCR noise and screenshot text) |
| 10010330 | much | 4 (range said 6; then an advert) | 30 (J) | 2 | 0 | 0 | J inline in backticks; subscripts as Unicode | 0 (hyphenation only); every verb checked by hand against its printed rows (no J interpreter here) |
| 10010550 | much | 8 | 210 (J and output) | 4 | 0 | 4 (`value`/`values`; wrapped NB. comments rejoined; `_` placement; missing `)`) | figure cropped to 1-bit PNG | 0 (OCR noise only); spm g1, spm h1, path values, slacks, connectivity, arclist, bf all recomputed and match |
| 10000410 | some | 4 (range said 4; ends p.50, next article starts p.51) | 105 | 4 | 0 | 4 (printed title; “Federick”; wrapped line; θ for ⍬) | quotation as blockquote; `0⊥` (last item) idiom kept | 0 (OCR noise only) |
| 10005140 | some | 11 | 70 (K) | 0 | 0 | 5 (printed title; “though”; “the how”; footnote moved out of code; footnotes as Markdown footnotes) | 8 footnotes → `[^n]`; K symbols in double backticks | 0 (OCR noise only) |
| 10005210 | some | 6 (range said 11; issue has only 148 PDF pages; Back Numbers notice follows) | 45 | 3 | 0 | 3 (printed title; secondary/primary slip; minor slips) | 2 screenshots, 16-grey; dfns with right-hand comments | 0 (residue is the notice and code OCR noise) |
| 10005980 | some | 8 | 75 | 2 | 0 | 6 (L2/L3 prose slip; VScroll 1/¯1; MakeVectorTest; B1 event; unclosed paren; `...` continuations) | screenshot 16-grey; one-line code snippets as separate blocks, as printed | 0 (OCR noise only) |
| 10008200 | some | 7 (range said 8; p.69 is a section divider) | 12 | 0 | 0 | 4 (printed title; winH… vs WINΔ…; typos; screens without captions) | 6 screen dumps as 16-grey images; function summary as table | 0 |
| 10008410 | some | 3 (range said 8; Index to Advertisers follows) | 45 | 0 | 0 | 4 (⍢ glyph; typeset output as image; “simple”; Word style dumps as code) | code nested in list items; box-drawing for boxed output | 0 |
| 10010290 | some | 5 | 25 (J) | 0 | 0 | 4 (printed title; missing `0` after `b.`; “sequence verbs”; `_` glyph) | definitions as definition lists; inline J in backticks | 0; diag rotv and `+/@-` results checked by hand |
| 10010300 | some | 5 | 35 (J) | 1 | 1 (`'abw'` read as `'abv'` at 300 dpi) | 5 (printed title; stereogram as image; “assesses”; unnamed joiner symbol; transliterated fractions) | stereogram and 2 plan diagrams as 1-bit PNG | 0 |
| 10010980 | some | 3 (range said 6; advert follows) | 50 | 5 | 2 (`|` in the exact expression; `¯1↑Y` read as `¯1↓Y` at 600 dpi, settled at 900 dpi by recomputing) | 4 (printed title; argument names swapped in prose; typos; empty lines) | — | 0; all four solutions recomputed and match the printed example |
| 10000180 | little | 4 (range said 2) | 1 | 0 | 0 | 4 (printed title; range; 10010060 index page wrong; grammar) | two-column abstracts → one column, titles italic | 0; UNINDEXED: "The APL95 Software Exchange" (Dick Holt) p.13 |
| 10001120 | little | 5 (range said 7; next indexed review starts p.52) | 30 (benchmark tables) | 0 | 0 | 4 (printed title; table alignment; subheading; two doubtful glyphs) | benchmark tables as code; AP124/GRAPHPAK as definition list | 0; all 19 ratios and the average recomputed and match |

Findings so far:
- Page range from the index is wrong both ways: articles end on the next article's first page (10006380), or end early with unindexed pieces or adverts following (10010120, 10003240). Transcriber must find the end by reading.
- Unindexed letters/pieces exist between indexed articles. Decided 2026-10-03: transcribe into `transcriptions/unindexed/`, list in #44 for editorial review.
- 300 dpi pages make zooms mostly unnecessary.
