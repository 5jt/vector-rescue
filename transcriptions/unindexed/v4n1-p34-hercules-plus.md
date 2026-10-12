---
title: 'Hardware Review: Hercules-Plus Monochrome Graphics Card'
authors:
- Adrian Smith
volume: '4'
issue: '1'
page: '34'
unindexed: true
transcribed: 'from page images of VOL.4-NO.1-JULY-1987.pdf, pages 36–38 (printed 34–36); Claude, 2026-10-12'
review: draft
tags:
- reviews
- user interfaces
queries:
- "Contents line “Hercules+”; the printed heading is “Hardware Review / Hercules-Plus Monochrome Graphics Card”. The review ends in the upper half of printed 36; the boxed “Prize Draw Results” below it is its own Contents line (unindexed/v4n1-p36-prize-draw-results.md)."
- "Kept as printed: “defacto standard”; “proprietory print driver”; “Iota-9999” and the symbol names Rho, Iota and Times spelt out; “paragraph markers which come out as ù’s”; “a 256 by 14 reshape of the 44 drop of said file”."
---

*by Adrian Smith*
{ .byline }

### Introduction

The Hercules Graphics card has been the defacto standard in monochrome PC graphics for as long as anyone can remember. It exploits the excellent resolution of the monochrome PC display and allows applications to access individual pixels, rather than just the entire 14 x 9 character cell.

Of course these days you can get cloned versions of practically everything, and ‘Hercules compatible’ cards are well under £100 in the computing magazines. Perhaps it is with this in mind that the Hercules Plus card was developed; it offers everything that the old card had, with one very significant addition – RAMFONT. Just what is a RAMFONT, and why is it significant? I wasn’t quite sure, until I’d plugged in the beast and turned the power back on: things cleared up quite quickly after that!

### Installation

This was straightforward in the extreme. The card was well-packaged, and the instructions very clear. Basically if you just had a single monochrome screen, and were running the printer off the mono adaptor, you could simply swap the cards. If you wanted to install the proprietory print driver to get graphics screen copies, you needed an extra line in the AUTOEXEC.BAT, but that was all there is to it.

The software comes on two (unprotected) disks, and has built-in drivers for Lotus-123, MS WORD, and Framework. Again, you can copy the relevant bits to your working disks. If you take the same attitude to PC software as I do, you will treat the instructions as a refuge of last resort; your first action will be to try something like ‘RAMFONT MEDIEVAL.FNT’ just to see what happens.

The effect is rapid and startling; type DIR and you get a disk directory in the most gorgeous medieval script you could imagine. Type APL and your workspaces take on the aspect of the Book of Kells . . . except of course for all those damned symbols!! My three-year old was quite upset when Rho turned into a square-root, and Iota into a passable imitation of a gallows. As you might expect, the Hercules corporation had catered for practically every taste in the book, except APL. Bother.

### Getting to Know RAMFONT

Of course the ultimate cop-out would have been to plug in the APL ROM; faced with the prospect of re-inventing the entire APL symbol set from scratch, I very nearly gave in and did just that. However, one could make a start somewhere, and there isn’t much to an Iota after all! A quick dip in the manual laid bare the secrets of FONTMAN, and a few trials in DOS suggested SANSERIF as the best place to start, so off we went.

FONTMAN has a lot in common with the GDDM Image Symbol Editor, but is rather easier to use. Basically you can page through the characters with ‘+’ and ‘–’, and use F5 and F6 to turn pixels on and off on a 14 by 8 grid. There are various obscure commands for shifting things up and down, and copying symbols from one character to another. The syntax of these makes EDLIN look sensible; fortunately you don’t need them very often.

A nice feature is the option of replacing the ‘Help’ menu with a display of the entire ASCII set (as redefined) life-size. I found this essential while I was getting some feel for the appearance of the characters I was designing; the alternative of backing off and peering at the screen through half-closed eyes is much less satisfactory!

Iota and Times were easy meat; Rho turned out to be a bit of a pig, and kept me going for close on half-an-hour. I began to suspect that the manual had not been understating the truth when it claimed “Designing legible and attractive characters from a matrix of rectangular dots is a skill that will take time and patience to master.” And so to bed.

The following morning, I was back at my post, hacking out APL on an AT fitted with the Enhanced Graphics Adaptor. Of course I was aware that this too had a soft character set, and the thought began to form that APLCHAR.COM must somewhere define the characters. Why not drag it into APL and do a bit of reverse engineering? Sure enough it turns out that a bit of base-2 encoding on a 256 by 14 reshape of the 44 drop of said file yields a 256 by 14 by 8 bit array defining the entire character set, APL symbols included.

These are not quite appropriate for Hercules use, as you really need a 14 by 9 grid for the mono adaptor. However they are very much better than nothing, and with a couple of hours’ work I can now claim to have a very decent looking Sanserif APL font which is a pleasure to use. By the time you read this, I should have lodged a copy with the Software Exchange; I might also send a copy to Hercules, in the hope that they might include it in future releases.

### Where Next?

Microsoft Word has long been a favourite piece of software; however even on a fast PC/AT it is very slow when scrolling text in graphics mode. So much so that I never use the WYSIWYG option, preferring to run in standard text mode at a reasonable speed. Now I can get the italic bits in italic, the bold bits in bold, and the APL bits in APL, all on the screen at the same time, and all at the same speed as standard text! In fact my plain old PC is about 50% faster than our office AT, which is gratifying, to say the least.

From an APL point of view, there are lots of potential applications where a soft character set could be a real bonus. For some time, I have been working on a factory information system, which uses ‘plant mimics’ to help in the display of data. By re-defining bits of `⎕AV` as valves, taps, and so on, you can do the whole thing in text mode, and consequently get it on the screen in a tiny fraction of the time it would take in graphics. Animation suddenly becomes a real possibility; so far my efforts have been restricted to the use of the cursor keys to control a 4-character mouse (actually 8, for left and right movement), which can be manoeuvred around a simple maze in search of a variety of cheeses!

### Summary

Leaving aside the unfortunate omission of an APL font, it is hard to fault anything about this card. It even seems to speed up ordinary screen handling a tiny bit; I’m sure that Iota-9999 goes past faster than it did before. RAMFONT is a major step forward, in that it finally frees us from chip-swopping, and lets us run APL and (say) Word on the same machine without: (a) funny APL symbols, or (b) paragraph markers which come out as ù’s. We can even stop subjecting DOS to 5-pointed stars!!

To sum up . . . . if you have a monochrome PC and £200 to spend (or that you can con your employer into spending) the Hercules Plus card represents excellent value for money.
