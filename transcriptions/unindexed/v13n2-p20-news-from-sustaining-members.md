---
title: News from Sustaining Members
authors:
- Gill Smith
volume: '13'
issue: '2'
page: '20'
unindexed: true
transcribed: 'from page images of VOL.13-NO.2-OCTOBER-1996.pdf, pages 22–26 (printed 20–24); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
- applications
queries:
- "Printed byline “Compiled by Gill Smith”. The piece ends on printed 24, the rest of the page blank."
- "Kept as printed: “This enables a systems designed to define a series of tasks”; “languished a bit of late due the development work”; “It is after all where we started 15 years ago! this will be not only APL …” (lower-case “this”); “APL*Plus” and “APL+Win” as printed."
---

*Compiled by Gill Smith*
{ .byline }

## Dyadic Systems Limited

At APL96, Dyadic announced two major new developments for Dyalog APL. The first of these is a new type of defined function called a *Dynamic Function.* Dynamic functions are fast, lightweight functions with intriguing possibilities for improving performance and reliability.

The second major new feature is the capability to turn a Dyalog APL namespace into an *OLE Server* object that can be called from Visual Basic, C++, Excel and so forth. This feature will allow you to package and distribute your APL code in a form that can readily be incorporated into non-APL applications in a totally standard manner.

Articles describing these exciting new features may be found in this issue of Vector.

In addition to the capability to act as an OLE Server, Dyalog APL/W Version 8.1 will also include the ability to act as an *OLE Automation* client. This facility is also founded upon the direct correspondence between Dyalog APL namespaces and OLE objects and will allow you to drive numerous Windows applications from APL.

Finally, Dyadic is announcing *TCP/IP socket support* for Version 8.1. Not only will this allow you to access the Internet directly from APL, but it will provide the basis for future client/server operations between Dyalog APL for Windows and Dyalog APL for UNIX platforms.

## Causeway Graphical Systems Ltd

The major news for this quarter is the long-awaited release of NewLeaf and RainPro for both the Dyalog APL/W and APL+Win platforms. Adrian and Gill have just been demonstrating the APL+Win versions at the APL2000 user show in Orlando.

RainPro is an extension to the Rain package distributed as shareware with Dyalog APL/W. It includes 3D tower charts, scatter plots and surfaces and has the facility to copy graphs to the clipboard as metafiles. It comes with both the standard help file and a 48-page user guide which has many worked examples.

NewLeaf is a completely new product which breaks fresh ground in providing the capabilities of a desk-top publishing package to the APL programmer. It is a "frame-paragraph-style" based product which takes the difficulty out of producing well laid out reports in proportional fonts. It can print complex tables with ease and supports tree-structured table headings in the same way as the Dyalog APL/W grid control. Indeed it would be the ideal tool to provide the print method for that control.

Each of RainPro and NewLeaf is a set of APL functions that have simple syntax, take array arguments and that you can integrate into your code easily. The Dyalog APL/W and APL+Win versions of NewLeaf and RainPro are functionally identical although the Dyalog versions use namespaces to hide the functions. They are written entirely in APL and so are fully modifiable by the user, something not true of any OCX or VBX solution you might consider.

The second piece of news is that at the end of October we will be joined by Jon Sandles. Many will be familiar with Jon from his role as recruitment and meetings organiser for the BAA and from his work on the Vector Working Group.

Jon has been involved in the development of Causeway from the start and has a deep understanding of its internal structure as well as having written perhaps more Causeway applications than anyone else we know. He also has experience of maintaining a site of Causeway developers and developing his own Causeway classes, that having been part of his job. His experience in this area will be incorporated into the forthcoming CausewayPro for which we have received many requests and on which we are currently working. He will be a major asset to the company and will allow us some much-needed flexibility in scheduling our new developments.

## Insight Systems / Adaytum Software

Converting applications to Windows is an unpredictable business. At Insight, we have just completed the process, including rollout of the apparently inevitable bugfix release, for Adaytum Planning, our multi-dimensional business planning product — with only slightly more than a 100% overrun of the project plan. Fortunately, despite the delay, sales of Adaytum Planning have continued to grow rapidly; we now have several customers in Denmark and opened an office in the USA in September. The success allows us to grow our development team to cope with the workload; since August we have recruited an APL Developer, a Quality Assurance Manager, and an Internal Support Manager. We expect to recruit additional APL and C developers during the next six months; if you are an experienced APL or C developer (especially if you are both), and interested in a job in Denmark, drop us a line.

As a result of the delays in our Windows conversion project, even only slightly attentive readers will have noticed that our sustaining news items have remained pretty static; almost all our announced product releases have gradually slipped by between 6 and 12 months. The ideas for and the driving force behind our Client/Server products originate in our own requirements for tools which make it possible to position our APL applications as first class citizens of the emerging world of distributed applications. It is not easy to get ideas while fighting bugs and getting an application to behave itself under Windows.

The good news is that we have now actually started work on new releases of our APL Client/Server products, for internal use in the next release of Adaytum Planning and for general release to APL users. Following discussions with APL vendors and users at APL96, we have decided to start with a revision of the SQAPL Server, with the primary goal of improving performance and making the server available on low-end platforms such as Windows NT, OS/2 and even "stand alone" under Windows 3.x or '95. A revised SQAPL Client, with functionality as described in the April 1996 Vector, will follow later.

So, if any of you intend to downsize to windows and are planning to base connectivity on our products, you may proceed with confidence. By the time you are done with the conversion and have the bugs out, the new SQAPL generation will be waiting for you.

## HMW Trading Systems Ltd.

HMW have completed the first two phases of porting their APL\*Plus based Trading Room product *4XTRA* to Dyalog for Windows Version 7.4. The third and final phase includes converting the remaining code which requires a GUI interface, and then switching to Version 8.

The functionality of the new system is in fact a superset of the existing *4XTRA* versions, adding Money Market products such as FRAs and Financial Futures. To reflect the increased capability of the product, the Windows version is now known as *iDeal.*

The GUI interface uses both Causeway and specialised routines making direct Dyalog calls (dealing systems have some uncommon requirements). The system also has interfaces to databases (using the ODBC links provided by Insight systems) and other generally used Dealing tools, such as Excel.

We have also decided to make several of our own internal products available generally. All are available for APL\*Plus and Dyalog, but some features may vary between the versions. They include:

**Object Manager** — This enables the programmer to build a series of system files, comprising APL functions, global variables, screen designs, etc. and group them into modules (which can be grouped into larger modules). A complete range of search, edit, copy, delete functions are provided, including point and edit, version comparison, etc. Interfaces to Word provide a standardised documentation method.

**Configuration Management Suite** — based around the system file concept described above, this gives version control of each object (functions, variables and groups) enabling them to be managed through a development, test, release, live cycle. Promotion and rejection mechanisms co-ordinate movement between these levels (which can be redefined) and full client configurations. It is also capable of having multiple development input sources, preventing clashes and documenting the dependency of changes. Interfaces to Word for release documentation in a standard format. Designed to be used with a compression tool, such as PKZIP to give a series of documented modules for upgrades or patches which can be placed on a bulletin board or despatched to the client via modem or diskette.

**Multi-Processor Sequence Scheduler.** This enables a systems designed to define a series of tasks to be run on any number of PCs and have the activity interlocked and automated as much as possible. Special hardware requirements can be associated with a PC and with a task, ensuring the task gets run with, say, the correct peripherals (e.g. some backup device). The process fully allows for restarts and checkpoints, reprinting of report images, etc. and is very fault tolerant. The task activity is co-ordinated ultimately by file requirements and this is used to drive a task dependency list — a task cannot start until the files it requires have been produced and are available, even though they have been created on a completely different PC. Individual tasks may be assigned different priorities, including "optional", i.e. the failure of the task is not critical and processing may continue. Once started a sequence can cycle indefinitely, initiating or "sleeping" according to parameters, reducing operator intervention to practically nil — one client described it as "the nearest thing to perpetual motion" he had ever seen.

**Process Monitor** — a central process, running on a single PC capable of monitoring the activity across a network. It can check the status of devices such as printers, monitor errors on user workstations (with the suitable error trapping routines running), broadcast messages (or even code to execute on a user's PC) and provides a graphical monitor of tasks being run via the Scheduler. If any of these tasks fail the APL\*Plus version can "take control" of the failed APL session, enabling remote editing of functions and reassignment of variables — in fact about anything you can do directly at the keyboard.

Since we are just in the process of launching these tools as separate products, we haven't decided on a pricing structure yet, but expect the price to be low as development costs have been met largely by sales of the *4XTRA* system, which makes extensive use of them.

We are also expanding the general consultancy side of the business, which has languished a bit of late due the development work undertaken on the major products. It is after all where we started 15 years ago! this will be not only APL (and other languages) design and programming, but the project management skills and methodologies that we have developed over the years to implement and maintain our projects.
