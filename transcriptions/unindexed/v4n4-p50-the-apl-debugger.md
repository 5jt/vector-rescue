---
title: The APL Debugger (Uniware)
authors:
- Alasdair Richardson
volume: '4'
issue: '4'
page: '50'
unindexed: true
transcribed: 'from page images of VOL.4-NO.4-APRIL-1988.pdf, pages 52–53 (printed 50–51); Claude, 2026-10-12'
review: draft
tags:
- reviews
- development practice
queries:
- "Printed heading “THE APL DEBUGGER”, “reviewed by Alasdair Richardson”."
- "APL names are spelled out in words as printed (quadEX, deltaDEBUG, 'goto deltaDEBUG', quadEDIT, quadELX, quadSEG, quadPOKE), not converted to APL symbols."
- "Kept as printed: the quotation mark pairing in \"WAIT'; “If Uniware manage to”."
---

## THE APL DEBUGGER

*reviewed by Alasdair Richardson*
{ .byline }

All programmers have to debug their programs, and APL programmers are no exception. I use APL\*PLUS/PC, and up to last year I was quite happy that an interpreted language, together with STOP and TRACE, makes this an easier job for me than for programmers in most other languages. Then at APL 86 I saw a product demonstrated which seemed to offer the possibility of making debugging even easier. This was the APL DEBUGGER from a French company UNIWARE. Shortly afterwards I ordered a copy, and have never looked back.

So what does this marvellous piece of software do? The beauty of the debugger is that you can, with the minimum of effort, actually watch your function executing line by line, see the result of each line, and home straight in on the line which is causing a problem. The time saved when debugging can be very substantial, and the simplicity of use can save a lot of swearing and cursing when you forget to put a STOP on the right line, remove STOPS before )SAVEing etc.

You are supplied with a workspace called DEBUGGER.AWS, which contains 15 functions and one variable. The functions are called deltaDEBUG, deltaDEBUG1 and so on up to deltaDEBUG14, and the variable DEBUGFNS is simply a list of the names of these functions. To use the debugger you first )COPY the workspace into your own workspace (the variable DEBUGFNS just makes it easier to get rid of them afterwards by quadEX DEBUGFNS). Then you insert 'goto deltaDEBUG' as the first line of the function you wish to debug. It doesn't matter if you are debugging a stand-alone function or one which is embedded in the middle of a complete system. The function can be recursive, and you can debug more than one function at a time.

When the function you are debugging is called, a flashing "WAIT' appears at the top right of the screen, and after a short time a window opens up at the right of the screen showing that function. The current line is highlighted in reverse video. Pressing RETURN takes you to the next line. As that line is executed, another window opens up at the top containing the full line of APL, and underneath the final result if there is one. If the result is too large to fit in the window, the cursor keys will scroll it so you can see the whole result. Pressing RETURN again takes you to the next line. Diamondised statements are executed one at a time, so unlike TRACE you can see the result of each statement. Comments are just ignored.

When a statement writes to or reads from the screen, the debugger will recognize this and withdraw all its windows so you can see exactly what your application screen looks like, then pressing RETURN again takes you back into the debugger. Pressing Scroll Lock opens up an 'immediate execution' window at the bottom left of the screen, the size of which you can alter if you so wish. In this window you cannot use any APL commands or branch expressions, but you can look at or alter any variables, test variations of APL statements etc. You cannot use quadEDIT to alter your function, but if you find a variable which has been given the wrong value you can alter it and carry on, or you can enter a naked branch to take you straight out to APL.

There are a few (well documented) restrictions on the use of the debugger, and I will just mention the most important here. It cannot be used for debugging graphics functions, which is a pity as the poor graphics programmer could really do with a tool like this. Your application quadELX does not work when debugging. If you are using your error handling purely for error trapping of course this doesn't matter, but if you are using it for cutting back the stack or something you need to be aware that it's not going to work. Finally if you want to use quadSEG or quadPOKE in the immediate execution window, you should read the supplied documentation carefully.

I have been using the DEBUGGER now for 9 months, and have come across only a few very minor irritations. Pressing Ctrl/ENTER will cause your function to go on executing as if you were continually pressing ENTER, but the result of each line is still shown so it takes some time. It would be nice if you could indicate that you want to stop displaying each line as it's executed after you have located your problem and if you don't want to branch straight out to APL. Occasionally using the debugger does odd things to the cursor, which have always been irritating rather than important. Thus very occasionally when branching out to APL I have been left with no cursor at all, necessitating going to look up the correct POKE in the manual to get it back again. When using the debugger in conjunction with POWERTOOLS/PC (an extremely useful combination), returning to menu fields you find that a cursor appears where normally it wouldn't.

All in all the APL DEBUGGER is a tool I would highly recommend to any APL programmer using APL\*PLUS/PC for non-graphics applications. If Uniware manage to produce a release 2 allowing debugging of graphics functions and the use of quadEDIT on the currently executing function it will be just about perfect.
