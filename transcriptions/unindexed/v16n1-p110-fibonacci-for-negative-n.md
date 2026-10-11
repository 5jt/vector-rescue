---
title: Fibonacci for negative n
authors:
- Joseph De Kerf
volume: '16'
issue: '1'
page: '110'
unindexed: true
transcribed: 'from page images of VOL.16-NO.1-JULY-1999.pdf, pages 112–113 (printed 110–111; within Technical Correspondence, the first letter under the section heading); Claude, 2026-10-11'
review: draft
tags:
- mathematics and statistics
- programming techniques
queries:
- "An untitled letter in Technical Correspondence, From: Joseph De Kerf, 24 May 1999; the title is ours. It is the first letter in the section, followed by Peter Donnelly’s “Knowledge, Age and Experience are no Substitute for Good Fortune”. It answers J. Sullivan’s “Functional Extensions to the Fibonacci Sequence” (Vector 15.4)."
- "Kept as printed: the second and third displays both read `N,[0.5] FIB1 N` although they show the results of FIB2 and FIB3."
- "Checked in Dyalog APL: with `N←¯7+⍳13`, FIB1 gives the zeros shown for negative N, and FIB2 and FIB3 both give `¯8 5 ¯3 2 ¯1 1 0 1 1 2 3 5 8`, as printed."
---

*From: Joseph De Kerf, 24 May 1999*
{ .byline }

In a recent paper [1], J. Sullivan extends in a very elegant way the domain of the subscript \(n\) of the Fibonacci numbers \(F_n\) from positive integers to negative integers, reals, and complex numbers. Just one remark.

Referring to my paper [2], he quite rightly notices that the function `FIB1` published in my paper, using only the first term of the golden section formula, doesn’t work for negative values of \(n\), the function giving zeros:

```apl
    ∇ F←FIB1 N;R
[1]   F←⌊0.5+(÷R)×(0.5×1+R←5*0.5)*N
    ∇

      +N←¯7+⍳13
¯6 ¯5 ¯4 ¯3 ¯2 ¯1 0 1 2 3 4 5 6

      N,[0.5] FIB1 N
¯6 ¯5 ¯4 ¯3 ¯2 ¯1 0 1 2 3 4 5 6
 0  0  0  0  0  0 0 1 1 2 3 5 8
```

He states that “the values for negative \(n\) are the same in absolute value as those for positive \(n\), but the signs alternate” and “in order to generate values for negative \(n\) as well as positive \(n\) you will need both terms of the golden section formula”, giving for that purpose the function `FIB2`:

```apl
    ∇ F←FIB2 N;R
[1]   F←⌊0.5+(÷R)×((0.5×1+R)*N)-(0.5×1-R←5*0.5)*N
    ∇

      N,[0.5] FIB1 N
¯6 ¯5 ¯4 ¯3 ¯2 ¯1 0 1 2 3 4 5 6
¯8  5 ¯3  2 ¯1  1 0 1 1 2 3 5 8
```

I don’t agree. The fact that the values for negative \(n\) are the same in absolute value as those for positive \(n\), but with alternating signs, may be formalized by the relation \(F_{-n}=-(-1)^n F_n\).

This means that, using this relation we may calculate \(F_{-n}\) from \(F_n\) by giving its value the appropriate sign, while calculating \(F_n\) only needs the first term. Incorporating the relation in `FIB1`, we get for instance the function `FIB3`:

```apl
    ∇ F←FIB3 N;R
[1]   F←(¯1*(N+1)×(N<0))×⌊0.5+(÷R)×(0.5×1+R←5*0.5)*|N
    ∇

      N,[0.5] FIB1 N
¯6 ¯5 ¯4 ¯3 ¯2 ¯1 0 1 2 3 4 5 6
¯8  5 ¯3  2 ¯1  1 0 1 1 2 3 5 8
```

## References

1. *J. Sullivan: Functional Extensions to the Fibonacci Sequence.* Vector Vol.15 No.4 pp.123-126
2. *J. De Kerf: From Fibonacci to Horadam.* Vector Vol.15 No.3 pp.122-130
