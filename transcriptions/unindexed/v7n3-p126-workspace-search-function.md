---
title: Workspace search function
authors:
- Peter Branson
volume: '7'
issue: '3'
page: '126'
unindexed: true
transcribed: 'from page images of VOL.7-NO.3-JANUARY-1991.pdf, page 132 (printed 126; within Technical Correspondence, the first letter, before Packaged Workspaces in APL2/370); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- development practice
queries:
- "Untitled in print: a letter, “From: Peter Branson, 7th Nov 1990”, the first under the Technical Correspondence heading; the title is ours. It answers Dave Piper’s letter in Vector 7.2, p.133 (unindexed/v7n2-p133-teaching-nested-arrays.md)."
- "Kept as printed: “David Piper’s reply” (signed Dave Piper); “As regard packaging”."
---

*From: Peter Branson, 7th Nov 1990*
{ .byline }

A couple of final remarks, please, on David Piper’s reply in Vector 7.2.133 to my letter of Vector 6.4.95.

He is partly right about the reason the original workspace search function ran so slowly; it was full of ‘each pepper’, but that was not the only reason. The author of the original had tried to please everybody by looking for all occurrences of the string in everything. By restricting this to functions and operators, and looking for only the first occurrence on each line, a further big saving was made. I find that this suits my needs 99 per cent of the time, and I rarely need to use a fuller version.

My second point takes us back again to the pornography, or otherwise, of dynamic function fixing, and I certainly can’t agree with his use of the word ‘ridiculous’ here. However, I will agree that this technique can only safely be used on very rare occasions, and I contend that mine was one of these. A classic case of the wrong way of doing this occurs in IBM’s ADRS2 code (particularly ADRS2BG) where, in some places, functions are redefined dynamically to ‘fix’ otherwise undetectable bugs!!! (Have you ever tried maintaining that code?)

David’s suggested alternatives are fine in their way, but don’t suit me. I don’t use indirect copy for utilities because I do not want all the utilities cluttering every workspace I am working on; I have spent too much time in the past creating different lists and then forgetting to maintain them.

As regard packaging, I think this is the best way in the long term, especially for central maintenance, and we will probably move this way when (if?) we get some time to clean our act up a bit.

In the meantime I shall continue doing it my way, and I see that I am not the only one. Have a look at Tibor Horvath’s *CYCLE* function on page 2 of APLBUG Newsletter, June 1990.
