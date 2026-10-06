---
title: Technical Editorial – Direct Definition
authors:
- Jonathan Barman
- Dave Ziemann
volume: '4'
issue: '3'
page: '102'
unindexed: true
transcribed: 'from page images of VOL.4-NO.3-JANUARY-1988.pdf, pages 104–105 (printed 102–103); Claude, 2026-10-06'
review: draft
tags:
- language design
queries:
- "“One of the most recent is presented later in this issue”: Camacho’s A Demonstration of Direct Definition (10001480), which in fact comes earlier, on p.95."
- "Slip transcribed as printed: “invoke tham all the time”."
---

by Jonathan Barman and Dave Ziemann
{ .byline }

It is generally conceded that the ‘direct definition’ of APL functions is much more elegant than the more traditional methods of defining functions in the APL workspace. Where direct definition is used, it tends to promote the development of short, easy to understand functions which can be used as building blocks to create complex systems.

Direct definition provides a way to associate an APL expression with a name in a single step. In the simplest form, a colon is used to separate the name from the expression, and the letters alpha and omega may be incorporated into the expression to represent the left and right function arguments, respectively. Alternatively, a multiple segment form can be used to define a conditional function, from which arbitrarily complex systems of interrelating functions can be constructed.

Over the years a number of different schemes for the direct definition of APL functions has been proposed. One of the most recent is presented later in this issue of Vector, and the article represents a good starting point for those unfamiliar with the idea.

Looking through the APL conference proceedings over the last few years gives the impression that APL purists and educators always use direct definition, but that APL pragmatists never use it. In fact one can almost classify papers by this method. Does the paper use direct definition? If yes, then it’s about APL, if no, then it’s an application.

The APL application programmer normally avoids using direct definition, presumably because it is not an integral part of the interpreter. Although it is fairly easy to write a pair of utility functions which will fix and display character vectors in direct definition format, it is just too much trouble to invoke tham all the time, the traditional editor being so readily available. You always have to surround your text with quotes, and at worst the utility functions are not in the workspace when you want them.

I-APL has led the way in changing this state of affairs; the ability to directly define functions in immediate execution mode is built into the interpreter. The mere fact that one can type a short function in direct definition format encourages one to do so. The power of APL as a ‘super calculator’ is greatly enhanced when it is possible to directly define short functions to solve problems, or explore a particular avenue by gradually building on existing definitions.

Direct definition is not just good for teaching or learning APL and mathematics however. Commercial APL users could also benefit by its inclusion, and at no great cost; the minimal direct definition scheme used in I-APL accounts for about 300 extra bytes of interpreter code.

A direct definition scheme need not go against the ISO APL Standard either. In the standard the immediate execution form <name>:<expression> produces an error, and so this error can be replaced by any other behaviour – in this case the definition of a function. In I-APL direct definition is a consistent extension to the APL standard.

We welcome correspondence on direct definition, and your experiences with it.
