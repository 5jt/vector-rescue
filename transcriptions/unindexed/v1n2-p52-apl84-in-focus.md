---
title: APL84 in Focus (meeting notes)
authors:
- Adrian Smith
- Dick Bowman
volume: '1'
issue: '2'
page: '52'
unindexed: true
transcribed: 'from page images of VOL.1-NO.2-OCTOBER-1984.pdf, pages 54–59 (printed 52–57; an H.M.W. advert follows on p.58); Claude, 2026-10-03'
review: draft
tags:
- conference reports
- implementations
queries:
- "Six pieces printed as one meeting report: Adrian Smith’s introduction, Dick Bowman’s commentary, and notes on five talks (Roy Sykes, John Scholes, Philip van Cleave, Jim Brown, Jim Ryan), each with its own heading and “by” line naming the speaker. Set as H2 sections. The introduction says the notes on the talks are by Steve Lyus and Derek Wilson."
- "Bowman says “four speakers from the USA, one of our very own”; the introduction counts 5 talks."
- "Slips transcribed as printed: “arbitary”, “accomodate”, “a relational databases”, “differences which makes”."
---

*June 22nd 1984, Waldorf Hotel, Aldwych*

Notes compiled by Adrian Smith
{ .byline }

This was very much a ‘special event’; there was an admission charge and delegates were asked to register in advance. In spite of (or because of!) this the meeting was very well attended, and a total of 98 bodies were counted.

All 5 talks were repeat performances of papers given at APL84 in Helsinki. I would like to thank Steve Lyus (Imperial Group) and Derek Wilson (Rowntree Mackintosh) for providing me with very comprehensive notes. I have used Steve’s comments on the papers by Roy Sykes and John Scholes, and Derek’s for the papers of Phil van Cleave, Jim Brown and Jim Ryan.

Before these notes we have included an overview of the event by Dick Bowman — the Association’s Activities Officer — who is to be congratulated for bringing such a good representation of the APL’84 Conference to London.

## APL84 in Focus: a commentary by Dick Bowman

The APL84 conference was a splendid occasion, but one which could be attended by only a minority of Association members. It seemed right that we should attempt to do something to bring back some flavour of what went on, whatever news there was, and maybe even catch one or two of the seminal figures of APL in transit.

As it turned out we were fortunate enough to be able to attract four speakers from the USA, one of our very own, and a number of hardware exhibitors.

The detailed notes by Steve Lyus cover the ground of what was said by our speakers and I shall comment briefly instead on the exhibitors and the audience.

Among the hardware exhibits was the Analogic APL Machine; we finally managed to get a full working demonstration of this most impressive piece of hardware, and are grateful to CACI, the UK distributors, for their involvement. Also present was the Ampere lap-top APL micro (MicroAPL can tell you more), which goes a long way towards cutting the entry cost of APL hardware and provides not only APL and ASCII characters, but also Katakana. We were also pleased to have a working NIAL system. NIAL derives from the array theory of Trenchard More; it could be summarised as an English keyword version of generalised APL arrays, although I suspect that it is biased more toward array manipulation and omits a few APL excesses. Dyadic Systems brought along one of their more transportable UNIX machines, and I.P. Sharp generated some interest in their new bargain-basement prices. IBM, unfortunately, did not respond to my suggestion that they’d like to demonstrate APL2 running on an XT/370.

At the end of the day the 100+ attendees had received the word direct from some of the innovators of the APL world and had seen some of the more stimulating new kit in action. On our part, we’d put on a meeting of greater length than our norm, and the first for many years in which we’d stepped outside the environment of Imperial College (Loughborough excepted). We even included a decent lunch. As an event additional to the usual schedule (which is financed by your subscriptions) we were obliged to charge a fee, but one which was considerably lower than the going rate for commercial events. After considerable nail-biting we made a small surplus, which is being ploughed back into further improvements in the Association’s services to the membership.

Finally, I’d like to record my thanks to the participating companies. Most of the speakers had delayed their return to the USA; Jim Brown interrupted a holiday in France and flew in for the day specially.

## An APL Compiler, by Roy Sykes (STSC)

RS started off with a brief history of attempts to speed up the processing of APL Code (both hardware and software). STSC thought that there was much greater potential available from a proper compiler and initiated a research project. They had proved it was possible by June 1983, and have since speeded it up. They aim to release the product from August onwards with a goal of 3 x faster running (the range is likely to be 100x to 0.5x!) for a restricted set of codes.

To the user, a compiled function will be like a locked function and as such can be copied and filed (quad-CR and quad-VR will return the source code). RS made several interesting comments about the different ways they are using to speed it up.

STSC aim to have two products available in the near future:

> A compiler support pack (APL\*PLUS in Aug 84, VS APL in Jan 85) which will include a set of utility compiled functions.
>
> APL Compilation Service: the user will submit functions to be compiled and they will be returned the following day. (It would appear that the greatest benefit will come to those who code in inefficient loops!)

They hope to have proper software products available around January 86 (When it arrives, will the mainstream D.P. establishment welcome us back as the prodigal son?)

## Dyalog APL, by John Scholes

JS went through in some detail all the extra goodies available on their Unix-based system.

e.g.
: System Utilities (arbitary Input/Output).

: The use of a hybrid system — APL plus compiled bits; these compiled bits being auxiliary processors. They would appear to the user as a locked function and would occupy negligible space in the W.S., but perform their tasks very quickly. Examples given were of a full screen editor and formatted screen I/O.

: Bridge systems — connections allowed between the APL W.S. and a relational databases or graphics routines written in other languages.

## The Ampere: a Portable APL Machine, by Philip van Cleave

> “If I have to think for 4 seconds, that is equivalent to using all the processing power of all the computing resources in the world!”

Philip van Cleave started his presentation by giving some background to 16 and 32 bit micros and portable machines. He said that 16/32 bit micros had given opportunities to try ideas and approaches which would not have been possible before. One can now have massive memory and real storage (which makes processing much quicker) which in turn has opened up new applications.

He then proceeded to quote various buzz-words and desirable features (access to other people’s data, “user-friendly”, “integrated office”) and the implication was that the product he went on to describe had all these attributes. “APL is one place where we can really hit the (portable computer) market.”

The portable APL machine has a MC68000-based interpreter providing 1 megabyte of storage. It also has a built-in modem which gives it the capability to work with other devices.

Philip van Cleave stressed the power of the machine, which resulted from the fact that there are two APL processes running simultaneously internally. Data and commands could be passed backwards and forwards between them.

The machine included many useful features, such as the ability to record and pass back voice patterns, being able to see the operating system from within APL, and restarting from the point of interrupt in the event of a power drop.

All in all it was a somewhat loosely structured presentation, but the claims made were interesting. His main theme was that the portable APL machine allows APL users to develop software for the mass market.

## APL2, by Jim Brown

Jim Brown’s talk consisted of an introduction to APL2 and a brief discussion of some of the features. He was very enthusiastic and had a naturally attentive audience. APL2 had been announced in Germany the week before and this, he said, was an indication of IBM’s regard for the European market.

APL2 on IBM would run under TSO and CMS and utilizes 32-bit architecture and therefore allows up to 128 Mbyte workspaces. IBM’s intention was to use APL2 rather than VS APL for any further enhancements of APL and he said “It is our opinion that APL will remain the base of the Information Centre products.”

He commenced by talking about general Relational Data and Structured Query Languages (SQL). Relational Data tables have columns with data of a common identity and rows are different entries. SQL allows data to be retrieved from one or more tables, the ability to create new tables, new columns, and temporary tables. SQL is a subset of an APL2 array. He also talked about ISPF under APL and features such as a menu with APL options; calling other applications from within APL (e.g. PL/1 programs); and general recursive routines.

The rest of the talk was a brief summary of APL2 and the new features. There are lots of new primitives and the existing ones can be combined in a number of extra ways. The inner and outer products have been extended to general functions; and the nested arrays and “Each” operator virtually do away with any looping (but also lead to some very contorted code). APL2 naturally leads to recursive functions.

APL2 can accomodate a “LISP”-type structure and has other arithmetic which is very useful for graphics applications.

There are a few minor differences which makes APL2 not quite upwards compatible, e.g. the display of nested arrays has meant that conventional arrays of many dimensions are displayed differently. Another change is that many of the errors now return results, which should make error-trapping easier.

The talk was interesting, but obviously the new features, and the pros and cons, would have to be looked at in great detail to assess the real benefits.

## The APL Machine, by Jim Ryan

Jim Ryan’s talk and demonstrations rather stole the show and everyone was very impressed by the power and versatility of the product. It was, he said, “a processor of arrays integrated with a language of arrays”.

The hardware configuration is best understood by reading the Analogic product literature. Basically there are three active systems: a work station, a peripheral system and an array system; and the way these work together gives very powerful processing and data recall. He said the operating times were comparable with an IBM 3081.

There is a virtual workspace of 850 Mbyte (which can go up to 1 Gbyte), i.e. up to the memory limits of the whole machine. There is no filing system (but does there need to be?).

Many of the software features are very impressive. The APL complies with ISO APL but there are layers of extensions. The workspaces are organised in a hierarchy, and this threaded workspace allows you to make components of a workspace available to others. The overall result is that it is possible to have a complete data-base of functions with the ability to make universal changes but with local versions and various security options also available.

There are also many exception management options which make validation and error-control easy. The overall result is a powerful, versatile machine which can be multi-user and allows multi-tasking (screen windowing is a key feature).

Analogic hope to have the lowest level of the system (ISO APL) available in September 1984.
