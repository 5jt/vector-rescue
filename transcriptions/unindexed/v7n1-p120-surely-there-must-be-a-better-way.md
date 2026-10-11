---
title: Surely There Must Be a Better Way ...
authors:
- Adrian Smith
volume: '7'
issue: '1'
page: '120'
unindexed: true
transcribed: 'from page images of VOL.7-NO.1-JULY-1990.pdf, page 122 (printed 120; within Technical Correspondence, after unindexed/v7n1-p119-falkoff-keyboard-franco-belgian-response.md); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- humour
queries:
- "A letter in Technical Correspondence, From: Adrian Smith, 17 June 1990. It is followed on p.121 by Anne D Wilson’s “Speculations on Fermat Equations ...”."
- "In the code fragment the glyphs are read as execute ⍎, drop ↓, grade up ⍋ and (APL\\*PLUS) pick ⊃."
---

*From: Adrian Smith, 17 June 1990*
{ .byline }

Code fragment recently excavated and much pored over ...

```apl
  RC←⍎(1↓⍋(4800,5052)∊⍎∆ADMIN)⊃(('EEV') ('EV'))
```

We believe that this is meant to execute `EV` if `∆ADMIN='5052  '`, otherwise execute `EEV`. Suggestions for simplification welcome!

P.S. The following fragment from John Preston (Saladin) via Bob Poate (MicroAPL):

```apl
  23817 ⎕INT 33
```

This closes a network print file, which will otherwise sit on the print queue until you exit from APL to the DOS prompt. Thanks.
