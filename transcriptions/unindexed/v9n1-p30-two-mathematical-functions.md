---
title: Two Mathematical Functions
authors:
- C.E. Williams
volume: '9'
issue: '1'
page: '30'
unindexed: true
transcribed: from page images of VOL.9-NO.1-JULY-1992.pdf, pages 32–33 (printed 30–31; follows art10005920, inside its index page range); Claude, 2026-10-03
review: draft
---

by C.E. Williams
{ .byline }

C.E. Williams (Cold Keld, Loweswater, Cockermouth, Cumbria) writes: a couple of functions which may be of use to someone. The function `CHAR4`, to find the characteristic equation of a 4×4 matrix, uses Bocher’s formulas which is a good illustration of APL’s ease of programming. It is easy to adapt for any order of matrix.

```
[0]     RES←CHAR4 A;B;C;D;A1;A2;A3;A4;S1;S2;S3;S4
[1]     S1←+/1 1⍉A        ⍝ Sums major diagonal
[2]     B←A+.×A           ⍝ Matrix multiplication
[3]     S2←+/1 1⍉B        ⍝ Repeat
[4]     C←B+.×A
[5]     S3←+/1 1⍉C
[6]     D←C+.×A
[7]     S4←+/1 1⍉D
[8]     A1←-S1
[9]     A2←(S2+A1×S1)÷¯2
[10]    A3←(S3+(A2×S1)+(A1×S2))÷¯3
[11]    A4←(S4+(A3×S1)+(A2×S2)+(A1×S3))÷¯4
[12]    RES←1,A1,A2,A3,A4
```

To test the function:

```
      A←4 4⍴1 ¯4 ¯1 ¯4 2 0 5 ¯4 ¯1 1 ¯2 3 ¯1 4 ¯1 6
      A
 1 ¯4 ¯1 ¯4
 2  0  5 ¯4
¯1  1 ¯2  3
¯1  4 ¯1  6
      CHAR4 A
1 ¯5 9 ¯7 2
```

i.e. the solution for this matrix is x⁴ - 5x³ + 9x² - 7x + 2 = 0.

## Romberg’s Integration

The second function is a version of Romberg’s method for numerical integration. It is slower than Simpson’s Rule. I hope someone will improve it — it is a start anyway!

```
[0]     ROMB X;A;B;C;J;M;L;S;T;I;I2;I3;A1;B1;W;N;K;⎕IO
[1]    ⍝Romberg integration, function in ∆FN
[2]    ⍝X is vector of lower, upper limits and N
[3]     ⎕IO←0 ⋄ A←X[0] ⋄ B←X[1] ⋄ N←X[2]
[4]     A1←∆FN A
[5]     B1←∆FN B
[6]     I←20⍴0
[7]     C←B-A ⋄ L←1 ⋄ M←K←0
[8]     J←(A1+B1)÷2
[9]     I[0]←C×J
[10]   L1:L←2×L ⋄ M←M+1 ⋄ W←1
[11]   L3:J←J+∆FN A+W×C÷L
[12]    →((L-1)≥W←W+2)/L3
[13]   I2←J×C÷L ⋄ S←0 ⋄ T←4
[14]   L2:⎕←I3←((I2×T)-I[S])÷T-1
[15]    →(N=K←K+1)/PRINT
[16]    I[S]←I2 ⋄ I2←I3 ⋄ S←S+1 ⋄ T←T×4
[17]    →(S<M)/L2
[18]    I[S]←I2
[19]    →L1
[20]   PRINT:'Integral is ',⍕I3
```

Running the function, to integrate the square root of x² + 3x - 4, with N=10, (the exact value is 1.577186) gives:

```
      ROMB 1 2 10
 1.513789887
 1.554609508
 1.557330816
 1.569181806
 1.570153293
 1.570356824
 1.574352706
 1.574697433
 1.574769562
 1.574786867
Integral is 1.574786867
```

Repeating the process with N=50 and N=100, gives 1.577181348 and 1.577185956 respectively (but be warned - it takes a long time!)
