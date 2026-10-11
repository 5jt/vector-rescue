---
title: While still in J ...
authors:
- Norman Thomson
volume: '13'
issue: '3'
page: '12'
unindexed: true
transcribed: 'from page image of VOL.13-NO.3-JANUARY-1997.pdf, page 14 (printed 12; within Correspondence, after art10009330); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- performance
queries:
- "A reply to Nick Cox’s letter “While in J...” (Vector 13.2, p.10). It is followed on the same page by Don Mattern’s “British J Association?”, transcribed separately as unindexed/v13n3-p12-british-j-association.md."
- "The J phrases were not run."
- "Kept as printed: “Ctl-Shift-C”; “(2Mb vs.16MB)”."
---

*From: Norman Thomson, 24 November 1996*
{ .byline }

Nick Cox in a letter (*Vector* Vol.13, No.2, p.10) compares a Fortran-like J program to the functionally equivalent one-liner `+/"1(* x.&^@i.@-@#)\y.` and asks whether a quicker and more concise J script can be produced. As far as the second requirement is concerned, Nick should observe that he is in fact evaluating a polynomial in his variable k (`x.` in the above), and a functionally equivalent verb to the above is `>@(#.&.><\)`. This is at least as fast in execution as either of Nick’s programs. Space depends of course on the length of the series `y.` — with 1000 terms, the polynomial version requires one-eighth of that needed by Nick’s one-liner (2Mb vs.16MB), although naturally the step by step version is superior to either (30KB).

As a tail-piece, timing experiments such as the above can be interrupted by Ctl-Shift-C. This piece of information, which I have not been able to find in any of the J manuals or Help material, was passed to me by Bill McLean.
