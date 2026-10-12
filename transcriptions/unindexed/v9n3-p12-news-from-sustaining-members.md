---
title: News from Sustaining Members
authors:
- Gill Smith
volume: '9'
issue: '3'
page: '12'
unindexed: true
transcribed: 'from page images of VOL.9-NO.3-JANUARY-1993.pdf, pages 14–18 (printed 12–16); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
queries:
- "Printed byline “Compiled by Gill Smith”. The piece ends on printed 16, the lower half blank."
- "Cocking & Drury: the new command is given as `)PLOT`."
---

*Compiled by Gill Smith*
{ .byline }

## Manugistics Inc

A lot of feverish activity has been happening at Manugistics over the past few months, mostly involved with preparing our latest version of APL\*PLUS II. What started out as a small project grew rapidly into a major release as we saw the potential in our Windows support.

We started shipping Release 5 of APL\*PLUS II early in December. The new release features an easy-to-use GUI Toolkit that makes building Windows applications an enjoyable task. The interface is much faster than Release 4 and your applications will run quickly and smoothly. New DDE tools include powerful sample functions to exchange data and instructions with EXCEL, Lotus 1-2-3 and Visual Basic. Functions to access the Common Windows Dialogs (like Open File Name and Choose Colour) are included.

Perhaps the most generally useful new feature is the fully integrated Debugger which is by far the most advanced APL debugging tool ever offered. It lets you step through your code primitive by primitive, literally watching your data change as it passes through the functions. The new Watchpoint feature lets you have the Debugger stop whenever a particular variable is referenced or modified, in a specific function, every so many iterations, and/or when a particular condition is met. Breakpoints can be set on lines and on statements within lines and execution can be recommenced from any stop point, even between two primitives.

For the DOS environment we have incorporated Rick Butterworth’s Graflib tools which make it easy to convert your data into line and bar charts, complete with titles, legends, gridlines, etc.

Among the other features you will find our new Install Program which will get you up and running on Version 5 in no time.

Now that Version 5 is out the door, we are turning our product hats to a new version of APL\*PLUS/PC. Version 11, due out early next year, will include the Screen Interface Toolkit introduced in APL\*PLUS II Version 4 and a Free Runtime .EXE Builder that will let you distribute your APL\*PLUS/PC applications at NO COST.

In addition to the PC release, we will be working hard on Version 5 of the UNIX product. Watch this space for more information.

One of our major goals for 1993 is to bring APL to a much wider audience. Chris Lee has just finished touring Europe and the U.S. presenting to any current APLers. Next year the emphasis will be on taking the message to the (slightly larger) group of non-APLers out there. To start with, we will be presenting APL\*PLUS at the Software Developer’s Conference in San Francisco in February. This will be attended by programmers who are currently using C, Pascal et al. We think that they deserve to see what array-oriented thinking can do to their productivity. We are also presenting a tutorial at the Application Developer’s SIG (SIGAPP) at the ACM’s annual conference in Indianapolis, Indiana. These two events will just be the start of a major campaign to broaden the market for APL.

Lastly we have just published our first Catalogue of Third Party Software. We are sending this out with all new software orders so you will get one when you get your next upgrade. If you have software you would like to see in the next catalogue, please contact us for more information.

Happy New Year!

## MicroAPL Ltd

Users of our APL.68000/X product for the IBM RISC System/6000 should all have received notice of the latest upgrade by now (to version 1.2). This upgrade has been triggered by the recent release of AIX 3.2 which has been a significant upgrade to AIX and appears to have fixed a number of bugs, some of which had been showing through into APL.68000/X. The ‘look and feel’ of Motif programs has also been improved. Our new version of APL.68000/X also includes an improved interface to routines written in ‘C’, BDF-format fonts for X-terminals and a number of minor bug fixes. The somewhat thorough nature of the AIX upgrade means that older versions of APL.68000/X must be upgraded to version 1.2 if you are upgrading AIX. As is our usual practice for most of our routine upgrades, we are not charging for this upgrade.

In what is planned as the first of a series of free seminars, we recently held a half-day seminar on ‘Trends in Workstation Technology’. This included an overview of the workstation market given by Richard Nabavi which looked at the various leading hardware platforms as well as the new generation of operating systems. We contrasted the various GUIs in use and assessed the significance of the RISC System/6000 in the workstation market. Readers of Vector who would like copies of the notes for this seminar should contact David Eastwood at MicroAPL.

We shall be starting 1993 with one or more seminars devoted to the new breed of GUI development tools that are now available and offering practical advice based on recent Windows projects we have undertaken. Again, contact David Eastwood for details.

## Cocking & Drury Ltd

By the time you read this we will have shipped upgrades to APL\*PLUS II Version 5. This new version includes the APL Graphical User Interface Toolkit — a collection of object-oriented tools that make it easy to design and build Windows applications. There is also a complete interface to the core Windows system libraries, so you can reach beyond the APLGUI tools and use any of the hundreds of Windows library routines. The Windows interface is profoundly faster than in Version 4 thanks to a new virtual device driver. DDE utilities enable easy linking of APL\*PLUS II with other Windows applications.

The DOS user is not forgotten however — the same package still allows the creation of DOS programs, and OS/2 users will now find APL\*PLUS II running happily in an OS/2 DOS session. Other enhancements include the APL\*PLUS II Debugger — a visual code debugger woven into the fabric of the interpreter. The GSS\*CGI interface has been revised and is now supplemented by a new `)PLOT` command which provides high-quality line and bar charts in any workspace. And those of us who struggled somewhat with Version 4’s installation will be delighted to hear that an automatic installation routine is included which allows for the selection of components.

Manugistics are rightly pleased with the outcome of the effort they have put into this new version and we are co-operating with them in a special offer for existing users of APL\*PLUS/PC, who may purchase copies of APL\*PLUS II Version 5 at the discounted price of £700 plus VAT.

Anyone who missed the talk by Chris Burke of Strand Software, Canada, on the use of APL in actuarial work can obtain a free copy of the utility disk by calling us on 071-436-9481. Cocking & Drury now have available a range of tools to assist in the migration of APL2 mainframe workspaces to APL\*PLUS II 386/486 — we have seen a number of companies reaching the decision to ‘down-size’ their APL use to networked PCs for greater flexibility (and considerable CPU savings!) and we have developed these tools in response to that need.

Levels of APL consultancy work and of APL training have remained fairly constant over the last 12 months. Our consultants are kept busy in other fields of endeavour and we have recently expanded into a new area of training which is proving to be very popular.

## Dyadic Systems Ltd

Dyadic is pleased to announce the availability of Dyalog APL/W Version 6.3 for Microsoft Windows. This release contains a host of new features of which the following are a selection:

- A new system function, `⎕NA`, is included. This provides access to Windows Dynamic Link Library (DLL) routines. Using `⎕NA`, you can call any DLL subroutine (16 and 32-bit) using familiar APL function syntax.
- Full control over foreground and background colours in GUI objects.
- Five new “graphical” objects, namely:

    POLY (lines, polygons, filled areas)<br>
    MARKER (for marking a series of points)<br>
    RECT (rectangles)<br>
    ELLIPSE (ellipses, circles, arcs, pie-charts)<br>
    TEXT (arbitrary graphical text)

    All the graphical objects allow you to draw several things at once (and with a single name). By default, APL handles repaint for you and automatically resizes your graphics when the user resizes a FORM. Graphical objects can even be dragged and dropped! A new GRAPHS workspace containing high-level “business graphics” functions is also provided.

- New BITMAP, CURSOR and ICON objects which you can import from standard files or create from APL matrices.
- Ability to associate bitmaps with BUTTONs and MENUITEMs, so that you can provide customised “toolbars” for your users. You can specify individual bitmaps for when a BUTTON is “out”, “in” and “inactive”, so that the appearance of the BUTTON changes instantly when it is pressed.
- A new FILEBOX object which provides a standard Windows 3.1 File Selection dialog box.
- Direct support for the printer via a new PRINTER object which provides for the output of device-independent text and graphics.
- Clipboard support via a new CLIPBOARD object. This allows you to move data to and from the Windows Clipboard under program control. The CLIPBOARD object has a CHANGED event so that your application can react immediately when (for example) the user copies data to the Clipboard from Excel or from any other Windows application.
- A new AUTOCONF property to simplify control over resize. An object can now optionally enable/disable automatic resize independently on both itself and on its children.
- The coordinate system has been extended to provide user-definable coordinates and origin.
- Improvements to the handling of CHANGED, GOT_FOCUS and LOST_FOCUS events to simplify validation etc.
- A new general DATA property allows you to associate any APL array with an object. This reduces the need to use global variables to communicate between callback functions.
- `⎕NQ` has been extended to allow you to send a message to an object instantly, bypassing the normal queue. If there is one, the appropriate callback function is invoked at once. This extension permits an even more “object-oriented” approach to programming.

Version 6.3 completes the definition of the Dyalog APL GUI support, and will be the basis for the forthcoming OSF/Motif, OS/2 and Windows NT implementations. These versions of Dyalog APL will be 100% compatible with one another and with Dyalog APL/W for MS-Windows. This will permit true portability of APL applications between different GUIs and different hardware platforms.
