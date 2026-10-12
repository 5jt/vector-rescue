---
title: 'Editorial: Namespaces'
authors:
- Jonathan Barman
volume: '7'
issue: '2'
page: '3'
unindexed: true
transcribed: 'from page images of VOL.9-NO.2-OCTOBER-1990.pdf (misnamed: Vol.7 No.2), pages 5–6 (printed 3–4); Claude, 2026-10-12'
review: draft
tags:
- language design
- implementations
queries:
- "Printed 4 also carries a short notice, “Overseas APL User Groups”, below a rule after the editorial; it has no Contents line and is kept here under its own heading."
- "The photograph is kept as a greyscale image."
---

*by Jonathan Barman*
{ .byline }

Namespaces and Packaged Workspaces have been available with IBM's APL2 for a number of years but surprisingly little has been published about their concepts and uses. This issue of Vector contains reports of the June meeting which was devoted to packaged workspaces, plus some additional tutorial material.

In traditional APL, a Workspace has a Symbol Table, which records all the names used, together with special internal information such as the location of the objects in memory. A Namespace is the term used for a set of names defined by a Symbol Table, which in traditional APL is not very interesting because this is exactly the same as a Workspace. However, in APL2 one can have more than one Namespace available, each with its own Symbol Table. The system function `⎕NA` (Name Association) can be used to access objects in different Namespaces. Workspaces are packaged up into a standard load module format to make them available for use as a Namespace, hence the term 'Packaged Workspace'.

![Jonathan Barman](v7n2-p3-editorial-namespaces/jonathan-barman.jpg)

*Jonathan Barman*
{ .caption }

Namespaces solve many of the problems that have beset the commercial application of APL systems, the main ones being the distribution and maintenance of standard utility functions and the management of global variables in large applications.

The management of utility functions is now very straightforward. All that is needed is a simple name association, using `⎕NA`, to a central packaged workspace. Should a utility function need maintenance, then there is only one copy to be changed, and everyone automatically gets the latest copy when they next load their workspace. File based function libraries, or complex copying procedures, can be thrown out of the window.

Global variables are always a worry, it is so easy to alter them inadvertently or to mask them with a local name. Namespaces make it possible to ensure that global variables are kept in a separate watertight compartment. For example, it is usually necessary to keep printing information such as page size and destination in global variables. Keeping all the printing functions in a separate Namespace means that these globals can be completely protected from the outside world.

Workspace listing functions are notorious for their bizarre local variable names and monolithic structure. They are deliberately written that way in an attempt to avoid any conflict with the names used in the workspace being documented. With `⎕NA` a suite of workspace documenting functions can be written in a sensible, easily maintainable way with no name clash problems.

Understanding the exact way in which namespaces can be used and manipulated takes rather longer than expected. I think that the reason for this is that there are virtually no sample applications available for study. The documentation supplied by IBM accurately describes what is available, but the worked examples tend to concentrate on the more complex aspects so that the elegance and simplicity of the underlying concepts tend to get lost.

I think that the namespace concepts can make a material contribution to writing systems which are both secure and easily maintainable. I hope that vendors of other flavours of APL will consider implementing equivalent facilities. This is a major new feature for APL which should help to promote its use for commercial systems.

---

## Overseas APL User Groups

The Vector working group are anxious to maintain contact with as many overseas associations as possible. If you are running an APL group and would like to receive Vector in exchange for your own newsletter or journal, please contact Alison Chatterton at the address on the inside back cover. We will endeavour to compile and maintain an accurate list of contacts of overseas groups, and publish this regularly with our APL Product Guide.
