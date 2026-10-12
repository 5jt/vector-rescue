---
title: Controlling Real-time Processes in a Brewery (with APL)
authors:
- Robert Poate
volume: '5'
issue: '1'
page: '64'
unindexed: true
transcribed: 'from page images of VOL.5-NO.1-JULY-1988.pdf, page 66 (printed 64); Claude, 2026-10-12'
review: draft
tags:
- applications
- system interfaces
queries:
- "The Contents page gives the title “Real-time Processes in a Brewery”; the printed heading is “Controlling Real-time Processes in a Brewery (with APL)”, with the byline “notes on a talk by Robert Poate (MicroAPL)”. The notes’ writer is not named."
- "Printed 65 carries a separate piece with no Contents line, “BAA Technical Meeting 25th March 1988 at the Royal Over-Seas League”, notes by Adrian Smith; not transcribed here."
---

*notes on a talk by Robert Poate (MicroAPL)*
{ .byline }

Robert Poate of MicroAPL talked about an application in an area which ordinary APL programs don't normally reach, namely real time control of a continuous flow process. The continuous flow in this case was kegged beer in Romford Brewery, a large plant with a capacity of 1 million kegs per year in a series of highly automated lines. The task which Robert undertook on behalf of MicroAPL was to install a management information system which draws its data from 8 plc's (Programmed Logic Controllers) located at strategic points in the keg-filling operation, and feeds it via RS232 links to a MicroAPL Spectrum running the Mirage-2 operating system.

This allows event handling and multitasking between 9 jobs, one corresponding to each of the plc's and the ninth to a filer job which makes updates to a series of rolling files every 15 minutes. These files contain the material for reports on production and rejects, as well as the current status of each of the filling lanes. About 4 days worth of such files are retained on disk, and the filer job runs a daily compression program which writes a consolidated day file. The total amount of data so stored is about 6 megabytes every 4 days. The shared memory which the Mirage system allows between the communicating jobs works like APL shared variables, and is much faster than a RAM disk.

The effect has been to provide management with a massive amount of information in the form of graphs and tabular reports. Among other things, it has allowed them to monitor cumulative production closely against target patterns. It has also given them the means to discover (for example) which depots have a habit of returning kegs the wrong way up, and a recent inference from the data led to the discovery of a CO<sub>2</sub> leak before a substantial loss had occurred.

With factory networks appearing more and more commonly, this sort of application is clearly one of which a lot more instances will be seen, and it is pleasing to know that APL is capable of supporting its share of the action. Robert concluded by making a plea to writers of such systems to make them highly extendable, a quality which APL makes it easier than most languages to instil.
