---
title: 'Hackers Corner: Check that Disk!'
authors:
- Adrian Smith
volume: '7'
issue: '3'
page: '125'
unindexed: true
transcribed: 'from page images of VOL.7-NO.3-JANUARY-1991.pdf, page 131 (printed 125); Claude, 2026-10-12'
review: draft
tags:
- system interfaces
- programming techniques
queries:
- "Printed heading “Hackers’ Corner: Check that Disk!”."
- "The listing is for APL*PLUS/PC (`⎕INT`, `⎕ELX`). The first example’s figures agree with line [13]: 42366976 = 34584576 + 7782400, all multiples of 2048."
---

*by Adrian Smith*
{ .byline }

One of the penalties of running your APL systems across a network is that you never quite know what is happening at the other end of the wire. I could be sitting quite happily in my planning system, having loaded up my data hours ago ... meanwhile someone has pulled a plug on the Vax that I fondly imagine holds my ‘P:’ drive! If I don’t spot the situation until APL reports ‘DRIVE NOT READY ERROR’, I need to do some fancy error recovery to give the user the chance to save things temporarily on the PC hard disk.

A much better way is to ask DOS to check out the disk first, and thus to avoid having to back out of my save routine halfway through:

```apl
    ∇ R←CHECK∆DRIVE DRV;⎕ELX
[1]      ⍝ Use INT 33H to verify drive status ...
[2]      ⍝  Returns R[1]←¯1 or 65535 for a dead disk
[3]      ⍝     else R[1]←bytes per allocation unit
[4]      ⍝     (e.g. 512 for floppy, 2048 for typical HD)
[5]      ⍝
[6]      ⍝  Other values of interest are: [2]=disk size
[7]      ⍝                                [3]=bytes used
[8]      ⍝                                [4]=bytes free
[9]      ⍝
[10]      DRV←'ABCDEFGHIJKLMNOPQRSTUVWXYZ'⍳''⍴DRV
[11]      ⎕ELX←'R←4↑¯1 ⋄ →0'
[12]      R←(4↑ 13824 0 0 ,DRV)⎕INT 33 ⋄ →(R[1]∊ ¯1 65535)↑Err
[13]      R←(×/R[1 3]),(×/R[1 3 4]),(×/R[1 3],-/R[4 2]),×/3↑R ⋄ →0
[14] Err:R←4↑¯1
    ∇

      CHECK∆DRIVE 'C'
2048 42366976 34584576 7782400

      CHECK∆DRIVE 'E'
¯1 0 0 0
```

The other returned information could be quite useful too ... for example to check that there is sufficient space on a floppy to hold the file you are about to save. Note also the allocation size ... it is quite pointless to set the APL\*PLUS/PC file blocking to less than this; you are simply wasting time and saving no space at all. Many network drives allocate in units as high as 16K, so all those tiny little files are really taking 16K bytes at a time off someone’s Vax! Be warned!!
