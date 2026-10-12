---
title: News from Sustaining Members
authors:
- Gill Smith
volume: '10'
issue: '4'
page: '11'
unindexed: true
transcribed: 'from page images of VOL.10-NO.4-APRIL-1994.pdf, pages 13–18 (printed 11–16); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
queries:
- "Printed byline “Compiled by Gill Smith”."
- "Names printed in the APL font (system functions, object classes and properties, `)IN` and `)OUT`, the RAIN and CAUSEWAY workspaces and `APL⋄385`) are set as code."
- "Kept as printed: “the bang up-to-date user-interface features”; “The names of your functions, and variables”; “built in to the user interface”; “NVSP-API” at the start of Soliton’s last paragraph, “NSVP-API” later in it."
---

*Compiled by Gill Smith*
{ .byline }

## Dyadic Systems Ltd

Dyadic is pleased to announce Version 7 of Dyalog APL/W. This is a major release packed with many new and exciting features.

One of the most important additions is the ability to use `⎕WC`, `⎕WS`, `⎕WG` etc. to access Visual Basic (.VBX) Controls alongside regular Dyalog APL/W ones with exactly the same syntax. This facility gives the Dyalog APL/W user access to hundreds of commercially available Visual Basic add-ons including various Graph, Grid and Spreadsheet controls; even an OLE client control. In addition, users can add controls of their own design written to the .VBX standard using ordinary Microsoft development tools. Access to Visual Basic Controls is implemented using a general mechanism for defining a new Class of object and will be extended to other standards (e.g. OLE 2.0) and user-defined Widgets under OSF/Motif in the future.

Dyadic believes that with the new VBX interface, coupled with the enhanced DDE and Clipboard support and the facility to access any Windows DLL with `⎕NA`, it alone can truly claim to offer an "open" APL for Windows.

A new `MDICLIENT` object is provided to allow users to develop applications that use the *Multiple Document Interface* (MDI) style. All of the standard MDI behaviour is supported. In addition, `FORM` class objects can now be children of other `FORMS`, and so can be used as general-purpose containers for a wide variety of uses and effects.

Version 7 now provides a variety of `EDIT` field types that perform built-in validation and formatting of numbers, dates etc.

Other new objects include `TOOLBAR`, `STATUSBAR` and `STATUSFIELD`. The `TOOLBAR` is normally displayed at the top of a `FORM` and is used to manage a scrollable set of tool buttons. The `STATUSBAR` is normally displayed at the bottom of a `FORM` and contains one or more `STATUSFIELDS`. These can have pre-defined meanings, such as monitoring the state of the Caps Lock key, in which case they are updated automatically by the interpreter. Alternatively, their contents can be set directly by your application.

All controls can now have associated `TIP` and `HINT` properties. A `TIP` is a (usually) short description which gets displayed as a pop-up message when the mouse pointer dwells over a control, for example over a `BUTTON` in a `TOOLBAR`. A `HINT` is typically a longer help message which gets displayed when an object (e.g. a `MENUITEM`) is selected. A `HINT` would normally be displayed in a `STATUSFIELD`, but you can in fact use any object capable of displaying text.

The `TAB_BAR` manages a scrollable set of `TAB_BTN` objects which allow you to provide a notebook-style interface similar to that used by the latest versions of Excel, Paradox, Lotus 1-2-3 and Organiser.

These new objects have all been designed to allow Dyalog APL/W users to build APL applications that provide the bang up-to-date user-interface features of other popular Windows products; and, because all the work is done for you by the interpreter, with the same snappy performance.

All `FORMS` and Controls now have a `3D` property that can be used to achieve a variety of 3D effects. Furthermore, as the value of this property is by default inherited from the parent, setting `3D` on the `SYSTEM` object '.' automatically gives a 3D appearance throughout your entire application.

Version 7 now provides support for *Windows Metafiles* so that you can incorporate fully scalable graphical pictures into your application. Not only can you import Metafiles, but you can also create them from primitive graphical objects and export them (via file or the ClipBoard) to other Windows applications. A final touch is a facility to disassemble an imported Metafile so that you can edit or rearrange its components within APL.

The *APL Session* has not escaped our attention and a *StatusBar* and *ToolBar* have been added. Furthermore, the components of the Session are directly accessible as named objects whose properties can be set by `⎕WS` and read by `⎕WG`. New menus, menuitems, tool buttons, status fields etc. can easily be added using `⎕WC`, and unwanted items can be removed with `⎕EX`. Menuitems and tool buttons can action predefined "system" operations (such as [load] and [edit]) or can execute any APL statement. This allows you to configure the Session exactly as you want and you can dynamically change it (manually or under program control) to suit particular workspaces. For example, your `⎕LX` could add special menuitems and/or tool buttons, fully equipped with `TIPS` and `HINTS`, to run particular functions in a statistics workspace.

The names of your functions, and variables may be displayed in a separate dialog box and are therefore only a click away for editing, copying to the clipboard, etc. A number of improvements have been made to the *Editor* and *Tracer* and fully CUA-compliant select/cut/paste operations have also been implemented.

Finally, Dyadic has introduced *Namespaces*, a major new enhancement to Dyalog APL. A Namespace provides the means to gather together a collection of objects and acts as a separate "context" in which functions (including callback functions) can be run. This means that local functions and variables can be hidden from the rest of the workspace. The implementation of Namespaces, which encapsulate code and data, is a further step towards Object Oriented technology and is intended to provide major benefits for APL developers. Further information on this exciting new feature will be available by the time you read this announcement. Please call Dyadic for details.

To coincide with Version 7, Dyadic is publishing "*Outer Products*" a catalogue of third-party tools and add-ons for Dyalog APL. Some "Outer Product" software, such as the `RAIN` graphics workspace and `CAUSEWAY` GUI design tool from `APL⋄385`, are also included in the Version 7 package.

For details concerning price and availability, please contact Dyadic or your local Dyalog APL supplier.

## Insight Systems

On the Product Front, we are concentrating our efforts on the design and implementation of a new version of SQAPL which will support Microsoft's Open Database Connectivity (ODBC) specification. The primary design goal is to provide an interface which is completely compatible with our existing product — so that our customers will be able to take advantage of ODBC drivers to access dBase, Btrieve, ACCESS, Paradox (or even Excel and Comma Separated Variable text files) — plus any remote databases for which they have an ODBC Driver — and still be able to use SequeLink without changing the application. SequeLink is still a preferable solution for many Windows environments, and the only solution under Unix and OS/2 or if an APL Server is required.

An ODBC Driver is now available for SequeLink, so SQAPL users will have the option of using SequeLink "direct" or via the ODBC driver. TechGnosis have also announced an ODBC version of their Open Server. Once we have an ODBC SQAPL Client out the door, we will start work on an ODBC version of the SQAPL Server. With an ODBC SQAPL Server, developers will be able to make APL-Coded Databases or Analytical Tools running under Unix available to any development environment which supports ODBC.

We would also like to intentionally leak an official rumour that our ODBC interface will probably be bundled with an upcoming version of Manugistics' APL\*PLUS III product. Due to the relatively long lead time for Vector, we have agreed to leak the news despite the fact that the agreement is still under negotiation. By the time you read this, you should be able to contact Morten Kromberg at Insight Systems or Paul Clements at Manugistics to hear whether we succeeded!

On the APL Consulting and Education Front, the Danish market is suddenly full of renewed interest in Graphical APL systems. It seems that many organizations who still use APL on a Mainframe are finally ready to "Downsize" — to the extent that APL courses have become a profitable activity! There was a waiting list for our first "Introduktion til Windows Programmering med Dyalog APL/W", so we will be scheduling several courses during 1994 and will also be "porting" the course to APL\*PLUS III.

We would like to take the opportunity to announce that Insight Systems is now an IBM Software Partner, so we now market and support IBM APL2 and APL2-based products (like AGSS) under OS/2 and Unix. We are also authorised RS/6000 resellers, and thus capable of delivering complete "turnkey" systems based on the RS/6000 and any one of APL2/6000, APL\*PLUS II/UNX and Dyalog APL/X. We look forward to cooperating with IBM Denmark in providing APL and Client/Server expertise to their APL2 customers!

## Manugistics Inc

Manugistics Inc is very pleased to announce the commercial release of APL\*PLUS III for Windows. An Advance Release (version 1.0) began shipping on February 25, and the general availability release (version 1.1) will be ready by the time this issue of Vector appears. Please contact Cocking & Drury in the UK, your local APL\*PLUS dealer, or Manugistics for specific information.

APL\*PLUS III is a 32-bit Windows system that runs on Windows 3.1, Windows for Workgroups, and Windows NT. It is a completely Windows-hosted program, with a graphical development environment that has been designed to be a pleasure to use, whether for personal APL computing or for building Windows applications to be used by others.

APL\*PLUS III includes a graphical development environment, event-driven user command processor, a built in graphical debugger, and a visual form editor that allows the programmer to build a graphical user interface by drawing with the mouse. The graphical user interface facilities are supported by fast, built-in system functions, and include regular and 3-dimensional versions of forms, frames, buttons, checkboxes, scrollbars, etc. Graphics support is also built in to the user interface, as is support for Dynamic Data Exchange. System functions provide access to Windows libraries and any other software packaged in a Windows DLL.

The design of APL\*PLUS III reflects our views of how APL needs to evolve to become a competitive alternative to other languages in this decade and beyond. The GUI development facility follows a strictly object-oriented structure, using "classes", "events", "methods", and "properties". The APL interpreter is based on the well-proven technology of APL\*PLUS II, but the heart of the system has been replaced with an event-driven architecture. Control structures, in the spirit of C or Pascal, provide an alternative to the "spaghetti code" that afflicts too many APL programs.

APL\*PLUS III will continue to evolve rapidly both in terms of new tools and in enhancements to the language itself. We welcome the comments and suggestions of Vector readers.

## MicroAPL Ltd

In the previous issue of Vector, MicroAPL announced APL Level II for the new PowerPC Macintosh computer. APL Level II was one of the first dozen applications to be seen running native on the new PowerPC Macintosh. To coincide with the launch of this important new computer, we have been upgrading our entire family of Macintosh APLs. The details of the upgrade are being finalised as this is written, but we have a fairly clear idea of what the upgrade will include.

The APL programming environment has been enhanced, combining ideas from our APL.68000/X for the RISC System/6000 and features found in Mac System 7 as well as improving our conformance to Apple's System 7 user-interface guidelines. We have added support for Apple Events — multiple workspaces may be launched simultaneously at startup. New Print menu items allow prints of workspace listings as well as contents of the APL window. The new Windows menu identifies multiple APL sessions by workspace name and we have added `)IN` and `)OUT` menu items for workspace exchange. The number of simultaneous APL tasks supported has increased as has the number of edit windows and user-defined windows. Improved user-preferences allow control over such items as default workspace sizes, window positions and sizes and default libraries.

APL programmers can now easily access hierarchical menus and popup menus and we have further improved event handling facilities with new event types. Amongst the new support workspaces is the PLOTMAC workspace for high-level business graphics. The interpreters themselves have been upgraded in line with our latest versions for the RISC System/6000 and PowerPC and a number of small bugs in the Level II interpreters have been fixed.

MicroAPL was instrumental in forcing the APL world into issuing free runtime licences and we have now included with our Mac APLs a packager to make stand-alone applications which may be distributed royalty-free.

Pricing details for the upgrades will be announced in April but we can confirm that we will be offering substantial incentives to upgrade to our Level II versions of APL as well as maintaining our policy of realistic pricing across the board.

## Soliton Associates Limited

Version 21 of SHARP APL for VMS, shipping in 2nd quarter 1994, offers improved performance and operability, in particular of the SHARP APL File System. For SHARP APL MVS applications requiring 24-hour 7-day availability, Version 21 offers new functionality supporting continuous on-line operation of databases stored in the SHARP APL File System.

Version 4.03 of SHARP APL for UNIX, shipping in 2nd quarter 1994, provides a powerful new Intrinsic Function facility, allowing secure and efficient access from SHARP APL for UNIX to software implemented in other languages.

Version 4.04 of SHARP APL for UNIX, shipping in 3rd quarter 1994, will support Sun's Solaris 2 operating system, allowing major multi-user SHARP APL applications to execute on large Symmetrical Multi-Processor Sun Unix platforms.

NVSP-API, an application programming interface for Soliton's Network Shared Variable Processor technology, will provide access from non-SHARP APL software to local or remote Network Shared Variable Processors, allowing, for example, non-SHARP APL client software to access local or remote SHARP APL server software, including SHARP APL for MVS Auxiliary Processors. Initially, NSVP-API will be available under UNIX and Microsoft Windows, and will support access to Network Shared Variable Processors operating under UNIX and MVS.
