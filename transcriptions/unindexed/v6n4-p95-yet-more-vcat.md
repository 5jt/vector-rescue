---
title: Yet more VCAT ...
authors:
- Peter Branson
volume: '6'
issue: '4'
page: '95'
unindexed: true
transcribed: 'from page images of VOL.6-NO.4-APRIL-1990.pdf, pages 97–98 (printed 95–96; within Technical Correspondence, after unindexed/v6n4-p94-m61-problem-partial-resolution.md); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- education
queries:
- "The first letter under the Technical Correspondence heading, printed “Yet more VCAT ...”, From: Peter Branson, 6th March 1990; it answers Norman Thomson’s “VCAT: A Response” in Vector 6.3. It is followed by David Piper’s “Is Function Ambivalence a Good Thing?” (unindexed/v6n4-p96-is-function-ambivalence-a-good-thing.md)."
- "The postal address of EDS Ltd, printed under the signature, is omitted."
- "The function `VCAT` is printed without its del and line numbers; kept as printed."
---

*From: Peter Branson, 6th March 1990*
{ .byline }

Norman Thomson’s response (Vector Vol.6 No.3) to my Education Vector `VCAT` example does raise a couple of interesting points (not to mention Adrian’s timing tests!).

Firstly, I don’t know what a ‘modern didactic view’ is, but if we want to use some APL2, why not try a half-and-half approach (`⎕IO←1`):

```apl
R←X VCAT Y
X←(¯2↑1 1,⍴X)⍴X
Y←(¯2↑1 1,⍴Y)⍴Y
R←⊃(⊂[2] X),⊂[2]Y
```

Fairly obviously, this will handle scalars and vectors also. Norman’s approach means carrying two names for a simple job, and I really don’t like doing that. Working with a plethora of production workspaces, I try to keep to the absolute minimum the number of names that I might need to copy around.

A more serious point was raised in his first paragraph; namely should we introduce beginners (kids and grown-ups alike) to the APL2-type enhancements at an early stage (irrespective of ‘free’ software)? With a requirement in the near future to start training one or more graduates in APL, I have been pondering this question already, and personally I think not. A full grounding in APL1 is essential if the person is going to be maintaining existing code (as most professional programmers are likely to be doing at some time or other) and he or she must be able to recognise the older idioms too. To bring in the enhancements as well is, I think, a bit too much in the early stages.

The final point is raised by Adrian’s timing tests. There are times when good APL1 is needed for efficiency, so a thorough grounding is essential. One small example of this arose when I joined my present company last year. They have a standard utility written using many APL2 features for searching a workspace for occurrences of a character string. Unfortunately, response was poor at the time, and it was rather boring waiting for the result to show. I re-wrote the function with a few APL2 bits, and used a localised function for the individual object searches, leaving only one ‘each’. Result: about 25 times faster, and much less boring!

Peter Branson  
EDS Ltd.
