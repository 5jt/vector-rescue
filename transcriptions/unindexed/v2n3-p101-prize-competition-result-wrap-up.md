---
title: 'Prize Competition Result: Wrap Up'
authors:
- David Ziemann
volume: '2'
issue: '3'
page: '101'
unindexed: true
transcribed: 'from page images of VOL.2-NO.3-JANUARY-1986.pdf, pages 103–105 (printed 101–103; the result of the competition set in v2n1-p105-prize-competition-wrap-up.md; the Test your Skill update follows on p.104); Claude, 2026-10-05'
review: draft
queries:
- "Listings are printed in a small monospace APL face; the comment lamp ⍝ is printed as a small ∩-like glyph. Long header and comment lines are kept on one line."
- "Checked: WRAPHR, simulated line by line as printed (index origin 0), gives exactly both printed results (10 0 WRAP and 11 2 WRAP). WRAPZH and WRAPNAPS were not simulated."
- "WRAPZH [18] is printed with ⍀ (expand along the first axis); [21] `VEC[BRK+1+¯1↓0,+\\I+~FOUND]←DELIM`."
- "WRAP1LINE [3] is printed `(--/N)↑1`, a double minus, read as negate of minus-reduce. WRAPNAPS uses APL*PLUS nested-array primitives: ⊂ (partition), ⊃ (disclose) and ¨ (each)."
- "In the VERSE session the second line is printed `'And the joint was‹ closed for the night'` with a stray mark after was; omitted."
- "Slips transcribed as printed: “inlcuded”, “quadTC”."
---

by David Ziemann
{ .byline }

The problem was to write a function \<WRAP\> which can fold delimited long lines as follows:

```apl
      ,S←'IN PARADISE',cr,'HERONS',cr,'APPROACH FROM THE LEFT.'
IN PARADISE
HERONS
APPROACH FROM THE LEFT.
      10 0 WRAP cr,S
IN PARADIS
E
HERONS
APPROACH F
ROM THE LE
FT.

      11 2 WRAP cr,S
IN PARADISE
HERONS
APPROACH FR
  OM THE LE
  FT.
```

The delimiter used to separate the lines is determined by the first character of the vector right argument. The left argument specifies the required width and the indentation for folded lines.

So what were the results like? One entry was disqualified because folded lines were themselves allowed to exceed the required width limit. Two solutions were disqualified for assuming that the delimiter was a carriage return character, one inlcuded a reference to the VS APL system variable quadTC (not standard-conforming) and one referred to a global variable \<cr\>.

This well commented solution was sent in by Heinz Reutersberg from Cologne in West Germany:

```apl
    ∇ OUT←N WRAPHR S;I;L;P;⎕IO
[1]   ⍝ VECTOR 2 1 105: WRAP TEXT  1↓S  TO  1↑N  COLUMNS, USING DELIMITER
[2]   ⍝ CHARACTER  1↑S  AND  1↓N  INDENTATION BLANKS FOR FOLDED LINES
[3]   ⍝ (0<1↑N), (0≤1↓N), (0<-/N) ARE ASSUMED BUT NOT CHECKED
[4]    ⎕IO←0
[5]    P←(S=1↑S)/⍳⍴S←,S
[6]    L←¯1+(1↓P,⍴S)-P
[7]    I←(1↑N)+(-/N)×⍳⌈((⌈/L)-1↑N)÷-/N←2↑,N
[8]    P←(,L∘.>I)/,P∘.+I
[9]    OUT←1↓(S,' ')[(⍴S)⌊⍋(⍳⍴S),((1+1↓N)×⍴P)⍴P]
[10]   OUT[P+(⍳⍴P)×1+1↓N]←1↑S
    ∇
```

which produces the desired results. Zeke Hoskin from Vancouver in Canada extended the problem specification to optionally fold lines on word breaks, thereby simultaneously satisfying the competition requirements as well as Mark Bassett’s Surely There Must be a Better Way problem from VECTOR 2.1. The word break option is specified as the third element of the left argument, which instructs the function to perform word breaking within that distance from the end of the line fragment. Here are some samples, using Zeke’s own sample text:

```apl
    ∇ VEC←WIB WRAPZH VEC;P;BOO;DELIM;⎕IO;W;I;B;LEN;LONG;BRK;DEPTH;FOUND;MASK;MX
[1]   ⍝ wrap  character vector to specified width, indenting and breaking
[2]   ⍝     preferentially at blanks
[3]   ⍝VEC=a character vector delimited by 1st character
[4]   ⍝WIB=width of output(not counting delimiters),indentation,blankdepth
[5]   ⍝ where blankdepth = how far from right-hand end of line to seek a blank
[6]   ⍝ Indentation and blankdepth default to 0
[7]    ⎕IO←1 ⋄ WIB←3↑,WIB ⋄ W←WIB[1] ⋄ I←WIB[2] ⋄ B←WIB[3] ⋄ DELIM←VEC[1]
[8]   TOP: ⍝ each pass breaks a given line at most once
[9]    P←BOO/⍳⍴BOO←VEC=DELIM
[10]  ⍝measure line lengths and quit if none is greater than W
[11]   →(∨/LONG←W<LEN←(1↓P,1+⍴VEC)-P+1)↓0
[12]  ⍝create matrix of beginnings of lines to be broken
[13]   MX←VEC[(P←LONG/P)∘.+⍳W+1]
[14]  ⍝break before last blank(that's why (w+1)th char included)
[15]   BRK←P+W-(FOUND←DEPTH≤B+1)×DEPTH←+/∧\⌽MX≠' '
[16]  ⍝since replicate is not in all APLs, construct expansion mask
[17]   MASK←(⍴VEC)⍴0 ⋄ MASK[BRK]←1
[18]   MASK←1,MASK⍀(((⍴BRK),I)⍴1),~FOUND
[19]   MASK←(,MASK)/,1,((⍴VEC),I+1)⍴0
[20]   VEC←MASK\VEC
[21]   VEC[BRK+1+¯1↓0,+\I+~FOUND]←DELIM
[22]   →TOP
    ∇

      VERSE←cr,'The beer was spilled',cr,'On the barroom floor'
      VERSE←VERSE,cr,'And the joint was closed for the night'
      VERSE

The beer was spilled
On the barroom floor
And the joint was closed for the night

      12 3 WRAPZH VERSE ⍝ Indent by 3, no blank search

The beer was
   spilled
On the barro
   om floor
And the join
   t was clo
   sed for t
   he night

      12 3 5 WRAPZH VERSE ⍝ Indent 3, break at blanks within 5 of limit

The beer was
   spilled
On the
   barroom
   floor
And the
   joint was
   closed
   for the
   night

      12 0 5 WRAPZH VERSE ⍝ No indent, break at blanks within 5

The beer was
spilled
On the
barroom
floor
And the
joint was
closed for
the night
```

Notice that the function leaves a leading delimiter character on its result. The extra generality of this function means that it runs a lot slower than Heinz’s when ignoring word breaks. By the way, the sample verse above wasn’t the most esoteric; one solution contained a sample of what appears to be late 19th century romantic French poetry! (Thanks to D Horton for that).

Maurice Jordan provides us with the following APL\*PLUS nested array solution:

```apl
    ∇ TV←N WRAPNAPS TV;LINES
[1]   ⍝ Solution for APL*PLUS nested array production system
[2]    TV←⎕TCNL,TV
[3]    LINES←(TV=⎕TCNL)⊂TV                  ⍝ split into lines
[4]    LINES←(⊂2↑N) WRAP1LINE¨LINES         ⍝ wrap each line
[5]    TV←1↓⊃,/LINES                        ⍝ Reassemble
    ∇

    ∇ TV←N WRAP1LINE TV;STARTS;LINES;INSERT
[1]   ⍝ Wrap 1 line TV. N←2 integer vector (max length)(offset for new line)
[2]    →((1+⊃N)≥⍴TV)/0 ⍝ No need to do processing
[3]    STARTS←(⍴TV)↑1,((INSERT←1+2⊃N)↑0),(⍴TV)⍴(--/N)↑1 ⍝ Where to wrap
[4]    LINES←STARTS⊂TV ⍝ Split into new lines
[5]    LINES←LINES,¨⊂INSERT↑⎕TCNL ⍝ Append insert to each line
[6]    TV←(-INSERT)↓⊃,/LINES ⍝ Reassemble and drop last insert
    ∇
```

Once you know what the symbols mean, it’s a lot easier to understand than the standard APL solution, and was probably a lot easier to code too.

Prizes of thirty, ten and ten pounds respectively go to Heinz Reutersberg, Zeke Hoskin and D Horton.
