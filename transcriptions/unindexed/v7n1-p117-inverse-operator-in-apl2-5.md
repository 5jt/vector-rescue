---
title: The INVERSE operator in APL2.5
authors:
- I. Phelfritt (née Leigh)
volume: '7'
issue: '1'
page: '117'
unindexed: true
transcribed: 'from page images of VOL.7-NO.1-JULY-1990.pdf, pages 119–120 (printed 117–118; within Technical Correspondence, after unindexed/v7n1-p117-power-operator.md); Claude, 2026-10-11'
review: draft
tags:
- humour
- language design
queries:
- "Untitled in print; the title is the sweep’s. A spoof letter, From: I. Phelfritt (neé Leigh), May 1990, signed “I. Phelfritt, c/o Dyadic Systems Ltd.”; passed on by John Scholes in the letter before it (unindexed/v7n1-p117-power-operator.md). It responds to the review of APL2.5 in Vector 6.4 (“APL2.5 for the Microwriter AgendA”, p.58). It is followed on p.118 by Cedric Heddle’s “The APL*PLUS ‘dead key’ Problem ...”."
- "The definition is printed `INV:ωβ` in italic APL type; the second glyph looks like a Greek beta and is transcribed as printed, with ω read as ⍵."
- "Kept as printed: “neé” (the Contents item has “née”)."
---

*From: I. Phelfritt (neé Leigh), May 1990*
{ .byline }

I was thrilled to see your review of IBM’s new APL2.5 in April’s Vector 6.4, and felt moved to send you a further couple of examples. One consequence of the direct definition of operators which may not be immediately obvious is the ease with which you can define the INVERSE operator for monadic functions:

```apl
  INV:⍵β
```

`INV` produces a derived function which reverses the effect of its operand. Formally: `A  ↔  F  INV  F  A` for any array `A` and any monadic function `F`. The following examples show the power of this operator ...

```apl
      ÷4
0.25
      ÷INV 0.25
4
      +\INV 1 3 6
1 2 3
```

Where the inverse is not unique, the system provides a ‘least squares’ solution:

```apl
      +\INV 6
6
      ?INV 4
7
```

and of course, `INV` may take a system function as operand, so:

```apl
      ⎕EX INV 1
FOO                 ⍝ re-instates a previously expunged function

2
      ⎕DL INV 2     ⍝ has the same effect as ⎕DL ¯2 in dyalog APL
```

We are only now beginning to appreciate the power of this new implementation, but I’m sure that such examples will soon swell our idiom libraries.

I. Phelfritt  
c/o Dyadic Systems Ltd.
