---
title: News from Sustaining Members
authors:
- Gill Smith
volume: '11'
issue: '2'
page: '13'
unindexed: true
transcribed: 'from page images of VOL.11-NO.2-OCTOBER-1994.pdf, pages 15–18 (printed 13–16); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
queries:
- "Printed byline “Compiled by Gill Smith”. The news ends a third of the way down printed 16; the rest of the page is blank."
- "The two SQL queries in the Insight Systems item, printed in italic code type, are set as code blocks. Insight Systems’ Internet address is a company’s and is kept."
- "Kept as printed: “via DDE or as a DLL?” (a question mark ending a statement); “more control structures; including :continue, :leave and :goto”; “SQAPL for APL\\*PLUS III” and “the /EL and /PE versions”."
---

*Compiled by Gill Smith*
{ .byline }

## Dyadic Systems Ltd

Dyadic is extremely pleased with the way the new version of Dyalog APL was received at APL94. Delegates who attended Dyadic’s Vendor Forum (and most did) heard John Scholes give the first presentation of “Namespaces” outside the UK. The reaction from the audience, most of whom were unaware of this new development, was extremely positive.

Namespaces allow you to organise your functions and variables into logical units and sub-systems, just as the DOS directory structure allows you to organise your files. In Dyalog APL, the active workspace is also known as the root namespace; rather like the root directory in DOS. Objects that you create at this level are held in the root namespace, just like files in your root directory. (If you don’t want to use namespaces, you can define all of your objects in the root namespace, just as before.) However, you can also create a namespace (analogous to a sub-directory) in which you can place other objects and indeed other namespaces. There is no limit to the number of namespaces you can have, nor to the depth they are nested.

Namespaces do not just allow you to organise your workspace better, they also act as different contexts for the execution of code. When a function runs in a namespace, the names of variables and other functions to which it refers are local to that namespace, and do not conflict with objects with the same names in other namespaces or in the outer workspace. This means that, for the first time in APL, you can write a self-contained utility or a complete application that can safely be copied into any other workspace and run without fear of name conflicts. Namespaces also make it extremely easy to implement large application workspaces that contain logically separate sub-systems, without the need to resort to overlay files and similar techniques.

Namespaces provide benefits to all APL developers, but are of particular appeal to those developing GUI applications. This is because GUI objects (Forms, Buttons, Grids and so forth) are also namespaces themselves. This means that you can store all of the callback functions, and any data variables that they require, inside the object to which they apply, rather than having them swill around in the workspace. Namespaces provide a much needed solution for the requirement to pass information between callback functions, and between successive invocations of the same callback, without the use of global variables (i.e. variables that are global to the workspace as a whole). Instead, such variables become static variables, that are local to an object (and thus directly accessible from functions running within that object) but do not pollute the workspace as a whole. Furthermore, as GUI objects are namespaces, you can write a completely self-contained GUI widget that contains all the required APL code and data, together with its GUI components, and save it as a single object that can subsequently be copied into any active workspace and run. The user sees only what the object does; not how it does it, a fundamental tenet of object-oriented programming.

Dyadic intends to use namespaces as the basis of further development towards object-oriented programming, and to provide the advantages (but not the complexities) of this approach for Dyalog APL users in the future.

## Insight Systems

So far, the second half of 1994 has left us breathless. After announcing SQAPL for SequeLink at APL93 in Toronto, we slowly sold about a dozen evaluation systems during the next twelve months. A year later, many of these customers are buying 20- to 50-user production systems. The first five beta copies of SQAPL 2.0 with ODBC support went to new customers in Helsinki, London, Melbourne, New York, and Rio de Janeiro. New customers are queuing up, and redistribution agreements are now more or less in place with three major APL vendors. The rumours regarding the death of APL seem to be premature, and the non-APL middleware market seems to be taking off like a rocket too, so we have never been busier.

Dyadic shipped SQAPL/EL with version 7 of Dyalog APL for Windows. The *Entry Level* version contains all the functionality required to get started with simple ODBC drivers for local databases such as dBase or Access. By the time this is printed, we should have completed the *Professional Edition*, which contains a number of additional features to increase programmer productivity, and take advantage of performance options in advanced ODBC drivers, especially when using remote databases. We are now concentrating on assisting Manugistics in the packaging of both the /EL and /PE versions of SQAPL for APL\*PLUS III, and working with Soliton to provide SQAPL for Sharp APL under Unix. We will also provide a version of /PE for J version 2 from Iverson Software, so you can get started on J using a familiar tool for database access. Upon demand, we will make the tool (SQJ?) available for J under OS/2 and Unix, too. Need a copy of SQK? Please call us!

A second generation of servers, based on SequeLink version 2.5, will provide ODBC access to Unix APL servers (and hopefully also APL2 under MVS) by the end of the year. We are also starting work on a local ODBC driver for APL, which will give direct access to Dyalog APL/W and APL\*PLUS III without the use of middleware. This product will also be available before yearend, if all goes well (we need it for a project of our own before that).

The idea of an ODBC driver for a local or remote APL interpreter may seem a bit strange. ODBC is for SQL databases, and the most natural way to call a development tool like APL under Windows would be via DDE or as a DLL? There are dozens of APL applications containing their own databases, which suffer from the fact that their internal databases are inaccessible to mainstream tools. With our ODBC APL drivers, we will provide tools to help you write simple SQL interpreters, so you can let people go into Microsoft Access, connect to APL (which you sold as a high-performance multi-dimensional DBMS) and say:

```
select high, low, close
  from currdb
  where market='NYC'
   and currency='JPY'
   and date>19940101
   and frequency='WEEKLY'
   and totalling='AVERAGES'
```

Although the underlying database may be a four-dimensional table with daily rates, we can return a two-dimensional table with massaged data, pretending that we have an SQL table containing weekly averages. This idea can be extended to all kinds of analyses — so APL can contain infinitely large SQL tables. The ultimate virtual database is the one which allows queries like:

```
select result from apl where expression='2+2'
```

Once more, a change of Internet address. Our address is now insight@inet.uni-c.dk.

## Manugistics Inc

Manugistics released version 1.2 of APL\*PLUS III for Windows almost a week ahead of schedule. We feel this version further positions APL\*PLUS III as the strategic choice for Windows development. Major enhancements found in this release include support for Visual Basic Custom Controls, calling 16-bit DLLs directly, new object classes for MDI application development and more control structures; including :continue, :leave and :goto.

Currently, there are several beta sites testing the ODBC interface developed by Insight Systems for APL\*PLUS III. Reports so far have been very positive and we soon hope to simultaneously release two versions of the product — one designed specifically for the single/ad-hoc user, the other designed for the commercial APL developer who needs to provide an ODBC enabled product with more functionality. For more information on ODBC for APL\*PLUS III, please contact Manugistics, Insight Systems or your local APL\*PLUS dealer.

The Manugistics troop returned safe and sound from APL94. In keeping with the conference theme of “The Language and its Applications”, a commercial application developed in APL\*PLUS III by GEIS called LEX2000 was presented during our vendor forum along with demonstrations of using VBXs and ODBC. Our software drawing winner was Daniel Jonusz of Mobil Oil Corporation in Princeton, NJ and APL\*PLUS Sport Radios were won by three other conference attendees.

A very exciting synergy is developing between our mainframe based enterprise-wide planning product and the APL\*PLUS Network Sharefile product. Two new sites began using Network Sharefile in the past few weeks with more to come. Network Sharefile allows multiple copies of the APL\*PLUS Sharefile system to communicate with one another. A user can be running an application that appears to be using one Sharefile database while a number of Sharefile databases in virtually any location may actually be in use. The benefits of Network Sharefile include better performance and better data security and integrity.
