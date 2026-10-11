---
title: More on Ambivalent Operators
authors:
- Dave Piper
volume: '6'
issue: '3'
page: '93'
unindexed: true
transcribed: 'from page images of VOL.6-NO.3-JANUARY-1990.pdf, page 95 (printed 93; within Technical Correspondence, after unindexed/v6n3-p91-is-it-apl2-or-is-it-me.md); Claude, 2026-10-11'
review: draft
tags:
- language design
- programming techniques
queries:
- "A letter in Technical Correspondence, From: Dave Piper, December 1989, quoting his reply to Claude Henriod. Henriod’s letter, which Piper forwarded, follows on pp.94–96 (unindexed/v6n3-p94-concern-a-possible-feedback.md)."
- "The postal address in the signature block (Rainham, Kent) is omitted."
---

*From: Dave Piper, December 1989*
{ .byline }

Following my letter to Vector discussing an *AMBIVALENT* operator to aid the implementation of ambivalent functions, I received the enclosed letter from Claude Henriod in Switzerland. Subsequently I sent the following reply:

> Dear Claude,
>
> Thanks for the feedback on the ambivalent operator. I apologise for the error omitting a pair of parentheses - they got lost somewhere between keyboard and letter! The error you found occurs because operators have short scope to the right, but long scope to the left. Thus `⎕NC` was taken as the right operand and the quoted string as the right argument to the derived function.
>
> I found your timings most interesting, especially the second batch where the ambivalent operator appeared to provide the quickest solution. I guess this could be a quirk in the implementation. I am opposed to the use of execute to achieve the same result since you lose control of the code (the strength of the function is reduced). In the branching solution you provide, I strongly prefer to branch to a label rather than `⎕LC+X`. I would also use the skipped line to assign a default left argument (as in the execute version) rather than perform a modified calculation.
>
> The functions *AVERAG2* and *AVERAG3* are coded less efficiently since you perform the division before the plus-reduction. This means you are performing many divisions instead of just one. I suspect this could have produced the timing results noted above.
>
> My own criticism of the operator I proposed is that it is still much too complex to achieve such a simple effect. That does not imply I can see a simple solution, however.
>
> I am forwarding a copy of your letter, listings and timings to VECTOR for publication, along with a copy of this letter.

I should like to thank my wife, Helen, for providing a translation of the above into French.

Yours faithfully,

D B Piper
