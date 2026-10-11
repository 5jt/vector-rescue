---
title: 'Hackers'' Corner: DOS Environment Variables'
authors:
- John Sullivan
volume: '6'
issue: '2'
page: '115'
unindexed: true
transcribed: 'from page images of VOL.6-NO.2-OCTOBER-1989.pdf, page 117 (printed 115; within Technical Correspondence, the first letter, after Adrian Smith’s “Hackers Corner: 256 VGA Colours”); Claude, 2026-10-11'
review: draft
tags:
- system interfaces
- programming techniques
queries:
- "A letter, From: John Sullivan, 17th July 1989, replying to Adrian Smith’s Hackers Corner “DOS Environment Variables” in Vector 5.4 (art10008260)."
- "The writer’s postal address, printed below the letter, is omitted."
- "Kept as printed: the function is printed as `SSTOMAT` but named “SStoMAT” in the text."
---

*From: John Sullivan, 17th July 1989*
{ .byline }

What is all this hacking around with Program Segment Prefixes? Has anybody tried to do this in APL\*PLUS II? No? - Good, because it doesn’t work. However, try the following which does work in both APL\*PLUS/PC and APL\*PLUS II:

```apl
     ∇Z←DOS∆ENV
[1]   ⎕CMD 'SET > SETOUT.TXT'
[2]   'SETOUT.TXT' ⎕NTIE 158
[3]   Z←⎕NREAD 158 82,(¯1+⎕NSIZE 158),0
[4]   ⎕NUNTIE 158
[5]   ⎕CMD 'DEL SETOUT.TXT'
[6]   Z←SSTOMAT ⎕TCNL,Z~⎕TCLF
     ∇
```

Where `SStoMAT` is supplied in STSC’s ASMFNS and is the equivalent of your `∆TAB`.
