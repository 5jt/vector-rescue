---
title: 'Hacker''s Corner: Getting Another 128 Colours on your EGA'
authors:
- Adrian Smith
volume: '6'
issue: '2'
page: '114'
unindexed: true
transcribed: 'from page images of VOL.6-NO.2-OCTOBER-1989.pdf, page 116 (printed 114); Claude, 2026-10-12'
review: draft
tags:
- system interfaces
- user interfaces
queries:
- "Contents line “Hackers Corner: 256 VGA Colours”; the printed heading is “Hacker's Corner: Getting Another 128 Colours on your EGA”. Printed 113, before it, is the Technical Section’s introduction page (no Contents line; not transcribed)."
- "The workspace function names in the APL font (WIN∆INIT, FSM∆FMT) are set as code."
---

*by Adrian Smith*
{ .byline }

Once again, Hackers' Corner takes a delve into the innermost secrets of your PC, but this time it is all decent and honest BIOS-compatible stuff! Sorry John, and all you hackers out there who found that getting at your PSP was less than easy under the PLUS II system: I hope this one will work for you!

Those of you with colour screens will have noticed that several packages allow you the full range of 16 background colours as well as the normal 16 in the foreground. However if you are tempted to try this with say `⎕WPUT 143`, all you will get is blinking white on black, rather than white on a nice dark grey. Now one of the packages which does give you the option of bright backgrounds is APL2/PC, so I rang Dave Selby and asked how he did it. In fact it is a standard BIOS call, but only applies to the EGA and VGA monitors, so none of the usual PC reference books mention it.

The little function below will do the trick, or you could just close your eyes and type `4099 ⎕INT 16` if you prefer.

```apl
    ∇ BLINK SW;RG
[1]  ⍝ FLIP BACKGROUND FROM BLINKING TO INTENSIFIED
[2]  ⍝   AH = 10H      ... BIOS SERVICE 10
[3]  ⍝   AL =  3H      ... SUBSERVICE 3
[4]  ⍝   BL = 0/1      ... 0 = BRIGHT; 1 = BLINK
[5]   RG←(4099,SW>0)⎕INT 16
    ∇
```

A couple of small caveats: Ctrl-Esc resets the screen to the default (i.e. blink) state, as does Desqview if you run your APL session in a window. I have incorporated the above code in all my screen routines (specifically `WIN∆INIT` and `FSM∆FMT`) so that I don't have any problems restarting after a break.

The improvement in appearance of standard data-entry screens is considerable (I recommend almost any colour on dark grey as a background, bright white on bright blue for fields, black on yellow for warnings, bright white on bright red for critical errors), and you can do a fair impression of OS/2 Presentation Manager with plenty of bright white as background!

Have fun!
