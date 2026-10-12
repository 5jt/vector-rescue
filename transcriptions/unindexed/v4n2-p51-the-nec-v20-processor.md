---
title: 'Hardware Review: the NEC V20 Processor'
authors:
- Adrian Smith
volume: '4'
issue: '2'
page: '51'
unindexed: true
transcribed: 'from page images of VOL.4-NO.2-OCTOBER-1987.pdf, pages 53–54 (printed 51–52); Claude, 2026-10-12'
review: draft
tags:
- reviews
- performance
queries:
- "The Contents line reads “The NEC-V20 processor”; the printed heading is “Hardware Review: the NEC V20 Processor”."
- "The benchmark tables are printed in an APL font and transcribed as code, with ⍝ for the lamp and ⋄ for the diamond. In the expression 'FAT'⍷S the glyph is an epsilon with an underbar, read as ⍷. The two tables on printed 52 stand side by side, “+/V+V” lower and to the right; they are given one after the other."
- "Kept as printed: “+/S×'T'” as the heading of the first table on printed 52, where the benchmark list has +/S='T'; “timimgs”; the V.5 timings for +/V+V of 5170 at 5000 and 19270 at 15000, out of sequence with their neighbours; “a straight swop”."
---

*by Adrian Smith*
{ .byline }

### Background

The NEC V20 is a straight swop for the standard 8086 CPU chip that comes with your PC. It costs around £18.00, and is claimed to speed up applications by an average of 10%. In particular it improves screen-access times, and anything involving graphics should go up to 50% faster.

Having shelled out my £18 to the imaginatively titled Ctrl-Alt-Deli (waits apprehensively for the machine to re-boot!!) I fired off my usual set of APL benchmarks. One side issue to note is the drop in speed on using APL-V.6 as opposed to APL-V.5 ... for interest I also timed some simple array operations on both versions; you may draw your own conclusions!

### Benchmark Results

Firstly my standard collection from VECTOR 4.1. As previously noted, the simple 1000 looper FN 1000 seems to be the best indicator of overall speed:

```apl
APL Expression                Type        Vn.6     Vn.5     V20(5)
--------------                ----        ----     ----     ------
T←⎕TS ⋄ +/V+V   ⋄ DO ⎕TS-T ⍝ INT ....      390      380      350
T←⎕TS ⋄ +/V[I]  ⋄ DO ⎕TS-T ⍝ INT ....       60       60       50
------------------------------------------------------------------
T←⎕TS ⋄ V+.×V   ⋄ DO ⎕TS-T ⍝ RL  ....      490      440      380
T←⎕TS ⋄ +/V*2   ⋄ DO ⎕TS-T ⍝ RL  ....     4220     4120     3680
T←⎕TS ⋄ X←+/M   ⋄ DO ⎕TS-T ⍝ RL  ....      710      720      660
T←⎕TS ⋄ V+.×,M  ⋄ DO ⎕TS-T ⍝ RL  ....     2360     2360     2140
------------------------------------------------------------------
T←⎕TS ⋄ +/S='T'    ⋄ DO ⎕TS-T ⍝ CH ...    4010     3790     3630
T←⎕TS ⋄ 'FAT'⍷S    ⋄ DO ⎕TS-T ⍝ CH ...      60       60       60
T←⎕TS ⋄ X←S∊'FAT'  ⋄ DO ⎕TS-T ⍝ CH ...    5710     2860     2520
------------------------------------------------------------------
T←⎕TS ⋄ X←B∨B∧~B ⋄ DO ⎕TS-T ⍝ BL....      5710     4950     4840
T←⎕TS ⋄ ∧/B      ⋄ DO ⎕TS-T ⍝ BL....       160      140      110
T←⎕TS ⋄ X←∨\B    ⋄ DO ⎕TS-T ⍝ BL....       320      280      220
------------------------------------------------------------------
T←⎕TS ⋄ FN 10    ⋄ DO ⎕TS-T ⍝ FN....       550      390      330
T←⎕TS ⋄ FN 100   ⋄ DO ⎕TS-T ⍝ FN....      4080     3300     3100
T←⎕TS ⋄ FN 1000  ⋄ DO ⎕TS-T ⍝ FN....     47.7s    34.6s    30.3s
==================================================================
```

... and then the timimgs for some simple array operations to illustrate the precipice at the 32K boundary:

```apl
+/S×'T'

   ⍴S      V.5      V.6
   --      ---      ---
  1000     380      440
  2000     770      820
  5000    1920     1970
 10000    3790     4010
 20000    7630     7910
 30000   11370    11860
 40000     ---     22.9s
 50000     ---     27.4s
 60000     ---     34.4s
100000     ---     WS FULL
                   IN 195K
```

```apl
+/V+V

   ⍴V      V.5      V.6
   --      ---      ---
  1000     380      440
  2000     730      770
  5000    5170     1920
 10000    9610     9670
 15000   19270    18460
 20000   11370    11860
 25000   24500    22900
 30000   28800    27400
 40000     ---    45900

⎕WA 300K APPROX
```

### Conclusion

The V-20 is good value for money in price-performance terms when compared with any of the other 'go-faster' boards, all of which come in well above £500. I could claim to see the difference in `⎕WPUT` and graphics tests, but the improvement is otherwise too marginal to show up in day to day use.

NEC V20 is available from:

<p style="margin-left: 2em">Ctrl-Alt-Deli, 44 Brownbaker Court, Milton Keynes.<br>Cost: £20 approx.</p>
