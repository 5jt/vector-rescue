---
title: News from Sustaining Members
authors:
- Gill Smith
volume: '11'
issue: '4'
page: '14'
unindexed: true
transcribed: 'from page images of VOL.11-NO.4-APRIL-1995.pdf, pages 16–18 and 160 (printed 14–16 and 158); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
- system interfaces
queries:
- "Printed byline “Compiled by Gill Smith”. The Dyadic Systems item is printed on 16 as “... please turn to page 158” and continues there under the heading “Sustaining Members’ News: Dyadic Systems Limited”; the continuation is transcribed here in place. The rest of printed 16 is blank."
- "Kept as printed: “This include 'methods'”; “were Oracle database”; “will allow ⎕WI access information”."
---

*Compiled by Gill Smith*
{ .byline }

## Causeway Graphical Systems Ltd

Adrian Smith and Duncan Pearson have set up Causeway to enable them to work full time on Causeway application development. The company is based in Malton, North Yorkshire, and has two clear aims:

- to use Causeway (under Dyalog/W or APL\*PLUS III as appropriate) to build high-quality decision-support tools with a true Windows 'look and feel'.
- to offer a professional level of support and training for the Causeway platform to APL sites needing an effective, reliable and future-proof environment for in-house development under Windows.

Over the first two or three years, we shall spend at least 60% of our time developing configuration and decision-support tools for the German software company SAP. The first of these will be included with release 3.0 of their R/3 product later this year. At APL95 we will provide Causeway for APL\*PLUS III, and also for Dyalog APL/W version 7.1 (fully exploiting namespaces and other 7.1 features).

*The Causeway architecture will remain in the public domain, and the new version of Causeway for Dyalog/W will be bundled free of charge with the interpreter.*

## MicroAPL Limited

Our last major upgrade to the Macintosh versions of APL.68000 Level II was released last summer when we announced support for the new Power Macintosh computers and also added a significant number of new features to the product.

We are now testing a further upgrade to our Macintosh versions of APL.68000 Level II and customers will shortly be receiving full details of the upgrade. This upgrade combines some features found in our RISC/System 6000 version of APL.68000 together with some additional enhancements to the `⎕WI` system function.

We have added the family of native file systems functions that are already available on our APL.68000/X product for the RISC/System 6000. These functions include `⎕NCREATE`, `⎕NERASE`, `⎕NLOCK`, `⎕NNAMES`, `⎕NNUMS`, `⎕NREAD`, `⎕NREPLACE`, `⎕NTIE`, `⎕NUNTIE`, `⎕NWRITE`.

Our APL component files on the Mac are now automatically multi-user, with users able to change their user ID via a preference dialog. We have also allowed users to specify the name for the APL component file and HELP file.

The `⎕WI` interface has been enhanced in a number of ways - we have added a new read-only property - class (the class of an object). The delete method is tolerated for non-existent objects (for better APL\*Plus compatibility and ease of programming). A new Printer object allows control of the printer using `⎕WI`. This include 'methods' for printing text, putting up a page dialog and a job dialog, plus properties for font, page size etc. We have added multi-select list boxes and multi-column list boxes. The new 'System' object will allow `⎕WI` access information such as screen size.

Finally we have added official support for Auxiliary Processors written in C. This last feature has been available for some time on an 'as required' basis but is now included with the interpreter.

In addition, all bugs reported to us have now been fixed.

## Manugistics Inc

One of the comments that Manugistics hears a lot from its customers is "How can we promote the use of APL more?" It seems that while some of us have found the value in this language, many others are still using less powerful tools. In talking with many of the APL special interest groups, we believe that with the support of these groups and a good shareware version of APL we could all spread the word to more people. In order to support this effort, Manugistics plans on making available a shareware version of its APL\*PLUS PC product. We intend to begin the distribution of this product through the APL special interest groups. We feel that with the support of a local group of APLers, new APLers can be found and trained.

This shareware version is a fully functional APL\*PLUS interpreter with no artificial limitations. It will run under DOS, Windows or OS/2 in the 640K of RAM that DOS provides. There are 6 chapters of basic APL language documentation included online; this documentation was written specifically to address the needs of brand new users.

If you are interested in helping us to make this available to the community, please stop by the Manugistics booth at APL95 in San Antonio, TX or contact us directly at +1-301-984-5468. We hope to see you at APL95!

## Insight Systems

By the time this is in print, we expect to be shipping the first copies of version 2.0 of our SQAPL Server for Unix. Version 2.0 will be based on the new SequeLink "Link Engine", which supports ODBC drivers under Microsoft Windows and on the Macintosh. By the middle of 1995, version 2.0 will allow you to turn APL databases or applications implemented using almost any APL interpreter running under Unix, Windows NT or OS/2 into "black boxes", which will appear to other applications as industry-standard ODBC data sources, as if they were Oracle database. Instead of moving APL data into a relational structure, losing flexibility and performance, we can now make data in APL files available to other applications *on their terms*. We believe that this opens up a lot of new opportunities for APL-based applications, which can be presented as open, "mainstream" products.

For "pure" APL-to-APL distributed applications, we are introducing a new product, which is already being tested by a few customers under the project name *"APL Pipes"*. The APL Pipes product does not use SequeLink for transport, but is based directly upon TCP/IP "sockets". As a result, it is available not only under the server operating systems supported by SequeLink, but also under plain Microsoft Windows. APL Pipes allows a single APL task or workspace under Windows, Windows NT, OS/2 or Unix (if you need VM or MVS support, please call) to support several clients simultaneously. APL Pipes supports transfer of APL objects of any type, rank, shape (and almost any size) between clients and servers which may be based on different APL interpreters. For example, you could use the product to call an APL\*PLUS server to read (or write) component files from a Dyalog APL client application (and vice versa). For developers wishing to use C or other compiled languages, we will also supply a library which allows APL servers to be called from such environments, effectively making any APL interpreter available as a C library (or DLL under Windows).

## Dyadic Systems Limited

... please turn to page 158

### *Sustaining Members' News*: Dyadic Systems Limited

The latest addition to Dyalog APL/W is a new system function `⎕CS` (Change Space), a significant enhancement to the namespace concept. Dyalog APL namespaces allow you to organise your workspace in a similar manner to the way you may organise your disk into different sub-directories. However, this is not all that namespaces do and perhaps more importantly, namespaces provide *separate execution contexts* in which your APL functions run.

For example, if you make a namespace called `MODEL` in which you install a function called `CALC`, when you run `MODEL.CALC` the function sees only the other functions and variables within the `MODEL` namespace and avoids potential name conflicts with other workspace objects. This is exactly right if `MODEL` represents a self-contained sub-system, but what if `MODEL` represents a particular scenario and you have several other namespaces; `PLAN`, `ACTUALS`, `FORECAST`, and so forth, containing similar, but independent scenarios, that you want to analyse. One thing you do not want to do is to maintain copies of `CALC` and any sub-functions it calls throughout your namespaces, except where the functions differ. This is where `⎕CS` comes in.

`⎕CS` provides a mechanism for a function to switch its execution context. This means that your `CALC` function can switch into the `PLAN` namespace if you want to analyse the `PLAN` scenario, or into the `ACTUALS` namespace if you want to use actual data. Functional differences between the way certain calculations are performed can be handled by having different sub-functions within the different namespaces. Functions that apply to all scenarios can be exported to the target namespace (the one that `⎕CS` switches into) by specifying their names in its optional left argument.

This technique lets you implement a class of objects (in this case a planning system) as a namespace (`MODEL`) which contains the base data variables (properties) and functions (methods) that define the behaviour of the class itself. Instances of the class are represented by other namespaces `PLAN`, `ACTUALS`, `FORECAST`, which contain just the *differences* (different data and perhaps some different calculation routines) between each scenario and the class itself. The main calculation routines exist only in the `MODEL` namespace. When you execute `MODEL.CALC`, you supply the name of the instance namespace in which it is to run. `CALC` then uses `⎕CS` to switch into the desired instance namespace, taking with it any class data and sub-functions that it needs.

This technique is not the only way to solve problems of this sort, but it adds yet another powerful tool to your armoury and is a further step towards the goal of object-oriented APL.
