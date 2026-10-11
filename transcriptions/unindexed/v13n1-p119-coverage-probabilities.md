---
title: Coverage probabilities
authors:
- Norman Thomson
volume: '13'
issue: '1'
page: '119'
unindexed: true
transcribed: 'from page images of VOL.13-NO.1-JULY-1996.pdf, pages 121–122 (printed 119–120; within Technical Correspondence, the first letter under the heading, before Dietrich Trenkler’s letter on LaTeX); Claude, 2026-10-11'
review: draft
tags:
- mathematics and statistics
queries:
- "Untitled in print: a letter under the Technical Correspondence heading; the title is ours."
- "`clb` is Thomson’s Clopper-Pearson function from reference [2]; it is not printed here."
- "Kept as printed: `Z+/(…` in line [2] of `Bin` (no assignment arrow); “2,..8”; “The confidence values boundaries”; “Volume 12, No.3, pp. 98-106, April 1996” (12:3 is dated January 1996)."
---

*From: Norman Thomson, May 1996*
{ .byline }

I received a letter from Dietrich Trenkler, following our recent articles on confidence intervals [1], [2]. In [2] I observed that I did not understand what Dietrich meant by “coverage probabilities”; Dietrich has now explained this, and I am happy to translate his clarification into APL terms which follow on from my version of the Clopper-Pearson routines.

As a reminder, here is the point where, having observed R successes out of, say N=10, 95% confidence intervals are calculated for the true but unknown underlying binomial probability *p*. R can range from 0 to 10, and the specific values of the confidence interval boundaries are:

```apl
      T,,[⍳0]0.95 clb¨10,¨T←0,⍳10
 0  0          0.3085
 1  0.0025286  0.44502
 2  0.025211   0.5561
 3  0.066739   0.65245
 4  0.12155    0.73762
 5  0.18709    0.81291
 6  0.26238    0.87845
 7  0.34755    0.93326
 8  0.44391    0.97479
 9  0.55498    0.99747
10  0.6915     1
```

Now fix on a specific value P of *p*. Each of these 11 intervals either contains P, or it doesn’t. For example, if P=0.5, the intervals corresponding to R in the range 2,..8 contain P. These seven values of R can be regarded as “plausible observations” given this value of P. The sum of the binomial terms for these values of R is the probability that one of the plausible values in the above sense is observed. This is the coverage probability for P.

The confidence values boundaries form a finite set of values, which means that coverage probabilities as a function of *p* have discontinuities at these points. For example as *p* is reduced below 0.44502 the value R=1 comes into the plausible set, and another term is added into the binomial sum. By extending the operations in [2] in the following way

```apl
[0] Z←N(C BinCOV)P;T
[1] ⍝ Z is coverage probability for given P; C is conf. level
[2]  Z←N(P Bin)(P IN¨C clb¨N,T)/T←0,⍳N

[0] Z←N(P Bin)R
[1] ⍝ Z is sum of ⍴R binom terms;R is a set of powers of P
[2]  Z+/((P*R)×(1-P)*N-R)×R!N

[0] Z←L IN R
[1] ⍝ Z is 1 if l is strictly within interval R
[2]  Z←0⌈-××/R-L

      10(0.95 BinCOV)¨0.444 0.445 0.4451 0.4452
0.99315 0.99313 0.97092 0.97095
```

the coverage probabilities for various values of *p* can be obtained, and these discontinuities observed. This is what is illustrated in Dietrich’s graph on p. 93, which was not, as I wrongly suggested, mis-transcribed.

The salient point, as Dietrich points out, is that the coverage probabilities can be proved mathematically to be consistently greater than \(1-\alpha\), something which is not shared by other comparable techniques for calculating confidence intervals.

I hope these additions will further clarify Clopper-Pearson intervals, and associated techniques.

## References

1. *Computing Clopper-Pearson Confidence Limits by the Illinois Method,* D. Trenkler, The Random Vector, Volume 12, No.2, pp. 87-94, October 1995
2. *Technical Note on Confidence Limits,* N. Thomson, The Random Vector, Volume 12, No.3, pp. 98-106, April 1996
