---
title: Coast-to-Coast revisited
authors:
- Adrian Smith
volume: '11'
issue: '3'
page: '96'
unindexed: true
transcribed: 'from page images of VOL.11-NO.3-JANUARY-1995.pdf, page 98 (printed 96); Claude, 2026-10-12'
review: draft
tags:
- programming techniques
- user interfaces
- language design
queries:
- "Printed heading “Coast-to-Coast Revisited”. The page references (101, 104, 105) appear to be to the listings of the Vector 10.1 article (Coast-to-Coast: Managing with Objects). Printed 97 is the Technical Section’s introduction and contents list, which has no line on the Contents page."
- "Kept as printed: the empty string `''` before `bmp` in line [8] of the first fragment."
---

*by Adrian Smith*
{ .byline }

Please refer to Vector 10.1, page 97 for the background to this note. One of the ideas that I introduced was of managing the Dyalog 'data' property using a pair of functions `set_data` and `get_data` to store named variables in any GUI object. I commented at the time that I felt this was a "huge step forward in design" and fitted in well with the APL style we already knew. I started with the assumption that I ought to be able to remove all this code, as namespaces were designed to do precisely the job I had coded around.

If you look first at `init_icons` (page 101) or `init_game` (page 105) you can see that *as long as you know what your object is called,* namespaces clean things up nicely:

```apl
[8]  'ttmk'⎕WC'BITMAP' ''bmp cm
[9]  ttmk.rtn ttmk.fn ttmk.map←2 'make_term 3' map

[24] BD.ToPlay←'WN'    ⍝ Either player may start!
```

The fun begins when you have the same callback on many objects, so the object name comes in as an argument. Look at `rotate_tile` on page 104:

```apl
[4] rtn fn←bmp get_data 'rtn' 'fn'   ⍝ Old version

[4] rtn fn←⍎bmp,'.rtn ',bmp,'.fn'    ⍝ New version
```

This is nasty enough, but putting the data back again gets quite horrible:

```apl
[8] bmp set_data ('rtn' rtn)('map' map)  ⍝ Old version

[8] ⍎bmp,'.rtn←rtn ⋄ ',bmp,'.map←map'    ⍝ New version
```

I know that Dyadic are working on `⎕CS`, to let us shift namespace under program control, so I suppose I will soon be able to write:

```apl
[8] ⎕CS bmp ⋄ rtn←##.rtn ⋄ map←##.map ⋄ ⎕CS '##'  ⍝ Switch ↑↓
```

... which is better, but leaves me in danger of forgetting to switch back at the end. I think what I really want is something that looks like:

```apl
[8] bmp ⎕CS { rtn←##.rtn ⋄ map←##.map }  ⍝ Execute in namespace
```

... but I don't hold out much hope of seeing it!
