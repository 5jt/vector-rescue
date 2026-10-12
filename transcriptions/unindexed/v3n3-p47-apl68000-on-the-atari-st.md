---
title: APL.68000 for the Atari ST
authors:
- Paul Chapman
volume: '3'
issue: '3'
page: '47'
unindexed: true
transcribed: 'from page images of VOL.3-NO.3-JANUARY-1987.pdf, pages 49–53 (printed 47–51; Martyn Adams’s review of APL*PLUS/PC release 6 follows on p.51); Claude, 2026-10-12'
review: draft
tags:
- reviews
- implementations
queries:
- "The Contents line reads “APL 68000 on the Atari ST”; the printed heading, under “Product reviews”, is “APL.68000 for the Atari ST”, “Reviewed by Paul Chapman”."
- "Kept as printed: “common to all APL installations” (a stray mark before “all”); “sotware”; “Furthur”; “occured”; “release the botton”; “The funcion CLEARWINDOW”; “It as also impossible”; “they the the reverse of this”."
---

*Reviewed by Paul Chapman*
{ .byline }

### Preface

The following review assumes some experience of the APL language and environment, and some of the concepts, such as workspaces, common to all APL installations. It also assumes at least a passing acquaintance with WIMP (windows, icons, mouse, pull down menus) environments.

### Introduction

The machine provided by MicroAPL was an Atari 520ST with high resolution monochrome screen and two disk drives. The software provided for review was sealed and obviously an end user production version. A full set of software and documentation for the 520ST was also provided.

The Atari 520ST and its younger, bigger brother the 1040ST are 8Mhz 68000 based microcomputers. The ROM-based operating system is called TOS. An Apple Macintosh-style desktop environment called GEM, which is driven by a two-button mouse (included as standard) is provided, also in ROM. On disk, Basic and Logo language interpreters are provided, as well as a word-processor called 1st word.

I concentrated my attention on the APL interpreter, and, in particular, its interface to the GEM WIMP environment.

### Getting Started

The interpreter comes in a box proclaiming “APL.68000 PROFESSIONAL PROGRAMMING LANGUAGE” and costs £170 plus VAT. The single disk provided contains the interpreter, five utility workspaces, and a demo workspace. The documentation comprises a generic APL.68000 language manual, which is provided with all implementations of the interpreter; a much smaller manual *APL.68000 for the Atari ST* containing a description of the desktop environment, and details of the workspaces supplied; a reference card; and a copy of the latest issue of *MicroAPL News*.

I had no problem getting the interpreter up and running. No special installation procedure was necessary – this is one piece of sotware which you can take home, plug in, and start using straight away. APL key stickers were already affixed to the keyboard supplied, and a set was also provided with the package. These would probably take about half an hour to put on.

My first problem came when I tried to load the DEMO workspace using the menu provided. With the mouse, I selected the “File” menu from the top of the screen, and then the “Open” item from that menu. After a little grinding from the disk, a list of the workspaces on the APL disk appeared in a new window, and I selected “DEMO” by pointing to it and “double-clicking” on it. (This piece of WIMP jargon indicates pressing the select button on the mouse twice in quick succession, which has the effect of opening the selected item.) The new window disappeared, and after a while the message “WS LOCKED” appeared in the main dialogue window. Repeating the attempt produced the same effect.

A manual )LOAD was successful, and thereafter the problem of being unable to load workspaces from the menu disappeared. Furthur investigation revealed that the problem only occured the first time after the interpreter was loaded, and before any expression had been entered. It’s an annoyance rather than a bug, and would be especially so to a newcomer, who might spend some time in the manuals trying to find out what he or she is doing wrong, or to find some other way (in this case, )LOAD) to get started.

The demo workspace illustrates very simply how APL can be used to write applications which use the WIMP environment and graphics on the ST. Typing DEMO caused the menu bar at the top of the screen to change to a list of menus defined in the application.

From the menu, it was possible to call up one of two graphic displays (a rather boring graph in one, and a number of variously shaded and patterned squares in the other), and also a “Dialog Box” which allows the further selection of options and switches (in this case a mock-up of a very simple serial port set up). The final menu item allowed me to return to native APL, either with or without clearing the workspace.

I began examining the functions in the workspace. The DEL editor worked much as expected, and used the normal APL dialogue window. Also provided is a full screen editor, which can be entered from the menu using the mouse. Upon selecting “Open fn” from the “Edit” menu, a dialogue box appears to ask the name of the function. The default is the last function edited, although perhaps a more appropriate default would be the function appearing at the top of the SI.

The editor uses the whole of the dialogue window, first of all saving the current contents, and then displaying the function selected on the screen. The editor is natural to use – I didn’t have to look in the manual to learn fancy control characters. My main reservation was that there was no distinction of lines beginning with labels or comments. This, taken together with the fact that blank lines, although they can be entered, are not retained in the function definition, made reading functions rather difficult.

I was impressed with how little code was apparently needed to interface to GEM, especially after some unpleasant experiences with the Commodore Amiga system documentation, which weighs several pounds and takes weeks to comprehend. The use of the graphics utility functions was immediately self-evident, and even the calls to GEM itself were fairly transparent.

Some of the functions, for example those used to set up menus and dialogues, took global variables as arguments. Unfortunately, the full-screen editor could not be used to examine and edit character vectors and matrices, which was an irritation.

The global arrays themselves were again mostly self-explanatory. For example, the array used to define the application menus was a character matrix, with menu titles starting in the first column, with the menu items for each title appearing below the title, on lines beginning with one space.

Typing a few APL expressions supplied sensible answers, though the overhead in display time produced from working within a window environment is slightly irritating after the memory-mapped characters of the IBM PC, particularly when scrolling. This shouldn’t bother 3278 users, however!

### A simple interactive graphics function

I now set myself the task of writing a function which would allow very simple line drawings to be produced under mouse control. The idea was to be able to point the mouse at the screen where I wanted the line to begin, then press the left mouse button and hold it down while I “dragged out” (another piece of WIMP jargon) a dotted line until I was happy with its position, then release the botton whereupon a solid line would be added to the picture.

I went to the pamphlet describing the particular features of the ST version of the interpreter, and quickly found a function called GETMOUSE in workspace TOOLS supplied with the system. This niladic function returns a 3-element vector of the current x and y co-ordinates of the mouse pointer, together with an integer from 0 to 3 indicating the state of the mouse buttons.

In the description of the STGRAPH workspace, I found a number of tools for line drawing, shape drawing and shape filling functions. LINECOLOR sets the line color, while LINETYPE sets the line style (solid and various patterns of dotted). Finally, POLYLINE draws a line or sequence of lines. The funcion CLEARWINDOW clears the window of APL dialogue, which may be restored with RESTORESCREEN.

It took twenty minutes of trial and error to set up this function, which worked quite successfully, if a little sluggishly.

### Many problems and some solutions

Many problems came to light during this process, however. Many could be dealt with by a careful study of the descriptions of the functions, but some were deficiencies in the implementation itself.

In particular, an irritating lack of elegance and consistency came to light in the use of the graphic functions.

The origin for mouse co-ordinates is the top left corner of the screen, whereas that for all graphic co-ordinates is the top left corner of the current window. Whenever it is necessary to translate from one to the other, an offset must be supplied which is supplied by the function WINDOWPOS. This can be overcome by taking the additional steps of setting a global variable called WHOLESCREEN to 1, and then calling CLIPRECT with argument WINDOWPOS.

This must be done repeatedly, since it is possible for the application user to move the window and change its size. Unfortunately, if the user does this more than once, the interpreter restores the contents of the APL dialogue to the window, wiping out any output from the application so far.

Some of the graphic objects are expressed using (x,y) co-ordinates, whilst the rest use row-column co-ordinates (ie (y,x) co-ordinates). This may be a reflection of the way the internal GEM routines work, but inelegance in the way GEM works should not be passed on to the APL programmer.

None of the graphics drawing parameters (eg. current line color, line type) can be interrogated by the programmer: the usual convention, that of making functions return the old values when given an empty argument, is omitted.

Most graphics systems allow different interactions to be specified between graphic objects to be drawn and the current contents of the screen. For example, it is usually possible to define XOR or inverting interaction, so that two successive placings of an object on the screen will have no net effect. This was essential in the simple program described above, for the purposes of drawing the “dragged out” dotted line which changes position as the mouse pointer is moved about the screen.

The graphics functions supplied allow this to be done only with solid objects like circles and rectangles (and not with their outlines), and then only some interactions are possible, eg. not AND or OR. No interactions are possible with line drawing. Eventually I chose to drag out a solid rectangle, which was ugly and unclear, but at least it was possible to do this in inverted display.

Presumably, the GEM kernel itself allows all these functions, so I can’t see any problem in providing them to the APL programmer.

Another problem which emerged was )COPYing from a nearly full or full disk. For some reason, )COPY uses temporary disk space, so the message I/O ERROR – DISK IS FULL can come as something of a surprise during a read operation.

There are all sorts of nasty little problems associated with using the cursor to select extracts for cut/copy/paste operations. For example, it is not possible to select a full line for pasting in the full screen editor.

It as also impossible to get in or out of the full screen editor without using the mouse, which is irritating. Also, the mouse pointer disappears altogether during output to the screen, so that if one moves the mouse to the menu bar during output, the position of the pointer cannot be seen.

### Documentation

I did not need to look at the APL language manual once, which is encouraging. What I was using was certainly a real APL, and worked fine.

The rather thin pamphlet describing the implementation is rather unsatisfactory. For example, the default colour numbers are described as 0 for black and 1 for white. In fact, they the the reverse of this. The descriptions of the utility functions are far from formal, and occasionally misleading because APL programmers should naturally assume consistent behaviour, since so much is made of this in the APL language itself.

### Software

I did not have time to explore the other workspaces provided. These are: MENUS for creating menus and interrogating the user’s selection of items; DIALOG for creating and executing dialogues; STFILE for accessing ST native files; and TOOLS which contains miscellaneous functions for programming function keys, setting keyboard translation, etc.

It really looks to me as if the STGRAPH workspace was cobbled together with the rest in a hurry to create a product. It also looks as if little or no beta testing of the product has been performed. I set out to review the usefulness of the implementation rather than to try and break the interpreter, and yet I found several bugs, inconsistencies and irritations within a very short time.

The functions I explored are simple to pick up and use, but this is more a result of lack of flexibility than careful and logical design. Much of GEM is inaccessible from APL, except through the use of custom-written shared variable processors and careful study of the GEM system manuals. If MicroAPL were to consider expanding the range of functions for accessing GEM in the future, they would find consistent extensions to the functions already defined very difficult.

### Conclusions

APL.68000 is a sound product as an APL interpreter, and competes fairly well in functionality and very well in price with its main rival on micros, STSC’s APL\*PLUS/PC.

The ST is used both at home and in business. Much of its appeal over, say, the IBM PC must be in its price for home users, and in the GEM environment for business. It is difficult to see which market APL.68000 is aimed at. Its price is too high, compared with that of the hardware it is running on, to be attractive to home users, and the lack of a full interface to GEM would put business users off.

For myself, if I owned an Atari ST, I would spend my money on a C compiler so that I could have full access to GEM’s facilities. If I had to recommend the purchase to a business user committed to the ST, I would point out the need to spend money on having a custom interface produced by a systems programmer if any serious use of the GEM environment were planned.

APL is praised for its natural extension to graphics environments, but MicroAPL have a long way to go to provide the access to GEM an APL graphics programmer needs.
