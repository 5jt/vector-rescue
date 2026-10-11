---
title: Humble-pie Corner
volume: '5'
issue: '3'
page: '19'
unindexed: true
transcribed: 'from page images of VOL.5-NO.3-JANUARY-1989.pdf, page 21 (printed 19; within The Education VECTOR, after Puzzle Corner); Claude, 2026-10-11'
review: draft
tags:
- education
- programming techniques
queries:
- "Unsigned; presumably by the Education Vector’s editor, Alan Sykes. It corrects the previous Education Vector (Vector 5:2), whose “Counting in APL” begins on printed 27 there. It follows Puzzle Corner (unindexed/v5n3-p19-puzzle-corner.md) on the same page."
- "The code is printed in a widely spaced APL font; `+/( ⍳6 )∘ . =NOS` is transcribed without the spaces."
---

Typesetting APL code is always a challenge; a couple of small glitches crept in to the last Education Vector, namely:

```apl
PAGE←2 3 4 20⍴⍳480
```

… half way down page 21. Also several places where there should have been a new-line to distinguish the bit you typed in from APL’s response. An example would be:

```apl
      +/(⍳6)∘.=NOS
2 3 1 2 1 1
```

… on page 28. At least one sharp-eyed reader (aged 5) spotted that you actually get:

```apl
1 5
3 3
5 2
```

… as the mid-interval frequency table, not `6 3 2` as shown. At some point the vector `NOS` must have gained an extra element, as there were definitely only 10 numbers in the initial list!
