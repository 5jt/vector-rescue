---
title: Errors in “Integrating with Insight”
authors:
- John R. Clark
volume: '10'
issue: '1'
page: '116'
unindexed: true
transcribed: 'from page images of VOL.10-NO.1-JULY-1993.pdf, page 118 (printed 116; within Technical Correspondence, after A Windows GOTCHER for APLIWIN); Claude, 2026-10-11'
review: draft
tags:
- mathematics and statistics
queries:
- "A letter in Technical Correspondence, From: John R. Clark, June 1993, on Norman Thomson’s “Integrating with Insight”. It ends with an editor’s note."
- "The postal address under the signature (P.O. Box and town) is omitted."
- "Kept as printed: “Vector Vol.9 No.2 Jan 1993” (the January 1993 issue is 9.3); “ESPL” beside “EPSL”; the vertical bars after ≤ and ≥ (“≤ |”, “≥ |”), which seem to stand for magnitude."
---

*From: John R. Clark, June 1993*
{ .byline }

The article “Integrating with Insight” by Norman Thomson, pages 113 to 116 of Vector Vol.9 No.2 Jan 1993, has some typographical errors and one logical error.

## Logical Error:

Page 115 line [2] of `METHOD` should end with `⍳L←Q×⌈L÷Q`. For Simpson the number of subdivisions must be even.

## Typographical errors:

Page 113. `1/4096` should be `1/4095`

Page 115. Line [4] of `ROMBERG`. `EPSL` is an undefined variable.

Page 115. Line [3] of `ADAPT`. `EPSn` is an undefined variable.

I am not sure what the undefined variables should be. If the `L` of `ESPL` is `≤|` then `ROMBERG` works. If the `n` of `ESPn` is `≥|` then `ADAPT` works. Perhaps you have a problem with your typesetting software. I believe you need magnitude in both tests.

I receive my copy of Vector through membership in Los Angeles SOCAL SIGAPL and Roy Sykes of Sykes Systems — I do enjoy your publication.

As a past algorithm editor of QuoteQuad I am aware errors do creep into publications.

Keep up the good work

John R Clark

*Ed: I created a translate table to convert Norman Thomson’s original text from APL2 `⎕AV` into APL\*PLUS/PC `⎕AV`, which is used for typesetting. Unfortunately I omitted `≤` and `≥` from the translate table, hence the EPSL and EPSn.*
