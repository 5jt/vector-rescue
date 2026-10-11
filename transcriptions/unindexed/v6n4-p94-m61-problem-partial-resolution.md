---
title: 'The M61 Problem: a Partial Resolution'
authors: []
volume: '6'
issue: '4'
page: '94'
unindexed: true
transcribed: 'from page images of VOL.6-NO.4-APRIL-1990.pdf, page 96 (printed 94; within the Technical Section, after art10008320); Claude, 2026-10-11'
review: draft
tags:
- user interfaces
- implementations
queries:
- "Unsigned note with its own heading, on the page after Adrian Smith’s “Hackers Corner: the Falkoff Dual Keyboard” (art10008320, which ends on p.93) and before Technical Correspondence (p.95); probably by the editor, Adrian Smith. It follows up “Hackers Corner: Beware the M61” in Vector 6.3."
---

## The M61 Problem: a Partial Resolution

For readers who own (or are thinking of buying) a PS/2-M61, the keyboard problem highlighted in the last Vector has been partially resolved. Apparently, IBM have changed to a new keyboard controller, which affects the scan codes sent to your application. Of course there is a new keyboard handler to cope with this, so mostly you don’t notice a thing.

However, when APL\*PLUS/PC attempts to flash the keyboard lights (e.g. if you hit Caps Lock), or if your code attempts a peek to see if Caps Lock is down, it resets the driver to the old version!! This totally screws the keyboard, as reported in Vector 6.3. The fix is:

```apl
      0 ⎕POKE 879   ⍝ Cancel keyboard lights
```

… this appears to be OK in the APL\*PLUS/PC standard system versions 8/9. Obviously, it needs to be the very first line in the very first function in `INIO`. It worries me slightly that on a couple of occasions I got the problem in a `CLEAR WS` before I had even touched a key, and on one occasion I got it in DOS having simply done `)OFF`. This suggests that there may be at least one more trigger in there somewhere, which will sooner or later catch me out!

As far as I can test, the extended system (APL\*PLUS/PC or APL\*PLUS II) does not show the problem. Watch this space.
