---
title: Property Names in APL+Win
authors:
- David Siegel
volume: '15'
issue: '4'
page: '77'
unindexed: true
transcribed: 'from page images of VOL.15-NO.4-APRIL-1999.pdf, pages 79–80 (printed 77–78; within Technical Correspondence, the first letter under the section heading); Claude, 2026-10-11'
review: draft
tags:
- system interfaces
- user interfaces
queries:
- "A letter in Technical Correspondence, From: David Siegel, March 1999, with a reply in italics signed “Jonathan” (Jonathan Barman, whose article “VideoSoft FlexGrid Pro with APL+Win” in Vector 15.3 it corrects); the first letter in the section, followed by Norman Thomson’s “Iterated Function Systems”."
- "Kept as printed: “both with AND without”; “APL+WIN” beside “APL+Win”; “the leading x X or onX”."
---

*From: David Siegel, March 1999*
{ .byline }

In Vector Vol.15 No.3, Jonathan Barman (in his article “VideoSoft FlexGrid Pro with APL+Win”) stated:

> “APL+Win requires that you prefix any OCX control properties with an ‘x’, methods with an ‘X’, and events with an ‘onX’.”

This is incorrect. For both OCX and COM interfaces, the properties are exported both with AND without the prepended ‘x’, ‘X’, or ‘onX’. The only exception is where an OCX control (or COM object) has a method, property, or event whose name duplicates one of the standard APL properties, methods, or events. For example, “size” is a standard APL property. If an OCX control exposes a ‘size’ property to which you wish direct access, you must use ‘xsize’ because a reference to ‘size’ will refer to the APL standard property (a cover for a Windows standard interface). However, a property such as ‘FixedCols’ may be accessed either as ‘FixedCols’ or as ‘xFixedCols’ since this is not the name of a standard APL property. Use of the latter guards against the (rather unlikely) possibility of a standard ‘FixedCols’ property being added to all APL+Win objects in some future release, of course.

This is a minor point, but it was mentioned as a difference between the Dyalog APL and APL+WIN interfaces. The actual difference is that as Dyalog exports all names without a prefix, access to the standard properties is lost if the control defines a property with the same name, whereas APL+Win permits access to either the standard property, or to the control-specific property in such cases.

David E. Siegel Software Developer, LEX2000 Inc (a COGNOS affiliate)  
[Associated with APL2000]

*I have no doubt that this is true, but the only help I could find was in Refv3c04.doc in the paragraph headed “Properties of an OCX Control” where it states: You can use the properties of an OCX control in APL GUI by prefixing their names with lowercase letter x. Similar statements about the X and onX are made in the “OCX Methods and Events” paragraph. I cannot find the fuller explanation given by David Siegel anywhere in the manuals.*

*It seems much safer to include the leading x X or onX in case a new property, method or event is introduced into APL+WIN which might mask the OCX property method or event. Jonathan*
