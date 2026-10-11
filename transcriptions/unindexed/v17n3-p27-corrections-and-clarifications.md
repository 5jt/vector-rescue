---
title: Corrections and Clarifications
authors:
- Jon Sandles
- Stephen Jaffe
volume: '17'
issue: '3'
page: '27'
unindexed: true
transcribed: 'from page image of VOL.17-NO.3-JANUARY-2001.pdf, page 29 (printed 27; within Zark Newsletter Extracts, the first item after Jon Sandles’s introduction); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- APL community
queries:
- "The first item in the Zark Newsletter Extracts. Jon Sandles’s introduction to the extract, which has no record of its own, is included at the head. The note is unsigned, from the editor of the extracts; the function that follows it is Steve Jaffe’s. It corrects 17:2, where the `CMIOTA` printed under Jaffe’s name (unindexed/v17n2-p25-from-stephen-jaffe.md) was really Carlo Spinicci’s."
- "Jaffe’s `CMIOTA` was run in Dyalog APL as a check on the transcription; it returns `2 5 1` for a small character-matrix sample."
- "Kept as printed: “behavior” in the comment of [4]; “Insert 1> ρX” in the comment of [17]."
---

*Zark Newsletter Extracts, introduced by Jon Sandles*
{ .byline }

I am pleased to report that we have some interesting entries from the last Zark Newsletter challenge. These can be found at the end of the following Zark extract. Once again I would like to encourage you all to enter responses as we can often shed new light on old problems, or even submit solutions in the more recent APL derivatives: J and K. In this case thanks to Morten Kromberg for submitting some interesting APL solutions, and to Stefano Lanzavecchia for the first K submission we have seen.

## Corrections and Clarifications

Production department would like to apologise for the following howler in Vector 17.2. We received two entries for `CMIOTA`, one from Steve Jaffe and one from Carlo Spinicci (APL Italiana). Perceptive readers may have been puzzled as to why Steve had signed his code with an APLIT timestamp! Well, now you know. Here is Steve’s code – the previous version really did belong to Carlo!

```apl
     ∇ I←X CMIOTA Y;J;K;Q;D
[1]    →S1×⍳1≠≡Y
[2]    →((2>⍴⍴X)∨1<⍴⍴Y)/⎕LC+1 ⋄ Y←(¯2↑1 1,⍴Y)⍴Y   ⍝ Patch for 1 Y value
[3]    X←(2↑(⍴X),1 1)⍴X                     ⍝ Library of values
[4]    D←1↑⍴X←⊖X              ⍝-----flip to simulate ⍳ behavior on repeats
[5]    Y←(2↑(⍴Y),1 1)⍴Y                     ⍝ Values to look up in Library
[6]    X←(Q←X[;⎕IO]∊Y[;⎕IO])⌿X              ⍝ Eliminate impossible X values
[7]    →(0=1↑0⍴X)/NUMERIC
[8]    K←⎕AV⍋X                              ⍝ Sort Library of values
[9]    I←I-⍋⍋I←(-1↑⍴Y)↑⍋⎕AV⍋X[K;],[⎕IO]Y   ⍝ LOOKUP for Characters
[10]   →CONTINUE
[11]  NUMERIC:
[12]   K←⍋X                                 ⍝ Sort Library of values
[13]   I←I-⍋⍋I←(-1↑⍴Y)↑⍋⍋X[K;],[⎕IO]Y      ⍝ LOOKUP for Numerics
[14]  CONTINUE:
[15]   J←¯1≠I←(¯1,K)[⎕IO+I]                 ⍝ Find Closest X value for each Y
[16]   J←J\∧/X[J/I;]=J⌿Y                    ⍝ Eliminate all but exact matches
[17]   I[(~J)/⍳⍴J]←⎕IO+(⍴X)[⎕IO]            ⍝ Insert 1> ρX for all Y not found
[18]   I←((Q/⍳⍴Q),⎕IO+⍴Q)[I]                ⍝ Expand to all X values (see [6])
[19]   I←(1+D)-I                            ⍝-----correct for flip
[20]   I[(I=0)/⍳⍴I]←1+D
[21]   →0
[22]  S1:I←(↓X)⍳↓Y
     ∇
```
