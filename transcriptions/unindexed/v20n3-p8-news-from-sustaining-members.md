---
title: News from Sustaining Members
volume: '20'
issue: '3'
page: '8'
unindexed: true
transcribed: 'from page images of VOL.20-NO.3-JANUARY-2004.pdf, pages 10–11 (printed 8–9; after the notice of the 2004 AGM, before the APL Product Guide); Claude, 2026-10-11'
review: draft
tags:
- APL community
- implementations
queries:
- "Printed under the heading “News from Sustaining Members”, unsigned: items from MicroAPL Ltd (APLX Version 2.0) and HMW Systems Ltd."
- "Kept as printed: “the session-window contents of a child tasks”; “Vector web site” and “web site hosting”."
---

## MicroAPL Ltd

The latest release of APLX for Windows, Linux, MacOS, and AIX (*server edition only*) is Version 2.0. The highlights of the new release are built-in APL multi-tasking, a new Grid object for spreadsheet-like display and editing, new system functions and `⎕FTIE`-style component files to assist migration from other APL interpreters, and support for Unicode. The new facilities include:

- Multiple sessions can now be open simultaneously, allowing you to run several APL tasks or browse one workspace whilst editing a function in another.
- Your APLX applications can now take advantage of multi-tasking. APL tasks can be run either as ordinary tasks with their own session windows, or as background tasks:

  ```apl
  'Task2' ⎕WI 'New' 'APL' ('wssize' 100000) ('visible' 1)
  ```

- Tasks can share variables using the traditional IBM-style shared variable mechanism, or can share data through ‘delta’ properties of `⎕WI` objects.
- Tasks can send signals to each other, for example to start a calculation or to indicate that a result is available. Parent tasks can also read or modify the session-window contents of a child tasks, and be signalled when the child task is awaiting input, about to execute, or finished executing.
- You can dynamically change workspace size using `)CLEAR N`, where N can be expressed in bytes, KB, MB or (if you have enough memory) GB.
- The interpreter has been enhanced to increase the maximum rank of an array to 63 and to remove limits on the size of executed token strings.
- New system functions include `⎕FI` and `⎕VI` for numeric to character conversion, `⎕PFKEY` to allow programming the function keys, and `⎕TCxxx` for compatibility with APL+Win.
- To supplement the existing component file system, APLX now also supports `⎕FTIE`-style component files, for compatibility with other APL interpreters. As well as the standard features and multi-user/multi-tasking support, APLX also allows insertion or deletion of components anywhere in the file. Unique tie numbers can be allocated automatically by APLX if required. APLX component files are of course 100% compatible across Windows, MacOS, AIX and Linux.
- Unicode support includes Cut/Paste as Unicode, `⎕UCS` to convert APLX character arrays to Unicode and vice versa, and the `unitext` property of the System object to access the Clipboard as Unicode. The native file system has also been enhanced to read or write Unicode text and byte-reversed Unicode text.
- Full path names are now allowed in system commands.
- The new built-in `⎕WI` Grid object is a spreadsheet-like control with text or numeric cells. It can be used for display, user-editing, or both, and is programmed using a natural syntax, compatible with other `⎕WI` controls. You can set and read cell arrays directly as APL arrays.
- A number of other new `⎕WI` facilities are provided, including the `fonts` property of the System and Printer objects to list available fonts. There are also enhancements to the `Draw` method, and to the Windows OCX/ActiveX/OLE interface.

For full details, visit our website. And please keep the suggestions coming - we are ready to hear what you would like to see in the next release!

## HMW Systems Ltd

Another year, ho hum. Not a lot has changed for us: we’re still plodding on with assorted maintenance agreements; we’re still selling our dealing systems; we’re still developing our range of APL products. We are, of course, still trying to find more customers!

We didn’t get many takers for our offer to sell your software, so I suppose that most of your applications aren’t really suitable for the “stack ’em high and sell ’em cheap” approach of an Internet software shop. HMW has branched out into the area of web site hosting (and yes, we too are Wiki fans, although a different flavour to that found on the Vector web site), so in a spirit of generosity we’ll make another offer - does anyone want or need reasonably priced web hosting? This isn’t intended as a commercial offer; we’ll pass on our costs, but won’t attempt to make swinging profits out of anyone. It’s intended to be in the same air of cooperation that seemed to flow from the Dyalog conference, to raise the profile of APL and APLers on the Internet.

If anybody is interested, please contact us.
