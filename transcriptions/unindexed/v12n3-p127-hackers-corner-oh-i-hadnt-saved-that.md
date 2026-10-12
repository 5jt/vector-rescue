---
title: 'Hacker’s Corner: Oh **** !! I Hadn’t Saved That!'
authors:
- Dave Phillips
volume: '12'
issue: '3'
page: '127'
unindexed: true
transcribed: 'from page images of VOL.12-NO.3-JANUARY-1996.pdf, pages 129–131 (printed 127–129); Claude, 2026-10-12'
review: draft
tags:
- programming techniques
- user interfaces
queries:
- "Printed heading “Hackers’ Corner: Oh ***! I hadn’t saved that!”, byline “by Dave Phillips”; the Contents line has “Hacker’s Corner: Oh **** !! I Hadn’t Saved That!”."
- "The underlined Δ of the APL\\*PLUS III code (Δautosave, Δwsid) is given as ⍙; the execute symbol in AS_Init[18] as ⍎; the match in AS_Timer[7] as ≡. The italic code face in the running text is given as code."
- "Kept as printed: “accompanied with”; “prefered”; “Ushort (i.e. 65536)”; “Win16”; the comment in AS_Init[16] “and interval is U”."
---

*by Dave Phillips*
{ .byline }

Don't you just love Windows? There you are minding your own business doing a bit of quiet experimentation into how to get things to happen in your *favourite* operating environment when all of a sudden... 'Now where did that go ?!!' ...usually accompanied with a much longer stream of unprintables.

And because you hadn't been too sure where your experiments were leading you hadn't troubled to save the workspace until you'd got something worth saving... ...and now you've got nothing!!

Being a 'bear of very little brain' this happened to me more than once and I was getting tired of it! Something had to be done! An autosave facility seemed to be a necessity.

So, how could I get my APL\*Plus III system to `)SAVE` every five minutes, say. If I could have a Windows Timer control around with the requisite 5 minute interval then when the interval popped off perhaps I could have that save my workspace. But I certainly wouldn't want to have to precondition each and every development workspace with a lot of code just for autosave.

Now, in Vector 11.1 Eric Lescasse (p112 et seq) showed how to build a small 'Time' application. More importantly he very clearly demonstrated the independence, in APL\*Plus III, of objects from any workspace. He )CLEARed the workspace and showed that the form still functioned properly. This is entirely true with one caveat, all the callback code for the object has to be contained within the definition of the object itself. That is fine when the callbacks are simple APL statements but what if they are of greater complexity requiring one or more functions to be called — if those functions have to be in a workspace 'BANG!!' goes our workspace independence.

Fortunately APL\*Plus III objects have the great facility of being able to store data on them — not just 'text' to go in an editbox or a 'list' for a listbox but any old data can be stored in the 'data' property of any form or control — and where goes data so too can go the canonical representation of a function.

I was nearly there; some code to build the form and load the data property with the `⎕VR` of some more code to oversee `⎕SAVE`ing the current workspace; an `onTimer` event to retrieve the function definition and run it; a switch to turn autosaving on and off; and finally cause all this to happen automatically by calling it in `⎕lx` of a workspace which would be loaded as the initial workspace every time I started APL\*Plus III.

The form, once created, would be 'owned' by the APL session so there'd be no need to worry about any closedown procedures — closing the session would close and delete all owned forms. Also, since `'New' 'Form'` would produce a form which was open (although in this case it would also be hidden), the Timer control would be active as soon as it was created. There would be no need for a wait-loop on this form, instead it would be activated when Windows generated the timer event. So there I had it!

Of course Windows had to have the last laugh! The Windows SetTimer call has a maximum interval setting of Ushort (i.e. 65536) milliseconds! ...just over 65 seconds. So, a little more work would have to be done by the autosaver unless I was going to be saving every minute! ...and I thought that was probably a little excessive. Also, I thought it would be best to save the workspace as 'AUTOSAVE' rather than have the possibility of a rubbishy experimental state overwrite something I would have prefered to keep intact.

So the final ingredients for this recipe are:

1. An entry in APLW.INI

    ```
    [Config]
    Initial Workspace=D:\Work\aplw1_2\initws
    ```

    to load my initial workspace INITWS.W3

2. INITWS.W3 has

    ```apl
    ⎕lx ← 'AS_Init'
    ```

3. The On/Off switch for autosaving is simply the existence or not in the current workspace of a global variable `'⍙autosave'` which can be created or erased by setting up a pair of Tools in the APL\*Plus III Tools menu option.

    Autosave on

    ```apl
    ⍙autosave ← 'on'
    ```

    Autosave off

    ```apl
    0 ρ ⎕ex '⍙autosave'
    ```

    ...and, of course, the bits you've all been waiting for ('WAKE UP AT THE BACK!!')

## The Functions to do it ...

```apl
     ∇ AS_Init;rc
[1] ⍝∇ AS_Init - called in ⎕lx
[2] ⍝ This creates the hidden Autosave Object which has
[3] ⍝ its own callback code entirely self-contained.
[4] ⍝ As a consequence this Object is workspace independent.
[5]
[6] :if ~(⊂'autosave') ∊ '#' ⎕wi 'children'
[7]           ⍝ if 'autosave' object does not yet exist
[8]     rc← 'autosave' ⎕wi 'New' 'Form' 'Hide' ('data' 0)
[9]           ⍝ build a hidden form with data value 0
[10]    rc← 'autosave.l' ⎕wi 'New' 'Label' ('data' AS_Timer_vr)
[11]          ⍝ apply a label to the form with data set..
[12]          ⍝ ..to the ⎕vr of our onTimer callback
[13]    rc← 'autosave.t' ⎕wi 'New' 'Timer' ('interval' 60000)
[14]          ⍝ apply a timer with a one minute interval
[15]          ⍝ n.b. 'SetTimer' is a Win16 call in Windows 3.1;
[16]          ⍝ and interval is U, therefore max. value is 65536
[17]          ⍝ i.e. approx 1min 5secs (timer is in msec)
[18]    rc ⎕wi 'onTimer' '⍎⎕def ''autosave.l''⎕wi''data'''
[19]          ⍝ when timer interval pops off, ⎕def the data..
[20]          ⍝ ..from the label and execute it
[21] :end
     ∇
```

`AS_Timer_vr ← ⎕VR 'AS_Timer'` where..

```apl
     ∇ AS_Timer;m;dt
[1] ⍝∇ AS_Timer - callback to handle the Autosave onTimer event
[2]  m←⎕wi ':data' ⋄ m← m+1   ⍝ Recall the current 'minute' from
[3]                           ⍝ the form and increment it.
[4] :if 5 ≤ m                 ⍝ If we've reached 5 'minutes'
[5]     m← 0                  ⍝ ..reset counter to 0
[6]     :if ×⎕nc '⍙autosave'  ⍝ } Is Autosave....
[7]     :andif ⍙autosave≡'on' ⍝ } ...'switched on'
[8]       ⍙wsid← ⎕wsid        ⍝ if so save real wsid as global
[9]       ⎕wsid← 'AUTOSAVE'   ⍝ ..rename the workspace
[10]      'RESET' ⎕save ⎕wsid ⍝ ..and save it
[11]      ⎕wsid← ⍙wsid        ⍝ ..and re-establish proper wsid
[12]      dt←,'G<Z9/99/99 99:99>' ⎕FMT 100⊥100|⎕TS[⎕io+2 1 0 3 4]
[13]      ⎕←'AUTOSAVE at ',dt ⍝ Display an Autosave message
[14]    :end
[15] :end
[16]  ⎕wi ':data' m           ⍝ Store the new 'minute' counter
[17]  0 0 ρ ⎕ex 'AS_Timer'    ⍝ ..and dispose of this code
     ∇
```

...now all I have to do is to remember to turn on the Autosa........... Oh \*\*\*\*!
