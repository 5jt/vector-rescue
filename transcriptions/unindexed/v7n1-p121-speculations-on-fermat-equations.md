---
title: Speculations on Fermat Equations ...
authors:
- Anne D Wilson
volume: '7'
issue: '1'
page: '121'
unindexed: true
transcribed: 'from page images of VOL.7-NO.1-JULY-1990.pdf, pages 123–125 (printed 121–123; within Technical Correspondence, after unindexed/v7n1-p120-surely-there-must-be-a-better-way.md); Claude, 2026-10-11'
review: draft
tags:
- mathematics and statistics
- programming techniques
queries:
- "The last letter in Technical Correspondence, From: Anne D Wilson, 12 June 1990, signed “Anne D Wilson, Rowntree, York”. It follows up Zdenek V Jizba’s article on Fermat type equations. APL Standards Update follows on p.124."
- "The mathematics is printed in running text with superscripts; set here as TeX. The two tables (the derivation of z² and the examples from p and q) and the HCF trace are printed in a typewriter face and are set as code blocks. “pteo” is the writer’s abbreviation for “prime to each other”, which is printed in bold where first used."
- "Checked in Dyalog APL: `31 HCF 12` gives 1."
- "Kept as printed: “led to me to”; “4k + 9 = 4n + 1” in (2)(ii); (4)’s “4(2m - k - 1).k” beside “(2m - k + 1)”; “Some example generated”; “similiar”; “z mod 4 = 0.5(1 + 1)”; the example row “998 6 1497 124496 124505” (998 is even, and 998×6 is not 1497); “K = 8, 9 , 18, 25 .....”."
---

*From: Anne D Wilson, 12 June 1990*
{ .byline }

Zdenek V Jizba’s article on Fermat type equations led to me to some interesting thoughts on solutions to \(x^2 + y^2 = z^2\) where \(x,y,z\) are integers and cannot be reduced to another equation by division; e.g. \(6^2 + 8^2 = 10^2\) reduces to \(3^2 + 4^2 = 5^2\).

The following discussion uses the concept of modulo algebra and numbers **prime to each other.** Modulo algebra deals only with the remainders, which can be generated using the APL primitive. If two numbers are prime to each other they have no common factor other than 1. Thus 4 and 9 are pteo, but 12 and 21 have a common factor of 3. The following recursive function returns the highest common factor (HCF) of 2 numbers. Where numbers are pteo the HCF equals 1.

```apl
      ∇ R←A HCF B;C
[1]    ⍎'R←B',(0<C←B|A)/' HCF C'
      ∇
```

It uses a chain of quotients and remainders to find the HCF. The intermediate results for 31 and 12 are:

```
by calculation                 using the above function
HCF of 31 and 12 is 1, ie they are pteo.
31 = 2 x 12 + 7                           31 HCF 12
12 = 1 x 7 + 5                            12 HCF 7
7 = 1 x 5 + 2                              7 HCF 5
5 = 2 x 2 + 1                              5 HCF 2
2 = 2 x 1                                  2 HCF 1
```

(1) In the equation  
\(x^2 + y^2 = z^2\)  \(x\) \(y\) \(z\) are pteo.  
Proof:- If \(x\), \(y\) have a common factor \(k\)  
\(k^2a^2 + k^2b^2 = k^2(a^2 + b^2)\)  
and \(k\) is a factor of \(z\);  
therefore the equation can be reduced by division by \(k\).

(2) In the equation  
\(x^2 + y^2 = z^2\)  \(x\) and \(z\) are odd and \(y\) is even, or \(y\) and \(z\) are odd and \(x\) is even.  
Proof:-  
(i) If 2 of the variables are even they have a common factor of 2, and the equation can be reduced by (1).  
(ii) Odd numbers are either \(4m + 1\) or \(4m + 3\)  
which when squared give \(4n + 1\) or \(4k + 9 = 4n + 1\)  
hence the square of any odd number is \(4n + 1\)  
Even numbers are \(2m\) and the square of an even number is \(4n\).

Considering all possible combinations:

```
           | x = 4m+1   |   4m+3   |   2n    |
           | x² = 4r+1  |   4r+1   |   4r    |
---------------------------------------------------      Table showing
y = 4n+1   |    4s+2    |   4s+2   |  4s+1   |          derivation of z²
y² = 4r+1  |     X      |    X     |  z odd  |          where x² + y² = z²
---------------------------------------------------
y = 4n+3   |    4s+2    |   4s+2   |  4s+1   |
y² = 4r+1  |     X      |    X     |  z odd  |
---------------------------------------------------
y = 2n     |    4s+1    |   4s+1   |  4s     |
y² = 4r    |    z odd   |   z odd  |  X      |
---------------------------------------------------
```

> As \(x\) \(y\) \(z\) are not all even, and the square of an odd number is \(4s + 1\) the only valid combinations are:
>
> &emsp;&emsp;\(x\) even, \(y\) and \(z\) odd  
> or&emsp;\(y\) even, \(x\) and \(z\) odd

With no loss of generality we can take the case where \(x\) is odd and consider the equation in the form: \(x^2 = z^2 - y^2\)

(3) If \(p\) \(q\) are odd numbers pteo \((p^2 + q^2) \bmod 4 = 2\)  
Proof:-  
\(p\) and \(q\) are odd therefore \((p^2 + q^2) \bmod 4 = 1 + 1 = 2\)

(4) If \(p\) \(q\) are odd numbers pteo \((p^2 - q^2) \bmod 8 = 0\)  
Proof:-  
\(p\) and \(q\) are odd therefore  
\(p = 2m + 1\)  
\(q = 2n + 1 = 2(m - k) + 1\)  
\(p^2 - q^2 = (p + q)(p - q) = 4(2m - k - 1).k\)  
Either \(k\) is odd when \((2m - k + 1)\) is even or \(k\) is even when \((2m - k + 1)\) is odd and therefore another factor of 2 can be extracted.  
Hence \((p^2 - q^2) \bmod 8 = 0\)

(5) If \(a\) \(b\) are odd numbers pteo  
and&emsp;\(z = 0.5(a + b)\)  
&emsp;&emsp;&emsp;\(y = 0.5(a - b)\)  
then if there exists \(x\) such that \(z^2 - y^2 = x^2\) \(a\) and \(b\) are squares.  
Proof:-  
\(z^2 - y^2 = (0.5(a + b))^2 - (0.5(a - b))^2 = ab\)  
Hence \(ab = x^2\) and \(a\) \(b\) pteo otherwise \(z\) and \(y\) have a common factor; therefore \(a\) and \(b\) are perfect squares.

Indeed any pair of odd numbers \(p\) \(q\) pteo will generate a solution to the equation. Thus it is only necessary to check that the parameters \(p\) \(q\) are pteo to produce triplets of Pythagorean numbers.

\begin{alignat*}{1}
x &= pq\\
y &= 0.5(p^2 - q^2)\\
z &= 0.5(p^2 + q^2)
\end{alignat*}

(6) We can deduce some characteristics of these triplets:-  
(i) \(z \bmod 4 = 1\) i.e. \(z\) has the form \((4m + 1)\)  
Proof:-  
\(z = 0.5(p^2 + q^2)\);  \(p\) \(q\) are odd therefore \(z \bmod 4 = 0.5(1 + 1) = 1\)

(ii) \(y \bmod 4 = 0\)  i.e. \(y\) is a multiple of 4  
Proof:-  
\(y = 0.5(p^2 - q^2) = 0.5(8m) = 4m\) therefore \(y \bmod 4 = 0\)

(iii) \(z - y = q^2\) which is a perfect square.

(iv) \(z - x = 0.5(p^2 + q^2) - pq = 0.5(p - q)^2\)  
and as \(p\) and \(q\) are both odd it equals \(2 \times\) a perfect square.

Some example generated from \(p\) and \(q\) are ...

```
   p    q   x=p.q    y=0.5(p² - q²)   z=0.5(p² + q²)
   3    1       3                4                5
  11    5      55               48               73
 101   67    6767             2856             7345
 101   99    9999              200            10001
 998    6    1497           124496           124505
1933  499  964567          1743744          1992745
```

Although the above discussion depends on the choice of \(x\) as an odd number similiar calculations can be performed when \(x\) is an even number. In this case the parameters \(r\) \(s\) are defined and deduced as:

\begin{alignat*}{1}
y &= (r^2 - s^2)\\
z &= (r^2 + s^2)\\
x &= 2rs = \sqrt{2r}\,.\,\sqrt{2s}
\end{alignat*}

However this merely generates the same triplets, but with \(x\) and \(y\) interchanged.

For the triplets generated by Jizba’s function `R←K  PFERMAT  W`

> where&emsp;\(K = z - x\) and \(W = y\)  
> or&emsp;&emsp;&ensp;\(K = z - y\) and \(W = x\)

\(K\) must be either (the square of an odd number) or (\(2 \times\) square) see 6(iii) and 6(iv). This explains why \(K = 3\) and \(K = 4\) do not yield triplets. \(K = 8, 9 , 18, 25\) ..... would yield triplets.

Anne D Wilson  
Rowntree, York
