---
title: Technical Correspondence
authors:
- Peter Donnelly
- Dan Wimbock
volume: '1'
issue: '4'
page: '107'
unindexed: true
transcribed: 'from page images of VOL.1-NO.4-APRIL-1985.pdf, pages 109–113 (printed 107–111; begins below the Introduction to Contributed Articles on p.107); Claude, 2026-10-04'
review: draft
tags:
- programming techniques
queries:
- "Two letters. Donnelly answers D.J. Horton (v1n2-p101-technical-correspondence.md, spelled “Horten” here). The second, from “Dan Wimbock MBAA”, with “Proposed New APL Features” and the editors’ reply in italics, is evidently an April-issue joke; the editor asks “doesn’t that name seem somehow familiar?”."
- "Checks: in the quadREVERT example, reverting 2 assignments restores WALLY←99, and 99÷9 = 11, as printed. ZILCH [4] collapses a variable by reshaping it with `(0⌊⍴V)⍴V`, as described."
- "Slips transcribed as printed: “Mr Horten”, “ommission”, “illadvised”, “oldAPL”, “e.g )WSFNS RTJUST” (described as finding a function, though the proposal names )WSFNS for variables too)."
---

## From Peter Donnelly, 13 February 1985

Sir: With reference to Mr Horten’s letter in the October issue of VECTOR, please note that Dyalog APL provides a system variable to control the result of division by zero.

```
      ⎕DIV←0       ⍝ the default

      2÷0
DOMAIN ERROR
      2÷0
      ∧

      ⎕DIV←1

      2÷0
0
```

Yours sincerely,

Peter Donnelly, Dyadic Systems Limited, 30 Camp Road, Farnborough, Hampshire GU14 6EW

## From: Dan Wimbock MBAA, 12 February 1985

**Objets Trouvés on the Circle Line**

I found the attached document underneath a discarded copy of the Financial Times on a westbound Circle Line train at Baker Street after the What’s New for 1985 show; it appears to contain details of a few new features of a hitherto-unknown APL implementation.

Perhaps the author would recognise the document if you were able to find some room to publish these proposed language extensions, indeed perhaps it would be of interest to many members of the Association.

Might we even hope for some comment from members of the APL Standards group?

Best Wishes,

Dan Wimbock.

*Ed: The document Dan Wimbock refers to is reproduced below in the hope that it will be identified by the author. Unfortunately Dan did not provide us with his address - but doesn’t that name seem somehow familiar?*

### Proposed New APL Features

#### quadDX - The Dormant Expression

We are all familiar with quadLX, which is activated whenever a workspace is loaded, and its value for conditioning the environment. Of equal importance in many applications is the need to decondition the environment. Take as an example a graphics application, where we might have a personal need to produce text upside down in large pink letters. If we leave the terminal in this state the next user may not get overly enthusiastic about us (a subtler ruse to ensure personal monopoly of the graphics terminal is to define all colours as invisible - this unfortunately leads to large bills from the engineer’s calls).

While it’s easy enough to write functions to perform this deconditioning it’s not so simple to remember to use them (if the timesharing service just falls over you don’t get the chance anyway). Which is where quadDX comes in; in the same way as execute quadLX is the first thing to happen when a workspace is loaded, so execute quadDX will be the last task carried out when you signal disinterest in your current workspace (e.g. by )OFF or loading a new workspace).

#### quadZILCH - Prototypical assignment

Easy enough to wipe out a variable with quadEX, or to assign it a completely new value; but rather tedious to keep its name in use, retain its type and give it an innocuous value.

In the new regime quadZILCH namelist is going to take all variables named in the namelist (same construction as quadNC), and set them to have prototypical values. That is, rank unchanged but all elements of shape set to zero and the variables flagged as containing characters or numbers in their last incarnation.

#### )RECOVER - Workspace undropping

The )DROP system command is commendable in its ability to make more library space available but suffers from a degree of finality; how many times have you realised that there was something useful in a workspace you no longer have? And how often did you realise this two seconds after you dropped it?

)RECOVER saves all the heartache by restoring dropped workspaces to your library.

#### quadREVERT - Inverse Assignment

How useful a facility, to be able to gracefully unravel the results of illadvised assignment. Examine the following sequence of events:

```
      WALLY←2 3⍴'∘'
      WALLY←99
      WALLY←'A CHAR VECTOR'
      WALLY←3 4⍴'A'
      WALLY÷9
DOMAIN ERROR
      WALLY÷9
      ∧
      WALLY ⎕REVERT 2
      WALLY÷9
11
```

The left argument names a variable, while the right argument specifies how many assignments to ignore (naturally quadREVERT is origin-sensitive).

#### )WSFNS and )WSVARS - Contents of other workspaces

A frequent occurrence during the development process is the need for a specific function or variable; you have a vague idea where it might be but not an exact one. The tedious solution in oldAPL is to save the workspace you have and successively load likely candidates. Not only is this tedious, but if shared variables are in use it may not even be possible. Two mechanisms for avoiding this problem are proposed:

a)
: An extension to the present )FNS and )VARS whereby a workspace name may be specified: e.g. )WSFNS 12345 WALLY will display the names of all functions in workspace 12345 WALLY

b)
: A more active searching method in which the variable itself is specified to the system: e.g )WSFNS RTJUST displays the names of all workspaces on the system which contain a function called RTJUST

The latter may be preferable from the viewpoint of the seeking user but might need further consideration from a security aspect.

*Ed: Undoubtedly the above proposals are long overdue for standardisation, save for quadZILCH perhaps, which can be coded via the user-defined function given here:*

```
    ∇ ZILCH W;I;J
[1]   ⍝ COLLAPSE EACH VARIABLE NAMED IN <W> TO ITS PROTOTYPICAL VALUE
[2]    J←(I←1)↑⍴W←MIM,' ',W
[3]   LP:→(I>J)/0
[4]    ⍎W[I;],'←(0⌊⍴',W[I;],')⍴',W[I;]
[5]    I←I+1
[6]    →LP
    ∇
```

*where the function MIM converts a blank-delimited vector into the corresponding matrix. The variable names used above should of course be changed to reduce the chance of name clash with those in the function argument.*

*Further to Dan’s proposals, we would additionally like to offer the following suggestions:*

#### Interpreter version control

*A surprising ommission from the above (as yet unclaimed) document is the extremely useful system variable quadVER which returns the version number of the interpreter being used. Naturally it allows the user to determine at run time whether the interpreter level is recent enough to support some desired APL feature. Sometimes it is also helpful to be able to rely on a feature belonging only to a previous release of the interpreter, such as some error behaviour or a particular quirk. Assignment of the required version number to quadVER achieves this result. Application developers will now be able to protect themselves from the untoward effects of interpreter improvements, and can guarantee that their code will run even after such modifications. The careful localisation of quadVER can allow this effect to be isolated to certain sensitive areas of the system.*

*This powerful tool is open to abuse however, and great care must be taken to avoid version specifications that refer to interpreter levels that were written prior to the implementation of quadVER. If this should be done, the user will never be able to return to the current release.*

*Another use of this extremely flexible tool is of course in writing APL code that employs interpreter features that have not yet been developed. This is achieved by merely assigning the version number of the required release. The interpretation of vector assignments to quadVER is currently a topic of hot debate in certain parts of the APL community.*

#### Completeness of quadNL.

*As you probably already know, APL’s system function quadNC returns the name class of each of the names specified in its argument according to the following table:*

- *3 - Function*
- *2 - Variable*
- *1 - Label*
- *0 - Identifier available for use*

*Similarly, the system function quadNL does the reverse trick, returning all the names of specified class numbers. For example executing quadNL 3 will return a matrix of all the defined function names in the active workspace.*

*Now, regarding APL’s usual consistency and completeness concerning such affairs, it is a matter of no small surprise to discover that this feature is in fact incomplete. QuadNL always yields the correct result when applied to any of the integers 3,2 or 1, but does not work for 0! Clearly this is an oversight made in the early days of APL\360 design which needs to be rectified as soon as possible. The result from quadNL 0 should of course be a table of all the valid APL identifiers that are currently available for use in the active workspace.*

*Apparently there seems to be resistance from some of the hardware manufacturers to fix this (what can only be described as a bug), although IBM have recently expressed interest in including the feature in APL2.*
