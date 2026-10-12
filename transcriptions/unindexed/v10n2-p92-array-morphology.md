---
title: Robert Bernecky ‘Array Morphology’
authors:
- Anthony Camacho
volume: '10'
issue: '2'
page: '92'
unindexed: true
transcribed: 'from page images of VOL.10-NO.2-OCTOBER-1993.pdf, pages 94–95 (printed 92–93; an APL93 talk report in Recent Meetings, after “From Trees into Boxes”); Claude, 2026-10-12'
review: draft
tags:
- conference reports
- performance
- implementations
queries:
- "Not on the Contents page: one of three APL93 talk reports following unindexed/v10n2-p87-workshop-a-gui-standard-for-apl.md on printed 91–94. Byline “reported by Anthony Camacho”."
- "Kept as printed: “if, for example they passing a localised variable”; “or, if one is unwilling to change the language to be able to deduce these”; “to use to the full its ability”; “Mike Jenkins' model of domino”."
---

*reported by Anthony Camacho*
{ .byline }

Robert Bernecky began by saying that the reputation APL has for being slow is deserved when it is used to do lots of operations on small arrays. This is because to execute a line of APL it is necessary to perform a series of initial tasks:

- Analyse the syntax and put together the actions to be performed
- Decide the storage needed and allocate it
- Check the type of each variable and intermediate value for compatibility
- Check the form of each argument to ensure they conform as necessary

These tasks vary little with the size of the variables; for a line which processes scalars the overhead is almost as much as for a line handling large arrays. When the large array has to be handled by a parallel processor there is extra overhead involved in deciding which bits to send to which processor and this adds to the overhead. According to Bob the average number of elements in an array is only about seven to fifteen. This is far too few for efficiency and the initial tasks require more work than the processing of the variables. It is therefore important to write APL so as to use to the full its ability to process large arrays and this becomes even more important when one wants to use a parallel processor efficiently.

To use a parallel processor in APL one has either to change the language by adding declarations of variable sizes and types or, if one is unwilling to change the language to be able to deduce these. Without changing the language it is possible to add lines of code which force a variable to take a particular type and if, for example they passing a localised variable which is not used the analyser can also omit the processing implied in the line from the final compiled code. The deduction can be done on a preprocessing pass through the code. It is surprising how much can be deduced from perfectly ordinary code; for example in Mike Jenkins' model of domino the Bernecky analyser was able to deduce 100 out of 175 types. Adding just a few declarations raised the total to 174.

The C code produced by the analysis and compilation is often not nice. No-one would want to maintain it. It may then be optimised and after that it may be unrecognisable.

In general the improvements that J makes to the APL syntax reduce the deductions that can be made. For example the APL expression `X[1;]` enables the analyser to deduce that *X* has rank 2 but the J equivalent does not give the equivalent information. However declarations by additional code which the analyser can recognise as omittable are equally easy in J and some features of J enhance compilability.
