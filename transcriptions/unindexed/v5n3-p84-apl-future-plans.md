---
title: 'February 17th: APL: Future Plans'
authors:
- Adrian Smith
volume: '5'
issue: '3'
page: '84'
unindexed: true
transcribed: 'from page images of VOL.5-NO.3-JANUARY-1989.pdf, pages 86–87 (printed 84–85); Claude, 2026-10-12'
review: draft
tags:
- implementations
- APL community
queries:
- "Contents line “February 17th: APL: Future Plans”; the printed heading is “APL: Future Directions February 17th at the Royal Over-Seas League”, with the byline “a brief report by Adrian Smith”. The report begins below a rule on printed 84, after the end of art10004210; printed 86 is an advertisement in the form of an APL function (PK64), and printed 87 the title page of the General Articles section."
- "Underlined words (“can”, “not”) are rendered as emphasis."
- "Kept as printed: “the UNX/VAX, II system”."
---

## APL: Future Directions

**February 17th at the Royal Over-Seas League**

*a brief report by Adrian Smith*
{ .byline }

We should all thank Jonathan Martin for both organising this excellent meeting, and getting the publicity out in time to get the attendance back up to scratch. Several of the speakers provided notes in advance, and all promised a speedy summary of what they should have said. These notes will all appear in the April VECTOR, so I shall confine this report to the significant news items, and some of the better quotes.

### Romilly Cocking (representing STSC and C&D)

> "If it really were my APL, I would be rich and famous, rather than just notorious"

STSC's plans include: version 2 of PLUS II, with `⎕NA` to interface to C and assembler (Spring 89); PLUS/VMS release 8 also with `⎕NA` (late 89); distributed sharefile (multiple mainframes 1st, then PC networks); compatible graphics PC/VAX/Mainframe (as long as you are using the PC as your workstation).

C&D's plans are for a link from mainframe APL\*PLUS to Oracle (late 89) and to DB2 (SQL/DS) in early 1990.

Further ahead, there lies OS/2. Maybe 2 years away ... nobody is yet making serious use of this, however:

> "By the time that situation has changed, I'm confident that STSC will have a product"

At the moment mainframe APL\*PLUS is still based on VS APL, which is old technology. It will eventually move to a mainframe version of the UNX/VAX, II system.

### Peter Donnelly (Dyadic Systems)

A full Oracle interface will be available to all versions of Dyalog APL (the current is only to the IBM badged version of Oracle). Concerning this interface:

> "The thought of what people are doing with this terrifies me, but it seems to work"

`⎕SM` to define and manipulate the screen (before nested arrays you couldn't do this), and a really exciting new session manager:

> "We have a strange relationship in Dyalog between the commercial and the technical people: the technical people never do what they are told to do. Fortunately they tend to come up with something better!"

Dyalog APL for PC DOS is in preparation (386 machines only). This will have `⎕SM`, the new development environment, and CGI graphics. It will lead on to an OS/2 version, to be developed by Dyadic in collaboration with MicroAPL.

### Richard Nabavi (MicroAPL)

Phar Lap and IBM's DOS extender are very roundabout ways of accessing memory. Why not use OS/2? Because it's not a 386 operating system, but being cleverer than DOS it *can* stop you doing all the naughty things you can get away with in DOS! Let's wait for OS/2-386!

Meanwhile there is APL.68000 for the smaller machines, and further work on the interfaces into the Mac environment. In the long term this is the approach which will be needed for OS/2 Presentation Manager ... however writing this kind of software is *not* easy: OS/2-PM demands a very new approach.

### Mark Turner (IPSA)

There will be continued emphasis on 'Dictionary' APL, with Sharp APL m/f converging on SAX. Future systems will need to support 'massive' user loads, say using a file system over multiple machines for 10,000 - 15,000 users. No longer can the system rest for 8 hours on Sundays: it will need 24-hr operation with online dumping, and the ability to survive at least one dead CPU.
