---
title: ASL at APL91
authors: []
volume: '8'
issue: '2'
page: '35'
unindexed: true
transcribed: 'from page images of VOL.8-NO.2-OCTOBER-1991.pdf, pages 39–40 (printed 35–36; within The Random Vector, before ASL: A Basic Statistics Volume Tutorial); Claude, 2026-10-11'
review: draft
tags:
- mathematics and statistics
- conference reports
queries:
- "Unsigned; written in the first person by the editor of The Random Vector (David Eastwood, per the Contents page), who introduces Jake Ansell’s tutorial that follows (art10000110). Not attributed here."
- "Kept as printed: “Jake’s article in Vector 8.1 ‘Bottom Shelf: Basic Statistics)”, with mismatched quotation mark and bracket."
---

Members of the ASL project were invited to give a tutorial presentation at APL91. Alan Hawkes, Alan Sykes and Alan Mayer from Swansea and Jake Ansell from Edinburgh gave a 90-minute team presentation on the ASL project. The audiovisual team at Stanford obviously deeply resented being asked to do anything as demeaning as audiovisuals and managed to live down to their customary low standards, but despite this the large audience of early birds who attended evidently enjoyed the presentation and were able to see most of the material being presented.

Alan Hawkes gave an introductory overview which covered the original aims of ASL and the way in which the ASL project has taken shape over the last few years. He outlined why it was originally felt that another set of APL functions for Statistical work might be beneficial to the APL community - and mentioned some of the standard works in this area (see the references I reproduce at the end of this review). Alan felt that the relative lack of success of earlier works in this area might be due to the common preference exhibited by APLers to write their own code rather than using code written by someone else. The ASL project hopes to overcome this ‘acceptance’ hurdle by the production of a definitive range of APL functions and, perhaps most importantly, functions which are supported by a large group of APL statisticians. This will lead ultimately to a comprehensive range of APL Statistics functions for all types of analysis. In a sense ASL could be thought of as a statistical equivalent of the Fortran NAG library.

At that stage it was realised that the concept should go beyond these bounds. It was necessary to create not just another set of APL software for Statistics but a wholly new concept. A unified structure and philosophy was required. It was subsequently perceived that the ASL project was attempting to create, paraphrasing APL itself, a statistical language.

There was an important realisation of the need to define the market of future users of ASL which arose out of the discussions held at the first ASL Workshop. It was fairly easy to list those who might use or be encouraged to use ASL: APL Statisticians, those teaching Statistics, Statistical Research workers, users of Statistics, etc. The real question was which group had priority? For the sound reason of knowing the group it was felt that ASL should attempt initially to satisfy APL Statisticians. Next would be college teachers of Statistics with the aim of exposing undergraduate students to ASL and hence APL. In Britain this could well be all students except those in the Arts Faculties. Once exposed, it was hoped that they would remember APL and wish to apply it in the future over a diverse range of careers. A potential consequence is the further acceptance of APL within colleges and hence its spread into other areas. This established in our minds the key aim of ASL, which is to increase the use of APL, not just within Statistics but as widely as possible. The production of a suite of good APL Statistics functions then becomes almost a by-product of the main objective.

Alan Hawkes cited a number of references to APL in statistics and I reproduce some here:

> Anscombe, F.J. [1981], *‘Computing in Statistical Science through APL’*, Springer-Verlag, New York.
>
> Douglas, J. *‘Stat APL’*.
>
> Grenander, U. [1982], *‘Mathematical Experiments on the computer’*, Academic Press, New York.
>
> Hawkes, A.G. [1990], *‘Markov Processes in APL’*, APL Quote Quad, Vol **20**, No **4**, 175-185.
>
> Smillie, K.W. [1969], *‘Statpack 2: An APL Statistical Package’*, 2nd Edition, Dept of Computing, University of Alberta Publication.

Jake Ansell then outlined the design philosophy that has evolved over the course of the ASL project and the way in which the software production cycle has been managed, paying a particular tribute to Maurice Jordan’s work in the automatic testing of APL code. For more details on these two topics, see Jake’s article in Vector 8.1 ‘Bottom Shelf: Basic Statistics) and Maurice’s paper published at APL91 (APL91 proceedings, ‘CATS - Computer Aided Testing of Software’).

The main part of the tutorial was based around live demonstrations of the three ASL Volumes now available - Basic Statistics, Generalised Linear Regression and Basic Graphics. The first two, Basic Statistics and Generalised Linear Regression are available to run under APL\*PLUS, Dyalog APL, APL.68000 and APL2/PC. Basic Graphics is currently written for Dyalog APL with ports to other interpreters under way.

Alan Sykes ran the tutorial on Regression and Basic Graphics and Jake Ansell gave the tutorial on Basic Statistics. Alan Mayer managed admirably in typing the examples as fast as the presenters introduced them.

Of the three sessions, I have chosen to include the Basic Statistics tutorial here. The Basic Statistics volume of ASL has so far had least coverage in Random Vector and this tutorial should serve as a good introduction to the scope of the functions included in the volume.
