---
title: Japanese APL on IBM 5550
authors:
- David Ziemann
volume: '2'
issue: '1'
page: '69'
unindexed: true
transcribed: 'from page image of VOL.2-NO.1-JULY-1985.pdf, page 71 (printed 69; the photographic review follows on p.70); Claude, 2026-10-05'
review: draft
warning: The session printout, mostly in Japanese characters printed by a dot-matrix printer, is reproduced as an image, not transcribed.
queries:
- "No byline on the page; the contents list gives David Ziemann."
- "The printout of an APL session on the IBM Multistation 5550 (two columns, with kanji city names, hiragana readings, and a yen-formatted report) is cropped as a 16-grey image. Its kana and kanji are too small and rough in the scan to transcribe with confidence. A reader with Japanese could transcribe it: the city names appear to be 東京, 名古屋, 大阪, 長崎."
- "“Hirakana” (hiragana) is printed so."
---

One of the more interesting displays at the APL85 exhibition was Japanese APL on the IBM 5550, apparently a mutant IBM PC. The Japanese characters (Kanji, Hirakana or Katakana) are stored internally as a new data type, with two bytes per element, occupying two columns when printed or displayed. They can be mixed with conventional one-byte characters, and can be processed via APL primitives (rho, transpose, indexing etc.) as normal.

The product was produced jointly by the IBM scientific centres at Tokyo and Madrid.

![A session on IBM Multistation 5550 日本語 APL Version 1.01 (produced by IBM Tokyo and Madrid Scientific Centers): a matrix of four city names in kanji is reshaped, reversed and transposed; their readings in hiragana are sorted with grade-up to order the cities; random data is formatted as yen; and a function Report prints the sorted table with totals](v2n1-p69-japanese-apl-on-ibm-5550/session-printout.png)
