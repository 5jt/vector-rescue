---
title: Mainframes, Micros and Co-existence, May 28th 1985 (meeting notes)
authors:
- Adrian Smith
volume: '2'
issue: '1'
page: '59'
unindexed: true
transcribed: 'from page image of VOL.2-NO.1-JULY-1985.pdf, page 61 (printed 59; the AGM meeting; Fieldsend’s paper, art10003160, follows on p.60); Claude, 2026-10-05'
review: draft
tags:
- system interfaces
- implementations
queries:
- "The introductory notes (p.45) say these are Eileen Dyson’s and Adrian Smith’s brief notes on the AGM meeting; the byline is “by Adrian Smith”."
- "Printed “APL*PLUS” with an asterisk; transcribed with an escaped asterisk."
---

The Royal Over-Seas League

by Adrian Smith
{ .byline }

## Introduction

Here we had two papers along very much the same lines. Graham Fieldsend and Dave Chivers both explored different aspects of the problem of sharing data and workload between mainframes and PCs.

Graham Fieldsend (Tesco) set out the basic problem. They have APL\*PLUS on both mainframe and PC, and they find that:

- users only want one terminal
- they want to get at mainframe data on their own machines
- they need to use APL systems downloaded from the mainframe.

By installing the IRMA board in the PC, and acquiring a good deal of ancillary software, they can answer most of these needs. However the installation was not without problems, and downloading APL workspaces is not straightforward. There is also a problem with the timings, as it can take several hours to ship a 1 megabyte file through standard IRMA (there are quicker ways of doing it however) and around 2 hours to reconstitute an APL workspace (100K) once it has arrived.

Dave Chivers talked more in terms of local networks with a single gateway to the outside world. These tend to be high bandwidth (hence very fast) as long as you are talking about PCs on a single site. In his view local processing will continue to increase in importance and the need for remote processing will decline except for occasional access to data bases.

Networks are getting faster, cleverer, more secure and more flexible year by year. Soon the network will itself be able to dial up, sign on, and fetch data from a remote database, all quite transparently to the user. However there are some snags to watch for: errors become much more important when vast amounts of data are automatically getting booted around the place; security is obviously a big headache; modems need to get a lot friendlier. However in spite of these worries, Dave was in little doubt that the future will see a significant move towards LANs and Gateways.

The discussion centred round the problems of getting all this hardware and software to co-operate on a variety of different combinations of mainframes, operating systems and PCs. There was also the question of cost effectiveness: are users shipping data up to PCs simply because they already know and understand Lotus? Would we do better to keep the processing close to the data source by providing better mainframe software?

Finally what about those amazing compact discs? Is the GPO an adequate network when you can ship Gigabytes per day for the cost of a first-class stamp? The answer appears to be ’yes’ as long as you don’t need to cross an international boundary. Customs folk happily ignore data travelling down wires, but tend to be upset by the same data in visible form. Pity.
