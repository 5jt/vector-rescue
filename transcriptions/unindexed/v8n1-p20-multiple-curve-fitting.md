---
title: Multiple Curve Fitting
authors:
- C.E. Williams
volume: '8'
issue: '1'
page: '20'
unindexed: true
transcribed: 'from page images of VOL.8-NO.1-JULY-1991.pdf, pages 22 and 25 (printed 20–21; within The Education Vector’s Letters, after Manfred Storn’s; two unnumbered inserted pages, an I-APL Ltd order form and I-APL News for Education Vector 8.1, fall between them); Claude, 2026-10-11'
review: draft
tags:
- mathematics and statistics
- education
queries:
- "Untitled in print: a letter, “From: C.E. Williams”, under Letters in The Education Vector, with an editor’s comment; the title is ours."
- "The listing uses ⍞ (quote-quad) in [6], ⍟ (logarithm) in [16], [23] and [30], and ⍕ (format)."
- "Kept as printed: [18] `'y=aexp(bx)` lacks its closing quote; [41] has one more closing parenthesis than opening ones."
---

*From: C.E. Williams*
{ .byline }

I enclose a function *MULCURFIT* which allows Multiple Curve Fitting, the fit of x,y data pairs to the four common equations:-

```
straight line      y=a+bx            (no restrictions)
exponential curve  y=aexp(bx)        (y positive)
log curve          y=a+bln(x)        (x positive)
power curve        y=aexp(bln(x))    (x and y positive)
```

The data is entered only once and retained, being transformed when required. The results are given with the correlation coefficient. This enables the best fit to be readily seen. There are some restrictions since logs are used (see the comments in brackets above). A test set of data pairs is included, together with the results on I-APL on BBC2. I hope it may be of some use to someone out there!

```apl
     ∇ MULCURFIT;A;B;M;MA;MB;N;SX;SY;R;Q;Z
[1]    'INPUT X AND Y VECTORS'
[2]    X←⎕
[3]    Y←⎕
[4]    N←⍴X
[5]   L:'INPUT REQUIRED FORM LIN(I),EXP(P),LOG(G),POW(W),END(E)'
[6]    →((1↑⍞)='IPGWE')/I,P,G,W,E
[7]    'INVALID CHOICE'
[8]    →L
[9]   I:A←X ⋄ B←Y ⋄ Z←1
[10]   →PRO
[11]   'y=a+bx'
[12]   'a=',⍕Q
[13]   'b=',⍕M
[14]   'r=',⍕R
[15]   →L
[16]  P:A←X ⋄ B←⍟Y ⋄ Z←2
[17]   →PRO
[18]   'y=aexp(bx)
[19]   'a=',⍕*Q
[20]   'b=',⍕M
[21]   'r=',⍕R
[22]   →L
[23]  G:A←⍟X ⋄ B←Y ⋄ Z←3
[24]   →PRO
[25]   'y=a+bln(x)'
[26]   'a=',⍕Q
[27]   'b=',⍕M
[28]   'r=',⍕R
[29]   →L
[30]  W:A←⍟X ⋄ B←⍟Y ⋄ Z←4
[31]   →PRO
[32]   'y=aexp(bln(x))'
[33]   'a=',⍕*Q
[34]   'b=',⍕M
[35]   'r=',⍕R
[36]    →L
[37]  PRO: MA←(+/A)÷N
[38]   MB←(+/B)÷N
[39]   SX←((+/(A-MA)*2)÷(N-1))*.5
[40]   SY←((+/(B-MB)*2)÷(N-1))*.5
[41]   M←((B+.×A)÷N)-(MA×MB))÷((SX*2)×(1-÷N))
[42]   Q←MB-M×MA
[43]   R←(M×SX)÷SY
[44]   →(Z=1)/11
[45]   →(Z=2)/18
[46]   →(Z=3)/25
[47]   →(Z=4)/32
[48]  E:→0
     ∇
```

```apl
      X←10 20 40
      Y←.1007 .1790 .2960

LINEAR:  a=.0064157    b=.042199    r=.99709
EXP:     a=.078308     b=.034398    r=.97393
LOG:     a=-.230136    b=.140879    r=.99351
POWER:   a=.01700      b=.777766    r=.99925
```

(Editor’s comment: I hope I have typed the program correctly together with one or two minor cosmetic changes. It is good to see this sort of program being produced and indeed used.)
