---
title: A.I. at APL86
authors:
- Neil Mitchison
volume: '3'
issue: '2'
page: '65'
unindexed: true
transcribed: 'from page images of VOL.3-NO.2-OCTOBER-1986.pdf, pages 67–68 (printed 65–66; an APL Ltd advert fills the rest of p.66); Claude, 2026-10-05'
review: draft
queries:
- "Slip transcribed as printed: “even although”."
---

by Neil Mitchison
{ .byline }

Over the last few years “Artificial Intelligence” has become quite a buzz-phrase. And recent studies in the United States have shown that this buzz can be the noise of very large sums of money being coughed up. One good indicator of the strength of the buzz has been the creak that has recently started to accompany it, the creak of closet doors opening as big Blue allows its research workers to admit that what they’ve been doing for years would have been called A.I. if it had been done by anyone else. And that creak was heard loud and clear at APL86.

In fact AI and AI-related themes at the conference were dominated by IBM people – even although several expected participants failed to appear. And the IBMers showed a refreshing openness of mind on the question of the suitability of APL for AI work – they managed to be represented on both sides in the debate on the subject!

A working majority of the papers that *were* delivered came from Jim Brown (IBM Santa Teresa). His essential theme was that APL2 gives users all the facilities for A.I. work that LISP does, and more besides. To appreciate the force of this argument you have to realise that in the States the equation “A.I.=LISP” is more or less an article of faith. While you might not expect the Chief Architect of APL2 to be totally unbiased on a question like this, he certainly demonstrated that a great many of the traditional activities associated with A.I., such as symbolic reasoning in formal logic, can be performed very easily in APL2. He even produced a 29-line implementation of PROLOG, the Logic Programming Language, in APL2. I suspect the performance of such a PROLOG might leave something to be desired, but then IBM will always sell you a bigger computer . . . . and for those concerned with performance, Manuel Alfonseca (IBM Madrid) described an auxiliary processor for the PC which performed logical deductions, comparing reasonably with PC PROLOG.

In case you needed any further convincing that APL2 can give you everything that LISP can, we were shown by Ramiro Guerreiro (IBM Brazil) that even some of the really silly features and problems of LISP can be mimicked in APL2. But he did end up by pointing out that you were much better off writing real APL2 in APL2, and not trying to pretend you were using LISP.

A paper from Gerald Sullivan and Kenneth Fordyce (IBM Poughkeepsie) described a super-spreadsheet system which used Expert System technology to manipulate the equations relating entries in the spreadsheet, so that it could work backwards or forwards to deduce the values of any variables it had not been given. And Gert Moeller gave an elegant geometric representation of predicate calculus, as an APL array with one dimension for each predicate – though again performance might be a problem if you had a modest knowledge base of 30 predicates . . .

Overall, then, there was a fairly convincing case made that APL, particularly APL2, has a place in the A.I. world. In particular Jim Brown’s demystifying of the esoteric language of A.I. was very welcome. And I am sure that over the next few years even the quite extraordinarily conservative LISP community (mainly in the United States) is going to realise that A.I. cannot be defined as “writing computer programs in LISP”. As we see A.I. applications going out into the commercial world, APL will be used more and more. But I still do not feel (even though I did lose the debate . . .) that APL, even APL2, is powerful enough to do everything that is needed in “real” A.I. research. Psychological modelling makes strange demands of computer systems; I really believe that I think in nested data structures with multiple entry points . . .
