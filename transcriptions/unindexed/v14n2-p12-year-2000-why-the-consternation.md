---
title: Year 2000 — Why the Consternation?
authors:
- Anne Wilson
volume: '14'
issue: '2'
page: '12'
unindexed: true
transcribed: 'from page images of VOL.14-NO.2-OCTOBER-1997.pdf, pages 14–15 (printed 12–13; within Correspondence, after M.E. Martin’s “Re: Year 2000”); Claude, 2026-10-11'
review: draft
tags:
- development practice
queries:
- "A letter in Correspondence, From: Anne Wilson, August 1997, replying to Bob Brown’s “Year 2000 — why the Consternation?” (Vector 14.1; unindexed/v14n1-p8-year-2000-why-the-consternation.md); followed by William Jones’s “Heron’s Rule and Integer Area Triangles”."
- "The writer’s postal address, printed below her signature (Anne D. Wilson), is omitted."
---

*From: Anne Wilson, August 1997*
{ .byline }

Bob Brown’s letter on this subject (*Vector* 14.1) shows a somewhat myopic view, looking at the problem from the point of one application maintained by one person. But the world is bigger than that, and *many mickles make a muckle* — a large number of little problems create a big problem.

Some problems will be external to the applications. The clock on my Compaq thinks that the date following 31/12/1999 is 4/1/1980 — one wonders why it is not 1/1/1980? If I then set it to the correct date most things are as expected. However, at least one accessory loses the ability to put a correct creation date on files. I can reset the date, but what would happen if the computer were controlling machinery?

In many commercial businesses there will be hundreds, if not thousands, of applications — and they all need testing and checking. Much of this code will have been written many years ago by programmers long since departed from the programming arena of that company — whereabouts in the programs does date processing occur — how many places does it need to be changed — what functions does it perform? A single programmer still maintaining his own code should find it easy to identify and correct, but who knows the workings of the mind of a long-departed programmer; who knows where to look for dates in code whose very purposes are lost in the mists of time, with many users and many alterations?

Files may not contain sufficient digits to hold years as 4 digits. To change the file layouts for many files, perhaps with many different date fields, can create a large implementation problem — imagine the potential size of the problem if it is for an insurance company or bank! And every program will probably need to be altered, even if only by recompilation. As this may originate from old Cobol programs, when storage was an expensive consideration, there may be thousands of references to 6-digit picture fields — how many need to be altered?

Bob describes his method of adding the extra two digits for dates; this makes assumptions about which hundred-year time slot is needed. Such assumptions require knowledge of the system, and may well precipitate more alterations at some later date. Does his system cope correctly with the Queen Mother’s date of birth in August 1900?

A decade ago many commercial programs had a life expectancy of 7 or 8 years; even databases were changed with amazing frequency. I can smugly say that all the systems I had control over hold 4-digit years; but I cannot say the same for the hundreds of programs in which I have been involved, but did not control. Way back in 1971 there were panics over the decimalization of money. What will the next panic problem be?

Anne D. Wilson
