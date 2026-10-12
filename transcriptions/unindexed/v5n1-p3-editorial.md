---
title: 'Editorial: Don’t Lose Touch'
authors:
- Adrian Smith
volume: '5'
issue: '1'
page: '3'
unindexed: true
transcribed: 'from page images of VOL.5-NO.1-JULY-1988.pdf, page 5 (printed 3); Claude, 2026-10-12'
review: draft
tags:
- system interfaces
- data and files
---

*by Adrian Smith*
{ .byline }

This VECTOR is all about interfaces. I hate interfaces! At least 90% of the hassle generated during any APL project is at the edges, where the array structure of APL fails horribly to dovetail with the files and records used by everyone else.

The projects I like best are the little hole-and-corner ones, where my file system is called )SAVE and I don't have to bother my head with the niceties of packed-decimal, or the inner secrets of the Lotus worksheet. So ... why a VECTOR about all the things I detest most in this life?

- it is an unfortunate fact that systems generally have users, and users soon get tired of copying figures off their CICS screens so they can type them in to your APL model. They start saying unreasonable things like "... but it's all on the same computer ...", as if this made life any easier for you.
- the PC DOS standard has made a huge psychological difference. A PC user assumes that any package he buys will (with a bit of frigging around) read data from any other package. He is much less willing to accept excuses from the mainframe brigade about incompatible formats, or variable length records, or whatever.
- things are gradually getting better. As mainstream data starts to find its way into databases like DB2 and Oracle, the APLer's life suddenly becomes bearable. At long last, we get data back in tables, organised into rows and columns!

In summary: we can't ignore this problem; it won't go away; and our best excuses don't wash any more. We have to face up to it, and we need all the tools and techniques we can get. In the mainframe world we use things like AP123 to read VSAM data, and where necessary we get new interfaces made to order, for example from APL\*PLUS to DB2. At the VAX and PC level, I am more and more convinced that we need to accept C as our programming partner. Unix is written in C, and so is almost any PC package you care to name. If you want to talk to them, you are going to have to talk in C. (You could try shouting in APL, but I don't think it would work.)

This all means broadening our horizons quite dramatically; I hope the papers in our technical section give you the start that you need.
