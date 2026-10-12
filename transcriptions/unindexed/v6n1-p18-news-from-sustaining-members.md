---
title: News from Sustaining Members
authors:
- Alison Chatterton
volume: '6'
issue: '1'
page: '18'
unindexed: true
transcribed: 'from page images of VOL.6-NO.1-JULY-1989.pdf, pages 20–24 (printed 18–22); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
queries:
- "Printed byline “Compiled by Alison Chatterton”. The MicroAPL advertisement (“MicroAPL for ... APL on the widest range of micros”) in the lower half of printed 22 is not transcribed."
- "HMW Computing: Stan Wilkinson’s home telephone number, printed for out-of-hours calls, is omitted; his office number is kept."
- "Kept as printed: “make our product confirm to IBM's SAA”; “we still looking for suitably qualified programmers”; “the Apple Macintosh version” after “version 7.20 for”; a stray mark after “interface” in “the ⎕NA interface” is dropped."
---

*Compiled by Alison Chatterton*
{ .byline }

## HMW Computing Limited

HMW Computing Limited continue to develop "4XTRA" our front end Foreign Exchange Dealing and Position Keeping System. The current upgrades will make our product confirm to IBM's SAA, Common User Access Panel Design and Interaction and allow full support of mice and touch pads. Interest in "4XTRA" continues to grow and we have many UK and International Banks showing interest. We are currently installing the product in a Major UK Clearing Bank.

Our employment service for the APL community 'HMW EMPLOYMENT LTD.' continues to supply people with jobs. Currently we have many vacancies for the less experienced APL technicians. To find out what we can offer, please call Stan Wilkinson on 01-353-4212. If you would prefer to phone out of office hours Stan's home number is [omitted].

## APL People Limited

For those of you reading Vector for the very first time, let me introduce myself. My name is Jill Moss and I run a specialist employment agency for the APL Community.

![Photograph of Jill Moss](v6n1-p18-news-from-sustaining-members/jill-moss.jpg)

If you are looking for skilled APL personnel, either on contract or for permanent vacancies, or are interested in finding out what opportunities are currently available - this is the place to come!

We are now in our eighth year of operation and have successfully placed people throughout the UK and Europe, including France, Belgium, Sweden and Luxembourg. Our next aim is to conquer the States! (We've already placed someone in Canada).

We also supply a consultancy service in APL, using our own highly-skilled professionals and supplementing their expertise with the use of top-quality freelance people. Our people offer a wide range of business skills, in addition to APL. For larger projects, we can supply a whole team of people, complete with Project Manager, to tackle the design, programming and implementation of major systems from start to finish.

## Dyadic Systems Ltd

Dyadic is pleased to announce the launch at APL89 of Dyalog APL for 386 PCs under DOS. The product includes the new Dyalog APL screen manager using `⎕SM` (Screen Map) and `⎕SR` (Screen Read), which is proving extremely popular with users. The screen manager is the subject of a paper given at the Conference by John Scholes, head of the Dyalog APL development team.

In addition Dyalog APL for DOS contains the first release of a new development environment which Dyadic expects to be equally popular. APL has always offered an interactive environment in which programs can be developed and debugged very rapidly. However, the programmer interface has not kept abreast of modern developments, and even BASIC now provides a more interactive method of programming. The Dyalog APL development environment exploits the workstation environment of a bit-mapped colour screen, mouse and keyboard to provide a more convenient and powerful means of writing applications.

All APLs have you type an expression, then press a special key (usually ENTER or RETURN) to execute it. In Dyalog APL this idea is extended by adding keys that mean EDIT and TRACE (the actual keystrokes mapped to these functions are user-definable). Furthermore the EXECUTE, EDIT and TRACE keys can be mapped to buttons to give you a 'point and click' mouse interface.

If you type `FOO` and press &lt;TRACE&gt;, the function `FOO` will appear in a pop-up window on your screen, and your cursor will point to the first executable line which will be highlighted. If you now press &lt;EXECUTE&gt; the line will be executed and the cursor will move on to the next line. If instead you press &lt;TRACE&gt;, the line would be executed with trace on any defined functions and operators referenced on that line. For example, if the statement traced in `FOO` said `Z←AVERAGE Y`, a new window containing the function `AVERAGE` would pop-up overlapping the `FOO` window. You could then single-step through `AVERAGE` or trace deeper into your application as you wish. Execution can be restarted at any arbitrary line by simply moving the cursor to that line and pressing &lt;EXECUTE&gt; or &lt;TRACE&gt;.

The function on top of the stack (the APL stack AND the window stack) is always available for editing. Other functions and variables can be edited by pointing at their name and pressing &lt;EDIT&gt;. At any time you can have the SESSION window, the stack in several overlapping windows, and one or more edit windows, active. You can move between windows with a single keystroke or by moving the mouse, and data can be cut from one window and pasted into another.

By default, the debugger will activate automatically when an APL event occurs. The event message (e.g. `DOMAIN ERROR`) will be displayed as usual, but the stack will appear with the top function in an editable window, and the cursor already placed on the line at which execution halted.

The interactive nature of APL and facilities like `⎕STOP` and `⎕TRACE` were originally crucial factors in establishing APL as a tool for rapid application development. To some extent, APL has fallen behind other software in this respect. The new Dyalog APL development environment is intended to redress the balance and bring APL once more to the forefront of software development technology.

## I.P.Sharp Associates

Version 20 of Sharp APL is due to be released this autumn. The enhancements and new features in this version fall into 3 categories:

- Language extensions include new primitives for enclosed arrays (raze, permissive disclose) and data searching (in, nubsieve).
- APL system extensions include task specific names for 'continue' workspaces, access control for file libraries, file (as opposed to component) information, and an alternative character control system for non-APL terminals.
- Changes to the APL environment include full dumps of workspace libraries with Sharp APL up and running, and transaction recording for improved user statistics. In response to customer requests, a dedicated OPR1 terminal is no longer required to operate Sharp APL.

The APLX interpreter is now available for the Siemens BS2000 environment. This is based on version 19 of Sharp APL and includes Auxiliary processors for BS2000 commands, file and syslist processing, and full screen management. It replaces the first generation APL1 product.

## Cocking and Drury Ltd

Release 2 of the APL\*PLUS II system for 386 machines is due for international launch this August. The new facilities include the `⎕NA` interface to non-APL programs, a numeric full-screen editor, easier migration and a very useful 'point and edit' feature which lets you open an edit session for the name nearest to the cursor, anywhere on the screen.

The `⎕NA` facility can be used to call programs written in Microsoft C and Borland Turbo C in real mode, or MetaWare High C in the 32-bit protected mode. APL arrays can be passed into and returned from C programs. The numeric editor is a very welcome facility. Each edit cell is a single number in the numeric matrix. Blocks of numbers can be tagged, moved, imported and exported.

For some time we have had an internal 2-day nested arrays course for mainframe and micro-based APL\*PLUS systems. We will develop this into a product if there is sufficient interest from users of these systems.

Readers may be interested to hear that we have successfully migrated two internal Symphony applications into Oracle PC, with interfaces to APL\*PLUS PC.

Cocking and Drury are pleased to announce the launch of our new FOCUS consultancy service. We are committed as a company to working with our clients in developing superior business support systems, and this new service gives recognition to the place that FOCUS plays in the portfolio of business support tools at our clients' disposal.

## MicroAPL Ltd

MicroAPL is continuing to place an increased emphasis on consultancy activities and we still looking for suitably qualified programmers for this area of our business. APL work undertaken in recent months includes Securities analysis, local government contracts and real time management information systems. Non-APL work has included PC network consultancy and installation as well as the provision of systems written in C, Assembly Language and work with some of the modern database software for micros.

Our core business of APL software sales is running at a higher level than in this period last year. Of the various implementations of APL.68000, the Mac version (both for the Mac and Mac II systems) is now the biggest seller having overtaken the Atari version in the last few months. In addition we have supplied various Unix-based versions of APL.68000 for systems such as Wicat and NCR.

Following our release of APL.68000 version 7.20 for the Apple Macintosh version, we have upgraded a number of other APL.68000 implementations to version 7.20. Users of our Mirage-based machines such as the Spectrum and the Aurora will be pleased to hear that version 7.20 is available for their machines - with the most significant feature being the inclusion of the EDIT full screen editor into APL.68000 as a system function (and command). We have also started shipping version 7.20 for the Wicat MCS and Unix versions and will shortly be announcing a release date for the Commodore Amiga. Apple Mac users should note that we have made some minor improvements to version 7 and version 7.30 is now available for the Mac. This is available at no cost for users of version 7. Apply to MicroAPL or its distributors for release details.

MicroAPL will be exhibiting at APL 89 in conjunction with our US distributors, the Spencer Organisation of New Jersey, and we look forward to meeting some of our many US customers in person at the conference. Richard Nabavi will be presenting a paper on his work with Windowing interfaces for APL and David Eastwood will be discussing some of the real time work that our consultancy operations have been involved with.
