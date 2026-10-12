---
title: 'APL Standards Update'
authors:
- Dave Ziemann
volume: '7'
issue: '1'
page: '124'
unindexed: true
transcribed: 'from page images of VOL.7-NO.1-JULY-1990.pdf, pages 126–128 (printed 124–126); Claude, 2026-10-12'
review: draft
tags:
- standards
queries:
- "Contents line “APL Standards Update”, David Ziemann; the printed heading is “14th ISO APL Working Group meeting, 30 April 90 - 4 May 90, Waterloo, Ontario, Canada”, with the byline “report by Dave Ziemann”."
- "The TeX logo, printed with a lowered E, is given as “TeX”."
- "Printed 126 ends the piece, its lower half blank; “A Survey of ⎕NC” (art10004390) begins on printed 127."
- "Kept as printed: “would not have been possible due the withdrawal”."
---

## 14th ISO APL Working Group meeting<br>30 April 90 - 4 May 90<br>Waterloo, Ontario, Canada

*report by Dave Ziemann*
{ .byline }

### Background

This is a report of the proceedings of the last ISO meeting for the standardisation of APL, which I attended on behalf of the BSI APL Standards Panel. This was made possible by funding provided by the British APL Association, without which British representation would not have been possible due the withdrawal of funding for ISO meetings by the DTI.

I took to the meeting five sets of BSI comments, and a report on symbol conflicts.

The meeting was relatively small, with eight representatives from Belgium, Canada, UK and the USA. A number of regular attendees, the French group in particular, were not able to come due to funding difficulties.

The main technical work of the meeting involved reviewing newly received documents, and working through the 1st Working Draft of the Extended APL Standard, page by page.

### The New Document

The changes to the existing standard are so pervasive that a supplement was not possible, and so a new document was created, based on IS 8485, the existing standard.

The 1st Working Draft was prepared by Eugene McDonnell, the editor, based on the existing standard and twenty-six accepted proposals from the following authors; Eugene McDonnell, Roland Pesch, Everett Allen, Bruce Frost, Greg Jaxon, Joseph de Kerf, Karl Soop, Brent Hawks and Phil Benkard.

The original standard document was produced by Alex Morrow using a version of IBM's Script language. This has now been converted to TeX by Eugene McDonnell with help from a TeX expert, thereby making the document more easily portable.

The topics in the document have not changed substantially since the Princeton meeting; they include, in no particular order: without, GCD and LCM, duplicate/commute operator, table, first-axis join, mixed arrays, use of overbar/underbar in names, replicate, character grade, unique, shared variable extensions, alpha and omega as names, ambivalent defined functions, event handling, transfer form, n-wise reduction, complex arithmetic, left and right, function rank operator, defined operators, `)OPS`, `)NMS`, component file cover functions and a revised Workspace Interchange Standard.

### Changes made at Waterloo

One significant change is in the area of name-class. Joseph de Kerf had earlier presented a review of name classifications in about forty dialects of APL. We had already agreed to use `4` for defined operators, and now Joseph was suggesting that `5` and `6` be standardised for system variables and system functions. In addition, `¯1` should be returned for arguments to `⎕NC` which are not valid names, rather than returning `4` or signalling an unhelpful `DOMAIN ERROR`.

All three changes were passed, with no votes against.

Although the new document did contain grade-up and grade-down extended for character arrays, they had not been defined for numeric matrices and higher rank numeric arrays. A proposal to plug this hole was accepted.

A number of extensive changes were required in order to fit defined operators into the document. Defined operators follow the APL2 philosophy, which means that they are not "true" operators, but are more accurately described as defined derived functions. Defined operators and the new function rank operator will accept defined function operands in the Extended Standard, even though it is not currently possible to generalise this to the existing primitive operators in the language.

The Annex which describes the Workspace Interchange Standard has been upgraded to WSIS2. Although the Extended Standard itself does not address nested or boxed arrays, WSIS2 describes a convention for dealing with them. The Annex is still termed "Descriptive", which means that a conforming implementation is not required to provide the facility.

### The Technical Report

A "Technical Report" is an ISO designation applied to a standard which fails to meet the necessary standardisation criteria. WG3 is using this mechanism to collect all the proposals for which consensus could not be achieved.

The topics to be included in the Technical Report have not changed since the last meeting. They are: reduction, nested arrays and fills, enclose / disclose / box / open, formatting for nested arrays, pick, partition, depth, link, enlist, strand notation, match, generalised primitive operators, compose, dual, first, each, national language characters, function rank in standard metalanguage, function assignment.

The document will contain brief descriptions of why each facility had to be included in the Technical Report, and could not go into the new standard. The Technical Report will be useful for implementors who require guidance, and will provide a strong basis for future standardisation efforts.

### A Warning

Standards committees have a habit of changing their minds. A decision made at one meeting can be reversed at the next; this can happen because the meeting composition varies according to the country in which it is held. Also, people do occasionally change their minds.

For this reason none of the information given in this report should be considered final. Anyone who implements an APL on the basis of pre-publication material takes a big risk. Some implementors fell foul of this in the first APL standard, where an early draft required the `)RESET` system command, which was later changed to the more expressive `)SIC` (SI Clear).
