---
title: PL/PC “APL for All”
authors:
- N.J. Small
volume: '4'
issue: '4'
page: '52'
unindexed: true
transcribed: 'from page images of VOL.4-NO.4-APRIL-1988.pdf, pages 54–56 (printed 52–54); Claude, 2026-10-12'
review: draft
tags:
- reviews
- implementations
- language design
queries:
- "The Contents page credits Nick Small; the printed heading is “PL/PC - \"APL for All\" ?”, “Reviewed by N.J. Small”, used here."
- "Kept as printed: “O(n*2)” (for n squared); “Harris,1973”; “say to edit a new function or a text file”."
---

## PL/PC - "APL for All" ?

*Reviewed by N.J. Small*
{ .byline }

Ever since APL was first implemented as a computer language there have been many and varied suggestions as to how it might be improved. However, the introduction of changes in the language has been slow, at least as perceived by the end user (i.e. the programmer). This has been so for a variety of reasons, among which are: small user base; concern about the "purity" of the language; complacency.

It would be only charitable to assume that the last given reason is why there is no sign of a full-screen editor in certain implementations. Similarly, the desire to avoid adulterating the language explains why there are available few of the special functions needed to do in O(n) steps (as immediately perceived as possible by the ex-FORTRAN programmer) what requires O(n\*2) steps in APL (not to mention the saving in storage). Again, there are plenty of user-defined functions that require more than two parameters - and whilst using nested arrays may be fine for this in APL philosophy, they are hardly computationally efficient; (sometimes it is nice to be able to pass arrays by address, too).

PL/PC is a new variation on the theme of APL. Its main enhancements over APL - control structures (resembling those of Modula-2: for, while, if, etc.) and compilation - are hardly new in concept; see for example Harris,1973 [1]. However, time has not eroded the benefits obtainable from these features. Indeed, control structures have become more valuable, owing to their ease of programming, flexibility, and clarity, because (i) the problems that programmers are expected to solve have become more difficult and (ii) the proportion of project costs attributable to programming and program maintenance is increasing. The advantages of compilation are clear, but difficult to quantify without a non-compiling version. PL/PC performs what might be described as "run-time compilation", in the sense that a subroutine is compiled only on the first time that it is invoked after the workspace has been loaded.

Other additional features include: a built-in numeric editor; a number of new primitive functions including Bessel operators and fast Fourier transforms; integrated numeric types, including single-bit logical values, single-byte integers, and complex variables; string as well as character data types.

There are some deviations from standard APL practice: keywords are used in place of special symbols; evaluation is from left to right; index origin is always zero; embedded assignments are not permitted; the "execute" function accepts only primitive functions in its argument - strings containing the names of user-defined functions produce an error; the state indicator is cleared when a workspace is saved, so one cannot interrupt a process, save the workspace, and resume tomorrow. The first two of these, and possibly the third, may be regarded as features of the language, but the remainder are definitely restrictions.

The graphics facilities offered include turtle graphics functions, functions to draw conic sections and polygons, and functions for "painting". Thus, plotting data, drawing a picture, or doing dynamic graphics should not present too much of a problem; there is not much help, however, for the programmer wishing to do the kind of full-screen management required for menus, etc., and as actually used by the numeric editor (do-it-yourself multiple windows are necessary).

In immediate execution mode, PL/PC is considerably less friendly than it might be. In particular: (i) the results lines are not cleared of any previous display, which can lead to confusion when a command line is edited and re-executed; (ii) facilities for cursor movement and the erasing of fields are rudimentary, comparing unfavourably with those available in editing mode; (iii) there is no insert mode - only single character insertion (in contrast to the editors described below); (iv) there is no scrolling memory. Also, it is frustrating to have the screen cleared every time that an editor is invoked or a workspace loaded.

There are two editors in PL/PC, a text editor for functions and a data editor for both character and numeric data. The former is reasonably friendly and in particular has tabbing to give indentation, allowing a marked improvement in the readability of functions (there is no automatic formatting of functions); most of the facilities are controlled by function keys and, unfortunately, these are not screened from any values assigned to them using the DOS PROMPT command, which can be a problem. This text editor makes use of a temporary disk file, which always contains the last subroutine edited (in ASCII format); this last edited subroutine unexpectedly becomes fixed in the workspace if one issues the edit command without an object name, say to edit a new function or a text file; if there is no temporary file and a text file is edited, error messages are issued on leaving the editor as the interpreter attempts to fix as a subroutine the contents of the (empty) temporary file.

The data editor has a few quirks as well. It displays the contents of the variable being edited on the main part of the screen, with a field at the bottom of the screen for the contents of the current element displayed for editing. For numeric data, the format specifications for these two field types differ, which can be confusing; also, with sufficiently many decimal digits it is possible to make a number fractionally smaller and yet induce rounding up. A more serious bug is that the advertised use of break does not enable one to abort an edit session. The editing of character variables is awkward as there is no automatic movement of the cursor when a new character is typed; for string variables, editing is restricted by the size of the edit field.

The use of the two editors would be made easier if they were more similar in their use of special keys.

The manual is rather thin considering the ground that it has to cover, but detail is generally on the right side of adequacy, though someone without prior knowledge of APL might find the going heavy. In one or two cases the explanation is definitely inadequate. For example, in describing the use of the "file" command, for transferring data to or from a file, the syntax is not explained and there is an unhelpful reference to the appendix; fortunately, an example that works is given. Incidentally, this file access method is well-suited to direct access use.

There is no atomic vector in PL/PC, though the expression string (index 255) is equivalent. What would be useful in the manual is a list of the character set, if only to avoid loss of time in finding substitute keys.

As might be expected, PL/PC takes up a lot of core, leaving some 300k bytes free on a PC with 640k bytes RAM, though there is some storage reserved for subroutines; the documentation states that workspaces can be up to 330k bytes. Object sizes are limited to 64k bytes (except for virtual objects used for file access).

In conclusion it may be said that the control structures of PL/PC make it a lot easier and neater to perform certain tasks than it is in APL - tasks such as (forgive my mentioning it) looping or performing conditional calculations. Its additional functions and graphics capabilities will prove useful for certain applications. However, ease of use is all-important in the market at which this package is apparently aimed, and some improvements will be required in this direction; but most of the deficiencies described above are of a fairly minor nature and could easily be overcome with a little "polishing" of the system. Then, perhaps, PL/PC will match the claim in the blurb of being "APL for all".

Reference [1] L.R.Harris. A logical control structure for APL. APL Congress '73, pp203-210 (North Holland, 1973).
