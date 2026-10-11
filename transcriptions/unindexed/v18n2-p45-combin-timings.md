---
title: 'Editor’s Note: COMBIN Timings'
volume: '18'
issue: '2'
page: '45'
unindexed: true
transcribed: 'from page images of VOL.18-NO.2-OCTOBER-2001.pdf, pages 47–48 (printed 45–46; follows the Zark reprint note after art10014430); Claude, 2026-10-11'
review: draft
tags:
- performance
- programming techniques
queries:
- "Within the Zark Newsletter Extracts, after the reprint note that closes the extract. The note has no heading; the title is supplied. It is unsigned, introduced “[Ed:”; whether the editor is Jon Sandles (who edits the extracts) or the editor of *Vector* is not said. It supplements the COMBIN solutions reprinted in 18:1 (art10014440)."
- "The three functions were run in Dyalog APL as a check on the transcription; each returns the ten combinations for `3 COMBIN 5` (`3 cmat 5`)."
- "Kept as printed: “off set”."
---

[Ed: The following is a summary of relative times for `4 COMBIN 15` (see *Vector* 18:1) in the original 1992 article and in Dyalog APL version 8.2:]

| `COMBIN` version | APL\*PLUS II | Dyalog APL |
|:-:|:-:|:-:|
| 1 | 14 | 23 |
| 2 | 10 | 21 |
| 3 | 92 | 166 |
| 4 | 17 | 32 |
| 5 | 27 | 56 |
| 6 | 5 | 8 |
| 7 | 1 | 1 |

Anne Wilson submitted the following function which unfortunately ran 242 times slower than the fastest version!

```apl
     ∇ i←n COMBIN m
[1]   ⍝ ADW 10/6/2001
[2]   ⍝ Returns n column matrix of all combinations of n from m
[3]    i←⌽⍉(m⍴2)⊤⍳¯1+2*m        ⍝ Generate all combinations
[4]    i←(n=+/i)/[1]i           ⍝ Keep those with n elements
[5]    i←i×(⍴i)⍴⍳m              ⍝ Turn them into indices
[6]    i←((⍴i)[1],n)⍴(0≠,i)/,i  ⍝ Remove all zeros
     ∇
```

Gordon Haig’s function only ran 63 times slower:

```apl
     ∇ Z←R COMBIN N;LIST;VEC;UPPER;COL;COLS
[1]     LIST←(0,R)⍴⍳0
[2]     VEC←⍳R                      ⍝ Lowest number
[3]     UPPER←(~(⍳N)∊⍳(N-R))/⍳N ⍝ Highest number stored for ref.
[4]    LQ1:LIST←LIST⍪VEC            ⍝ Current lowest number onto list
[5]     →(VEC≡UPPER)/LQ2            ⍝ Finish if reached highest number
[6]     COL←R-+/(VEC=UPPER)         ⍝ Rightmost incrementable column
[7]     COLS←⍳(R+1-COL)             ⍝ COLS: the consecutive increments
[8]     VEC[¯1+COL+COLS]←VEC[COL]+COLS ⍝ Increments off set & placed
[9]     →LQ1
[10]   LQ2:Z←LIST
     ∇
```

Finally, not a submission, but the Dyalog version 9.0 `dfns` sample workspace contains the following function which ran 3 times slower than the fastest Zark example:

```apl
cmat←{⎕ML←2                         ⍝ ⍺-combination matrix of ⍳⍵.
     ↑↑(⊂⊂1 0⍴0){                   ⍝ base-case: [0 ⍵].
         ¯1↓↑{                      ⍝ removing base case from,
             (⍪/⌽{⎕IO,⍵}\1+⍺(↑⍵)),⍵  ⍝ accumulation of,
         }/⍵,⍺⍺                     ⍝ sub- (⍺ ⍵-1) combinations,
     }/(⍳0⌈⍵-⍺),⊂(⍺≤⍵){⍺ ⍵⍴⍳⍵}¨⌽+\⍺⍴1 ⍝ with base cases [⍺ 0].
 }
```
