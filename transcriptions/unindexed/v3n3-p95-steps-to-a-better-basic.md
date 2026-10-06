---
title: Steps To A Better BASIC — Everything AND the kitchen sink (reprint from Datalink)
authors:
- Anthony Camacho
volume: '3'
issue: '3'
page: '95'
unindexed: true
transcribed: 'from page images of VOL.3-NO.3-JANUARY-1987.pdf, pages 97–98 (printed 95–96; art10006320 follows on p.97); Claude, 2026-10-05'
review: draft
queries:
- "Earlier parts: v1n1-p77, v1n2-p73, v1n4-p95, v2n1-p81, v2n3-p89, v3n1-p93 (all unindexed). An APL People advert fills the foot of p.96. Subtitle printed “Everything AND the kitchen sink or how to take it with you when you go”."
- "“My BBC microcomputer a version of APL running” is printed so (has a version?)."
---

by Anthony Camacho
{ .byline }

## Everything AND the kitchen sink or how to take it with you when you go

When you go caravanning, instead of taking tents out of the boot of the car and erecting them in the pouring rain, it seems like luxury. It’s not the same, of course, as doing things the hard way, but it does make life easier.

The COBOL or BASIC way of taking things with you is to put them into constants or DATA so you unpack the luggage freshly on every run. This is fine for a data processing application, but less than ideal when it comes to programming.

That calls for easy ways to handle parts of the program such as subroutines. A COBOL library is easy. Most BASIC methods are not. COBOL writers can copy from the library at compile time, so there is no problem with clashes of line number. BASIC programmers have to write their standard subroutines with high line numbers so that they can be merged with any main program.

Programmers in most BASICs do not have the facility to call subroutines by name so they get to know the line numbers of the main routines and of course they get used to a particular line number doing each of the common things they want to do. For example GOSUB 9873 may display M$ centred on line 21 flashing with three beeps. The main program can’t be tested without the subroutines; after they are merged it can’t be renumbered because that would move all the subroutine addresses.

Where BASIC does have an advantage over COBOL is in the programmers’ toolkits which provide all kinds of useful debugging aids. In microcomputers this may be held in ROM so that it is always available. This brings such joys as the ability to display the list of all variables and their current values or to trace a variable’s changes of value.

In APL on the other hand it is easy to take things with you. Indeed that is the default. All APL work is done in a notional “workspace” which is a block of real or virtual memory. The workspace holds your bits of program (which are all in the form of procedures or “functions” as APL calls them). It also holds all the variables that have been assigned a value. At any time you can get a sorted list of variables with the command )VARS or a list of functions with )FNS. The workspace also contains the stack, which records all the return addresses for functions in progress and such “global variables” as the print precision, the print width, the comparison tolerance (yes APL finds a million millionths equal to 1), the seed for pseudo-random numbers and so on. If you interrupt the execution of an APL program and )SAVE the workspace, everything is stored, and branching to the line counter after reloading it will carry on exactly as if there had been no interrupt at all.

You can copy functions and variables into your workspace from another workspace if you need, so any useful tools (such as a full-screen editor or a format controlled listing function) can be copied when needed and either kept in the workspace or erased from it before it is saved.

This approach removes most of the pain of holding the latest run date, master file identity and any current parameters from one run to the next – they are simply stored in the production version of the workspace which automatically can save a new version of itself each time it runs. There is no need for those troublesome bits of program to store such details in one of the master files in a place where they will be accessible from the beginning of the next run.

APL provides filing systems – and often it isn’t practical to hold all the data in the workspace. If the records are extremely large it may even be necessary to read them in and process them one at a time. But for most purposes the workspace will suffice. Even on microcomputers quite respectable amounts of data can be held without bothering with files.

My BBC microcomputer a version of APL running and the workspace limit is 400K – about the size of a respectable book. On the IBM PC workspaces of up to half a megabyte are common, and with the 68000 they can be as large as you need, up to the address limit of 16 megabytes.

In short the workspace is ideal for programmers. It saves trouble, simplifies manipulation of programs and data, and assures consistency between runs. Why doesn’t any other language have one?
