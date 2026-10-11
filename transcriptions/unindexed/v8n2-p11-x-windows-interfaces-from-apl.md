---
title: X-Windows interfaces from APL
authors:
- Richard Nabavi
volume: '8'
issue: '2'
page: '11'
unindexed: true
transcribed: 'from page images of VOL.8-NO.2-OCTOBER-1991.pdf, pages 15–16 (printed 11–12; within General Correspondence, its only letter, before British APL Association News); Claude, 2026-10-11'
review: draft
tags:
- user interfaces
- system interfaces
queries:
- "Untitled in print: a letter, “From: Richard Nabavi, 6th September 1991”, signed from MicroAPL Ltd, the only letter under General Correspondence; the title is ours. It answers the articles by Jensen & Beaty (art10004090) and Peter Donnelly (art10002880) in Vector 8.1."
---

*From: Richard Nabavi, 6th September 1991*
{ .byline }

Dear Sir,

I am sure that lots of Vector readers will have found Vector 8.1, the “Windows Special”, particularly interesting. But I fear that they may also have been unnecessarily disheartened by it. Eager to consider bringing their APL applications into the new world of X-Windows and the Motif windowing interface, they will have turned to the articles by Jensen & Beaty, and by Peter Donnelly - and they will have been horrified.

Take IBM’s X-Windows interface, AP144. A 103-line function just to do a simple “Hello World” program? The window doesn’t even appear until line 51! Is this really the kind of developer-friendly high-level software tool which is going to make life easier for us?

Maybe graphics is a bit hard. Let’s turn to Peter Donnelly’s article. After all, user dialog boxes are a pretty standard feature for windowing systems. His last example seems to address a fairly straightforward requirement - a selection list with four “radiobuttons” and two exit buttons. That shouldn’t be too difficult. But look at the code! What is all this stuff about “XmATTACH_POSITION” and “XtManageChildren”? Things are even worse here than in the “Hello World” example - you get to line 72 before you “realize the widget tree” (which I think means show the dialog box).

The problem - as always with this sort of thing - is that in both cases, the work is being done at the wrong level. It is important not to fall into the trap of providing an APL interface which comprises a one-to-one correspondence between low-level language calls - in this case the C interfaces to X-Windows and Motif - and APL functions. Whilst this may very occasionally be necessary, for 99% of cases it gives you the worst of all worlds - code which is as long-winded as C, without the advantages of C’s high speed as a compiled language and the documentation and type-checking advantages of including standard interface files.

The APL programmer does not want to know about “XtInitialize” or “XLookupString” - and he most certainly does not want to be bothered with mapping X-windows data types to and from APLs. He will not be very impressed by the fact that giving a wrong argument to a function can crash APL, as will certainly be the case if C pointers are directly manipulated from APL. He will be concerned at the CPU usage of an APL function which takes 100 lines to do a simple part of a screen display. And he will be very worried about how difficult it will be to port these massive functions to other windowing systems.

Fear not - it does not have to be done this way. The X-Windows example can be done in about nine easily-readable lines of APL. Peter’s Multiple Widget Example can be done in about eight, depending on exactly what functionality is desired (bringing up the dialog box takes three lines). It can be done using an APL system which provides sensible defaults for everything which is not explicitly specified, and which can be used without specialist X knowledge. And what is more, it can be done in such a way that the code will be portable from (say) Motif to Open Look without change. And it can be written using an APL system which itself conforms to the style guidelines of Motif, with the proper scroll bars and menus and dialog boxes built in, all controllable using the standard Motif resource mechanism.

You will not be surprised to hear that I am referring to MicroAPL’s way of doing things, as refined into APL.68000/X for Unix machines such as the IBM RS/6000. But you might be surprised - as I was - that no less than five years after we first launched our Macintosh version of APL.68000, others are still at the level of transliterating C subroutine names into APL functions, providing clever solutions to the wrong problem. The problem is not “How can we call the X-Windows C interface from APL?”, but “How can we avoid having to call the X-Windows C interface from APL?”.

Richard Nabavi<br>
MicroAPL Ltd
