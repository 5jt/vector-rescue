---
title: 'Hacker''s Corner: Beware the M61'
authors:
- Adrian Smith
volume: '6'
issue: '3'
page: '90'
unindexed: true
transcribed: 'from page images of VOL.6-NO.3-JANUARY-1990.pdf, page 92 (printed 90); Claude, 2026-10-12'
review: draft
tags:
- implementations
queries:
- "Contents line “Hackers Corner: Beware the M61”; the printed heading is “Hacker’s Corner: Beware the M61”."
- "The follow-up, “M61 Problem: Partial Resolution”, is in Vector 6:4 (unindexed/v6n4-p94-m61-problem-partial-resolution.md)."
- "The character the left shift key gives is printed as the APL glyph ⊃."
- "Kept as printed: “swop”."
---

*by Adrian Smith*
{ .byline }

**\*\* Urgent Warning \*\* \*\* Urgent Warning \*\* \*\* Urgent Warning \*\* \*\* \*\* \*\* Urgent Warning \*\* \*\* Urgent Warning \*\* \*\* Urgent Warning \*\***

Should you be contemplating the purchase of an IBM PS/2 model-70 M61 to run your APL\*PLUS/PC systems .... don't! Rowntrees have just taken delivery of 5 of these machines, and so far none of them will reliably get beyond `CLEAR WS`. I think that the problem is rooted in the new half-size motherboards, my evidence for this conjecture being:

- I use the (now obsolete) 16 MHz F61, and have had a happy and trouble-free time. My colleague took delivery of an ostensibly identical machine, which gave the weird symptoms outlined below. Accordingly we called in IBM to fix the machine, and here the fun began. The engineer attempted to swop the motherboard for the one he had brought with him, and found to his astonishment that it wouldn't fit, as the F61 had a strange half-size board he had never seen before. He checked that his (full-size) board was the correct one, and did a bit of nifty rewiring of the speaker leads to make it fit. The machine has run trouble-free ever since.
- IBM then quietly withdrew the F61, and are shipping the 20MHz M61 in its place. The very first of these showed the same symptoms as the above-mentioned F61, and on removing the case we observed the same half-size board! We already had several of these on order, and sure enough, they all behave in exactly the same way!

The effect occurs at random, but seems to be easier to produce on a fully warmed up machine. Essentially, APL completely loses track of the keyboard, such that (for example) the left shift key gives an ⊃, the escape key gives F1, and the Prt-Scrn key reboots! Obviously, a power-off reset is the only escape from this state! On two occasions, APL continued to work normally, but on exit to DOS the symptoms manifested themselves as described above.

I am told that IBM have accepted that there is a problem with one of the EPROMs on the motherboard, but I have not yet (27th Jan) heard of a date when a replacement is likely to be shipped.
