---
title: 'Windows 3: the Implications for APL'
authors:
- Adrian Smith
volume: '7'
issue: '3'
page: '61'
unindexed: true
transcribed: 'from page images of VOL.7-NO.3-JANUARY-1991.pdf, pages 67–70 (printed 61–64); Claude, 2026-10-12'
review: draft
tags:
- user interfaces
- implementations
- system interfaces
queries:
- "The “C macros” on printed 64 are printed spaced, `∘ . =`; transcribed `∘.=`."
- "Kept as printed: “swopped out to disk”; “the Dos Protected Mode Interface”; “Meta-ware Hi-C”."
---

*by Adrian Smith*
{ .byline }

## Background

These notes are a brief attempt to explain why I think Windows 3 matters a lot to APL. I will start by outlining some of the things you can do **now** with Windows and APL\*PLUS/PC or APL2/PC; the rest of this note is a look a little further ahead to where I would like to get to in (say) 18 months’ or 2 years’ time. The assumption behind all that follows is that you have at least a 16 MHz 386SX with about 4Mbyte of memory; Windows will also run in ‘standard’ and ‘real’ mode if you insist, but both of these effectively cripple it, and should be disregarded unless you are absolutely desperate!

## What you can do with Windows

The most obvious thing is task-switching. I never added up all the time I lost whenever the phone rang: `)SAVE` and `)OFF` followed by a quick dive into the mainframe or Word or a spreadsheet, followed by APL and `)LOAD` to get back to where I was. To leave my APL\*PLUS/PC session sitting on the screen, kick out into something else, and recover it **exactly** as I left it is a huge time saver.

There seems to be no practical limit on the number of DOS applications you can fire off alongside each other; I have often had 6 sessions running and Windows has never fallen below 75% free. Switching is literally instant, you use Alt+Tab to toggle round the sessions, and your screen flicks back the instant you take your thumb off the Alt key. There is only a minimal cost in memory; I lose 17K off my APL workspace as a consequence of running under Windows, and the e=8192 option works fine.

The next thing you might try is setting one or more sessions to run in the background. This is especially handy when that session is doing something slow and wasteful of processor resources, like copying a big file across a slow network. For example to upgrade our MTP system to a remote site requires about 8 minutes over a 2400baud line; I can run this in background at a low priority and get on with something useful in the meantime. Not recommended with things like GoScript which really hammer the CPU! You either slow your printing to a crawl, or make APL so jerky you can’t use the editor ... set the print running in foreground and go for lunch!!

You can get more ambitious, and try cut and paste between sessions! For example I can write a line of code in APL, copy it into the Windows clipboard, and paste it straight into Word. This saves a deal of wondering whether rho is really alt-251 (`⍴` ... so it was!) and should speed up Vector production quite a bit. The only snag is that you can only use the clipboard when the application is running windowed, and this switches it to a graphics character set, hence losing all the APL symbols (at least in versions prior to 10). However you can toggle between windowed and full-screen with Alt+Enter, so this is quite bearable in practice.

Amazingly enough, cut and paste works fine in graphics mode too. For example I have an APL function to draw the Rowntree logo (any size, any colour etc.); I copied the logo from APL into Windows Paintbrush, and hence was able to use it to tile my desktop, as well as being able to scribble graffiti all over it with the mouse!

## What you can’t do with Windows

You can’t run APL2/PC 32bit, APL\*PLUS II or Dyalog APL. APL\*PLUS II and Dyalog use the same memory management as QEMM, which will only co-operate with Windows if you have QEMM version 5.1. However this still limits you to the Windows ‘standard mode’, in other words applications get swopped out to disk, instead of being stacked away in extended memory. One of the great joys of Windows is the instant switching, so I personally still tend to close Windows down and run Dyalog APL from the DOS prompt.

## Where APL needs to be Right Now

Obviously, APL has to co-operate with the Windows memory management, at least to the extent that it will run under Windows as a standard DOS application. Windows is quite happy to allocate extended memory as old-style LIMS/EMS memory, which is why APL\*PLUS/PC still gets to use e=8192 to load 64K of the interpreter high. However if you want true, flat, 32-bit addressing, you need to use a new interface called the Dos Protected Mode Interface (DPMI for short) ... see the recent PC edition of Byte (from page 113) for details.

At this point, I go way outside my technical knowledge; all I can say is that it would appear that all the fancy Protected-mode support given by interface software like Phar Lap now comes free with the system, in fact it will probably be in DOS 5.0 even without Windows.

This leaves vendors like Dyalog and STSC in the happy position of being able to wave goodbye to Phar Lap, and hence to the hefty royalties they are paying on every copy of the interpreter they sell. The implications would seem to be:

- cheaper development systems, and very much cheaper runtime.
- more straightforward development of APs, ideally in common or garden C, rather than the super-whizzo Meta-ware Hi-C that Dyalog currently demands.
- you should get as much memory on your system as you can afford! If you want to run 32-bit APL alongside Aldus Pagemaker and MS Word, you are looking at 12 Mbyte minimum.

That will do for starters ... there is one more goody that deserves detailed explanation, and offers APL the chance of a giant step back to the future ....

## Dynamic Data Exchange (DDE)

How many of you remember `⎕SVO` and `⎕SVC`? They actually gave their name to APLSV ... and I don’t mean the perversion of a brilliant design concept into a lousy mechanism for reading and writing files!! I mean genuine user-user shared variables, which are a superb mechanism to manage concurrent processing, and deal with all the problems that arise when you need to organise co-operating tasks.

I last tangled with `⎕SVO` under VSPC, when we used it to set up a simple tele-conferencing system between our planners. Essentially, it allowed two or more logged-on users (in York and Edinburgh) to update the same data, and see what each other was doing. With DDE under Windows, you have a defined interface whereby any Windows application can share variables with any other, using the Clipboard to pass messages, and shared memory to exchange data.

In other words, you could imagine a situation where you were running an Excel spreadsheet alongside an APL session, with the values in some range of cells shared with an APL array. As you modify the array in APL, the spreadsheet reflects the changes instantly (possibly on a chart); alternatively when you update the spreadsheet you find that the values in the array automatically stay in step. This sort of thing makes particular sense when one of the partners is a background task, such as an SQL server. Rather than setting up an APL-specific database link through SQL\*NET, you just use a standard windows task (probably also used by Excel) via DDE. It all looks so much simpler!

## Where I would like to be in 2 years’ time

I want an APL system that is a real pukka Windows application!! That means a lot of work for somebody, but the benefits must surely be enormous for APL in general, and in particular for the first vendor to get there! Here are a few reasons why:

- if you know one Windows application, you know them all! No more session managers or editors to learn ... just use the Notepad to edit functions and the Clipboard to cut and paste! At last I will be able to throw away all my code for pop-ups and pull-downs and dialog boxes! How much simpler it would be if I let Windows do all this for me.
- I want to write systems which look for all the world like other Windows applications. No-one need know I wrote them in APL in 1/10th of the time it took some poor hack to write the same thing in C. If anyone asks, I just say that I used this fancy set of C macros, like `⍴` and `∘.=` ... it may help.
- true integration of text and graphics. I want to be able to edit the data in one window, and see the graph change in another. Alternatively, I want to drag the graph around with the mouse, and see the numbers change to match. I want to be able to put a map of Europe on the screen, and see the production plan at Halifax by pointing at it ... and so on.
- DDE. This should go without saying. I want to share data between background server tasks, APL, and any other Windows applications I happen to be running, like Pagemaker or MS Word.
- no more hanging on the coat-tails of DOS-extenders like Phar Lap. Assuming Windows really has got the memory management right (and Microsoft aren’t stupid) we should be clear to run up to 15Mbyte and beyond. We may at long last shake the notion of runtime licences out of the system.
- a whole lot of intangible things, like the far richer visual environment that Windows gives me. Some of the games are quite good too ... I suspect that proficiency at Reversi has taken over from proficiency at Billiards as a sign of a mis-spent youth.

I am sure St Paul felt the same on the road to Damascus ... MicroAPL and their Mac users must be laughing like drains at all this; they have been shouting it from the rooftops for years. I have nothing to say in my defence except that I was blind and now I can see! Please don’t take my mouse away!!
