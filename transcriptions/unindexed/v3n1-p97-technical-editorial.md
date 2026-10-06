---
title: Technical Editorial
authors:
- Jonathan Barman
- Dave Ziemann
volume: '3'
issue: '1'
page: '97'
unindexed: true
transcribed: 'from page image of VOL.3-NO.1-JULY-1986.pdf, page 99 (printed 97; an advert follows on p.98; the technical correspondence follows on p.99); Claude, 2026-10-05'
review: draft
tags:
- APL community
queries:
- "Slip transcribed as printed: “a mixture of APL and other languages are used”."
---

by Jonathan Barman and Dave Ziemann
{ .byline }

The objective of anyone creating a system is to make it work well and not spend too much time programming it. APL is but one of the tools that a programmer can use, and if other languages or systems can do a specific job better and quicker than APL there is no good reason not to use them. Often a mixture of APL and other languages are used so that we can have the best of both worlds; sometimes the bulk of the processing can be handled by a package and the twiddly bits dealt with in APL, and occasionally APL is just too slow for a particular process, and so it has to be written in a compiled language.

A large amount of APL is already mixed with other systems. The typical PC user does a bit in APL, comes out to the DOS environment to run packages such as DBASE or SYMPHONY, goes back into APL and does more work. Similarly, the IBM VSAPL user running under TSO will intersperse APL with ISPF sessions. The switching process can be automated with BAT, CLIST or EXEC files. If an extensive amount of work is done before switching to the next environment then this method works well. If, however, the amount of work done outside APL is small and the switching between systems is frequent, then this method works very slowly. The APL interpreter is a large beast and loading it takes time, so nipping in and out of APL slows things down. The alternative is to load APL and stay there, running other applications as and when required. This is the best method where small programs need to be run quite frequently. The problem here is that every APL interpreter seems to have a completely different way of accessing the outside world and running programs; some easy, some quite tricky, and some impossible. The impossible is usually deliberate, for example a timesharing bureau will need to guarantee complete security and if assembler programs could be run the security might be compromised. It is normally easy to run programs that are designed to be called directly as independent units, but it is usually much more difficult to run programs that manipulate data in the workspace, as one needs to know quite a lot about the internal structure of the interpreter.

APL2’s Name Association facility looks as if it will make calling programs much easier. The quadNA system function is available in Release 2 of the product, and allows external programs to be invoked as if they are locked APL functions.

For some time a shared variable processor has been available for VSAPL which does a similar sort of job, but there does not seem to be anything comparable for the other APL interpreters.
