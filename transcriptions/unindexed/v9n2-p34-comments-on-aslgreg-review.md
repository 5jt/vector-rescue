---
title: Comments on the ASLGREG Review
authors:
- Alan Sykes
volume: '9'
issue: '2'
page: '34'
unindexed: true
transcribed: 'from page images of VOL.9-NO.2-OCTOBER-1992.pdf, pages 36–37 (printed 34–35; follows art10007490, within The Random Vector); Claude, 2026-10-11'
review: draft
tags:
- reviews
- mathematics and statistics
queries:
- "Alan Sykes’s reply to Jon Sandles’s review of ASLGREG (art10007490), within The Random Vector; it is followed by his “Corrections to Known Bugs in ASLGREG (September 1992)”, transcribed separately as unindexed/v9n2-p35-corrections-to-known-bugs-in-aslgreg.md."
---

*by Alan Sykes*
{ .byline }

I am grateful to Jon Sandles for his careful review of ASLGREG. I think it is fair to say that his views on the software have been echoed by other people who have used it, which is very heartening to those of us who have been involved in its production! It has now been available for some 10 months, and in that time only five bugs have materialised. They are easily put right and the corrections are listed below.

Jon raises a number of important points that deserve some response. On the question of prediction, I do have a beta-test version of a function `PREDICT` which allows the user to obtain predicted values corresponding to given values of predictor variables. (This is not a simple function to write in view of the generality of model specification!) Further work might perhaps incorporate confidence intervals. Such a function would be useful in producing graphical output e.g. plotting fitted values. (On this subject Norman Thomson has sent me some first thoughts on graphical tools for ASLGREG, but I have not had time to do further work in this direction as yet.)

I agree that there may well be problems of formatting and welcome specific examples to aid in correcting this. (Note however that the user does have the option of outputting straight unformatted numbers to the screen.)

Finally, on the question of dealing with missing values, it is not quite true to say that there are no provisions. Suppose that all your regression data was contained in a matrix `M` with missing values indicated by `9999`. Then APL comes to the rescue to create the zero-one vector

```apl
      WT←∧/M≠9999
```

and this can be declared as a priorweight vector so that the regression analysis is performed only on the data points for which all information is available. However, I agree that no further missing data facilities such as those in GENSTAT are available.
