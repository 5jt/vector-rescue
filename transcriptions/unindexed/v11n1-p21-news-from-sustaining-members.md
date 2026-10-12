---
title: News from Sustaining Members
authors:
- Gill Smith
volume: '11'
issue: '1'
page: '21'
unindexed: true
transcribed: 'from page images of VOL.11-NO.1-JULY-1994.pdf, pages 23–30 (printed 21–28); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
queries:
- "Printed byline “Compiled by Gill Smith”; the Contents line gives no author."
- "The foot of printed 28 carries a boxed BAA house notice, “Vector Back Numbers” (“REDUCED PRICE”), not transcribed."
- "System functions printed in the APL font (`⎕NA`, `⎕WCALL`, `⎕WI`, `⎕WE`, `⎕CMD`) and the `GETEVENT` function are set as code. Manugistics’ e-mail addresses are a company’s and are kept."
- "Kept as printed: “The most exciting of which has to be”; “Static text, (or Label) Button”; “New Windows’ menu”; “Insight are also the author of SQAPL”; “APL*Plus III” in the MicroAPL item."
---

*Compiled by Gill Smith*
{ .byline }

## Insight Systems

Since we introduced our *SQAPL Client* product a year ago and gave APL developers access to most multi-user SQL databases on the market, the most frequent request for an enhancement to the product has been for it to support local databases or file systems such as Access, dBase or Paradox. We are therefore pleased to announce that version 2.0 of SQAPL supports Microsoft ODBC as an alternative to SequeLink under Microsoft Windows and in the OS/2 Windows box (WINOS2). ODBC drivers are available for almost all PC file formats. Many client/server database vendors also provide ODBC drivers for their own middleware products (such as Oracle’s SQL\*NET). If you only need access to a single client/server database, a proprietary middleware solution from the database vendor may be an acceptable solution — but SequeLink remains the best solution in heterogeneous environments, and the only solution if you have client workstations running Unix and OS/2.

We are also pleased to announce that we have entered into redistribution agreements with both Dyadic Systems and Manugistics for the ODBC version of SQAPL 2.0. Contact your regular supplier if you want to use this product with APL\*PLUS III/Windows or Dyalog APL/W version 7. Until further notice, we are still handling distribution of SQAPL for SequeLink under Windows, OS/2 and Unix, for APL2, APL\*PLUS II and Dyalog APL.

Whether you use SQAPL with SequeLink or with ODBC drivers, the APL function calls are identical across all APL systems and environments in which SQAPL is available. You can easily prototype an application under Windows using a local database, and put it into production running APL under Unix to access DB2 on a mainframe. Unfortunately, although the SQAPL function calls are the same, the “local” ODBC drivers we have tested so far have been quite different when it comes to data types. Data types which have fundamentally the same internal representation can have quite different names from one driver to the next. For example, in testing ten or so drivers for PC files (dBase, Btrieve, CSV, TXT and Excel drivers from Microsoft and Q+E) , we came across VARCHAR data types named VARCHAR, MEMO, NOTE, TEXT and LONGCHAR — usually (but not always) requiring a maximum length declaration in CREATE TABLE statements. You will also find data types with the same name, which have subtly different internal data types.

We are more than a little surprised and disappointed by these differences between ODBC drivers. The differences may not be of great importance to the “personal” APL user — but they will be rather irritating to the software professional who needs to be able to provide portable, scalable solutions. Our strategy to cope with the situation is to provide an Entry Level product for the personal APL user, available immediately at low cost or bundled with an APL interpreter. Within a few months, we will provide *Professional Edition* with a number of performance and portability features important to the professional software developer. Besides hiding the differences in data type naming and handling, we will try to deal with some of the most irritating differences in transaction processing (are cursors closed after a commit?) — to make it as easy as possible to write portable applications.

In the slightly longer term, we will be transferring our attention to the server side of our product. The two most important goals are to port the SQAPL Server to the mainframe and support IBM APL2 and possibly Sharp APL under MVS. We will develop an ODBC compatible version of the SQAPL Server, so that APL applications can act as ODBC servers for any ODBC-enabled client application (including MS Query, Powerbuilder and other popular prototyping and analysis tools).

Although our customers still see SQL database access as their most pressing need, it is the SQAPL Server which we think is the important product in the longer term. Although we now derive an important part of our income from the sales of APL to SQL interfaces, we make no secret of the fact that we have found very few (APL) applications where SQL had any real functional advantage over APL component files. We have seen customers move multi-dimensional timeseries structures into relational databases and be rewarded with a loss of flexibility, and a hundred- or thousand-fold increase in resource consumption. Ten users of a sales forecasting system which used to consume a small fraction of the machine when using APL component files can consume all of a big mainframe when the data moves to DB2 and they all generate the dynamic SQL statements required to multiply the sales forecast by unit price and currency rate(s), then total it on three dimensions while converting the frequency from monthly to quarterly. The resulting two-dimensional table will most often need a lot of afterburning before it is ready for presentation. Remember that retrieval is the **strong** side of SQL. After all, the people who designed the language named it a Query language — and anyone who has tried to write non-trivial data entry applications using SQL will agree that it is aptly named.

We believe that the SQAPL Server can provide a more attractive solution. Instead of moving the data to an SQL database, you can turn the sales forecasting system into an ODBC or SequeLink server, which can be used by a frontend coded in APL or called from most other tools on any kind of workstation. You can even put a simple SQL frontend up which allows people to use SQL on virtual tables which are generated by APL. In this way, the APL data and services can become integrated with mainstream applications without sacrificing the advantages of APL. We feel that there are a lot of opportunities open to APL as an application server. We can provide computation engines or specialized database servers which are not only more flexible than relational databases, but also outperform them by one or two orders of magnitude for the types of data that APL is good at handling.

## Manugistics Inc

Manugistics Vector Sustaining Member News

A great deal has been happening in Rockville since our last sustaining member news. The most exciting of which has to be the tremendous success we’ve had so far with APL\*PLUS III for Windows. We officially began shipping version 1.1 in late April, although we had been selling pre-release versions for nearly two months to customers who couldn’t wait and wanted to take APL\*PLUS III for a spin. To be honest, even we were a little surprised at how quickly we reached the 1,000 units shipped mark. Next stop 2,000.

Our development group is busy putting the finishing touches on version 1.2, which we hope to be shipping by the end of August. Version 1.1 has been such a stable system that we have been able to spend the bulk of our time putting more features in 1.2 instead of fixes. Top on the list of new features for 1.2 is support for Visual Basic Custom Controls (version 1). We are also adding the necessary object classes to APL\*PLUS III to allow developers to implement MDI style applications and `⎕NA` and `⎕WCALL` are being modified so both will support 16 bit DLLs directly, so you won’t have to “thunk” any longer.

While building APL\*PLUS III, our developers became so enamoured with syntactic colouring, we decided to put it in version 1.2. This really is a nice feature and along with control structures, makes reading APL code much easier. We are also enhancing the product’s graphics capability by adding a “Picture” class, for persistent graphics, and a new “chord” operation to the “Draw” method. Help and prompting tools are also being added to assist the developer in implementing status line and pop-up help messages and a few aesthetic changes to the session manager are liable to sneak in as well including support for the classic APL keyboard.

We see APL\*PLUS III evolving into a modular system, with add-on packages being offered by Manugistics as well as other parties. At the time of this writing, an ODBC module, developed by Insight Systems, is about to go into beta test. When commercially released, the product will be available through Manugistics’ regular distribution channels. Please contact Manugistics or your local APL\*PLUS re-seller for more information.

Last week we held another successful annual international dealer conference. Re-sellers from various countries came to Rockville for 4 days of speeches, round-table and one-on-one discussions and networking. We want to thank all of our friends for making the trip and participating this year and we hope to see even more next time.

As always, Manugistics welcomes all suggestions, feedback and inquiries from Vector readers. To facilitate this, we have added the following two Internet addresses. In the United States, e-mail us at aplsales@manu.com. Outside the United States, use the address intl@manu.com.

## MicroAPL Ltd

In the last issue of Vector, we announced details of an upgrade to our Macintosh versions of APL.68000 Level II. We have now completed work on Version 3 of APL.68000 Level II for the Macintosh and it represents a major enhancement to the leading APL2-compatible interpreter for the Apple Macintosh family.

### ‘Native’ Power Macintosh Support

With the advent of the new RISC-based Power Macintosh systems, Apple has dramatically improved the potential performance of Macintosh systems, *provided* applications are re-engineered to run ‘native’ on the new PowerPC processors. For over two years, MicroAPL has been working closely with Apple on tools for converting 68000-family applications to the PowerPC. One of the fruits of this work is that the full power of the Power Macintosh is available to APL applications running under Version 3 of APL.68000 Level II. This provides one of the fastest APL interpreters available for a small computer, particularly for code that makes heavy use of floating point.

### New Object-Based GUI Programming

Included in Version 3 is a new system function `⎕WI` which provides a simple, consistent and object-based method of controlling user-interface elements such as buttons, list boxes, pop-up menus and pictures. Objects are created using `⎕WI`, and their behaviour is defined by setting *properties*. And to help APL users develop cross-platform applications, the implementation of `⎕WI` is largely compatible with Manugistics’ APL\*Plus III for Windows, making it straightforward to move applications between the Macintosh and Windows PCs.

The object classes supported by `⎕WI` are Window (or Form), Document, Dialog, Static text, (or Label) Button, Radio button (or Option button), Check box, Edit field, List, PopUp menu (or Combo), Icon, Picture, Scroll bar, Line, Rectangle, RoundRect, Arc, Movie and Timer.

### New Callback-Based Event Handling

In addition to the `GETEVENT` function previously available, Version 3 of APL.68000 Level II implements callback-based event handling. A ‘callback’ is an APL function (or other expression) which is run when a given event occurs (for example, if a Button is pressed).

To give you full control of event handling, callbacks are run during the `⎕WE` (wait for event) system function, to which you pass a timeout value as the right argument. This allows applications to continue processing events during lengthy calculation or other processing. You also have full control over whether APL’s default event handling takes place, which together with an event triggering feature makes it possible to write APL custom controls.

### Play Quicktime Movies from APL

Amongst the object classes supported by APL.68000 Level II is the Movie object. This allows an application to take advantage of Apple’s Quicktime movie technology, with the possibility of multi-media applications under APL control.

### Improved Programming Environment

Many enhancements have been made to the user interface, further developing APL.68000 Level II’s position as one of the most user-friendly APL programming environments. These include:

- New Windows’ menu, with multiple sessions identified by workspace name, and improved dialog design.
- Support for Apple Events — multiple workspaces may be launched simultaneously at start up, and double-clicking on a workspace icon during APL execution opens a new APL task.
- Improved File Menu with Import and Export options to exchange Transfer format files with other APLs
- New Print menu items allow print of workspace listing as well as contents of any APL window.
- Improved editor facilities including new find/replace facility.
- Closer conformance to Apple’s System 7 user-interface guidelines.
- Removal of limits on number of edit windows open simultaneously (up to overall limit of 99 open windows).
- Up to nine APL tasks can run simultaneously!
- New user preferences dialog for startup configuration.

### 100% Upwards Compatibility

In implementing the new features in APL.68000 Level II, we have retained 100% upwards compatibility for existing APL applications — even if you have written 680x0-family auxiliary processors and want to run them on a Power Macintosh!

### Royalty-Free Packager Included

MicroAPL pioneered the concept of royalty-free runtime APL licences, allowing you to distribute your APL applications without paying licence fees. Version 3 of APL.68000 Level II now makes this even easier by including as standard a ‘Packager’ which turns your APL workspace into a standalone Macintosh application.

### Business Graphics Workspace

The new PlotMac workspace allows you to create simple business graphics with a few easy APL commands, automatically scaling and labelling axes. You can create line and scatter plots; histograms; and pie charts. The graphs can be shown on-screen, printed or exported to other applications.

### Free APL Toolkit

Finally, we have included a copy of the public domain APL Toolkit produced by the Toronto APL SIG which contains a wide variety of useful APL utility functions that will run under all types of APL interpreter.

### Requirements

APL.68000 Level II Version 3 runs on all models of Apple Macintosh, including running in native mode on the PowerMac range, and requires Apple System 7.0 or later. APL.68000 Level II Version 3 will automatically use the hardware coprocessor on those 68000-family Macintosh computers which support 68881/2 operations.

## Soliton Associates Limited

*Viewpoint*, Soliton’s APL-based end-user report generator, previously available only for Sharp APL MVS, is now available for Sharp APL UNIX.

*DBIUtils*, the *Viewpoint* Application Programming Interface, provides APL access to *Viewpoint* data, and allows integration of *Viewpoint* into custom APL applications.

As well as operating upon its own internal databases, *Viewpoint/UNIX* can operate upon external databases, including DB2. Via *NSVP*, Soliton’s *Network Shared Variable Processor* product, *Viewpoint/UNIX* can access mainframe data, including DB2.

## Dyadic Systems Ltd

Dyadic is pleased to report the availability of Dyalog APL/W Version 7 that was announced at the end of April. The new release contains a number of improvements and additional features that were not included in the April announcement.

One of the most important additions is the implementation of a built-in Grid object, which has proven extremely popular among audiences that have seen it demonstrated. Originally Dyadic had planned to rely on third-party custom control objects to satisfy the requirement for a spreadsheet-like editor. However, Grid objects designed for Visual Basic turn out to be highly scalar-oriented and not particularly convenient for APL. Dyadic therefore decided to develop its own built-in Grid object which is tailored specifically for the APL language.

The Dyalog APL Grid looks and behaves like a typical spreadsheet. The body of the spreadsheet is (naturally) a matrix, and individual cells can be numbers, character vector or character matrices. This makes it rather more than a simple numeric editor as it will handle the more commonly used nested array structures too. You can specify your own column titles and row titles or you can let the Grid label them with typical spreadsheet defaults. You can also disable the titles to provide a simple scrolling list. The Grid supports ‘in-cell’ editing or lets you use an external edit field. This is done by providing an association between the Grid and an Edit object; indeed it is possible to associate different Edit objects with different cells. Once this association has been done, APL manages the input entirely automatically; and, because the Edit object now supports Numeric, LongNumeric, Currency, Date and Time fields, APL performs most of the routine validation and formatting for you. The Grid also allows colours and fonts to be specified at the individual cell level, so you can readily customise its appearance.

The second major new feature is the provision of an Auxiliary Processor that allows you to access databases that support the Microsoft ODBC standard. Such databases include Microsoft Access, dBase, Paradox, Oracle, Ingres and Sybase. The Auxiliary Processor has been developed for Dyadic by Insight Systems who are specialists in this field. Insight are also the author of SQAPL which provides similar database connectivity using the SequeLink product, and which is already in production use at a number of large Dyalog APL sites. The ODBC interface from Insight Systems is included with Dyalog APL/W Version 7 at no extra charge and is fully supported by Dyadic and the author. When ODBC drivers begin to appear for Unix systems, Dyadic intends to provide the same functionality for the Unix implementations of Dyalog APL.

Another addition is the provision of a DOSFNS DLL together with a set of complementary APL functions. These functions perform many of the standard tasks of `⎕CMD` without the overhead of starting a new DOS command processor.
