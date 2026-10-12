---
title: 'Technical Correspondence: Vector Jan 2000: Utility Corner (pp. 27-35)'
authors:
- H.J. Veenendaal
volume: '17'
issue: '1'
page: '106'
unindexed: true
transcribed: 'from page images of VOL.17-NO.1-JULY-2000.pdf, pages 108–111 (printed 106–109); Claude, 2026-10-12'
review: draft
tags:
- programming techniques
- development practice
queries:
- "Printed heading “Vector Jan 2000: Utility Corner (pp. 27-35)”, with no Technical Correspondence heading on the page; the Contents line gives “Technical Correspondence” and H.J.Veenendaal. Two letters from Veenendaal (16th and 18th March 2000) about the Utility Corner in the Zark Newsletter Extracts of Vector 16.3 (printed 27–35), followed by his code listings. The piece ends on printed 109; printed 110 begins “At Play with J: Blists in OLEIS”."
- "Following the project rule for individuals’ contact details, Veenendaal’s e-mail address (in the From line) and his street address (after the second letter) are omitted; “Den Haag (NL)” is kept with the omission marked."
- "Only the listings’ glyphs were checked, not the code: it is APL\\*PLUS SE code (`⎕CR`, `⎕NL`, `⎕CURSOR`) and was not run. Read from small italic APL type: in `ANALYSE` [5] and [14] etc. and `ANALYSE1` [31], `1↑⍴` (take), but in `ANALYSE` [4] `1+⍴`; in `ANALYSE1` [30] `1↓⍴`, [51] `1↓I,LEN`; the slashed `/` in [49], [55], [85] and [87] as `⌿`; [87] `0 0⍉<\\IDS∧.=⍉IDS`; [60] `'∆⍙'` (delta and underbarred delta)."
- "The listing of `ANALYSE1` skips lines [6]–[26], as printed (marked “...”)."
- "Kept as printed: “Remarks by the solution on disk”; “a analyse of”; “alle functions”; “excecuting”; “not existent fns”; “ANALYS1 [0]” and “ANALYS1” beside `ANALYSE1`; “superflous”; “renamed in INMAT”; “APLS\\*PLUS SE”; in the code, “unless to long”, “0 if to long”, “folowed”, “raveled”, and `[⍳2]` in the comment of [78]."
---

*From: H.J.Veenendaal ([e-mail address omitted]), 16th March 2000*
{ .byline }

Remarks by the solution on disk: (workspace VECTOR)

1. I did not understand the purpose of the mixed use of `ANALYZE` and `ANALYSE`.
2. I used `ANALYSE` for testing of `ANALYSE1` (= modified given function with same line-numbers) (this makes testing much easier and you don’t create extra global variables in the workspace)
3. The given function doesn’t work if `FNAME` has no local variables!!! (but see for my correction the lines [42] and [55]).<br>
   The correction in line [31] accounts for a function that doesn’t exist or is locked.
4. In line [60] a character ‘s’ must be changed in ‘z’ (but I used `⎕AV`)
5. A display of FNS is not given because it concerns a analyse of `FNAME` and not of the workspace!
6. I removed duplicate names from IDS (a SORT should also be useful) by adding lines [86] and [87].
7. The function `SUBFNS` gives the indices for the subfunctions in FNS and uses the subsubfunction `BIJMAT`.
8. You should (for completeness) have added a similar analyse for global variables used in `FNA`
9. I use APL\*PLUS SE.
10. The workspace VECTOR contains also the function `DOEALL` (using TEXTREPL for 'MMM').

You can test `ANALYSE` for alle functions in the WS by excecuting :

```apl
(⎕NL 3) DOEALL 'ANALYSE ''MMM'''
```

### [Second letter dated 18th March]

**Herewith an improved version of my workspace ‘VECTOR’ (my letter dd. 16/3)**

The improvements concern:

> A display of FNS is added to function `ANALYSE`
>
> An error-message is given by function ‘`ANALYSE`’ for function-names shadowed by local variable-names, locked functions and not existent fns.
>
> (see `ANALYS1` [0] and [31] for corrections concerning your `ANALYSE`-function)
>
> A sort of the IDS-list is added to `ANALYSE1` (see [88]).
>
> Function `BIJMAT` (called in `SUBFNS`) is renamed in `INMAT`.
>
> A part of my function `DOEALL` was (very) superflous and is now removed.

**Remarks:**

After `ANALYSE 'TEXTREPL'` the identifier `TEXTREPLvOBJ` is missing owing to `'⎕'`!.

Line [87] of `ANALYS1` doesn’t work (in APLS\*PLUS SE) for large functions with many identifiers, do you have a better solution?

NB: You can test the `ANALYSE` functions for all functions in the workspace by executing:

```apl
(⎕NL 3) DOEALL 'ANALYSE ''MMM'''
```

> H.J.Veenendaal<br>
> [address omitted]<br>
> Den Haag (NL)

### Code Listings (see www.vector.org.uk/v171/hjv.zip)

```apl
     ∇ ANALYSE FNAME;FNS;RESULT;ARGS;LOCALS;LABELS;IDS;IDS1;COLS;CR;
          HDR;I;LEN;LET;MAX;N;NUM;OK;START;VC;WID
[1]   ⍝ ANALYSE the identifiers within the function named in FNAME.
[2]    ' '
[3]    FNAME,':'
[4]    (1+⍴FNAME)⍴'='
[5]    →(0=1↑⍴⎕CR FNAME)/ERR
[6]    ANALYSE1 FNAME
[7]    'FNS:    The names of functions in the workspace'
[8]    '---'
[9]    FNS
[10]   ' '
[11]   'RESULT: The name of the result variable (0 rows if none)'
[12]   '------'
[13]   RESULT
[14]   ⍎(0=1↑⍴RESULT)/'''[none]'''
[15]   ' '
[16]   'ARGS:   The names of the argument variables (0, 1 or 2 rows)'
[17]   '----'
[18]   ARGS
[19]   ⍎(0=1↑⍴ARGS)/'''[none]'''
[20]   ' '
[21]   'LOCALS: The names of the variables localised in the header'
[22]   '------'
[23]   LOCALS
[24]   ⍎(0=1↑⍴LOCALS)/'''[none]'''
[25]   ' '
[26]   'LABELS: The names of the labels'
[27]   '------'
[28]   LABELS
[29]   ⍎(0=1↑⍴LABELS)/'''[none]'''
[30]   ' '
[31]   'IDS:    The names of all identifiers within the body of
        the functions'
[32]   '---'
[33]   IDS
[34]   ⍎(0=1↑⍴IDS)/'''[none]'''
[35]   ' '
[36]   'SUBFNS: Indices of subfunctions'
[37]   '------'
[38]   SUBFNS
[39]   ⍎(0=⍴SUBFNS)/'⎕CURSOR[1]←¯1+⎕CURSOR[1]'
[40]   ⍎(0=⍴SUBFNS)/'''[none]'''
[41]   ' '
[42]   'SUBFUNCTIONS:'
[43]   '-------------'
[44]   FNS[SUBFNS;]
[45]   ⍎(0=⍴SUBFNS)/'''[none]'''
[46]   →0
[47]  ERR:
[48]   ' '
[49]   'ANALYSE NOT POSSIBLE FOR: ',FNAME
[50]  ⍝ ANALYSE: H.J.Veenendaal 18/03/00 11:29
     ∇

     ∇ ANALYSE1 FNAME;⎕IO
[1]   ⍝ ANALYSE the identifiers within the function named in FNAME.
[2]   ⍝ The ANALYSE1 function creates six global character variables
[3]   ⍝ with one left-justified name per row:
[4]   ⍝ FNS, RESULT, ARGS, LOCALS, LABELS and IDS (see also ANALYSE)
[5]   ⍝
...
[27]  ⍝
[28]   ⎕IO←0
[29]   FNS←⎕NL 3
[30]   COLS←1↓⍴FNS
[31]   →((0=1↑⍴CR←⎕CR FNAME)∨(3≠⎕NC FNAME))/0 ⍝ Quit if FNAME not available
[32]   WID←⍴HDR←CR[0;]
[33]  ⍝
[34]   CR←1 0↓CR
[35]   LEN←('←'∊HDR)×HDR⍳'←' ⍝ Length of the result-var if any
[36]  ⍝ Result is 0 or 1 row matrix (0 if to long)
[37]   RESULT←(((LEN≤COLS)∧×LEN),COLS)⍴COLS↑LEN↑HDR
[38]   HDR←(LEN+×LEN)↓HDR
[39]   HDR←(+/∨\⌽HDR≠' ')↑HDR ⍝ Delete trailing blanks
[40]   LEN←HDR⍳';'
[41]   ARGS←LEN↑HDR
[42]   HDR←(LEN↓HDR),';' ⍝ Drop syntax leaving semicolon!!!!!
[43]   I←(ARGS=' ')/⍳LEN
[44]   N←⍴LEN←(I,LEN)-0,I+1 ⍝ Length of names in syntax
[45]   MAX←⌈/LEN ⍝ Length of longest name
[46]  ⍝ Convert to matrix:
[47]   ARGS←(N,COLS)↑(N,MAX)⍴(,LEN∘.>⍳MAX)\ARGS~' '
[48]  ⍝ Select args, not fn name, unless to long:
[49]   ARGS←((LEN≤COLS)∧(N≥3 1 2)/1 0 1)⌿ARGS
[50]   I←(HDR=';')/⍳LEN←⍴HDR ⍝ Indices of semicolon
[51]   N←⍴LEN←(1↓I,LEN)-I+1 ⍝ Length of localised name
[52]   MAX←⌈/LEN ⍝ Length of longest localised name
[53]  ⍝ Convert to matrix:
[54]   LOCALS←(N,COLS)↑(N,MAX)⍴(,LEN∘.>⍳MAX)\HDR~';'
[55]   LOCALS←¯1 0↓(LEN≤COLS)⌿LOCALS ⍝ Ignore long ones (and extra one)
[56]   OK←=\CR≠'''' ⍝ Flag code NOT within quotes
[57]  ⍝ Flag code NOT within comment or quotes:
[58]   OK←OK∧∧\OK≤CR≠'⍝'
[59]  ⍝ Chars that can begin identifier-names:
[60]   LET←⎕AV[(65+⍳26),(97+⍳26)],'∆⍙'
[61]  ⍝ Other valid chars:
[62]   NUM←'0123456789'
[63]  ⍝ Flag any valid chars, adding col for ending IDs:
[64]   VC←,(OK∧CR∊LET,NUM),0
[65]  ⍝ Flag start and end (+1) of each run:
[66]   VC←VC≠¯1↓0,VC
[67]   N←⍴IDS←VC/⍳⍴VC ⍝ Convert to indices
[68]   IDS←((N÷2),2)⍴IDS ⍝ Two col-mat of start/end indices
[69]   CR←,CR,' ' ⍝ Ravel code and pad to match VC
[70]   START←IDS[;0] ⍝ Start of indices
[71]   LEN←IDS[;1]-START ⍝ Length of names
[72]  ⍝ Must start with letter not be too long and not be preceded by '⎕':
[73]  ⍝
[74]   OK←(CR[START]∊LET)∧(LEN≤COLS)∧'⎕'≠CR[0⌈START-1]
[75]   START←OK/START ⍝ Squeeze out bad ones
[76]   N←⍴LEN←OK/LEN
[77]   IDS←(N×COLS)⍴' ' ⍝ IDS in raveled form
[78]  ⍝ I←(⍳LEN[0]),(⍳LEN[1]),(⍳LEN[⍳2])...:
[79]   I←LEN/¯1↓0,+\LEN
[80]   I←(⍳⍴I)-I
[81]  ⍝ Insert IDS where they belong:
[82]   IDS[I+LEN/COLS×⍳N]←CR[I+LEN/START]
[83]   IDS←(N,COLS)⍴IDS ⍝ Reshape to a matrix
[84]  ⍝ Labels start a line and are folowed by a colon:
[85]   LABELS←((0=(WID+1)|START)∧CR[START+LEN]=':')⌿IDS
[86]   IDS1←IDS
[87]   IDS←(0 0⍉<\IDS∧.=⍉IDS)⌿IDS ⍝ IDS without double items
[88]   IDS←SORTMAT IDS
[89]  ⍝ ANALYSE1: H.J.Veenendaal 18/03/00 11:29
     ∇
```
