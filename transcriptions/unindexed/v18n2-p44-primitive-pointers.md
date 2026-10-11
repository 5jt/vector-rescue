---
title: Primitive Pointers
authors:
- Gary A. Bergquist
volume: '18'
issue: '2'
page: '44'
unindexed: true
transcribed: 'from page images of VOL.18-NO.2-OCTOBER-2001.pdf, pages 46–47 (printed 44–45; follows the Limbering Up column after art10014430); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
queries:
- "Within the Zark Newsletter Extracts, introduced by Jon Sandles. The column is unsigned; it is attributed to Gary Bergquist as the index attributes the Utility Corner columns of the series. The reprint note at the foot of p.45, which closes the extract, is included here."
- "The underlined epsilon is transcribed `⍷` (find) and the slashed bar `⌿`. The expressions were run in Dyalog APL as a check on the transcription; the bit strings and selections agree with those printed."
- "Kept as printed: “If you don’t believe use, try it out!”; “characters that are *not* with quotes or comments”."
---

(The purpose of this column is to point out some facts about the primitive APL functions you may have overlooked or forgotten. If you don’t believe use, try it out!)

From last issue: the first step in parsing an executable APL expression for identifier names is to ignore the text within quotes. Here’s an example:

```apl
      EXPR←'SUB←(∨/''FL''⍷NAMES)⌿NAMES'
```

The identifiers used in this expression are `SUB` and `NAMES`. `FL` is not an identifier because it’s within quotes. The `=\` and `≠\` functions can be used to distinguish between text within quotes and text outside quotes. Let’s try them (blanks between bit elements are omitted for clarity):

```apl
      EXPR
SUB←(∨/'FL'⍷NAMES)⌿NAMES
```

Mark the quotes:

```apl
      EXPR=''''
000000010010000000000000
```

Text within quotes including leading quote:

```apl
      ≠\EXPR=''''
000000011100000000000000
```

Select all other characters:

```apl
      (~≠\EXPR='''')/EXPR
SUB←(∨/'⍷NAMES)⌿NAMES
```

`=\` is the opposite of `≠\`:

```apl
      EXPR≠''''
111111101101111111111111
      =\EXPR≠''''
111111100011111111111111
```

Exclude both quotes, selecting just non-quoted text:

```apl
      (=\EXPR≠'''')∧EXPR≠''''
111111100001111111111111
      ((=\EXPR≠'''')∧EXPR≠'''')/EXPR
SUB←(∨/⍷NAMES)⌿NAMES
```

The second step in parsing an executable APL expression is to ignore the text following lamp (`⍝`) symbols. An example:

```apl
      X←'SUB∨/''⍝FL''⍷NAMES ⍝ LOOK FOR ''⍝FL'''
```

The identifiers used in this expression are `SUB` and `NAMES`, not `FL`, `LOOK`, or `FOR`. What APL expression selects from a character vector `X` just those characters that are *not* with quotes or comments?

Answer next issue. (Hint: Experiment with `∧\` and `∨\`. Consider only lamp symbols outside quotes.)

---

*Reprinted with kind permission from Zark APL Tutor News, a quarterly publication of Zark Incorporated, 23 Ketchbrook Lane, Ellington, CT06029, USA*
