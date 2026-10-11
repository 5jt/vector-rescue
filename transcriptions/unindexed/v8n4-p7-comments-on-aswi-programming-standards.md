---
title: Comments on “ASWI Programming Standards”
authors:
- Ray Cannon
volume: '8'
issue: '4'
page: '7'
unindexed: true
transcribed: 'from page images of VOL.8-NO.4-APRIL-1992.pdf, pages 9–10 (printed 7–8; the only letter in General Correspondence, before British APL Association News); Claude, 2026-10-11'
review: draft
tags:
- development practice
- standards
queries:
- "A letter in General Correspondence, From: Ray Cannon, 1 February 1992, on the paper by FHD v.Batenburg et al in Vector 8.2."
- "Kept as printed: “to all sub-function”; “Are scalar dyadic function not”; “asking it’s audience”; “gross over simplification”."
---

*From: Ray Cannon, 1 February 1992*
{ .byline }

I would like to raise some objections to some of the standards as put forward in the paper “ASWI Programming Standards” by FHD v.Batenburg et al in Vector 8.2.

The main reasons for standards are human readability and maintainability; as the authors state “Good APL functions are readable”. They may, as in this case, also need to define a common subset of APL that all the target machines can work with.

First, the naming of “sub-functions”. Adding a System ID (SID) as a prefix to all sub-function, not only makes it far harder to maintain the workspace but, in extreme cases, may cause difficulties with the symbol table. Trying to find the name of a function from the results of `)FNS` or `⎕NL 3` is much harder if most of the functions start with the same letters. If the SID has to be included in the name, at least put it last, not first.

Next, “imported sub-functions”. This naming convention for these utility functions seems silly to me. What SID is applicable for the utility function `IOTA`? Is it `SIM_IOTA` because it came from the SIMulation of whaling population growth first? Sorry, I’ve missed a point here, it would not be called `SIM_IOTA` but something like `SIM_CNSPIOTA` because it occurred as a sub-function to “splitting” which is a sub-function to “continuous”. Surely, a true utility’s name should be independent of its origin. If the origin of a function is important, then comment it, don’t clutter up the name space.

The standard specifies the use of the underbar character in sub-function names, and lower case alphanumerics in global variable names. These are invalid characters in important mainframe APLs, for example, VSAPL and APL\*PLUS Mainframe. Also APL2 Version 1 does not support lower-case letters. The standard should have given alternative characters to be used in these APLs.

Local variable names are often short, but it seems unnecessary to force local variable names to 4 characters or less as this could make the code less readable. Often a variable may have a “natural name”. Shortening such a natural name to 4 characters may make it so cryptic that the code becomes unreadable.

In the section defining “Good APL functions:”

Point 5:

> “work for missing left arguments” implies ambivalent functions. Again this is an extension to the ISO standard and may not work on all implementations.

and Point 6:

> “receive data in the right argument and control in the left” is a gross over simplification. Are scalar dyadic function not “Good APL functions” because they receive data in both arguments?

I am sorry to be so negative about this, but standards like these cannot be imposed. If standards are to be implemented by programmers, they have to be useful to the author, reasonable and work. For shareware, they must work on any APL ISO conforming implementation, and should work on most of the others.

Following good standards will aid readability. Try rewriting some of the functions from Education Vector following these standards and then asking it’s audience if it helps or hinders.

Ray Cannon
