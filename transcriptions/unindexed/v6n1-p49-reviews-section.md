---
title: Reviews Section (introduction)
authors:
- Adrian Smith
volume: '6'
issue: '1'
page: '49'
unindexed: true
transcribed: 'from page image of VOL.6-NO.1-JULY-1989.pdf, page 51 (printed 49; introduces the Reviews section, before The CIPS APL Toolkit on p.51; p.50 is a Dyalog APL advertisement); Claude, 2026-10-12'
review: draft
tags:
- reviews
- performance
queries:
- "Printed heading “Reviews Section”, with “introduction by Adrian Smith”."
- "The benchmark table is set in APL type; transcribed in a code block with its printed layout. The Contents line REVIEWS had no page; given 49 here, although the APL Product Guide (p.39) is listed under it."
---

## Reviews Section

*introduction by Adrian Smith*
{ .byline }

Thanks to Jonathan Barman, Anthony Camacho and Jonathan Martin for completing three excellent reviews to a very tight schedule.

We have a much fuller technical review of the IBM APL2/PC product which will be carried in the next VECTOR. Unfortunately the twin constraints of space and time conspired to keep it out of this issue. Just for fun, here is a selection of the infamous ‘Smith Benchmarks’ as first seen in VECTOR Vol.1 No.4 page 55:

```
BENCHMARK              APL*PLUS/PC V.8        APL2/PC 32-BIT
---------              ---------------        --------------
⎕WA                         220K                  3.6M

+/V+V                        60                   <50
+/V*2                       350                   160
V+.×,M                      220                   110

+/S='T'                     550                   490
X←S∊'FAT'                   550                  1260

X←B∨B∧~B                    770                   <50

FN 1000                    5200                  6810
```

The tests were run on a PS/2 Model-70 (16 MHz) with 4Mbyte of memory and a maths co-processor fitted.
