---
title: News from Sustaining Members
authors:
- Gill Smith
volume: '13'
issue: '1'
page: '12'
unindexed: true
transcribed: 'from page images of VOL.13-NO.1-JULY-1996.pdf, pages 14–17 (printed 12–15); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
queries:
- "Printed byline “Compiled by Gill Smith”. The news ends on printed 15; printed 16 is a Dyalog APL advertisement (“The Definitive APL for Windows”), not transcribed."
- "Kept as printed: “(:IF,:WHILE,:FOR, etc.)”; “OCX’s”; “focussed”; “outwith”; “APL+win 1.8” in the heading “Free to 1996 Purchasers of APL+win 1.8”."
---

*Compiled by Gill Smith*
{ .byline }

## APL2000 Inc (Bloomsbury Software Ltd)

### APL+Win Release 1.8

Release 1.8 of APL+Win is now available to APL Windows developers. This release adds the popular Windows95 controls on all three Windows platforms: NT, Win95 and Windows 3.\*. These include a Treeview control for managing hierarchical lists, a Listview control to help organize columnar data, a Selector control to provide Property Sheets and Wizards as well as Statusbar, Spinner, Trackbar, Imagelist, Progressbar, and Owner Drawn Buttons. These controls can enhance your application and give it the new interface clients expect. This release also adds: tooltips, an unlimited number of user-defined data properties, the ability to suppress events from firing when changing properties under program control, and many other useful properties and events.

To enhance your application when run under Win95, we have added the ability to call 16-bit DLLs and long file name support. Long file names may also be used in NT. None of your existing code needs to change, but using these extended file functions you will get better file error messages (in your native language), wildcard searching for filenames, as well as allowing meaningful names. While these extended file functions work under Windows 3.\* (so you only need one workspace) the 8.3 character limit still applies. In addition to all of the above, they also allow you to give APL component files any extension you wish.

As if all this wasn't enough, we're also including a set of APL widget workspaces and utilities. These include an AVI movie player, calendar and date controls, and a workspace to demonstrate the new controls and widgets.

### APL+Win Release 2.0: Free to 1996 Purchasers of APL+win 1.8

Later this year we will be releasing version 2.0 to take further advantage of Windows95 and NT. This newer version will include all of the above as well as adding support for OCX/ActiveX controls. ActiveX is the newest standard for adding custom third-party controls to your application. We will also be including new and enhanced widgets including a RichEdit control and an APL forms browser. To give you the opportunity to get started NOW with Windows95, version 2.0 will be free to all users who purchase version 1.8 this year.

### APL+UNIX: Release 5.2: Improving Compatibility with Other Platforms

A new release of APL+UNIX is also available. This maintenance release adds control structures (:IF,:WHILE,:FOR, etc.) and numerous small enhancements and corrective services. The addition of control structures makes the UNIX and Windows systems even more compatible, and will enhance your ability to write APL functions which will work on either system.

### APL2000 on the World Wide Web

Check out the Web site at HTTP://MEMBERS.AOL.COM/APL2000. The site includes general information about APL2000, news on upcoming events and releases, technical tips and demo workspaces.

### APL2000 Conference

APL2000 will be holding its first user conference in Orlando, Florida from October 23 through 25 1996. The conference will include application developer presentations and training sessions on new and existing products.

## Soliton Associates Ltd

General distribution of Release 22 of SHARP APL for the IBM MVS mainframe environment is planned for 4th quarter 1996. Release 22 is Year 2000 compliant. The emphasis of Release 22 development was on performance and operability.

The first customer shipments of the SQAPL Client for SHARP APL UNIX were made in 1st quarter 1996. The SQAPL Client provides SHARP APL with access to standard SQL database products on a wide range of server platforms.

Soliton has announced TimeSquare, a time series database manager for the open systems environment. TimeSquare manages the flow of time-based financial market data through a financial organization, from the data feeds provided by commercial data vendors through to the delivery of market data to end-users.

TimeSquare is an ODBC-compliant SQL server based upon the SQAPL Server for SHARP APL. TimeSquare supports both standard SQL and TimeSquare Extended SQL (a set of proprietary SQL extensions allowing sophisticated time series analysis at the TimeSquare Server).

The open systems networking and interfacing capabilities of SQAPL are provided by DataDirect SequeLink Client/Server Middleware from INTERSOLV Inc. Soliton Associates distributes and supports DataDirect SequeLink for use with SHARP APL.

## Dyadic Systems Limited

Dyadic is pleased to announce that the long awaited Version 8 for UNIX is now on Beta Test.

With a few restrictions due to differences in the environments, Version 8 for UNIX is fully compatible with Version 8 for Windows 95 and NT and with Version 7.2 for Windows 3.1. This means that you can develop a GUI application under Windows and deliver it to customers running on UNIX platforms. Indeed, as the workspaces are compatible at the binary level, you have only a single set of application code to support and maintain; Dyalog APL takes care of the rest for you. Under UNIX, your application will have a Motif look and feel, but will otherwise behave the same as it does under Windows.

The beta test release of Dyalog APL Version 8 for UNIX is currently available on IBM RISC System/6000. Versions for SUN SPARC (both Solaris and SunOS), DEC Alpha and HP9000 will be available in due course.

The current release of Dyalog APL/W Version 8 supports OLE Controls (OCX's). In OLE terminology, Dyalog APL (and a Dyalog APL application) acts as an OLE *Client*. In this context, the *Server* is the .OCX module in which the object (or control) resides. In practical terms, this means that you can use OLE custom controls in your Dyalog APL application.

At APL96, Dyadic will demonstrate the next phase of its OLE strategy, namely the ability for Dyalog APL, and more importantly a Dyalog APL application, to act as an OLE Server. Firstly, this means that you will be able to call Dyalog APL directly from another application such as Visual Basic. For example, you could build the user interface of an application in Visual Basic but perform the calculations using Dyalog APL. Secondly, it means that you will be able to build your own OLE Objects in Dyalog APL. These objects will be based upon Namespace technology and be manipulated by other applications through their properties (variables), events and methods (functions).

## Causeway Graphical Systems Ltd

It is hard to believe that three months have elapsed since the last time we sat down to compose our *Vector* news. During that time we have made solid progress on our two main consultancy projects, as well as bringing our APL product list significantly nearer to completion.

Our major project of 1996 is to extend and integrate the "Organisational Architect" tool fully into the SAP implementation process. Two months ago, we reluctantly made a major design decision — we are moving the implementation from Dyalog APL/W to a mixed platform with Microsoft C++ for the visual components and J for the calculation and logic engine. We will continue to use Dyalog to prototype and design new objects and interfaces.

The reasons for making this move are complex, and partly technical, for example we need to support double-byte characters (Japanese) and a multiplicity of keyboards and fonts, including Unicode. We also felt that we were constantly 'pushing the envelope' of what Dyadic offer in the Gui, and that by moving to C++ we could be sure that we had access to **everything** that Microsoft offer. Having decided to re-implement the Gui, we then had a choice of only 1 APL interpreter that can run as an in-process OLE2 server, and that interpreter was J! I think it is fair to say that (a) it was the right decision anyway and (b) we would never have moved if the same facility had been available in symbolic APL.

Needless to say, part-1 of the project was to code the core of the Causeway 'change-notify-refresh' logic as a DLL and to ensure that we could continue to benefit from the design principles that have given us such an edge in APL application development. It is interesting to speculate on the possible application of these ideas completely outwith the APL world, particularly given the move to Java which does at least have a partially interpreted approach.

The majority of the product development work has been focussed on getting *Rain* and *NewLeaf* up to a common level of functionality and reliability on Dyalog and APL+Win. Rain has already proved to be a major asset in our other consultancy project — migrating VDI-based graphics from APL\*PLUS II to APL+Win for a logistics planning package with some very complex charting requirements. Both Rain and NewLeaf are now with APL2000 customers for pre-release testing, and we are confident that we will have shaken out any remaining problems and deficiencies by APL96.

We will continue to ship Causeway as shareware for Dyalog versions 7.2 and 8, and we are targeting the APL2000 user conference as our release date for Causeway for APL+Win as well as the professional version of Rain (including 3D charting) and NewLeaf. Now that we have a solid platform for 95/NT we can begin to move ahead with Causeway/Pro for Dyalog — we see Causeway, Rain and NewLeaf as strongly complementary products and we urgently want all three on both the major APL platforms, sharing common documentation and support.
