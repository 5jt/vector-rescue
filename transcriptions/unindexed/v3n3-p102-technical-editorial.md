---
title: 'Technical Editorial: Interpreters for Debuggers'
authors:
- David Ziemann
volume: '3'
issue: '3'
page: '102'
unindexed: true
transcribed: 'from page images of VOL.3-NO.3-JANUARY-1987.pdf, pages 104–105 (printed 102–103; the technical correspondence follows on p.104); Claude, 2026-10-05'
review: draft
tags:
- implementations
- development practice
queries:
- "The p.101 section introduction (v3n3-p101-technical-section.md) is taken from the identical 3:2 text, checked against the OCR."
- "Slips transcribed as printed: “a application”, “outide”, “facilties”."
---

by David Ziemann
{ .byline }

Those of us who use APL to develop applications already know that the language offers remarkable reductions in implementation time when compared with other languages. What effect does using APL have on the other phases of system development, and in particular, how helpful is APL during debugging? Let us remind ourselves of the various stages in the life of a application. Broadly speaking the application development process can be broken down into the following nine tasks:

- Determine requirements
- Specification
- Design
- Implementation
- Testing
- Debugging
- Documentation
- Maintenance
- Modification

No task is truly independent and a definitive order should not be implied – documentation for example, may well be developed in parallel with other phases.

Direct use of interpreter facilities is only strictly necessary during the implementation, debugging, maintenance and modification phases, although APL may also be used to help in other ways. (An APL prototype for example, can be considered as a specification for a final system). Maintenance and modification can be viewed as similar activities to implementation, where APL is used to build, correct and extend programs. When APL programs go wrong, the user still remains in the APL environment, and so the interpreter is necessarily used during debugging. The debugging process, however, does not usually require the construction of programs, but more often depends on the use of facilities available in immediate execution mode. The ability to view the SI stack, to look at the names and values of variables and even to change their values are all debugging tools which are ‘naturally’ available. Trace and Stop facilities are provided in most APLs as system functions or via the T-delta and S-delta syntax. Trace and Stop seem however to be the only tools available explicitly for debugging, and Stop has even found other uses outide this area.

Do these typical debugging facilities match up to the typical problems that one experiences during debugging? The sort of questions that we want to answer are; “A spurious 1 appears on the screen while my system is running. Where was it produced?”, or “Where on Earth did the variable \<flag\> get set to 17?”, or “How did this simple expression produce this strange result?”, or “My system accidentally leaves a variable \<I\> as global. In which function did I forget to localise it?”. Although the answers to such questions may usually be determined by a combination of esoteric programming combined with trial and error, the interpreter does not make it easy for us.

APL interpreters do not appear to be improving in this area, in fact there is evidence to the contrary. Well over ten years ago Xerox’s Sigma APL included the system commands )OBSERVE and )CATCH. )OBSERVE caused the subsequently executed APL expression to be ‘observed’, ie for every intermediate result to be displayed under a caret line indicating the progress at each stage. )CATCH allowed the programmer to trap the assignment of a variable. The command )CATCH X VIA FOO caused the function \<FOO\> to be executed whenever the variable \<X\> was assigned a value. Very useful indeed, but I’ve never seen it anywhere else since. It might be possible to provide this facility in systems that support exception handling by considering assignment as a type of exception.

Other desirable debugging facilities include the validation of newly defined functions for simple syntactic errors, global references and assignments and even clashes between local names such as labels with other names. The ability to ‘travel’ through the SI stack environments to examine their local contexts would also be valuable.

One objection to the provision of these, and other, debugging tools is that they result in unacceptable performance penalties during production use. If this is true, then solutions must be found which enable debugging aids to be delivered to the programmer. One approach, particularly in the PC environment, might be to provide two interpreters – one which includes a whole family of debugging facilties, and one without the features, the production interpreter. Which interpreter is used could be decided by an APL invocation option, or perhaps more flexibly by running an ‘interpreter generation program’ which would produce one of the two interpreters as its output.

It is clear that implementers have concentrated their efforts in encouraging the programmer to reduce the cost of the implementation phase of a project by providing high-performance tools such as nested arrays, full-screen I/O facilities and exception handling, among others. Now is the time for them to similarly enhance our debugging tools so that savings can also be made in this area.
