---
title: Setting PF keys and Other Initialization
authors:
- Nicholas Small
volume: '5'
issue: '4'
page: '97'
unindexed: true
transcribed: 'from page images of VOL.5-NO.4-APRIL-1989.pdf, pages 99–100 (printed 97–98; within Technical Correspondence, after David Piper’s “An Ambivalent Operator”, before art10004360); Claude, 2026-10-11'
review: draft
tags:
- system interfaces
- development practice
queries:
- "A letter in Technical Correspondence, From: Nicholas Small, April 1989; the last under the heading, after unindexed/v5n4-p96-an-ambivalent-operator.md. It is unsigned."
- "The DOS batch lines are set as a plain code block. GETWS is APL*PLUS II code and was not run."
---

*From: Nicholas Small, April 1989*
{ .byline }

I have always found it very convenient for program development to have such frequently used strings as ‘)EDIT’ and ‘)SAVE’ on programmed function keys. With APL\*PLUS/PC these strings can be incorporated in the interpreter so that they are there when one starts up APL. Consequently, I was somewhat disappointed when I discovered that it is not possible to have preset PF keys with APL\*PLUS II.

We have a number of PC based APL applications, all run via DOS batch files, each of which calls the batch file which runs APL, passing to it the name of the desired workspace. The obvious thing to do to get values on PF keys, without having to edit every workspace, is to use an initializing workspace which, having done its work, loads the application workspace. The difficulty is: how to pass the name of the workspace? The technique I found makes use of the output redirection facility in DOS. My batch file to call APL\*PLUS II has the following lines in it:

```
SET TEMP= %1 %2
IF X%1==X SET TEMP=?
ECHO %TEMP% > C:\TEMP\APLWS.NAM
SET TEMP=
D:\APLII\APLSM J=D:\APLII\XAPL387 Q='8 INIT'
```

The third line writes the name of the required workspace, or ‘?’ if none was specified, to a temporary file. The last line invokes APL, requesting a quiet load of the initializing workspace. (If you need to have parameters other than the workspace name passed to the APL-calling batch file, then the latter will have to be correspondingly more sophisticated.)

The latent expression in INIT performs the initialization, which clearly need not be restricted to setting up PF keys, and then calls the following function:

```apl
     ∇ GETWS;X
[1]   ⍝ Retrieve the name of the ws the user wanted, and load it
[2]   ⍝ If nothing requested, or error, then CLEAR
[3]    ⎕SA←'CLEAR'
[4]    X←¯2↓NCREAD 'C:\TEMP\APLWS.NAM'
[5]    →('?'=1⍴X)/0
[6]    ⍎'⎕LOAD''',X,''''
     ∇
```

The function `NCREAD` reads the contents of a native file as a character string (excluding any end-of-file marker); the carriage-return and line-feed, which DOS adds after the workspace name, are dropped. The loading is done via an execute so that, if an error occurs during the `⎕LOAD`, the name of the requested workspace will be displayed (rather than just the name of the variable, `X`).
