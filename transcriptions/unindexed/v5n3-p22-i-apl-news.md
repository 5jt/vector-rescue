---
title: I-APL News
authors:
- Anthony Camacho
volume: '5'
issue: '3'
page: '22'
unindexed: true
transcribed: 'from page images of VOL.5-NO.3-JANUARY-1989.pdf, pages 24–26 (printed 22–24; within The Education VECTOR, after the ICME-6 report); Claude, 2026-10-11'
review: draft
tags:
- implementations
- education
queries:
- "Headed “I-APL NEWS”; listed in the Education Vector’s own contents (printed 17) as “The Latest I-APL News”. It follows unindexed/v5n3-p20-promotion-of-i-apl-at-icme-6.md. The I-APL Ltd order form of February 1989 that it announces (“Below is an order form”) fills printed 25; a house notice, not transcribed. Alan Sykes’s “Counting in APL - Part Two” follows on printed 26."
- "Kept as printed: “the model B with 32 of sideways RAM”, “near- clones”, “workspce”."
---

*by Anthony Camacho*
{ .byline }

Version 1.1 of the I-APL interpreter is ready. Below is an order form.

I-APL is ready for the BBC Master and for the model B with 32 of sideways RAM.

I-APL is ready for RML Nimbus (PC, AX, VX and others) and Archimedes.

I-APL is available again for PC clones. The new version will run on many near- clones which would not work with version 1.0.

We said we would have version 1.1 ready by November 1988. We are very sorry for the delay. It is not Paul Chapman’s fault. We felt it important to get the BBC version launched and couldn’t print a combined manual until we were sure how the BBC version would work.

Everyone on the mailing list will be sent an order form and this newsletter.

## BBC B and Master

You need 32K of sideways RAM to run I-APL on a BBC B. Type \*APL &lt;return&gt; and an autoload program will search for sideways RAM or shadow RAM and will load two ROM images from the disk and reset the machine. If your sideways RAM is an unusual type and this operation fails then you may have to use other methods to load the files IAPL0 and IAPL1 into ROM image. On a BBC B you should then set the mode you wish to use as in this machine it is unsafe to change mode from within APL. Then \*APL will start I-APL running.

If you have EPROM writing equipment you may write the two files into EPROMs and insert them into two sideways ROM sockets. With these installed \*APL &lt;return&gt; starts I-APL instantly.

We decided not to supply I-APL in EPROMs because the price of the EPROMs would be almost as high as the price of 32K sideways RAM. The many other benefits of sideways RAM persuaded us that very few people would be wise to choose the EPROMs. We will be sending out details of the 32K sideways RAM from Brainsoft, of which we have tried one sample. This only occupies a single ROM socket. N. B. I-APL Ltd. does not guarantee this or any other product.

## Archimedes

The Archimedes implementation is as similar to the BBC as we can make it. It is also fast.

## RML Nimbus

I-APL for PC clones now runs on the Nimbus PC and other Nimbus machines. Version 1.0 would not run even with the IBMULATOR program because it used hardware features to scroll the display and the Nimbus PC is not fully hardware compatible. Version 1.1 includes an option to use software scrolling and, though slower, this works on all the Nimbuses we tried on a visit to the RML office. Type IAPL ? &lt;return&gt; for a list of all the options.

## New Books

The instruction manual has been revised and extended to cover the BBC B, Master, the Archimedes and PC clones and near-clones such as the RML Nimbus PC.

We regret that we don’t yet have an introductory guide suitable for people who are both new to APL and not expert at their machine. We have done our best to put all the facts you need to know in the instruction manual or in the HELP files, but you may need to read them twice and study the examples carefully. The HELP function is included in workspaces such as USEFUL, PGRAPH, BBCFNS, DFILE, PGCANON and maybe others. It will read and display pages from the corresponding .HLP file. We will do our best to help if you really get stuck.

The second edition of the Tutorial is ready. A few improvements have been made.

“APL in Social Studies” is a completely new book by Tama Traberman who has taught APL in the USA. It uses simple and easy APL to do things such as drawing maps with characters. If you or your pupils find the Tutorial hard going this may be just right.

We still have some copies of “An APL Encyclopedia” by Garry Helzer in stock. Garry is working on the second edition which we will print as soon as it is needed.

Several schools now have introductory courses which use I-APL and we are hoping to document these, print them and supply them cheaply to anyone who wants to learn or teach using I-APL. Please let us know of any course you run of which we could print details. If you could write an introductory book or pamphlet we are always keen to publish suitable materials. We pay a small royalty.

## New Workspaces

BBCFNS and DFILE on the BBC and Archimedes machines are new.

DFILE gives access to a single native file at a time in the same way as the PC DFILE workspace. DFILE contains a set of functions of the same names which do the same things as the PC functions. Note that the maximum file size is 32767 bytes.

BBCFNS contains an intelligent VDU function, SOUND, ENVELOPE, OSCLI, OSBYTE, OSWRCH, OSWORD and OSRDCH. The VDU function accepts a vector of VDU arguments which are converted into the correct one or two byte form and executed. A complete drawing can be displayed with a single VDU command. Please read the HELP screens and the manual carefully and save your work before trying anything; it is very easy to make a mistake and lose control of the computer.

FSCREEN is a new workspace for PC clones. The full screen functions are implemented by holding a buffer of the characters displayed on the screen. The WINDOW, WPUT and WGET functions specify a rectangular window on the screen (the character position of the top left corner and the number of rows and columns) and reading from or writing to such a window is very fast indeed. There is a HELP file with examples.

APL LESSONS - Zdenek V. Jizba has put together a disk full of lessons in APL which run on a PC. We hope to have these converted to run on BBC and Archimedes by the time this is published.

Graphics - Morten Kromberg has written a nice graph drawing workspce which uses PGRAPH to draw scaled graphs of any function. GRAFDEMO draws sine and cosine curves. For anyone who finds the facilities of PGRAPH hard to master this example may be just the ticket. N.B. For the best effect use the graphics on as fast a machine as possible and with a fully populated EGA board, so that you can display the 256 colours. On a CGA only four graphics colours can be used and at rather low resolution.
