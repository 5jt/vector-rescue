---
title: Namespaces and ⎕SE
authors: []
volume: '11'
issue: '4'
page: '119'
unindexed: true
transcribed: 'from page images of VOL.11-NO.4-APRIL-1995.pdf, page 121 (printed 119; within Technical Correspondence, the first letter, before “More on APL 2.5”); Claude, 2026-10-11'
review: draft
tags:
- implementations
- development practice
queries:
- "The letter is signed only with a personal e-mail address (at tie.metsa.fi), dated 3rd March 1995; the address is omitted, so no author is given."
- "Kept as printed: “about been run in a namespace”."
---

*From: [e-mail address omitted], 3rd March 1995*
{ .byline }

Concerning the Dyalog session-file, I seem to be adopting a minimalist approach! I don’t use any named `session.dse`; what I need I will load into a namespace under `⎕SE` dynamically from a set of little utility workspaces, that are saved and maintained in a quite traditional manner. The functions in them don’t know a thing about been run in a namespace. (Most of them can be used as well under version 6.3.)

My APL loads in at the start a little workspace consisting only of a `⎕lx` that moves the most generally used fns & idiomlike stuff (those `ROWFIND`s) to `⎕SE` to be always available. Among those is a two-line function `WS2NS` by which I’m able to load dynamically whatever tool-ws to a namespace under `⎕SE` or `#`. This gives me the functionality, keeps my application workspace clean and allows me to get rid of the tool whenever space is needed, or if there is no use for it anymore.

There is nothing very brilliant or clever in this, but to me it seems to work perfectly, and brings me the advantages that I consider most relevant in the namespace-concept.
