---
title: PCs, Graphics & APL
authors:
- Martyn Adams
volume: '3'
issue: '1'
page: '51'
unindexed: true
transcribed: 'from page images of VOL.3-NO.1-JULY-1986.pdf, pages 53–58 (printed 51–56); Claude, 2026-10-12'
review: draft
tags:
- graphics
- reviews
queries:
- "Contents line “PC Graphics Cards (EGA and PGC)”; the printed heading is “PCs, Graphics & APL”."
- "The editor’s interjection on printed 55 is in italics in the text, as printed. Quad names printed with a space after the quad (“⎕ GWRITE”) are given closed up as code; “the ⎕ Gfunctions” is kept as printed."
- "Kept as printed: “also known as the PGS”; “acheived”; “if it wants too”; “I would be only to pleased”."
---

*by Martyn Adams*
{ .byline }

One of the more enjoyable aspects of my job is to evaluate new pieces of kit and, if they check out O.K., write code for them. Recently I’ve been devoting my attentions to two such pieces of kit – both from IBM – the E.G.A. (Enhanced Graphics Adapter) and the P.G.C. (Professional Graphics Controller – also known as the PGS). Both have been around since last Summer, but the lack of availability will probably have prevented many readers from laying their hands on one.

## IBM Enhanced Graphics Adapter

Now we at Metapraxis use APL\*PLUS/PC on IBM PC/XTs and ATs and on the whole have been more than satisfied with it. (I have reservations about the choice of some ⎕ functions and which way their arguments go and other niggly things like that but all in all I am pretty impressed.)

It was then with great delight that we received both the E.G.A. system and APL\*PLUS release 4.6. (This was before the new release 5 but it supported the E.G.A.) We plugged it all in and hey presto! It worked first time! Now the E.G.A. supports many different modes – most of them the boring emulations of the basic IBM colour graphics card. These, as any discerning PC user will know, are little short of pathetic. The low resolution and poor choice of colours means that the basic colour card has few serious graphics applications. But the E.G.A. is a delight!

Our software package – RESOLVE – is designed to display very good quality colour images, graphs and such, to senior management. Consequently we are a bit fussy about the graphics devices we consider supporting and we had deliberately not used the standard colour card. By purchasing the additional memory expansion for the E.G.A., we were able to use the highest resolution possible on the E.G.A. This is obtained from APL by using mode 6 (APL graphics mode, not the E.G.A. graphics mode) which gives the 16-colour 640 by 350 pixel image. Once you’ve started using this, you’ll never want to hear or speak of the colour graphics card again. Consequently that is the mode with which I am most familiar.

Having sung the praises of the APL interpreter and the E.G.A. I would like now to point out some practical considerations. Back at base, deep in the steamy Metapraxis jungle (our oversized office plants are rumoured to be carnivorous) we run the E.G.A. on a PC/AT. Speed, we thought, would be no problem with the extra horsepower of the AT as against our older XTs.

We used to have a performance problem on the XT with the primitive colour graphics card. It took several seconds just to write a line of text while in graphics mode! The problem seems to lie within `⎕GWRITE` which is the function used to write text to the graphics screen. But the E.G.A. on the AT does not improve the speed of the text writing by much – although for most operations it is significantly faster. I think this is simply because there are more pixels to write to on the screen and so the extra speed of the AT is being traded for extra resolution on the card.

Oh well! We do get good graphics even if it is a mite slow. One advantage with the APL is that it takes advantage of the extra resolution and allows you to write 80 columns of text in full colour. The characters are fully programmable from within the APL but it is not a simple process. I have never used STSC’s supplied functions so I cannot say if they supply a character design utility.

With release 4.6 of the APL (I am not sure but I think it is also true of release 5) we were supplied with a little program to define the characters to be used by the E.G.A. card. You see the E.G.A. has a fully programmable character set and STSC thoughtfully supplied a routine to program it. This means that you don’t need the STSC APL character chip if you’ve got the E.G.A., even if you don’t use the graphics options. I don’t know what effect this has on any of the other programs that are lying around which use the PC’s extended character set though. One could expect there to be a few funny characters lying around especially if you use a multilingual word processor. All of those horrid foreign characters are redefined as lovely APL symbols. To top it all the character quality, whether within APL, graphics or not, is very good and note that the E.G.A. still remains programmed even when in DOS.

Well done STSC on that one, but not so well done on the printing side! I have found a bug, or is it a feature? STSC have quite rightly put in a very nice and simple graphics printing function (`⎕GPRINT`) which takes a snapshot of the displayed image and churns it out to the EPSON FX-100 dot matrix printer. You can decide what character represents what colour as a left argument to the function. This means that you can define black on white or white on black, by judicious selection of the appropriate characters from the STSC modified extended ASCII/APL character set.

I liked that. But the printing is rotated sideways on the printer, so to rotate it back to the correct way the manual recommends `⎕POKE`’ing location 234. On simple black and white images this works beautifully – printing a very crisp image which really looks quite impressive. What the manual doesn’t tell you is that your choice of shading patterns goes all funny and if you select anything other than black and white (black is a block character and white is a space character) then your picture will look as if it has put on a set of ghastly striped pyjamas.

This caused me much upset, but at the time of writing the Cocking and Drury Helpline were chasing up the problem with STSC and I am awaiting the answer with anticipation. It does seem a shame that such a nice and simple facility which has been well implemented should have this problem. In fact the other bug I mentioned to C&D was chased up and fixed pretty much straight away. I was very impressed! The bug is simple enough, if you `⎕CR` or `⎕VR` a function then the interpreter zaps the screen attribute character where the cursor lies. You don’t normally notice it though because it sets the attribute to ‘normal’ display. It only shows up when you have a screen full of other attributes and then suddenly one of them switches off. However, there is a ‘patch’ available from C&D and later releases of APL\*PLUS/PC should include that minor correction.

On the graphics side the line drawing, shading and circles all work amazingly well, although one has to be careful with the painting (colour fill). Many a time I have looked with utter dismay as the colour flooded out of the pretty little shape on the screen to obliterate everything else. Make sure your border’s fully enclosed before using the `⎕GPAINT` function.

A good alternative option would be to have a graphics function which allows one to specify an arbitrary shape by defining the corners and just say “fill it”. It would make life so much easier. I have often needed to define a shape and fill it without knowing exactly where to start the painting. If you think about it it is not an easy task. What if the shape folds back on itself? What if there is a hole in the shape where the centre of gravity should be? Where do you start painting from? Perhaps STSC would like to consider that as a future development.

The `⎕GINIT` function allows you to define the colours you want. All in all you can define up to 16 from a palette of 64. The 64 are not awe-inspiring and some of them look remarkably similar, but if you fancy 8 different shades of blue then you can do that. Actually I found that the choice of 16 colours was about right for nearly all of my applications and for most systems it should be enough. Using the `⎕GINIT` function is very easy and you can even define the border colour – a thoughtful touch that.

One of the few nice things about the standard colour card was that after drawing your grotty picture you could `⎕PEEK` it off the screen and compress the resultant variable, so that it held only the addresses and values where the screen was non-blank. By `⎕POKE`’ing it back to the screen the image took just a second to recreate itself. If that variable was sorted by address or colour value then spectacular results could be acheived when it was written back to the screen again.

Unfortunately life is not so simple on the E.G.A. One can’t simply peek and poke to the screen and get sensible results any more. At least we haven’t found an easy way of doing it yet. Do you know of any way of doing it? It is a shame though, perhaps STSC could come up with a `⎕GPEEK` or something which allows a quick read of any supported screen? Please!

Anyway, to compound the problem, the E.G.A. with 128k memory spills over the 64k segment size which was so thoughtfully built into the IBM PC architecture, and a fullish picture would more than likely take up more than 64k. There is no way one can fit a pint into a half-pint bottle. Or is there, STSC?

The Enhanced Colour Display – the special monitor that plugs into the E.G.A. (the older colour ones can’t operate at a fast enough frequency) – has one really dumb feature. On the right of the screen are three knobs; one is the on/off, the middle one is the contrast and the third is the brilliance. Great. Except that when I first got the machine the contrast knob did not appear to work. Oh well, you can’t win them all – I thought.

It turns out however that to activate the contrast knob you have to pull it out. Then it works quite well. As soon as you push it in again, the contrast returns to its factory default setting and you have to pull it out again to return to your desired setting. I think that’s dumb. Why bother with a pull switch at all? And if you’re going to have one, why not document it? Such are the wonders of modern technology I suppose. I wonder if the next screen will have an on/off switch which only works if you pull it out first. . .

To finish up on the E.G.A., I would have to recommend it as a serious graphics card which is more than I can say for the previous IBM offering. If performance is what you want, then you’ll have to have an AT as the XT can be a bit slow. I can guarantee that you will be impressed with the picture quality of the device. I hope that the current rumours about IBM bundling the E.G.A. in with the new ATs as the standard monitor card turn out to be true.

By the way, a flood of E.G.A. compatibles seem to be hitting the market and we’ve successfully run all our software on one of these (Quadram) without having to make a single change.

## IBM Professional Graphics Controller

The P.G.C. (Professional Graphics Controller) is a very different animal. IBM started selling them at very high cost because they are very high spec. However earlier this year the prices were slashed by about 50%. Don’t get too excited about this though – we haven’t been able to lay our hands on one in the U.K. since last Autumn, although they have been available to our knowledge in the States and in France.

The P.G.C. has a resolution of 640 by 480 and can display 256 colours from a palette of 4096. Not only that, but it has its own onboard 8088 processor! Unfortunately you can’t speak to it by using the ⎕ Gfunctions in APL\*PLUS, you have to send it commands.

I remember the days when my finances ran to an APPLE II. Remember them? I later upgraded it with a keyboard that had its own processor but technology had advanced so fast since I had bought the APPLE that the processor in the keyboard was more powerful than the CPU! It nearly had more memory too! I seriously considered programming the keyboard to be an interpreter for the CPU. Pipelining on the APPLE? No. I’m not that good unfortunately. But I digress. . .

The P.G.C. is one of the products supported by IBM’s version of GKS called VDI. To translate into English that means that Big Blue wrote a packaged offering called Virtual Device Interface which emulates the Graphics Kernel System for its PC range of computers. That should, in theory, permit pictures drawn on one device to be transportable to another. In practice, as I have explained in a previous article (see VECTOR Vol. 2, No. 3), that doesn’t work very well.

Virtual Device? I have visions of a printer zipping about the office on its little wheels, wires dangling, plugging itself into each PC workstation and accepting a line of printed output from each. Providing it doesn’t bump into the virtual graphics screen (a P.G.C. perhaps) also skidding about trying to display at least one frame of a graphics image from each machine – it might work. Until the manager walks in and gets a flying RS232 in the mouth. . .

In the future, despite my previous article in VECTOR on the uselessness of GKS, it may well be worthwhile to write a VDI/APL interface, as VDI currently supports the P.G.C., E.G.A. and that other blotchy thing. For simple drawings it may prove a useful transporting tool but don’t get carried away. Apart from the difficulty of defining pictures using VDI it also has a serious performance overhead. Oh roll on the 80386!

Rumour has it (lots of rumours around these days!) that the P.G.C. VDI driver doesn’t quite work properly and that’s why you can’t lay your hands on a P.G.C. in the U.K. *(Ed: It must be something to do with the weather if it works in Silicon Valley and on the Riviera!)* Apparently IBM do not think there is much demand for a new graphics screen which uses a different protocol (yes – another graphics protocol) without having the VDI programs.

Anyway we – the amazing APLers – do not need the new proposed Esperanto of the graphics world in order to get the P.G.C. working. Besides which, unlike real Esperanto, VDI can slow down your application by as much as three times – rumour has it of course. I tried to get VDI into the APL workspace but VDI didn’t cooperate and I’d be pleased to know if anyone else has any success in this field.

The P.G.C. is the biggest PC card I’ve come across; it takes two complete expansion slots and there is a little half card stuck between them. It certainly feels like you are getting your money’s worth when you install it. In PC mode the P.G.C. emulates a feeble graphics card, which is not the E.G.A. but that older one, and it will only switch to its high-res mode by a specific command. The graphics commands are sent to it by accessing a memory buffer in the PC memory map and setting pointers. Unlike the E.G.A., the P.G.C. has a command processor on board and so it has to be sent a series of command strings. For this reason APL\*PLUS doesn’t yet support the P.G.C. with its ⎕ functions. I have written a function to send the command strings and if anybody wants a copy of my code (unsupported of course), just ask.

Using my function we have been able to draw incredibly pretty pictures with incredible resolution and in incredibly quick times. The P.G.C. does support arbitrary polygon fills and you can dynamically change colour palettes enabling you to emulate rotating planets and flashing arrows and such like. There is a suite of 3-D graphics functions, but be warned – they do not always work properly. You can rotate defined objects through a three-dimensional plane and end up with a really screwy picture. The P.G.C. doesn’t support hidden line/surface removal. Pity that. . .

It will draw in 2D, 3D, convert from one to the other, circles, lines, polygons etc. You can even draw with absolute coordinates or relative coordinates. You can define command lists and run them whenever you want. You call them back in a translated form and you can read pixels from the screen as well as write them. You can program variable sized characters as well and the amazing thing about the P.G.C. is that it *could* look remarkably like an IBM 3279 graphics terminal if it wants too.

The P.G.C. is a very good device but is not for the casual user unless you really require the resolution or the greater colour selection. Development of programs can have its difficulties. Remember that the P.G.C. is a computer in its own right so that if you lose communications with it and the monitor is displaying the P.G.C. screen – not the PC screen – then tough! You can quite happily display a graphics image and while doing so return to APL with a SYNTAX ERROR and do frightening things, without the P.G.C. batting an eyelid. It still hasn’t been told to return to PC mode and so will quite happily display its graph without you knowing what is happening under the bonnet. Even a soft re-boot won’t help and you may have to switch the PC off and then on again before you can continue. Remember that rebooting the PC will restart the PC but not the P.G.C. IBM have thoughtfully not supplied a reset button on the card.

On the other hand you can draw a graphics image while still in PC mode and then suddenly flash to the graphics image without the user having to watch the graph being built up.

A big let down with the P.G.C. was the proportional spaced lettering which is supposedly able to cope with any character size. I don’t know why I was led to believe that, it certainly isn’t explicitly stated anywhere. With all those CPU cycles to spare you would have thought that the P.G.C. could draw properly proportional characters at any size anywhere on the screen – but it doesn’t. As you increase the character size the spacing within the character string gets bigger until the P.G.C. decides that it can fit a double size character in. Then *bang!* – the characters are twice as large and closer together.

In conclusion then, I have to say that overall I am impressed with the E.G.A. (especially with the extra memory) and APL\*PLUS’s integration of it into their offering, even to the point that they support the extra memory without the manual saying so! STSC could do a little more in the way they handle graphics from APL and I would be only to pleased to make a few constructive suggestions.

VDI does not seem so impressive. The P.G.C. is very good for those who need the extra specification but remember that it didn’t come cheap (and now it doesn’t seem to come at all!). I suspect that there are already a few P.G.C. clones around that support hidden-line removal and one or two little extras which will make them superb for animated graphics.
