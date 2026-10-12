---
title: Benchmarks Updated
authors:
- Adrian Smith
volume: '3'
issue: '1'
page: '44'
unindexed: true
transcribed: 'from page image of VOL.3-NO.1-JULY-1986.pdf, page 46 (printed 44); Claude, 2026-10-12'
review: draft
tags:
- performance
- implementations
queries:
- "Contents line “PC Benchmarks updated”; the printed heading is “Benchmarks Updated”."
- "Kept as printed: the machine is called “IBM RT PC” in the introduction but “IBM PC/RT” in the table and text."
---

*by Adrian Smith*
{ .byline }

## Introduction

VECTOR (Vol. 1, No. 4) included some highly unrepresentative benchmarks of various APLs on the IBM PC and the MicroAPL Sage. Several of these were specifically set up to sniff out oddities in the various interpreters, and are probably worse than useless in comparing the speed of the computers themselves. Having had a chance to play with Dyalog APL on the DEC MicroVAX and also on the IBM RT PC (or 6150 as it wishes to be known in this country), I thought readers might be interested in the average performance of the most basic benchmarks across all the tested machines.

## Benchmark Results

The times are all relative to the standard PC running APL\*PLUS/PC with the co-processor fitted. It was not fitted in the PC/AT. The ‘real’ and ‘integer’ figures are averages of the three tests shown before; the ‘function’ figure represents a simple 1000-looper, which I have found (Dyalog would agree with this) is probably the best test you can perform to get a good all-round picture of application speed.

| Computer | Integer | Real | Function |
|---|--:|--:|--:|
| IBM PC (8087) | 1.0 | 1.0 | 1.0 |
| IBM PC/AT | 1.8 | 3.2 | 3.0 |
| Sage (APL.68000) | 2.8 | 3.8 | 3.9 |
| DEC MicroVAX | 1.9 | 6.1 | 2.6 |
| IBM PC/RT (Dyalog APL) | 3.0 | 5.9 | 5.8 |

The DEC MicroVAX was the fastest floating-point machine, but was otherwise rather disappointing, being slightly slower than the PC/AT at function execution. I gather from Dyalog that the C-compiler is less than clever at procedure calling, so their APL (being a nice modular beast) is badly penalised.

The IBM PC/RT was (across the board) an impressive machine; marginally slower than the MicroVAX on intensive floating-point, but way ahead of the rest on all-round performance. Running it multi-user had a barely-detectable effect on elapsed times.
