---
title: Horner’s Method
authors:
- Walter G Spunde
volume: '8'
issue: '3'
page: '138'
unindexed: true
transcribed: 'from page images of VOL.8-NO.3-JANUARY-1992.pdf, pages 144–145 (printed 138–139; within Technical Correspondence, after A Note on CPU Time Monitoring); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- mathematics and statistics
- education
queries:
- "A letter in Technical Correspondence, From: Walter G Spunde, 30 Sept 91. An advertisement for the DELPHI Panel Design Toolkit follows it on printed page 139 and is not transcribed."
- "The first code line is a formula rather than APL to execute; it is set as printed."
---

*From: Walter G Spunde, 30 Sept 91*
{ .byline }

Norman Thomson’s neat recursive formulation for calculating Stirling numbers (Vector Vol.8 No.1 p.95) has been gratefully added to my collection of teaching examples. Here is another one which readers of Education Vector may find useful:

Horner’s method for calculating values of a polynomial with coefficients C0,C1,C2,C3,…,Cn in ascending order, at points V, is:

```apl
C0 + V × C1 + V × C2 + V × C3 + ... + V × CN
```

Texts on numerical methods present this as the most efficient and accurate way of calculating the value of polynomials.

The exercise is to implement these operations, and one solution is:

```apl
Z←VS HORNER CS
→0 IF 1 = ⍴Z ← CS
Z ← CS[1] + VS × VS HORNER 1↓CS
```

which shows the nesting of linear functions that is involved here, and may be compared with the encoding

```apl
Z ← (⍉ ((⍴CS),⍴VS) ⍴ VS) ⊥ ⌽CS
```

or other algorithms for calculating polynomial values

Walter G Spunde<br>
School of Information Technology<br>
University of South Queensland<br>
AUSTRALIA
