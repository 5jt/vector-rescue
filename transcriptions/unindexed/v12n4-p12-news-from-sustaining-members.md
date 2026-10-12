---
title: News from Sustaining Members
authors:
- Gill Smith
volume: '12'
issue: '4'
page: '12'
unindexed: true
transcribed: 'from page images of VOL.12-NO.4-APRIL-1996.pdf, pages 14–18 (printed 12–16); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
queries:
- "Printed byline “Compiled by Gill Smith”."
- "Kept as printed: “doesnÆt” (Dyadic, a garbled apostrophe); “(a’hem)”; “closer in line to the APL2 language”; “APL 2000” beside “APL2000”."
---

*Compiled by Gill Smith*
{ .byline }

## APL2000 Inc (Bloomsbury Software Ltd)

We are busily working on release 2.0 of APL+Win and expect to release it at the end of March 1996. This new release will allow your APL+Win applications to be used under Windows 3.1, Windows 95 or Windows NT so as a developer, you only need worry about one set of code for your application. We are adding new controls that will allow your applications to have the new "look and feel" that users have come to expect, and give it to them in any Windows environment. This means less complexity, reduced documentation, simpler training and easier support.

Among the controls we are adding is a single selector control that will enable you to easily create Tabbed Property Sheets, Application "Wizards", and button driven input forms. You will like the "ease of use" of this particular feature. In addition we are adding ListView, TreeView, Progress bar, TrackBar, and more to enhance your applications and speed development. You will also enjoy speedups and enhancements to the interpreter (such as Take and Drop along Axis). Applications written using 32 bit DLLs will work fine in all environments and 16 bit DLLs can be accessed in Win95 or 3.1. A second release providing OCX support is expected to be demonstrated at the international APL96 conference in July. With this group of APL enhancements your development tools will be expanded to include virtually all of the widely available programming and utility packages, and allow you to smoothly integrate APL with other tools and environments.

We said our mission goes beyond keeping the interpreter up-to-date. With this in mind, we're pleased to announce the creation of some workspaces called APL+Widgets. These are workspaces of tools or application fragments that can help you add features to your application, or perhaps see new approaches to using APL+Win. The collection currently includes a calendar control (which looks remarkably like the calendar in Quicken for Windows) and a video control for showing AVI files. Over time, we'll add additional workspaces to showcase the features of the language.

We believe APL+Unix is important to your long-term Client-Server strategy. We will be improving our UNIX product to make it a better tool for Server applications. APL+Unix is being upgraded to incorporate control structures and to consolidate all of the bug fixes and changes given out on a per request basis for the product. You will find the addition of control structures to be especially useful in developing Server applications. In addition to this major change, we are adding Take and Drop along Axis to bring us closer in line to the APL2 language. This release is expected to be ready for beta distribution in the second quarter of 1996.

To ease the flow of code among all three platforms, we are adding control structures to APL+DOS in the third quarter. This will allow computational routines to be easily moved without having to be rewritten.

Any license purchased in 1996 will be eligible for free (with the exception of shipping charges) upgrades to all releases of that product during the calendar year. This will include all improvements and fixes to that product. That means that if you purchased APL+Win in January, you will receive all of the APL+Win improvements as they are available. To order any product in the UK call Bloomsbury Software on 0171 436 9481.

To help in that communication effort we are now on the World Wide Web located at **http://members.aol.com/APL2000**. Our site has information about our products and services and innovative ways to use them. In addition, a section on technical tips will give you examples you may find useful in improving your business application.

## Insight Systems / Adaytum Software

### Adaytum Planner for Windows

Development of version 2.0 of our multi-dimensional business planning product, previously known as the Kunzle Planning System (KPS), is finally completed. Rolling the product out to 200 customers will take up a considerable amount of our time over the next several months, but even so we can now schedule new releases of our Client/Server product range.

### SQAPL Client 3.0

Development of a new version of the SQAPL or APL Link client will be completed in the 2nd quarter of 1996, with general availability planned for August/September. The primary goal is to take advantage of enhancements to SequeLink (version 3.0), and to ODBC drivers. In particular, we would like to:

- Remove the object size limitations of previous versions of MiddleWare products, by supporting "partial bind" calls. The only remaining limits on object size will be workspace size and limits imposed by the host database.
- Support SequeLink 3.0 functionality, making ODBC-style dictionary calls and data type support available under Unix and OS/2. This will remove most of the differences which exist between the SequeLink and ODBC versions of SQAPL.
- Improved "Data Set" functions, supporting multiple keys.
- Support for ODBC calls to interrogate the list of installed drivers, driver options, and to support interactive logon panels provided by ODBC drivers.
- Implement workarounds for errors in popular ODBC drivers, in particular the Microsoft Office drivers.

We invite all our existing customers to write to us to suggest features to be included in the new release.

### SQAPL Server 3.0

No new release of the SQAPL Server is planned for the immediate future. We do expect that our own use of the product in the Client/Server version of Adaytum Planner will lead to the development of a number of new features, which will find their way into a new version of the SQAPL Server later this year.

### APL Pipes 1.0

We finally have the time to complete the packaging and documentation of APL Pipes, our TCP-based communications product. We will also add support for non-APL applications, so Pipes can provide access to APL services from Visual Basic and other application development tools, and access to TCP services like FTP, telnet and the World Wide Web from APL.

### APL96

This year's APL conference, to be held at Lancaster at the end of July, is promising to be an APL training event of the highest calibre. Judging from the APL consulting work we have been asked to do during the last 6-12 months, downsizing of APL applications is now really happening. At APL96 you can learn about all the relevant technologies: using enclosed arrays, moving from one APL system to another, using remote databases and building distributed systems using TCP/IP and other communication tools.

Together with APL 2000, Dyadic, IBM and Soliton, we will be there to show you how to use our software in combination with their APL systems. See you in Lancaster!

## Dyadic Systems Limited

Dyadic is pleased to announce that Dyalog APL/W Version 8.0 is **finished** and should be shipping by the time this edition of Vector is printed. The last few pieces of the jigsaw, including Control Structures and support for 32-bit OLE Controls, were added during February and issued to Preview Program Subscribers in March. The new OLE Control support is worthy of special mention.

Version 7 of Dyalog APL has, for a long time, supported Visual Basic Custom Controls (VBX). Whilst a *well behaved* VBX is indeed a valuable tool in the Dyalog APLer's armoury, VBX technology is (a'hem) not exactly a rigorous science, and has now all but been abandoned by Microsoft. Its replacement, *OLE Controls*, provides similar functionality, but is based upon sound object-oriented technology. OLE Controls are constructed from a properly defined set of function calls and a prescribed set of rules and protocols. In Microsoft terminology, Dyalog APL/W Version 8 acts as a fully fledged *OLE Control Container* and can therefore access any OLE Control that adheres to the rules. The good news is that so far, Dyadic has not found an OLE Control that doesnÆt work with Version 8.

When an OLE Control is installed on your computer, all of the information needed to access and manipulate the Control is recorded in the Windows Registry and Type Library. This information includes a list of Properties, Events and Methods provided by the Control together with information about the data structures they use. For example, not only does the system record that the *Crystal Reports* OLE Control has a property called *Destination*, but it also records that it may be set to 0, which means "To Window", or 1 which means "To Printer" or 2 which means "To File". Pointers to on-line help topics are also available and all this information is directly accessible in Dyalog APL.

One test of a true OLE Control Container is whether or not it can act as a browser. The proof is a Version 8 workspace named OCXBROWS which lists all of the OLE Controls installed on your system. Select one and it will create an instance of the Control together with a hierarchical view of its Properties, Events and Methods. Click on a property name and it will give you a brief description of the property, its data type and, if appropriate, a list of the values it may take. Click again and you will get full on-line help. You can also experiment with the Control directly through a standard property sheet interface.

OLE is in fact a set of technologies of which OLE Controls is just a part. In terms of its implementation, OLE Controls utilises all of the other technologies and is in a sense the most difficult to achieve. With the hardest part completed, Dyadic plans to add support for the other OLE technologies in future releases.

## Causeway Graphical Systems Ltd

The highlight of this quarter was our trip to the USA and Canada, where we had the opportunity to address keen and interested APLers in Toronto and New York. At both meetings the emphasis was on the principles behind the Causeway environment, and we were able to show how our approach helps developers to manage complexity, even in very advanced Windows applications. We will also be talking at the GSE/APL Club of Germany meeting on April 23rd in Frankfurt, as well as participating in the BAA's Vendor Forum in May.

We were very encouraged by the positive news from APL 2000. We have resumed development of Causeway for APL+Win, this time with the goal of producing a much lighter-weight implementation which is very interpreter-specific. This gives us speed at the expense of cross-platform compatibility. So far, the results are quite startling — on a P90 laptop a collection of 20 forms, all watching the same text variable, can be set to notify/refresh **on keystroke**. All 20 keep up with normal typing speed.

We shall, of course, support the existing Causeway 'shareware' platform on both Dyalog 7.2 and 8 — the Windows 95 version includes many of the new Gui controls (trackbar, tree etc.) as Causeway objects.

The *NewLeaf* printing namespace is now functionally complete, and is undergoing pre-release testing at a number of Dyalog APL sites around the world. By the time you read this, it will also be available for APL+Win users to download and test, as the code has been written for maximum cross-platform compatibility. The beta programme has resulted in several useful additions, for example NewLeaf tables now support tree-structured column titles and HTML-style tags for bold, italic, sub- and super-script text both in the titles and in the table cells. Decimal alignment was also introduced for numeric columns as a result of a specific user-request, as was spooling to file for large reports (several hundred pages). NewLeaf will be priced at £400 per developer, with unlimited runtime and discounts for major APL sites. Watch for details on our web site at www.causeway.co.uk.

We are now working with a number of companies who are beginning to migrate existing APL code to the Windows platform. So far we have been able to help with advice on choice of platform, migration issues for mainframe or APL\*PLUS II code, and detailed interface design. We are also continuing to work with SAP to extend the 'Organisational Architect' configuration tool to cover the entire process of setting up a company structure in the SAP R/3 system. If you would like to know more, please call Adrian or Duncan at +44 (0) 1653 696760 or Email us via 100265.1564@compuserve.com and ask for a copy of our brochure.
