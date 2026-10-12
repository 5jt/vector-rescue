---
title: News from Sustaining Members
authors:
- Gill Smith
volume: '11'
issue: '3'
page: '7'
unindexed: true
transcribed: 'from page images of VOL.11-NO.3-JANUARY-1995.pdf, pages 9–12 (printed 7–10); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
- data and files
queries:
- "Printed byline “Compiled by Gill Smith”. The news ends at the rule on printed 10; the rest of that page is blank."
- "Kept as printed: “heterogenous/mixed result”; “PC's running APL*PLUS III Windows”; “Version 7” (for 7.1) in “In addition, Version 7 offers an optional APL2-compatible partitioned enclose”."
---

*Compiled by Gill Smith*
{ .byline }

## Dyadic Systems Ltd

Dyadic is pleased to announce Dyalog APL/W Version 7.1 for Microsoft Windows. This is a maintenance release that will be distributed to customers free of charge. It does however contain a significant number of enhancements.

As further evidence of Dyadic's commitment to provide greater compatibility with IBM APL2, Dyalog APL/W Version 7.1 includes the following language enhancements: Enclose with Axes, Take and Drop with Axes, Ravel with Axes, and Strand Assignment with parentheses. These enhancements do not conflict with existing Dyalog APL language conventions and are implemented at all migration levels (defined by the system variable `⎕ML`). In addition, Version 7 offers an optional APL2-compatible partitioned enclose at migration level 3.

The Dyalog APL/W session now supports *drag and drop* editing which is implemented in a manner that is consistent with Microsoft Word for Windows. Drag and drop editing provides a fast and convenient method for moving and copying text (both whole lines and partial lines) within an edit window or between edit and session windows.

Namespaces have been extended in several ways. You may now create a GUI object, such as a Form, as a child of a namespace. Indeed, you can insert a namespace at any level in the GUI hierarchy. For example, you could create a namespace as a child of a Form and then create Buttons and other objects as children of the namespace together with any code and data that the objects need to share. Secondly, namespaces and GUI objects may be stored on component files in their `⎕OR` form. This feature will greatly simplify the management and re-usability of complex objects and provides the basis for the implementation of *class libraries* in the future. Further enhancements to namespaces may also be included in Version 7.1.

The popular Grid object now supports the selection of rows, columns and blocks of cells. A selected block can be cut or copied to the clipboard and pasted back into the Grid. This facility also allows the user to transfer data very quickly between the Grid object and other spreadsheets such as Microsoft Excel. You may also drag a block of cells and drop them elsewhere within the Grid. Individual rows and columns may be resized by the user dragging the row and column title dividers. The user may also have the system resize a row or column to fit the contents of that row or column, by double-clicking the mouse over a divider. All of these operations generate new events to which you may attach callback functions and you may also generate these actions under program control. A new mechanism is provided to control the input mode and the behaviour of the cursor keys. All these features have been implemented in a manner that is consistent with Microsoft Excel.

In addition to these changes, the Grid now allows you to associate Combo and Button objects with individual cells. Combos provide a very convenient means for the user to input one of a series of options and Buttons (particularly Check boxes) provide a good way of making and displaying yes/no choices. As Button objects may display bitmaps, icons and metafiles, you can also use them to display pictures in individual Grid cells.

On top of these enhancements, Dyalog APL/W Version 7 users will find that a large number of minor enhancements have been added. Dyadic intends to ship Version 7.1 during January.

## Insight Systems

Insight Systems is pleased to announce general availability of the *Professional Edition* of SQAPL. In addition to being an interface from APL to SQL, the SQAPL product range allows APL to function at both ends of a Client/Server application. *SQAPL/PE* is available from Insight Systems for Dyalog APL and APL\*PLUS II under Windows and Unix, and for IBM APL2 under OS/2 and Unix. It is available from Soliton for Sharp APL under Unix, and from Manugistics for APL\*PLUS III under the name *APL Link Pro.*

Compared to the *Entry Level* version of SQAPL, which is now also available from Manugistics under the name *APL Link*, and is bundled with version 7 of Dyalog APL for Windows, the Professional Edition contains the following enhancements:

- Support for *SequeLink* drivers as an alternative to ODBC, giving high performance access from Windows, OS/2 and Unix to most popular SQL databases and a number of non-SQL services such as IBM CICS, AS/400 Transaction Programs, or our own SQAPL Server.
- Automatic detection of performance options supported by good ODBC drivers; most significantly block fetch modes, which can substantially increase performance (in one example with a WatCom ODBC driver, an order of magnitude increase in performance for multi-row fetches).
- Support for a number of additional APL data types, in particular date/time columns as Julian day numbers, Quad-TS vectors, or base-100 encoded integers, in addition to the ISO Standard character format.
- The ability to store any APL array in a CHAR or BINARY column, in a format which can be extracted by any other SQAPL/PE client even though data is stored in binary format. This can be used to implement a Component File system, which can be used by all four major APL systems, under Windows, OS/2 and Unix.
- Support for data sets, so that you can extract a (subset of a) table, make changes to it using APL, and then get SQAPL to generate the required SQL to apply the same changes to the underlying SQL table.
- Output data can be *grouped* according to the requirements of your application. For example, you can extract all columns of the same data type in a single cell of output, to conserve space compared to the heterogenous/mixed result returned by the Entry Level product.

For more information, contact us at the address on the back cover, or ask your APL dealer.

We are close to releasing most of the new server products mentioned in our news item in the October Vector. Make sure to get the next issue of Vector to read all about them!

## HMW Trading Systems Ltd

Please note a new Email contact and a change to our phone number:

> Tel: 0171-353-8900; Fax (unchanged): 0171-353-3325<br>
> Email: 100020.2632@Compuserve.com

## Manugistics Inc<br>(UK Re-seller: The Bloomsbury Software Company Ltd)

Manugistics are now shipping *APL Link*, the fast easy-to-use interface from APL\*PLUS III Windows to all of your data. Using Microsoft's ODBC, APL Link lets you access a wide variety of databases on different hardware platforms, you'll be able to write APL programs that use powerful yet simple SQL statements. And because ODBC is an industry standard, you can change databases and your programs will work with little or no modification.

There are two versions of APL Link to choose from: *APL Link* is an inexpensive yet powerful interface from APL\*PLUS III to a variety of databases; *APL Link Pro* is designed for the power user and combines increased performance with advanced functionality including: the ability to execute blocks of SQL statements simultaneously, support for more data types, and the ability to distribute APL Link as part of a run-time application.

Further details from our UK re-sellers:

> The Bloomsbury Software Co Ltd.,<br>
> formerly Cocking & Drury (Software) Ltd.,<br>
> 3-6 Alfred Place,<br>
> Bloomsbury, London WC1E 7EB.<br>
> Tel: 0171 436 9481;<br>
> Fax: 0171 436 0524.

Bloomsbury Software report a number of customers approaching them recently with a view to moving their VSAPL off their mainframes onto PC's running APL\*PLUS III Windows — no previous version of APL having offered them both the ease of migration and the necessary performance to make this exercise a reality. Bloomsbury Software have some tools they developed to help automate this process.

*See our advertisement on page 141 for more details.*
