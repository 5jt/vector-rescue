---
title: Comments on J Questionnaire
authors:
- Roger Hui
- Ken Iverson
volume: '8'
issue: '4'
page: '83'
unindexed: true
transcribed: 'from page images of VOL.8-NO.4-APRIL-1992.pdf, pages 85–86 (printed 83–84; within Featuring j, after R.H. Oates’s letter, before Comments on Power Reduction and Stirling Numbers); Claude, 2026-10-11'
review: draft
tags:
- language design
- implementations
queries:
- "A letter, From: Roger Hui and Ken Iverson, 4 February 1992, answering the report on the J questionnaire in the January Vector. The J is the 1992 dialect, in which ' is the tie conjunction; it is kept as printed."
- "The J example lines are set in the printed typewriter face; “i.” there is the iota verb."
---

*From: Roger Hui and Ken Iverson, 4 February 1992*
{ .byline }

We were pleased by the interesting articles appearing in the J Section of the January VECTOR, and by the report on the questionnaire. We offer the following comments:

1. “The Atari user did not get an editor at all. Characters can be typed on the command line, and there is a destructive backspace, but nothing else.” Terminal input/output are implemented in such a way as to avoid interference with underlying facilities. A line editor would have been available if the system had one; that line editing is not more “user friendly” on the Atari is a deficiency of the underlying system.

2. “... the Suite variable an awkward method of program control”. Since the effect of **`$.=. label`** is equivalent to *branch to label*, it is hard to see what the difficulty is. Perhaps readers are looking for something like *if then else*, *do while*, or *case* statements, matters that are better handled by gerunds combined with agenda (`@.`) and power(`^:`) as illustrated in part by the following examples from *An Introduction to J*:

    ```j
       +:'-:'*:'%: @. (4&|@<.)"0 i. 10
    0 0.5 4 1.73205 8 2.5 36 2.64575 16 4.5
       1:'(]*$:@<:) @. * "0 i. 6
    1 1 2 6 24 120
    ```

3. “... or insist on tacit definition and operators for everything.”. Whereas we encourage tacit programming, we do not agree that proscription (even of obscenities) belongs in language design. In particular, beginners in tacit programming find it useful to make an explicit definition in the form `m : d`, and then enter `m : 11` and `d : 11` to see the equivalent tacit forms.

4. “... would love graphics support.”. The current availability of the documented J Source (in C) will make it possible for others to port J to further systems, and to provide links to graphics and other resources appropriate to the particular system.

5. “... if the 640K barrier was broken” This barrier was imposed by the limitations, both technical and legal, of the C compilers previously available. J for the 386 is now compiled using WATCOM C386, and the barrier no longer exists.

6. Although McIntyre’s use of names such as `lesser_of` is valid, we would advise instead the use of names such as `lesserOf` and `LesserOf`. The reason is that a name with an underscore will be treated as a *locative*; for example, `abc_def` refers to the name `def` in the *locale* (or *file*) `abc`. Locatives are referred to and assigned in the normal manner.
