---
title: Experience of Using IBM's APL2/PC
authors:
- Anthony Camacho
volume: '6'
issue: '1'
page: '57'
unindexed: true
transcribed: 'from page images of VOL.6-NO.1-JULY-1989.pdf, pages 59–62 (printed 57–60); Claude, 2026-10-12'
review: draft
tags:
- reviews
- implementations
queries:
- "Contents line “Using IBM's APL2 on the PC”; the printed heading is “Experience of Using IBM's APL2/PC”."
- "The piece ends with “Some Additional Remarks ....” by Adrian Smith (printed 60), kept here under its own heading and byline."
- "“Setting the control variable to ⍳0” is read as iota zero in the APL font; it could be read as “10”."
---

*by Anthony Camacho*
{ .byline }

## Why I Bought It

I bought APL2/PC because of its free run time packager, hoping to be able to do some of the work which I was being asked to write in compiled BASIC in my favourite language instead. The end user, I thought, would not be able to tell the difference between one .EXE file and another. Furthermore I would be able to tell him I was doing his job with software supplied by IBM.

Of course there were some vicissitudes; the nature and resolution of these is described below. However I have to say that in general, my best hopes were realised: this product deserves success. I am plainly going to use it a lot.

## The Maths Co-Processor

I use an Amstrad portable, which has the advantage that I can take it to the client, and use it to demonstrate things on, even if he hasn't a free machine for me. I can also transfer files on the spot, even if I have not foreseen the need and don't have the file on a disk of the client's format. APL2/PC would not run on it. 1 + 1 gave an answer consisting partly of letters u with grave accents.

I sought advice and was told that some timing characteristics of the processor were not PC compatible: the co-processor emulator will not run properly with this incompatibility. I had to buy a co-processor emulator for my Amstrad. Then it worked and I have had no compatibility problem since. Incidentally I understand that even 1 + 1 uses the maths co-processor and that the strong advice given in the manual to use a co-processor is because almost any program will run as much as four times faster with one.

## Reading in Short Files

The jobs on hand each involved reading in several ASCII files of about 20K, and merging selected data from each of them into one or two output files. With BASIC this was difficult because there is insufficient array space to hold the files in memory. In APL2 the workspace available can easily exceed 400K; it depends on which auxiliary processors you load and on how much resident software you hold in memory.

To read the files in there is an auxiliary processor and a FILES workspace containing nice functions to do everything you want without having to read all about the AP. I soon established that `READFILEV` would read a file into a vector where each element was one line of the file. This form is marvellously convenient for subsequent handling.

A system function `4 ⎕AT <namelist>` returns, for each object in the namelist, the number of bytes of memory it occupies and the number of bytes of data. I soon discovered that the nesting overhead on vectors of short vectors was high. 40K of characters (I was reading Financial Times share data) can use up 100K of memory.

## The Shrinking Workspace

I encountered the first serious problem one Friday evening when there was no-one to phone for help. I had been trying out various file reading options and I got an unexpected `WS FULL`. `⎕WA` returned 67K. Where had my 400K of workspace gone?

I read the manual. I sometimes have to write manuals and count myself something of a connoisseur. This one is excellent. Every explanation I sought was in there - but not always easy to find. For example it was when reading about the packager that I discovered that APL2's internal tables can be cleared by:

```apl
)RESET                   ⍝ Clears the stack (essential for OUT)
)OUT WSNAME              ⍝ Writes WS to .ATF file
)CLEAR                   ⍝ Clear WS
)IN WSNAME               ⍝ Copies WS in from .ATF file
)WSID WSNAME             ⍝ Was CLEAR WS
)SAVE                    ⍝ Cleared tables in saved version
```

When I did this, I got back my 400K. I now do this routinely, using the .ATF and .APL versions of the workspace to back each other up. On I-APL I alternately save MYWS and MYWSX.

When I tried to repeat the fault I couldn't. It took some time to establish that as I was trying out file reading options, the workspace was mysteriously shrinking. Each time I read one of my small files in, I lost some space ... until eventually something failed with a `WS FULL`.

Next Monday I rang Dave Selby. Apparently there is at present no garbage collection process to restore to the workspace the space used by shared variables. Once a variable has been shared and retracted, the space it used is lost. In the FILES workspace such processes as `READFILEV` share the variables, read the file and then retract the sharing, so each time a file is read or written workspace is lost. Dave Selby told me of a simple work-around. Share the variable in the top level function, use it for all file reading and writing operations and only retract it at the end. Setting the control variable to `⍳0` closes the current file. This way the space is only lost once. It was necessary to amend some of the functions in the supplied FILES workspace. After that all was well. How pleasant to discover that they are all unlocked!

## No Errors Found in the Interpreter

About the APL interpreter no news is good news. I haven't tried to find a bug and haven't found one by accident. The implementation does not support the diamond for multi-instruction lines, and the standard full screen editor doesn't allow function lines to exceed 80 columns. As I like to write functions which fit easily on a screen, this suits me fine. I haven't discovered how to edit a 200 character line. Maybe it is impossible.

I have not yet used the editors supplied in the EDIT workspace. I believe that they do allow you to edit 160 column lines. Under pressure to get the job done I stayed with the editor I know and have found the del editor perfectly adequate. One thing only I miss - being able to call back the last line with ")&lt;enter&gt;". I have quite often lost a long line I was working on by displaying a variable that was longer than expected. The default session manager does not allow you to scroll back to see items which have left the screen.

## The Packager

The packager is a separate program that takes an APL saved workspace, incorporates or omits the co-processor emulator and such auxiliary processors as you specify, and produces a .EXE program. If you forget to set the `⎕LX` the .EXE run is very short! Any untrapped error or attempt to return to APL command mode in a packed program immediately returns you to DOS. The packaging process is interactive and fast. On one client's PS/2 model 70 it takes no more time than to enter the details required. Incidentally there is no )XLOAD to load a workspace without executing the `⎕LX`, so I got into the habit of pressing CTRL+Break immediately after entering the load command. This prevents the `⎕LX` executing and doesn't leave anything on the state indicator. On the PS/2 model 70 I could only rarely do this. The disk is read so fast that nine times out of ten the program would load and begin executing before I could get interrupt pressed. That hard disk is really fast!

I have used the graphics auxiliary processor with success to do experimental map distortions. I have used the printing and DOS auxiliary processors too. DOS has occasionally puzzled me because I've somehow got it into a state where the variable is reported as shared, but commands assigned to it get no reaction. The cure is to reload the workspace. I have promised to seek and provide to Dave Selby a reproducible instance of this - it may be something I am doing wrong. I haven't yet had time to keep my promise. It is not really fair to write about it before he has had a chance to help, but Vector deadlines have to be taken seriously nowadays.

## I Have a Long Way to Go with APL2/PC

I have now delivered two jobs using APL2/PC and am delighted with it. As you see I have scarcely scratched the surface of the 27 workspaces or 17 auxiliary processors. I haven't even yet used the AP124 screen manager. I will.

For anyone who wants to deliver working programs to customers fast (where the customer doesn't care how you do it) this is a quite splendid product. For me it was worth its price and the cost of the 8087 just to get away from BASIC on the jobs I've done. I hope to do many more with it.

## Some Additional Remarks ....

*by Adrian Smith*
{ .byline }

I too have a copy of this excellent little APL, and I too have liked almost everything about it. Some random thoughts to soak up this spare half page:

- if anyone would like a Hercules+ Ramfont for APL2/PC I would be delighted to pass mine on. Look out for it on the software library soon.
- AP124 works rather well. As a pressure test I pulled my GDDM-based editor off the mainframe and took it back to its 1982 status (i.e. to AP124). It runs fine; what's more you can do useful PC-ish things like pop-up help, fancy background colours, and character attributes. I much prefer it to `⎕WIN`.
- this beast deserves a better session manager! I flirted briefly with AP120, but found that it simply hobbles the PC and makes it feel like a mainframe! Like Anthony, I have retreated to using the 'raw' session instead.

Apparently it is shortly going to cost me £330 to upgrade my APL\*PLUS/PC from version 5 to version 8. For £348 I could have free runtime, nested arrays, defined operators, and a 3.5Meg workspace. Clearly there is some effort involved in making the transition, but just at the moment I feel like giving it a damn good try!
