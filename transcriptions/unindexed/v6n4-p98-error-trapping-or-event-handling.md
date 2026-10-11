---
title: Error Trapping or Event Handling?
authors:
- Richard Nabavi
volume: '6'
issue: '4'
page: '98'
unindexed: true
transcribed: 'from page images of VOL.6-NO.4-APRIL-1990.pdf, pages 100–101 (printed 98–99; within Technical Correspondence, after unindexed/v6n4-p96-is-function-ambivalence-a-good-thing.md); Claude, 2026-10-11'
review: draft
tags:
- language design
- implementations
queries:
- "A letter in Technical Correspondence, From: Richard Nabavi, 14th March 1990, signed Richard Nabavi, MicroAPL Ltd. It is followed by Rex Swain’s “APL and MS Word for HP LaserJet” (unindexed/v6n4-p99-apl-and-ms-word-for-hp-laserjet.md). The italic parenthesis “(What about WS FULL, or SYMBOL TABLE FULL? Ed.)” is the editor’s, printed so."
- "“Bug” is printed in a small italic font, set here in italics."
---

*From: Richard Nabavi, 14th March 1990*
{ .byline }

I have been following with interest the recent VECTOR articles on Error Trapping in its different manifestations within APL\*PLUS, Dyalog, IPSA, APL.68000 etc. But may I make a plea for greater terminological exactitude in describing what these facilities actually do?

My gripe is a simple one. What I used to think of as *Error Trapping* is being termed *Event Handling*. This term is used by Dyalog, by I.P. Sharp, and even by IBM in the APL2 reference material. Now it seems to me that if your APL code is happily tripping along, interpreting and executing statements according to the will of the sentient being who wrote the function, and suddenly it encounters a `SYNTAX ERROR`, then that is not an *event*, it is a *Bug*. The term *Event*, as used by most of the computing fraternity outside APL, is normally reserved for external events that meet two criteria: (a) they cannot be predicted by following the logic of the code, and (b) they can happen at any time, not just when the system makes a specific operating system call or carries out a particular instruction.

In fact, the only real Event which can normally be trapped in a conventional (non-windowing) APL environment is the user hitting the Attention key; this is indeed a true external event which can happen at any time, and which cannot be predicted by following the logic of the APL code. It is clearly different in nature from a `VALUE ERROR` or a `RANK ERROR`. (*What about `WS FULL`, or `SYMBOL TABLE FULL`? Ed.*) However, in modern windowing systems, and on networks or sophisticated multi-user machines, a plethora of other external events can occur, which the APL system might need to know about. Examples of these true Events are:

- the user has selected a menu item from a pull-down menu
- the application’s window has been overwritten by another task, and needs to be redrawn
- the network has sent a message containing an update of the $ to Dmk exchange rate.

Now, as far as I know, these kinds of Events are not really handled by any of the trapping facilities which APL interpreters provide. Even APL.68000 on windowing machines like the Macintosh - which does provide Event Handling through a library workspace - does not yet have these facilities built in to the APL interpreter itself, although the operating system interface is largely built around responding to events. So shouldn’t we use the term Error Trapping to describe what we have got already, so that confusion can be avoided when we finally announce that APL now has Event Handling built in to it?

In fact, when you do start to think about true Event Handling in APL, you begin to realise that it is a difficult subject, and may require fundamental changes in the way APL systems are designed. But that is another matter; in the meantime, let us not use misleading expressions.

Yours sincerely,

Richard Nabavi  
MicroAPL Ltd.
