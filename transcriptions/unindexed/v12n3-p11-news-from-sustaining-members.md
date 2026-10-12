---
title: News from Sustaining Members
authors:
- Gill Smith
volume: '12'
issue: '3'
page: '11'
unindexed: true
transcribed: 'from page images of VOL.12-NO.3-JANUARY-1996.pdf, pages 13–18 (printed 11–16); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
queries:
- "Printed byline “Compiled by Gill Smith”."
- "Causeway’s namespace diagram on printed 15 is given as a code block, its vertical strokes as “|” and the comment symbols as ⍝; the design variable, set in the same italic code face, is given as a code block too."
- "Kept as printed: “end-user products such Lotus 1-2-3”; “APL2000 hope users will view the additional cost as an investment in the future of the product. They do, and are committed …”; “You can either give a simple type declaration such as bool or txt for your property, or you must provide the name of a suitable function”."
---

*Compiled by Gill Smith*
{ .byline }

## Soliton Associates

Soliton Associates is pleased to announce the availability of SQAPL for SHARP APL UNIX. SQAPL provides SHARP APL UNIX with generic client and server interfaces for the Open Systems Environment.

The SQAPL Client provides an interface from SHARP APL UNIX to standard SQL database products such as Oracle, Sybase and DB2. The SQL databases accessed by the SQAPL Client can be on the same computer as SHARP APL UNIX or on network-connected computers. The SQAPL Client allows SHARP APL UNIX to fetch data from SQL servers for use by APL, and to store APL data in SQL servers for use by non-APL applications and standard reporting tools.

The SQAPL Client can also store APL arrays as binary SQL objects with preservation of APL data structure. This allows an SQL server to be used instead of an APL file system as a repository for APL data. The data representation used by SQAPL is APL vendor independent, so that, for example, APL arrays stored by SHARP APL UNIX in Oracle as binary objects can be accessed by Dyalog APL for Windows.

The SQAPL Server provides a generic interface to SHARP APL UNIX server applications. Client applications accessing the SQAPL Server can be ODBC-compliant end-user products such Lotus 1-2-3, Microsoft Excel and Microsoft Access, or they can be custom applications implemented in standard languages such as C/C++, Visual Basic, Digital Smalltalk/V and APL. APL-coded client applications require the SQAPL Client, which is available for SHARP APL, Dyalog APL, APL\*Plus and APL2.

If both components of a client/server application are APL-coded, the client application can use the SQAPL Remote Procedure Call to call the server application. The SQAPL Remote Procedure Call passes APL arrays as arguments, and returns APL arrays as results. SQAPL performs automatic conversion between different APL vendors' data representations, so that, for example, a Dyalog APL client application on a Microsoft Windows platform can call a SHARP APL server application on a UNIX platform.

The networking and interfacing capabilities of SQAPL are provided by SequeLink Data Direct, a product of Intersolv Inc. Soliton Associates distributes and supports SequeLink Data Direct for use with SHARP APL. SQAPL is a product of Insight Systems ApS. Soliton Associates distributes and supports SQAPL for SHARP APL UNIX.

SequeLink Data Direct supports a wide range of database products, hardware platforms and network protocols. The use of SequeLink reduces application development and maintenance effort, and enhances application portability and scalability.

SQL database products supported by SequeLink Data Direct include Oracle, Sybase SQL Server, Microsoft SQL Server, Informix, CA-Ingres, Rdb (for Open VMS), DB400 (for OS/400), DB2 (for AIX, OS/2 and MVS), Adabas and Teradata.

Server platforms supported by SequeLink Data Direct include OS/2, Windows NT, UNIX, Open VMS, AS/400 and IBM MVS.

Client platforms supported by SequeLink Data Direct include Windows, Windows 95, Windows NT, Open VMS, OS/2, Macintosh, UNIX and AS/400.

Networks supported by SequeLink Data Direct include TCP/IP, Novell SPX, NetBIOS, NetBEUI, AppleTalk, APPC and DECnet.

Support for SHARP APL and SequeLink Data Direct is available from Soliton Associates 24 hours per day, 365 days per year.

## APL2000 Inc (Bloomsbury Software Ltd)

APL2000 Inc is a newly formed entity that has acquired certain APL assets from Manugistics. Among the assets acquired were the PC and UNIX APL products.

This was a strategic acquisition on two levels:

- APL2000's core product — LEX2000 Financial Reporting Software — is built in APL. That gives them a powerful vested interest in ensuring that APL's own development keeps pace with other technologies and with market demands.
- Second they believe there is a need to accelerate APL's evolution to ensure that its capabilities keep pace with other languages. They intend to fill that need.

In addition to that announcement there is good news and bad news.

First the bad news — prices are going up (see *Product Guide* on page 34).

And the good news: they will use the additional revenues to fund an aggressive development effort for APL. APL2000 take the position that because the worldwide universe of APL developers is relatively small, current revenues are not sufficient to support the kind of development required to ensure APL's continued viability in the marketplace. APL products will be priced competitively, but it is vital that they generate enough revenue to support on-going development and evolution.

APL2000 hope users will view the additional cost as an investment in the future of the product. They do, and are committed to providing users a return on that investment. They are assembling the most experienced and qualified team of APL developers in the business.

APL+Link provides the connection between APL+Win and data stored in non-APL databases. It uses ODBC connectivity to access a wide variety of databases on different hardware platforms.

For further information contact Bloomsbury Software on 0171 436 9481.

## Insight Systems / Adaytum Software

There is little to report in terms of new products from Insight Systems during the last quarter of 1995. We have ported our products in order to support Dyalog APL Version 8 under Windows 95 and NT, but most of our energies have been spent on version 2.0 of KPS, and growing the company to be prepared to support both KPS and the continued development of our APL Client/Server product line.

1995 has seen Insight Systems more than triple in size from 4.5 persons to 15. The group of APL developers grew from 2 to 6; C developers from 1 to 2. The bulk of this growth happened during the last quarter of the year, coinciding with the rush to meet KPS version 2.0, so this quarter has taught us a new meaning of the word "busy".

Our first major product release in 1996 will be version 2.0 of KPS, Adaytum's flagship product for multi-dimensional business planning. Version 2.0 is the first full Windows version of KPS; a Windows 'Multiple Document Interface' product which will be based on Dyalog APL version 7.2 under Windows 3.1 and OS/2, and version 8.0 under Windows 95 and NT. This and future versions of KPS will rely heavily upon the Client/Server product line, which will also be enhanced significantly during 1996 as a result of our own requirements in addition to those of our customers:

> KPS Version 2.0 will make use of the Insight Systems' SQAPL Client product in order to provide read/write access to ODBC data sources. Product releases scheduled for the 2nd and 3rd quarters of 1996 will use the SQAPL Server and SequeLink Client/Server Middleware to provide access to the KPS engine as an ODBC data source.
>
> KPS will use APL Pipes for internal messaging in multi-user environments to provide "groupware" functionality. Finally, the upcoming extension of APL Pipes to support Visual Basic and C DLL Client modules will be used to provide access to the KPS Macro Language from development tools such as Visual Basic, Borland Delphi, or C.

The sales and marketing side of the company has seen the same rate of growth as has development. We have built new sales teams to market KPS and SequeLink in Scandinavia, and continue to market SQAPL in conjunction with SequeLink worldwide. If you are having problems keeping track of this growing portfolio of products and services, remember to set a week aside at the end of July to visit us at APL96 in Lancaster, where we will provide you with the opportunity to see presentations of, or take part in, hands-on workshops using our products.

## Dyadic Systems Limited

Dyadic has received an excellent response to its Version 8 Preview Program for Windows 95 which is now closed to new subscribers.

Although Version 8 for Windows 95 and NT is Dyadic's flagship product, the company recognises the need to provide ongoing support and further enhancements for Windows 3.1 and OS/2 users. It has therefore announced Dyalog APL/W Version 7.2 to meet this requirement. Version 7.2 will include all of the enhancements provided in Version 8 with the exclusion of those that rely on features found only in Windows 95 and NT 3.51. Version 7.2 is intended for Windows 3.1 and OS/2 but will also run under Windows 95.

The following enhancements, already finished or under development in Version 8, are just some of the new features that will also be provided in Version 7.2:

- New Native File System (`⎕NCREATE`, `⎕NTIE`, `⎕DR` and so forth).
- Control Structures.
- A search path mechanism coupled with a facility to control the export of objects from namespaces. Among other benefits, this avoids the need to specify full pathnames for utilities stored in namespaces.
- Various enhancements to the Grid object including multi-level titles, extended formatting and support for graphics.
- A facility to attach and detach a GUI structure to and from a namespace without destroying any functions and variables it contains. This enhancement simplifies the maintenance of GUI objects as namespaces.
- The capability to draw graphics inside any GUI object that has its own window. This allows you to embellish standard controls such as Buttons and Combo boxes with your own graphics.

Version 7.2 and Version 8 will share a common set of manuals which will be available during the first quarter of 1996. A limited number of copies of version 7.2 will be available for testing during January but upgrade pricing has yet to be finalised.

## Causeway Graphical Systems Ltd

Since November, we have been fully occupied in turning Causeway for Dyalog/W into a fully-supportable, professional package suitable for major APL sites to include alongside other development and object-management tools. We have been greatly helped by the use of *namespaces*, as the Causeway class table now becomes a much simpler and more comprehensible structure:

```apl
#.Gui ---+          ⍝ All the Gui functions are now here
         |
         #.Gui.classes ---+        ⍝ All classes are here
                          |
                          #.Gui.classes.ac     ⍝ Action Button
                          |
                          | functions (such as Disable)
                          | variables (property defaults)
                          | documentation (e.g. design)
```

This makes it possible to view and modify class code with the standard Dyalog editor, which obviously makes classes very much more accessible to APL application developers. It also becomes very easy to integrate this structure with your in-house utility management, as a namespace can be written as a file component, and also retrieved with minimal delay into the workspace.

The `design` variable is another important step towards openness:

```
[General]
name=Action Button
type=Buttons

[Properties]
Appearance=*
Behaviour=*
Accel=txt
Default=bool
Bitmap=txt
Hint=txt
Tip=txt

[CueCard]
... descriptive text goes here
```

The new Causeway designer groups objects by type (rather than just accumulating new ones under 'Special') and it offers all the allowed properties of an object in a grid structure, similar to Borland's 'Object Inspector' as found in Delphi. You can either give a simple type declaration such as `bool` or `txt` for your property, or you must provide the name of a suitable function. In this case the grid will just have a button to call your own code, which can do whatever is necessary to maintain the property.

This effectively removes the need for object-specific styles in `∆styletab`, leaving only global settings such as font and colour. It also allows all objects to have a local event table, which reduces `∆events` to a much shorter (and unchanging) table of truly generic events such as MouseDown. The effect will be to decouple the Causeway architecture completely from class and application code, allowing us to maintain and improve the `Gui.xxx` functions (including the designer) while users can enhance and modify classes quite independently.

In order to allow for future change, we have restructured the dialogue box definition (hopefully for the last time) as a five-column array. Columns 1-4 remain as they were (Class ID, Caption, Position, Size) and column 5 now contains a set of Property-Value pairs, one pair for each non-null property listed in the class's design documentation.

Clearly, this is much easier to extend, and will allow Causeway to accommodate new concepts such as Hint and Tip cleanly. We will also take the opportunity to fix all the little anomalies such as the ordering of the columns in the event table (see Jan Karman's review) which have accumulated over the years.

Naturally, Causeway II will be shipped with a full set of utilities to find and migrate existing dialogue boxes, and to assist in moving class code from `∆classtab` into the new namespace structure.

We have already shipped a namespace version of the *Rain* graphics software to selected users for testing, and will have this ready to go out with Dyalog 7.2 this month. We are also nearly ready to ship a major new set of printing utilities (working title *NewLeaf*) designed to bring the same quality and ease of use to report-preparation from APL.
