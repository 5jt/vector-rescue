---
title: The Hungarian Naming Convention
authors:
- Ray Cannon
volume: '9'
issue: '1'
page: '9'
unindexed: true
transcribed: 'from page images of VOL.9-NO.1-JULY-1992.pdf, page 11 (printed 9; precedes art10006850, in General Correspondence); Claude, 2026-10-11'
review: draft
tags:
- development practice
- performance
queries:
- "A letter in General Correspondence, From: Ray Cannon, March 1992; the first letter under the section heading, followed by David Piper’s “With reference to STSC’s Double Whammy” (art10006850)."
---

*From: Ray Cannon, March 1992*
{ .byline }

The Hungarian naming convention has been well documented elsewhere, but is basically a naming convention in which the object class or type is used as a prefix in its name. Thus lots of objects of the same class will all start with the same prefix. This can, depending on implementation, have one very big disadvantage in large APL systems: it can slow them down.

The reason for this is the way symbol tables are often designed to work. They use some hashing algorithm to convert the object’s symbol into an address to start searching from. However, if lots of symbols produce the same address, as might happen if they all start with the same prefix, the number of symbol entries needing to be searched is much higher than if all the symbols produced very different addresses.

As an example of this type of behaviour, I have seen a system running extremely slowly due to the fact that every file in the file system started with the same letter. Renaming all the files with different letters speeded up the whole process.

So the idea I would like to put forward, is to use a class postfix rather than a class prefix. That way the names would not all start the same and the hashing algorithms would produce different addresses, hence shorter searches. This naming convention could then be called Reverse Hungarian Notation.
