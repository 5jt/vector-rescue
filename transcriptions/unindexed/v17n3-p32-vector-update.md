---
title: Vector Update
authors:
- Morten Kromberg
volume: '17'
issue: '3'
page: '32'
unindexed: true
transcribed: 'from page images of VOL.17-NO.3-JANUARY-2001.pdf, pages 34–36 (printed 32–34; within Zark Newsletter Extracts, after “Utility Corner: Comma-Delimited Data”); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- performance
queries:
- "Within the Zark Newsletter Extracts. The framing text (the Dyalog timings, the table and the lead-in to the K entry) is unsigned and evidently by Jon Sandles, who introduces the extracts; the three functions and the “Notes by Morten Kromberg” are Kromberg’s. It is followed on p.34 by Stefano Lanzavecchia’s K solution, transcribed separately as unindexed/v17n3-p34-what-about-a-solution-in-k.md."
- "`c∆m`, `c∆m∆dya` (in Dyalog APL) and `c∆m∆apl2` (with `⎕ML←2`) were run as a check on the transcription, with `SEP` set to newline and comma; each gives the matrix and `fieldwidths` of the Zark sample."
- "Kept as printed: “line and field delimited chars”; in the timings table `COMMA∆MAT2` twice (the third row is evidently `COMMA∆MAT3`); in `c∆m∆apl2` the unused local `sss` and “Alexei” in the comment (“Alexey” in the notes)."
---

## Vector Update

In Dyalog APL version 8.2, running under Windows 2000 in a 32 Mb workspace, the relative times were 174%, 100% and 161% for versions 1, 2 and 3 respectively. To get a reasonable number of seconds to make the timing comparison each function had to be run 2000 times on a character vector of length 63000.

Here are three modern day entries from Morten Kromberg:

```apl
     ∇ r←c∆m v;x;row;col;nl;cm;p;cw;f;b;s;o;fw;i;z
[1]   ⍝ Comma-separated to Char MX.
[2]   ⍝ Global SEP[1] is line delimiter, SEP[2] field delimiter
[3]
[4]    x←SEP[1],v,SEP[1]                    ⍝ Put elephants in Cairo & Cape Town
[5]    row←+\nl←x=SEP[1]                    ⍝ Which row is each char in?
[6]    col←col-⌈\nl×col←+\cm←x=SEP[2]       ⍝ Which field is each char in?
[7]    cw←¯1+1↓p-¯1↓0,p←(b←cm∨nl)/⍳⍴nl      ⍝ Widths of each segment
[8]    f←1+col[¯1+1↓p]                      ⍝ Column number of each piece
[9]    fw←(×/s←(¯1+¯1↑row),⌈/f)⍴0           ⍝ Ravelled field width matrix
[10]   fw[(s[2]×¯1+¯1↓b/row)+f]←cw          ⍝ Insert field widths
[11]   fw←⌈⌿s⍴fw                            ⍝ Find greatest width of each field
[12]   r←(×/s←s[1],+/fw)⍴' '                ⍝ Now we know how big r must be
[13]   o←o-⌈\b×o←⍳⍴b                        ⍝ Offset within each field of each char
[14]   i←o+((+\¯1↓0,fw)[1+col])+s[2]×¯1+row ⍝ Where in r does each char go?
[15]   r[z/i]←(z←~b)/x                      ⍝ Place them in r (except separator
                                              chars)
[16]
[17]   r←s⍴r ⋄ fieldwidths←fw
     ∇

     ∇ r←c∆m∆apl2 x;sss
[1]   ⍝ APL2-style solution, thanks to Alexei for inspiration
[2]
[3]    r←(SEP[1]=r)⊂r←SEP[1],x              ⍝ Cut into rows
[4]    r←SEP[2],¨1↓¨r                       ⍝ Replace line separator by field
                                              separator
[5]    r←(⊂0 1)↓¨⊃¨⊂[1]⊃(r=SEP[2])⊂¨r      ⍝ Cut rows into fields, mix, split,
                                              drop leading separators
[6]    fieldwidths←2⊃¨⍴¨r                   ⍝ One field in each cell now
[7]    r←↑,/r                               ⍝ Extract the result
     ∇

     ∇ r←c∆m∆dya v;x;row;col;nl;cm;p;cw;f;b;s;o;fw;i;z
[1]   ⍝ Comma-separated to Char MX.
[2]   ⍝ Global SEP[1] is line delimiter, SEP[2] field delimiter
[3]
[4]    x←SEP[1],v,SEP[1]                    ⍝ Put elephants in Cairo & Cape Town
[5]    row←+\nl←x=SEP[1]                    ⍝ Which row is each char in?
[6]    col←col-⌈\nl×col←+\cm←x=SEP[2]       ⍝ Which col/field is each char in?
[7]    cw←¯1+1↓p-¯1↓0,p←(b←cm∨nl)/⍳⍴nl      ⍝ Widths of each segment
[8]    f←1+col[¯1+1↓p]                      ⍝ Column number of each piece
[9]    fw←(⌈/f)⍴0 ⋄ fw[f]⌈←cw               ⍝ ⌈← in Dyalog APL only, sorry: search
                                              FinnAPL idiom library for PMAXREDUCE
[10]   r←(×/s←(¯1+¯1↑row),+/fw)⍴' '         ⍝ Now we know how big r must be
[11]   o←o-⌈\b×o←⍳⍴b                        ⍝ Offset within each field of each char
[12]   i←o+((+\¯1↓0,fw)[1+col])+s[2]×¯1+row ⍝ Where in r does each char go?
[13]   r[z/i]←(z←~b)/x                      ⍝ Place them in r (except separator
                                              chars)
[14]
[15]   r←s⍴r ⋄ fieldwidths←fw
     ∇
```

### Notes by Morten Kromberg

Here is my entry. It does not conform 100% with the spec, because I have made the separators configurable, you need to initialise the global variable `SEP` to contain the line and field delimited chars. In the workspace, they are set to `'/,'`, so you must replace `SEP[1]` with newline.

The comment on line 4 about elephants is a reference to an old joke about the PL/1 programmer who was asked how he would go about finding an African elephant. His explanation began: before starting in Cairo, I will send one elephant to Cape Town to make sure that the search will end.

`c∆m` is my actual entry. No enclosed arrays, just lots of scans and indexing – pure “ISO APL”. `c∆m∆dya` is a DyalogAPL only version, which is a bit shorter because it uses a `⌈←` on line [9].

`c∆m∆apl2` is a MUCH shorter/simpler version using partitioned enclose (thanks to Alexey Miroshnikov for providing inspiration for this solution).

Depending on the arguments, the two functions take turns at being the fastest (it seems the APL2 version is actually significantly faster on quite a variety of arguments though, I would have sworn that the plain vanilla APL version would do better than it actually does).

Note `⎕ML` is 2 in the workspace, so that the “APL2” solution is APL2-like.

---

Sadly, they do no better than the three original Zark solutions:

```text
COMMA∆MAT1   172
COMMA∆MAT2   100
COMMA∆MAT2   160
c∆m          298
c∆m∆apl2     210
c∆m∆dya      353
```

(Timings as percentages of the fastest)

I do not have the facilities to compare Stefano’s K entry. However, here it is:
