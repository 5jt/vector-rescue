---
title: Six Months in the Life of Vector (letter)
authors:
- John Searle
volume: '9'
issue: '2'
page: '7'
unindexed: true
transcribed: 'from page images of VOL.9-NO.2-OCTOBER-1992.pdf, page 9 (printed 7; the first letter in General Correspondence, before David Crossley’s letter); Claude, 2026-10-11'
review: draft
tags:
- implementations
- programming techniques
queries:
- "An untitled letter in General Correspondence, From: John Searle, 26 July 1992, on the editor’s article “Six Months in the Life of Vector” (Vector 9.1); the title is ours. It ends with the editor’s reply."
- "Kept as printed: “0 4 ⊥” (decode), though the editor’s reply speaks of Encode (⊤), which gives the results quoted; “Mangled-Logic APL*PLUS and Dyalogdic interpreters”."
---

*From: John Searle, 26 July 1992*
{ .byline }

Thank you for improving upon my submitted function in the article *Six Months in the Life of Vector*. It was much more interesting than my original. Unfortunately, if you type it into IBM’s APL2/PC in TryAPL2 it reveals a bug in their interpreter! Using the published example, the expression to the right of the `0 4 ⊥` should be integer `36`, giving a result of `9 0`. However, APL2 calculates an expression very close to `36`, but gives a result of `8 4`, and hence the function returns `8 5`, not `9 1`.

The IBM stand at APL92 was not impressed, but the Mangled-Logic APL\*PLUS and Dyalogdic interpreters gave the “correct” results.

*ED: Thanks John, I should have written `⌊10×A` rather than relying on APL\*PLUS to demote the result of the multiplication to integer. Not sure that this is a bug in any interpreter, as Encode is not `⎕CT` dependent and one should not depend on an interpreter demoting floating point numbers to integer. These little things are set to trap the unwary!*
