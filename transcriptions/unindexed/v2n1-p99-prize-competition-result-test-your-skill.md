---
title: 'Prize Competition Result: Test your Skill'
authors:
- David Ziemann
volume: '2'
issue: '1'
page: '99'
unindexed: true
transcribed: 'from page images of VOL.2-NO.1-JULY-1985.pdf, pages 101–106 (printed 99–104; the result of the competition set in v1n3-p126-prize-competition-test-your-skill.md; the next competition follows on p.105); Claude, 2026-10-05'
review: draft
queries:
- "Checked: the printed JOBS SKILLSMATCH CONS result follows from CONS and JOBS, and SM1–SM10 as transcribed, simulated in Python/NumPy (index origin as each function sets it), all give exactly that result."
- "SM2 is printed `R←⍉∧/∨⌿ 3 4 2 1 ⍉A∘.=B,0`."
- "SM6 [3]: the ⍉ is printed before `¯1 0↓`; [2] `C←C×C≤N←1+⌈/,J`."
- "SM9 [5]: the outer-product function is printed as ∧ overstruck with ~, read as ⍲ (nand), which the logic requires. [4] `→lab←1+(SK⍴Loop),End,CT←1` builds a vector of line numbers to branch through."
- "The Sharp APL function is printed SMIPSA (I, not 1), though it is a variant of SM1; transcribed as printed."
- "SMIPSA: Sharp APL’s ‘ON’ (rank) operator is printed as a ∘ with a dieresis (⍤ in later notation): `R←⍉∧/J∊⍤ 2 1 C,0`. Transcribed with ⍤."
- "SMAPL2 is printed `R←∧/¨((⊂[2]J)~¨0)∘.∊⊂[2]C`; in the scan the each operators show as dieresis marks over the preceding space."
- "Slips transcribed as printed: “invariable means”, “Bengt Lingren”, “are following boolean identities”, “<SM1>under”."
---

by David Ziemann
{ .byline }

To recap; in our mythical consultancy we have a consultants’ skills matrix as follows:

```apl
      CONS
1 2 3 7 0 0
1 3 7 9 2 6
7 9 0 0 0 0
1 6 5 3 9 0
```

where each row represents one consultant’s skills, and each non-zero entry is an index into a table of skill descriptions. For example, the third consultant(row) has skills 7 and 9. Notice that zeros are used to pad the shorter rows. Also, we have a matrix of skills required for the jobs that have arisen, as follows:

```apl
      JOBS
1 2 3
7 9 0
1 4 0
1 3 0
1 6 3
```

The fifth job (last row) requires skills 1, 6 and 3 for example, and it could in fact be performed by the fourth consultant, who has the relevant skills. The problem was to write a function to generate a boolean matrix that specifies which jobs can be tackled by each consultant, i.e.:

```apl
      JOBS SKILLSMATCH CONS
1 1 0 0
0 1 1 0
0 0 0 0
1 1 0 1
0 1 0 1
```

Although the consultancy has a potentially large number of customers and employees, the number of unique skills is low, and it was stated that contestants would not be penalised for offering solutions that assumed no more than 10 skills. Workspace demands, execution speed, robustness and intelligibility were named as the factors that would determine the winners.

Over thirty functions arrived before the closing date, with entries from many parts of the planet. The entries split into two broad types; those that are ‘pure’ APL solutions and work for any number of skills, and those that take the hint about 10 skills being acceptable. The majority of functions entered fall into the first group, so let’s deal with them first. The ‘do it all at once’ approach was used by many entrants; Henri Schueler from Toronto, and Bengt Lingren from Sweden for example, produced the following solution, as did four others:

```apl
    ∇ R←J SM1 C
[1]   ⍝ <R> IS SKILLS MATCH MATRIX FOR JOBS <J> AND CONSULTANTS <C>
[2]    R←∧/[2]∨/J∘.=C,0
    ∇
```

A column of zeros is catenated to the consultants’ skills table to ensure that everyone has skill zero, which is used for padding in the jobs matrix. The OR reduction of the outer product shows whether a consultant has each of the required skills, and the AND reduction tells us if the consultant has ALL the required skills.

Simon Barker from London came up with this noteworthy algorithm:

```apl
    ∇ R←A SM2 B
[1]   ⍝ <R> IS SKILLS MATCH MATRIX FOR JOBS <A> AND CONSULTANTS <B>
[2]    R←⍉∧/∨⌿ 3 4 2 1 ⍉A∘.=B,0
    ∇
```

The following origin-independent answer was submitted by David Quas from Bristol:

```apl
    ∇ RES←A SM3 B
[1]   ⍝ <RES> IS SKILLS MATCH MATRIX FOR JOBS <A> AND CONSULTANTS <B>
[2]    RES←(¯1↑⍴A)=+/[1+⎕IO]∨/A∘.=B,0
    ∇
```

These concise and elegant algorithms work for any number of skills, but can be very greedy on workspace for large arguments - after all, an outer product followed by a couple of reductions invariable means that we are throwing a lot of generated data away. This waste can be avoided by coding a looping solution, where the correctly shaped result matrix is initially established and its contents modified within the loop. This approach was taken by David Quas who provided us with this function:

```apl
    ∇ RES←A SM4 B;⎕IO;N;MAX
[1]   ⍝ <RES> IS SKILLS MATCH MATRIX FOR JOBS <A> AND CONSULTANTS <B>
[2]    RES←((1↑⍴A),1↑⍴B)⍴0
[3]    ⎕IO←1
[4]    B←B,0
[5]    N←0
[6]    MAX←1↑⍴B
[7]   LOOP:→(MAX<N←N+1)/0
[8]    RES[;N]←∧/A∊B[N;]
[9]    →LOOP
    ∇
```

Notice that one iteration is needed for each row in the consultants’ table, and that a leading loop test is performed to ensure the correct behaviour with empty arguments. This type of looping solution takes less workspace to run and can also be very much faster than the previous examples. In the words of Simon Barker:

> “The fact is, the looping solution is much faster (and more space conserving) than the one-line non-looping solution. To me, the non-looping answer is the most pleasing because it is the purest of all APL solutions and its conciseness could not be achieved in a million years in any other language. Sadly, however, the thoroughness of comparison between elements of different arrays is its downfall, as a lot of what it does is not necessary.”

Some people decided to make use of the fact that the required solution needed to work with no more than 10 skills. Curtis Jones from San Jose, USA and Phil Last from London discovered that a substantial speed-up over the one-liner could be achieved by coding

```apl
    ∇ Z←J SM5 C
[1]   ⍝ <Z> IS SKILLS MATCH MATRIX FOR JOBS <J> AND CONSULTANTS <C>
[2]    J←∨/[2]J∘.=⍳10
[3]    C←∨/[2]C∘.=⍳10
[4]    Z←J∧.≤⍉C
    ∇
```

Similar techniques were used by Henri Brudzewsky from Denmark and Ken Goralski from London, while Richard Fisher replaced line 4 by

```apl
Z←~J∧.∨⍉~C
```

which runs faster on some APLs. A conceptual leap was made by Greg Mateja from Hartford, USA who provided this:

```apl
    ∇ R←J SM6 C;N
[1]   ⍝ <R> IS SKILLS MATCH MATRIX FOR JOBS <J> AND CONSULTANTS <C>
[2]    C←C×C≤N←1+⌈/,J
[3]    J←⍉ ¯1 0 ↓(N⍴2)⊤+/(J≠0)×2*J
[4]    C← ¯1 0 ↓(N⍴2)⊤+/(C≠0)×2*C
[5]    R←J∧.≤C
    ∇
```

Greg receives a special commendation for supplying a 52-line function, all but 4 lines of which were comments! The technique he uses involves raising 2 to the power of all the non-zero elements in each skills matrix, and summing. Converting the result back to base 2 then provides a boolean with every possible skill flagged either 1 or 0. (This works because there is no significance to a skill appearing more than once in a row). These matrices are then directly compared by using the appropriate inner product. Note that the method fails when the jobs skills numbers get too large. Mike Day from London used a similar approach, but discovered that in MIPS APL the code fragment

```apl
(1-W)∧.∨Y
```

runs more quickly than the more obvious

```apl
W∧.≤Y
```

His function is as follows:

```apl
    ∇ R←JOBS SM7 CONS;MAXSKILL;TWOS;TWOPOWERS;⎕IO
[1]   ⍝ <R> IS SKILLS MATCH MATRIX FOR JOBS <JOBS> AND CONSULTANTS <CONS>
[2]    TWOPOWERS← 0 1 ,×\TWOS←(MAXSKILL←⌈/(,JOBS),(,CONS),⎕IO←0)⍴2
[3]    R←(1-⍉TWOS⊤+/TWOPOWERS[JOBS])∧.∨TWOS⊤+/TWOPOWERS[CONS]
    ∇
```

Mike also presented another ‘mathematically attractive’ algorithm, which he included for comparison; instead of powers of 2, a base 3 representation of the sums of powers of 3 is used. If any 2s exist in the base 3 representation then there must be a mis-match between the required and actual skills. In fact, this will work for any base higher than 2, but larger numbers would soon cause problems with precision. Again, time and memory requirements are excessive. For interest, here is such a function:

```apl
    ∇ R←J SM8 C;M;⎕IO
[1]   ⍝ <R> IS SKILLS MATCH MATRIX FOR JOBS <J> AND CONSULTANTS <C>
[2]    M←1+⌈/(,J),(,C),⎕IO←0
[3]    R←⌈0,3*⍳M
[4]    R←2∧.>(M⍴3)⊤(R[M]-+/R[J])∘.++/R[C]
    ∇
```

Well, we’re almost home and dry, but first, another looping solution. This one was sent in by Adrian Smith, who accepts that he is ineligible to enter, being on the VECTOR working group! It’s interesting because it loops not on the rows of the jobs matrix, but on the number of skills in it. Here it is:

```apl
    ∇ MAT←JB SM9 CN;lab;CT;SK
[1]   ⍝ <MAT> IS SKILLS MATCH MATRIX FOR JOBS <JB> AND CONSULTANTS <CN>
[2]    SK←⌈/,JB
[3]    MAT←((1↑⍴JB),1↑⍴CN)⍴1
[4]   Loop:→lab←1+(SK⍴Loop),End,CT←1
[5]    MAT←MAT∧(JB∨.=CT)∘.⍲(CN∧.≠CT)
[6]   End:→lab[CT←CT+1]
    ∇
```

A modification would need to be made for correct operation with empty arguments. Adrian would like to know if anyone else has a sufficiently warped brain to have tackled it this way (Frankly I doubt it…). He says:

> “It took from Potters Bar to just north of Peterborough to dream this up, and most of the way to Doncaster to check it! As long as you meant that hint about small numbers of skills, you will find that it goes quite quickly. It would be fascinating to see some timings against one of the jot.epsilon solutions from APL2!!”

The idea of using the skills matrices as indices into a set of numbers, as seen above, can be pursued further. What happens if instead of indexing from powers of 2 or 3, we use prime numbers? By taking the product over such a set we create a unique number; one that could only have been generated from the original set. Let’s look at a simple example. Can the consultant with skills 1, 3, 7, 9, 2 and 6 attempt the job for which skills 1, 6 and 3 are required? The products over the set of primes are as follows:

```apl
      P←1 2 3 5 7 11 13 17 19
1 2 3 5 7 11 13 17 19
      ×/P[1 3 7 9 2 6]
16302
      ×/P[1 6 3]
33
```

Because these results are unique, if the first divides exactly by the second, then its original set is a superset of the second’s. And so the answer to the above question is “YES” because

```apl
      33|16302
0
```

Here is the complete function:

```apl
    ∇ Z←J SM10 C;P;⎕IO
[1]   ⍝ <Z> IS SKILLS MATCH MATRIX FOR JOBS <J> AND CONSULTANTS <C>
[2]    ⎕IO←0
[3]    P← 1 2 3 5 7 11 13 17 19 23
[4]    Z←0=(×/P[J])∘.|×/P[C]
    ∇
```

This trick is often colloquially referred to as ‘Goedelisation’, after the mathematician Goedel. The use of index origin 0 in the function provides a neat way of correctly ignoring the effect of the zeros used for padding — the contribution to the product being 1. You have to be sure to use enough primes for the index expressions to succeed; in origin-0 this is one plus the highest skill number. The algorithm is elegant, concise and economic; the amount of space required is dependent on the size of the result, not on some intermediate structure. It is also the fastest, as can be seen by the sample timings below.

Three contestants supplied this function; they are Richard Fisher from Epping, Australia, Derek Wilson from York and Bernd Fohlmeister from Cologne, Germany. Phil Last’s entry was very similar and Greg Mateja provided a close variant. Deciding how to split the booty is a soul-searching torment, but the postmark dates decide, and so £30 goes to Richard and £10 each to Derek and Bernd.

The following timings were made on version 4.1 of APL\*PLUS/PC on an IBM PC with the 8087 enabled. A JOBS matrix of shape 20x5 and a CONS matrix of shape 40x6 were used, to yield a result shape of 20x40. All times are in seconds:

```
SM10   2.3
SM4    4.0
SM9    4.4
SM7    4.6
SM5    5.3
SM6    6.1
SM1   13.4
SM3   13.4
SM2   16.6
SM8   22.4
```

This ordering of functions according to speed may vary when other APL interpreters are used, but \<SM10\> will probably remain unbeaten.

Two respondents provided solutions written in non-standard APL. This Sharp APL answer was sent in by someone whose surname is Baronet (first name unfortunately unreadable), from Toronto, Canada:

```apl
    ∇ R←J SMIPSA C
[1]   ⍝ <R> IS SKILLS MATCH MATRIX FOR JOBS <J> AND CONSULTANTS <C>
[2]    R←⍉∧/J∊⍤ 2 1 C,0
    ∇
```

The right argument of the ‘ON’ operator is the integer vector 2 1 which controls the way the membership function is applied; the 1 means that the function is applied to vectors of the matrix right argument. The 2 causes the left argument, J , to be treated as a matrix (which in this case it is anyway). Apparently the function runs about 40% faster than \<SM1\>under Sharp APL, and clearly takes less room.

Norman Thomson (whose tutorial on APL2 nested arrays appears later in this issue) suggests the following APL2 function:

```apl
    ∇ R←J SMAPL2 C
[1]   ⍝ <R> IS SKILLS MATCH MATRIX FOR JOBS <J> AND CONSULTANTS <C>
[2]    R←∧/¨((⊂[2]J)~¨0)∘.∊⊂[2]C
    ∇
```

The tilde symbol represents the function ‘without’. Norman also thoughtfully provides us with this translation into something he calls APL1:

```apl
    ∇ R←J SMAPL1 C;X
[1]   ⍝ <R> IS SKILLS MATCH MATRIX FOR JOBS <J> AND CONSULTANTS <C>
[2]    R← 1 1 2 ⍉(+/X)∘.=(X←⍉∨/(⍳10)∘.=J)+.∧∨/(⍳10)∘.=C
    ∇
```

although he says he’s sure that other VECTOR readers could do better.

What a shame we don’t have an interpreter that can run all flavours of APL - we could come up with some interesting comparative timings!

Please note that the author’s original comment lines have not been included in the functions as presented here.

By the way, the above functions show a great deal of creativity in the area of the inner product operator, with all these products appearing at least once:

```apl
∨.∧
∧.≤
∧.∨
∧.>
∨.=
∧.≠
+.∧
```

Also worthy of note are following boolean identities, which the competition has revealed:

```apl
A∧.≤B   ←→   ~A∨.∧~B   ←→   (1-A)∧.∨B
```

Studying how they work can help us to better understand APL and to use it more effectively, and is well worth the effort involved.
