---
title: STSC APL*PLUS/PC release 6
authors:
- Martyn Adams
volume: '3'
issue: '3'
page: '51'
unindexed: true
transcribed: 'from page images of VOL.3-NO.3-JANUARY-1987.pdf, pages 53–56 (printed 51–54; begins in the lower half of p.51 after Paul Chapman’s Atari ST review, and Mark Bassett’s Macintosh review follows on p.54); Claude, 2026-10-12'
review: draft
tags:
- reviews
- implementations
queries:
- "The Contents line reads “APL*PLUS/PC release 6.0”; the printed heading is “STSC APL*PLUS/PC release 6”, “by Martyn Adams”."
- "Kept as printed: “COMPAQ seem to marketing the new machine”; “⎕PEEK and ⎕POKES”; “144 ⎕functions”; “write in ⎕code only”."
---

*by Martyn Adams*
{ .byline }

At last I have received a copy of STSC APL\*PLUS release 6.0 for the PC! I always look forward to receiving a new version of my favourite piece of software. This version’s great claim to progress is its ability to handle objects over the 64k-byte limitation but there are several other features which are really quite useful.

We quickly discovered that Grade-up and Grade-down give NONCE ERRORs when trying to process objects larger than 64k. So you can’t sort large objects. We also found that ⎕VI and ⎕FI give DOMAIN ERRORs on large objects, so you can’t validate large character arrays either.

We also tried the ASMFNS workspace and found that some of the assembler functions were slower than ‘doing it by hand’ in APL. I haven’t checked but I suspect they may have used less workspace. STSC, could we have some ASMFNS written in 80286 machine code (for our ATs) for even faster code?

The 64k-byte variable size barrier has never actually been a problem to me personally. If any object went over that size I guessed that something had gone wrong with my coding. If you only have 400k or so of workspace on a 640k machine then 64k can be a very large percentage of space devoted to one object. WS FULL has always been my problem. Nevertheless a dark cloud has been removed and if you want to process a large object then, provided you have the workspace, you do not need to chop it up any more.

This begs the question… when can we break the 640k machine size barrier? Already lots of software take advantage of extra memory. Sometimes this memory is banked so as to appear as another parallel memory space. Sometimes it sits on top of the operating system (DOS) as extended memory. I prefer the latter idea – it is easier for me to understand.

Anyway, we all wait for the latest version of DOS running on IBM’s new PC based on the Intel 80386 chip. This should break all known speed and size barriers which currently limit the PC architecture. It is rumoured to be called DOS 5.0 – we all wait with anticipation.

Meanwhile COMPAQ have beaten IBM by releasing their COMPAQ 386 to the public. It runs very, very fast. It is to IBM PC/AT what the AT was to the IBM PC/XT. COMPAQ seem to marketing the new machine as basically a go-faster DOS box. It runs a version of MS-DOS and does one or two tricks with its internals in order to maximise performance. And it is claimed to be pretty nearly 100% compatible with IBM’s PCs.

Unfortunately the latter statement isn’t strictly true. I had a chance to run APL\*PLUS release 5.0 on it. Everything seemed to work fine except that the inner product always returned 0. Even when the APL statement should have returned 1. This was very disheartening. I suspect that there may be one or two other areas which do not give results as expected. I understand that release 6 will also not run on the 386 so we will have to wait for a 386 compatible APL.

⎕WIN, which handles the PC screen as a full-screen manager, has been improved. The few improvements are very useful and can be quite significant if you program them properly. Unfortunately the new manual that comes with release 6, although nicer than the old one, is still a little confusing when it comes to describing the actions and effects of the keyboard and what characters are allowed where under what circumstances. After a little experimenting though, all becomes clear and it really isn’t as difficult as it first seems.

Function keys are now handled better, so they say, but I still find the definition of a complex data entry/edit screen a long and tiresome process.

STSC have improved the way APL starts up in “noddy” mode for the first time users. I haven’t explored these features as I consider myself a bit of a power user but I understand that for the first time user these can be really helpful.

Other nice features include ⎕CHDIR, ⎕RMDIR, ⎕MKDIR and ⎕LIBD. The first three mimic the DOS commands for changing, removing and creating directories. These are very useful. Especially useful is ⎕LIBD which allows you to dynamically set up and delete (and ⎕LIBS interrogates) the APL library structure. Before ⎕LIBD you had to use a file called APLLIBS on start-up which is a very clumsy method of defining libraries.

I do however have a gripe with the native file naming convention. In this release you can define a native file called: ‘B:DATA\FILEA.XXX’ and it is found, as one would expect, on the directory called DATA on diskette drive B:. This is much better than the old method where it was very difficult to read files which lived in directories other than the current one.

Full marks for that one – but if you specify a native file called: ‘B:FILEB.XXX’ then the APL will not look for the file where you would expect. The DOS standard is that the file should be found on drive B: in its current directory. However the APL replaces the drive B: characters with the library 1 definition (drive A: would be library 0, drive C: library 2 etc.).

This, I thought, was confusing. ‘B:’ means drive B: if there is a backslash in the file name; otherwise it means the diskette drive and directory specified in library 1 (except on alternate Thursdays?). I suppose the developers at STSC know what they are doing. I don’t.

⎕GPRINT has been upgraded to handle the LaserJet Plus printer – I haven’t had time to try this option but am looking forward to it. STSC have thoughtfully supplied a little reference manual along with the revamped documentation. Called the *Quick Reference Guide* it happens to be so full of information that it is not a very quick reference at all (it is quicker and more handy than the manual though). It is so useful that I hide it from my colleagues.

In addition to the comprehensive language description the *Quick Reference Guide* gives details of the 87 odd different authorised ⎕PEEK and ⎕POKES. Additional POKES include:

- whether or not you wish to allow low minus as negative signs in character strings when validating them using ⎕VI or converting them using ⎕FI.
- Inhibit creation of objects greater than 64k.
- Allow the display of sub-directories and/or volume ID when using ⎕LIB.
- Disable buffering of keyboard input while functions are executing when using the DOS keyboard routines.
- Make ⎕TRACE give a short form output.
- Force a return to text mode from graphics mode whenever immediate execution is entered.

Incidentally the *Quick Reference Guide* doesn’t specify all the parameters for ⎕GPRINT.

Finally, as a general point, I would just like to add that as an APL purist at heart I am disappointed that there are now 144 ⎕functions in APL\*PLUS release 6. I guess we may soon be able to forget the APL and write in ⎕code only. I also feel uneasy about the way that a lot of machine-coded functions (using ⎕CALL) are supplied as optional extras and one, BOX (which turns a character vector into a matrix), is practically compulsory.

The fact that APL\*PLUS has to use so many ⎕functions and the odd machine-coded program indicates to me that perhaps the APL should be made a little more practical. It should understand about its working environment a little more, even if it means that variables and files are one and the same thing! I do not blame APL\*PLUS for their policy of enhancing their APL by the addition of ⎕functions (in fact it is a very rich language for this reason) – but somehow I feel that something is being lost from the concept of APL as a computer programming language. I guess it has something to do with the fact that APL is really a computer implementation of Iverson’s notation. Still, full-screen management and full file management as APL primitives have their appeal.

In conclusion then, APL\*PLUS release 6 is a definite evolutionary step forward. Well worth looking at for the serious PC APL developer. I consider it a real professionals’ tool and an improvement on release 5. A lot of barriers have been lifted – roll-on release 7.
