---
title: 'Technical Correspondence (Sullivan, Barker, Branson)'
authors:
- John Sullivan
- Simon Barker
- Peter Branson
volume: '4'
issue: '2'
page: '93'
unindexed: true
transcribed: 'from page images of VOL.4-NO.2-OCTOBER-1987.pdf, pages 95–99 (printed 93–97); Claude, 2026-10-06'
review: draft
tags:
- programming techniques
- system interfaces
queries:
- "Three letters: John Sullivan (How to Unlock Locked Functions in APL2), Simon Barker (More about APL2), and Peter Branson’s (Idioms and Oddities); the last is signed at its end. The writers’ addresses, as printed, are kept."
- "⎕AF and ⎕FX are printed with small capitals after the quad; transcribed as ⎕AF, ⎕FX."
- "IDIOM is printed with a crossed slash before X←A2, read as ⌿ (rows), and ⍉ for the transpose glyph. Checked: selecting rows by the mask as read gives both printed results: SURELY THERE MUST BE A BETTER WAY!, and a 0 4 matrix for THIS THIS THIS THAT THAT."
- "Slips transcribed as printed: “Natonal Westminster Bank”, “heiroglyphic”."
---

## How to Unlock Locked Functions in APL2

<p>From: John Sullivan<span style="float: right">27th May 1987</span></p>

Now that David Piper has ‘blown the gaff’ on the APL2 system command )CHECK SYSTEM, I feel I can rush into print with the following useful item. You may, for some reason or other, have a locked function that you want to unlock, and nowhere in the APL manuals can you find a way of doing this. The method is as follows:

In the APL workspace, enter the following

```text
)CHECK SYSTEM SYSDEBUG(128)
)OUT filename function-names
```

Then you edit the output file (which will be APLTF.filename in TSO, unless your system has changed the defaults or you have enclosed the name in quotes), changing all occurrences of 1 1 1 1 ⎕FX to 0 0 0 0 ⎕FX. You can do this without leaving the workspace if you are using ISPF. The final step is to enter

```text
)IN filename
```

and your functions will then be unlocked in the workspace.

Note that if you don’t issue the )CHECK command, the )OUT command will not write the locked functions to the output file.

P.S. With reference to Joseph de Kerf’s reply in the latest VECTOR to my article on Fast Fibbing, yes I did know about omitting the second term in the formula (it appears in other sources, not just the one cited. A good analyst should be able to spot that the second term can be omitted without reference to the sources, in this case), but in my hurry to prepare the article, which was written from memory, I completely overlooked it. I realise that this is not good enough, and so I tender my humblest apologies. Mea culpa!

<p style="margin-left: 2em">John Sullivan<br>Business Development Division<br>Natonal Westminster Bank plc<br>41 Lothbury<br>LONDON EC2P 2BP</p>

## More about APL2

From: Simon Barker

Following on from Dave Piper’s letters regarding the undocumented APL2 features, here are some more oddities/features/bugs that have come to light.

### The Atomic Function (⎕AF)

Primarily, this system function has two uses: given a simple text array it will return the indices into the atomic vector for each element; and when given an array of integers within the range 0 to 255 will use these as indices into the atomic vector to return text. In both these cases an index of origin of zero is used which is local to the system function.

This is not the end of the story however, because ⎕AF will return a result for ANY positive integer. When an integer exceeds 255 a special character is returned which is not a member of the atomic vector (typically, IBM chose to represent this as an Omega symbol). This can be regarded as a character encoding of the given number, with a storage requirement of 4 bytes. Thus, when ⎕AF is given this symbol as its argument the original number encoded is returned.

As you may know, APL2 will store integers in a single byte if the values lie in the range 0 to 255. The only way I have found to force storage in this way is by using ⎕AF. All that is required is to use ⎕AF on the output of ⎕AF used on the data you wish to compact. Beware though, any number representation other than positive integer or boolean gives a domain error.

### The )CHECK Command

Here are some parameters that can be passed to the )CHECK system command.

```text
)CHECK SYSTEM SMAPL (OFF)
```

This will switch the Session Manager off mid-session, saving screen data if the log size is set greater than zero.

```text
)CHECK SYSTEM SMAPL (ON)
```

This switches the Session Manager back on, with no corruption of the session log if the log size is set above zero.

```text
)CHECK TRACE STMT
```

This will display each line of any function or operator executed, next to a CPU usage figure indicating how much CPU time has elapsed prior to the execution of the line.

```text
)CHECK TRACE EXEC
```

This command displays information for any line of APL that is executed, whether in a function, operator, or entered directly. As well as showing the information indicated above, special two-character prefixes are used to indicate how APL2 is processing the expression. These indicate such things as recognition of idioms that are coded as special routines in the APL2 Executor.

Other facilities available include various types of workspace dumps, listings of the names of the assembler modules that APL2 is comprised of (with save dates, problem reports, etc.), and other trace options. A full explanation of these commands is available in the IBM manual “APL2 Diagnostic Reference”, order number SY26-3932-1.

### Notes

I am currently using APL2 release 2, running under CMS, at my workplace. Prior to this I used VSAPL under CICS and CMS.

Keep up the good work on VECTOR - it’s much better than Quote Quad, and at a cheaper price.

<p style="margin-left: 2em">Simon Barker<br>55 Conisborough Crescent<br>Catford<br>LONDON SE6 2SP</p>

## Idioms and Oddities

### Removal of all rows which are duplicated

Removal of duplicate (multiplicate?) rows from a character matrix (leaving 1 copy) is a much-used process with several idiomatic synonyms. I tend to stick to the 1 1 transpose version, e.g. FINNAPL No.208 (et al), from which the following is derived.

I recently found a need to do a similar thing, except that I wanted to scrap all the entries in duplicated rows (i.e. no copies retained). One feels that this must be published somewhere, but I have a limited set of APL references, and scanning the FINNAPL permuted index under ‘duplicate’, ‘rows’ etc. got me nowhere - although I always have a nasty feeling that with 600+ entries I might have missed something.

Hence the suggestion listed below, which at least served my purpose at the time. Although I slightly regret the embedded assignment, I think it makes it a little clearer than repeating the assigned part, and perhaps it makes it more efficient.

```apl
      IDIOM
(~+/<\Y-<\Y←X∧.=⍉X)⌿X←A2

      A2                       THIS IS ONLY TO DEMONSTRATE THE EDGE
SURELY                         CONDITION (ALL ROWS ARE DUPLICATES),
THERE                          AND ORIGIN INDEPENDENCE.
MUST
SAME JUNK                            ⍳3
BE                             1 2 3
A
SAME JUNK                            A2
SAME JUNK                      THIS
BETTER                         THIS
WAY!                           THIS
                               THAT
      ⍎IDIOM                   THAT
SURELY
THERE                                ⍴⍎IDIOM
MUST                           0 4
BE                                   ⎕IO←0
A
BETTER                               ⍳3
WAY!                           0 1 2

                                     ⍴⍎IDIOM
                               0 4
```

### A peculiarity in Quote Quad …

Using VS APL under VM/CP I had, tucked well down in a 30-odd line function, two lines of fairly conventional form:

```apl
⍞←SINK←'MESSAGE'
→(('YN'=1↑(⍴SINK)↓⍞),1)/YES,NO,OTHER
```

but kept getting the message catenated onto the name of a local variable. After looking in the wrong place for a while, I decided to think instead, and soon found towards the top of the function I had accidentally typed:

```apl
...... 1↑0⍴⍞←VARNAME ......
```

where the Quote-quad assignment should not have been there at all! Well, that was alright; after deleting the two unwanted symbols it behaved properly. Clearly, because of the ‘nought reshape’, the name was stacked away and appeared on the next Quote-quad call.

However, what I found of interest was the behaviour of TRACE in this situation. With the error present, and TRACE embracing the pair of lines mentioned, the workspace seemed to be locked into an inescapable situation, and the ‘message’ kept re-appearing whatever I did. Normal interrupts (PA1 and PA2) seemed to be of no help, and switching the monitor off (naughty boy!) did no good; the logon gave automatic re-connect into the same loop - with the ‘heiroglyphic’ character set, of course.

Up until recently I have successfully managed to avoid VS APL, but the mortgage repayments need looking after, so I was stuck with it. I will also echo other people’s comments about IBM manuals, so I didn’t bother with those. Well, a little more trial and error showed me the only way out I could find, which was a weak interrupt (PA1) into CP, then a direct CP logoff - and of course you cannot save anything. Interestingly, with the error (and TRACE still on) the same loop re-appeared, but this time the strong interrupt (PA2) worked as expected; one could clear the stack and save the work.

Can anyone tell me whether this problem is specific to VS APL, or do similar things happen with other APL implementations?

<p style="margin-left: 2em">Dr Peter Branson<br><br>Oaklands Cottage<br>Wray Common<br>Reigate,<br>Surrey RH2 0LE</p>
