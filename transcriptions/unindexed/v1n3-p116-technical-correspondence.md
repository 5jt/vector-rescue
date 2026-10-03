---
title: Technical Correspondence
authors:
- Andrew Tarr
- Adrian Smith
- Mark Bassett
volume: '1'
issue: '3'
page: '116'
unindexed: true
transcribed: 'from page images of VOL.1-NO.3-JANUARY-1985.pdf, pages 118–121 (printed 116–119; follows the unindexed Technical Editorial); Claude, 2026-10-03'
review: draft
queries:
- "Three letters. The APL is in a dot-matrix APL face; read at 600 dpi."
- "Tarr: `ω` is DEC APLSF’s omega primitive (indices of ones), not an APL2 symbol; kept as printed. FI 41 read as `(+/B)↑⍒B`."
- "Smith’s ∆PMAX and ∆PMIN checked by hand: with a trailing partition, `⌽+\\⌽MSK` numbers the partitions from the end, so grading `VEC+(1+⌈/VEC)×-⌽+\\⌽MSK` up (or the `+` form down) sorts partition by partition, and `MSK/` picks the last, i.e. largest (smallest), value of each."
- "Bassett’s XR: line [8] is printed `¯2↑ I I ,⍴X` (read as `1 1`, as in [9]); in [11] the arrow is read as `1↑⍴X` (rows), which XR’s logic needs; the glyph before X is `⍉`. In CHANGEWORD [42] `J/` (compress) is printed with a slash through J’s right edge, like `≠`; read as compress. [50] `(B⊖R)[2;]`."
- "Slips transcribed as printed: “sepcified”, “occurence”."
---

## From Andrew Tarr, 28th June 1984

Sir: In applications requiring a search (e.g. names in lists) APL will normally generate a boolean vector, the ones indicating locations where a match was found. Frequently the next step is to translate this into an index. FINNAPL offers three idioms to do this; one of them is the universal favourite, and while the other two present an interesting angle on the problem I cannot see any use for them as they are horribly slow by comparison:

```
FI 506:   B/⍳⍴B
FI 41:    (+/B)↑⍒B
FI 280:   (+\B)⍳⍳+/B
```

To my mind the need to convert a boolean vector to an index is common enough to make a strong case for a special primitive. This is available in DEC-10 APLSF as omega, and although it is non-standard and therefore not documented in the current manual, omega must be an early example of optimised code. Omega is defined for vectors as follows:

```
ωB  ←→  B/⍳⍴B
```

It is invariably faster to execute than the equivalent compression, and because the boolean vector is its right argument, bracketing or assignment is often avoided. Unfortunately it is hard to see a sensible symbol for this primitive; as its closest relative is iota, iota-bar might be a possibility.

Perhaps surprisingly, FINNAPL only offers one idiom to count the ones in a boolean vector:

```
FI 370:   +/B
```

However (depending on the implementation) this is not necessarily the best. In APLSF, of course, the best answer is:

```
⍴ωB
```

Idiom 370 should be last choice for speed, because the DEC interpreter takes time to convert boolean to integer, so it is usually quicker to use:

```
⍴B/1
```

I attach some interesting comparisons between the idioms I have mentioned in VSAPL and in APLSF, for sparse (2.5%) and dense (50%) boolean vectors of 2000 elements.

| (Times in milliseconds) | DEC-10 APLSF 2 Sparse | DEC-10 APLSF 2 Dense | IBM 3081K VS APL (4.0) Sparse | IBM 3081K VS APL (4.0) Dense |
|---|---|---|---|---|
| `B/⍳⍴B` | 13 | 20 | 2 | 2.5 |
| `(+/B)↑⍒B` | 270 | 385 | 25 | 30 |
| `(+\B)⍳⍳+/B` | 405 | 7300 | 23 | 710 |
| `ωB` | 1 | 10 | — | — |
| `+/B` | 20 | 20 | 0.3 | 0.5 |
| `⍴B/1` | 6 | 12 | 2 | 2.8 |
| `+/B/1` | 7 | 20 | 2.3 | 3.0 |

Yours sincerely,

Andrew Tarr, ICI plc (Mond Division), Finance and Info Systems Dept., The Heath, Runcorn, Cheshire.

## From Adrian Smith, 18 August 1984

Sir: You might like to add a couple of functions to the compendium of partition operations from the first issue; both these use a trailing partition, and were written to help analyse commodity data where the weekly highs and lows are important indicators.

```
    ∇ R←MSK ∆PMAX VEC
[1]   ⍝ RETURN MAXIMUM VALUES OF <VEC> WITHIN TRAILING
[2]   ⍝ PARTITIONS MARKED OFF BY <MSK>.
[3]    R←MSK/VEC[⍋VEC+(1+⌈/VEC)×-⌽+\⌽MSK]
    ∇

    ∇ R←MSK ∆PMIN VEC
[1]   ⍝ RETURN MINIMUM VALUES OF <VEC> WITHIN TRAILING
[2]   ⍝ PARTITIONS MARKED OFF BY <MSK>.
[3]    R←MSK/VEC[⍒VEC+(1+⌈/VEC)×⌽+\⌽MSK]
    ∇
```

Both the above are variations on an original theme by Elaine Gathercole.

Yours sincerely,

Adrian Smith, Operational Research, Rowntree Mackintosh plc, YORK.

## From Mark Bassett, 17th December 1984

Sir: The functions we were asked to find in your ‘Life’ competition of two issues back provide a handy way of manipulating text at the word, rather than character, level.

Partition functions are inappropriate to this kind of work due to the complexity of updating the word/non-word partition every time the text is amended. However we can use run-coding to generate a vector showing the lengths of successive words, interspersed with the lengths of the gaps between them, and this is very easy to maintain.

As an example I offer the function CHANGEWORD which performs search and replace functions on character arrays; this is superior to the functions found on some editors as it operates on words not substrings (thereby avoiding constructions such as ‘dogalogue’) and because it performs its substitutions in parallel it can permute words in a document without error.

One use for CHANGEWORD I have already found is a function that relabels others to bring them into line with the convention that line labels follow the sequence L1, L2, L3 … — shades of BASIC!

```
    ∇ R←W CHANGEWORD M;A;B;C;D;I;J;L;N;O;X;Y;⎕IO
[1]   ⍝ WORD BASED SEARCH AND REPLACE FUNCTION
[2]   ⍝ Algorithm by M.S. Bassett - bugs introduced by Forces of Darkness
[3]   ⍝
[4]   ⍝ SYNTAX:
[5]   ⍝ <W> Character vector of words separated by the delimiter in W[1]
[6]   ⍝ <M> Character array to replace in
[7]   ⍝ <R> Character array like <M> with changes made as sepcified by <W>
[8]   ⍝
[9]   ⍝ DESCRIPTION:
[10]  ⍝ <W> is broken up into pairs of words; each occurence in <M> of the
[11]  ⍝ first member of a pair is replaced by the second member. If the
[12]  ⍝ second element is all spaces then the word is deleted.
[13]  ⍝ N.B. - All changes take place simultaneously, and replacement is
[14]  ⍝        performed at the word, not character, level.
[15]  ⍝      - The first element of ⎕AV must not appear in <W> or <M>
[16]  ⍝
[17]   ⎕IO←1
[18]  ⍝ <A> specifies the character set used for recognising words in <M>
[19]   A←'ABCDEFGHIJKLMNOPQRSTUVWXYZ∆abcdefghijklmnopqrstuvwxyz⍙0123456789'
[20]  ⍝ Form <W> into its component words
[21]   W←W[1]FMV 1↓W
[22]   W←((0.5×1↑⍴W),2,¯1↑⍴W)⍴W
[23]  ⍝ Identify Old and New words in <W>
[24]   O←W[;1;]
[25]   N←W[;2;]
[26]  ⍝ Add line delimiters to <M>
[27]   M←M,⎕AV[1]
[28]  ⍝ Flag word-characters in <M>
[29]   B←,M∊A
[30]  ⍝  Run-code the information in <B>
[31]   C←BTR B
[32]  ⍝ Strip out the non-words in <M> and reduce it to its component words
[33]   D←(~B)/,M
[34]   L←' ' FMV B\B/,M
[35]  ⍝ Locate old words in the list <L>
[36]   I←O XR L
[37]   J←I≤1↑⍴O
[38]  ⍝ Replace old by new(this means making <L> and <N> the same width)
[39]   X←(¯1↑⍴L)⌈¯1↑⍴N
[40]   L←((1↑⍴L),X)↑L
[41]   N←((1↑⍴N),X)↑N
[42]   L[J/⍳1↑⍴L;]←N[J/I;]
[43]  ⍝ Now count the new word lengths in <L> and update <C>
[44]   Y←+/' '≠L
[45]   C[2×⍳⍴Y]←Y
[46]  ⍝ Expanding <C> into its boolean form now lets us reform <M>
[47]   B←RTB C
[48]   R←B\(L≠' ')/L←,L
[49]   R←R,[0.5](~B)\D
[50]   R←(B⊖R)[2;]
[51]  ⍝ Reshape <R>, preserving the line-breaks
[52]   R←⎕AV[1]FMV R
    ∇

    ∇ M←D FMV V;M;S;X;⎕IO
[1]   ⍝ FORM MATRIX FROM VECTOR
[2]   ⍝ SYNTAX:
[3]   ⍝ <D> scalar delimiter
[4]   ⍝ <V> vector delimited by <D>
[5]   ⍝ <R> Matrix whose rows are the stretches of <V> between delimiters
[6]   ⍝
[7]    ⎕IO←1
[8]    V←,V,D
[9]    S←(D=V)/⍳⍴V
[10]   X←(X≠0)/X←¯1+S-¯1↓0,S
[11]   M←X∘.≥⍳⌈/0,X
[12]   M←(⍴M)⍴(,M)\(D≠V)/V
    ∇

    ∇ R←X XR Y
[1]   ⍝ MATRIX INDEXING FUNCTION
[2]   ⍝
[3]   ⍝ SYNTAX:
[4]   ⍝ <X> Array of rank ≤ 2  ( Arguments are automatically
[5]   ⍝ <Y> Array of rank ≤ 2    reshaped into matrices     )
[6]   ⍝ <R> Numeric vector giving indices of rows of <Y> in <X> (cf ⍳)
[7]   ⍝
[8]    X←(¯2↑ 1 1 ,⍴X)⍴X
[9]    Y←(¯2↑ 1 1 ,⍴Y)⍴Y
[10]   R←(1↓⍴X)⌈1↓⍴Y
[11]   X←(R,1↑⍴X)↑⍉X
[12]   Y←((1↑⍴Y),R)↑Y
[13]   R←⎕IO++/∧\Y∨.≠X
    ∇
```

M.S. Bassett, 26 Falconwood Ct., Montpelier Row, Blackheath, London SE3 0RS.

*Editor: We hope to get some feedback on Mark’s function as we have not had the time to test it.*
