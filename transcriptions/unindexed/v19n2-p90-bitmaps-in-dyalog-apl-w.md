---
title: 'Vol 19.1: Bitmaps in Dyalog APL/W'
authors:
- David Crossley
volume: '19'
issue: '2'
page: '90'
unindexed: true
transcribed: 'from page images of VOL.19-NO.2-OCTOBER-2002.pdf, pages 92–94 (printed 90–92; within Technical Correspondence, the first letter, before art10014360); Claude, 2026-10-11'
review: draft
tags:
- graphics
- data and files
- system interfaces
queries:
- "The first letter under the Technical Correspondence heading, printed as “Vol 19.1: Bitmaps in Dyalog APL/W”. It corrects and completes the author’s “Bitmaps in Dyalog APL/W” in 19:1 (art10002690), adding the Appendix left out there. It is followed by Howard A. Peelle’s “Second-order Josephus” (art10014360)."
- "In `BM_Read` [28] and [32] the words NOT and BOTTOM are underlined in print."
- "The functions use Dyalog APL/W native files and `⎕DR` and were not run."
- "Kept as printed: in `BM_Read` the comment “abseht if Colour bits is 24”; [60] has no `⊖` before `h w↑`, unlike [51], [56] and [62]; in `BM_WORD` the comments “representedation” and “WORD and DWORD are big-endian”."
---

*From: David Crossley, 28th July 2002*
{ .byline }

I would like to make three points regarding my article in Vector 19.1.

Firstly, I wish to correct the record in that Dyalog APL/W can now interface fully with Bitmaps represented in 24-bit colour using the CBits property whose data element is an integer matrix of the same size as the Bitmat object giving the encoded RGB components for each pixel. This was implemented later than Version 8.1. 3 on which I based my article. However, the discussion regarding the specification of Bitmap structures, which are relevant also to the data structures for Cursors and Icons, may still be of general interest.

Secondly, I wish to correct an error in a code fragment near the beginning of the article (entirely the fault of the author) which read as follows:

```apl
bits←0≠'ff.bm'⎕WG'Bits' 'CMap'
```

You will of course realise that the CMap parameter should not be there.

Thirdly, a whole Appendix was omitted from the article (not the fault of the author) which contains the all-important specification of the Bitmap file structure. This may well appear on the Internet site for Vector 19.1, though not available when I wrote this letter, but for readers preferring paper copy it is reproduced below.

## Appendix

```apl
     ∇ r←BM_Read f;Bits;CMap;h;hdr;i;j;n;t;w;z

[1]   ⍝∇ Read and define Bits and CMap from Bitmap file f

[2]   ⍝  r ↔ 1(<LM/IM/NM Bits><NM CMap>) if successful,
                 or 0 ((0 0⍴0)(0 3⍴0)) if failed
[3]    →Start
[4]   ⍝ Bitmap file structure...
[5]
[6]   ⍝ BITMAPFILEHEADER
[7]   ⍝ 1  0-1   UINT  BM indicates Bitmap
[8]   ⍝ 2  2-5   DWORD Total file size in bytes
[9]   ⍝ 3  6-7   UINT  0 - reserved
[10]  ⍝ 4  8-9   UINT  0 - reserved
[11]  ⍝ 5  10-13 DWORD Offset to bits from beginning of file
[12]
[13]  ⍝ BITMAPINFOHEADER
[14]  ⍝ 6  14-17 DWORD Size of this structure in bytes
[15]  ⍝ 7  18-21 LONG  Width of bitmap in pixels
[16]  ⍝ 8  22-25 LONG  Height of bitmap in pixels
[17]  ⍝ 9  26-27 WORD  Planes (set to 1)
[18]  ⍝ 10 28-29 WORD  Colour bits per pixel (1,4,8 or 24)
[19]  ⍝ 11 30-33 DWORD Compression scheme (or 0)
[20]  ⍝ 12 34-37 DWORD Size of bitmap in bytes (0 unless compr scheme used)
[21]  ⍝ 13 38-41 LONG  Horizontal resolution in pixels/metre
[22]  ⍝ 14 42-45 LONG  Vertical resolution in pixels/metre
[23]  ⍝ 15 46-49 DWORD Nr of colours used (supersedes Colour bits info)
[24]  ⍝ 16 50-53 DWORD Nr of important colours in image
[25]
[26]  ⍝ RGBQUAD 4 bytes per colour (abseht if Colour bits is 24)
[27]  ⍝          BYTE  Blue intensity  |
[28]  ⍝          BYTE  Green intensity | Note order, ie NOT RGB
[29]  ⍝          BYTE  Red intensity   |
[30]  ⍝          BYTE  Set to 0
[31]
[32]  ⍝ Bitmap Bits, rows padded to 4-byte boundary, from BOTTOM row to top..
[33]  ⍝ 1-bit    1 bit/pixel (row width÷8 bytes rounded to 4-byte boundary)
[34]  ⍝ 4-bit    4 bits/pixel (row width÷2 bytes etc)
[35]  ⍝ 8-bit    1 byte/pixel
[36]  ⍝ 24-bit   3 bytes/pixel in order B-G-R (no colour map)
[37]
[38]  Start:
[39]   r←0((0 0⍴0)(0 3⍴0))
[40]   :Trap 0
[41]       :If 'BM'≢2↑z←biread f ⋄ :Return ⋄ :EndIf
[42]       hdr←16⍴0
[43]       hdr[2 5 6 7 8 11 12 13 14 15 16]←2 BM_WORD
              z[(2 10 14 18 22 30 34 38 42 46 50)∘.+⍳4]
[44]       hdr[9 10]←BM_WORD z[26 28∘.+⍳2]
[45]       i w h n←hdr[5 7 8 15]
[46]       :Select 10⊃hdr
[47]       :Case 1
[48]           n+←2×n=0
[49]           CMap←¯1+⌽⎕AV⍳0 ¯1↓n 4⍴z[54+⍳4×n]
[50]           t←⎕NXLATE 0 ⋄ ((⍳256)-⎕IO)⎕NXLATE 0
                 ⍝ to avoid translation in byte→bit conversion
[51]           Bits←⊖h w↑(h,32×⌈w÷32)⍴11 ⎕DR i↓z
[52]           t ⎕NXLATE 0
[53]       :Case 4
[54]           n+←16×n=0
[55]           CMap←¯1+⌽⎕AV⍳0 ¯1↓n 4⍴z[54+⍳4×n]
[56]           Bits←⊖h w↑(h,8×⌈w÷8)⍴⍉16 16⊤¯1+⎕AV⍳i↓z
[57]       :Case 8
[58]           n+←256×n=0
[59]           CMap←¯1+⌽⎕AV⍳0 ¯1↓n 4⍴z[54+⍳4×n]
[60]           Bits←¯1+⎕AV⍳h w↑(h,4×⌈w÷4)⍴i↓z
[61]       :Case 24 ⍝ convert to use colour table if possible
[62]           Bits←⊖h w⍴(3⍴256)⊥¯1+⎕AV⍳⊖⍉((h×w),3)⍴(h,w×3)↑(h,4×⌈w×0.75)⍴i↓z
[63]           :If 256≥⍴CMap←∪,Bits
[64]               Bits←¯1+CMap⍳Bits
[65]               CMap←⍉(3⍴256)⊤CMap
[66]           :Else
[67]               CMap←0 3⍴0
[68]           :EndIf
[69]       :EndSelect
[70]       r←1(Bits CMap)
[71]   :EndTrap
     ∇

     ∇ r←{a}BM_WORD b
[1]   ⍝∇ Convert WORD/DWORD from text to integer, or vice-versa
[2]   ⍝  a ↔ IS     {←1} 1:WORD, 2:DWORD
[3]   ⍝  b ↔ TV/TM Each 2/4 bytes represents a WORD/DWORD, or
[4]   ⍝        IS/IV integer to text representedation of a WORD/DWORD
[5]   ⍝  r ↔ IV or TV
[6]   ⍝  Note: WORD and DWORD are big-endian
[7]    :If 0=⎕NC'a' ⋄ a←1 ⋄ :EndIf
[8]    a←2×1+a≠1
[9]    :If 82=⎕DR b ⋄ r←(a⍴256)⊥¯1+⎕AV⍳⍉⌽((⌊(⍴,b)÷a),a)⍴b
[10]   :Else ⋄ r←⎕AV[⎕IO+,⌽⍉(a⍴256)⊤,b]
[11]   :EndIf
     ∇

     ∇ r←biread n;t
[1]   ⍝∇ Binary read: Read file without translation
[2]    n ⎕NTIE t←¯1+⌊/0,⎕NNUMS
[3]    ((⍳256)-⎕IO)⎕NXLATE t
[4]    r←⎕NREAD t,82,(⎕NSIZE t),0 ⋄ ⎕NUNTIE t
     ∇
```
