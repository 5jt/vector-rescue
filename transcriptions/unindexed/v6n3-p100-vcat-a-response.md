---
title: 'VCAT: A Response'
authors:
- Norman Thomson
volume: '6'
issue: '3'
page: '100'
unindexed: true
transcribed: 'from page images of VOL.6-NO.3-JANUARY-1990.pdf, pages 102–103 (printed 100–101; within Technical Correspondence, after unindexed/v6n3-p97-yet-more-on-that-ambivalent-operator.md); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- performance
- education
queries:
- "A letter in Technical Correspondence, headed “VCAT: A Response”, unsigned at the head and signed at the foot by Norman Thomson, IBM UK Laboratories. It answers Peter Branson’s VCAT in The Education Vector of 6:2 (“Start Building your own Utilities”). The editor’s italic note and timing table that follow it on p.101 are included here. Peter Biddlecombe’s “SHARP APL Event Trapping” (art10000990) follows on p.102."
- "The postal address in the signature block (Mail Point 188, Hursley Park, Winchester) is omitted; the name of the writer’s organisation is kept."
- "In the timing table NT and PB are Norman Thomson and Peter Branson; the units of the timings are not stated."
---

While it gives me great pleasure to see Peter Branson’s contribution to the Education Vector (Vol.6 No.2) I wonder whether his *VCAT* example reflects the ways in which we should be encouraging APL newcomers to tackle such a problem now that APL2 is becoming so commonplace that even kids can have it for nothing (providing of course that they have access to a computer made by a certain well-known manufacturer...!)

The modern didactic view of this situation is to make each of the two matrices into vectors of the rows (`⊂[2]¨`), join them (`,/`), then restore the second dimension by de-nesting (`⊃`).

Here is the function:

```apl
[0]    Z←L VCAT R
[1]    Z←⊃⊃,/⊂[2]¨L R

      LEFT RIGHT
BREAD  MAN
FRUIT  CAN
       EAT

      LEFT VCAT RIGHT
BREAD
FRUIT
MAN
CAN
EAT
```

The second disclose is necessary on account of the implicit enclosure arising from the derived function `,/`.

This *VCAT* is fine provided both arguments are matrices. If the function is to work with vectors or scalars, we have to generalise `⊂[2]` to:

```apl
[0]    Z←EXPAND R
[1]    Z←⊂[⍴⍴R]R←1/R
```

`1/R` which makes *R* into a 1-item vector if it is a scalar, otherwise does nothing.

Rewriting *VCAT* we have:

```apl
[0]    Z←L VCAT R
[1]    Z←⊃⊃,/EXPAND¨L R

      LEFT VCAT '3'
BREAD
FRUIT
3
      3 VCAT 4
3
4
      'PIG' VCAT 'SHEEP'
PIG
SHEEP
```

Norman Thomson  
IBM UK Laboratories

*Ed: this looked interesting enough to time! From the results below, I would have to say that I side with Peter, at least until someone comes up with an interpreter that will run Norman’s code as fast for realistic sizes of data!*

```apl
+-----------------------------------------+
|         |         |      Z←L VCAT R     |
| ⍴LEFT   | ⍴RIGHT  |    NT    |    PB    |
|         |         |   VCAT   |   VCAT   |
|---------|---------|----------|----------|
|  2   5  |  3 3    |   270    |   380    |
| 12  80  |   23    |  1480    |   390    |   ⍝ screen builder
| 56 132  |   63    |  9500    |   450    |   ⍝ report builder
+-----------------------------------------+
```
