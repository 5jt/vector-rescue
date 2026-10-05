---
title: Technical Correspondence (Sullivan, Buckland, Horton, Last)
authors:
- John Sullivan
- John Buckland
- D.J. Horton
- Phil Last
volume: '2'
issue: '3'
page: '95'
unindexed: true
transcribed: 'from page images of VOL.2-NO.3-JANUARY-1986.pdf, pages 97–101 (printed 95–99; letters with editors’ replies; an advert follows on p.100); Claude, 2026-10-05'
review: draft
queries:
- "Contents list gives “Sullivan, Buckland, Horton & Last”. Editors’ replies are italic, transcribed as italic paragraphs."
- "Last’s four functions are printed in a small monospace APL face, header and body lines without line numbers or ∇; transcribed as printed. Checked by simulating each (right-to-left evaluation, index origin 1) on 500 random cases: DUPSOUT gives the unique elements in first-occurrence order, DYOTA gives V⍳V, DIOTA gives V⍳A, MEMBER gives A∊B. DIOTA alone tests group starts with `L≠¯1⌽L`, not `¯1↓(1+¯1↑L),L`; it gives an INDEX ERROR when every element of V,A is equal. Transcribed as printed."
- "Slips transcribed as printed: “on the face of,”, “Camberely”, “continous”, “util”, “inadvertantly”, “rightargument”, “fulfill”."
---

*This column features letters which are unlikely to interest readers who do not already know APL. Writers are requested to observe the requirements for the inclusion of APL code in VECTOR. All correspondence should be addressed to the Editor, who will forward technical letters to the technical editorial team.*

## From John Sullivan, 30th August 1985

Sir: Surely there must be a better way? Why didn’t you ask me this before!

Seriously, though, I enclose some code which, on the face of, seems to satisfy Andrew Wiggins’ problem from Vol 2 No. 1. I’m sorry this doesn’t match Greg Mateja’s 12-1 comments/statements ratio but as you know we programmers hate writing documentation.

Yours faithfully,

John Sullivan,  
Research Officer,  
Statistics & Market Research Section,  
Business Development Division,  
National Westminster Bank PLC,  
41 Lothbury, London, EC2P 2BP.

*Editor: John’s solution is published in ‘Surely There Must Be a Better Way’. Never mind John, 10-1 isn’t bad either.*

## From John Buckland, 27th August 1985

Sir: I was browsing through VECTOR (July, 1985), enjoying my first issue as a new member, when I saw a chance to give my favourite function ‘maximum scan’ another airing.

You may like to offer the function REDUCE, of which I enclose a listing, to Andrew Wiggins. It seems to meet the needs of his accounting problem which is described on page 97 under the heading ‘Surely There Must Be a Better Way’!

The function is just bare bones. I have omitted normal checks for empty and unequal vectors and so on, so as not to obscure its main point.

I hope this is of interest.

Yours Sincerely,

John Buckland,  
Westwood,  
9 Grove Road,  
Camberely,  
Surrey, GU15 2DN.

*Editor: John’s function is reproduced in ‘Surely There Must Be a Better Way’.*

## From D Horton, 22 October 1985

Sir: I enclose my solution to the competition ‘Wrap Up’. I was interested in this problem as I had previously faced the analogous task of inserting page headings into a continous block of text, certain lines of which must start on a new page.

I failed then and now to find a non-looping solution to the problem of not ending a page (line) halfway through a block of information (word). I shall await publication of the solutions with interest.

Yours faithfully,

D.J. Horton,  
Budget Manager,  
Pfizer Limited,  
Sandwich,  
Kent, CT13 9NJ.

## From Phil Last, 2nd September 1985

Sir: Sour grapes notwithstanding I should like to point out a few discrepancies in Dave Ziemann’s competition result: Test Your Skill.

The winning entry, as printed, does not fulfill the problem as specified. Nor is it correctly described in the text below it. Nor is the text below it correct in itself.

The list of primes must be extended to include the tenth prime, viz. 29, in order to process 10 skills.

The description refers to the required number of primes being, in origin zero, one plus the highest skill number. The code actually contains one less than the highest skill number. The required number of primes is actually equal to the highest skill number, in origin zero, one or minus ninety-nine for that matter.

The use of origin zero does not provide a neat way of ignoring the zeros used for padding. It provides a normal way of avoiding either an index error or the addition of quad-IO to each array. The leading one in the vector of primes is a (fairly) neat way of ignoring the zeros used for padding. The indexing is a mapping of skills onto primes. Zero is not a skill, one is not a prime.

Sincerely,

Phil Last,  
19 Stanley Road,  
Lower Edmonton,  
London N9.

*Editor: Glad we’ve got that straight!*

## From Phil Last, 2nd September 1985

Sir: I wrote the functions documented below several weeks ago following the production of an ad hoc fix to an unacceptably slow database indexing routine.

At the time they were envisaged as a stop-gap solution util we upgraded to VS APL release 4.

I then tried them out on a version of release 4 we had that someone had inadvertantly left lying around and found that there was no improvement in the primitives my functions are designed to replace. Performance of these functions was still far better where it counts. Well perhaps APL2 would improve matters! Not according to ‘INTERLINK’ (Published by Interprocess Systems Inc.) where it is reported that all the relevant primitives are slower with the villains of this piece being among the worst.

The problem was caused by the poor performance of membership and dyadic iota on long numeric vectors.

We had a DUPSOUT function using the traditional algorithm:

```apl
((V⍳V)=⍳⍴V)/V
```

which was very slow when the vector was large and contained many unique elements.

It seemed that a partition operation on the ordered vector could also do the job (possibly quicker) and hence this cumbersome looking DUPSOUT.

```apl
R←DUPSOUT V;L
R←(L≠¯1↓(1+¯1↑L),L←V[L])[⍋L←⍋V]/V
```

In short the negative not-equals difference of the sorted vector is re-sorted by the ranking vector and applied as a compression on the original.

The ensuing benefits are heavily dependent on the length of, and the distribution and frequency of the elements within, the argument. But for vectors of length greater than 300 elements with average frequency of less than two the new algorithm starts to show significant speed up. By the time length is 5000 with 2500 unique elements the new is taking 1 cpu second compared with 17 seconds for the old.

Taking the max scan of the product of the dupsout boolean with its index set produces a replication index vector to be applied after re-sorting to the upgrade vector.

```apl
R←DYOTA V;L
R←R[(⌈\L×⍳⍴L←L≠¯1↓(1+¯1↑L),L←V[R])[⍋R←⍋V]]
```

This result is identical with that of dyadic iota when both arguments are the same. To apply the same technique to differing arguments requires only catenation of the two, selection of that part of the result referring to the rightargument and controlling the maximum value of the result.

```apl
R←V DIOTA A;L
R←(⍴A)⍴(⎕IO+⍴V)⌊R[(⌈\L×⍳⍴L←L≠¯1⌽L←L[R])[(⍴V)↓⍋R←⍋L←V,,A]]
```

Again a membership function does the same but compares indices with the element count of the right argument returning that part referring to the left.

```apl
R←A MEMBER B;L;S;⎕IO
⎕IO←1
R←(⍴A)⍴S≥R[(⌈\L×⍳⍴L←L≠¯1↓(1+¯1↑L),L←L[R])[(S←×/⍴B)↓⍋R←⍋L←(,B),,A]]
```

These last two functions show similar speed up characteristics to those of the DUPSOUT algorithm above. The primitives perform well when either argument is small or the left argument of dyadic iota or the right of membership contains many well dispersed duplicates, and most of the other argument is actually contained in the target.

Nevertheless the overhead of upgrade, drop, max scan and indexing can be counted in a few milliseconds while the speed advantage gained with less convenient data must be counted in seconds.

> An aside: As coded DUPSOUT probably won’t work on APL\*PLUS/PC because of the re-assignment to L while the upgrade of L is still pending and the other functions will probably produce value error on R left of the index brackets as its value is assigned within them.

To conclude, the two functions DIOTA and MEMBER are either immensely superior in performance to the primitives (up to 12 times as fast in some cases, on IBM APL’s at least) or are not significantly worse, depending on the size and structure of the arguments. No mention has been made so far but it should be fairly apparent that they will work only for simple numeric arrays. In VS/APL-3 a conditional branch after a test on data type to a line which merely runs the primitive adds 2 milliseconds to the execution of the code.

What I really can’t understand is how I can run upgrade twice and still outstrip the machine code when the desired results could easily be (but manifestly aren’t) temporary values thrown out of the upgrade itself.

And why IBM (and others) haven’t done anything about this before?

Sincerely,

Phil Last,  
19 Stanley Road,  
Lower Edmonton,  
London N9.

*Editor: We hope the code has been reproduced correctly, lengthy lines of APL can be difficult to copy. Phil’s comment about running grade-up twice and still coming out faster can be explained by the fact that the time taken for sorting is approximately linear; double the number of elements and the cpu time will be only a little more than double. Searching in the way dyadic iota is implemented will tend to increase with the square of the number of elements. These functions are good candidates for the ‘Surely There Must Be a Better Way’ column. Has anyone got a solution that eliminates the second grade-up?*
