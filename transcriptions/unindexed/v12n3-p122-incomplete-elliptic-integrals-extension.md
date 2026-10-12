---
title: 'The Incomplete Elliptic Integrals and APL - an Extension'
authors:
- Joseph De Kerf
volume: '12'
issue: '3'
page: '122'
unindexed: true
transcribed: 'from page images of VOL.12-NO.3-JANUARY-1996.pdf, pages 124–126 (printed 122–124); Claude, 2026-10-12'
review: draft
tags:
- mathematics and statistics
- programming techniques
queries:
- "Printed heading “The Incomplete Elliptic Integrals and APL: an Extension”. The piece ends on printed 124; printed 125 is the Technical Section’s title page and printed 126 a MicroAPL advertisement (“APL for the Apple Macintosh”), not transcribed."
- "The author’s postal address at the end (a private address in Duffel, Belgium) is omitted under the project rule for individuals’ contact details."
- "The article writes π as a capital Pi (Π) throughout; kept as \\Pi. The function listings are given as printed, with line numbers in brackets; the first-line displays “∇IEI1[⎕]∇” are kept."
---

*Joseph De Kerf*
{ .byline }

Elliptic integrals of the first kind \(K(\phi;p)\) and of the second kind \(E(\phi;p)\) may be defined as:

\begin{equation*}
K(\phi;p)=\int_0^{\phi}\frac{d\theta}{\sqrt{1-p^2\sin^2\theta}}
\end{equation*}

\begin{equation*}
E(\phi;p)=\int_0^{\phi}\sqrt{1-p^2\sin^2\theta}\;\;d\theta
\end{equation*}

with \(p^2\le 1\) or \(-1\le p\le 1\).

For \(\phi=\Pi/2\) those integrals are defined as the complete elliptic integrals of the first kind \(K(p)=K(\Pi/2;p)\) and of the second kind \(E(p)=E(\Pi/2;p)\). For \(0\le\phi<\Pi/2\) the elliptic integrals of the first kind \(K(\phi;p)\) and of the second kind \(E(\phi;p)\) are called the incomplete elliptic integrals, the complete elliptic integrals being their boundary values. It should be noted that:

\(K(-\phi;p)=-K(\phi;p)\) and \(E(-\phi;p)=-E(\phi;p)\).

With all this in mind, APL user-defined functions for calculating those elliptic integrals for \(-\Pi/2\le\phi\le\Pi/2\), based on the common mean algorithm [1], were given in [2]: IEI1 for calculating the elliptic integrals of the first kind \(K(\phi;p)\) and IEI2 for the elliptic integrals of the second kind \(E(\phi;p)\) (*cf.* Figure 1.)

```apl
      ∇IEI1[⎕]∇
     ∇R←F IEI1 P;I;A;B
[1]   →((1≠|P)∨(○÷2)=|F)/LAB1
[2]   →0,R←⍟3○0.5×F+○0.5
[3]  LAB1:R←(2+I←¯1),(1-P*2)*0.5
[4]  LAB2:A←(-/R)×1○F×2*1+I←I+1
[5]   B←2×+/R×(2 1○F×2*I)*2
[6]   F←F-(¯3○A÷B)÷2*I+1
[7]   →(≠/R←(0.5×+/R),(×/R)*0.5)/LAB2
[8]   R←F÷0.5×+/R
     ∇

      ∇IEI2[⎕]∇
     ∇R←F IEI2 P;I;S;T;A;B
[1]   →(1=|P)/0,R←1○F
[2]   R←(1+S←T←1+I←¯1),(1-P*2)*0.5
[3]  LAB:A←(-/R)×1○F×2*1+I←I+1
[4]   B←2×+/R×(2 1○F×2*I)*2
[5]   F←F-(¯3○A÷B)÷2*I+1
[6]   S←S+(-/R*2)×2*I
[7]   T←T+(-/R)×1○F×2*I+1
[8]   →(≠/R←(0.5×+/R),(×/R)*0.5)/LAB
[9]   R←(T÷2)+(2-S)×F÷+/R
     ∇
```

**Figure 1**

In some applications, however, we need the elliptic integrals of the first kind \(K(\phi;p)\) and of the second kind \(E(\phi;p)\) for values of the argument \(|\phi|>\Pi/2\). For \(p\ne\pm1\) and \(|\phi|>\Pi/2\) the user-defined functions shown still give the correct results, but for \(p=\pm1\) and \(|\phi|>\Pi/2\) they may fail:

For \(p=\pm1\) and \(|\phi|\ge\Pi/2\), the elliptic integral of the first kind \(K(\phi;p)\) is always infinite (\(\infty\)), while the user-defined function IEI1 eventually returns a value instead of a domain error report, for example when \(3\Pi/2\le\phi<5\Pi/2\).

For \(p=\pm1\), the user-defined function IEI2 returns \(\sin\phi\), but this is only correct for \(-\Pi/2\le\phi\le\Pi/2\). Indeed:

\begin{equation*}
\begin{array}{lll}
\text{for} & \Pi/2\le\phi\le3\Pi/2 & E(\phi;p)=2+\sin(\phi-\Pi)\\
 & 3\Pi/2\le\phi\le5\Pi/2 & \qquad\;\;=4+\sin(\phi-2\Pi)\\
 & 5\Pi/2\le\phi\le7\Pi/2 & \qquad\;\;=6+\sin(\phi-3\Pi)\\
 & \ldots\ldots\ldots & \qquad\;\;\ldots\ldots\ldots
\end{array}
\end{equation*}

In general: \(E(\phi;p)=2n+\sin(\phi-n\Pi)\) where \(n\) is the result of rounding off to an integer the quotient \(\phi/\Pi\). It should be noted that this procedure is also valid for \(\phi\le-\Pi/2\).

APL user-defined functions, IEI1 for the elliptic integrals of the first kind \(K(\phi;p)\) and IEI2 for the elliptic integrals of the second kind \(E(\phi;p)\), valid for every value of the argument \(\phi\) are given in Figure 2.

```apl
      ∇IEI1[⎕]∇
     ∇R←F IEI1 P;I;A;B
[1]   →((1≠|P)∨(○÷2)≤|F)/LAB1
[2]   →0,R←⍟3○0.5×F+○0.5
[3]  LAB1:R←(2+I←¯1),÷÷(1-P*2)*0.5
[4]  LAB2:A←(-/R)×1○F×2*1+I←I+1
[5]   B←2×+/R×(2 1○F×2*I)*2
[6]   F←F-(¯3○A÷B)÷2*I+1
[7]   →(≠/R←(0.5×+/R),(×/R)*0.5)/LAB2
[8]   R←F÷0.5×+/R
     ∇

      ∇IEI2[⎕]∇
     ∇R←F IEI2 P;N;I;S;T;A;B
[1]   →(1=|P)/0,R←(2×N)+1○F-○N←⌊0.5+F÷○1
[2]   R←(1+S←T←1+I←¯1),(1-P*2)*0.5
[3]  LAB:A←(-/R)×1○F×2*1+I←I+1
[4]   B←2×+/R×(2 1○F×2*I)*2
[5]   F←F-(¯3○A÷B)÷2*I+1
[6]   S←S+(-/R*2)×2*I
[7]   T←T+(-/R)×1○F×2*I+1
[8]   →(≠/R←(0.5×+/R),(×/R)*0.5)/LAB
[9]   R←(T÷2)+(2-S)×F÷+/R
     ∇
```

**Figure 2**

For \(p\ne\pm1\) and/or \(|\phi|\ge\Pi/2\), the flow of user-defined function IEI1 is branched from line 1 to line 3. However, in line 3 the expression `(1-P*2)*0.5` has been substituted by the equivalent expression `÷÷(1-P*2)*0.5`. This means that for \(p=\pm1\) and \(|\phi|\ge\Pi/2\), a domain error report is returned.

In line 1 of the user-defined function IEI2, the result \(R\) is *a priori* set to \(2n+\sin(\phi-n\Pi)\), with \(n\) assigned the value as defined above. If \(p=\pm1\), flow of execution returns to the invoking expression and \(2n+\sin(\phi-n\Pi)\) is returned. If \(p\ne\pm1\), flow of execution continues in line 2 and the *a priori* set result is replaced by its actual value.

## References

[1] J. De Kerf, *The Common Mean and APL*, Vector 11.3, pp 21–23, 1995

[2] J. De Kerf, *The Incomplete Elliptic Integrals and APL*, Vector 12.2, pp 95–100, 1995

> Joseph De Kerf<br>
> [address omitted]
