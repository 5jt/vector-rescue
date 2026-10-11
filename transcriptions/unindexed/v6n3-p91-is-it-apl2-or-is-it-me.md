---
title: Is it APL2, or is it me?
authors:
- Peter Branson
volume: '6'
issue: '3'
page: '91'
unindexed: true
transcribed: 'from page images of VOL.6-NO.3-JANUARY-1990.pdf, pages 93–94 (printed 91–92; within Technical Correspondence, after the section heading); Claude, 2026-10-11'
review: draft
tags:
- implementations
- programming techniques
queries:
- "A letter in Technical Correspondence, From: Peter Branson, December 1989; the first letter under the section heading, which follows Adrian Smith’s “Hackers Corner: Beware the M61” (p.90). It is followed by Dave Piper’s “More on Ambivalent Operators” (unindexed/v6n3-p93-more-on-ambivalent-operators.md)."
- "The function is named both STRIPX (in the call `STRIPX '∆STRIPX'`) and ∆STRIPX; transcribed as printed."
---

*From: Peter Branson, December 1989*
{ .byline }

A while back (Vector 4.2.99), I enlarged Adrian Smith’s *∆STRIP* function to do a stand-alone search for global (or semi-global) names in individual functions, under VSAPL. Recently I moved to a new site with APL2 (Release 2), and since there was nothing comparable immediately available, I put this function up again (using the better ‘del-all-dupes’ idiom from Vector 4.4.97, of course).

Unlike VSAPL, APL2 allows trailing comments on code lines, so I put in some (APL2-type) code to handle these in the same position as before, plus some other minor improvements. At first it seemed OK, and worked on some small functions, but then I tried it on itself, with this result:

```apl
      STRIPX '∆STRIPX'
FAIL
NAME
0123456789
∆TAB
```

and only *∆TAB* should be there!

I double-checked for typos and possible name coalescence, etc., but could find nothing wrong. Finally I narrowed the problem down to the ‘delete if in quotes’ line:-

```apl
V←(~(V='''')∨≠\V='''')/V
```

I have looked at this idiom in all sorts of ways, including breaking it right down to the individual boolean results, and it seems alright on various test objects. It is difficult for me to do a detailed analysis on `'∆STRIPX'` itself since I cannot print anything yet, and the intermediate results are a bit large to analyse from screen displays in the limited time available, so I tried a different approach.

Since the trouble occurs with quoted bits and a label name well down in the `⎕CR`, I created a little *DIQ* (Delete in Quotes) function, which just does the above job, plus delete multiple blank rows for a neater display. The matrix which this works on was caught from *∆STRIPX* into a global variable, and *DIQ* was run against this with progressively fewer of the top lines dropped off, i.e. `DIQ ,(N,0)↓MAT,' '` with reducing N (taking care not to drop the lines causing the trouble).

The results were surprising. The function has 27 lines (different from the original because of trailing comments,etc.) and for values of *N* of 12 and above *DIQ* is fine; the result is a vector occupying a few screen lines holding bits of function lines, all entirely as expected with no rogue entries at all. At *N* = 11 there is an abrupt change, the result of *DIQ* now being:-

```apl
⎕WA ⎕FX : 0123456789 INVALID FN NAME
```

and that is all there is! Thereafter, as *N* is progressively reduced to 0, the result gradually builds back upwards from this short result, but now always containing rogue bits.

The matrix, *MAT*, is formed in this *∆STRIPX* by disclosing the result of a localised sub-function and checks OK at depth 1. However, when IBM’s DISPLAY function is applied to it, two of the right hand vertical border lines are displaced one print position to the right; I have not seen this before, but the positions don’t have any obvious relation to the problem lines.

At present I am baffled. Unless I am missing something obvious (or perhaps quite subtle), it’s weird. I don’t yet have any access to IBM so ......???????

Peter Branson
