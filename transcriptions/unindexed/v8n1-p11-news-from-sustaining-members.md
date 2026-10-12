---
title: News from Sustaining Members
authors:
- Alison Chatterton
volume: '8'
issue: '1'
page: '11'
unindexed: true
transcribed: 'from page images of VOL.8-NO.1-JULY-1991.pdf, pages 13–18 (printed 11–16); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
queries:
- "Printed byline “Compiled by Alison Chatterton”. The piece ends on printed 16, its lower half blank."
- "The Dutch APL Users Group’s hardware/software table, printed in a typewriter face with box-drawing rules, is given as a pipe table."
- "Kept as printed: “ASWI: a component file system, an object library system and a system of relational data functions for arrays” after “2 packages”; “Jean-Jaque Riethoven”; “the new AP124 processor”; “well-known with APL”."
---

*Compiled by Alison Chatterton*
{ .byline }

## Dyadic Systems Limited

Dyadic is pleased to announce an implementation of Dyalog APL for Windows 3.0. The new product is called Dyalog APL/W and is based on Dyalog APL/X for the X Window System. Dyalog APL/W is written specifically for Windows 3.0 and makes full use of the Windows environment. It is a true Windows 3.0 product and cannot be run under DOS alone.

Like Dyalog APL/X, this new implementation will provide the APL developer with the facility to concurrently edit/view functions and variables in separate windows on the screen. The product also features the unique Dyalog APL debugger which lets you step through an application watching the functions pop up and down in windows as they run. Dyalog APL/W will include a means to invoke Windows menus, dialog boxes, scroll bars and so forth in end-user applications. It will also provide DDE support.

In addition to a Windows 3.0 environment, Dyalog APL/W requires a 386 or 486 processor with (ideally) 4Mb+ of memory. On a 386-based system, a 387 coprocessor is strongly recommended. The product runs as a protected mode application in Windows 386 enhanced mode. This means that it can support very large workspaces and even utilise Windows demand paging if required.

Early trials (and this announcement was written in May) indicate that performance will be every bit as good as Dyalog APL for DOS/386.

A detailed specification for Dyalog APL/W will be available at APL91, or can be obtained by post from Dyadic or any Dyalog APL distributor.

As an Authorised IBM RS/6000 VAR, Dyadic is pleased to report significant price reductions, and improvements in performance and specification across the range. The new Model 320H now comes as standard with 16Mb RAM, 400Mb disk and offers 38 MIPS and 11.7 Mflops performance. Based on this model, a single-user workstation with a 16" colour 1280x1024 display, X-Windows, Motif, and Dyalog APL costs around £16,500. A 10-user Dyalog APL system, using ASCII terminals or PCs, can be put together for under £25,000.

## Cocking & Drury Ltd

First of all we’d like to apologise to you all for our non-appearance in the last issue. We had anticipated a lot of the news in the issue before, but we should have tried a bit harder to dream something up! We have a lot more to tell you this time around though.

Many of you will have received our publication ‘Upgrade’ around mid-June. This publication, which used to be a regular feature in Cocking & Drury activities, lapsed some years ago and we were pleased to be able to re-instate it. The 8 page issue contained news of developments at C&D, developments with APL\*PLUS, a user-story from London Life, a technical article by Allan Gay on migrating from APL\*PLUS PC to the II System for the 386 and more.

Anyone who didn’t get a copy but would like one - give us a call.

At the time of writing (early June) we are deep in the throes of preparing for our presence at Software Tools ’91. We shall be showing APL\*PLUS PC, II System for the 386 and II System for UNIX. (We shall also be showing the full range of Smalltalk/V products - but that’s another story for someone else’s newsletter!)

The launch of the new APL\*PLUS II for UNIX for the IBM, SUN and DEC RISC machines has gone really well. James Wheeler - Vice President of STSC in charge of development - did a presentation in our training room to many of our leading customers the day before his presentation to the BAA.

That - and our marketing work and several mentions in the computer press - has led to a steady stream of enquiries and all our demonstration copies are currently out on loan which bodes well for future sales.

James also gave us an insight into future developments for APL\*PLUS. DOS-based machines remain dominant, in their view, with the 32-bit architecture becoming standard but with an increasing interest in extending DOS with Windows - and in UNIX workstations.

STSC strategies will be to concentrate R&D on 32-bit software, exploiting Windows in DOS and X Windows in UNIX. There will be considerable improvements in interfaces to non-APL software - Database managers, graphics, SQL-based client-server databases over networks etc. But more importantly the future of APL\*PLUS will include the ability to call APL from other programmes.

STSC have clearly committed themselves to developing APL\*PLUS to interface with the various GUI’s and to achieving the highest level of compatibility between them. The result will inevitably be to achieve even more sales for APL\*PLUS in the future.

We at Cocking & Drury are delighted to be involved with these developments. We are currently celebrating the most successful year for software sales ever - having set ourselves the target of £500,000 from APL\*PLUS products in 1991 we are happy to report that 21 weeks into the year we are ahead of target by over 10% and are now wondering if we can make it £600,000 for the year! We’ll let you know.

Our course programme is busy - in the weeks surrounding the writing of this news we shall have given 3 courses in Ireland and one on the Isle-of-Man. Our course tutors are becoming well-travelled.

On the consultancy front we can report that we recently started work for a first-time client, not new to APL but new to us, and that hasn’t been a common occurrence in recent months. There are several similar contracts currently under negotiation, as well as new contracts with existing customers, and we have job offers out to two consultants with more to follow. More news on that next time.

## MicroAPL

In Vector 7.1, exactly one year ago, MicroAPL announced the launch of our second generation APL - APL.68000 Level II. In this issue of Vector, we hope to do even better. We have two major product announcements to include, one of which signals an entirely new area of operation for MicroAPL.

First of all we have completed work on the first significant upgrade to APL.68000 Level II. Version 2 of APL.68000 Level II removes most of the remaining differences between APL.68000 and IBM’s APL2/370. APL.68000 Level II has always been much closer in its specification to APL2/370 than any other APL, even IBM’s own APL2/PC, and we have now further narrowed the gap. At the same time we have managed to include some **dramatic** optimisations in certain key areas of the interpreter.

The main features in Version 2 of APL.68000 Level II include format-by-example; axis on scalar functions; extensions to selective assignment; N-wise reduction; partition with axis. At the level of system commands and system functions we have now implemented the name sorting and string range rules for system commands and we have implemented `)SIS`.

The optimisations we have implemented focus on simple cases of some of the most widely used functions. For example, scalar integer arithmetic (e.g. `+-⌈⌊`) has been substantially improved. Catenation operations with simple vectors have been enhanced as have indexing operations with integer indices. The effect of these improvements can lead to marked speed-ups - STSC’s benchmark 4 (Mixed functions) is some 2.75 times faster! The final optimisation of note is with respect to pick selective specification where, in some cases, speed-ups of two orders of magnitude have been achieved.

Version 2 of APL.68000 Level II is, however, just the warm-up act to our main product launch of 1991. At APL91 in early August, MicroAPL will be launching the first of a whole new series of implementations of APL.68000. Since early this year we have been working on porting the source code for APL.68000 onto a wide variety of RISC systems (Reduced Instruction Set Computers) and our first release is for the IBM RISC System/6000 family of computers.

The RISC System/6000 is making dramatic inroads into the workstation and supermicro market and here at MicroAPL we felt it to be an appropriate first machine to support. APL.68000 running on the RISC System/6000 will bring with it a number of powerful benefits for APL users. On the one hand we have based our product specification on IBM’s APL2 specification (ensuring compliance with large system APLs). On the other hand we have included a number of features in our APL.68000 which are of major importance to the user. There are a whole host of APL language features to complement and enhance the APL2 specification. APL.68000 on the RISC System/6000 will offer a fully thought out and fully developed windowing interface for APL programmers to use. The five years that we have spent developing windowing interfaces on machines like the Mac and the Amiga have allowed us to get the interface right without the burden of all sorts of inappropriate hang-overs from previous implementations.

So what will APL.68000 for the RISC System/6000 include? Firstly it will support either dumb terminal connection or X-terminal connection. The windowing interface will use OSF/Motif and will include all the sorts of features that our Mac users are used to. We are also including on-line documentation in the shape of the entire APL.68000 manual. As usual we will not be subscribing to the theory that binary compatibility is impossible. Any APL.68000 file or workspace from any other version of APL.68000 will be directly usable on the RISC System/6000.

APL.68000 for the RISC System/6000 will be launched at APL91.

On a closing note, our many Atari ST users will be pleased to know that we have completed and are now shipping the upgrade to APL.68000 on the ST. All registered users will have been contacted by post.

## Report of the Dutch APL Users Group

In Vector 7.3 the Dutch APL Users Group reported the start of the APL ShareWare Initiative (ASWI). The recent activities of ASWI were as follows:

1. The first activity of ASWI was to decide about the hardware platform and for which APL system the software should be developed. The result of the first discussion was as follows:

    | | Hardware | Software |
    |---|---|---|
    | primary target | PC's | APL2/PC |
    | secondary target | Atari Mac | APL.68000 II |

2. The next activity was to establish a set of standards about coding and documentation. The result of this has been submitted for publication in Vector.

3. The third activity will be to compile a priority list of useful programs and subsequently their specifications.

On Saturday April 6th the Dutch APL Users Group organised a fair at the OASIS premises in Nieuwegein.

A number of microcomputers and workstations were installed with all available APL interpreters such as APL.68000 level I and II, IBM’s APL2/PC, Dyalog APL/386, Dyalog APL/X, APL\*Plus/PC and APL\*Plus II. Various people showed their products and their applications (in alphabetical order):

- Eke van Batenburg showed a simulation for biological research in order to answer the biological question whether left-coiled snails can invade a population of right-coiled snails. Furthermore he demonstrated 2 games which were developed for his son in 1 day using APL.68000.
- In Tom Bonnema’s booth one could get various public domain APL systems, such as I-APL, TryAPL2, Sharp APL/PC and J.
- M.Bouwma demonstrated a very useful database package for STSC APL. This package used inverted files and contained a number of functions to create on-screen dialogues in an easy way. A substantial amount of programming was invested to ensure the integrity of the database.
- Louis van Geldrop showed a menu system developed for APL2/PC using the new AP124 processor. He also showed 2 packages already developed for ASWI: a component file system, an object library system and a system of relational data functions for arrays.
- Oasis hosted the whole event. The smooth organisation was mainly due to the efforts of the people of Oasis. They received the visitors in a nice and productive atmosphere. Furthermore, Oasis showed various APL interpreters.
- Jean-Jaque Riethoven showed STAR, a package to analyse the folding of RNA strings, using APL.68000.
- Bernard Smoor organised an extensive display of APL literature.
- Fred Visser was present with I-APL together with English and Dutch documentation.

The fair was attended by about 60 persons among whom nine copies of STSC’s Pocket APL were raffled by Oasis Decision Support Systems B.V. The greater part of the visitors were well-known with APL, but also some new faces were discovered.

## APL People Limited

Things have been very quiet on the recruitment front in the UK for the first half of this year. We now have a lot of excellent ‘APLers’ looking for either contract assignments or permanent vacancies. Any companies requiring skilled APL personnel to work either here or abroad should contact me straight away! We currently have a wide range of APL consultants and contract programmers available at very reasonable rates!

Surprisingly business is booming for APL People’s sister company, APL Manufacturing, whose production control software has recently been sold to companies as diverse as Philips Electronics, Jaguar Cars, Peak Engineering, and Marconi Defence Systems (to mention but a few!)
