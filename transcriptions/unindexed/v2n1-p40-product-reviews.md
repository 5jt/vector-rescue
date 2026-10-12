---
title: Product Reviews
authors:
- David Preedy
volume: '2'
issue: '1'
page: '40'
unindexed: true
transcribed: 'from page images of VOL.2-NO.1-JULY-1985.pdf, pages 42–45 (printed 40–43); Claude, 2026-10-12'
review: draft
tags:
- reviews
- graphics
queries:
- "Two reviews under the section heading “PRODUCT REVIEWS”, “by David Preedy”: the Hewlett-Packard 7550 8-pen plotter (printed 40–41) and the Hewlett-Packard 2686A LaserJet printer (printed 42–43), the latter with an italic editor’s note."
- "Kept as printed: “One of areas where APL has made a major contribution”; “significantly greater then previous plotters”; “put up with the the fan-noise”; “and I am sure that will be this lack of suitable packages”."
---

*by David Preedy*
{ .byline }

## Hewlett-Packard 7550 8-pen plotter.

One of areas where APL has made a major contribution to business computing has been in introducing quality graphics to improve the presentation of corporate information. Despite improvements in ink-jet printers, the pen plotter still provides the best quality colour hard-copy. So in view of Hewlett-Packard's long established reputation in the plotter market, it was with high expectations that I set down to use their latest offering.

The 7550 allows you to have up to eight different pens per carousel, giving a choice of colours and/or line thickness. It can handle A3 or A4 paper, and the latter can be automatically fed from a stack underneath the plotting-bed. The plotter uses the latest grit-wheel technology, which means that the pen moves in one direction only, and the paper is moved as required in the perpendicular direction. By simplifying the mechanism and reducing the number of moving parts, this should improve reliability substantially. It also allows pen velocities and acceleration to be significantly greater then previous plotters.

The HP7550 has different carousels for the standard fibre-tip pens, roller-ball pens, liquid-ink drafting pens and special pens for overhead transparencies. On its own, the use of carousels is a major advance, as it removes the need to be continually changing individual pens if you switch frequently between paper and acetate copies, and the carousels give you somewhere convenient to store the pens not currently in use. But H-P have built even more functionality into the carousels. They control the default settings of the pen velocity and pressure, so that the plotter will automatically slow down and reduce pressure when drawing on acetate. So the choice of what plotting medium to use can be made locally on the plotter without having any implications for the software generating the graphics.

In fact the whole area of software requirements seems to have been well thought out by Hewlett-Packard. The 7550 uses HPGL — Hewlett-Packard's own graphics language; this means that there is a reasonable chance that code written for other recent Hewlett-Packard plotters will work without needing changes, although you may find that you want to modify your software to take advantage of any new features.

If you do have to start from scratch, then HPGL makes the programming reasonably straightforward. No longer do you have to write complex encoding routines to compress the x-y coordinates of a point into the minimum number of bytes. HPGL takes coordinates represented as ASCII text. Similarly you can throw away that 30-line function you used to shade an arbitrarily shaped polygon. The 7550 firmware provides automatic polygon-shading, giving you control over the line-patterns, angles and separation used for shading. If you want multiple copies then you can simply send a command to repeat the last chart up to 99 times; the copies will be done locally without tying up your computer.

With a little bit of care in the design of your software, you can arrange for character sizes, patterns, etc., to be defined relative to the size of your plotting area. This enables you to change the plotting area on initialisation of a chart (e.g. to use A3 paper, or to fit several charts onto one page), and the chart will be automatically scaled and rotated without you having to change your program.

To my mind, however, the key requirement of a device like this is that it can run under user control with the minimum operator involvement. In the past this has required the use of roll-feed paper with an automatic guillotine. Not only was the paper-feed mechanism notoriously unreliable, but the finished graph ended up on special paper that was a different quality from the rest of your report and could never be pressed flat. The A4 paper stack-feed overcomes these problems. It seems to be very reliable if you load it carefully and try to make sure that the leading edge of the paper is not creased. But the great advantage is that you can load the same quality paper that is used for the rest of your report, for instance using your company's headed stationery.

So far our use of the HP7550 has highlighted only two significant complaints. The first arises from the use of grit-wheels to move the paper backwards and forwards. This has two side-effects. On normal paper you tend to get two slightly rubbed areas along the sides of the chart. More importantly, you cannot use conventional acetate for overhead transparencies because the grit-wheels will not grip; instead you have to buy special acetate which Hewlett-Packard has treated to have roughened areas where the grit-wheels can grip.

The second complaint concerns the loop-through arrangement, whereby you can put the plotter in the line between your computer and your terminal. Unlike previous Hewlett-Packard plotters, the 7550 disables this link when it is turned off. Consequently you either have to rewire your link or put up with the the fan-noise (and heat) generated by the plotter continuously. Moreover, even when it is turned on, the plotter accepts 8-bit characters from the computer, but only transmits 7 bits on to the terminal, and it does not transmit any hard-wire handshaking to or from the terminal.

In summary, the new HP7550 sets new standards by which the current generation of plotters can be judged. Hewlett-Packard seem to have learnt from the shortcomings of their previous plotters and this latest model exhibits many excellent design features. The trend to increase the local power of the plotter will presumably continue and this enables micro users in particular to achieve significant improvements in performance. My main regret is a nostalgic one; no longer can you see the pen writing out the characters using the left-handed style of the old HP7221!

## Hewlett-Packard 2686A LaserJet printer.

For many years there has been a straightforward choice for low-volume printers. If you want reasonable speed, you choose a dot-matrix printer; for "letter-quality" output you need a daisywheel printer. Over the past year though a third option has emerged in the form of low-cost laser printers. Many manufacturers' names may appear on the front, but these represent different offerings of a couple of basic printing engines. The LaserJet is one of several models based on the Canon engine.

The basic LaserJet provides excellent quality printout, at a reasonable speed (8 pages per minute). A growing range of font-cartridges are available, and these let you mix several different fonts onto one page of output. Typically you may want to have normal, bold and italic text. The maximum paper size is A4, which can be fed automatically from a stack held at the bottom of the printer. This can be overridden by a manual feed at the back and this can take labels, envelopes, etc. There is a rudimentary graphics facility (monochrome only of course) which may be suitable for drawing boxes but would need some fairly hefty software to do anything much more interesting.

The main attractions of the LaserJet as an office machine are the superb quality of the printed output (a resolution of 300 dots per inch is claimed), the A4 stack feed (for the same reasons as given above for the HP7550 plotter) and the fact that it is virtually noiseless. It looks much more like a small photo-copier than a printer and its noise level is similar. You can also send a command to request up to 99 copies of the current page should your photo-copier be out of action.

The range of fonts is extensive, but it is worth looking closely at the exact specifications of the cartridges to make sure that the font combinations you want are available together. Some of the literature gives a misleading impression of how many combinations are available. Fonts are defined by several attributes — orientation, symbol set, spacing, point size, style, stroke weight and typeface. This gives some 7500 possible different fonts but a typical cartridge may contain 10 or so.

This flexibility does have some unfortunate side-effects. In order to select a font, you can't simply say "select font number 3 from the loaded cartridge". Instead you have to specify enough of the font attributes to uniquely define a font available on the cartridge you currently have loaded. Typically, this means that you may have to send a 25-byte string to the printer to ensure that it loads the correct font. This is simply a chore if you are working direct from APL, but is normally impossible using a package unless it has been designed with the LaserJet in mind. In particular, I doubt whether any word-processing packages have yet built in the capability to use the LaserJet's facilities effectively.

We have had to develop an APL front-end in order to get Wordstar to change fonts and even then we don't have the complete flexibility that we would like. We cannot easily combine more than 2 fonts per document and we cannot get justified text using the proportionally spaced fonts. Probably a good Wordstar interface will be developed sometime, but I suspect that it is likely to be later rather than sooner. We have heard of two companies working on the link, but we have yet to see something working.

Whilst I cannot envisage the LaserJet being used for bulk APL listings, its ability to mix fonts suggests a useful role for preparing high-quality mixed APL/ASCII output — either as camera-ready copy for all the budding Gilmen and Roses preparing their next tome, or for those all-important VECTOR competition entries. Whilst Hewlett-Packard do not to my knowledge offer an APL character set, a company called Electronic Printing Services do provide a range of different fonts, including APL.

*(Ed — we would welcome contributions from anyone with experience of using this or similar APL fonts on laser printers.)*

We have had a few grumbles about some aspects of the LaserJet. I think the most significant is the absence of any facility to download a font definition from your host computer. This capability would open up all sorts of options for specialised fonts; two suggestions that spring immediately to mind are APL symbols and a character set with the pound sign somewhere vaguely resembling its position on a U.K. keyboard. My other main complaint is the LaserJet's refusal to fit 80 columns of text onto an A4 sheet using 10 pitch character spacing. It fits 77 columns on and there would be room for the other three, but if you want to dump your VDU contents you have to select a non-standard font.

On the whole reliability has been pretty good, but the printer did have one spell when it seemed unable to orientate the lines parallel to the edge of the paper. Paper-feeding has been of intermittent quality with occasional days when the printer refuses to feed heavier grades of paper and sometimes using lighter grades of paper, it picks up two sheets at a time. It tends to be particularly unreliable when the paper feed is almost full or nearly empty. On the good side, it is straightforward to clear a misfeed (unlike the majority of photocopiers seem to be), and the hot parts are not only suitably labelled and insulated, but are also coloured a lurid, almost luminescent green.

We have attempted to create overhead transparencies through the machine (the manual says it works) and, to be fair, it did create a good image on the acetate. But the heat of the printer caused the acetate to buckle a lot, and the dread of having to extract a molten sheet of acetate from the inside of the printer has deterred me from experimenting much further with it.

Obviously the LaserJet is considerably more expensive than a daisywheel printer, but in return it offers much better quality, is much quieter and needs much less maintenance. Unfortunately, I think it will take some time for software vendors (of word-processing packages in particular) to come to terms with the options offered by this device, and I am sure that will be this lack of suitable packages that will limit the attractions of the LaserJet for many users.
