---
title: 'Hackers’ Corner: Unlocking Functions in Dyalog APL for MS DOS'
authors:
- Ray Cannon
volume: '7'
issue: '2'
page: '132'
unindexed: true
transcribed: 'from page images of VOL.9-NO.2-OCTOBER-1990.pdf (misnamed: Vol.7 No.2), page 134 (printed 132); Claude, 2026-10-12'
review: draft
tags:
- implementations
- system interfaces
queries:
- "Contents line “Hackers Corner: Unlocking in Dyalog APL”; the printed heading is fuller, “Hackers’ Corner: Unlocking Functions in Dyalog APL for MS DOS”."
- "The DEBUG commands are printed run into the text; they are kept inline here, in code style."
- "Kept as printed: “This will be follow about 8 HEX numbers”; “You the write the change back to disk”."
---

*by Ray Cannon*
{ .byline }

By comparing DYALOG APL workspaces as DOS files, it is easy to discover that locked functions differ from unlocked functions by a single byte. Unlocked functions have a marker of hex 23, but in locked functions, this marker is hex 33.

So here is how to unlock a locked function. (To simplify the explanation, I will use a function called `FOO` and a temporary workspace named LOCK.)

First copy the function `FOO` into a clear ws. Save this workspace as LOCK. (Don't name the ws the same as the locked function as this might cause difficulties later.) Exit back to DOS.

Change directory to the one holding your newly saved ws. Now using DEBUG modify the HEX 33 to HEX 23 viz:- Enter DEBUG thus: `DEBUG LOCK.DWS<enter>` Then after DEBUG's prompt (a minus sign) type: `L 0<enter>` This will load the file starting at offset 0. Then locate the locked function by searching for it thus:- `S 0,700 46 4F 4F<enter>` Where 46 4F 4F is `FOO` (the function name) in hex. Debug will respond with its location thus:- 27F4:05C8 or some such numbers. Ask DEBUG to display its contents round there by typing: `D 05C8<enter>` DEBUG will respond with 8 lines of hex with text on the right. At the position 5C8 in the text will be the function name (`FOO`). In the HEX the function name will be followed by 00. This will be follow about 8 HEX numbers and then the all-important HEX 33. (In the text, this will display as the number 3.) If the HEX 33 is at location 5D4 you change it to HEX 23 by typing:- `E 5D4 23<enter>` You the write the change back to disk by typing:- `W 0<enter>` Debug will say "Writing 062c bytes" or some such. Then exit from DEBUG by typing:- `Q<enter>`

Now reload DYALOG APL, `)COPY  LOCK  FOO` and check `FOO` is unlocked. Simple!

Alternatively, you could write a function in APL to read LOCK as a DOS file into APL, modify the HEX 33 to 23, and write the data back out to the same DOS file. But I'll leave that up to you.
