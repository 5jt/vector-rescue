---
title: Dyalog APL on the IBM 6150
authors:
- Adrian Smith
volume: '4'
issue: '2'
page: '53'
unindexed: true
transcribed: 'from page images of VOL.4-NO.2-OCTOBER-1987.pdf, pages 55–61 (printed 53–59); Claude, 2026-10-12'
review: draft
tags:
- reviews
- implementations
- data and files
queries:
- "Printed byline “reviewed by Adrian Smith”. The review ends on printed 59; printed 60 is a SimCorp Ltd recruitment advertisement, not transcribed, and printed 61 is the RECENT MEETINGS section page (unindexed/v4n2-p61-recent-meetings.md)."
- "The session listings are printed in an APL font, transcribed as code with ⍝ for the lamp and ⋄ for the diamond. Checked in Dyalog APL: with DATA as read, +/DATA[;1] gives 100, ⍴↑DATA[;2] gives 4 10, and ⍴⍕DATA[;2] gives 41, confirming the readings ↑ (mix) and ⍕ (format). The DISPLAY diagram is transcribed character by character as printed; its box widths are approximate."
- "In the paragraph after Lp:→(N<CT+←1)↑End, the explanation is printed in the APL (typewriter) font as part of the indented block; it is set here as an indented paragraph."
- "`⎕ELX` is printed “LELX”, the quad apparently mis-set as an L (the neighbouring `⎕ERROR` and `⎕FNS` have the quad); transcribed as ⎕ELX. On printed 59, the quirk examples are printed with a plain epsilon (‘FAT’∊S), not the underbarred one of the NEC V20 review; kept as ∊."
- "Kept as printed: “no-one want to be first in”; “If you can accept you data as nested vectors”; “knock spots of SQL*FORMS”; “opputunity”; “Sel Cursor” for “Set Cursor” in the comment on line [4]; the function SQ is displayed by ∇SQ∇."
---

*reviewed by Adrian Smith*
{ .byline }

### Acknowledgements

I must first of all thank Dyadic Systems Ltd for the loan of their APL, and IBM UK Ltd for the loan of a 6150 on which to run it. This machine also came with a copy of the Oracle database to allow me to try out the interface to SQL for data query and update.

I would also like to thank Sun Microsystems for setting up a trial of Dyalog APL on a Sun 3/140 at their Stockport office.

### Introduction

This was a system trial to which I had been very much looking forward. I well remember enjoying Dyalog's 'Mexican Snacks' at APL86, and thinking then that their APL had got so many things right, and that the 6150 was a superbly crafted machine. I had been interested in SQL, and particularly in the Oracle implementation of it, for some time; I had also been itching to get my hands on a genuine Unix box! Consequently it was with a real sense of anticipation that I wheeled in the considerable bulk of a (slightly used-looking) IBM 6150 and powered up.

### Unix and the 6150

I had known for some time that Unix was regarded within the company as a very severe barrier to the acceptance of any system. In short, if it ran under VMS we would consider it; if it ran under Unix we would consider all the alternatives first! This impression was strongly contradicted by many of my university contacts, and indeed by the occasional DEC representative when taken quietly to one side.

All I can really report is that the basic setting up was straightforward, but that I did have some help from a Unix buff who made it all look very easy. I found the DOS shell quite helpful to start with, but soon dispensed with it in favour of the tiny subset of Unix commands I needed to get by.

I wish I had a really clear crystal ball on this one; judging from the current literature many other people are in the same position. There are lots of super products under Unix, but no-one want to be first in with an operating system which may never really escape from the bounds of academia, and is known to give experts the kind of freedom that DP departments dread!

What is true without a shadow of a doubt is that the fortunes of Dyalog are currently hitched firmly to the Unix star. They will prosper in universities and in companies who have taken on board the 'workstation' concept. In VMS shops like ours, it will have a long hard slog to gain entry, let alone acceptance in the mainstream of application development.

### Dyalog: Documentation and Installation

I really ought to find a live user of Dyalog to confirm my feelings on this. The manuals look and feel really excellent; they also come with the neatest set of keyboard stickers I have seen, and Dyalog have thoughtfully included a key-puller so that you get the little blighters on straight! What bothers me is that I had the very devil of a job finding my way round the documentation. There are just too many thumb indexed separators, and the sections may have made sense to the system author; they certainly did not make intuitive sense to me!

In short this has the look and feel of a manual which has grown up with the APL, and has had new features slotted in rather ad hoc. It really would benefit from a proper restructuring with far fewer sections and better organisation within them.

Installation was superb. You simply bung in the disks, type Install and follow instructions! I only wish more PC packages were as easy.

### Dyalog - the Environment

This seemed to me to fall roughly midway between the typical mainframe session manager, and the environment on APL\*PLUS/PC. I had always to keep reminding myself that I was running on a terminal, and that although this machine looked like an overgrown PC/AT it was actually a fully fledged minicomputer, capable of supporting another 7 users like me.

It compared very well with (say) the TSO session manager, and the sort of 'cut and paste' on prior lines was helpful and easy to use. I suspect it also compared well with the typical Vax environment, although my contact with Vax's has to date been rather limited. One significant beef was the use of the Unix 'vi' editor as the full-screen editor for APL code. I'm afraid I quickly gave up on this intractable beast in favour of dear old del. Again it could just be my total lack of Unix exposure, but I found this one of the worst APL editors I have ever met!

Incidentally, the Del-editor had one very handy feature: simply typing `∇FNAME` gave you an immediate display of the function. Please could some of the other purveyors of APL take note!

The contrast with APL\*PLUS/PC was much less in Dyalog's favour here. I suppose it was inevitable that the PC, with its memory-mapped screen and instant response, would win on feel. I would have to say that users moving up to this much more advanced machine would face a considerable reduction in the feel and power of the user-interface.

### Dyalog - the APL

As I said at the beginning, there are many, many good things about this APL. It is close to being a complete implementation of the APL2 standard, complete with defined operators and most of the enhanced functionality. In a week of fairly solid testing, I crashed it once on an APL system error ... the fault was clearly mine in inventing a ridiculous piece of code!

Rather than dwelling on all the good things, let me just air a few reservations; I'm sure Dyalog (or maybe some of their users) will take me to task on these ... but here goes!

- The error-trapping behaviour seemed much too complex for its own good. I assume this comes from IPSA originally, but whatever the source, you can tie yourself in some horrendous knots very easily! Please can we have something simple and useable like `⎕ELX` and `⎕ERROR`, rather than a heap of obscure `⎕FNS`!
- I felt that there were often too many alternative ways of getting to the same end result. For example you can `⎕CR`, `⎕VR`, and `⎕NR` (nested representation) functions. Much of the original beauty of APL lay in the orthogonality of the primitive functions; Dyalog have very much taken the `⎕KITCHENSINK` approach to system functions, which leads to functional overlap, confused users, and an overloaded manual!
- the same is true of external variables. These are a wonderful concept, but they exist alongside a conventional (and very effective) component file system. In my view, they only serve to clutter the documentation, lock users firmly into the Dyalog environment, and add an unnecessary extra choice into the system design process. Sorry!
- the final one relates to the 'composition' of any dyadic operation with assignment, to give compound functions such as 'increment'.

    ```apl
          A←0
          A+←1
          A
    1
    ```

    In my looper benchmark, I had the classic line of code:

    ```apl
    Lp:→(N<CT←CT+1)↑End
    ```

    Naturally, I thought I would just improve this a bit by incrementing `CT`, rather than adding then assigning:

    ```apl
    Lp:→(N<CT+←1)↑End
    ```

    ... would anyone like to tell me why this doesn't work? Basically what happens is that this (very C-like) expression actually behaves in a fairly APL-like way. The counter is indeed incremented, but the result of the '+←' function is the right argument, i.e. it always returns 1. Oh dear!!

Enough nitpicking! To wrap up this section, I liked this APL very much, but felt that it was still being treated rather as a private research vehicle by its authors. As a result it has lots of interesting and exciting ideas (which you are unlikely to come across elsewhere), but because these ideas have never faced the hurdle of an international standards body there are some things in there which are distinctly screwball. Caveat emptor, as they say!

### Graphics

I was provided with an IBM 6154 monitor, which showed the supplied graphics demos off to good advantage. The speed was acceptable (say 10 to 20sec for a reasonably complex chart), and the imaging quality admirable. The APL code of the demo functions was clear and readable, but I'm afraid I did not have the time to explore this side of the system as fully as I would have liked.

### Linking with SQL

This was really good! The examples were clear and easy to follow, and the overall efficiency rivalled that of the native Oracle products. In fact I suspect that with a bit of thought you could write a full-screen update in APL which would knock spots of SQL\*FORMS!

Here are a few examples, to illustrate how you set up a simple query, and how the data is structured in the workspace. Please note that I was using the (default) matrix representation. If you can accept you data as nested vectors, everything runs about twice as fast, and the overhead on the array sizes is minimal.

```apl
Dyalog APL Session Manager
Mon Apr 13 08:55:52 1987
./APL.ACTIVE.WS saved Fri Apr 10 16:31:35 1987
      )LOAD ACDSQL
./ACDSQL saved Mon Apr 13 08:52:54 1987


      ∇SQ∇
     ∇ R←SQ QRY;RC;DATA;HD
[1]    ⍝ Run SQL Query and return formatted result
[2]     R←'**** NO JOY FROM QUERY ****'
[3]     RC←PREP'XX'QRY                     ⍝ Get ready
[4]     RC←OPEN'XX'                        ⍝ Sel Cursor
[5]     RC DATA←FETCH'XX' ⋄ →(0=1↑RC)↓Err
[6]    ⍝
[7]     RC HD←DESC'XX' ⋄ HD←HD[1;]         ⍝ Pick up titles ...
[8]     HD←HD,[0.5](⍴¨HD)⍴¨'-'             ⍝ ... and rule off
[9]     DATA←HD⍪DATA                       ⍝ Tag on to data
[10]    R←(⍕DATA)⍪'=' ⋄ →0                 ⍝ Finish off
[11]   Err:R←R,' RC = ',⍕RC
     ∇


      QQ
SELECT EMPNO,RDESC,DAYS FROM abs,rs
       WHERE abs.RCODE = rs.RCODE
         AND EMPNO = 7839
         AND DAYS > 10


      SQ QQ
 EMPNO  RDESC      DAYS
 -----  -----      ----
  7839  Bad Back     11
  7839  Bad Back     12
  7839  Bad Back     11
  7839  Flu          11
  7839  Flu          12
  7839  Flu          12
  7839  Wife Ill     12
  7839  Wife Ill     11
  7839  Wife Ill     12
======================
```

```apl
      OPEN'XX'
 0 0 0 0

      RES←FETCH 'XX'

      ⍴RES
2

      RES
 0 0 0 0 0  10  ACCOUNTING  NEW YORK
            20  RESEARCH    DALLAS
            30  SALES       CHICAGO
            40  OPERATIONS  BOSTON

      RC DATA←RES

      ⍴DATA
4 3


              DISPLAY DATA
         .→-----------------------------.
         ↓      .→---------.  .→-------. |
         | 10   |ACCOUNTING|  |NEW YORK| |
         |      '----------'  '--------' |
         |      .→-------.    .→-----.   |
         | 20   |RESEARCH|    |DALLAS|   |
         |      '--------'    '------'   |
         |      .→----.       .→------.  |
         | 30   |SALES|       |CHICAGO|  |
         |      '-----'       '-------'  |
         |      .→---------.  .→-----.   |
         | 40   |OPERATIONS|  |BOSTON|   |
         |      '----------'  '------'   |
         '∊------------------------------'


      +/DATA[;1]
100

      DATA[;2]
 ACCOUNTING  RESEARCH  SALES  OPERATIONS

     ↑DATA[;2]
ACCOUNTING
RESEARCH
SALES
OPERATIONS

    ⍴↑DATA[;2]
4 10

   ⍴⍕DATA[;2]
41
```

### Timings, and Impressions of the Sun 3/140

No, I'm not going to go through that benchmark table again! However it did turn over some interesting quirks in the interpreter, e.g.

```apl
'FAT'∊S       ... 15 sec for 100 executions
'FAT CAT'∊S   ... 14 sec for 100 executions!
```

The times that matter are for simple function execution, which gave the results:

```text
PC/AT :       13sec (APL*PLUS/PC)
../386:       7sec
6150  :       6sec  (Dyalog APL)
Sun   :       3.6s
```

In other words, as a single-user system the (old) 6150 is roughly comparable with a Compaq/386. The Sun is about half as fast again. Running these against a heavy second session (a 40 second SQL query was set running) increased the clock time by almost exactly 50% across the board.

The Sun was in some senses a disappointment. You can do all sorts of visually exciting things (e.g. spinning a globe in one window while APL runs in another); the snag is that APL totally ignores all the mice, icons, pull-downs and so on. Essentially it gives you a simple VT220 session in a 24 by 80 window; after seeing MicroAPL's Mac interface, I found this a real waste of opputunity.

It does, however, go like a bat out of hell!!

### Summary

I liked this APL very much indeed. I liked the 6150 very much indeed. However I must add that there are some big question marks hanging over the future of Unix (in the commercial sense), and that Dyalog seem to me to have been too willing to throw every available good idea into the same pot.

A super research vehicle, and ideal in an academic environment, but I would have a hard time getting one into the company. I hope for Dyalog's sake that this is not generally true.
