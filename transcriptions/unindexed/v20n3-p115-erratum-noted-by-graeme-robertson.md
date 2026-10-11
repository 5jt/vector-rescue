---
title: Erratum noted by Graeme Robertson
authors:
- Graeme Robertson
volume: '20'
issue: '3'
page: '115'
unindexed: true
transcribed: 'from page image of VOL.20-NO.3-JANUARY-2004.pdf, page 117 (printed 115; within the Technical Section, after its introduction and contents list); Claude, 2026-10-11'
review: draft
tags:
- APL community
- language design
queries:
- "Printed as “Erratum noted by Graeme Robertson” at the foot of the Technical Section’s opening page. It corrects Robertson’s “New Foundations” in 20:1 (art10007380), where p.138 has the heading “3. Promotion of primitives” followed by a run of APL glyphs (perhaps the “printing error”), and the next page has `VF←{1},{⍵},{⍵*2},{⍵*3}`."
---

## Erratum noted by Graeme Robertson

Thanks for printing my *New Foundations* article. There was a small printing error with the APL on the page 138 title line

3\. Promotion of primitives

but that is not very important. There was also a small oversight in the code on the next page on a line which should have read:

```apl
VF←{⍵*0},{⍵},{⍵*2},{⍵*3}
```

because the valence of each function must be explicit or the whole construction of function arrays breaks down. This was part of my motivation for introducing the one-line and no-braces precursor of Dfns.
