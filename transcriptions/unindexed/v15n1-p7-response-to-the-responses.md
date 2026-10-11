---
title: A Response to the Responses in Vector...
authors:
- David Piper
volume: '15'
issue: '1'
page: '7'
unindexed: true
transcribed: 'from page images of VOL.15-NO.1-AUGUST-1998.pdf, pages 9–10 (printed 7–8; within Correspondence, the first letter under the section heading); Claude, 2026-10-11'
review: draft
tags:
- performance
- development practice
queries:
- "A letter in Correspondence, From: David Piper, 30 July 1998; the first letter in the section, followed by Roger Hui’s report “Honorary Doctorate for Ken Iverson” (art10003880). It answers the letters on his Niven-number code in Vector 14.4 (Correspondence, art10010280)."
- "The writer’s e-mail address, printed after his name in the heading, and his postal address, printed below the letter, are omitted."
---

*From: David Piper, 30 July 1998*
{ .byline }

Well, it made for an interesting edition of Vector, if nothing else. First, blame the guilty parties — OK *mea culpa*. All transcription errors were entirely my own, I could of course blame the technology (I don’t have), or the blinding heat of enthusiasm. But no, when it comes right down to it, I transcribed some of the code wrongly. Much amusement engendered, tongue-in-cheek articles etc. etc. etc. For Phil Last’s benefit — the code did run and the timings were genuine...

However let’s not throw the baby out with the bath water. The message I was trying (some might say failing) to get across was simply that it’s not worth trying to speed up code by taking advantage of some quirks in one (or more) interpreters when there remains a lot you can do simply by making the algorithm more appropriate (to APL in this instance).

In the original article the algorithm implemented worked on a one-at-a-time basis — a sure fire recipe for bad performance in APL. So attention should be focussed on creating a parallel algorithm rather than on tweaking the code. Sometimes — as in this example — the changes required to move from one-at-a-time to many-at-a-time are minimal and the benefits so significant that further tweaks are probably not justified. In other cases creating the parallel algorithm is so difficult (a.k.a. impossible) that we have to end up resorting to tweaks.

Even where parallel algorithms are too costly to justify their development, there are techniques such as loop-hoisting (i.e. ensuring loop invariant lines of code are outside the loop) which should be applied before (potentially) interpreter dependent tweaks. Most experienced practitioners do this sort of thing automatically, so the scope for deriving benefits may be limited — but where they can be applied, such techniques can give rise to substantial benefits.

Claude Henriod makes some interesting and valid points in his response. Maybe it was a mistake to introduce the concept of “style” into my original letter — after all style is subjective. I stick by the use of longer variable names — because I find they make life easier. I plead guilty to the complex path issue — maybe with more thought I would have improved this.

I stoutly defend the “only one assignment per line” rule. The problem with assignments is that they are essentially side-effects. If you adhere to the rule of one-assignment-per-line then you stand a chance of being able to restart any line when it collapses with an error. Assuming of course that side effects have not been created by other actions (like shared variable activity, system function activity or the use of global variables in functions invoked on the line — maybe these are also the basis for important style guidelines). So in the interests of being lazy (something which I find appeals to a lot of people), stick to one assignment per line.

Anyone want to think about diamonds?

David Piper
