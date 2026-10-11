---
title: Let's Integrate - Using APL (Education Vector, July 1991, p.22)
authors:
- Tony O'Hagan
volume: '8'
issue: '2'
page: '20'
unindexed: true
transcribed: 'from page images of VOL.8-NO.2-OCTOBER-1991.pdf, page 24 (printed 20; within The Education Vector’s Letters, after Andy Pole’s, before Peter Branson’s); Claude, 2026-10-11'
review: draft
tags:
- mathematics and statistics
- education
queries:
- "A letter under Letters in The Education Vector, headed “From: Tony O’Hagan, University of Nottingham. Let’s Integrate - Using APL (Education Vector, July 1991, p.22).”. It answers Alan Sykes’s article (art10009660)."
---

*From: Tony O’Hagan, University of Nottingham.*
{ .byline }

**Let’s Integrate - Using APL (Education Vector, July 1991, p.22).**

I would just like to make a technical point about Simpson’s rule. Applied to 3 points it is unarguably a good thing. It integrates a quadratic exactly, and so on. You can easily justify the weight 4 in the middle because of smoothness of the function. Whichever way it curves, the area under a piecewise linear interpolant (trapezium rule) underestimates or overestimates the integral according as the middle point is high or low. So we want more weight than the value 2 given by the trapezium rule.

What is not sensible is applying the rule repeatedly on 2m+1 points with weights 1, 4, 2, 4,…, 4, 1. I know this is often found in textbooks, but think about it. That will integrate exactly a function that is piecewise quadratic. That is, a quadratic on intervals 1 and 2, then a different quadratic on 3 and 4, and so on. Why is this sensible? Why not a function that is quadratic on intervals 2 and 3, 4 and 5, etc.? That makes just as much sense. Why not use that, with a bit of trapezium rule on the first and last intervals? Then you get weights 1.5, 2.5, 4, 2, 4,…, 4, 2.5, 1.5. If this is just as good as the other, why not average the two sets of weights, giving 1.25, 3.25, 3, 3,…, 3, 3.25, 1.25. Now you have almost exactly got back to the trapezium rule with weights proportional to 1, 2, 2,…, 2, 1.

There is no good heuristic argument for weighting the even points 4 and the odd points 2. Repeated use of Simpson’s rule looks odd, and it really does not make sense. I always use the trapezium rule for a lot of equally spaced points in one dimension. (In high dimensions, when the sheer number of function evaluations is a problem, then we need other rules, but I still do not use Simpson’s in practice.)
