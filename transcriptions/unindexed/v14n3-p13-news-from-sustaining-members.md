---
title: News from Sustaining Members
volume: '14'
issue: '3'
page: '13'
unindexed: true
transcribed: 'from page images of VOL.14-NO.3-JANUARY-1998.pdf, pages 15–17 (printed 13–15); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
queries:
- "No byline is printed. Dyadic’s list of enhancements is printed as two columns (feature, description) and is given here as a table; the APL names printed in the APL font (`:For`, `⎕LX`, `)LOAD`, `NAMESPACE.SUB.FOO`, `⎕OR`) are set as code."
- "Adaytum’s recruitment address mkrom@adaytum.dk is a company contact and is kept."
- "Kept as printed: “Insight Systems / Adaytum Software” as the heading over the SQAPL item; “A COM Automation API to allows VB”; “the comments, (tips that appear …)”."
---

## Dyadic Systems Ltd

Dyadic is pleased to announce the successful launch of a new Dyadic Support Service (DSS) for Dyalog APL. This is primarily an electronic service based on email and the World Wide Web.

One of the key features of the service is that users may download patches containing enhancements and problem corrections from the Dyadic web site http://www.dyadic.com. The process of downloading and applying a patch is completely automated (it's written in Dyalog APL, of course) and convenient to use. Furthermore, the patch files are updated on a daily basis, so DSS users can stay absolutely up-to-date with the latest Dyalog APL developments. In addition, Dyadic's new change control system issues email messages to DSS users, informing them of changes, enhancements and fixes automatically as code is released.

Behind the new service is a totally new *incremental* approach to the development, enhancement and maintenance of Dyalog APL. This technique allows small changes to be made, tested, and safely released to users in a much shorter time-scale than was previously possible. As a consequence, Dyadic is able to deliver a steady stream of enhancements, as well as fixes, that would previously have had to wait for a new software release.

Since the start of the service, some of the enhancements made for the benefit of DSS subscribers are as follows:

| | |
|---|---|
| **Grid Comments** | the Grid object has been enhanced to support comments, (tips that appear when the user hovers the mouse over a cell) which are consistent with the latest edition of Microsoft Excel. |
| **:For** | the `:For` control structure now accepts multiple variables as in: `:For a b c :in (1 2 3)(4 5 6) ...` |
| **MetaFiles** | making complex graphical pictures using the Metafile object is now much faster than before. |
| **Tracer** | You can now trace the execution of `⎕LX` on `)LOAD`. |
| **ActiveX** | The OCX support has been extended to cater for ActiveX objects that expose an object hierarchy (like OLE Servers). |
| **Syntax colouring** | Improvements have been made to the colouring of compound names (e.g. `NAMESPACE.SUB.FOO`) and dynamic functions and operators. |

Further enhancements in the pipeline include a facility to reformat a function during editing, and a significant improvement in the efficiency of cloning namespaces using `⎕OR` and of making new instances of OLEServer objects.

Naturally, there will still be new major releases of Dyalog APL issued at roughly 12-monthly intervals, and Dyadic intends to announce some exciting new features at APL98.

## Insight Systems / Adaytum Software

**SQAPL Client Version 3.0.** Available at APL98. Work on the next release of SQAPL (previously announced as version 2.1, now renumbered to 3.0), has now reached a stage where we can commit to a release date: the release will be available by the APL98 conference in Rome (July 1998). We hope to see you all there! Initially, the release will be available for 32-bit Windows (Windows NT, 95 and 98), for the APL systems available in these environments (APL+Win, APL2 and Dyalog APL).

Key features of version 3.0 are:

- No limits on the size of bind variables or record length, except those imposed by the drivers themselves (and "Workspace Full" of course).
- Support for the ODBC ExecDirect, allowing execution of statements without preparing them first, and improved support for stored procedures.
- GetInfo and PutInfo calls, which allow you to inquire about the capabilities of a particular data source, and set options after connection.
- Support for "BrowseConnect", allowing the ODBC driver to provide dialog boxes to guide the user through connection to a data source.
- Bulk Input, allowing insertion or update of multiple rows of data (sets of bind variables) in a single operation.
- For advanced users, we will make the Environment, Connection and Statement handles available so that you can extend the product from APL by making direct ODBC DLL calls.
- Installation Script

**Adaytum Software.** We believe that Adaytum Planning is en route to becoming one of the biggest APL-based businesses ever. Adaytum Software now employs almost 100 people world wide. In January, our US revenues exceeded UK revenues for the first time, after about eighteen months of operation in the US market, a period in which the UK has also experienced substantial growth. The total number of customers world wide is now in excess of 450.

Our development team has grown to about 15 people, our goal is to more or less double this number during the next twelve months. If you have a knowledge of APL and C++, Visual Basic or Java (or preferably a combination of these), please contact mkrom@adaytum.dk or check our Web site: www.adaytum.dk for an up-to-date list of open positions. We are also recruiting technical writers, product designers and testers. Positions will exist in Denmark, the UK and in North America.

The next major product release is due at the end of 1998. The focus of development for this release is "large, distributed customers": Workflow, Distribution of Reports and Data Entry Tools for organisations with hundreds of widely distributed users. A multi-user Server architecture will provide a Web Server, and an ODBC Server.

Another major theme is "Open Systems": A COM Automation API to allows VB, C++ and other "third party" developers to call our "Planning Server" and build custom planning applications.

## Causeway Graphical Systems Ltd

The autumn and early spring have been a period of consolidation and plain hard work for all of us. It may be the approach of 1/1/2000, or maybe the advantages of array programming are again getting noticed. Either way, the result has been that the "Products Department" (Adrian) has been lagging behind the software in getting CPro out of beta and into production.

The good news is that the software itself is proving fast, stable and reliable. Watch the website (the release notes are posted with every significant update) for progress on the tutorial and help files. *NewLeaf* and *RainPro* updates are also available for both Dyalog and +Win to all users on current maintenance — email us for the ZIP passwords, or to receive your copy by diskette if you prefer.

The other good news is that we are now happy to accept both **VISA** and **Mastercard**, which greatly simplifies payment from non-UK customers. Finally, congratulations to Eric Lescasse who has sold more copies of RainPro and NewLeaf than anyone else, including us!
