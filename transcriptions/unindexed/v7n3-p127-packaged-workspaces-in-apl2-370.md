---
title: Packaged Workspaces in APL2/370
authors:
- Nicholas Small
volume: '7'
issue: '3'
page: '127'
unindexed: true
transcribed: 'from page images of VOL.7-NO.3-JANUARY-1991.pdf, pages 133–134 (printed 127–128; within Technical Correspondence, after Peter Branson’s letter, before PostScript Support for APL under Windows); Claude, 2026-10-11'
review: draft
tags:
- implementations
- development practice
queries:
- "A letter, “From: Nicholas Small, 3rd December 1990”, in Technical Correspondence."
- "The function name in the header of DEFAULT is printed with a lower-case prefix, read as `pwFINDVAR`; the second letter may be a capital W in this italic font."
- "Kept as printed: “namescope” and “name scope” both used."
---

*From: Nicholas Small, 3rd December 1990*
{ .byline }

At the recent meeting at which packaged workspaces were discussed, one question (or, rather, a pair of questions) that was given only fleeting consideration was: are there objects that cannot or should not be packaged?

These questions cannot be answered without consideration of how packaging is to be done - if whole applications are packaged into single workspaces then the answer to both questions is, trivially, “no”. If, however, utility functions are to be packaged separately, into a number of workspaces, then the answer is not so obvious.

To ensure that it is possible to package utilities, one must organize one’s packaged workspaces so that no function which requires the use of *EXP* when invoked from a namescope different from its own is called from its own namescope (when the use of *EXP* could result in an incorrect reference). The reason for this restriction is that, so far as I am aware, there is no way in APL2 to determine from within a function the name of a calling function and hence whether or not the calling function is in the current name scope (not that this would be desirable, because of the complexity it would introduce); the alternative of using *QNS* and passing the identity of the calling name scope to the utility is hardly to be countenanced, as this would entail changes to the calling function.

Turning now to the desirability of packaging an object, I feel that any feature that requires more than a simple application of *EXP* should militate against packaging, because simplicity should be the order of the day. Consider, for example, trying to package the function *ISPEXEC*, which is supplied by IBM to provide access to ISPF Dialog Manager services (using AP317). Requests are passed as character strings, so calls to *ISPEXEC* to browse or edit a file are not a problem, but attempts to use *VPUT* or *VGET*, to transfer variables to or from the ISPF variable pools are a different matter - AP317 will expect to find variables in the namescope of *ISPEXEC* and will return values by creating variables there. A packaged *ISPEXEC* must detect that a *VGET* or *VPUT* request has been made and determine appropriate use of *EXP*, by analysing the request. I think that this is enough to indicate that *ISPEXEC* provides an example of a function that ought not to be packaged, because of the complexity of the changes that would be necessary.

Another topic of interest is that of utility functions and operators that need extending for use within packaged workspaces, rather than just modification to ensure that they will refer properly to objects in a calling namescope.

A simple example of such a function is the following, which endeavours to ensure that a variable is available, with an optional default value, and provides a result indicating whence the value came.

```apl
     ∇ Z←DEFAULT pwFINDVAR NAME
[1]    ⍝ Look for var NAME in current namescope; if not found, look in prev n/s
[2]    ⍝ If still not found, assign value DEFAULT if provided (else undefined).
[3]    ⍝ Z is set according to the source of any value for the variable:
[4]    ⍝ ¯1 - from prev n/s; 0 - undefined; 1 - from current n/s; 2 - default
[5]     →(0≠⎕NC NAME)/0,Z←1
[6]     ⍎(0≠EXP '⎕NC' NAME)/'→0,(Z←¯1),⍴',NAME,'←EXP⊂NAME'
[7]     →(0=⎕NC 'DEFAULT')/Z←0
[8]     ⍎NAME,'←DEFAULT'
[9]     Z←2
     ∇
```

This function is useful, for example, in a print utility for determining whether or not a printer has been defined.
