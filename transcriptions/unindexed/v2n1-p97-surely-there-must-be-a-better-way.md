---
title: Surely There Must Be a Better Way
authors:
- David Ziemann
volume: '2'
issue: '1'
page: '97'
unindexed: true
transcribed: 'from page images of VOL.2-NO.1-JULY-1985.pdf, pages 99–100 (printed 97–98; the prize competitions follow on p.99); Claude, 2026-10-05'
review: draft
queries:
- "Byline printed “compiled by David Ziemann”; the contents list gives “Andrew Wiggins, Mark Bassett”, whose problems these are (see their letters, v2n1-p95-technical-correspondence.md)."
- "Checked: Wiggins’s required solution (Profit/(Loss) 30 0 0 0 0 70 0 0 10 0; Carried forward 0 20 40 40 20 0 20 20 0 40) follows from the example data and rules."
- "Checked: WORDWRAP, simulated line by line as printed, gives exactly the two printed results (20 WORDWRAP X, 8 WORDWRAP Y)."
- "WORDWRAP [9] is printed `C←C-N<C←C+N×C=0`; [10] `R←R,[1]N↑C↑X`."
- "Slips transcribed as printed: “uneccessary”, “borogroves”, “momerathes”; the Profit(Loss) row name in the last sentence."
---

compiled by David Ziemann
{ .byline }

This issue we have two STMBABWs; one from Andrew Wiggins of Lombard North Central, and one sent in by Mark Bassett. In their letters, which appear on the Technical Correspondence page, they both explain that they have found looping solutions to their respective problems, but have not been able to find non-looping ones. Here’s Andrew to kick off with his problem:

> “The problem is accountancy based, but don’t let that put you off. It involves two pieces of information:
>
> 1) Income  
> 2) Depreciation
>
> The rules are that:
>
> a) Depreciation must never exceed income, (although they may be equal).  
> b) Any excess of depreciation over income must be carried forward and used as soon as possible AFTER the period(s) in which any excess may occur.

Here is an example problem:

| Year | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Income | 100 | 110 | 120 | 130 | 140 | 150 | 160 | 170 | 180 | 190 |
| Depn. | 70 | 130 | 140 | 130 | 120 | 60 | 180 | 170 | 150 | 230 |
| Profit/(Loss) | 30 | (20) | (20) | 0 | 20 | 90 | (20) | 0 | 30 | (40) |

… and its required solution:

| Year | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Income | 100 | 110 | 120 | 130 | 140 | 150 | 160 | 170 | 180 | 190 |
| Depn. | 70 | 110 | 120 | 130 | 140 | 80 | 160 | 170 | 170 | 190 |
| Profit/(Loss) | 30 | 0 | 0 | 0 | 0 | 70 | 0 | 0 | 10 | 0 |
| Carried forward | 0 | 20 | 40 | 40 | 20 | 0 | 20 | 20 | 0 | 40 |

Presumably Andrew will be happy with a solution that yields the Profit(Loss) and Carried forward rows from the required solution table shown above.

Mark Bassett wants a function \<WORDWRAP\> that reshapes text into a left justified matrix of specified width with no uneccessary word breaks. He provides the following examples, along with his version of the function:

```apl
      X←' Twas brillig and the slithy toves '
      ,X←X,'did gyre and gimble in the wabe. '
 Twas brillig and the slithy toves did gyre and gimble in the wabe.
      Y←'All mimsy were the borogroves '
      ,Y←Y,'and the momerathes outgrabe.'
All mimsy were the borogroves and the momerathes outgrabe.
      20 WORDWRAP X
Twas brillig and the
slithy toves did
gyre and gimble in
the wabe.
      8 WORDWRAP Y
All
mimsy
were the
borogrov
es and
the
momerath
es
outgrabe
.
```

```apl
    ∇ R←N WORDWRAP A;C;D;V;X
[1]   ⍝ Wrap text <A> into a matrix <R> of width <N>
[2]   ⍝ If at all possible, words are not broken.
[3]    D←1↑0⍴V←,A
[4]    R←(0,N)⍴''
[5]   L1:→(0=⍴V)/0
[6]    V←(∨\V≠D)/V
[7]    X←(N+1)↑V
[8]    C←N+1-+/∧\⌽X≠D
[9]    C←C-N<C←C+N×C=0
[10]   R←R,[1]N↑C↑X
[11]   V←C↓V
[12]   →L1
    ∇
```

Can anyone improve on this, in terms of either algorithmic elegance or execution speed? Let us know how you get on.
