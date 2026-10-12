---
title: Second Generation APLs on the PC
authors:
- Adrian Smith
volume: '5'
issue: '4'
page: '54'
unindexed: true
transcribed: 'from page image of VOL.5-NO.4-APRIL-1989.pdf, page 56 (printed 54); Claude, 2026-10-12'
review: draft
tags:
- implementations
- reviews
queries:
- "Contents line “2nd Generation APLs on Micros ...”, page 53; the printed heading is “Second Generation APLs on the PC”, with the byline “Introductory notes by Adrian Smith”. Printed 53 carries “Books Received for Review” (unindexed/v5n4-p53-books-received-for-review.md) and “IBM Personal Computing in Schools” (unindexed/v5n4-p53-ibm-personal-computing-in-schools.md); this piece is on printed 54 only. The Contents line’s page is corrected to 54."
- "Kept as printed: “Peter Donnelly's notes on page 81”, where the Contents page puts Peter Donnelly’s “Dyadic Systems” at page 78 (art10002870); “NEXT”."
---

*Introductory notes by Adrian Smith*
{ .byline }

The Technical Editorial in VECTOR 5.3 made the point that microcomputer hardware is finally catching up with the demands made of it by APL. We can at last have decent workspaces (I get over 3Mbyte of `⎕WA` in IBM's APL2/PC on my PS/2 Model-70), and the arithmetic is back to the mainframe standard with proper long integers and real bitty booleans. What's more these beasties go rather fast! Accordingly we have three (going on four) 386-specific APL systems to look at:

1. STSC's APL\*PLUS II system. This is currently at the top end of the scale in terms of both performance and price. Peter Cyriax has taken a technical perspective, and Ajay Askoolum (of the Legal & General Assurance Society Ltd.) has looked at the product from the application side.
2. SAX from I.P. Sharp Associates. SAX was implemented as a joint development project between I.P. Sharp and STSC. The software is based on the STSC Unix APL, but the language follows SHARP APL, not the STSC product. Please check the note at the end of the review for a statement from IPSA on the availability of this product.
3. IBM's APL2/PC (32 bit). Dick Bowman is reviewing this for us for VECTOR 6.1. In price performance terms it really is a rather remarkable product. For £348 you get 32-bit arithmetic, workspace up to 15Mbyte (with no restrictions on object size), an APL2 interpreter (with almost nothing that matters left out) and a rather faster system than STSC's APL\*PLUS/PC release 8. It requires an 80387 maths co-processor. David Selby gives a brief summary of this APL (or should we say **his** APL) on page 82.
4. Dyalog APL for MS DOS. The α-test version of this becomes available at the end of May, and we have every hope of getting a ‘first impressions’ into VECTOR 6.1. Some idea of its features can be gleaned from Peter Donnelly's notes on page 81 of this VECTOR.

I think we are moving into interesting times! We shall soon be looking towards the 80486 (some 5 times the speed of the 386), and towards I-APL on machines like NEXT and the transputer boards. Watch this space!
