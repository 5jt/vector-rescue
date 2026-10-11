---
title: I-APL News for Education Vector 8.1
authors:
- Anthony Camacho
volume: '8'
issue: '1'
page: '20'
unindexed: true
transcribed: 'from page images of VOL.8-NO.1-JULY-1991.pdf, page 24 (unnumbered, an inserted page after printed p.20, following the I-APL Ltd order form; within The Education Vector); Claude, 2026-10-11'
review: draft
tags:
- implementations
- education
queries:
- "Printed on an unnumbered inserted page, after an unnumbered I-APL Ltd order form, between pp.20 and 21, in the middle of C.E. Williams’s letter; page 20 is kept as the sweep recorded it. Signed “Anthony Camacho 8 July 1991”."
- "A line has been struck through by hand or in printing at the start of the third paragraph of section 2: “~~Sharp APL/PC is the same~~ mainframe version 17 with 370 emulator as before.” The struck words are kept, struck."
- "Kept as printed: “unuseable”; “DFILE.IWS”."
---

## 1 Archimedes 32-bit version - I-APL/32

Paul Chapman has finished it! (He says I can’t write a paragraph without exclamation marks and brackets). Although the precision and accuracy of the arithmetic is the same as the previous version, this version gives access to all the available memory so the maximum workspace size is within a quarter megabyte of the memory installed. The disk and notes on differences will be supplied to people who have bought the previous version for £2 plus the packing charge *from the enquiry address only.* It includes a version of DFILE.IWS which will read or write any size of file; previous versions of I-APL only give access to the first 32K. It also includes mechanisms to convert I-APL workspaces into I-APL/32 workspaces and vice versa. All the other facilities of I-APL are available in the 32-bit version. We do not plan any other 32-bit versions of I-APL.

## 2 ISI Product Changes

ISIAPL01, ISIAPL02 and ISIAPL03 have been superseded by new products. Instead of upgrades to Sharp APL/PC these are each complete products. None of them is shareware. They each include the Sharp APL/PC system documentation, but if you already have this then you may buy disks only without documentation which is much cheaper. The advantage of the new product range is that the purchaser no longer has to carry out any upgrade process. The new product runs straight out of the wrapping. A minor disadvantage is a slight increase in cost as now what you get is three disks in the set instead of a single disk.

~~Sharp APL/PC is the same~~ mainframe version 17 with 370 emulator as before. The interpreter is shareware and is available on two disks from any owner of a copy. Its enormous range of features and facilities make it impractical for anyone but an expert to get the best out of it without the system manual.

APLI/PC is version 20 of mainframe Sharp APL. It supports APL characters on CGA, EGA and VGA. It runs on 8088, 8086 and 80286 machines and the largest workspace possible, with no shared variable processors and the minimum use of DOS memory, is 280K. There is a simplified session manager and editor and there is a simplified asynchronous comms workspace. The FSCR screen workspace is fast. There is an AP124 screen manager. There is a character mapping option which uses only the standard IBM PC character set. This can be used when there are no APL characters available or to avoid CGA graphics which makes FSCR and the editor unuseable.

APLI386/PC is version 20 for 80386 or 80486 machines only. It runs in real mode and requires an XMS driver. It gives all the APLI/PC facilities and runs about 40% faster than Sharp APL/PC. There is a SHELL facility which can run DOS commands and programs in the 640K DOS memory when the interpreter and workspace are in extended memory. Most of the other options of APLI/PC are available.

Both enhancements give colour, and, if you have VGA, function key flip between 25 and 50 row screens. Both drop some Sharp features for the sake of speed (such as the date and time stamp on file components and numeric arguments to `⎕arbin` and `⎕arbout`). Both require extra care with the DOS Shared variable processor.

Anthony Camacho 8 July 1991
