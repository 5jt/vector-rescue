---
title: Technical Correspondence
authors:
- Roger Hui
volume: '20'
issue: '3'
page: '116'
unindexed: true
transcribed: 'from page images of VOL.20-NO.3-JANUARY-2004.pdf, page 118 (printed 116); Claude, 2026-10-12'
review: draft
tags:
- programming techniques
- APL in perspective
queries:
- "Printed heading “Correspondence”; the Contents line has “Technical Correspondence”. One letter, from Roger Hui, undated, about E.E. McDonnell’s “At Play with J: The Magical Matrix” in Vector 20.2. It fills printed 116; “At Play with J: Giddyap” begins on printed 117."
- "The APL87 expression is printed with APL glyphs spelt out in braces (`{rank}`, `{is}`, `{iota}`, `{omega}`), kept as printed; the paper’s title “Some Uses of { and }” is also kept as printed."
- "Kept as printed: “is due that I “wrote it all””."
---

*From: Roger Hui*
{ .byline }

Re: E.E. McDonnell’s article “At Play with J: The Magical Matrix” in Vector Volume 20, Number 2, October 2003.

In the article, Mr. McDonnell insinuated that my use of the “magical matrix” and indexing to generate permutations is due that I “wrote it all”. That statement is far from the truth! Revisionist history, even!

The “magical matrix”, computed as:

```j
   \:"1 = i. 4
0 1 2 3
1 0 2 3
2 0 1 3
3 0 1 2
```

(grade-down each row of the identity matrix) first saw the light of day in the APL87 conference proceedings, in the paper “Some Uses of { and }”, section 4.3, computed as:

```text
k ~{rank}1 0 k{is}{iota}{omega}
```

The paper also presented functions for generating combinations, compositions, and self-upgrading and self-downgrading permutations, using a similar technique of growing a table from a seed through indexing.

I should point out that in 1987 J was not yet even a gleam in Ken Iverson’s eyes. Therefore, I deny the allegation, and I defy the allegator!

Roger Hui (with tongue firmly in cheek)
