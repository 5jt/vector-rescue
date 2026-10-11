---
title: The Card Collecting Problem
authors:
- Norman Thomson
volume: '6'
issue: '4'
page: '22'
unindexed: true
transcribed: 'from page images of VOL.6-NO.4-APRIL-1990.pdf, pages 24–25 (printed 22–23; within The Education VECTOR, after unindexed/v6n4-p19-communications.md); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- education
- mathematics and statistics
queries:
- "A letter in The Education VECTOR, introduced at the end of Alan Sykes’s “Communications” (unindexed/v6n4-p19-communications.md) as “My final letter, from Norman Thomson”; it answers Claude Henriod’s card-collecting function in Vector 6.3. It is followed by Alan Sykes’s “Doing Useful Things With Strings” (art10009590). The italic parenthesis in the third paragraph is the editor’s comment, printed so."
- "In art10009970 (Comparison Tolerance Explained) Norman Thomson corrects the first line of `DRAW`, which should begin `DRAW: ⍺DRAW …`; transcribed here as printed."
- "Kept as printed: “Claude Henrion’s” (for Henriod); “cards ( ⍴⍵ )” and the spaced “( ⍳⍺ )”, “( 1↑⍺ )” in the text."
---

*by Norman Thomson*
{ .byline }

Whilst wishing to express general pleasure at Claude Henrion’s contribution from Switzerland (VECTOR 6.3) I feel compelled to express in somewhat stronger terms than Alan’s footnote the view that this sort of code is *NOT* the way to promote APL in education, and indeed provides ammunition for its critics.

Look again at the offending line:

```apl
  R←+/∨\⌽∨⌿<\(⍳C)∘.=?(N,11×C)⍴C
```

In the first place the program cannot be guaranteed to work if chance delivers a run of exceptional length (*editor’s comment - I reckon that the probability is in excess of .9999 for all C - any offers for a formal proof using APL of course?*). In the second, reading it from left to right as one should with all good APL code, requires a string of six functions to be comprehended before any data is reached. It is rather like encountering a mathematical expression like …

```
log(2+cos(exp-arctan(...)))
```

… for which little feeling for what the expression does remains by the time the argument is reached.

By contrast, a direct definition approach offers an excellent solution. Let `DRAW` describe the process of obtaining a full set of cards, given one starts with the card sequence `⍵`. At each step, test whether `⍵` contains a full set `( ⍳⍺ )` - if so stop and return the number of cards `( ⍴⍵ )`, if not obtain a new card, add it to the sequence and repeat. This leads to the function:

```apl
      DRAW: DRAW (?⍺),⍵:∧/(⍳⍺)∊⍵ :⍴⍵

      6 DRAW ⍳0
13
```

Simulation consists of repeating this process a prescribed number of times `( 1↑⍺ )` - for good measure we will additionally calculate the average on completion:

```apl
      SIM: SIM((¯1↑⍺)DRAW ⍳0),⍵:(1↑⍺)≤⍴⍵:⍵,(+/⍵)÷⍴⍵

      5 6 SIM ⍳0
13 19 8 12 11 12.6
```

If complete compatibility with Claude’s function is required, define:

```apl
      CARDS: (⍺,⍵)SIM ⍳0
```

We thus have a solution which relates to the problem in an obvious way, which doesn’t require the best bit of a page to explain it, which works in all cases, and which incidentally runs 7-8 times faster in I-APL than Claude’s APL trickery (the sort of thing I have to confess I have all too often wallowed in myself).

I believe that the issue raised here is important in discussing APL in education, and please Claude do continue to make your valued contributions to VECTOR - this letter is in no sense an attack!

Yours sincerely

Norman Thomson
