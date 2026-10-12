---
title: ODBC Client-Server with Morten Kromberg
authors:
- Bronwen Tuffen
volume: '13'
issue: '2'
page: '65'
unindexed: true
transcribed: 'from page images of VOL.13-NO.2-OCTOBER-1996.pdf, pages 67–69 (printed 65–67); Claude, 2026-10-12'
review: draft
tags:
- conference reports
- data and files
queries:
- "Printed heading “ODBC Client Server - Morten Kromberg”, “recorded by Bronwen Tuffen”: notes on Morten Kromberg’s first ODBC workshop at APL96, Lancaster. It begins on printed 65 below the end of “TCP/IP - Timo Laurmaa” and ends on printed 67, the lower part of which is blank."
- "The displayed results of SQATables and SQAColumns are set in code blocks with their printed column layout; the leading 0 is the return code."
- "Kept as printed: the SQAColumns example is called on 'People' but its result lists the columns of the table “lakes”; “a cursor nameed X.i1”; “values(:x:,:y<I:)” (the character after “<” is read as a capital I); “If you want to do slightly more complicated things”; “being used, does or does not support”."
---

*recorded by Bronwen Tuffen*
{ .byline }

Morten Kromberg from Insight Systems ran two workshops on using ODBC with APL. These are notes on the first session which was using APL as the client getting ODBC data from external data sources.

There is a workspace supplied with Dyalog held in the `dyalog/ws` directory called `sqapl.dws` which contains all the functions needed to try these examples. They are a basic set of functions which allow you to connect to, and interact with an external ODBC data source.

**SQAInit** - This initialises the environment for using ODBC and should always be run before starting a session.

**SQAConnect ‘X’ ‘ODBCSource’** - This connects you to the ODBC data source ‘ODBCSource’ and gives the connection a name of X. You can specify any name for this connection and it will be used for all subsequent communication with the data source.

Once you have connected to your data source there is a variety of things you can do. Firstly you can query it to see what information is available there. There are 2 useful query functions.

**SQATables ‘X’** - This returns all the tables available on the data source, and some information about them. The result is 3 elements, of which 2 seem useful. The first is a return code, the second the actual table information.

```apl
0  TABLE_QUALIFIER          TABLE_OWNER TABLE_NAME TABLE_TYPE   REMARKS
   c:\Dyalog95\ws\TestODBC              lakes$     SYSTEM TABLE
   c:\Dyalog95\ws\TestODBC              People$    SYSTEM TABLE
   c:\Dyalog95\ws\TestODBC              SQATST$    SYSTEM TABLE
   c:\Dyalog95\ws\TestODBC              lakes      TABLE
   c:\Dyalog95\ws\TestODBC              People     TABLE
   c:\Dyalog95\ws\TestODBC              SQATST     TABLE
```

**SQAColumns ‘X’ ‘People’** - This returns all the columns available within a table and their data types, again the result is 3 elements, the first being the return code, the second the data and the third appearing unused.

```apl
0  TABLE_QUALIFIER          TABLE_OWNER TABLE_NAME COLUMN_NAME DATA_TYPE
   c:\Dyalog95\ws\TestODBC              lakes      lake               12
   c:\Dyalog95\ws\TestODBC              lakes      distance            8
   c:\Dyalog95\ws\TestODBC              lakes      length              8
```

continued....

```apl
TYPE_NAME PRECISION LENGTH SCALE RADIX NULLABLE REMARKS ORDINAL
TEXT            255    255     0     0        1               0
NUMBER           15      8     0    10        1               1
NUMBER           15      8     0    10        1               2
```

Once you know what is available on the data source there are several ways to extract and manipulate this. The simplest way is `SQADo`.

**SQADo ‘X’ ‘select \* from People’** - `SQADo` passes through a SQL statement to the data source. This can be a select statement, or a create/update/insert statement. Used without a left argument it creates a cursor, prepares the statement, executes it and returns the results. It returns a 4 element result: the first is the return code, the second the cursor name used, the third the data retrieved, and the final one is empty.

If the amount of data you are requesting is large you may not want to retrieve it all in one large lump. In that case you can pass a left argument to `SQADo` of 0. This sets up the cursor and the statement as before but only returns the first block of data, you retrieve the subsequent blocks of data with **SQADo ‘Cursorname’**.

If you want to do slightly more complicated things or have more control over the process then you can use the lower level SQA functions. These allow you to prepare SQL statements (optionally with parameters in them) and then execute the statement a successive number of times in a more transaction-based way. To prepare a statement, execute it and then close the transaction you would need the following functions:

> **SQAPrepare ‘X.i1’ ‘insert into people values(:x:,:y&lt;I:)’** – this sets up the statement with a cursor nameed X.i1.
>
> **SQAExec ‘X.i1’ ‘Joe’ 43** – This runs the prepared statement with ‘Joe’ as parameter x and 43 as parameter y. You would run this for as many lines as you wanted to insert data.
>
> **SQATransact ‘X’ 0** – This is a commit on the transaction. If the ODBC driver you are using supports rollbacks passing in a 1 instead of a 0 rolls back the transaction.

This method can also be used for updating data within a table (optionally the where clause can also be parameterised, e.g. ....**where name=:x:**)

The constraining factor on using this code seems mainly to be with what the ODBC driver being used, does or does not support. The Excel one I tested it with did not seem to support parameters and also seemed to return some numbers in an odd format. Also if running in Dyalog 8 it accesses the 32-bit ODBC so you can only use those data sources for which you have a 32-bit ODBC driver defined.
