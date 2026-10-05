---
title: 'Case Study: VSPC – The Last Rites'
authors:
- Adrian Smith
volume: '3'
issue: '1'
page: '68'
unindexed: true
transcribed: 'from page images of VOL.3-NO.1-JULY-1986.pdf, pages 70–76 (printed 68–74; art10006020 follows on p.75); Claude, 2026-10-05'
review: draft
queries:
- "Part 2 of the VSPC conversion saga; part 1 is “VSPC: for whom the bell tolls?” (art10008170, Vol.2 No.2), which we have no scan of (#62)."
- "The opening IEC161I console messages are printed in bold capitals; transcribed as a code block."
---

## Author’s Note

by Adrian Smith
{ .byline }

As promised, here is part-2 of the VSPC conversion saga. Much of what follows is lifted straight from my Email diary; a potentially fascinating archive for the software archaeologist of 4086!

If there is a moral to be drawn from this tale, it is probably “Panic sooner rather than later”. In general a problem perceived was a problem solved; once we had wound ourselves up to face the fact of TSO the actual conversion rapidly became a well-drilled routine.

The ‘wake’ was scheduled for April 1st at 8.00pm; some of us made it with rather less than 2 hours to spare!!

## VSPC : The Last Rites

```
IEC161I 056-084,TX02001,IEFPROG,OPTION,,,SYS3.ISPF.OPTIONS.CLUST
IEC161I SYS3.ISPF.OPTIONS.DATA,ICFUCAT3
IEC161I 056-084,TX02001,IEFPROG,OPTION,,,SYS3.ISPF.OPTIONS.CLUST
IEC161I SYS3.ISPF.OPTIONS.INDEX,ICFUCAT3
IEC161I 062-086,TX02001,IEFPROG,OPTION,,,SYS3.ISPF.OPTIONS.CLUST
IEC161I SYS3.ISPF.OPTIONS.DATA,ICFUCAT3
```

To recap briefly . . . . I left my tale of woe suspended in mid-air towards the end of September 1985. The things that were really bugging me at the time were:

- the TSO environment, in particular the session manager, and the way workspaces were saved and (?) shared.
- VSAM record-locking. Could VSAM files be held at the record-level rather than by reserving the whole file?
- the sheer bulk of data to copy across and check through.
- the persistent rumours of heavy increases in CPU cost.

In no particular order, this is what we did . . . .

### VSAM Record Locking

The first problem to be tackled was the knotty one of multi-user VSAM files. We depend absolutely on these for all our APL printing; a routine called VTAMPRT scans constantly through a shared VSAM file, pulling off completed prints and dishing them out to the appropriate destinations. Typically up to a dozen users could be spooling prints concurrently to the file, so to try to work with file-level holds would be quite impossible.

Diary: 24/10/85

> “Current state of play on VTAMPRT:
>
> As feared the VSAM record locking does not hold up under TSO. We really do need shareoptions 3/4 as otherwise every user locks the whole file while they update. Ergo there are two lines of attack:
>
> 1. Andy writes an assembler routine to book the record for us. This could use shareoptions-4 and then ENQ appropriately. I suspect that we would need a product called CALL/AP (from the same stable as AFM) to do this.
> 2. Having booked the frame we then read it back to check that it hasn’t been double-booked. This adds a bit to the VSAM I/O, but is hardly significant as Andy is increasing the record length to 22K. Most prints (168 by 20 = 3360 lines) will fit on one frame anyway.
>
>     The only worry is that each user will simply re-read a buffer, rather than the real record! As soon as Andy has set up a file I suggest we check this. The only way round might be to close/re-open the file . . . yuk!”

Diary: 28/10/85

> “More on TSO and VTAMPRT . . .
>
> It appears that with shareoptions-4 we can re-read the control record to check that we really have grabbed it. DJW & I did a quick check of the protocol on Friday, and it behaved as expected (as did shr-3 which simply re-read the buffer and is therefore quite useless). Essentially this is a ‘last-in first-served’ queue; hardly fair but quite effective!
>
> I am now recoding a version of the APL side to fit in with this new protocol, and also to make use of the 22K record length (168 lines of print per record).
>
> To do this efficiently I feel I need to change the way print data is buffered in APL (catenating to the end of a buffer this big could get very slow . . . the cost goes up as the square of the object size). I shall experiment with some alternatives and do a few timings . . . we should be able to cut a fair whack off the CPU cost of printing (as well as chopping the VSAM overhead by about 3/4) if we take a bit of care over the design.”

Diary: 29/10/85

> “I think that we are home and dry with TSO/VTAMPRT.
>
> Andy has written a little assembler command which books a frame number and returns the frame number it booked. This is able to queue sensibly on the records, and there is no possibility of a double-booking. It also simplifies the APL routines and seems rather faster. All the APL side now does is generate a random slot number (1 – 99) as the starting point for a sequential search for a free slot.
>
> I don’t think that this is likely to lead to any more searching than the present strategy of trying all 99 slots at random. Apart from this very minor change the new routine is functionally equivalent to the old one. I shall now try some comparative timings of the two systems. I don’t expect to see any significant difference.”

Diary: 4/11/85

> “The final timings on the new VTAMPRT for TSO suggest a reduction in CPU (as recorded by APL) to approx 70% of what it was. This is largely due to the 22K blocking, and only really shows up for files of 2000 lines or so. However the new booking arrangement does mean that even for small files (1 line) the new system is ahead (92% of the old).
>
> I think we can safely put this one to bed.”

As you can see, the final solution (found after several blind alleys had been explored) was simple and effective. Because we could ‘book’ a slot on the file with a simple TSO command (the numeric return code suffices to get back the slot number) we could get away with AP100 as the assembler interface. Of course it was much easier for APL to generate the random starting point, so this is passed as a (formatted) number, along with the user number, date and time.

As an aside, I got caught out by the behaviour of ⎕RL when you start with too small a seed. Due to an attack of sloppiness I set the seed to ⎕TS[5 6] encoded to base 100. If you generate ?99 from this the maximum number you get varies from 5 to 48 depending on the number of minutes past the hour! Consequently users were getting dreadful response to print requests just after the hour, because the booking routine always started to search from the very low end of the file. Slots above 49 were never used, which is why the problem soon became painfully obvious!!

### Workspaces and Files

One little note in the TSO-APL manual brought on a bad attack of fear. It pointed out that a system problem in the middle of a )SAVE would not only lose your immediate changes, but would by then have wiped the previous copy! This looked like a sure-fire way to lose a day’s work, and as true believers in Murphy’s Law we felt that we had to do something about it. The obvious line of attack was to use ‘Partitioned Datasets’ (PDSs), rather than simple sequential files, for workspace saving. These preserve the old version during a )SAVE, but have a nasty habit of filling up with old copies and needing compressing just when you don’t want to.

Once again an angel of mercy came to the rescue, in the unlikely guise of PDSMAN. This little wonder will reuse old slots and generally attempt to keep things tidy; it can’t always make full use of the space available, but at least the need for regular compresses is avoided.

Once we had bitten the bullet and patched APL to use our PDS libraries we began to think round our ‘ideal world’ solution to the whole area of project libraries and data sharing. What we needed was some set of conventions which would protect private data, but allow easy read access for crash recovery, and controlled write access for routine maintenance. In general we wanted to get away from our VSPC habit of logging on to other people’s IDs for routine updating.

The structure we settled on gave each TSO user two APL libraries:

```
APL.GLOBAL.AW002001     ... shared data for user 2001
APL.PRIVATE.AW002001    ... private data
```

In addition there are any number of ‘Project Libraries’:

```
APL.SHARED.AW100012     ... updated by anyone in (say) OR
```

. . . and of course public libraries which are updated only by a select band of initiates:

```
APL.PUBLIC.AW000020     ... Adrian’s utilities on )LIB 20
```

From an APL point of view, this works quite nicely once you get accustomed to the distinction between ‘)LIB’ and ‘)LIB 2001’; obviously you need to remember ‘)WSID 2001 MYWS’ if you want the fruits of your labours to be generally available. However it is a bonus over VSPC to have the command ‘)LIB 2012’ return the contents of someone else’s global library; again this saves one from logging on to the owner’s Id to find out what he called things! For the first time, we really don’t need to know each other’s passwords . . . this must be a good thing in the long term.

### The APL Session

I felt that the VSPC Session Manager had been written by someone who used session managers; the TSO equivalent gives quite the opposite impression. It has that unwieldy feel which is so characteristic of ‘design from the outside’; it just doesn’t come comfortably to hand.

The only real bonus is the facility to queue a bunch of lines for re-execution. Particularly during the ‘peak’ of our conversion activity I found I was constantly going through ‘)LOAD this; )COPY that; )WSID the other; )SAVE’ routines; the session manager was very helpful in automating a lot of this.

Now for the gripes . . . the colours you can mitigate (by setting ‘Highlight Off’) or improve (by sneaking on to page 1001 and resetting them) to be quite acceptable. The behaviour on \<CLEAR\> still seems inexcusable. To be faced with the rigmarole of \<RESET\> \<PA2\> and \<ENTER\> to recover from a perfectly reasonable assumption (to clear the screen . . . press the key labelled ‘CLEAR’) is absurd. So far I have failed to find any way round this; closing and re-opening the GDDM device with a different ‘clear/PA1 protocol’ leaves you unable to interrupt APL loops. Has anyone else got any bright ideas??

Developing lines of APL ‘at the terminal’ is far less convenient under TSO. VSPC had a very handy \<Last\> key which pulled back whatever you just did, for possible modification and re-execution (APL\*PLUS/PC has the same thing). Under TSO you have to go and find the damn thing (it might be several screens back) or just give up and re-type it. Oddly enough you often want to repeat a line without changing it at all; to be forced into overtyping (say) blank with blank to get the line back . . . . well what can I say??

In summary the session screen would be improved out of all recognition with two extra facilities:

- a ‘last command’ facility available via SM command or PFkey.
- a ‘mark’ key to re-execute a line without the nonsensical modification.

IBM, are you listening?

### The Conversion

TSO does have some nice things, one of the most useful being a sniffer-dog called ‘APL WSID’ which goes poking about in your workspace to find the time and date it was saved. Having discovered this, I did a bit of hacking and came up with the following:

Diary: 26/11/85

> “To whom it may concern . . .
>
> I am now in possession of a Trojan Horse routine which will copy into your workspace any utilities which are:
>
> - already there
> - are on the utility library with a saved date after the date when the workspace itself was saved.
>
> I suggest we adopt this across the board as the latent exec, and will thus be saved all the hassle of recopying changed utilities under TSO”

This simple notion had the enormous benefit that we could ‘preset’ the conversion in existing workspaces. In systems where we needed to move around 20 users ‘simultaneously’ we just wouldn’t have had time to load up all the workspaces, make the changes and resave, in one weekend. All we now needed to do was (at leisure) to patch in AUTOEXEC and let the system cope with the upgrades. Wonderful. What’s more it really did go alright on the night! I think we had between 3 and 5 cases where someone had been ‘naughty’, and had changed a standard function without renaming it. I’m afraid we also had one example of a utility which was not (quite) upward compatible; it suddenly started returning 1-element vectors instead of scalars!! These minor snags apart, everyone carried on as if nothing had happened.

I had been quite right in seeing AFM as a major saving grace; in almost every case we were able to stick to the same user-number (VSPC 32670 became TSO PX32670=AFM 32670), so all those embedded user numbers:

```apl
'18750 BUDGET' GET 'VAR1,VAR2,....,etc'
```

. . . caused us no hassle at all! In general we had completed the AFM conversion several months before the final move to TSO, so it was literally a 5-minute batch run to copy over all the files for a set of target users. Apart from one spectacular cock-up when we accidentally deleted the entire TSO/AFM system, all went astonishingly smoothly.

### Postscript

TSO is undoubtedly a more ‘powerful’ environment than VSPC. The easy access to batch, and the linkage to packages like ‘Focus’, are major improvements. It is also much less ‘protective’; the occasional splurge of red messages is bad enough, however it is quite possible to (say) ‘abend’ the session manager or get hung up somewhere between APL and SPF; in every case your only escape is to ring up and get thrown off the system! With a lot of work, we made TSO bearable; in the long term we may well be better off, but there is a lot of lost ground to make up.

I would like to conclude with two more diary entries, both slightly facetious:

Diary: 19/02/86

> “In checking through the vector and image symbol editors I have come across a slight oddity in that my sheep have mysteriously turned green! This turns out to be a minor change in the use of the GSIMG command and is now OK. As far as I can see there is no problem in exporting VSPC-created symbol sets to TSO and building your own library of vector/image symbols.”

Diary: 10/03/86 (Reference VDU menu entry for TSO)

> “Most of us tend to see TSOB as short for TSO – B
>
> Most users tend to see it more in terms of T – SOB, which loosely translates as ‘That Son Of a Bitch’. Is this a good idea??”

**1986 (May): Concluded**
