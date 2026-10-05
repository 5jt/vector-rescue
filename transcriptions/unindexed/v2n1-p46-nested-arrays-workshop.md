---
title: Nested Arrays Workshop, April 26th 1985 (meeting notes)
authors:
- Adrian Smith
volume: '2'
issue: '1'
page: '46'
unindexed: true
transcribed: 'from page images of VOL.2-NO.1-JULY-1985.pdf, pages 48–49 (printed 46–47; heads art10002640, Crossley’s paper, on p.48); Claude, 2026-10-05'
review: draft
queries:
- "Notes on four talks: Crossley (written up in full as art10002640), Bryant, Robertson and Scholes. The Scholes notes on p.47 have their own heading and byline (“by John Scholes (Dyalog)”), though they are Adrian Smith’s notes on Scholes’s talk; transcribed as an H2 section with the speaker in italics, like the others."
- "Printed “APL*PLUS” with an asterisk; transcribed with an escaped asterisk."
---

The Royal Over-Seas League

by Adrian Smith
{ .byline }

## Introduction

A most invigorating meeting, with four contrasted but fascinating papers. David Crossley began with a useful summary of the logical structure of the nested systems, and then went on to show how it was physically implemented on APL\*PLUS. My interest had already been aroused by some examples in the Interprocess Newsletter (the topic was the extension of their AFM file package to include APL2) which showed how a 7-element character vector could be combined with a 2 by 3 integer matrix to occupy an astonishing 95 bytes of storage! For more details, have a careful look at David’s paper, which follows these notes.

## APL2 and SQL/DS

*David Bryant (IBM)*

To some extent, this talk assumed a basic knowledge of what SQL is and does. My impression is that it provides a very high-level query capability (of the ’FETCH this WHERE that OR the other’ variety) for good old fashioned batch languages like PL/1. It applies this language to IBM’s relational database (called DB2) to give programmers an extremely powerful tool for application development. Many SQL expressions look so like the sort of things we write in APL that I seriously wonder if APL was used to prototype it!

David first made the point that the interface to SQL is pretty well the same under VM/CMS and TSO. It effectively gives ‘pipeline’ access to SQL commands, and a few simple cover functions will make APL access to SQL look just like PL/1 or whatever. However APL has one great advantage over other languages when it comes to dealing with the results of the SQL operations: typically what you get back are subsets of tables; poor old PL/1 then has to loop through these row by row; in APL you can generally process them as they stand.

This is in part because the SQL structure (any element can be a number, a character or null) is just a simple form of an APL2 array! This lets you do block retrievals directly into APL objects extremely cleanly and efficiently.

Naughty (non-IBM) thought: was the APL2 array philosophy (in particular the use of heterogeneous arrays) designed with SQL heavily in mind? The interface is so ‘made to measure’ that I can’t help feeling that it was. This may be a good thing in the short-term, but surely it must compromise the future of APL. Does anyone else have any views on this? (ACDS)

## The Grammar of Nested APL

*Graeme Robertson (IPSA)*

My notes on this talk are succinct and to the point: “ …eek - has GR finally flipped?!” is all I could manage to record about this extremely entertaining half hour. It was one of those talks which probably has some significant subliminal effect on your whole outlook on APL; the impact on the conscious and rational part of the brain was (at least in my case) close to zero. I hope Graeme will try to write it down, and hit us with a technical paper sometime soon. It should make good bedtime reading.

## Displaying Nested Arrays

*John Scholes (Dyalog)*

Audience participation was the key element in this ‘talk’. John sat behind a keyboard, and responded to a battery of questions about how one could format simple reports using nested structures.

His basic message was that plain vanilla APL is easy enough when all you want is ‘2 + 2’, but that it really gets in your way (and up your nose) when you want to format a simple report. You end up with so much catenating and reshaping (not to mention the need to ‘format’ all the numbers) that even the most trivial report can require quite an investment in time and brain cells.

With nested structures, at least the simple things are once again made simple. To get headings, stubs and footers around a table of numbers you just catenate them on the appropriate axes, and a simple monadic ‘format’ will do the rest. The way John built these up as he went along was most impressive, all the more in that he clearly wasn’t following a preset script.

What was also interesting was that there is still a cutoff point beyond which you once again get into the realms of re-shaping, and lots of nasty looking ‘takes’ with shoals of brackets. I can’t remember exactly where this occurred, but it seemed to me to lead straight from ‘very easy’ to ‘very hard’ as the nested structure suddenly started to get in the way, and you needed to make sure everything was at the right *depth* as well as being the right shape. Maybe John would like to come back at me on this.
