---
title: Ambivalent Operators...
authors:
- Phil Last
volume: '6'
issue: '2'
page: '117'
unindexed: true
transcribed: 'from page images of VOL.6-NO.2-OCTOBER-1989.pdf, page 119 (printed 117; within Technical Correspondence, after unindexed/v6n2-p115-more-on-finding-the-psp.md); Claude, 2026-10-11'
review: draft
tags:
- language design
- programming techniques
queries:
- "A letter, From: Phil Last, 12th July 1989, on David Piper’s letter in Vector 5.4. In the first listing two arrows printed under the line mark the added parentheses; set as a line of ↑ below the code."
- "The writer’s postal address, printed below his name, is omitted."
---

*From: Phil Last, 12th July 1989*
{ .byline }

With reference to David Piper’s letter in VECTOR 5.4 ... The right operand to David’s operator must be parenthesized to force the value rather than the `⎕NC` function itself to become the operand:

```apl
  [2] →(↑(RUN AVE)←(⍴NUMS)(AVERAGE ∆MONADIC(⎕NC 'SIZE'))NUMS)/0
                                           ↑          ↑
```

Once this is done, it works! However both the operator itself and the convoluted expression required to call it are perfectly described by the editorial from the same edition! Nevertheless, if we’re after a tricksy solution, the following avoids all conditional code, be it branch or execute, it tells you what it’s doing, and it works faster:

```apl
      ∇
[0]     AVE←SIZE AVERAGE NUMS
[1]    ⍝ MOVING OR NORMAL AVG DEPENDING ON EXISTENCE OF SIZE
[2]     AMBIVALENT 'SIZE'
[3]     AVE←(SIZE+/NUMS)÷↑SIZE,⍴NUMS
      ∇

      ∇
[0]     AMBIVALENT AMBIVALENT
[1]    ⍝ DCL CALLING FN AMBIVALENT WITH NAME OF ITS LEFT ARG.
[2]     AMBIVALENT←⎕FX('R←',AMBIVALENT,' B')('R←B')
      ∇
```

The function `AMBIVALENT`, given the name of the left argument to its calling function, attempts to fix a function with that name which returns its only argument. In the example, this would be:

```apl
[0]   R←SIZE B
[1]   R←B
```

This can only be fixed if `SIZE` does not already exist, in which case the call to plus reduction is genuinely monadic and the right argument to divide defaults to the shape of `NUMS`.

Phil Last
