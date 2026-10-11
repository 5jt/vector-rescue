---
title: VCAT in Sharp APL
authors:
- E.E. McDonnell
volume: '7'
issue: '1'
page: '113'
unindexed: true
transcribed: 'from page images of VOL.7-NO.1-JULY-1990.pdf, pages 115–116 (printed 113–114; within Technical Correspondence, after unindexed/v7n1-p112-dangers-of-apl-risc-programming.md); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- performance
- implementations
queries:
- "A letter in Technical Correspondence, From: E.E. McDonnell, 9 April 1990, signed Eugene McDonnell. It answers Norman Thomson’s “VCAT: A Response” in Vector 6.3 (p.100). It is followed by Norman Thomson’s “How to Kill More Cats...” (p.115)."
- "The writer’s postal address (Reuters, Palo Alto) is omitted."
- "Sharp APL glyphs: link is printed ⊃, table as comma-bar ⍪, and monadic thorn (format) as a thorn-like glyph read as ⍕. The left argument is the italic lower-case letter l."
- "The timing table is printed in a monospaced box drawn with + - and broken bars; set here as a code block with | for the bars."
- "Kept as printed: “influence by the design”."
---

*From: E.E. McDonnell, 9 April 1990*
{ .byline }

I was interested to see Norman Thomson’s note "VCAT: A Response" in Vector 6, 3. He provides a "modern didactic view" of the problem which, as your editor points out, is slower than the "antique, pragmatic" utility which it offers to supplant. It is, of course, not at all uncommon for the initial implementation of a new feature to be slower than the facility it is intended to replace; when the implementors have enough experience (or often enough complaints from customers) they often find ways to make the new facility more competitive in speed.

I can report, however, on an alternative which is also modern, and while I can hazard no guess as to its didactic merits, I do know that it has the merits of being much shorter even than Mr Thomson’s solution, handles the degenerate cases of scalar and vector arguments with no extra fuss, and is faster than the antique it can replace.

The solution is written in **Sharp APL**. The view of the problem it takes is influence by the design of the monadic format function and by the availability of the table, or matrix-making primitive. A boxed list of the arguments is formed using the link function: `l⊃r`; this two-element list is made into a two-by-one matrix, using the table function: `⍪l⊃r`; and this is formatted using monadic thorn, which has the property that it expands boxed items to match the largest in size: `⍕⍪l⊃r`. That’s all there is to it.

Here is the whole function:

```apl
[0] z←l vcat r
[1] z←⍕⍪l⊃r
```

Timings made on the Sharp mainframe system for arguments of varying sizes are as follows:

```
+-------------------------------------------+
|         |         |      z←l vcat r       |
| ⍴left   | ⍴right  |    eem    |     PB    |
|         |         |    vcat   |    VCAT   |
|---------|---------|-----------|-----------|
|  2   5  |   3 3   |    118    |    115    |
| 12   80 |    23   |    125    |    112    |
| 56  132 |    63   |    137    |    131    |
|100  200 |300  30  |    270    |    320    |
+-------------------------------------------+
```

Yours faithfully

Eugene McDonnell
