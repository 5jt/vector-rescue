---
title: Production Manager’s Observation
authors: []
volume: '12'
issue: '1'
page: '106'
unindexed: true
transcribed: 'from page images of VOL.12-NO.1-JULY-1995.pdf, page 108 (printed 106; follows art10004440, The Complete Elliptic Integrals and APL, as a note on it); Claude, 2026-10-11'
review: draft
tags:
- mathematics and statistics
- implementations
queries:
- "A note by Vector’s production manager on Joseph De Kerf’s “The Complete Elliptic Integrals and APL” (art10004440), whose sample evaluations it reruns in Dyalog/W. No name is printed; the entry has no authors."
- "In the printed results some trailing digits of the second column are underlined, apparently to mark where they differ from the article’s results: first example, the last digit for 0.6 (3) and 0.7 (4), and the last two for 0.8 (30); second example, the last two for 0.3 (50), and the last digit for 0.5 (4), 0.7 (5) and 0.9 (6). Code blocks cannot show the underlining."
---

When run in Dyalog/W, the sample evaluations produce very slightly different results! Both are run in the same comparison tolerance!

First Example …

```apl
      ⎕CT←1E¯15
      R←CEI1¨ P←0,0.1×⍳9
      3 1 15 10 20 15⍕P,R,[1.5] R
0.0   1.5707963268   1.570796326794897
0.1   1.5747455615   1.574745561517356
0.2   1.5868678475   1.586867847454166
0.3   1.6080486199   1.608048619930513
0.4   1.6399998659   1.639999865864511
0.5   1.6857503548   1.685750354812596
0.6   1.7507538029   1.750753802915753
0.7   1.8456939984   1.845693998374724
0.8   1.9953027777   1.995302777664730
0.9   2.2805491384   2.280549138422770
```

Second Example …

```apl
      ⎕CT←1E¯15
      R←CEI2¨ P←0,.1×⍳10
      3 1 15 10 20 15⍕P,R,[1.5] R
0.0   1.5707963268   1.570796326794897
0.1   1.5668619420   1.566861942021668
0.2   1.5549685462   1.554968546242529
0.3   1.5348334649   1.534833464923250
0.4   1.5059416124   1.505941612360040
0.5   1.4674622093   1.467462209339424
0.6   1.4180833944   1.418083394448724
0.7   1.3556611356   1.355661135571955
0.8   1.2763499432   1.276349943169906
0.9   1.1716970528   1.171697052781616
1.0   1.0000000000   1.000000000000000
```

Perhaps someone with *Mathematica* could say which is correct!!
