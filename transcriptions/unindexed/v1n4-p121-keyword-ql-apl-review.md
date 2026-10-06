---
title: Keyword QL/APL - An (Occasionally) Technical Review
authors:
- David Ziemann
volume: '1'
issue: '4'
page: '121'
unindexed: true
transcribed: 'from page images of VOL.1-NO.4-APRIL-1985.pdf, pages 123 and 125–131 (printed 121, 123–129; p.122 is a MicroAPL advert); Claude, 2026-10-04'
review: draft
tags:
- reviews
- implementations
queries:
- "The review of the interpreter described in art10003020; it calls Eastwood’s paper “later in the technical section”, though it appears earlier in the general articles. Printed so."
- "QL/APL’s Quad is printed as # with doubled strokes; transcribed as #. Negative numbers in #CC arguments are printed with hyphens (QL/APL’s single minus sign), as described."
- "Table 1 transcribed from a dot-matrix print. Benchmark 14 reads `Z←MR⌹10↑VR`, 10 `Z←2 1⍉MC`, 18 `Z←⍟VR`. Check: the ratio of total times, Spectrum to QL, is 0.63 (“about 60% as fast”), and IBM PC APL to QL 0.36 (“35% as fast”)."
- "Slips transcribed as printed: “I need to press”, “and result from a good integration”, “approch”, “most experience APLers”, “benchmarks tests”, “its all Greek to me”."
---

by David Ziemann
{ .byline }

Well, it’s here at last - a fully featured APL interpreter that runs on a home micro. It was not long after the first rumours that MicroAPL were planning an APL implementation for the Sinclair QL that I finally stopped procrastinating about buying a home computer. So with a telephone in one hand and a plastic card in the other I ordered my QL and expectantly awaited its arrival. Several years later (or so it seemed) it surfaced. I looked at the four Psion packages that come with the machine (Easel is good) and - dare I admit it - toyed gingerly with the Superbasic language (an excellent Basic, but appears to be slowish). Then I put it away. A while later QL/APL arrived, and the machine seemed strangely more attractive. QL/APL vied with the likes of Dallas and Doctor Who for the use of the television, and often won. This is the story of my initial excursion into QL/APL.

## What you get

The QL/APL package that I received comprised a QL/APL manual, a handy reference “card”, a ROM with carrier and a microdrive cartridge that contained the APL interpreter and a demonstration workspace. In fact about 30K of the interpreter resides on the ROM, which must be plugged into the ROM slot at the back of the QL if you want to use APL. Presumably this frees up some space on the supplied cartridge as well as providing a good degree of copy protection. Having previously had a few nasty experiences with microdrive cartridges (poor maligned beasts) I swiftly took a copy of the master to use as the working copy.

The manual seems comprehensive and introduces QL/APL to three types of user: the user with no computer skills, the user with experience of a computer language and the traditional APL programmer.

## Starting off

The first thing the QL does when you power it on or press RESET is to ask you if you’re using a TV or monitor. QL/APL makes its presence felt even at this early stage by additionally displaying the following reassuring message:

```
QL/APL, Keyword Version 1.03
```

This tells you that the APL ROM is in place and all is well.

## Initial problems

Because I was using an (old and failing) colour TV, I need to press function key F2 (there are 5 function keys in all). This tells the QL that a TV is being used, and then searches for a boot file on the cartridge in microdrive 1 (the left one of the two). With the QL/APL cartridge in place this causes APL to be loaded, and a large red banner is displayed to confirm this. The total load time comes out to a variable 15-20 seconds (not bad compared with a PC), and after this period I was greeted with:

```
QL/APL
Copyright (c) 1984 MicroAPL Ltd.
Keyword Version 1.03 Ws size=28K
```

followed by the message

```
LEAR WS
```

Experience with other APL systems suggested that I had probably not been dumped into some Shakespearian application, but rather that I was just losing the first character of the machine’s responses. Experimentation showed this to be the case, and it was clear that the TV was giving the first column the chop. Although QL/APL was certainly not to blame for this behaviour, I decided to see if QL/APL could be used to provide a solution. It was apparent from the thin white border around three sides of the TV image that QL/APL had defined itself a window to work within, and that if the size of the window could be reduced a solution might be found. APL.68000, on which the QL interpreter is based, uses a console control system function to handle console operations, and it seemed likely therefore that QL/APL should do things similarly. After finding quadCC in the manual (or hashCC as it should probably now be pronounced) a solution was obvious. The statement

```
#CC -8 15 2
```

did the trick. The first element indicates the type of operation to be performed; -8 means “set border width and colour”. (In this case, the minus sign is a high-minus and so the number is negative 8. More about minus-sign handling later). The other two elements here specify a border thickness of 15 with a border colour of 2. The effect was to thicken the screen window border sufficiently to bring its subsequent contents clearly into view.

QL/APL displays what you type in red and all its responses in green - very useful unless your TV is shot. It was simple enough to set the output colour to blue so that it could be seen more clearly, by typing

```
#CC -2 5
```

QL/APL had passed its first test (with flying colours). The ease with which the two problems were fixed was impressive, and result from a good integration of the QDOS operating system’s calls with APL. By the way, if you can afford a monitor then problems with recalcitrant TVs are avoided and you’ll get a readable 80 columns rather than 40. (You can use a TV in 80 column mode, but its harder to read the screen). The picture quality is of course much better, and you can also exploit the QL’s high resolution graphics mode.

## QL/APL features

QL/APL supports all the functions, operators, system variables, system functions, system commands and function editing mechanisms required by the draft ISO APL standard i.e. the ones you’d expect to see in VS APL. In addition it also supports the following features:

- an APL statement separator (&)
- ambivalent user-defined function calling
- a simple single-user component-filing system
- a variable and function overlay facility
- an error-trapping facility
- “if” and picture format as primitive functions
- silent versions of )COPY, )DROP, )PCOPY, )SAVE and )WSID
- application of the execute function to system commands
- a shared-variable processor (although no auxiliary processors are supplied).
- many extra system variables and functions, including:

| | |
|---|---|
| #A | the alphabet from A-Z |
| #BOX | vector-matrix interconversion |
| #CC | console control |
| #CONF | APL configuration function |
| #D | the digits 0-9 |
| #DBR | delimited blank removal |
| #DR | data representation report and conversion |
| #ERS, #ERM, #ERX and #LER | error handling |
| #HC | hard copy function |
| #M | English month names |
| #MOUNT | assign devices to logical units |
| #SI | SI stack as a character vector |
| #SS | string search and replacement |
| #TT | terminal type |
| #W | English weekday names |

QL/APL does not currently support the following facilities:

- the quadFMT formatting system function
- a full-screen object editor
- a Superbasic command interface
- groups ( as in )GROUP etc.)
- an alternate alphabet

## The filing system

The whole of the component filing system is controlled via three primitive functions: fput, fget and fdrop. As far as APL is concerned files have numbers, not names. To write an array X to component 3 of file 27 you would use

```
X fput 27 3
```

Component numbers can be sparse and if the file doesn’t exist when you do an fput, then it’s created. Retrieve the data by coding

```
X is fget 27 3
```

and drop the component by

```
      fdrop 27 3
1
```

When the last component of the file is dropped, the file no longer exists. You can discover the numbers of the extant components on a file by entering

```
      5 fget 27
1 2 4 5 6 7 11
```

and obtain a vector of file numbers by

```
      5 fget 0
27 99
```

A logical unit number may also be specified with each of these three primitives, in order to gain access to the second microdrive or other storage media such as floppy or hard disks.

## Sound and vision

All QL/APL’s control over the console is achieved via the #CC system function, which provides about seventy distinct operations. These can be broadly grouped into:

- arbitrary I/O
- terminal control; cursor positioning, character translation, character attributes.
- channel management; open, attach and close channels.
- sound control
- graphics (the largest group)

In many cases the intrinsic power of the QL is made available to APL by direct QDOS calls from #CC. For example, the QL’s graphics facilities can be invoked by use of #CC. Points, lines arcs and ellipses (generalised circles!) can all be directly plotted in both relative and absolute coordinate systems. Flood mode can be turned on to cause subsequently drawn graphic objects to be automatically filled with the desired colour and filled rectangles may also be drawn. In high resolution mode 8 distinct solid colours are available, with blended colours, or stipples as they are called, making the total up to 255. As an example, an ellipse can be drawn by

```
#CC -204 50 60 1500 15 100
```

The -204 tells #CC that an ellipse is to be drawn using the absolute graphics coordinate system. The x and y coordinates are 50 and 60, with the eccentricity of the ellipse 1500 in this case. (An eccentricity of 1000 will produce a circle). The radius is 15 graphics scale units and the rotation of the ellipse is 100 milliradians.

The syntax chosen for CC does not allow for a matrix to be passed in, and so a whole set of ellipses (say) cannot be drawn at once in this way. However the right argument is allowed to be a vector of CC calls catenated together:

```
#CC -2 3 -24 70 80 -222 90 100
```

Here the -2 sets the output colour to 3, the -24 sets the graphics cursor to graphics coordinates 70 80 and the -222 draws a line from the graphics cursor to the absolute point at 90 100.

Unfortunately the right argument to #CC is restricted to 50 elements, and therefore no more than 8 ellipses, for instance, can be drawn at once. It is fairly easy however, to write a cover function to #CC that supplies its own argument to #CC in no more than 50 element chunks. A relaxation of this restriction would apparently result in a smaller clear workspace size, and at 28K for a standard QL this is probably not a good idea. For users with a memory expansion board however, the ability to specify their own #CC size limit at APL load time might be a bonus.

## Keywords and symbols

If there are any controversial aspects of QL/APL, then the choice of keywords and the dual use of the minus sign must be the two main ones. The reasons behind these decisions are documented in David Eastwood’s paper “QL/APL - A new approch to popularizing APL” which appears later in the technical section of this issue of VECTOR. Because QL/APL aims to convert Basic users rather than those who already know APL, the choice for a particular keyword is not based on the APL name for the corresponding symbol. Thus the keyword “size” is used rather than “rho”, which would have little meaning to a non-APLer. Additionally, no name distinction is made between a keyword that represents a monadic or a dyadic function call. So “size” is used both to discover the shape of an array as well as to reshape an array. This is entirely consistent with user-defined functions, where the function name is the same whether we invoke the function monadically or dyadically. This scheme leads to only 47 reserved names, but can be confusing. It is difficult for example, to explain to a non-APL user why it is necessary to type

```
V is rotate W
```

when we actually want to *reverse* the order of elements in W. (Actually this is also a mistake made in speech by even the most experience APLers - it is a subject which can lead to much philosophical speculation about whether symbols or functions are being named). Anyway, as an APLer I found the scheme very easy to use, and rarely had to refer to the manual to look up a keyword, the obvious choice usually being correct.

As far as the choice of symbols goes, most of them are obvious, with +, -, \* and / retaining their meanings as in Basic. The symbol = has no meaning in QL/APL because the keyword “eq” is used instead, to be consistent with the use of keywords for all the other relational functions. The angled brackets &lt; &gt; replace the square brackets [ ] throughout, i.e. in indexing, axis or drive specification and in function editing requests. The function editor is different in other ways too, with the comma replacing the quad character in all display requests. Thus a request to open definition for a function FOO, display it and close the definition becomes

```
defn FOO<,>defn
```

A line can be deleted from a function by issuing, for example

```
<-17>
```

As there is only one type of minus sign in QL/APL, a modification to the syntax analyser was made in order to determine the appropriate meaning according to context. So the sequence space/minus-sign/digit as in

```
X is 3 -2 9
```

indicates the use of minus as a high-minus, or negative marker, whereas its use in subtraction can be seen in

```
      5-8
-3
```

In the expression

```
X-1
```

however, the minus is taken as a negative marker and a syntax error is produced, which is worrying. A minus sign can be forced to mean subtraction by always following it by a space, as in

```
X- 1
```

which works fine. This convention will surely lead to problems when code is transferred between QL/APL and other APLs.

## Performance

This is always a tricky one, because it depends on what you measure. Casually, QL/APL “feels” fast, but how does it compare with other APLs? Well, there are no definitive benchmarks tests that I know of, and those that have been published are usually woefully incomplete - either because they ignore important areas, overemphasise less relevant ones or just fail to test the sort of demands placed on an interpreter in a real application. Anyhow, time seemingly never permits the design of a good set of benches and so we’ll have to make do with what we’ve already got. In this case what we’ve got is a set of benchmarks comparing IBMs APL and APL\*PLUS on the IBM PC, published in BYTE magazine in March 1984. These tests were additionally timed using APL.68000 on a MicroAPL Spectrum and on the QL. The results are summarised in Table 1, with BYTE’s original PC timings left in for comparison. Considering only these benchmarks, QL/APL comes out at about 60% as fast as APL.68000 on a Spectrum and 35% as fast as APL on the PC, although these figures should be taken with a pinch of salt as the tests are by no means exhaustive.

When trying to assess the speed of component filing onto microdrive cartridges, things start to get a little nasty, with the appearance of apparently non-deterministic behaviour. After creating a one thousand element vector of random integers by

```
A is rand 100 size 100
```

the following expression was timed:

```
A fput 1 1
```

After ten trials, the shortest time was 30 seconds and the longest 55 seconds (the first fput), with an average of 36 seconds. Presumably the random position of the read/write head over the tape loop is causing this variation. The time to write the vector to ten successive components on file was 8 minutes when I tried it, with a reduction to 40 seconds when empty vectors were written instead. The time to read the 1000 element vector timed in at a significantly lower 8 seconds over twenty trials. These tests were performed using a newly formatted cartridge, and I have no indications of timings with nearly full cartridges.

*Table 1*

```
                                IBM PC      IBM PC      SPECTRUM     QL
                                ------      ------      --------     --
                     CHIP   :   8088        8088        68000        68008
                     APL    :   IBM APL     APL*PLUS    APL.68000    QL/APL(K)
BENCHMARKS           VERSION:   1.00        2.6         4.10/B       1.03

 1. Z←+/VI                      90         102          26           54
 2. Z←∨/VL                       0.4         3           6           16
 3. Z←⌈/[1]MI                   40          25          20           42
 4. Z←VI*.1                    390         282        4312         6824
 5. Z←|VR                       80          79          87          169
 6. Z←VR[VI[⍳20]]               20          14          23           51
 7. Z←VI[⍒VI]                  600         112         190          325
 8. Z←¯2 1↑MR                    9          24          12           27
 9. Z←VI∊VI                    150         146         217          202
10. Z←2 1⍉MC                   450          60         188          355
11. Z←VC∘.=VC                  360         141         158          363
12. Z←(⍳50)∘.+⍳50             2530         439         241          535
13. Z←VR⌊.+VR                  210         341         192          340
14. Z←MR⌹10↑VR                  70        1488         340          559
15. Z←FIB                     2200        3827        1654         3250
16. Z←VR×3.14                  100         136         229          396
17. Z←VR÷3.14                  110         142         389          541
18. Z←⍟VR                      150         143        2428         3807
19. Z←1○VR×.1                  411         438        3462         4559

Note 1: Each benchmark was run 100 times in succession. The times are in
        milliseconds and are adjusted to represent one execution of the
        given expression (net of looping overhead).

Note 2: The figures for the PC benchmarks were taken directly from the
        March 1984 issue of BYTE, page 248. Since that time two major
        updates to the APL*plus/PC product have been announced, and
        version 4.1 shows significant speed-ups over 2.6 in many areas.

Note 3: The variables used in the benchmarking were created by
        MI←10 10 ⍴VI←(500⍴ 0 1 0 0 1)/⍳500
        VL←1 0 1 1 0 0 0 1
        MR←10 10 ⍴VR←VI+0.1
        MC←26 26 ⍴VC←'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

Note 4: The IBM PC was running with the 8087 maths coprocessor installed
        and enabled. The MicroAPL Spectrum was running in single-user mode.

Table 1: 19 benchmarks for IBM PC APL, APL*plus/PC,
         APL.68000/Spectrum and keyword QL/APL
```

## Behaviour and “feel”

An important part of how popular a new interpreter becomes is its general overall behaviour. QL/APL feels robust and responsive, and would appear to behave itself in most cases. Many of the problems I experienced were a direct result of my own APL knowledge - e.g. it was extremely difficult to remember to use the keyword “on” in place of / for doing compressions. This is particularly unfortunate because the resulting division is often not detected until some time later! Incorrect use of the minus-sign has also plagued me somewhat.

The names of user-defined functions must be chosen to be different from those of the 47 primitives or a defn error will result - a problem if you need to transfer code to a QL from another APL interpreter.

A very frustrating drawback of the version I used was the inability to run Superbasic commands from within APL. In particular, the need to format a microdrive cartridge from APL. This would be wonderfully useful when you’ve just created a workspace only to discover you haven’t enough space left on a formatted cartridge.

An interesting quirk of the system command )OFF is that it clears the active workspace, but leaves you in APL, forcing you to press the RESET button to return to Superbasic (“Surely you don’t really want to leave APL do you?”).

## Some philosophy

The use of keywords (and the space that usually precedes and succeeds them) results in function lines that suddenly become very long, especially if you’re working in 40 columns rather than 80. Although I made the shift to keywords quite easily, I found that program development and debugging became much harder, my productivity certainly being reduced. The code would always be written in symbolic APL and then mentally converted to keyword form on input. (Using a keyboard that feels like you’re typing in cold porridge doesn’t help either). Spotting idioms in keyword APL becomes more difficult; how long would it take you to recognise the following idiom?

```
N is((V index V)eq index size V)on V
```

It may be possible that such idioms take longer to arise in the mind of a keyworder than in that of a symbol person. Alternatively it may be that QL/APL will attract users who are more “wordy” than symbolic and who have none of the problems we might experience as traditional APLers. If QL/APL can be used in a classroom environment, we might even expect to see a higher proportion of “right-brain” people becoming interested, e.g. those with a greater capacity for synthesis and word-skills rather than analysis and symbol-skills. Although many will buy a QL to run APL on, the important step as far as APL is concerned is in convincing people to buy APL for a QL they’ve already got; let’s hope the 100 pound price tag won’t scare them off.

One final word of warning to those who might think that QL/APL will permanently silence APL’s detractors: a friend of mine with no computer knowledge came into the room where I was using keyword QL/APL and remarked, after taking a look at the screen “Well, its all Greek to me”.
