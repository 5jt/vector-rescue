---
title: Teaching nested arrays
authors:
- Dave Piper
volume: '7'
issue: '2'
page: '133'
unindexed: true
transcribed: 'from page images of VOL.9-NO.2-OCTOBER-1990.pdf (misnamed: Vol.7 No.2), pages 135–136 (printed 133–134; within Technical Correspondence, the first letter, before Comparison Tolerance Explained); Claude, 2026-10-11'
review: draft
tags:
- education
- programming techniques
queries:
- "Untitled in print: a letter, “From: Dave Piper, 12th Sept 1990”, the first under the Technical Correspondence heading; the title is ours. It answers Peter Branson’s letter in Vector 6.4, p.95."
- "The writer’s postal address, printed after the signature, is left out here."
- "The underscored ∊ in the code (APL*PLUS ‘find’) is transcribed ⍷."
---

*From: Dave Piper, 12th Sept 1990*
{ .byline }

I feel I must follow up a couple of points raised in Peter Branson’s letter to Vector (Vector[6;4;95]).

Firstly with regards to training people in nested array versions of APL. I suspect Peter is arguing from the point of view of someone who learnt nested arrays after learning “APL1”. If introduced in a well structured course, the concept of depth is no more difficult to grasp than that of rank. Once depth is understood, most of the other bits to do with nested arrays follow quite easily.

In my experience, one of the first things students on APL fundamentals courses try is:

```apl
A←1 2 3
B←4 5 6
C←A B
```

I find the explanation of why you cannot put names next to each other is often quite difficult!

If you are training people to use nested array versions of APL, why introduce any unnecessary differentiation between simple and nested arrays? Peter’s point about being able to maintain “APL1” code is valid I guess; however, getting students to work out how to do things without nested arrays (on a course which teaches nested arrays) can form a useful exercise. By teaching nested arrays from the first, their work can take advantage of nested arrays and their associated benefits immediately.

Secondly, Peter talks about a workspace search function. From his description it sounds as if the original uses “peppery” code e.g.:

```apl
LIST←(∨/¨,¨(STR)⍷¨⎕CR¨[2]FNS)⌿FNS
```

Pepper-ised code (nothing to do with my surname), is one of the deadly sins of nested array versions of APL. The best technique for the application of EACH is to write a function that works on a single example, then generalise this by using each. We would solve the problem:

```apl
     ∇ R←STR SEARCH_FN NAME
[1]    R←∨/,STR⍷⎕CR NAME
     ∇
```

and use this function:

```apl
LIST←((STR)SEARCH_FN¨[2]FNS)⌿FNS
```

… thereby reducing the use of each to just one! It sounds from his letter as though this is just the approach Peter took - I’m not surprised it ran so much faster. The important point is that the first version may use “many APL2 features” (in reality no more than the second version) - but it uses them in an inappropriate manner. It is the appropriate use of facilities that is often the most important factor when designing code.

My only other comment is the idea of fixing *SEARCH_FN* or its equivalent as a local function to help with this is ridiculous. Far better to set up a copy list variable and use the indirect copy facility. Alternatively, with APL2 Version 1 Release 3, you can always set it up as a packaged workspace.

Dave Piper
