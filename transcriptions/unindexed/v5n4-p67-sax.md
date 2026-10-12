---
title: SAX
authors:
- Michael J.A. Berry
volume: '5'
issue: '4'
page: '67'
unindexed: true
transcribed: 'from page images of VOL.5-NO.4-APRIL-1989.pdf, pages 69–79 (printed 67–77); Claude, 2026-10-12'
review: draft
tags:
- reviews
- implementations
- language design
queries:
- "Printed byline “reviewed by Michael J.A. Berry”; the Contents line gives Michael Berry."
- "The review runs printed 67–75. Printed 76 is a Renaissance Data Systems advertisement (“All APL Books in Print”, with an order form), not transcribed; printed 77 is the untranscribed introduction to the RECENT MEETINGS section (with its own contents list), which has no Contents line or file of its own. The closing statement “From: David Smith (SAX Product Manager), 4th April 1989” belongs to the review’s Availability section."
- "SHARP APL glyphs: the rank operator (printed as a jot with diaeresis) is transcribed as ⍤; the dual operator as ¨; from and merge as { and }. The merge example is transcribed as printed, “'HELLO' 2¨{} n”."
- "In the displays of m (65↓⎕av), the characters at the backtick and vertical-bar positions of ASCII print as a short bar and a semicolon-like glyph; transcribed as printed, “|” and “;”. The top borders of the enclosure boxes print as raised dashes, transcribed as “-”. The indentation of output lines is approximate."
- "In “The |FROM| function { selects cells”, the marks around FROM print as bars (perhaps braces in the APL font); kept as printed."
- "Kept as printed: “(F⍤0 and F¨> is nicely illustrated” (no closing parenthesis); “taking its input form STDIN”; “The APL work environment”; “IPSA”."
---

*reviewed by Michael J.A. Berry*
{ .byline }

I love APL, and at one time I hoped that the qualities which endear it to me would cause it to sweep the world leaving the likes of Fortran and Basic rocking in its wake.

I no longer harbour that hope. My new, more modest, desire is that APL continue to be available as an alternative to those of us who would like to use it. For even this goal to be achieved, two things must happen:

[1] APL must continue to be the best tool available for expressing algorithms in a form which is both readable and executable.

[2] APL must learn to coexist happily with the rest of the software world.

SAX makes significant progress in both of these areas.

## The Language

SAX is a partial implementation of the language defined by Dr. Kenneth Iverson in 'A Dictionary of APL' (APL Quote Quad Vol. 18, no. 1, September 1987). Readers who are unfamiliar with the dialect of APL described by Dr. Iverson, may wish to consult it for amplification of the examples in this review. The SAX implementation also includes most, if not all, of the 'bells and whistles' which have accreted to the Sharp mainframe product over the years. `⎕TRAP`, `⎕FMT`, `⎕PACK` and so on are all available.

SAX was implemented as a joint development project between I.P. Sharp associates and STSC. The software is based on the STSC Unix APL, but the language follows SHARP APL, not the STSC product.

For reasons which I will examine in the second part of this review, APL programmers are sometimes forced to use other languages in the course of their work. It is often a painful experience. All those declarations! All those loops! After using SAX for a few months, I now get much the same feeling about the other APL's I have available (STSC's APL\*PLUS/PC and SHARP APL/PC). The old familiar APL idioms now seem like clumsy circumlocutions filled with semi-colons and explicit iteration. I return to SAX with a feeling of liberation.

Much of the feeling can be attributed to the differences between any 'advanced' APL and the APL's I have available for comparison which are embellished versions of ISO Standard APL. The most important difference between advanced APL dialects and standard APL is that in the former, operators may take derived and defined functions as arguments. Without that extension, available for several years now in APL2 and its derivatives, other common extensions such as arrays of arrays are robbed of much of their power and appeal.

SAX differs from other advanced APL dialects both in the set of primitive operators provided, and in the centrality of a concept called 'function rank'. The rest of this section examines the consequences of these differences. The information on APL2 comes from 'APL2 Programming: Language Reference' (IBM 1984) and 'APL2 at a Glance' (James Brown, Sandra Pakin, Raymond Polivka. Prentice Hall 1988).

Major steps in the evolution of APL have often come about through the recognition that something already extant in the language as a special case could be described in a general way and then extended. Thus `∧.=` became part of APL because Iverson recognized that the inner product used in mathematics was just one member of a useful family of operations. Similarly, reductions and inner products existed in the language long before a theory of operators existed to explain what the / and . were doing there. Once these few special cases were recognized as members of a whole class of operators which produce functional results, the stage was set for adding new ones and extending the old ones to new domains. The resulting proliferation of operators, especially operators for functional composition, has made possible a much more functional style of APL programming. Things formerly accomplished through modification of the control flow through branching may now be accomplished by modifying the way functions are applied. The result is not only more aesthetically pleasing programs, but also programs which preserve the essentially parallel nature of many algorithms rather than obscuring it with branch points.

Function rank is another idea which has always been in the language but has only recently been formalized and generalized. A function's rank is defined by the rank of its arguments at the fundamental level of its definition. All the scalar functions are said to have rank zero. They are defined in terms of scalars, and applied to arrays of higher rank according to rules well known to readers of Vector. In SAX, these rules are extended to cover what are often called the 'mixed' functions. They, too, have default ranks. Monadic `⌽` for example, is of rank one. Its fundamental definition is in terms of vectors. When faced with an argument of rank 2 or higher, `⌽` partitions the array into cells of rank 1 and then applies its fundamental (rank 1) definition to each of them. This is precisely what scalar (rank 0) functions have always done, except that a scalar function partitions its arguments into cells of rank 0 before applying its fundamental definition.

Dyadic functions may have differing left and right ranks. Again, `⌽` makes a good example. It is said to have left rank 0 and right rank 1. In the expression `(⍳5)⌽ 5 5⍴⎕AV` each scalar cell of the left argument controls the rotation of a vector cell of the right argument. Many functions have infinite rank by default. That is, they apply to the entirety of their array argument without partitioning it into cells. Ravel is such a function, as is enclose.

Once the concept of function rank is recognized, it is natural to want an operator to control it. The `⍤` operator of SAX, with a functional left argument and a data right argument, does just that. The following examples give a feel for its use.

```apl
      m← 3 4 5⍴65↓⎕av
      m
 ABCDE
 FGHIJ
 KLMNO
 PQRST

 UVWXY
 Z[\]^
 _|abc
 defgh

 ijklm
 nopqr
 stuvw
 xyz{;

      ,⍤2 m
 ABCDEFGHIJKLMNOPQRST
 UVWXYZ[\]^_|abcdefgh
 ijklmnopqrstuvwxyz{;

      ⍉⍤2 m
 AFKP
 BGLQ
 CHMR
 DINS
 EJOT

 UZ_d
 V[|e
 W\af
 X]bg
 Y^ch

 insx
 joty
 kpuz
 lqv{
 mrw;
```

```apl
      ⍴m
 3 4 5
      ⍴⍤2 m
 4 5
 4 5
 4 5

      n←4 5⍴⍳20
      n
  0  1  2  3  4
  5  6  7  8  9
 10 11 12 13 14
 15 16 17 18 19

      (5⍴100) +⍤1 n      ⍝Add a vector to the rows
 100 101 102 103 104
 105 106 107 108 109
 110 111 112 113 114
 115 116 117 118 119

      (4⍴100) +⍤0 1 n    ⍝add a vector to the columns
 100 101 102 103 104
 105 106 107 108 109
 110 111 112 113 114
 115 116 117 118 119

      <m                 ⍝the default rank of enclose is infinite
 |-----|
 |ABCDE|
 |FGHIJ|
 |KLMNO|
 |PQRST|
 |     |
 |UVWXY|
 |Z[\]^|
 |_|abc|
 |defgh|
 |     |
 |ijklm|
 |nopqr|
 |stuvw|
 |xyz{;|
 |_____|
      <⍤2 m              ⍝Enclose the 2d cells
 |-----||-----||-----|
 |ABCDE||UVWXY||ijklm|
 |FGHIJ||Z[\]^||nopqr|
 |KLMNO||_|abc||stuvw|
 |PQRST||defgh||xyz{;|
 |_____||_____||_____|

      <⍤1 m              ⍝Enclose the 1d cells
 |-----||-----||-----||-----|
 |ABCDE||FGHIJ||KLMNO||PQRST|
 |_____||_____||_____||_____|
 |-----||-----||-----||-----|
 |UVWXY||Z[\]^||_|abc||defgh|
 |_____||_____||_____||_____|
 |-----||-----||-----||-----|
 |ijklm||nopqr||stuvw||xyz{;|
 |_____||_____||_____||_____|

      <⍤0 m              ⍝Enclose the scalar cells
 |-||-||-||-||-|
 |A||B||C||D||E|
 |_||_||_||_||_|
 |-||-||-||-||-|
 |F||G||H||I||J|
 |_||_||_||_||_|
 |-||-||-||-||-|
 |K||L||M||N||O|
 |_||_||_||_||_|
 |-||-||-||-||-|
 |P||Q||R||S||T|
 |_||_||_||_||_|

 |-||-||-||-||-|
 |U||V||W||X||Y|
 |_||_||_||_||_|
 |-||-||-||-||-|
 |Z||[||\||]||^|
 |_||_||_||_||_|
 |-||-||-||-||-|
 |_|||||a||b||c|
 |_||_||_||_||_|
 |-||-||-||-||-|
 |d||e||f||g||h|
 |_||_||_||_||_|

 |-||-||-||-||-|
 |i||j||k||l||m|
 |_||_||_||_||_|
 |-||-||-||-||-|
 |n||o||p||q||r|
 |_||_||_||_||_|
 |-||-||-||-||-|
 |s||t||u||v||w|
 |_||_||_||_||_|
 |-||-||-||-||-|
 |x||y||z||{||;|
 |_||_||_||_||_|
```

An important consequence of the availability of the rank operator in SAX is that in comparison with other advanced APL's, enclosed arrays are greatly de-emphasized. In examples I have seen from APL2, items are often enclosed solely for the benefit of the each operator. Strand notation also encourages the proliferation of enclosures. In SAX, one tends to use the array structure rather than enclose to define cells on which to operate. This approach is more flexible because each function may partition the data as appropriate to its own algorithm.

The prevalence of enclosed arrays in APL2 may also explain the decision by its designers to make some functions 'pervasive' (operating inside what is nominally a scalar) and others not. Decisions such as this are best left in the hands of the programmer. In SAX, no function is pervasive, but `FOO¨>` produces a version of foo which pervades one level. `FOO¨>` is read 'foo dual disclose.' `F¨G` derives a function which, for each argument cell, applies g, followed by f, followed by the inverse of g. The particular case `F¨>` is closely related to APL2's `F¨` (read 'f each') for pervasive functions. The difference between the two flavours of 'each' in SAX (`F⍤0` and `F¨>` is nicely illustrated using monadic `⍳`:

```apl
      (⍳⍤0) 1 3 5 7 9
 0 0 0 0 0 0 0 0 0
 0 1 2 0 0 0 0 0 0
 0 1 2 3 4 0 0 0 0
 0 1 2 3 4 5 6 0 0
 0 1 2 3 4 5 6 7 8

      ⍳¨> 1 3 5 7 9
 |-||-----||---------||-------------||-----------------|
 |0||0 1 2||0 1 2 3 4||0 1 2 3 4 5 6||0 1 2 3 4 5 6 7 8|
 |_||_____||_________||_____________||_________________|
```

SAX follows dictionary APL in cleaning up many of the messier parts of ISO APL. In SAX, one may dispense with square brackets and semi-colons completely. It is now easy to write functions which work correctly on arguments of unknown rank. The `|FROM|` function `{` selects cells from its right argument. The definitions of `↑` and `↓` have been extended so that it is not necessary to know the rank of the right argument in order to construct a meaningful left argument. Indexed assignment is made obsolete by the merge operator `}` which given a selection function, derives a dyadic function which selects elements from both its arguments to form a new result:

```apl
      n
  0  1  2  3  4
  5  6  7  8  9
 10 11 12 13 14
 15 16 17 18 19

      3↑n
  0  1  2  3  4
  5  6  7  8  9
 10 11 12 13 14

      0{n
 0 1 2 3 4
      2{0{n
 2

      'HELLO' 2¨{} n               ⍝Merge character vector into n
 0  1  2  3  4
 5  6  7  8  9
 H  E  L  L  O
 15 16 17 18 19
```

## The SAX Environment

The term 'environment' is used in two ways. The first refers to the programming environment and user interface. This includes editors, debuggers, cross-referencers, and the like. The second refers to the operating system environment of linkers, run-time libraries, etc. APL needs to do a better job of fitting into both of these environments. Twenty years ago, when commercial APL systems first became available, The APL work environment was a great leap forward. The interactive interpretive time-shared environment took much of the tedium out of programming. Because there was no existing programming environment as rich as the one which came built into APL\360, there was no reason for APL to run as part of a standard environment.

The world has come a long way in the last two decades. There are now programming environments which offer much more than any APL session manager. Unfortunately, it is not possible to run APL under most of these programming environments because APL interpreters usually come with an inseparable session manager which attempts to do everything the user might want. Even if the built-in full-screen editors and so on were not inferior to general purpose ones such as Emacs, they are different.

Differences are annoying. Before SAX, I could use GNU Emacs to program in C, Fortran, and Lisp, and to read my mail, look at usenet articles, and manage multiple shell windows, but I had to shut it all down to bring up APL. SAX properly separates the language from the environment. I can now run APL like any other UNIX process taking its input form STDIN and writing to STDOUT. This has allowed me to build an APL-Interaction mode for GNU Emacs which is modeled on the Lisp Interaction mode that comes bundled with the (free) GNU software.

I would like to donate this APL mode to the Free Software Foundation to make it part of the GNU software shipped everywhere. Unfortunately, it is not much use without a public domain screen font and printer font. It is time the owners of APL fonts realized that they are more valuable if given away. The first vendor who supplies a free X font for APL will be rewarded by having their `⎕AV` become a de facto standard.

Of course, many users may not be inclined to write their own session manager! SAX may also be run under its own session manager which includes the STSC full-screen editor. The 'union' keyboard layout used by the session manager preserves the traditional keyboard locations of ascii characters. This is important in any environment where the same keyboard device is used for more than one purpose.

Another welcome step towards integration with the rest of the computer world is that `ASCII≡128↑⎕AV`. This means that ordinary files look right when read into APL, and that APL files which avoid the second half of `⎕AV` are acceptable to any other program. Now that standard screen tools such as SunView and X support 8-bit (256 character fonts) natively, APL's large character set is no longer a problem.

The documentation came packaged as 3 sets of 3-hole punched paper suitable for inserting in the standard North American ring binder. (Try buying one of these in the UK and see how far you get! Ed.) The three volumes are titled 'Language', 'Environment', and 'System'. Although I usually dislike multi-volume documentation sets, in this case I found that my first guess as to which volume I needed to consult was almost always correct. The Language volume is the one I consulted most often. It is well written and easy to understand. The System volume covers all the `⎕NAMES`, system commands, shared variables, etc. The Environment volume covers installation, printing, and how to write your own AP's.

SAX is less successful at integrating with the operating system environment. Communication with Unix is through the traditional APL shared variables. In order to install the shared variable processor, one must recompile the Unix kernel; an operation fraught with peril. Once installed, the shared variable processor did not prove to be very robust. Hiccoughs in the local area network which only slow down other systems, seem to cause shared variable transactions to hang forever. The postscript file printing facility which was packaged with SAX had to be altered in order to run in the SUN OS (Berkeley) Unix system as it contained system 5 commands.

Large systems today are often made up of modules written in several different programming languages. In my own shop, modules written in C, Fortran, and assembler are freely intermixed. Systems written in Lisp, while not as promiscuous as these other languages, may at least call routines written in them. SAX still generally refuses to call or be called. One of the most impressive features of APL2 is the ability to write `∘.FOO` where `FOO` is a Fortran program.

The ultimate goal should be an APL processor which generates .o files which can be linked into an application in the same manner as the output of compilers for other languages. Only when that day comes will I feel that my right to continue using APL in my work is safe.

## Experience

I used SAX to build a moderately large application which generates Fortran code from test specification records. I have used this application to generate many hundreds of thousands of lines of Fortran code. Because of the nature of the application, I put great stress on the interface between SAX and Unix. I use both component files (to store the test records which include APL objects), and native files (for the Fortran output). I made a conscious effort to program in a 'new' style, using the rank operator in place of iteration and using functional composition of various kinds to derive just the function which would do what I wanted with a single application, rather than using intermediate results. At times this meant I spent longer writing the programs than I would have had I stuck to the APL vocabulary I have been using for years.

In the end, I was glad I had made the effort to master the new ideas. SAX is a far more powerful language than old-style APL. I would happily recommend this product to anyone. My understanding, however, is that it is not generally available except in quantity due to customer support considerations. My suggestion to IPSA is that they drastically lower the price and make it available with no support.

## Availability

Subsequent to receiving Michael's review, VECTOR was asked to add the following statement from I.P. Sharp Associates giving the official position on the availability of the SAX product:

> How can you get a copy of SAX? I.P.Sharp Associates is basically a wholesaler of the SAX technology. This means that only qualified educational institutions, potential large volume commercial purchasers, and prospective OEMs should contact I.P.S.A. directly. However, you can expect some announcements from selected computer manufacturers in the near future. Such third party suppliers will be making SAX available to the general public.

From: David Smith (SAX Product Manager), 4th April 1989.
