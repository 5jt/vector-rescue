---
title: News from Sustaining Members
authors:
- Gill Smith
volume: '12'
issue: '1'
page: '13'
unindexed: true
transcribed: 'from page images of VOL.12-NO.1-JULY-1995.pdf, pages 15–17 (printed 13–15); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
queries:
- "Printed byline “Compiled by Gill Smith”. Printed 16 is a MicroAPL advertisement (“APL for the Apple Macintosh”), not transcribed."
- "Kept as printed: “Expanding our offices and the APL95 conference has left us little time”; “a very pragmatic APLers’ approach”; “Windows95 logo” (beside “Windows 95 logo”)."
---

*Compiled by Gill Smith*
{ .byline }

## Insight Systems

On April 1st, Insight Systems merged with Adaytum Software Ltd. To quote our Press Release:

> Insight Systems ApS, based in Hellebæk, Denmark, announced today a merger with Adaytum Software, one of the UK’s leading providers of Budgeting and Management Reporting software solutions. The merger, which will be in the form of a share exchange, will be effective 1st April 1995.
>
> Adaytum will base its technical development team in Hellebæk, Denmark. Headed by Morten Kromberg, current Technical Director of Insight, Adaytum’s aim will be to attract and build a team of the most talented APL developers available internationally. Their focus over the next two years will be to provide state of the art Client/Server based financial data analysis software solutions. These will complement Adaytum’s flagship product ‘The KPS System’, a multi-dimensional Business Management system, used principally for complex Budgeting, Forecasting and Management Reporting requirements.

The implementation of the merger has kept us quite busy for the last quarter. In addition to the new tasks resulting from the merger, we have seen substantial growth in our consulting business, and as a result we added five people to our headcount during the same period (including three new APL developers). Expanding our offices and the APL95 conference has left us little time for product development, so there is little to announce this time — but now that the situation is stabilizing we will be back in greater strength than ever before.

Our first goal is the completion of the ODBC-compatible version of the SQAPL Server, which will make it possible to “wrap” APL applications in the guise of an SQL database (making APL effectively indistinguishable from for example Oracle, from the point of view of reporting tools). More about this and other new product releases in three months!

## Dyadic Systems Limited

Fresh back from APL95 in San Antonio, Dyadic has begun work in earnest on the next release of Dyalog APL/W. Although plans have not yet been finalised, the following has been decided and was announced at APL95.

Although the current release of Dyalog APL/W (Version 7.1) runs extremely well under Windows 95 preview, a new version of the product (codename Version 7.95) is being developed specifically for Windows 95 and Windows NT. For the technically minded, the new version will be based on Microsoft WIN32 in place of the equivalent Watcom software which Dyadic has used up to now. This software will provide some benefits in terms of improved memory management under NT, but more importantly, is a qualification requirement for the new Windows 95 logo. Of greater interest to most users is that Version 7.95 will include support for all of the new GUI objects and features provided by Windows 95. These include DragList, ListView, ProgressBar, RichEdit, TrackBar, TreeView and Spinner objects.

The *DragList* object is a list box that allows the user to re-order its items. The *ListView* displays items as a set of icons, in a list format or a report format (like File Manager). The *ProgressBar* is a standard output control that indicates the progress of a time-consuming operation. The *RichEdit* control is a multi-line text editor that provides extensive word-processing facilities including mixed alignment, fonts and colours. This control will allow Dyalog APL/W applications to exchange complete documents with Microsoft Word and other word-processors. The *TrackBar* control provides a variety of different sliders for analog user input. The *TreeView* control may be used to display a hierarchy, such as a function calling tree, a namespace tree, or a directory structure.

The new version of Dyalog APL/W will also support OLE2 and .OCX custom controls.

Dyadic intends to be able to provide an early release of the new product on the day that Windows 95 is released by Microsoft. This will allow Dyalog APL/W users to immediately begin to generate Windows 95 compliant applications and to qualify for the new Windows95 logo themselves.

## Causeway Graphical Systems Ltd

I suppose we went to APL95 to get our name known, to get our faces known, and to start convincing some hundreds of sceptical APL developers that we really have hit upon a better way of managing the “concept — prototype — negotiate — build” cycle that characterises effective APL development. To this end, we put our name and Email on the conference pens, we talked at length to the development teams (Dyadic, Soliton, Manugistics, IBM, and Strand), and we threw a party!

Following Dyadic’s example (Manchester, 1986) we ordered more beer than we thought we could possibly need (wrong!) and invited anyone interested to our suite for a Causeway BeerBOF. They left having seen “Distributed Architect” — the tool that SAP are now shipping to selected customers for configuration modelling; they were given a first viewing of the “Rain” business graphics software running under APL\*PLUS III, and they had ample opportunity to grill both Adrian and Duncan on the future of Causeway for Dyalog, APL\*PLUS, APL2 for OS/2, and J.

The key message that we tried to leave people with is that Causeway pays exponentially increasing dividends as the application gets complex! It takes a very pragmatic APLers’ approach to OOPS, and as a result leaves the way open for rapid evolution while enabling small teams to work concurrently on many components of the same project with a minimum of external co-ordination.

In the longer term, we made a good beginning convincing the major APL vendors to start designing into their interpreters all the right hooks to make Causeway run fast. Dyadic are already well on the way with namespaces, but IBM are developing some really interesting ideas using shared variables, and the latest release of J (from Strand Software) at last has the facilities we need.

We should re-iterate that the Causeway utilities are a by-product — we needed something to help us deliver high-quality decision-support tools that we knew we could support and enhance into the future, regardless of APL platform. The architecture and the Dyalog and Manugistics workspaces will remain in the public domain.

P.S. Registered users have already received workarounds for two interesting new Dyalog bugs which we first noticed in 7.1; try executing `⎕NC'inx⊃vec'` having defined `inx`. The quick fix is to clear everything to the right of the `∧` in `Gui_read[21]`. Unfortunately the fix for their new configure bug is not so easy, so if you get an ever-growing button in the designer (try it with *Snap=1*) you will need to register so that we can send you the necessary patch.
