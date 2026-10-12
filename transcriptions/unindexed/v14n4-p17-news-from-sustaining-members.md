---
title: News from Sustaining Members
volume: '14'
issue: '4'
page: '17'
unindexed: true
transcribed: 'from page images of VOL.14-NO.4-APRIL-1998.pdf, pages 19–20 (printed 17–18); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
queries:
- "No byline is printed. The piece has two items, from Dyadic Systems and Causeway Graphical Systems; printed 19 begins the Product Guide."
- "Kept as printed: “which in Dyalog APL, may be used to clone”."
---

## Dyadic Systems Ltd

Dyadic continues to release a steady stream of enhancements to Dyalog APL, which are immediately available to DSS subscribers as downloads from http://www.dyadic.com.

APL users throughout the world have long been accustomed to the component file system (`⎕FSTIE`, `⎕FREAD`, `⎕FAPPEND` etc.) and the native file system (`⎕NTIE`, `⎕NREAD`, `⎕NAPPEND` etc.) which are supported by most modern implementations of APL. Recently, Dyadic has implemented two apparently small but significant extensions to these file systems. These extensions are *upwards compatible*, i.e. existing APL code will work unchanged.

The first extension is to provide for the automatic allocation of a *tie number*. If you specify 0 as the right argument to `⎕FCREATE`, `⎕FTIE`, `⎕FSTIE`, `⎕NCREATE` and `⎕NTIE`, Dyalog APL assigns the next available tie number and returns it as the result of the system function. This avoids the need to calculate the tie number yourself. More importantly, it is an atomic operation and a *safe* method of obtaining a tie number when your workspace is attached to a number of concurrent users as may be the case if it is acting as an OLE Automation server or a Web server.

The second extension is that all component and native file system functions that did not previously return a result, now return a *shy* result. (A *shy* result may be assigned to a variable, but if it is *not* assigned, the result is *not* displayed). This means that you can perform several file operations in a single expression; for example, to delete a component file called `TEMP` you can use the expression:

```apl
'TEMP'⎕FERASE 'TEMP'⎕FTIE 0
```

which is much neater than doing:

```apl
TIENO←1+⌈/0,⎕FNUMS
'TEMP' ⎕FTIE TIENO
'TEMP' ⎕FERASE TIENO
```

This extension permits more convenient use of file system functions in dynamic functions. For example, a dynamic function `RENAME` to rename a file could be expressed as follows:

```apl
RENAME←{
     ⎕NUNTIE ⍺ ⎕NRENAME ⍵ ⎕NTIE 0
 }

'NEW' RENAME 'OLD' ⍝ Rename file from OLD to NEW
```

Another important change is an enhancement to the `⎕OR`, `⎕NS` and `⎕WC` system functions, which in Dyalog APL, may be used to *clone* or make an *instance* of a namespace (or GUI object); for example:

```apl
'Instance'⎕NS ⎕OR'Class'
```

This creates a new namespace called `Instance` which contains all of the objects (functions, variables and sub-namespaces) defined in the namespace `Class`. However, the objects are not actually *copied* from `Class` into `Instance`. Instead, `Instance` merely contains *pointers* to the objects in `Class`. Only when you change an object in `Instance` will it be de-coupled from the original object in `Class` and consume additional workspace.

This enhancement makes it practical to create large numbers of instances of namespace objects (e.g. an OLE Server) and to make extensive use of *inheritance* in your applications.

## Causeway Graphical Systems Ltd

We are delighted to announce that Joachim Hoffmann (of J Austria) has agreed to work with us for a year — this brings us up to the team size that we always felt was 'about right' in terms of productivity and minimal management overhead. Joachim will continue to support his Austrian customers from our Malton office, as well as bringing J expertise and a thorough knowledge of the Dyalog Gui to our team.

The *CausewayPro* documentation (Tutorial and Reference Manual) will be following this Vector to the printer. It will be posted on the web site in HTML format and will be mailed out to existing customers very soon after you read this. Additional classes (for example a simple wrapper for the editing capabilities in *RainPro*) will be available as add-ins from our web site, priced between £25 and £50 depending on complexity.

The latest version of *RainPro* is also available on the web to all customers on current maintenance (call us for the ZIP password). This supports graphical data editing (line-graphs and barcharts only for now), drill-down, and in-place update of data series, headings and labels. We are also working on OpenGL support for the 3D charts and expect to have a demo version available in Rome.
