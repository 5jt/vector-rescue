---
title: 'Re: letters published in VECTOR 4.2'
authors:
- Mark Cranny
volume: '5'
issue: '1'
page: '11'
unindexed: true
transcribed: 'from page images of VOL.5-NO.1-JULY-1988.pdf, pages 13–16 (printed 11–14; within General Correspondence, the first letter under the section heading); Claude, 2026-10-11'
review: draft
tags:
- APL in perspective
- APL community
queries:
- "A letter in General Correspondence, From: Mark Cranny, 18th May 1988. The section’s standing introduction (“The VECTOR working group welcomes correspondence …”) precedes it and is not transcribed here. It is followed by F.H.D. van Batenburg’s “Public Letter to P Chapman” (unindexed/v5n1-p14-public-letter-to-p-chapman.md)."
- "Underlined words (“many”, “sold”) are set in italics."
- "Kept as printed: “s**t”, “E J Sargeants’s”."
---

*From: Mark Cranny, 18th May 1988*
{ .byline }

After they had sat on my desk for several weeks, I finally got round to reading editions 4.2 and 4.3 of VECTOR, and was so amazed at some of the correspondence in 4.2 that I felt the need to stop revising and put pen to paper - or finger to keyboard even.

The first letter was from Dick Bowman claiming that APL goes further than any 4GL in that it is far more flexible. He mentions ADRS, yet doesn’t seem to make the connection between APL and 4GLs. In several issues of VECTOR, there have been full-page adverts for IC/1, which IBM has consistently refused to market as a 4GL, preferring to call it an “integrated multifunction center environment”, yet by the traditional criteria for a 4GL it certainly is one:

> non-procedural (menu driven)<br>
> database query language<br>
> input validation routines / tables<br>
> report generator<br>
> financial planning/analysis facility<br>
> graphics facility<br>
> complete application generation facilities<br>
> interfaces to other systems (OS, DBMS, TP etc.)

For the uninitiated, IC/1 is ADRS II the reporting system, APLDI the APL data interface, ADRS/BG business graphics, FPS II financial planning and APE (application prototyping environment) all thrown together and called IC/1. It emerged from Sweden, was taken over by the Americans when 4GLs first started to become fashionable, and when it didn’t take off was handed back to the Swedes to continue to support and develop (probably after causing quite a lot of damage). IC/1 allows rapid or evolutionary prototyping to take place, with its own inbuilt indexed sequential filing system, or it can act as a front end to other DBMSs such as SQL/DS. The ADRS sections of code provide the reporting and data-validation capabilities, and APE allows screen design for interface creation. The graphics facility is probably the weakest part of the package, and is certainly nowhere near as well developed as the graphics of IBM’s flagship 4GL, Application System (AS). IC/1 is far from being the best 4GL available, but the ideas are there, and (as estate agents are fond of saying) it has potential.

I completely agree with Mr Bowman that current 4GLs only go part of the way to presenting effective application generation, but IC/1-type environments give the best of both worlds: a non-procedural language for fast prototyping, but also the ability to get out of the menus and to get to the actual source code that the package is written in, allowing complete customisation of the application to fit the design requirements. Maybe a future development could be that when an application is completed, all internal documentation and unused functions could be erased to save space, and then the code compiled to create the finished production workspace, only being recompiled after updates and system changes to the original development workspace. Perhaps the “sustaining members” of the BAA are already developing advanced APL tools along these lines?

I first came into contact with APL at university, but it was not until I worked for IBM for an industrial experience year that I really started to use APL and its associated products, such as IC/1. At first I couldn’t understand why IC/1 was not successfully marketed by (probably) the best marketing organisation in the world. However, I think there can be only one conclusion - IBM doesn’t want to market products like IC/1 when it can market the more glamorous AS. As with DB2, IBM tries to get customers interested in AS and then informs them that it needs their biggest and most powerful boxes in order to run it.

There was also a letter from Richard Connor, who claimed that:

> “One of APL’s great virtues is that its effective use doesn’t require technical knowledge of computers and software. It is an excellent language for the end-user.”

Of all that I have read about APL, this has to be the biggest load of horse s\*\*t I have come across. Yes, APL is a powerful tool when hidden behind interfaces such as ADI, but Mr Connor seems to be suggesting that end-users get down to the nitty-gritty in raw APL code. I’d love to know what he does for a living, and what experiences he has had of end-user computing! I spent 13 months actually sitting next to the people who were using the systems I had designed, and several that I inherited and had to maintain. It was difficult enough to get users to use IBM’s PROFS office system (based around PF keys), let alone get them to accept a programming language per se.

One particular user had a habit of leaning backwards and hitting me over the back of the head whenever something went wrong or there was something he didn’t understand. If he had been given raw APL to use as an analysis tool I should have had to wear a crash-helmet! There are *many* computer-illiterate people out there with a very real fear of the keyboard, and if the BAA has been spending its time over the years trying to encourage those people to use APL in its raw form, and not as completed applications, then it is not surprising that APL is still pretty much a dead duck. APLers seem to expect everyone else in the computer world to share their enthusiasm for the aesthetic qualities of the language: in the real world people just want to see results, or to have effective and straightforward end-user tools made available to them.

Barrie Webster’s letter contained an accurate insight into the current position and problems of APL - the language has just not been *sold*, and has always had the image of being a mathematician’s toy. If 4GLs written in APL were actively marketed, then users could be introduced to the power of APL without realising it, but the facility to go further and to get more involved with the source code would be there if required.

I am constantly surprised when I discover yet another company who use APL - Midland Bank, British Airways, IBM etc - and yet the language still accounts for only a minute proportion of all systems development. It is this business community which needs educating as to the benefits of APL, rather than schoolchildren. Companies have too much investment in COBOL to rewrite their complete applications portfolio in another language, especially one that is also a 60s love-child. However, a move towards prototyping in APL can be encouraged: after all, C started to be more widely used as a result of Unix, so why not use the 4GL environment as a vehicle to get APL more widely accepted?

Commercial organisations are interested in the business advantages to be gained (increased speed of development, flexibility of design, reduced maintenance costs etc.), and at what cost, not how pretty or elegant the code is! Maybe the powers that be in the BAA could “encourage” Computing or Computer Weekly to give a couple of pages over to articles looking into the pros and cons of APL. If APL doesn’t move with the 4GL environment, it will remain with an ever-decreasing band of enthusiasts.

After leaving IBM and returning to college to finish my degree in systems analysis, I joined the BAA in order to keep up with developments in APL. I think that I am addicted to the language, in that I enjoy using it more than any other 3GL I have come across, but I am not a disciple or APL bigot. The BAA have been the Jehovah’s Witnesses of the computer world for too long; when a member of the APL True and Faithful puts their foot in the door of a disbeliever, and starts talking about dyadic iotas and Atomic Vectors, who can blame them for switching off? As a business computing person, I will use any tool necessary to achieve efficient and cost-effective results, and I am not brainwashed to the extent that I see APL as the ultimate systems cure-all. However, I do think that its power has been completely overlooked and underestimated by the business community. The power of APL is there provided it is implemented with good in-house standards for readability and maintainability, prototyping and documenting tools.

The BAA has the image of a group of mathematicians masquerading as computer professionals; developing ever more intricate and useless utilities for other computer scientists. I would suggest that the business-minded members of the BAA form a breakaway party to concentrate on promoting the business advantages of APL, and leave the academics to argue over whatever they want to argue over. However, in light of what has happened to the SDP, maybe that is not such a good idea?!

I would love to see APL become a popular and widely-used language, but to be honest, I don’t think it ever will.

Yours in deepest perspiration (exams only 2 weeks away)

Mark Cranny<br>
Dept for Business Systems Analysis<br>
City University, London

P.S. E J Sargeants’s letter suggesting an APL-based calculator was a joke, wasn’t it?
