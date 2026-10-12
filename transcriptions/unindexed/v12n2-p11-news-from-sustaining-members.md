---
title: News from Sustaining Members
authors:
- Gill Smith
volume: '12'
issue: '2'
page: '11'
unindexed: true
transcribed: 'from page images of VOL.12-NO.2-OCTOBER-1995.pdf, pages 13–17 (printed 11–15); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
- user interfaces
queries:
- "Printed byline “Compiled by Gill Smith”. Printed 16 is a MicroAPL advertisement (“APL for the Apple Macintosh”), not transcribed."
- "Kept as printed: “For the forseeable future”; “will not be able to take advantages of”; “(see below)” without a full stop; “Ok” in “Ok and Apply Now buttons”; “Trackbar” beside “TrackBar”; “Windows 3.11” beside “Windows 3.1”."
---

*Compiled by Gill Smith*
{ .byline }

## Insight Systems

Insight Systems is proud to present two new Client/Server products, the *SQAPL ODBC Server* and *APL Pipes*, which make it possible to integrate application servers written in APL with other development tools, using industry standard interfaces and communications products:

- The *SQAPL ODBC Server* allows your APL application or database system to be accessed as an ODBC data source. You can present your APL-based data or the results of analyses as a set of relational tables which can be used as input into other reporting packages. It is also possible to use application generators such as Borland Delphi or Microsoft Access to create front-ends to APL applications via ODBC. The APL application must run under Unix or Windows NT, but becomes accessible from almost any end-user application or development tool on virtually any platform.
- With *APL Pipes*, you can write distributed APL applications without the overhead of a relational interface such as ODBC or SequeLink. APL Pipes is a TCP/IP based system which is similar to Shared Variables, except that it supports sharing of data and function calls between APL2, APL\*PLUS II or III, Dyalog APL and SHARP APL systems running under Windows, Windows NT, OS/2 and Unix. Before the end of the year we plan to add Microsoft Visual Basic and Borland Delphi to the list of *APL Pipes* clients. This will mean that developers in these environments will be able to effectively share variables and make function calls to almost any APL application, whether this application is running on the same machine or accessible over the network.

Until the end of the year, Insight Systems will be very busy with the completion of the Windows version of the KPS System for Adaytum KPS Software Ltd. KPS is a multi-dimensional planning system written in APL, and is currently the UK market leader for budgeting software. We are looking forward to developing the Client/Server versions of KPS scheduled to follow the Windows product, which will allow us to practise our Client/Server preaching and enable APL-based solutions to compete head on with mainstream products in a highly competitive market.

## Dyadic Systems Limited<br>Announcing Dyalog APL/W Version 8

### What is Version 8?

Dyalog APL/W Version 8 is a completely new implementation of Dyalog APL/W that is designed specifically for Windows 95 and for Windows NT Version 3.51. It is fully compatible with the current release of Version 7 (7.1 Release 2), but contains many enhancements to support the Windows 95 user interface and other features.

Version 8 is based on Microsoft WIN32 in place of the equivalent Watcom software used for Version 7. WIN32 provides improved memory management under NT and is a key requirement for the new Windows 95 logo for which the product is intended to qualify.

Version 8 includes support for most of the new GUI objects and features provided by Windows 95 and Windows NT 3.51. These include *ListView*, *ProgressBar*, *PropertySheet*, *RichEdit*, *Spinner*, *TrackBar* and *TreeView* objects. All new and existing GUI controls have also been enhanced to support the drag-drop feature of Windows 95. This permits the user to drag-drop file icons into a Dyalog APL/W application. It is intended that the new version of Dyalog APL/W will also support OLE2 and .OCX custom controls.

### Availability

Dyadic expects to be in a position to ship Version 8 by the end of 1995. However, an early release will be available by the end of September that includes much (if not all) of the additional functionality. Customers may obtain this release by enrolling in the Version 8 Preview Program (see below)

### What is the policy for 3.1 and 95?

For the forseeable future, it is likely that many customers will continue to use Windows 3.1. Others will migrate immediately to Windows 95. To cater for both requirements, Dyadic intends to maintain two separate versions of Dyalog APL/W for as long as the requirement to do so exists.

Version 7 will continue to be maintained for Windows 3.1 and OS/2 users. Version 7 is also supported under Windows 95, but it is NOT supported under NT. Customers who need to run applications under Windows 3.1 or OS/2, should remain with Version 7. Applications based upon Version 7 will also run under Windows 95, but will not be able to take advantages of the new Windows 95 features.

Version 8 is Dyadic’s product for Windows 95 and NT 3.51 and includes support for many of the special facilities provided by these systems. It is not supported under Windows 3.1. Version 8 is intended to be the state-of-the-art APL for Windows and will be the basis for ongoing developments in the future.

### Prices

Version 7 and Version 8 will be marketed and supported as separate products. Version 8 is not provided as an upgrade from Version 7. However, there will be a reduced price for customers purchasing both Versions and for customers who already have Version 7 and purchase Version 8 in addition. Please contact Dyadic or your local Dyalog APL distributor for details.

### Version 8 Preview Program

The Version 8 preview program is intended to allow customers to begin to develop Windows 95 (and NT 3.51) applications immediately, without having to wait for the final release of the Version 8 product. It also provides a basis for customers to influence development. This program is open only to existing Version 7.1 users and to any customers who purchase Version 7.1 prior to the final Version 8 release until further notice. The Version 8 Preview Program is chargeable but the price includes a copy of the final release which will be supplied as soon as it becomes available. Enrolling in the Preview Program is the cheapest way for existing Version 7.1 users to obtain Version 8. Contact Dyadic or your local Dyalog APL distributor for details.

During the Preview Program, Dyadic will supply a stream of test releases as new functionality is added and as bugs in the existing code are fixed. In addition to bug reports, subscribers may submit suggestions and requests for enhancement to the new Windows 95 and NT features as they are developed. Dyadic does not guarantee to incorporate all of the requests in the final version, but will endeavour to meet popular demands.

### Summary of New GUI Features

Version 8 provides 10 new objects, over 30 new properties and over 40 new events. These new features are summarised below.

- The *PropertySheet* object is a dialog box that allows the user to view and edit the properties of an item. A Standard PropertySheet contains one or more overlapping child windows represented by *PropertyPage* objects, each containing controls for setting a group of related properties. Each PropertyPage has a tab that the user can select to bring the page to the foreground of the PropertySheet. The Display Properties dialog (obtained by clicking the right mouse button on the desktop and choosing Properties) is an example of a standard PropertySheet object. A *Wizard PropertySheet* consists of a sequence of dialog boxes that guide the user through the steps of an operation. In a Wizard PropertySheet, the PropertyPages do not have tabs, and only one page is visible at a time. Also, instead of having **Ok** and **Apply Now** buttons, a Wizard PropertySheet has a **Back** button, a **Next** or **Finish** button, and a **Cancel** button. Windows 95 Setup is an example of an application that uses a Wizard PropertySheet.
- The *ListView* object displays items as a set of icons, in a list format or a report format. ‘My Computer’ is an example of an application based upon this object.
- The *TreeView* control is a window that displays a hierarchical list of items, such as the headings in a document, the entries in an index, or the files and directories on a disk. Each item consists of a label and an optional bitmapped image, and each item can have a list of subitems associated with it. By clicking an item, the user can expand and collapse the associated list of subitems. ‘Windows 95 Explorer’ is an example of an application based upon this control.
- The *RichEdit* control is a multi-line text editor that provides extensive word-processing facilities including variable text and paragraph alignment, fonts and colours. This control allows Dyalog APL/W applications to exchange complete documents with Microsoft Word and other word-processors. Data may be imported and exported using .RTF files or via the clipboard. The object also includes direct printer support.
- The *ProgressBar* is a standard output control that indicates the progress of a time-consuming operation.
- A *Trackbar* control is a window that contains a slider and optional tick marks. When the user moves the slider, using either the mouse or the direction keys, the trackbar generates events to indicate the change.
- The *UpDown* control is a pair of arrow buttons that the user can click to increment or decrement a value, such as a scroll position or a number displayed in a companion control.
- The *Spinner* object is a special Dyalog APL object that combines an *UpDown* with an *Edit*. The Spinner permits the user to select from a range of numerical values or text strings.
- The *Grid* object has been extended to allow *Spinner* and *Trackbar* objects to be used to edit cell values.
- The *List* object has been extended. It has a new *MultiColumn* property that allows you to display items in several columns. In addition, the List supports the facility for the user to drag-drop items within it.
- Most controls support the new *AcceptFiles* property. If this is enabled, an object will generate a *DropFiles* event when the user drag-drops one or more file icons onto it from another application, such as ‘My Computer’ and ‘Windows Explorer’.

## Causeway Graphical Systems Ltd

Our main item of news is a very simple one: around 3 weeks ago, SAP started cutting our software onto CD to issue with their R/3 3.0a release. From SAP’s point of view, 3.0a is a strategic release and is, to the best of our knowledge, the first truly distributed business management system to hit the world market. Perhaps the most encouraging thing about this is that a major player in the world software market has been willing to rely on APL for a critical configuration tool. This has to be a good thing for the future of our language.

This leads naturally to the second item: *Causeway – the Next Generation* (working title: *CTNG*). For the past two weeks, we have had time to relax and work on the future of Causeway rather than hitting the impossible deadlines set by our clients. Since we first released the Causeway utilities in November 1993 (at the British APL Association’s BAA-GUI workshop) we have seen a massive increase in the functionality of the Dyalog interpreter. In particular it can now handle resize and reposition (via the `ATTACH` property) in the way that we need it, and it has *Namespaces*. Anyone who has looked through the `Gui_xx` functions will have noticed that a significant slab of code in `Gui_make` is no longer necessary, and may have wondered what all the complex use of `⎕OR` and `⎕SHADOW` is doing in `Gui_exec`.

Rather than attempting a piecemeal upgrade, we decided to take the bull by the horns and do a top-down rewrite. It was important to preserve the dialogue-box structure, and it is clearly essential that CTNG behaves in exactly the same way as Causeway, to the calling application. However the internal structure of the class table will be very different (and will support managed replication of functions between classes), and the implementation of localisation and event-handling has been built entirely around the namespace model.

The main visible difference is a huge reduction in the lines of APL code needed to support form-level localisation of variables, and local functions on objects. The entire set of `Gui_xx` functions written so far can be listed on 3 sides of A4, and most of these will never appear outside `#.Gui`. In particular, all the Causeway ‘modules’ (such as the *Rain* PostScript interpreter) simply become namespaces, and the code in them can be executed much more simply with statements such as `ps.FullScreen` replacing `ps Gui_do'FullScreen'` in application code.

We are on course to have the first release of CTNG included with Dyalog 8; however we also intend to support it under Dyalog 7.1.2 for users who prefer to stay with Windows 3.11 for the moment.
