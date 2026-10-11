---
title: An Ambivalent Operator
authors:
- David Piper
volume: '5'
issue: '4'
page: '96'
unindexed: true
transcribed: 'from page images of VOL.5-NO.4-APRIL-1989.pdf, pages 98–99 (printed 96–97; within Technical Correspondence, after John Warden’s letter); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- language design
queries:
- "A letter in Technical Correspondence, From: David Piper, 24th February 1989, signed D.B. Piper. It follows unindexed/v5n4-p96-ibm-bug-when-moving-to-apl2.md and precedes Nicholas Small’s “Setting PF keys and Other Initialization” (unindexed/v5n4-p97-setting-pf-keys-and-other-initialization.md)."
- "DEFAULT [4] is printed `R←1(DEFAULT FUNC RIGHT)`; the glyph after the arrow is clearly a digit 1, though the comment (“EXEC WITH DFLT ARGUMENT”) suggests something else was meant. Kept as printed. The code is APL2 and was not run."
- "The writer’s home address in Rainham, Kent, is omitted."
- "Kept as printed: “acheive”, “acheived”."
---

*From: David Piper, 24th February 1989*
{ .byline }

Here is an APL2 operator of use in ambivalent functions. One use of ambivalent functions is to elide the left argument, and thereby force it to take a default value. The methods normally used to achieve this are, for example:

```apl
[..]  →(2=⎕NC 'LEFT')/dyadic
[..]   LEFT←default
[..] dyadic:
```

or perhaps …

```apl
[..] ⍎(0=⎕NC 'LEFT')/'LEFT←default'
```

Neither of these solutions is ideal - the first embodies too much apparent complexity to acheive such a simple effect - code in which errors can be made. The second uses execute, which is bad for all the normal reasons!

The defined operator listed below allows the effect of the second example to be acheived without using execute:

```apl
     ∇R←DEFAULT(FUNC ∆MONADIC CLASS) RIGHT
[1] ⍝ OP: default func right if class is not 2
[2]  R←0                                ⍝ ASSUME DYADIC CALL
[3]  →(2=CLASS)/0                       ⍝ EXIT IF CALL WAS DYADIC
[4] R←1(DEFAULT FUNC RIGHT)             ⍝ EXEC WITH DFLT ARGUMENT
     ∇
```

The operator is used as follows:

```apl
     ∇AVE←SIZE AVERAGE NUMS;RUN
[1] ⍝ FN: MOVING OR NORMAL AVERAGE DEPENDING ON ⎕NC 'SIZE'
[2]  →(↑(RUN AVE)←(⍴NUMS)(AVERAGE ∆MONADIC ⎕NC 'SIZE')NUMS)/0
[3]  AVE←(SIZE+/NUMS)÷SIZE
     ∇
```

I trust the above is of interest, and look forward to any feedback.

Yours sincerely

D.B. Piper
