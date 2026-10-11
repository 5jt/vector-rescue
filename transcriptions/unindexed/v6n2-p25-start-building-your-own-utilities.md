---
title: Start Building your own Utilities
authors:
- Peter Branson
volume: '6'
issue: '2'
page: '25'
unindexed: true
transcribed: 'from page images of VOL.6-NO.2-OCTOBER-1989.pdf, pages 27–30 (printed 25–28; within The Education VECTOR, after Gérard Langlet’s APL “RISC Programming Style”, art10012110); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- education
queries:
- "The `DOC1` listing is printed without the opening ∇, with its header underlined by a row of hyphens and with blank lines between most of its lines; reproduced as printed."
- "In line [3.5] the take arrow is printed with a short crossbar; read as ↑, the take of the text."
- "In line [4] of `DECOMM` the compress is printed as ⌿. In the running text “DECOMM” is first set in roman, later in the APL font; both kept."
---

*by Peter Branson*
{ .byline }

## What are Utilities?

As you get going with APL, you may find it useful to start building up a library of utility functions. These are functions not tied to any particular APL application, but come in useful all over the place, such as alphabetical sorting, selecting a particular name from a list of names. It may be that your APL has the nucleus of a good set in a supplied workspace. Use them. The odds are that, sooner or later, you will want some of your own. In any case writing utility functions helps extend one’s knowledge of APL, since some care is needed to make them robust.

## A Useful Example

Let’s look at an example. When handling character (text) data, there is often a need to join two matrices of characters one above the other - the technical term is catenation on the first axis. The direct APL way of doing this is:-

```apl
      (3 3⍴'CATANDDOG') ,[1] 2 3⍴'XYZ'
CAT
AND
DOG
XYZ
XYZ
```

Here the bracket index join `,[1]` tells APL that we want to join the right argument onto the bottom of the left argument. Note that the example above will only work when the two matrices have the same width. If they are not the same you will get a length error (try it and see).

Now, what if the matrices do have different widths, which occurs fairly often? A simple line of APL will no longer suffice, so let’s set up a utility function for this. I will call this `VCAT` with a header `R←A VCAT B`. Here `A` and `B` may well both be matrices, but it would be useful if the function would work with vectors as well.

For example, we might sometimes want to add just one name to a namelist, in which case B could be a vector. And while we are at it let’s allow for the case where A or B is a singleton; a one-element vector or even a scalar.

How shall we do this generalisation? Well, your first thought might be to do some tests on the shape of `A` and `B` and, according to what type of object each is, to branch to different parts of the function to do what is needed. But this is APL, remember, and of course there is a better way, without branches! Here is one way of writing the `VCAT` function:

```apl
    ∇ R←A VCAT B;MAXW;TOP;BOT
[1]  ⍝ VCAT: VERTICAL CATENATION
[2]  ⍝ EXTEND SINGLES AS REQD. FOR MATRIX RESULT - NUM OR CHAR
[3]  ⍝
[4]   A←(¯2↑ 1 1,⍴A)⍴A
[5]   B←(¯2↑ 1 1,⍴B)⍴B
[6]   MAXW←(¯1↑⍴A)⌈¯1↑⍴B
[7]   TOP←((1↑⍴A),MAXW)↑A
[8]   BOT←((1↑⍴B),MAXW)↑B
[9]   R←TOP,[1] BOT
      ∇
```

Have a look at line 4; this finds the shape of `A` (the result of shape is always a numeric vector), catenates this onto the vector 1 1 and uses the last two elements of the result to reshape `A`. If `A` is a two-dimensional array to start with, it will be unaffected; the reshape will be to its original shape. If it is a vector it will be reshaped to a one-row matrix of the original vector length and if it is a scalar (the shape of a scalar is the empty vector) then it will be reshaped to a one-row, one-column matrix.

The next line does the same for `B`, and line 6 just gets the larger of the two widths. One of lines 7 and 8 will always be redundant; if either of `A` and `B` has fewer columns than the other then a take (`↑`) with the `MAXW` number of columns will pad it with blanks if the arguments are characters and with zeros if the arguments are numeric. This capability of take is often called ‘overtake’, a term worth remembering if it helps to fix this in your memory. And as you will have realised `VCAT` has the added bonus that it works for numeric data as well as characters.

## A Documentation Utility

Looking back at `VCAT` you will see that the first line is a comment showing the function name with a brief description of what it does. Many experienced APLers put comments like this in all their functions, so that by running a suitable documentation utility, a list of names and outline descriptions can be obtained for all the functions in the workspace. This can be useful as the number of functions builds up; it is only too easy to forget what some of them do, and their names (often kept short for typing convenience) may not be mnemonic enough so `)FNS` won’t do the job.

Let’s see what is needed. We will be obtaining the function as a character matrix from `⎕CR` and can pick the appropriate line by indexing. The line lengths will vary but `VCAT` will allow for this when forming the result.

A suitable function, `DOC1`, is listed below. I hope the comments obviate further description:

```apl
      R←DOC1;NAMES;N;J;CR
      -------------------

[1]       ⍝ LIST FN NAME AND 1ST COMMENT LINE OF ALL FNS IN WS
[2]       ⍝ NAMES IS LIST OF ALL FN NAMES, N IS NO OF NAMES

[3]        N←1↑⍴NAMES←⎕NL 3

[4]       ⍝ R IS INITIAL RESULT - EMPTY CHAR MATRIX

[5]        R← 0 0 ⍴''

[6]       ⍝ SET COUNTER J TO 0

[7]        J←0

[8]       ⍝ NOW TAKE EACH NAME IN ORDER

[9]   LOOP:→(N<J←J+1)/END

[10]      ⍝ CR IS THE FN AS A CHARACTER MATRIX

[11]       CR←⎕CR NAMES[J;]

[12]      ⍝ GO TO NEXT IF HEADER LINE ONLY OR DIRECT DEFINITION

[13]       →(1≥1↑⍴CR)/LOOP

[14]      ⍝ DROP LEADING '⍝ ' AND TRAILING BLANKS FOR NEATNESS

[15]       CR←1↓('⍝'=CR[2;1])/CR[2;]
[16]       CR←(+/∧\' '=CR)⌽CR
[17]       CR←(+/∨\⌽' '≠CR)↑CR

[18]      ⍝ R IS PREVIOUS RESULT PLUS (VCAT) THIS COMMENT LINE

[19]       R←R VCAT NAMES[J;],':',CR
[20]       →LOOP
[21]  END:
      ∇
```

Can you amend this function so that it will select all the comment lines in any index origin? (Ed: Can you rewrite it without parentheses?)

## Comment or Decomment

Experienced APLers often recommend that all functions be extensively commented, either to explain some of the tricky APL or to help describe the overall task. There are times when you may want to remove the comments e.g. if space is short.

You could )SAVE the workspace under a different name and then run DECOMM and )SAVE with the usual name. Don’t fail to keep a commented copy.

```apl
      ∇ R←DECOMM FNAME;CR;MASK
[1]   ⍝ DECOMM: DECOMMENT A FUNCTION
[2]    CR←⎕CR FNAME
[3]    MASK←CR[;1]≠'⍝'
[4]    CR←MASK⌿CR
[5]    R←⎕FX CR
       ∇
```

Here we form `CR` as before and then do a not-equals comparison of the first column with the lamp symbol. This gives us a boolean vector with ones for the lines we want to keep and zeros for the lines whose first characters are lamp. Then we compress `CR` to remove the unwanted lines and finally convert `CR` back to a function with `⎕FX`. As it has the same name it will overwrite the previous version.

One disadvantage of `DECOMM` is that it will remove the first line comment. The simplest modification will keep it: add line:

```apl
  [3.5] MASK←MASK∨(⍴MASK)↑0 1
```

This ensures that line one is always represented by a 1 in `MASK`.
