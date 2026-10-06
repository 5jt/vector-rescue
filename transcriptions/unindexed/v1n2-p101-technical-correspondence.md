---
title: Technical Correspondence
authors:
- Norman Thomson
- D.J. Horton
volume: '1'
issue: '2'
page: '101'
unindexed: true
transcribed: 'from page images of VOL.1-NO.2-OCTOBER-1984.pdf, pages 103–108 (printed 101–106; follows the unindexed Technical Editorial); Claude, 2026-10-03'
review: draft
tags:
- programming techniques
queries:
- "Three letters with editor’s replies (in italics, as printed). Thomson’s first letter answers art10003490; his second, art10000550."
- "The APL in the letters is typeset in a monospaced APL face. Glyph readings: `⌹` (printed as a boxed glyph); `¨` (each) in EXPON; `⊂` (enclose); `⌽` in DIFF. The L1 column of both tables has marks above and below the 1s; read as alternating `1` and `¯1`, which agrees with DIFF: L[1]=¯1 gives the negative (¯1↓0,R) differences, L[1]=1 the positive."
- "Checks: DIFF with `¯1 0` and `<` gives `A<¯1↓0,A`, the first algorithm, as stated; `⌹2 2⍴1 1 0 0J1` is `2 2⍴1 0J1 0 0J¯1` (the inverse of [[1,1],[0,i]] is [[1,i],[0,−i]]), and [[1+i,2],[1,1−i]] is singular, as stated."
- "Slips transcribed as printed: “In face VS APL allows”, “awsome”, “progamming”, “gobbledegook”, “heterogenous”, “the character ‘1’” (for ‘P’)."
---

## From Mr. Norman Thomson, 26th July 1984

Sir: Following Professor Alan Hawkes’ article on “Complex Numbers in APL” in the first issue of “VECTOR”, and at the risk of appearing to gloat over those of your readers who are constrained to APL1, I cannot resist pointing out the merits of complex numbers and other features of APL2. Here is the article paraphrased in APL2, and thereby reduced to a single page.

Some assignments:-

| | |
|---|---|
| scalar: | `A←7J8` |
| one element vector: | `B←1⍴A` |
| vector: | `C←1J5 2J6 3J7 4J8` |
| or | `C←(⍳4)+0J1×4+⍳4` |
| matrix: | `D←3 4⍴(⍳12)+0J1×12+⍳12` |

Real and imaginary parts of D are given by using 9 and 11 as the left argument to the Circle function; 10 gives the same result as Modulus. Plus, Minus, Times, Divide, Power, Log and Domino are as for reals, e.g.

```
⌹2 2⍴1 1 0 0J1 ←→ 2 2⍴1 0J1 0 0J¯1
```

and

```
⌹2 2⍴1J1 2 1 1J¯1
```

is DOMAIN ERROR.

To calculate e<sup>A</sup> where A is a matrix, define first

```
EXP: L+.×/L⍴⊂R
```

which raises matrix R to the power L,

```
NORM: ⌈/+/|R
```

to define the 1-norm, which is applicable both to the real and complex case, and

```
M: 1+⌈2⍟NORM R
```

so that M is the smallest non-negative integer satisfying

```
||A÷2ᴹ|| = ||A||÷2ᴹ < 1/2
```

The function

```
I: T∘.=T←⍳↑⍴R
```

produces the identity matrix. The exponential function for matrix R is then

```
EXPON: T EXP(I R)+↑+/((⍳13)EXP¨⊂R÷T←2*M R)÷¨!⍳13
```

To paraphrase Professor Hawkes’ penultimate paragraph —

> “Oh well, it’s better than doing it in APL!”

Yours sincerely,

Norman Thomson

IBM United Kingdom Laboratories Limited

Hursley Park

Winchester, Hampshire.

## From Mr. Norman Thomson, 7th August 1984

Sir: I should like to offer some comments on the article “APL and Partitioned Data” by Jonathan Barman in the first issue of “VECTOR”.

In his conclusion, he states rightly that generalised arrays will do much to obviate the need for partition vectors. I believe, however, that there will still be uses for such vectors even when extended APL is available. The appendix (pp. 138—141) suggests naturally a demonstration of another invaluable feature of extended APLs, namely user defined operators. To illustrate, all the 16 little algorithms given can be subsumed in the single user-defined monadic operator:

```
DIFF: R LO L[1]↓(0⌈L[1])⌽L[2],R
```

where R and L stand for right and left arguments and LO for left operand.

For example, the first algorithm

```
A<¯1↓0,A
```

becomes

```
¯1 0<DIFF A
```

I find it helpful to regard the 1’s in a partition vector as markers for elements in R, and if the elements of the left argument are referred to as L1 and L2, then the roles of various argument/operand combinations can be summarised as follows.—

| L1 | L2 | LO | Marks:— |
|---|---|---|---|
| `1` | `1` | `<` | Last zeros |
| `¯1` | `1` | `<` | First zeros |
| `1` | `0` | `>` | Last ones |
| `¯1` | `0` | `>` | First ones |
| `1` | `~¯1↑R` | `≠` | Last in each run |
| `¯1` | `~1↑R` | `≠` | First in each run |

In each case complementing L2 has the effect of ignoring the trailing or leading run.

Also changing the function LO to its complement, i.e.

```
< → ≥
> → ≤
≠ → =
```

obtains the complement of the result.

Further, R need not be boolean. For numeric R,

| | |
|---|---|
| `¯1 1<DIFF R` | marks the starts of monotonic non-strictly increasing subsequences. |
| `¯1 0>DIFF R` | marks the starts of monotonic strictly decreasing subsequences. |
| `¯1 1≠DIFF R` | marks non-repeating elements. |

For the logical functions R must be boolean and we have:

| L1 | L2 | LO | Extends runs of:— |
|---|---|---|---|
| `1` | `1` | `∨` | 1’s on the left (including trailing 0) |
| `¯1` | `1` | `∨` | 1’s on the right (including leading 0) |
| `1` | `0` | `∧` | 0’s on the left (including trailing 1) |
| `¯1` | `0` | `∧` | 0’s on the right (including leading 1) |

“Extend” means “increase run length by one by overwriting”, and extending say, 1’s to the left is equivalent to reducing runs of 0’s on the right.

In each case complementing L2 excludes the leading/trailing 0/1.

Yours sincerely,

Norman Thomson

IBM United Kingdom Laboratories Limited

Hursley Park

Winchester, Hampshire.

*Editor: APL2 and STSC’s Nested Array Research System allow a numeric left argument to the derived functions produced by the reduction and scan operators. The left argument is a scalar which defines the grouping over which the derived function is to take place. The positive Not Equals first difference is:—*

```
2≠\A
```

*where the 2 specifies that a Not Equals reduction of the first element, the first two elements, the second and third elements, and so on up to the last pair of elements, is to be performed. The negative Less Than first difference is:—*

```
¯2<\A
```

*where the negative-2 specifies that the reduction is applied to reversals of pairs of elements in the right argument.*

*These are equivalent to the difference operator, but give more interesting results when the left argument is greater than two.*

## From Mr. D.J. Horton

Sir: I have greatly enjoyed reading the first issue of VECTOR and am enclosing my entry to your competition.

There is much talk about all the enhancements to APL which are in the offing, and as a convert to the language I welcome any improvements. I feel, however, that as much effort should be put into making the language more “user-friendly”. The identification and detection of errors is a particular area where I feel some useful work could be put in. For example, there are several quite distinct reasons for the message DOMAIN ERROR, (a splendid example of jargon), so why cannot the standard for the interpreter lay down greater intelligibility. Again, it is incomprehensible to me why the only division by zero which the interpreter handles is when the numerator is zero. Someone once told me it was an advantage for the machine to collapse in a heap when any other number is divided by zero. On the charitable assumption he was not an isolated case, then at least there should be a switchable option. The mixture of character and numeric data (pre APL2, I agree) is a bar, but how can an interpreter (VS APL) admit

```
'1'=1
```

as a valid statement (the response is zero) when, if PAGE is a numeric scalar, it would reject

```
'PAGE',PAGE
```

In face VS APL allows

```
=/'PAGE'
```

but rejects

```
=\'PAGE'
```

I am aware that all these niggles can be overcome with simple functions. My concern is that their existence turns APL into an awsome oriental mystery religion whose initiates gleefully converse in magical phrases unintelligible to the plebs. If progamming is to be for all then the initial steps must not be too daunting for the timid outsider. Let us then rid the interpreter of gobbledegook and make allowances for “human” ways of thinking.

Yours sincerely,

D.J. Horton, C.A.

Budget Manager

Pfizer Group Limited

Sandwich, Kent.

*Editor: With reference to 0 divided by 0, there are many good arguments for returning the result 0, rather than 1. See for example “Zero divided by zero”, a paper by Eugene MacDonnell in the APL76 proceedings. There are also convincing reasons for producing a DOMAIN ERROR. See, for example, “The story of 0 divided by 0”, by Joseph de Kerf in the APL80 proceedings. The desire to keep interpreters upward-compatible and to conform to the standard means that few implementors would be willing to change in this area. The best they can do is to provide, as you suggest, a switchable option. This was the approach taken in GEC’s APL, where a system function is used to control the result of division by zero.*

*Your points about numeric and character data are worth looking at more closely. The expression*

```
'1'=1
```

*does indeed produce the result 0, and this is the only reasonable answer if we don’t want to report a DOMAIN ERROR. The fact that we do get a result is very useful — it provides VS APL with a mechanism for determining the type of an array. (The expressions*

```
0=0\0/,W
```

*or*

```
0=1↑0⍴W
```

*will yield a 1 if W is numeric, otherwise a 0). Catenation of a character array with a numeric array does cause a DOMAIN ERROR, and this is reasonable in a language which does not support heterogenous arrays. The definitions of “equal” and “catenate” are different, and so we should expect different results. To understand the reason for the result of*

```
=/'PAGE'
```

*we must recall the informal definition of reduction — the function is inserted between each element of the argument. Therefore the result is*

```
'P'='A'='G'='E'
```

*The first comparison is between two characters (‘G’ = ‘E’), which yields a numeric result. The second and subsequent comparisons are then always of the type ‘character = numeric’, which must give a 0 (recall ‘1’ = 1). The final result must always be 0 for character vectors containing more than two elements. For two element vectors the result is 1 or 0 dependent on whether the characters are the same or not. For scalars or one element vectors the function is not applied and the result is the scalar character, because a dyadic function can be applied between only two arguments. The result of*

```
=\'PAGE'
```

*now follows from the definition of scan, which composes its result by performing a set of reductions on windows of its argument. i.e.*

```
=\'PAGE'   ←→   (=/'P'),(=/'PA'),(=/'PAG'),=/'PAGE'
           ←→   'P',0,0,0
```

*and the DOMAIN ERROR comes indirectly, because character and numeric data cannot be catenated in VS APL. In APL2 this restriction is lifted, and the indicated result would be returned — a vector whose first element is the character ‘1’ and whose final three elements are numeric 0s.*

*Any improvement to APL’s “user friendliness” would indeed be welcome, particularly in the area of error messages. (A recent estimate by Joseph de Kerf put the total number of different error messages in 50 dialects of APL at 1500!). In fact, the message DOMAIN ERROR has a very specific meaning, which has been borrowed from mathematics; if a function argument is outside the domain of that function then the error is reported. Thus division by zero, catenation of a numeric with a character and square-rooting a negative number all report DOMAIN ERROR in VS APL, because the arguments lie outside the domains of the respective functions.*

*The ISO APL standard sensibly uses a new error class — LIMIT ERROR — to report errors which are not strictly errors of domain, but limitations of the system. Attempting to evaluate by multiplication a number whose magnitude is larger than the machine limit, for example, is an error caused by the physical limits of the machine (or APL interpreter) rather than a theoretical deficiency of the multiply function.*
