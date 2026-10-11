---
title: APL and the rank operator
authors:
- Norman Thomson
volume: '14'
issue: '1'
page: '7'
unindexed: true
transcribed: 'from page images of VOL.14-NO.1-JULY-1997.pdf, page 9 (printed 7; within Correspondence, after Norman Thomson’s “Optimizing the Antecedent Precipitation Index”); Claude, 2026-10-11'
review: draft
tags:
- language design
queries:
- "A letter in Correspondence, From: Norman Thomson, 12 May 1997; it follows his “Optimizing the Antecedent Precipitation Index” and precedes Joseph De Kerf’s “The Enclose of an Empty Array”."
- "The glyph in Burke’s quoted expression `[⍬]` is printed as a circle with a bar, the zilde of the APL font; read as `⍬`."
---

*From: Norman Thomson, 12 May 1997*
{ .byline }

Chris Burke in his article *APL and J(4) : Function Application and the Axis Operator* does APL an injustice when he dismisses the axis operator as a “patchwork of special cases”. He says that the APL interpreter gets the error messages wrong — he does not say *which* interpreter he is talking about — IBM interpreters correctly give *AXIS ERROR* for the two “wrong” messages he cites for transpose and rotate. He also says that “we would expect that `(⍴,[⍬]A)↔(⍴A),1` ”. This is precisely what happens in APL2, that is `(⍴,[⍳0]A)↔(⍴A),1` .

While it is true that the rank operator is a unifying concept, and that the APL axis notation has always been something of an inconsistency, it is unfair to condemn the APL syntax for transpose and rotate which were standardised long before the rank operator was conceived. In both cases, the values necessary to differentiate the various possible cases can be provided with total adequacy as function parameters, and there is logically no reason why such definitions should be altered to an operator form just because this route has been chosen in J.

As a historical footnote, Chris says of dyadic APL functions that “In theory... a semi-colon could be used to delimit the ranks of left and right axes”. The first experimental version of the IBM APL2 interpreter did just that, but the idea was abandoned.
