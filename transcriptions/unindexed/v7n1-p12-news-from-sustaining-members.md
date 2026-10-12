---
title: News from Sustaining Members
authors:
- Alison Chatterton
volume: '7'
issue: '1'
page: '12'
unindexed: true
transcribed: 'from page images of VOL.7-NO.1-JULY-1990.pdf, pages 14–18 (printed 12–16); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
queries:
- "Printed byline “Compiled by Alison Chatterton”. Printed 16 ends with the MicroAPL item, its lower half blank; The Education VECTOR begins on printed 17."
- "MicroAPL’s feature list: the underlined ∊ is given as ⍷ (find); the last item on the first line is a quad followed by a dieresis, given as “⎕ ¨” as printed."
- "Kept as printed: “In response to customers requests”; “high-level use-interface functions”; “broken into seperate units”."
---

*Compiled by Alison Chatterton*
{ .byline }

## APL People Limited

Enquiries have started to come in about the interface between APL and IBM's AS (Application System) product. For those of you who are not aware, APL People are collaborating with IBM in the development and marketing of this interface to Information Centres. We offer assistance to those wishing to be able to use the APL on their mainframe in conjunction with AS, and have the full backing of IBM in this.

On the recruitment front, at the time of writing, we still have a number of prestigious positions in the City waiting to be filled. Anyone who wishes to be considered should have excellent APL development skills, be keen to work in a fast-moving dynamic environment, and be prepared to put in 110% effort in return for a generous remuneration package! A knowledge of 'C' and a financial or banking background would be a distinct advantage as well.

We invariably have a range of vacancies for people with APL skills and are always pleased to hear from companies seeking to recruit, and individuals contemplating a move, whether they be in the UK or overseas.

Expansion plans are afoot too on the Applied Production Logic front (APL People's sister company). We have recently had a major order for our Production Engineering software (now numbering some 27 modules in total) from a company in Scotland. This has prompted us to investigate the possibility of setting up another office in the North of England to service this part of the country better (and save on travel costs for our salesmen!)

## Dyadic Systems Ltd

Dyadic is pleased to announce Dyalog APL Version 6.0 for Unix systems. This is functionally identical to the DOS/386 implementation and features the same integrated development environment consisting of a window-based Session, Editor, and Tracer. Apart from external system interfaces, Dyalog APL applications are now 100% compatible between DOS/386 and Unix platforms.

In addition to functional improvements the Unix implementation also benefits from the performance optimisation techniques which were introduced in Release 2 of the DOS/386 version. These result in a significant improvement in speed for basic arithmetic primitive functions working on large arrays. Typically this means a speed-up by a factor of 2 in the arithmetic benchmarks published by STSC.

There are in fact two flavours of Version 6.0 for Unix. The first is a multi-user version designed to support APL/ASCII terminals and/or PCs running terminal emulators. In this version, the APL development environment works in a surprisingly effective manner despite the inherent limitations of ASCII terminals.

The second flavour is Dyalog APL/X which is designed to take full advantage of X-windows, the widely accepted basic window manager for Unix workstations. The product is also designed to be consistent with OSF/Motif, which sits on top of X-Windows and provides a standard user interface compatible with Presentation Manager.

In Dyalog APL/X the Session, Editor and Tracer operate in separate X.11 windows which may be moved and resized using the mouse. The User Screen managed by `⎕SM` also becomes a separate moveable and resizable window. New trappable event codes have been added to allow such user actions to be handled under program control. For example, if the user resizes the `⎕SM` window your APL function can trap a resize event, query the new window dimensions, and reformat the display accordingly. Controls are provided to allow the APL programmer to specify what a user may or may not do.

Dyalog APL/X also includes an Auxiliary Processor which provides a direct interface to X.11 functions. This will initially provide graphics facilities, but is intended to be developed to include access to the Motif "Widget" set, a toolkit of high-level use-interface functions such as dialog boxes, menus, buttons, and so forth. The Auxiliary Processor will allow an APL application to pop-up a new window and display graphical information within it.

Dyalog APL/X will initially be available on IBM Risc System/6000, Hewlett-Packard and Sun workstations. In due course the product will be ported to other popular X.11/Motif platforms. Full details and dates of availability will be announced at APL90.

In response to customers requests Dyadic has developed a software interface that allows Dyalog APL to be called from a C-program. The interface is very simple and requires only a few additional lines of C-code in the calling program. It allows the C-program to invoke Dyalog APL, `)LOAD` a workspace, and then run any function and capture its result. Data is transferred efficiently between the C and APL tasks in binary form. The interface can be developed to support a network environment.

Dyadic is also proud to announce a change of ownership following a **Management Buyout** on March 31st 1990. The new directors and shareholders of the company are Pauline Brand, Peter Donnelly and John Scholes who have been with Dyadic for between ten and thirteen years. The company is delighted by its newly won independence, will continue to develop innovative APL products, and looks forward to providing an even more effective service to its current and future customers. By the time this edition of Vector is printed, Dyadic will have moved to new and larger premises. If you miss the mailshot, the new address can be obtained by calling the company's old number 0420-87024.

## Cocking and Drury Ltd

We have to begin our news with an apology this time. The release date of June that we announced for the APL\*PLUS II System Version 3 was the US release date - international release will be during August.

Cocking & Drury will be previewing the new features of Version 3 at a presentation in our London office on July 12 - anyone who would like to attend should call Beverley Satterley on 071 436 9481 to reserve a space.

Our consultants are spending an increasing proportion of their time working with clients migrating applications from mainframes to 80386 machines running the II System.

We have also noticed an increasing level of interest in the APL\*PLUS UNX product to run on Sun Sparc and other RISC stations.

At the more elementary level the APL Fundamentals courses run here in London continue to attract a large number of learner APLers. The first Nested Array course in May proved popular and we are now taking bookings for that course on July 17/18 and September 25/26. The final System Design course before it is broken into seperate units will take place on September 4-7.

Paul Bolwell - our current sandwich year student - will be leaving us at the end of July for a holiday before returning to college. His replacement, Steve Hill, joins in mid-July. And Steve Weller, the sandwich year student from 1988/89, will be joining the Company as a permanent employee in July too.

## MicroAPL Ltd

MicroAPL is delighted to be able to use the pages of Vector to announce a major new software product - APL.68000 Level II. For the last year or so we have to all intents and purposes given the appearance of being preoccupied with the user interface of our APL.68000 product - notably on the Mac and Amiga versions. This emphasis does indeed reflect our view that the user interface is the most neglected area of APL but we have not been completely ignoring the development of our APL interpreter.

There is a consensus that a 'second generation' definition for APL exists and that this includes, amongst other things, concepts such as nested arrays and heterogeneous objects. The definition of a second generation APL doesn't go much further than that because of the differences in the specifications of those second generation APLs that are on the market.

MicroAPL has made a major contribution to the portability of second generation APL code. APL.68000 Level II is an implementation of APL2 for processors which belong to the 68000 family. As with APL.68000 we have attempted to use as our model the version of APL that we regard as the de-facto standard. That standard is, in our estimation, IBM's APL2. In the same way that the original APL.68000 represents a useful superset of APL.SV, APL.68000 Level II offers a faithful implementation of IBM's APL2 (see below for what we think that is!) together with a number of vital enhancements.

There are actually two main versions of APL2 issued by IBM - APL2/370 and APL2/PC. APL.68000 Level II is midway between these two versions. A full list of the features that we have included is beyond the scope of this article but includes:

> Nested Arrays; Mixed Arrays; Selective Specification; Axis Extensions
>
> ```apl
> ⊂ ⊃  ∊ (enlist)  ⍷ ↑ (first)  ≡ ~ (without)  ⎕ ¨
> ⎕AF ⎕AT ⎕CS ⎕EM ⎕EC ⎕ES ⎕EA ⎕ET ⎕FC ⎕PR ⎕TC ⎕TF
> )IN )NMS )OUT )RESET )TIME
> ```

At the same time APL.68000 Level II incorporates all the features of APL.68000. In fact APL.68000 Level II is upward compatible with APL.68000 and existing workspaces can be `)LOAD`ed into the new APL. For those of you who are not familiar with APL.68000's features, this means that we have added `⎕EDIT`, `⎕HC` (hard copy), component files, `⎕SS`, `⎕BOX` and many other useful features to the APL2 specification.

The inclusion of the `)IN` command means that APL code can be transferred to APL.68000 Level II from other APL2 environments with the minimum of fuss. This last point is critical as APL.68000 Level II adds a number of key machines to the family of those computers that run APL2. Users of mainframe or PC-based APL2 systems can now move applications painlessly to the Apple Mac, or any one of a number of Unix computers or even their Atari ST to carry on working in APL2 at home! APL.68000 Level II has been designed by Richard Nabavi and is available for all machines that support APL.68000.

<p style="text-align:center">APL.68000 Level II will be officially launched at<br>APL90 in Copenhagen.</p>

For more details, contact David Eastwood at MicroAPL
