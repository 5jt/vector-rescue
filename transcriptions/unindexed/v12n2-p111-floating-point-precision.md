---
title: Floating-Point Precision
authors:
- Joseph De Kerf
volume: '12'
issue: '2'
page: '111'
unindexed: true
transcribed: 'from page images of VOL.12-NO.2-OCTOBER-1995.pdf, pages 113–114 (printed 111–112; within Technical Correspondence, after art10010100, Calculating Probabilities); Claude, 2026-10-11'
review: draft
tags:
- mathematics and statistics
- implementations
queries:
- "A letter answering the Production Manager’s Observation on De Kerf’s “The Complete Elliptic Integrals and APL” (art10004440; unindexed/v12n1-p106-production-managers-observation.md)."
- "Kept as printed: the comparison tolerances “1E15” and “1E16” (meaning 1E¯15 and 1E¯16), and “Addams-Hippisley”."
- "The writer’s postal address, printed after his name at the end of the letter, is omitted."
---

*From: Joseph De Kerf, 23 August 1995*
{ .byline }

In [1], it was shown how the so-called common mean concept may be used to calculate the complete elliptic integrals of the first and second kind. APL user-defined functions were given and illustrated for p = 0.0(0.1)0.9/1.0. Results were displayed with 10 and 15 digits after the decimal point. Calculations were done with VAX APL under VMS (DEC) and for comparison tolerance its default value 1E15.

In a companion note however, the production manager observes he found slightly different results when run in Dyalog/W. So I did my homework again, however with comparison tolerance 1E16 (instead of 1E15). In addition I did the same calculations but with APL user-defined functions based on:

1. gaussian quadrature (Newton-Cotes formulae) and
2. series expansion (MacLaurin’s series integrated, Addams-Hippisley series and the series dedicated to A. Caley).

For all of these runs, carefully avoiding the accumulation of errors as far as possible, I found the same results as published in [1]. So, I suppose those results are correct.

On the other hand, I did the same calculations on other APL systems and found, for all of them, some differences similar to or even greater than those observed by the production manager.

I suppose that the origin of the difference lies in the floating-point mantissa precision. For VAX APL under VMS this is more than 16 decimal digits (about 16.86D), such that the 16th decimal digit may be correct. However, for all the other APL systems I checked, floating point representation is based on the ANSI/IEEE Std 754-1985 [2]. This means that for those systems the floating-point mantissa precision is somewhat less than 16 decimal digits (about 15.95D), such that the 16th decimal digit of the intermediate and *a fortiori* of the end results becomes more or less unreliable.

This is the reason why, in some implementations such as IBM’s APL2/PC and MicroAPL’s APL.68000, the upper limit of the domain of the print precision variable is set to 15. On the other hand, the advantage of the standard is that the largest number representable is about 1.80E308, while in practice, who cares about the accuracy of the 16th decimal digit?

Joseph De Kerf

## References

1. Joseph De Kerf; *The Complete Elliptic Integrals and APL*; Vector, Vol 12, No. 1 July 1995, pp 102-106
2. *ANSI/IEEE Std 754-1985*; IEEE Standard for Binary Floating-Point Arithmetic; Published by the IEEE, New York, USA; 12 August 1985
