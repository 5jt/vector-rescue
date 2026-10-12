---
title: 'Hackers Corner: Lots More VGA Colours'
authors:
- Adrian Smith
volume: '7'
issue: '1'
page: '110'
unindexed: true
transcribed: 'from page images of VOL.7-NO.1-JULY-1990.pdf, pages 112–113 (printed 110–111); Claude, 2026-10-12'
review: draft
tags:
- graphics
- system interfaces
- programming techniques
queries:
- "Contents line “Hackers Corner: Lots More VGA Colours”; the printed heading is “Hacker's Corner: Lots More VGA Colours”."
- "The piece fills printed 110–111. The Contents page gives Technical Correspondence as printed 111, but its heading is on printed 112."
- "`VGA∆BORDER`, used in the first example, is not listed in the piece."
- "Kept as printed: “When setting you a range of colours”; the comment “AL = 10hex … subservice 16” beside “AH = 10hex … BIOS service 16”."
---

*by Adrian Smith*
{ .byline }

I have always been slightly puzzled by those ads in the computer press which talk about the zillions of possible colours you can get out of XYZ Corporation's latest VGA. I always seemed to be stuck with 16 foreground and 16 background (assuming you kill the blink bit) which makes 256 in all.

The first breakthrough was when I noticed that `⎕GINIT` can take a left argument specifying up to 16 VGA **Palette Registers**. Of course there were no clues as to which of the possible 64 colours was which (other than the hint that the normal range was found in the bottom 8 and the top 8 - 0 1 2 3 4 5 6 7 and 56 57 58 59 60 61 62 63). At the time, I was playing with a Hercules-oriented version of C&D's Starmap workspace, adding a bit of helpful colour. One obvious extension was to put the bright stars into their correct spectral types ... Betelgeuse should be red, and the sun should be orange. Armed with an old star atlas, I experimented with the palette settings, and quickly discovered that colour 38 is a rather excellent orange!

Of course this trick only works for graphics, and APL\*PLUS helpfully resets everything when you exit! As a last resort, I read the instructions (in this case a very useful MicroSoft book all about VGA programming) to find the BIOS calls involved. The screen border and palette registers are trivially easy to set, and can be used to good effect to brighten up your screen designs. There are several excellent background colours (e.g. a nice deep green) available, as well as the above mentioned orange. As with all these settings, note that &lt;Ctrl-Esc&gt; resets everything to default in APL\*PLUS/PC.

```apl
    ∇ VGA∆PALETTE VEC;RG;BX

[1]   ⍝ Set Vga palette register VEC[1] to VEC[2]
[2]   ⍝    AH = 10hex       ... BIOS service 10 (EGA/VGA only)
[3]   ⍝    AL =  0hex       ... subservice 0 (1 sets the border)
[4]   ⍝    BH = 0-63        ... required colour
[5]   ⍝    BL = 0-16        ... palette register to set (0 for bdr)
[6]    BX←(256×VEC[2])+VEC[1]
[7]    RG←(4096,BX)⎕INT 16
    ∇

VGA∆PALETTE 6 38        ⍝ Switch brown to orange
VGA∆BORDER 38           ⍝ Use an orange frame
43 15 55 62 38 52 4     ⍝ OBAFGKM ... star spectral types!
```

If you want an example of a really good use of this feature, try out a wonderful little program from Quarterdeck called Manifest (comes along with QEMM 5.0). To select an appropriate range of colours for your application, I suggest you set up a simple workspace which splashes colour around the screen, and experiment. Of course different types of monitor may give more or less acceptable results, and users can always wreck the whole thing by fiddling with the contrast button!

Of course 64 colours is more than 16, but we are still some way short of the 64,000 or so that the advertisers claim! The next stage is to fiddle with the Red/Green/Blue balance of any of the 64. Having created a colour which is to your liking, you then map it to one of the 16 palette registers as above.

```apl
    ∇ VGA∆COLOUR VEC;RG;BX;CX;DX

[1]   ⍝ Set Vga colour register VEC[1] to VEC[2 3 4] (RGB)
[2]   ⍝    AH = 10hex       ... BIOS service 16 (EGA/VGA only)
[3]   ⍝    AL = 10hex       ... subservice 16
[4]   ⍝    BX = 0-63        ... colour register
[5]   ⍝    CH = 0-63        ... green intensity
[6]   ⍝    CL = 0-63        ... blue intensity
[7]   ⍝    DH = 0-63        ... red intensity
[8]   ⍝ Note that intensities go down by half for -8 from 63
[9]   ⍝ e.g. 63 .... 55 .... 47 .... 39
[10]  ⍝        full... half... qtr ... eighth
[11]   VEC←4↑VEC
[12]   BX←VEC[1]
[13]   DX←256×VEC[2]
[14]   CX←(256×VEC[3])+VEC[4]
[15]   RG←(4112,BX,CX,DX)⎕INT 16
    ∇

      VGA∆COLOUR 38, 48 48 0     ⍝ Set up orange as Red + Green
```

The intensity of each colour is specified on a scale from 0..63, but the relationship is highly non-linear; a good rule of thumb is that by subtracting 8 you halve the brightness:

> 63 63 63 ..... bright white<br>
> 55 55 55 ..... half intensity white<br>
> 47 0 0 ..... quarter intensity red<br>
> 42 24 42 ..... Laura Ashley 'Autumn Plum' etc.

When setting you a range of colours, you need to decide whether you belong to the Benetton school (lots of primaries), or the Laura Ashley school (subtle blends). Have fun.
