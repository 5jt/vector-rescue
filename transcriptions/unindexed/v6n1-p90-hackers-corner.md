---
title: "Hacker's Corner: Where to Zap APL*PLUS Version-8"
authors:
- Adrian Smith
volume: '6'
issue: '1'
page: '90'
unindexed: true
transcribed: 'from page images of VOL.6-NO.1-JULY-1989.pdf, page 92 (printed 90); Claude, 2026-10-12'
review: draft
tags:
- programming techniques
- implementations
queries:
- "Contents line “Hackers Corner”; the printed heading is “Hacker's Corner: Where to Zap APL*PLUS Version-8”."
- "The search string in the NFIND example is printed in PC line-drawing characters (a long double rule with a corner); the two lines, expression and result, are kept as an image."
- "The function headers are underlined with dashes in print; the underlines are not reproduced. ΔEXE is printed with an underscored delta (⍙EXE); PUTΔBAN has a plain delta."
- "Kept as printed: “Version-8” with Release 6 examples (ZAP6.EXE). In line [2] of NFIND, “R←⍬” is printed with the θ-like APL*PLUS zilde."
---

*by Adrian Smith*
{ .byline }

I eventually became bored with the exercise of tracking down the banner in APLx.EXE, so I wrote a function to do it for me ...

```apl
     R←STRING NFIND FI;LEN;OFF;IN
[1]      ⍝ Returns position of <STRING> within DOS file (origin-0)
[2]       FI ⎕NTIE ¯2 ⋄ LEN←⎕NSIZE ¯2 ⋄ OFF←0 ⋄ R←⍬
[3]      ⍝ Now check file contents in 4000-byte segments ...
[4]  LOOP:IN←⎕NREAD ¯2 82 ,(4000⌊LEN-OFF),OFF
[5]       R←R,¯1+OFF+(IN ⎕SS STRING)/⍳⍴IN
[6]       →(LEN≤OFF+4000)↑DONE
[7]       OFF←OFF+4000 ⋄ →LOOP
[8]  DONE:⎕NUNTIE ¯2
     ∇
```

Version-8 is a distinct improvement on its predecessors, as you only need to replace the banner. In earlier releases you had to obliterate the serial number and release information as well! It now has the good sense to detect that the banner has altered, and to suppress the version and serial information. This is probably just as well, as it checks for a valid number before it will load at all!

Here is the much simplified function to install your own signon banner:

```apl
     BNRPOS PUTΔBAN BANNER
[1]  ⍝ Patch in <BANNER> to file ⍙EXE at <BNRPOS>.....
[2]   ⍙EXE ⎕NTIE ¯1
[3]   (631↑BANNER,⎕TCNL,630⍴⎕TCNUL)⎕NREPLACE ¯1,BNRPOS
[4]   ⎕NUNTIE ¯1
     ∇

     ⍙EXE←'ZAP6.EXE'                         ⍝ .... set filename
     140932 PUTΔBAN 'HELLO FROM APL6'        ⍝ Replace current banner
```

Maybe one day they will get the message and restore the B= option.

![The expression '…' NFIND 'ZAP6.EXE' ⍝ Release 6, where the quoted string is a run of line-drawing characters, with its result 140932](v6n1-p90-hackers-corner/nfind-banner.jpg)

```apl
     BNR←153429          ⍝ Vn8
     BNR←102804          ⍝ Vn8 with SM
```
