---
title: The Enclose of an Empty Array
authors:
- Joseph De Kerf
volume: '14'
issue: '1'
page: '8'
unindexed: true
transcribed: 'from page images of VOL.14-NO.1-JULY-1997.pdf, page 10 (printed 8; within Correspondence, after Norman Thomson’s “APL and the rank operator”); Claude, 2026-10-11'
review: draft
tags:
- language design
queries:
- "A letter in Correspondence, From: Joseph De Kerf, 1 May 1997; it follows Norman Thomson’s “APL and the rank operator” and precedes Bob Brown’s “Year 2000 — why the Consternation?”."
- "The writer’s postal address, printed below the letter, is omitted."
---

*From: Joseph De Kerf, 1 May 1997*
{ .byline }

ISO APL and the proposed standard for Extended APL define an empty array *A* as an array, the count of which is 0, the count being the product of the shape list of the array (`×/⍴A`). APL books and manuals translate this by defining an empty array as an array of rank 1 or more with at least one length of its axes being 0.

So, empty scalars do not exist. The basic idea seems to be that, as a scalar has no dimensions, it cannot be empty. But what about the enclose of an empty array, for instance the enclose of the empty numeric vector (`⊂⍳0`) or the enclose of the empty character vector (`⊂''`)? It’s a scalar: its rank is 0. On the other hand, it has no value. Should we call such a scalar a ‘pseudo empty scalar’ or a ‘non-valued scalar’?

Joseph De Kerf
