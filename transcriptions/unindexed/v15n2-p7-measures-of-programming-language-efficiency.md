---
title: Measures of Programming Language Efficiency
authors:
- Joseph De Kerf
volume: '15'
issue: '2'
page: '7'
unindexed: true
transcribed: 'from page images of VOL.15-NO.2-OCTOBER-1998.pdf, pages 9–10 (printed 7–8; within Correspondence, the only letter in the section); Claude, 2026-10-11'
review: draft
tags:
- APL in perspective
- performance
queries:
- "A letter in Correspondence, From: Joseph De Kerf, 30 September 1998; the only letter in the section, followed by a house notice for Vector back numbers."
- "Kept as printed: “In 1997, M.H. Halstead … published a book”, where reference [1] gives 1977; “with those for other the languages”; “Algol 58”; “Vol.53” for SIGPLAN Notices in reference [4]."
---

*From: Joseph De Kerf, 30 September 1998*
{ .byline }

In 1997, M.H. Halstead of Purdue University published a book on a theory allowing to measure characteristics of software and their relations [1]. One of the parameters is the programming language level \(\lambda\). Programming time is inversely proportional to the square \(\lambda^2\) of this language level \(\lambda\). As such, the square \(\lambda^2\) is a measure for programming efficiency.

In a paper, published in the ACM SIGPLAN Notices in 1986 [2], programming language level \(\lambda\) and efficiency \(\lambda^2\) of simple array APL (APL/SA) were compared with those for other the languages, published by Halstead. According to the results, APL/SA would be about 12 times as efficient as Assembler. This result wonderfully agrees with an experimental result reported at the SEAS APL Working Committee’s Meeting in 1971 [3].

In a paper, published this year in the ACM SIGPLAN Notices [4], the investigation is extended to nested array APL (APL/NA). According to the results, APL/NA would be about 17 times as efficient as Assembler, giving for APL/NA versus APL/SA an extra increase of programming efficiency of about 39%. An overview of the results is given below.

| Language | \(\lambda\) | \(\lambda^2\) | \(\lambda^2\)/ASS |
|:---------|-----:|------:|------:|
| APL/NA | 3.62 | 13.07 | 16.88 |
| APL/SA | 3.07 | 9.43 | 12.17 |
| PL/1 | 1.53 | 2.34 | 3.02 |
| Pascal | 1.53 | 2.34 | 3.02 |
| Algol 58 | 1.21 | 1.46 | 1.89 |
| Fortran | 1.14 | 1.30 | 1.68 |
| Pilot | 0.92 | 0.85 | 1.09 |
| Assembler | 0.88 | 0.77 | 1.00 |

Both investigations have been reported in the ACM SIGPLAN Notices in order to address not only the APL community, but also all those who are interested in programming languages.

## References

1. M.H. Halstead: *Elements of Software Science.* Elsevier Computer Science Library; Elsevier North-Holland, New York 1977
2. J.L.F. De Kerf: *APL Compared with other Languages according to Halstead’s Theory.* ACM SIGPLAN Notices Vol.21 No.1, January 1986, pp. 31–39
3. *Abstract of the Proceedings at the SEAS APL Working Committee’s Meeting, Grenoble, February 15–16, 1971.* APL Quote-Quad, Vol.3 No.1, June 11 1971, pp. 14–15
4. F.H.D. van Batenburg, E. de Ridder & J. De Kerf. *APL Extended compared with other Languages according to Halstead’s Theory.* ACM SIGPLAN Notices, Vol.53 No.6, June 1998, pp. 54–60
