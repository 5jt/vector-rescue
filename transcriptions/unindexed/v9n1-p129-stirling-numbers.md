---
title: Stirling Numbers
authors:
- David Appleton
volume: '9'
issue: '1'
page: '129'
unindexed: true
transcribed: 'from page images of VOL.9-NO.1-JULY-1992.pdf, page 131 (printed 129; follows art10009980, in Technical Correspondence); Claude, 2026-10-11'
review: draft
tags:
- mathematics and statistics
- programming techniques
queries:
- "An untitled letter in Technical Correspondence, From: David Appleton, 10 March 1992, replying to Norman Thomson and Ken Iverson on his article on Stirling numbers; titled here from its subject. It follows Norman Thomson’s letter (art10009980) and fills p.129."
- "The expression that calculates t·σⁿₜ₋₁/σⁿₜ is set in TeX. The APL version of Iverson’s method was run in Dyalog APL (⎕IO←0, N←5) to check the transcription: S1 and S2 give the two kinds of Stirling numbers."
---

*From: David Appleton, 10 March 1992*
{ .byline }

I am delighted that Norman Thomson and Ken Iverson were interested enough to comment on my article on Stirling numbers. As a result, I have learned enough J to understand and execute the wonderfully concise and interesting expression in the latter’s letter, thanks to my colleague Chris Brunsdon. Unfortunately, I ran out of workspace on my micro long before I could execute it with a sufficiently high parameter value (60) to compare the results with those of the programs I presented.

It might help anyone interested in this correspondence if I gave an APL version of the method (index origin is zero as in J).

```apl
K←⍳N
D←K∘.-K
S←D≥0
F←⍉(⍴D)⍴!K
A←K∘.*K
B←(F×S)÷!D×S
S1←B⌹A
S2←A⌹B
```

The relationship between the two kinds of Stirling number is certainly made very clear, though as a practical method of calculation it is not as useful as Norman’s recursive function.

Perhaps I should come clean! I wrote the original article because the expression `⍎1↓(7×P)⍴'×+\(⍳N)'` amused me, and I thought it might amuse others. I am sure that J can produce the same sort of expression without using character vectors, but I am afraid I cannot yet construct it. However, I also had a real problem involving Stirling numbers, or, as it turned out, the ratios of Stirling numbers, and I needed a good algorithm. Recursion seems to fit the bill best, and my eventual function to calculate \(t\sigma^{n}_{t-1}/\sigma^{n}_{t}\) was (with index origin back to 1):

```apl
    ∇Z←STIRRAT T;U
[1] →(T=1)/0,Z←1
[2] Z←(T×(¯1⌽U)÷T-1+(⍳T-1)×U←¯1⌽U←STIRRAT T-1),0
    ∇
```

If this looks very like Norman’s function, that is because I modelled the final version on it!
