---
title: Gizz a Font
authors:
- Iain Hayward
volume: '5'
issue: '2'
page: '86'
unindexed: true
transcribed: 'from page images of VOL.5-NO.2-NOVEMBER-1988.pdf, pages 88–89 (printed 86–87; within Technical Correspondence, after John Sullivan’s “Sharing GDDM pages between APL2 and Fortran”, before art10007040); Claude, 2026-10-11'
review: draft
tags:
- implementations
- system interfaces
queries:
- "A letter in Technical Correspondence, From: Iain Hayward, 3rd November 1988; the last under the heading. It follows unindexed/v5n2-p86-sharing-gddm-pages-between-apl2-and-fortran.md."
- "The writer’s home address in Luxembourg is omitted."
---

*From: Iain Hayward, 3rd November 1988*
{ .byline }

I am running APL.68000 on my Amiga at home, but those meanies at MicroAPL Ltd didn’t give me a downloadable font for the printer. In fact printer support for what is otherwise an excellent product is almost nil (more on that later).

If recent claims by MicroAPL are anything to go by then there must be a lot of other users out there with the same setup. Has anyone got a downloadable font for a 24-pin Epson LQ-compatible printer? I’m thinking of making one and it should be quite interesting at first, writing a font editor (in APL of course!) and then designing the first few characters, but after a while it will become tedious and very time-consuming. I know because I have already done one for the Epson FX80. On that occasion the font editor was knocked up for me by Maurice Jordan in what seemed like a few minutes (including full-screen interface and automatic validation) in a remarkable demonstration of what a serious APLer can do with this language. Even with that program it still took a long time to design the whole font and I am therefore reluctant to do it all again unless it’s necessary.

Why should we just give him a font that took us so long to make? I hear you ask. Well, if you’ve got the same setup as I have then you may still be having problems with printing. This is where a C programmer comes in handy (like me). Amiga APL.68000’s printer support only goes as far as giving you a copy of what appears on the screen, including the input lines unfortunately. The manual says that if you want to do more than this (i.e. print reports, workspace documentation, etc., like most people) then you will need to use the ‘Arbitrary Input/Output’ functions. However, this only works with the serial port, fine for comms, but most people have their printer connected to the parallel port.

My solution to this problem so far, is to write output into a temporary DOS file first, and then (via a DOS window) run a C program which does a character translation and sends the output to the printer. I am thinking of writing a special printer driver so that I can send APL output directly to the printer. This won’t be easy, but it should be worth it in return for a nice font.

By the way, did anyone see David Eastwood’s article on idioms in the latest edition of MicroAPL News? Neat example of the use of not-equals-scan, wasn’t it?

Yours sincerely,

Iain Hayward
