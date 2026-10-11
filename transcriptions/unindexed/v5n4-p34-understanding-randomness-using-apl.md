---
title: Understanding Randomness Using APL
authors:
- Alan Sykes
volume: '5'
issue: '4'
page: '34'
unindexed: true
transcribed: 'from page images of VOL.5-NO.4-APRIL-1989.pdf, pages 36–44 (printed 34–42; within The Education VECTOR, after I-APL News: The State of the Project); Claude, 2026-10-11'
review: draft
tags:
- mathematics and statistics
- education
- programming techniques
queries:
- "The last piece in the Education Vector, after unindexed/v5n4-p31-i-apl-news-state-of-the-project.md; the Reviews section follows on printed 43. FREQTAB and BAR come from the author’s “Counting in APL” (Vector 5:2) and are not listed here."
- "PBAR, PROBTAB and E, and the expressions without random numbers, were run in Dyalog APL (⎕IO←1, ⎕PP←4) as a check on the transcription. PROBTAB [1] is printed `Z←Z[Z]`, without the grade-up; with `Z[⍋Z]` the function reproduces the printed tables and charts. Kept as printed."
- "The bar charts were counted from the page images; the simulated charts each total 100. The chart under `PBAR ⎕←DISTMAX←…` is printed with bars of 3 7 14 18 21 37 boxes, where PBAR gives 2 7 11 16 20 24 for the probabilities printed above it. Kept as printed."
- "Kept as printed: `P E(X) 3.5` with the result on the same line as the expression; “specified by X1 2 3 4 5 6 and P(61)6” in the text, with the assignment arrows, rho and divide lost; `+/?100 2⍴60` (presumably `6`); “each of the six possible results are equally likely”; “The probabilities associated with each of these outcomes is however calculated”."
---

*by Alan Sykes*
{ .byline }

## Introduction

My aim in this article is to use APL and some of the tools introduced in previous articles to explore randomness. As I showed in the first of my articles, quite surprising patterns can occur where random phenomena are concerned, and in a sense that’s what Statistics is all about - order from chaos.

Many people find Statistics very difficult to follow. One of the reasons for this is the need to think on two planes at the same time. First there is the statistical recipe - what you do with the data. But to understand why the recipe makes sense, the theoretical model for randomness also needs to be studied. Through the interplay between recipe and theoretical model sense can be made of the results of applying the recipe. In this article I hope to integrate both planes of thought through the use of APL.

## Throwing a Fair Die

Let’s start with throwing a die (singular of dice). APL allows us to simulate throwing a die using `?` - e.g.

```apl
      THROW←?120⍴6

      .5 1 FREQTAB THROW
1 22
2 15
3 22
4 14
5 19
6 28
```

Can we make sense of these results? If the die is well-behaved, then on each throw, each of the six possible results are equally likely. This means that if we denote the outcomes by the vector `X←1 2 3 4 5 6` then the associated probabilities must be given by the vector `P←(6⍴1)÷6`. The interpretation is that on one throw the probability of obtaining a 1 is one sixth, and the understanding is that in a large number of throws the proportion of 1’s will be about one sixth. Equivalently, we can say that the expected frequency of each possible number in 120 throws is 20.

Some care must be taken to interpret the word ‘expected’ correctly. It does not mean that the observed number of 1’s equal to 22 is wrong - what it does mean is that if we repeatedly took samples of 120 throws of a die, then the number of 1’s in each sample would be a random number with an average value (in the long run) of 20.

Can we make any other observations concerning expected frequencies? If each of the six possible outcomes is equally likely, then we would expect one half of all observations to be even, i.e. 60 even numbers out of the 120 total. The observed number of even numbers in `THROW` can be calculated from the frequency table or directly by the expression

```apl
      +/T=⌊T←THROW÷2
57
```

(This simple expression uses `⌊` to round down to the next smallest integer and also employs `T` as a temporary variable - a useful trick.)

To proceed further, we need to be able to calculate the average value or sample mean. The function `MEAN` is probably the most often quoted APL function:

```apl
     ∇R←MEAN DATA
[1]   R←(+/DATA)÷⍴DATA
     ∇
```

Alternatively using the direct definition, we write:

```apl
MEAN:(+/⍵)÷⍴⍵
```

Applying `MEAN` to `THROW` we have:

```apl
      MEAN THROW
3.6416667
```

Corresponding to this value is the expected value for the throw of a die which can be calculated using the vectors `X` and `P` previously defined. Remembering that P contains the expected proportion of the throws that equal the values 1 2 3 4 5 6, it is clear that the expected value for a throw of a die is given by the sum of the probabilities times the values, namely `+/P×X` or `P+.×X`, giving in this case the value 3.5. This idea is embodied in the expected value function given by:

```apl
     ∇R←P E X
[1]   R←(,P)+.×,X
     ∇
```

or

```apl
E:(,⍺)+.×,⍵
```

This makes it possible to emulate the mathematical notation very closely. For example, using a pair of redundant brackets, we may write:

```apl
P E(X) 3.5
```

Try convincing yourself that this calculation tells you what would happen in the long run by statements such as `MEAN ?1000⍴6`.

Let’s consolidate the discussion so far by another simple example. Suppose our die was not fair, and that a six was three times as likely as the other values. At the theoretical level the probabilities `P` must be calculated using `P←1 1 1 1 1 3÷8`. Using our expected value function `E`, we now get the expected value equal to 4.125:

```apl
      P E(X)
4.125
```

This calculation tells us to expect a sample mean of around 4.125 when such a die is used. Let’s see if this is the case. To simulate throws of the new die, let the vector `A←1 2 3 4 5 6 6 6`. It is clear that if we sample at random from `A`, then we will have three times the chance of selecting a 6 as any other number.

```apl
      THROWB←A[?100⍴8]

      BAR .5 1 FREQTAB THROWB
1|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
2|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
3|⎕⎕⎕⎕⎕⎕⎕⎕
4|⎕⎕⎕⎕⎕⎕⎕⎕⎕
5|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
6|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
```

The bar chart shows us that the simulation works, giving an excess of 6’s over the other values. Calculating the mean of `THROWB`:

```apl
      MEAN THROWB
4.29
```

… gives a value quite close to that expected.

## Simulating a Biased Die

The simulation of the biased die poses a general problem: given a set of probabilities P associated with a set of values X, how can we choose numbers from X according to the probabilities specified by P? One possibility is to represent the probabilities in P correct to, say, two decimal places, and then construct a vector A which contains the values in X repeated `100×P` times; i.e. an extension of the idea used already.

The more correct procedure involves using numbers which are randomly chosen between 0 and 1 - the so-called Uniform Distribution. Consider the APL function `RND`:

```apl
     ∇ R←RND N;T
[1]   R←(¯0.5+?N⍴T)÷T←100000
     ∇
```

or

```apl
RND:(¯0.5+?⍵⍴T)÷T←100000
```

Then `RND 3` produces 3 numbers chosen at random between 0 and 1

```apl
      RND 3
0.845315
0.351765
0.945705

      BAR 0 .1 FREQTAB RND 100
0.05|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
0.15|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
0.25|⎕⎕⎕
0.35|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
0.45|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
0.55|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
0.65|⎕⎕⎕⎕⎕⎕⎕
0.75|⎕⎕⎕⎕⎕⎕⎕⎕
0.85|⎕⎕⎕⎕⎕⎕
0.95|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
```

To choose an element of X according to the probabilities in P, we proceed as follows:

1. select a random number r between 0 and 1;
2. determine n such that there are at most n of the elements of `+\0,P` less than r;
3. choose X[n].
{ type="a" }

For example, suppose `P←(1 2 1 1 1 4)÷10`, so that if `X←1 2 3 4 5 6`, then a six is twice as likely as a 2 which in turn is twice as likely as a 1,3,4 or 5. To choose a value of X according to the probabilities in P we can write:

```apl
      X[+/(RND 1)>+\0,P]
3
```

This does not demonstrate that the probabilities are being adhered to. To do this we need to repeat this procedure many times. The easiest way to do this is to use the ‘jot-dot’ construction we used in my first article on counting.

```apl
      Y←X[+/(RND 100)∘.>+\0,P]

      BAR .5 1 FREQTAB Y
1|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
2|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
3|⎕⎕⎕⎕⎕⎕⎕⎕⎕
4|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
5|⎕⎕⎕⎕⎕⎕⎕⎕⎕
6|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
```

## Throwing a Die Twice

In the previous sections, we have tried to understand the theoretical model for randomness involving probabilities and expected values in terms of what happens when the experiment of throwing a die is repeated many times. Under this comparison, probability is understood in terms of long-run proportion, and expected values in terms of sample means. If you try the above experiments with increasing values of the sample size, you will note that the predictions of the theoretical model are more nearly adhered to as the sample size increases. For example, look at the proportion of even numbers in samples of size 10, given by:

```apl
      BAR 0 .1 FREQTAB .1×+/T=⌊T←.5×?100 10⍴6
0.05|⎕⎕⎕
0.15|⎕⎕⎕⎕
0.25|⎕⎕⎕⎕⎕⎕⎕⎕⎕
0.35|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
0.45|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
0.55|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
0.65|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
0.75|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
0.85|⎕⎕
```

… and the equivalent proportion in samples of 100, given by:

```apl
      BAR 0 .1 FREQTAB .01×+/T=⌊T←.5×?100 100⍴6
0.05|
0.15|
0.25|
0.35|⎕⎕
0.45|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
0.55|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
0.65|⎕⎕⎕⎕⎕
```

It is important to be able to understand this theoretically. Hence we need to develop the extension of our model to looking at samples.

Returning to throwing a fair die, consider throwing it twice. No one would question the fact that the score on the first throw is a different entity to that on the second throw, though of course they could both equal the same numeric value. However the distribution for each throw is the same, and specified by X1 2 3 4 5 6 and P(61)6.

What of the distribution of both scores? Here, APL fails us (at least at the first generation level) because the possible outcomes can be displayed in the form

```apl
1 1  1 2  1 3  1 4  1 5  1 6
2 1  2 2  2 3  2 4  2 5  2 6
3 1  3 2  3 3  3 4  3 5  3 6
4 1  4 2  4 3  4 4  4 5  4 6
5 1  5 2  5 3  5 4  5 5  5 6
6 1  6 2  6 3  6 4  6 5  6 6
```

which ought to be achieved by `X∘.,X` (because 1,2 catenates 1 and 2 together to form the vector 1 2 for example).

The probabilities associated with each of these outcomes is however calculated with the expression `P∘.×P` (assuming that the two throws are ‘independent’), consisting of a 6 by 6 matrix of values equal to one thirty-sixth.

However, if we wish to look at the distribution of an actual numerical value derived from the two throws, then APL provides us with very elegant and satisfactory tools to perform the distribution arithmetic. As a first example suppose S is the sum of the two throws. Then the set of possible values (with repetitions) is given by `X∘.+X` and the associated probabilities are given by `P∘.×P` as before. The distribution of S is then given by summing up all the probabilities associated with equal values in the array `X∘.+X`.

To help us in this section, we need two further functions. First `PBAR` is a simple alteration of `BAR` so that it will display a bar chart of probabilities rather than frequencies, obtained from `BAR` by multiplying the probabilities by 80 (for an 80 character screen). Secondly we need an equivalent of `FREQTAB` that accumulates probabilities associated with the same numerical values. The functions are as follows:

```apl
     ∇ B←PBAR F
[1]   B←(⍕F[;,1]),'|',' ⎕'[1+F[;2]∘.≥⍳⌈/F[;2]←⌊.5+80×F[;2]]
     ∇

     ∇ R←P PROBTAB X;Z;V;PR;I
[1]   Z←,X ⋄ Z←Z[Z] ⋄ V←(I←Z≠¯1⌽Z)/Z ⋄ R←1,1↑Z ⋄ →(0=1↑I)/0
[2]   PR←+/(V∘.=,X)×((⍴V),⍴,X)⍴,P
[3]   R←V,[1.5]PR
     ∇
```

Now we can investigate the distribution of the sum of two throws of a die with X and P as last defined.

```apl
      ⎕PP←4

      (P∘.×P) PROBTAB X∘.+X

 2    0.02778
 3    0.05556
 4    0.08333
 5    0.1111
 6    0.1389
 7    0.1667
 8    0.1389
 9    0.1111
10    0.08333
11    0.05556
12    0.02778
```

Note that the probability that the sum is equal to 7 is one sixth, as out of the 36 possible equally likely values for the outcomes of throwing a die twice, there are six of them such that the sum of the two scores is 7.

Further,

```apl
      PBAR DIST←(P∘.×P) PROBTAB X∘.+X

 2|⎕⎕
 3|⎕⎕⎕⎕
 4|⎕⎕⎕⎕⎕⎕⎕
 5|⎕⎕⎕⎕⎕⎕⎕⎕⎕
 6|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
 7|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
 8|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
 9|⎕⎕⎕⎕⎕⎕⎕⎕⎕
10|⎕⎕⎕⎕⎕⎕⎕
11|⎕⎕⎕⎕
12|⎕⎕
```

… and we see the pattern of increasing and decreasing probabilities that we derived from simulation in the first of my articles on Counting in APL. Alternatively we can produce a simulation of this distribution using:

```apl
      +/?100 2⍴60
```

and so

```apl
      BAR 1.5 1 FREQTAB SUM←+/?100 2⍴6
 2|⎕⎕⎕
 3|⎕⎕⎕
 4|⎕⎕⎕⎕⎕⎕⎕⎕⎕
 5|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
 6|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
 7|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
 8|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
 9|⎕⎕⎕⎕⎕⎕⎕
10|⎕⎕⎕⎕⎕⎕⎕
11|⎕⎕⎕⎕⎕⎕
12|⎕
```

Note the similarity in the two bar charts. Further note that `MEAN SUM` gives the answer 6.84, quite close to the value of `DIST[;2] E DIST[;1]` which of course gives the answer 7. The fact that the distribution of the sum of two throws peaks about the middle value is due to a very important mathematical theorem, called the Central Limit Theorem, a consequence of which is that the distribution of the sample mean is nearly always more closely centred around the theoretical mean than the distribution of just one observation. For example, compare the distribution of one throw, displayed by

```apl
      PBAR P PROBTAB X
1|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
2|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
3|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
4|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
5|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
6|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
```

and the distribution of the mean of three throws, given by

```apl
      PBAR (P∘.×P∘.×P) PROBTAB (X∘.+X∘.+X)÷3
1    |
1.333|⎕
1.667|⎕⎕
2    |⎕⎕⎕⎕
2.333|⎕⎕⎕⎕⎕⎕
2.667|⎕⎕⎕⎕⎕⎕⎕⎕
3    |⎕⎕⎕⎕⎕⎕⎕⎕⎕
3.333|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
3.667|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
4    |⎕⎕⎕⎕⎕⎕⎕⎕⎕
4.333|⎕⎕⎕⎕⎕⎕⎕⎕
4.667|⎕⎕⎕⎕⎕⎕
5    |⎕⎕⎕⎕
5.333|⎕⎕
5.667|⎕
6    |
```

The Central Limit Theorem tells us that, barring a few pathological examples, no matter what shape the distribution of one observation is, the bell-shaped curve of the Normal or Gaussian distribution will appear as you look at the distribution of the sample mean, providing the size of the sample is large enough. Let’s take one more example of the calculus of distributions. Suppose, instead of calculating the sum of the two scores, we calculate the maximum.

```apl
      PBAR ⎕←DISTMAX←(P∘.×P) PROBTAB X∘.⌈X
1 0.02778
2 0.08333
3 0.1389
4 0.1944
5 0.25
6 0.3056

1|⎕⎕⎕
2|⎕⎕⎕⎕⎕⎕⎕
3|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
4|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
5|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
6|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
```

Not surprisingly, larger probabilities are given to higher values.

The expected value is given by `DISTMAX[;2] E DISTMAX[;1]` and equals 4.472. If we simulate this example with the expression:

```apl
      MAX←⌈/?100 2⍴6
      BAR .5 1 FREQTAB MAX
1|⎕⎕⎕⎕
2|⎕⎕⎕⎕⎕⎕⎕⎕⎕
3|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
4|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
5|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
6|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
```

we see that again, the correspondence between theoretical model and simulation is close. Further `MEAN MAX` gives the sample mean of 4.32.

So, to round off, we have demonstrated some of the patterns that can occur when randomness is explored, and in particular shown how APL provides superb tools for the calculations involved with the theoretical models. However I must add one slight word of caution: all the simulation results shown here were to some extent chosen because they were close to the results predicted. If you try them for yourself, you will find that randomness may sometimes hide the patterns. For example, in the distribution of the maximum of two throws of a die the probabilities of 1 2 3 4 5 or 6 are increasing. This pattern may well be absent from the simulation results! So perhaps Lady Luck has the last word after all.
