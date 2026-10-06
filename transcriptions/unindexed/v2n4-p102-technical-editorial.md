---
title: 'Technical Editorial: Utility functions'
authors:
- Jonathan Barman
- Dave Ziemann
volume: '2'
issue: '4'
page: '102'
unindexed: true
transcribed: 'from page image of VOL.2-NO.4-APRIL-1986.pdf, page 104 (printed 102; the technical correspondence follows on p.103); Claude, 2026-10-05'
review: draft
tags:
- programming techniques
- development practice
queries:
- "Slip transcribed as printed: “that is well documented” (that it is)."
---

by Jonathan Barman and Dave Ziemann
{ .byline }

Having just lost a couple of utility functions, and having spent an extremely aggravating couple of hours recreating them, the question arose of how to keep track of utility functions so that they are available when needed.

Ideally, there should be a book of every function that anyone could ever want, but although there are several good books published, they can never cover the full field. Everyone has slightly different requirements, and one person’s utility function may be useless to another; particularly true where different APLs are used under different operating systems.

How should one keep utility functions? Probably the most common method on a mainframe computer is to keep them in public workspaces; each workspace containing the functions which will help solve a particular class of problems. New utility functions are usually created while developing a system, but in the general rush and panic of meeting a deadline the small job of adding the functions to the appropriate public workspace can be forgotten. Hence the “lost” functions, which were somewhere around but not in the proper utility workspace, or if they were, did not have a name that was very meaningful.

Another popular method of managing utilities is to store them on file, in their ⎕CR or ⎕VR formats. The application does not need to keep the functions in the stored workspace, but merely defines them when they are needed at run time. This has the advantage that each utility is stored centrally, but may be accessed by many users. In this way any given function can be revised by a supervisor and simultaneously made available to all the applications that use it. Such a system was described by Maurice Jordan of British Airways at a BAA meeting last year.

Part of the success of the FINNAPL idiom library is that is well documented and has very simple code that is generally applicable. Several possible solutions are given for a problem, and although there is no attempt to say which method is best it is often rewarding to consider each of them.

*“Quote-Quad”* has a regular column of algorithms, but has not as yet published a compendium, so all the past issues have to be purchased, which is rather awkward for newcomers to APL.

Has anyone got a documented set of utility functions that could be published? Do you feel there is a need for such a publication, or should we all write our own utilities? Let’s hear your views.
