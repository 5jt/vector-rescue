---
title: Puzzle/Problem Corner
authors:
- Alan Sykes
volume: '5'
issue: '4'
page: '29'
unindexed: true
transcribed: 'from page images of VOL.5-NO.4-APRIL-1989.pdf, page 31 (printed 29; within The Education VECTOR, after its editorial); Claude, 2026-10-11'
review: draft
tags:
- competitions and puzzles
- mathematics and statistics
- education
queries:
- "No byline is printed; the Education Vector’s own contents list (printed 27) gives Puzzle Corner to Alan Sykes. It follows his editorial and precedes the Letters (unindexed/v5n4-p30-letter-3-million-pcs-for-the-soviet-union.md)."
- "`6×+/÷⍳6` was run in Dyalog APL as a check on the transcription; it gives 14.7."
---

In keeping with the theme of ‘Understanding Randomness through APL’ consider the age-old ‘coupon-collecting’ problem. I believe ‘cigarette cards’ in tea-packets etc. are coming back into fashion and so the topic has some relevance to everyday life!

Suppose there are six different cigarette cards in a set, and that each packet of tea contains one of the six cards chosen at random. How many packets (on average) do we need to buy to get the whole series? I know of course that there is a very neat theoretical solution to this problem that is easily computed in APL - the answer is `6×+/÷⍳6` which equals 14.7.

The problem here is to apply APL to simulate this random process. Readers are asked to submit APL solutions that provide one simulation and then to consider how to provide a sufficiently large sample of simulations efficiently, so that an average value of about 14.7 can be derived. Submissions that present more than one method together with an appraisal of their relative merits are encouraged.

(Editorial Note: I was reminded of this problem at a workshop on simulation at the Sheffield conference - at the time I only had a BBC micro with BASIC at my disposal and it took me about an hour to write a program and produce 14.6 as the average of 1000 simulations!)
