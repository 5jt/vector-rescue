---
title: An IBM Bug to watch for, when moving to APL2
authors:
- John Warden
volume: '5'
issue: '4'
page: '96'
unindexed: true
transcribed: 'from page images of VOL.5-NO.4-APRIL-1989.pdf, page 98 (printed 96; within Technical Correspondence, the first letter under the section heading); Claude, 2026-10-11'
review: draft
tags:
- development practice
- system interfaces
queries:
- "A letter in Technical Correspondence, From: John Warden, 16 May 1989, signed John E Warden. It is followed by David Piper’s “An Ambivalent Operator” (unindexed/v5n4-p96-an-ambivalent-operator.md)."
- "The writer’s home address in Hungerford, Berkshire, is omitted."
---

*From: John Warden, 16 May 1989*
{ .byline }

I would like to draw your attention to a major programming bug in some of the public workspaces distributed by IBM with VSAPL, which only becomes apparent when systems developed using certain of IBM’s utility functions are migrated from VSAPL to APL2.

The problem is in the function OPEN, which is found in all of the utility workspaces for handling AP126. On line 3 of this function is a conditional branch to LO. However, there are two lines labelled LO, lines 6 and 18. In VSAPL, if there are duplicated labels, branching is to the first occurrence, in this case to line 6. This is the correct path through the function so no error occurs. However a problem arises when workspaces which use this function are migrated to APL2. In APL2 the action taken when there are duplicated line labels is to branch to the highest line number. In this case the branch would be to line 18. This line issues an error message and exits the function.

The label LO on line 18 appears to be redundant as there is no apparent reason for a branch to this line. The solution is to check all workspaces migrated to APL2 from VSAPL which contain the IBM utility functions for communicating with AP126 for the existence of the OPEN function and edit it to remove the label on line 18.

Yours faithfully,

John E Warden
