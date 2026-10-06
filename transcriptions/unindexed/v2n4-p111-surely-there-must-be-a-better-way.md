---
title: Surely there must be a better way (Fuzzy Look-Ups; Phonetic Searching)
authors:
- David Ziemann
volume: '2'
issue: '4'
page: '111'
unindexed: true
transcribed: 'from page images of VOL.2-NO.4-APRIL-1986.pdf, pages 113–116 (printed 111–114; APL Trivia follows on p.115); Claude, 2026-10-05'
review: draft
tags:
- programming techniques
queries:
- "Byline printed “compiled by David Ziemann”; the contents list names the parts “Fuzzy look-up, Simon Barker” and “Phonetic searching, David Ziemann”."
- "Checked: MAT MATCH 'PL.' gives 0 0 0 1 as printed; SOUNDEX∆CODE, simulated as printed, gives T265 for TISSERAND, TISEROND and TIZZEWRONGED; REP’s example 2 0 3 1 REP 'ABCD' gives 'AACCCD'."
- "p.114: the table of Soundex codes for distortions of “Wensleydale” is not printed; a blank space of about a third of the page stands where it should be (a paste-up omission). Noted in the text."
- "The text says “the call to function <REP> on line 4”; REP is called on line [6] of SOUNDEX∆CODE. Printed so."
- "MATCH [7] is printed `⍎(0=⎕NC 'badchrs')/'badchrs←''AEIOUY ../;:-+'''`; SOUNDEX∆CODES [10] `R←(,1,R≠1⌽R)/,'/',R`; MIM [7] `I←1↓I-1↓0,¯1↓I←B/⍳⍴B`; MIM [9] `R←(⍴R)⍴(,R)\\(~B)/V`. The listings are in a small monospace face; lower-case comments as printed."
---

compiled by David Ziemann
{ .byline }

## Fuzzy Look-Ups

Simon Barker from Catford, London has sent us a function which he uses for doing what he calls a fuzzy table lookup. Here is Simon to explain his problem and solution:

> “In several applications used in my place of work there is a need to take into account mis-spellings of names used for selecting records from a file, the name being the key to an individual record. As an example, the names ‘PETER’ and ‘PEATER’ should both match a record with a key of ‘PETER’. In effect a sort of fuzzy version of the commonplace expression
>
> ```apl
> MAT∧.=VEC
> ```
>
> “is required, where \<MAT\> contains a matrix of names and \<VEC\> contains a name that is to be matched against \<MAT\>. The fuzzy version of the above expression might look like this:
>
> ```apl
>       ⎕←MAT←4 5⍴'CATS DOGS .....A.P.L'
>       badchrs←'AEIOU .'
>       MAT MATCH 'PL.'
> 0 0 0 1
> ```
>
> “The variable \<badchrs\> contains characters that are to be ignored in the matching process. My solution is as follows:
>
> ```apl
>     ∇ R←SET MATCH ITEM;SH;M;DF;Z
> [1]   ⍝ DOES EQUIVALENT OF <SET> ∧.= <ITEM>
> [2]   ⍝ <ITEM> IS ANY CHAR. VECTOR, <SET> IS ANY CHAR. MATRIX
> [3]   ⍝ MATCHING IGNORES ANY CHARS. ASSIGNED TO GLOBAL VAR <badchrs>
> [4]   ⍝
> [5]   ⍝ IF GLOBAL VARIABLE HAS NOT BEEN ASSIGNED, SET IT TO DEFAULT
> [6]   ⍝
> [7]    ⍎(0=⎕NC 'badchrs')/'badchrs←''AEIOUY ../;:-+'''
> [8]   ⍝
> [9]    SH←⍴SET
> [10]   M←~SET∊badchrs
> [11]   DF←(Z←⌈/+/M)-⌊/+/M
> [12]   M←,M,(Z-+/M)∘.≥⍳DF
> [13]   SET←M/,(SH+0,DF)↑SET
> [14]   SET←(SH[1],Z)⍴SET
> [15]   R←SET∧.=Z↑(~ITEM∊badchrs)/ITEM
>     ∇
> ```
>
> “Although reasonably efficient, the function can only cope with a vector right argument. I would be very interested to see an improved version of \<MATCH\> which could emulate the standard inner product solution to a higher degree, i.e. matrices on either/both side(s) and numbers as well as text. One final point, the solution I have supplied does not behave consistently when the right argument is made up of characters that are all contained in \<badchrs\> and the left argument has a row of spaces in it. Can you spot why this is so, and propose a generalised solution?”

We would be glad to receive any comments or improvements on Simon’s function. Have any other readers worked in this area?

## Phonetic Searching

Another technique for locating names in a database or table of names is Soundex searching, which can return entries that sound alike but are spelt differently. The Soundex system works by converting the name to a four digit key. There are four steps to this process. First, each letter of the name except the first is replaced by the corresponding number from the following table:

| Letter | Number |
| --- | --- |
| A,E,H,I,O,U,W,Y | 0 |
| B,F,P,V | 1 |
| C,G,J,K,Q,S,X,Z | 2 |
| D,T | 3 |
| L | 4 |
| M,N | 5 |
| R | 6 |

Second, all successive occurrences of the same digit are removed from the string. Next, all zeros are deleted. The last step is to make the code four characters long, either by truncation or by padding with zeros. Here’s an example of the process using the name “TISSERAND”:

| Step | Code |
| --- | --- |
| 1 | T02206053 |
| 2 | T0206053 |
| 3 | T2653 |
| 4 | T265 |

The following functions implement the above algorithm directly:

```apl
    ∇ R←SOUNDEX∆CODE W;L;N
[1]   ⍝ Return the SOUNDEX code corresponding to the name in <W>
[2]   ⍝ <R> is a 4 character code. <W> is a character vector
[3]   ⍝ Alphabet
[4]    L←'AaEeHhIiOoUuWwYyBbFfPpVvCcGgJjKkQqSsXxZzDdTtLlMmNnRr'
[5]   ⍝ Correspondence vector from alphabet to digits
[6]    N← 16 8 16 4 2 4 2 REP '0123456'
[7]   ⍝ Map all but first letter onto digits
[8]    R←(N,'0')[L⍳1↓W]
[9]   ⍝ Delete consecutive duplicate digits
[10]   R←(R≠1⌽R)/R
[11]  ⍝ Delete zero digits
[12]   R←(R≠'0')/R
[13]  ⍝ Pad or truncate code to four characters
[14]   R←4↑(1↑W),R,'000'
    ∇

    ∇ R←A REP W;⎕IO
[1]   ⍝ Return a vector of elements from <W> replicated by <A>
[2]   ⍝ Arguments may be scalars or vectors only
[3]   ⍝ EXAMPLE : 2 0 3 1 REP 'ABCD' ←→ 'AACCCD'
[4]    ⎕IO←0
[5]    A←(⍴W←R/W)⍴A←(R←×A)/A
[6]    R←W[+\(⍳+/A)∊+\A]
    ∇
```

The function copes with lowercase as well as uppercase alphabetic characters. Users of APLs that support the “replicate” extension of the compress function may replace the call to function \<REP\> on line 4 by a /. Alternatively the line can be recoded as the catenation of reshapes. Here’s the function in action:

```apl
      SOUNDEX∆CODE'TISSERAND'
T265
      SOUNDEX∆CODE'TISEROND'
T265
      SOUNDEX∆CODE'TIZZEWRONGED'
T265
```

If a database or table of names already exists, it is more useful to be able to directly convert a matrix of names into their Soundex codes, for storage with the original names. The function can be modified to deal with a matrix argument as follows:

```apl
    ∇ R←SOUNDEX∆CODES W;L;N
[1]   ⍝ Return SOUNDEX codes corresponding to the names in <W>
[2]   ⍝ <R> is a 4 column matrix of codes. <W> is a char. matrix.
[3]   ⍝ Alphabet
[4]    L←'AaEeHhIiOoUuWwYyBbFfPpVvCcGgJjKkQqSsXxZzDdTtLlMmNnRr'
[5]   ⍝ Correspondence vector between alphabet and digits
[6]    N← 16 8 16 4 2 4 2 REP '0123456'
[7]   ⍝ Map all but first letter onto digits
[8]    R←(N,'0')[L⍳ 0 1 ↓W]
[9]   ⍝ Delete successive occurrences of same digits
[10]   R←(,1,R≠1⌽R)/,'/',R
[11]  ⍝ Delete zero digits
[12]   R←(R≠'0')/R
[13]  ⍝ Pad or truncate codes to four characters
[14]   R←W[;1],MIM R
[15]   S←⍴R←((1↑⍴R),4)↑R
[16]   R←,R
[17]   R[(R=' ')/⍳⍴R]←'0'
[18]   R←S⍴R
    ∇

    ∇ R←MIM W;⎕IO;V;B;I
[1]   ⍝ Make character vector <W> into character matrix <R>
[2]   ⍝ Rows of <R> are delimited by 1↑<W> in <W>
[3]   ⍝ 2←→⍴⍴R
[4]    ⎕IO←1
[5]    V←W,1↑W
[6]    B←V∊1↑W
[7]    I←1↓I-1↓0,¯1↓I←B/⍳⍴B
[8]    R←I∘.≥⍳⌈/I
[9]    R←(⍴R)⍴(,R)\(~B)/V
    ∇
```

The function \<MIM\> is a standard Make-Into-Matrix function which takes the first element of its argument as a delimiter indicating where the argument should be broken into rows in the resulting matrix.

Here are the results of applying the function to a table of distortions of the word “Wensleydale”:

*[The table of results is missing: the space for it on p.114 is blank.]*

Notice how the last attempt does not produce the same Soundex code as the others and therefore would not constitute a “hit” on the name.
