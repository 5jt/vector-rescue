---
title: The APL*PLUS ‘dead key’ Problem ...
authors:
- Cedric Heddle
volume: '7'
issue: '1'
page: '118'
unindexed: true
transcribed: 'from page images of VOL.7-NO.1-JULY-1990.pdf, page 120 (printed 118; within Technical Correspondence, after unindexed/v7n1-p117-inverse-operator-in-apl2-5.md); Claude, 2026-10-11'
review: draft
tags:
- user interfaces
- implementations
queries:
- "A letter in Technical Correspondence, From: Cedric Heddle, 12 June 1990, signed “Cedric Heddle, APL Impetus Ltd.”. It is followed on p.119 by Alain Delmotte’s “The Falkoff Keyboard: a Franco-Belgian Response!”."
- "The printed heading has quotes round dead key: “The APL*PLUS ‘dead key’ Problem ...”; the sweep’s Contents item had none, and now has them."
---

*From: Cedric Heddle, 12 June 1990*
{ .byline }

I hope that one of your readers may be able to tell me how to solve the ‘dead key’ problem on UK PS/2 keyboards when using STSC APL\*PLUS/PC and the Unified keyboard. The key is immediately to the left of ‘Z’, has a key button number of 45, a scan code of 86 and in DOS it produces ‘/’ when unshifted and ‘|’ when shifted. Apparently this key does not exist on American keyboards, whose left-hand shift key is wider than those on the UK keyboard.

STSC say that they believe that the scan code for this key is 86 and that their `⎕POKE 198 197` code should work with this key, although they do not have a UK keyboard with which to test this belief. In my experience, this key remains dead despite poking characters into the 86th row of the keyboard table. I have even poked into every one of the twenty or so empty rows in the 128-row keyboard table without having any effect on this key. Incidentally, the shifted ‘/’ above ‘8’ on the numeric pad, which also produces a ‘/’ seems also to be unchangeable.

An assembler routine executed via `)CMD` confirms the BIOS scan code of 86. If any of your correspondents has a solution I am sure I shall not be the only grateful reader.

Yours sincerely,

Cedric Heddle,  
APL Impetus Ltd.
