---
title: 'Technical Editorial: More on APL2'
authors:
- Jonathan Barman
- David Ziemann
volume: '2'
issue: '3'
page: '93'
unindexed: true
transcribed: 'from page image of VOL.2-NO.3-JANUARY-1986.pdf, page 95 (printed 93; an advert on p.94; the technical correspondence follows on p.95); Claude, 2026-10-05'
review: draft
queries:
- "“the old problem of equating the cost of people with the cost of hardware resurfaces” is printed so (the sentence lacks a verb for “nested arrays”)."
---

by Jonathan Barman and David Ziemann
{ .byline }

We are starting to get feedback from you on APL2. In this issue we are pleased to include two very different views – a report of the problems migrating to APL2 and a look at the joys of APL2 operators.

The most extensively used new feature of the language must surely be the ‘each’ operator, which loops through an array applying a function to each of its items. Of course, it’s still early days, but already we’re getting a feel for how ‘each’ is being used; in one sense it takes all the clever bits out of APL, as one user commented. APL often attracts those who enjoy being intellectually stimulated, and if there’s a faint possibility that a problem can be solved without looping they will spend hours searching for an arcane parallel construct. With the new operator the looping solution can be coded directly by using a defined function with ‘each’. In this way the thought processes of ordinary mortals can be implemented in the most obvious way. Even so, we expect that there will be plenty of amazing code written in APL2!

What about the question of APL2 CPU requirements? Has anyone made any studies yet? In general, nested arrays will need more CPU and memory, and the old problem of equating the cost of people with the cost of hardware resurfaces. Good programmers are getting more and more expensive, while the hardware (and software?) is getting relatively cheaper, but if a big new machine is required to run the language then careful evaluation is called for. The argument hasn’t really changed –

> The cost of running a system includes the cost of its development, and APL2 can be expected to show an overall improvement in many cases.

What of the future of APL2? There are some encouraging signs that links to the APL2 environment are attracting users of other programming languages to APL2. In particular, the ability to access ISPF service routines through a shared variable, and the SQL/DB2 database should cause users of those products to take a serious look at APL2. Also the ‘name association’ feature of the newly announced Release 2 of APL2 further increases the ability of APL2 to communicate with its environment. The quadNA system function allows you to treat an external program as if it were a defined function within the APL2 workspace – a very powerful feature. (That’s how IBM provide the valuable ‘partitioned-enclose’ facility, sadly missing from the base product).

Another big boost for APL2 would be its availability on a personal computer, and it should now be possible to run APL2 under VM on an AT/370. If only IBM can keep the price of the software low enough this might be the route to the mass market we’ve all been waiting for.

We hope that VECTOR will become a useful forum for discussing APL2, so please share your views and discoveries with the other readers. If you’ve found any incompatibilities from VS APL, or bugs in APL2 we’d like to hear from you too.
