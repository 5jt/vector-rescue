---
title: 'Hackers’ Corner: Reshaping your Mouse'
authors:
- Adrian Smith
volume: '8'
issue: '4'
page: '112'
unindexed: true
transcribed: 'from page images of VOL.8-NO.4-APRIL-1992.pdf, page 114 (printed 112); Claude, 2026-10-12'
review: draft
tags:
- user interfaces
- programming techniques
queries:
- "The underlined delta of `⍙mouse` is transcribed ⍙; the mouse character in the example is printed as a domino glyph, transcribed ⌹."
---

*by Adrian Smith*
{ .byline }

There are times when a simple reverse-video block is not the kind of mouse pointer you need. To save you the (not inconsiderable) effort of decoding the appropriate page of Ray Duncan's book, here is a simple extension to `MSΔINIT` which does the trick:

```apl
    ∇ CH MSΔINIT CU;RC

[1]    ⍝ Initialize mouse ... sets global ⍙mouse←1 if OK ... else 0
[2]    ⍝ CU is the cursor type ... 0=mouse cursor; 1=hardware cursor
[3]    ⍝ (CH) is the character and colour to be used for the mouse block.

[4]     RC←0 ⎕INT 51 ⋄ ⍙mouse←0≠1↑RC ⋄ →⍙mouse↓0
[5]     →CU↑Hw ⋄ →(⎕NC 'CH')↓0

[6]    ⍝ Use left arg as mouse character, possibly with colour ...

[7]     ⍎(0≠1↑0⍴CH)/'CH←¯1+⎕AV⍳CH'

[8]    ⍝ Colour defaults to bright white ...

[9]     CH←2↑CH,15

[10]   ⍝ CX is set to 'F000' Hex to retain background only;
[11]   ⍝ DX is the encoded character and foreground ...

[12]    RC←(10 0 ,¯4096,CH[1]+256×CH[2])⎕INT 51 ⋄ →0
[13] Hw:RC← 10 1 ⎕INT 51
    ∇
```

This defaults to the normal mouse block, unless you provide a left argument. This may specify the mouse character (as a character scalar or `⎕AV` index), and optionally a colour. APL\*PLUS II users should note that the `¯4096` is really Hex(F000), but that in APL\*PLUS/PC you trip over the 2-byte integer line, and have to pretend that you mean Hex(-F + FFF).

```apl
'⌹' MSΔINIT 0     ⍝ Mouse pointer is a white Domino ...
4 14 MSΔINIT 0    ⍝ ... or a yellow diamond!
MSΔSHOW           ⍝ Let's see it!
```

That's it folks. Next issue, the .EPS format exposed, or how to get your fancy PostScript graphs into MS Word, Aldus PageMaker and so on. Watch this space.
