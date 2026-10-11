---
title: APL and MS Word for HP LaserJet
authors:
- Rex Swain
volume: '6'
issue: '4'
page: '99'
unindexed: true
transcribed: 'from page images of VOL.6-NO.4-APRIL-1990.pdf, pages 101–102 (printed 99–100; within Technical Correspondence, after unindexed/v6n4-p98-error-trapping-or-event-handling.md); Claude, 2026-10-11'
review: draft
tags:
- system interfaces
- implementations
queries:
- "The last letter in Technical Correspondence, From: Rex Swain, 28 March 1990, followed by an italic Editor’s Note; the next item is John Scholes’s “A New Development Environment for Dyalog APL” (art10007720)."
- "The writer’s postal address in Washington, Connecticut, printed after his name at the end of the letter, is omitted; it is where readers were asked to send diskettes."
- "“Helvetica” is printed in Helvetica, as a sample."
---

*From: Rex Swain, 28 March 1990*
{ .byline }

For quite some time, I have wanted to be able to use my word processor to mix APL with other fonts. I recently took the time to solve this problem, and have developed programs that teach Microsoft Word to treat STSC’s APL font for the HP LaserJet as it would any other font.

Now, I can mix APL symbols such as `⎕←⍳⍴` with Helvetica and Times Roman and any other fonts I have, on the same line or in separate paragraphs. (*so can I …. Ed!*). I format the APL portions with the normal Word commands; Word automatically downloads the APL font when necessary. If you have the STSC APL video characters turned on when you invoke Word, you can toggle between Word’s text and graphics display modes: in text mode you can see the APL characters on the screen; in graphics mode you can see the full PC character set.

Briefly, my programs modify a specified .PRD file, inserting the APL font definition and translate table; create or add to the corresponding .DAT file; and extract the downloadable APL fonts from STSC’s PRINTERS.ASF file. I am willing to distribute these programs on a virtually freeware basis. Anyone who is interested may send me:

- a diskette (360K, or any density 3.5") and a stamped, self-addressed return mailer; or
- for $10, or $15 outside the US, (cash only; no checks) I will supply the diskette (specify size), mailer, and postage.

Requirements are:

- an HP LaserJet printer that accepts downloadable fonts (any model except the original 2686A),
- Microsoft Word version 5.0, and APL\*PLUS/PC version 8 (or higher, I suppose).

Rex Swain

---

*Editor’s Note: this is a rather faster and cheaper way of doing what I do with MS Word and GoScript. We both exploit the availability of APL character drivers (I use the Hercules RAMFONT approach) in similar ways, and we both rely on the excellently open architecture of MS Word.*

*I would still recommend PostScript as the best long-term solution, but if you already have APL\*PLUS/PC and an HP LaserJet, I think Rex’s offer is a most generous and useful one. Many thanks.*
