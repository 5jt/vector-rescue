---
title: Second Generation APLs - Comment on Items in Vector 5.4
authors:
- N.J. Small
volume: '6'
issue: '2'
page: '7'
unindexed: true
transcribed: 'from page images of VOL.6-NO.2-OCTOBER-1989.pdf, pages 9–11 (printed 7–9; within General Correspondence, after the section’s introductory note); Claude, 2026-10-11'
review: draft
tags:
- language design
- implementations
- development practice
queries:
- "A letter, the only one in General Correspondence, From: N.J.Small, 23rd August 1989. It comments on the editorial and on the articles by Peter Cyriax and Ajay Askoolum on APL*PLUS II in Vector 5.4. Signed “N.J.Small, Assistant Research Manager, IT Systems Support Section, National Westminster Bank”."
- "Names in the APL font in the running text (⎕FMT, ⎕HNAMES, ⎕LIBD, DTFN, LFFN, WSTOFILE, PCFILETOWS, PCFILES, WSSHOW, SCAN, FNREPL, ⎕INKEY, ⎕KEYW, ⎕WGET, ⎕POKE, ⎕SEG, ASMFNS) are set as code."
- "Kept as printed: “a two column-mixed array”; “speeded”; the result of `1 2 3(/)¨'ABC'` shown as `A BB CCC`."
---

*From: N.J.Small, 23rd August 1989*
{ .byline }

## Editorial

One way of avoiding Heffalump traps is not to behave like a Heffalump - though this may be easier said than done!

The problems described arise from the freedom that strand notation and mixed arrays allow. One defensive action that can be taken is to tighten up one’s programming style, in particular by using unnecessary parentheses to make programs more readable - especially in distinguishing functions and data. Another thing one can do is to learn how to get out of the traps as quickly as possible. A little experience soon teaches one to recognize the type of trap one has fallen into, and that is usually half the way to escaping.

Whilst these new facilities are of great value in creating data structures, I feel that they are not really what one needs to solve the problem of passing multiple parameters to functions. I consider it very inelegant to have to start each function by unpacking parameters (though erasing the original parameter is probably unnecessary with the new data-pointer storage systems). An alternative solution has already been implemented in embryo form in the system function `⎕FMT` used by STSC and Sharp; a typical function header would look something like:

```apl
  (Z1;Z2;Z3) ← (L1;L2) FN (R1;R2;R3;R4)
```

(In most cases, left arguments would not be required.)

With data structures one needs to take care if they are to contain more than a small number of elements at the highest level, as there is an overhead of about 30 bytes per element in mixed or nested arrays, plus a performance penalty. For example, if one has a long list of serial numbers and names, these should be stored as a two-element nested vector, rather than as a two column-mixed array.

## Article by Peter Cyriax on APL\*PLUS II

1. Peter must have a disk cache or some other facility stored in the upper end of extended memory; with all of a 1 Mbyte extended memory available one will get a workspace of 915120 bytes.
2. As described in the Release Notes, when `/` and `\` are used to the left of another operator there is an ambiguity, because the symbols represent both functions and operators. To indicate interpretation as a function, enclose the symbol in parentheses. For example:

   ```apl
         1 2 3(/)¨'ABC'
   A BB CCC
   ```

   (Without the parentheses one gets `NONCE ERROR`.)
{ type="i" }

## Articles by Ajay Askoolum on APL\*PLUS II

1. There is a SYSHELP.SF file, but in my release (1.1) it contains very little. For a help file to be accessible, it must be named as the desired help file in the configuration file; perhaps STSC would like to reinstate the system variable `⎕HNAMES`. As F1 is generally recognised as the standard key for help, one could use the keyboard mapping facilities to give this the same value as Alt-F6. Alternatively, one could put one’s home-made help facility on F1 and map Alt-F6 to that.
2. The function `⎕LIBD` is implemented, as in APL\*PLUS/PC, so libraries may be defined from within a program, as well as in the file CONFIG.APL.
3. The session manager editor does not add extra bytes to DOS files.
4. A numeric editor will be incorporated in release 2 of the interpreter.
{ type="i" }

Migration from APL\*PLUS/PC will, in most cases, be fairly straightforward. Appendix D of the reference manual gives details of the differences between the systems, and suggests three ways of transferring code (none of which will move locked functions):

- Source Level Transfer (functions implementing the Workspace Interchange Convention of the international APL standard)
- functions `DTFN` and `LFFN`, which use a native file
- functions `WSTOFILE` and `PCFILETOWS`, using an ASF file (this is the quickest and easiest option). The workspace `PCFILES` contains functions to transfer component files and workspaces in either direction between the two systems (though, obviously, one cannot transfer mixed or nested arrays to the PC version).

File and workspace transfer is very quick and easy; modifying code may take somewhat longer, but can be speeded by making use of the supplied functions `WSSHOW`, `SCAN`, and `FNREPL` to find and edit strings within functions.

Of course, it helps to migrate one’s utility workspaces first, so that functions from them can be copied into application workspaces.

The following are probably the items that will most commonly necessitate code changes:

- `⎕INKEY` - the code for Home has changed, and there are some new codes
- `⎕KEYW` is no longer supported
- `⎕WGET` - type 4 is no longer supported (use type 3 instead)
- `⎕POKE` - a few of the more obscure values do not get translated by the interpreter, and `⎕SEG` must be null or 0
- functions from the `ASMFNS` workspace should be replaced by their new versions.

In general, the better one’s programming practices and the more modular one’s code, the less work one will have to do. Now may be the time to write those little cover functions that one always intended to do tomorrow!

Yours sincerely,

N.J.Small  
Assistant Research Manager  
IT Systems Support Section  
National Westminster Bank
