---
title: Technical Correspondence (Bowman)
authors:
- Dick Bowman
volume: '3'
issue: '1'
page: '99'
unindexed: true
transcribed: 'from page images of VOL.3-NO.1-JULY-1986.pdf, pages 101–102 (printed 99–100; Surely There Must Be A Better Way follows on p.101); Claude, 2026-10-05'
review: draft
tags:
- mathematics and statistics
- programming techniques
queries:
- "The three results are printed in a dot-matrix face with right-aligned system comments. Checked against a numerically careful least-squares fit (NumPy polyfit): the cubic’s coefficients are about ¯61569508.6, 92648.743, ¯46.4719853, 0.00777000062. The APL*PLUS line is close; the VSAPL line agrees on the last three but its first is printed ¯6159617.48, about a tenth of the true value: presumably ¯61596174.8 with a digit lost (or the decimal point misplaced). Transcribed as printed."
---

## From Dick Bowman

Sir:

Incorporated into a graphics package there’s the following little snippet of code associated with curve-fitting:

```apl
COEFF←Y⌹X∘.*0,⍳CURVEORDER
```

There are a few twiddly bits around it to ensure that it doesn’t fall over too frequently because the user has total control of data values Y and X and of the order of the fitted curve – in the worst case the embedding function reverts to joining the points with a set of straight lines.

Curious as it may sound this had been working fine for some years in a VSAPL/VSPC environment and also in an APL\*PLUS/PC incarnation; however implementation in APL2/TSO resulted in a series of phone calls along the approximate lines of “’ere, why are my curves all jaggy?”. So with a sample set of data to hand we take a look at what goes on in the three incarnations:

```apl
Y←37 36 39 38 41 39 43 38 43 35 42
X←1984+⍳11
```

Strange as it may sound, our user wanted to fit a third-order curve to this, so let’s look at

```apl
      Y⌹X∘.*0 1 2 3

¯6159617.48 92648.90706 ¯46.47206775 0.007770014433    ⍝ VSAPL

¯61569559.53 92648.8197 ¯46.47202385 7.77000708E¯3     ⍝ APL*PLUS PC

DOMAIN ERROR                                           ⍝ APL2
```

A fascinating finding; further investigation shows that there is a reasonable agreement between the three cases for orders less than three, and when we go to higher orders both VSAPL and APL\*PLUS/PC refuse at six, agree with one another moderately well at four, but diverge wildly at five. Which gives us a potentially very interesting situation that with the same data and the same code within the functions, we can end up with three totally different graphs depending on which system we use to draw them.

Let’s come to some conclusions:

a)
:   Given sufficiently perverse data there’s something different about the domino algorithm in APL2;

b)
:   Letting end-users choose the order of a fitted curve is a nice idea in theory and essential sometimes, but quite often all they want is for it to look nice and smooth;

c)
:   Sometimes a little thought about algorithmic subtlety can repay itself in avoidance of nasty surprises.

Yours sincerely,

Dick Bowman,  
C.E.G.B.,  
85 Park Street,  
London, SE1.

*(Editor: The draft ISO APL standard specifies that the algorithm to be used for matrix-divide is implementation-defined. Although no sensible implementer would use an algorithm other than matrix division, it does allow implementers to use different variations of the general technique. This means that different APLs can produce different results and yet still conform to the standard. An acceptable algorithm for matrix division can be found in “Domino – An APL Primitive Function – Its Implementation and Applications”, from Quote-Quad Vol.3, No.4, February 1972.)*
