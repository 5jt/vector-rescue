---
title: 'Technical Correspondence (Sullivan; Piper; Hayward; Bykerk; Donnelly; Prys-Williams)'
volume: '4'
issue: '4'
page: '92'
unindexed: true
transcribed: 'from page images of VOL.4-NO.4-APRIL-1988.pdf, pages 94–104 (printed 92–102); Claude, 2026-10-06'
review: draft
queries:
- "Several letters under one heading; writers’ addresses kept as printed."
- "Sullivan’s GETSCR is printed `GETSCR: GETSCR ω,⎕AV[⎕IO],V : 0=⍴V←⍞ : ω`; the input glyph after V← is read as ⍞ (quote-quad), as screen input requires."
- "Bykerk’s idiom is printed `(1=+/R∧.=⍉R)/R` in a crude font; read with ⌿ (rows). It keeps only rows that occur once, as Branson’s del-all-dupes does (v4n2-p93)."
- "Donnelly’s numbered points skip 8 (7 is followed by 9); transcribed as printed."
- "Slips transcribed as printed: “out editor”, “swear by at”, “be please to know”, “mullarkey”, “conpliance”, “occurences”, “coul be published”."
---

## Direct Definition

<p>From: John Sullivan<span style="float: right">16th Feb 1988</span></p>

Direct definition seems to me an admirable vehicle for displaying algorithms in APL (which may be why conference papers use it so much), but as everybody who has ever written an application knows, applications contain far more than just algorithms. For instance, any function that operates on supplied data should contain all of the following three items:

1. Documentation (comments)
2. Data validation
3. Algorithm

and unless some convoluted logic is used it is pretty difficult to fit data validation and the algorithm into a one-line function. Add to this the need to keep function lines short (everybody in the BAA is exhorting me to do this these days!) and you are in trouble. And if you can’t see the need for data validation, try executing FACTORIAL 2.5 using the function on p.100 of Vol 4 No 3. You cannot assume that the users are going to get the data right every time, and so you have to provide coding to deal with data errors.

Anthony Camacho’s MAT (Vol 4 No 3 p.100) provides a good example of direct definition used to excess. This function is really only a utility, yet it consists of five directly-defined functions, some of which seem to do excess work for no good reason (see below for my version of MAT). Multiply that by the number of other functions you need to get even a simple application working (even if you can use some of the ‘subroutines’ more than once) and you will easily get 200 or more functions in your workspace. I well remember the reaction from the audience at the Royal Over-Seas League when the slide displayed on p.62 of Vol 4 No 3 was shown. It seems to me that we are being told to do two conflicting things here: reduce the number of names in the workspace in order to make maintenance etc. easy; and increase the number of names in the workspace for the sake of using direct definition.

I’m sure most of our members have workspaces of utilities, mainly because most APLers come packaged with at least one. As an example of these utilities look at Vol 3 No 4 pp.127-8 [1]. Would anybody even consider converting these to direct definition (or using direct definition for them in the first place)? I wouldn’t: I’ve got too much work to do. Having said that, I’m sure there are occasions where a good set of directly-defined functions could come in handy: for example, a suite of data-verification functions on the lines of those shown at APL86 by Alan Graham.

All of this direct definition mullarkey reminds me of an article I read some years ago [2] which attempted to give the reader an introduction to LISP. I know that some people are trying to write AI applications in APL, but that is no reason for writing APL in the style of LISP.

As for writing MAT in an elegant way, here is my four penn’orth.

1. Get the right algorithm. Repeated screen input needs a (expletive-deleted) loop, but you shouldn’t do ANY processing inside the loop.
2. You’ve got a workspace of utilities, so use them. The utility for converting a segmented string (delimited vector) into a matrix is so well known it needs no introduction. It comes in a variety of flavours, and the one I am using here (ROWNAMES) appears in the standard APL ‘textbook’[3]. This function has a left argument that defines the rowlength of the final matrix (use the null vector for a default), which can be used to make MAT monadic.

This example uses direct definition as far as it goes because that is the reason for its existence.

```apl
MAT:     ω ROWNAMES GETSCR ''
GETSCR:  GETSCR ω,⎕AV[⎕IO],V : 0=⍴V←⍞ : ω
```

Again, this suffers from the lack of a data validation routine (try MAT 2.5) but this could be overcome by making MAT pseudo-niladic and replacing ω by (⍳0). More elegant than Anthony’s code? Maybe, but in a production environment who cares about elegance? This code is ‘better’ than Anthony’s because it removes all but the barest essentials from the loop (recursion is looping with the mechanism changed to confuse the innocent!), but it’s probably not the best that could be written. The question remains, is it worth it? Why waste half a week being ever-so-clever when you can get the results in half an hour using other methods?

To sum up: direct definition is a useful addition to the tools of the APL programmer, but it is not the be-all-and-end-all. An excessive desire to see everything coded via direct definition can lead to a waste of time and effort.

### References

1. David Piper, ‘Using Name Association for Data Transfer’, VECTOR Vol 3 No 4.
2. Douglas Hofstadter, ‘Metamagical Themas’, Scientific American Vol 248 No 2 (February 1983) p.14.
3. Leonard Gilman & Allen J Rose ‘APL, an Interactive Approach’, John Wiley & Sons, 3rd. edition, 1984.

Yours faithfully,

<p style="margin-left: 2em">John Sullivan<br>Research Manager, IT Systems &amp; Library Support<br>Market Intelligence Dept, Business Development Div.<br>National Westminster Bank<br>LONDON EC3V 3NN</p>

## APL 88 Code Quality

<p>From: David Piper<span style="float: right">15 March 1988</span></p>

I have just been reading the proceedings of the APL88 conference and have been made extremely angry at the quality of some of the published code. In today’s systems development environment, when conpliance to standards and quality of code is given the highest priority, how can the APL community ever hope to be taken seriously when it publishes such appalling code examples?

Superficially it is reasonable to argue that there are no standards in the APL world; there are, however, widely agreed guidelines for writing APL. The following are just a few that are broken:

<p style="margin-left: 2em">- Widespread use of global variables<br>- Use of execute (even worse with ‘IF’)<br>- Pepper-wise use of EACH<br>- Non-use of arguments and explicit results<br>- Lack of comments (especially descriptive comments)<br>- Gluing of lines of code</p>

The scale of these violations is indicated by the following example, analysing the code of a single operator:

<p style="margin-left: 2em">- 10 uses of execute (6 with ‘IF’)<br>- 2 occurrences of output suppression, using</p>

```apl
→0⍴expression
```

<p style="margin-left: 2em">- 4 occurences of line gluing by strand notation, using</p>

```apl
→0 expression
```

<p style="margin-left: 2em">- 2 global variables</p>

Or again, in a single function:

<p style="margin-left: 2em">- 20 lines of code<br>- 13 global variables set<br>- 38 uses of each (up to 12 in a line, 4 together)<br>- No arguments<br>- No explicit result</p>

Two major problems arise from the publication of such bad code. Firstly, the perception of APL as a ‘gauche’ language is perpetuated amongst those on the fringes of the APL community who perhaps disapprove of it anyway. Secondly, and I believe more importantly, it encourages new users of APL to adopt the same habits, thinking them to be acceptable practices.

As a solution, I would like to suggest that papers submitted for publication in journals and at conferences are scrutinised more closely, with equal weight (or even more weight) being given to the quality of the code and the content. In order to make the authors work easier, a set of general coding guidelines coul be published. This would allow the assessment of code to be automated, papers violating the acceptable metrics being rejected. Even more helpful would be a report sent to each author (even of accepted papers) showing bad points in their code.

I would like to stress that not all was bad in the APL88 proceedings. Many of the papers and much of the code was of a high standard. Some even presented hope for a more professional APL methodology. Notable here was the paper by Bob Bykerk describing the development toolbox developed for use within the ECC.

In future, let’s have more of the high quality code and less (preferably none) of the bad.

Yours faithfully,

<p style="margin-left: 2em">D.B.Piper<br>41, Sandown Drive<br>Rainham<br>Kent ME8 9DT.</p>

## In Defense of Dyalog

<p>From: Iain Hayward<span style="float: right">31st March 1988</span></p>

Concerning your review of Dyalog APL on the IBM 6150 in VECTOR 4.2, I feel it necessary to put the record straight for the benefit of prospective users of Dyalog APL, if not just out of fairness to the suppliers.

My attention was first drawn to this article by an indignant colleague who took exception to your description of the ‘vi’ editor. Now, I wouldn’t argue with that because you were expressing an opinion based on limited experience of Unix, however further reading did provoke me.

Firstly, you complained about the excess of system functions – how can you say that! It seems to me that Dyadic have kept these to a minimum, preferring instead to allow you to make your own, either by executing a Unix command from within APL, or else by writing an auxiliary processor (just how much time it takes to write an AP is another story). If you had taken the trouble to get to know the ones that they have supplied you might have realised how valuable they are. For example have you thought how useful the ⎕NR (nested representation) would be when writing a documentation system? As for ⎕VR, it was the first function I had to write when I took delivery of MicroAPL’s APL.68000, just to be able to produce a satisfactory listing of functions on the printer.

Secondly, you complain that the ‘external variables’ facility only serves to clutter the documentation, and imply that the conventional component file system is quite adequate. I for one think that the conventional component file system is the pits! Dyalog APL lets you use real files, ones which other systems can read and write to. Overall Dyalog APL’s facilities for transferring data to and from the outside world are superb and unparalleled. APL will never be widely accepted without this capability.

The impression I get is that you didn’t have time to get to know this product and that you reacted in the way that many a beginner does when faced with a new, large, and complicated system – complain that it is too different and criticize the manual.

Yours faithfully

<p style="margin-left: 2em">Iain Hayward<br>9 rue de Clairefontaine<br>1341 Luxembourg<br>Grand Duchy of Luxembourg</p>

## In defence of VIA …

<p>From: Bob Bykerk<span style="float: right">30th March 1988</span></p>

Dear Sir,

Referring to Dr Peter Branson’s letter in VECTOR 4.2; to remove all the duplicated rows from a matrix, he should try the following:

```apl
(1=+/R∧.=⍉R)⌿R
```

Adrian Smith’s review of Dyalog APL was interesting, but I think it is unfair to print scathing criticism of a feature of a product that the author admits to having little experience with (i.e. the VIA editor).

I suggest that he takes a little more time to learn a product before he criticizes it. There is one thing that can be stated: the VIA editor is a different approach to editing, and can be AT FIRST difficult to master, especially after using other editors such as )XEDIT, SPF and ⎕EDIT. However, after the short initial learning time, this editor can be very powerful indeed, and certainly becomes intuitive. It is only a shame that there are not more features of the Unix ‘vi’ editor available.

Yours sincerely

<p style="margin-left: 2em">Bob Bykerk<br>55, Rue Charles Arendt<br>Luxembourg</p>

**Editor’s note:**

sorry via! It bit me rather badly, to the tune of around 15 minutes lost work, quite early on. I’m afraid I never forgave it sufficiently to have a really serious go. In fact with the Dyalog session manager ∇ is really quite adequate, much more so than on most other systems.

I stand by my comment that you don’t need three different ways to convert functions to characters. If you have ⎕CR you can easily program ⎕VR and ⎕NR and so on! APL used to be all about orthogonality; it upsets me to see such a high degree of overlap between supplied functions.

Maybe I’m just getting old and crabby! Maybe I’m just upset that no-one will give me a Unix box to play with? Please keep the letters coming – anything except direct abuse gets published, honest.

## From Dyadic Systems …

<p>From: Peter Donnelly<span style="float: right">11th April 1988</span></p>

Thank you for your interesting review of Dyalog APL in VECTOR 4.2. I would like to make one or two comments about the article, which your readers might find informative.

1. Dyadic chose Unix because it offered portability, speed, multi-user support and unlimited memory. Just the things for an effective APL environment. I agree with you that there is resistance to Unix, but there is always resistance to change, particularly when so many vested interests are involved. Today, <u>virtually all</u> of the major hardware developments in computing (RISC, parallel architecture, vector-processors) are Unix based. In my opinion, DP managers who choose to ignore Unix are paying through the nose for their MIPS!

    Yes, DEC may continue to ‘lock users in’ with VMS, but Hewlett-Packard, NCR and Unisys are firmly committed to Unix, as is IBM. IBM recently claimed that it spends as much time on its Unix product AIX, as on any other of its operating systems, and underlined its long-term Unix strategy with the announcement of the ‘AIX Family Definition’ in parallel with SAA.

2. You certainly don’t like out editor, do you! Rightly or wrongly, Dyadic decided to emulate the standard Unix editor ‘vi’. This has the advantage that users only have to learn one set of editor commands; not one set for APL and another for the rest of the system. I agree that ‘vi’ can be difficult at first, but like many other powerful tools (e.g. APL?) it more than repays the effort of learning. Lots of our users swear by at.

3. We too can provide instantaneous screen response. Dyalog APL/386 on an IBM PS/2 Model-80 or a Compaq-386 is every bit as fast as APL\*PLUS/PC in terms of screen handling. The particular screens you used in your evaluation are also instantaneous when used in full-screen or graphics mode. They are however comparatively slow at scrolling. I expect that this was your problem.

4. I have to disagree with you about the error trapping. Having used many different versions of APL I am convinced that Dyalog APL’s error trapping is more powerful and easier to use than any other I have encountered.

    For example `⎕TRAP←9 'E' '→ERR'`

    means that if a DOMAIN ERROR occurs in my function, the program will branch to ERR. Surely that’s simple enough!

    If I say `⎕TRAP←0 'C' '→ERR'`

    it means that if any error occurs in a function called by this one, the stack will be ‘cut back’ automatically to here before executing the branch.

    Using these two cases in combination, you can quite simply set up very comprehensive error handling, without having to resort to complex lexical analysis of ⎕DM.

    Dyalog APL also has ⎕SIGNAL, which is very similar to ⎕ERROR, but that’s all that’s needed for error-handling. There is no heap of obscure ⎕FNS.

5. We introduced ⎕NR because a vector of text vectors is so much easier to handle than either a matrix or a line-list. We retained ⎕CR and ⎕VR for compatibility with the ISO standard, and with other APLs.

6. Really Adrian, there are only 54 system functions, variables and constants in Dyalog APL (including 20 for the component file system) compared with 144 (a gross) in APL\*PLUS/PC. I don’t think it is Dyadic who should be accused of taking the ⎕KITCHENSINK approach!

7. Yes, you’re partly right about modified assignment. Everyone who uses Dyalog APL (including myself) falls over the same thing, i.e. that the ‘pass through’ values of modified assignment is the thing on the right, not the result of the assignment. The problem is that what is theoretically correct is (initially at least) intuitively wrong. Incidentally, we were not the first to implement this feature; Burroughs APL had it too.

9. You will be please to know that since your evaluation, we have enhanced our graphics APs to take full advantage of nested arrays. Basically, the output functions now accept nested arguments so you can draw more than one object at a time. This means that you can avoid writing loops, so your graphics applications run faster. The most complex of the demo charts you tried is now calculated and displayed in under 3 seconds.

10. I am glad you liked our interface to Oracle. This seems to be very popular with users. As you noted, you can improve on the standard database management facilities by writing your own tools in APL. Several of our users have already done so, and one customer has even built a fully relational IC1 look-alike.
{ start="9" }

Finally, a note on performance. The IBM 6150 Model 20 you were using was superseded last year by the model 125. This is 2 - 4 times faster than the old model, and outperforms the Sun 3/140.

Yours sincerely

<p style="margin-left: 2em">Peter Donnelly<br>Operations Manager, Dyadic Systems Ltd<br>Park House, The High Street,<br>Alton, Hampshire GU34 1EN</p>

## Dyalog APL on the IBM 6151: A Reply

<p>From: Allan Prys-Williams<span style="float: right">8th April 1988</span></p>

As someone who has been using this system in workstation mode for eighteen months now, perhaps I could be allowed to expand on Adrian Smith’s review in Vector 4.2. Obviously, my view is coloured by my coming to this system from mainframe rather than PC use, but I thought that his review was unfairly critical in some ways, while missing one or two actual problems.

### Unix

Obviously, any system that gives real flexibility to the user is going to frighten DP managers, but the AIX implementation is already based on a hierarchy of users.

- The superuser can do anything, but no-one logs in as superuser except for specific purposes. It is too dangerous even for the administrator to use routinely.
- The system group can do many things that are fairly dangerous, such as altering the status of printers. On my system, I normally work within this group. On a DP-manager-friendly system, most commands would be moved to have this restriction, and only the managers would belong to it.
- Ordinary users only need a very small set of commands, especially if their profile causes them to wake up in APL. On my system I have a ‘demo’ user configured so that colleagues can try things out without causing any damage.

I have to say that every time I find myself on e.g. a DEC mainframe I can’t wait to get back to UNIX. Only, don’t let yourself get posted as the superuser of any UNIX system that doesn’t have explicit superuser’s manuals. UNIX provides a friendly environment for ordinary users by loading all the awkward bits onto the superuser, which can be terrifying. The IBM6150/1 has good manuals, but the Cadmus I was on before had not.

### Editors

The ‘vi’ editor is pretty horrible, but the really good full-screen editor and file manager provided within AIX – ‘INed’ – is not compatible with APL as it uses the ‘alt’ key to control editing functions. Indeed, if you start this up after running APL from the console, it won’t work at all. In practice, I have found that using the full-screen cut and paste functions in the session manager, combined with the del-editor, is excellent for generating new functions, as you can test code in bits and then capture it into the function. Vi works rather well for documenting things and going through changing names of variables and things like that, so one ends up using both. Many of the session-managing keys work within vi, though the manual omits to say so. At least I have been able to give up using things like ‘///4 A’ and other del-incantations.

### The APL

External variables are marvellous. Of course, they are only high-class component files (as you find out if the system goes down at the wrong moment) but they have the tremendous virtue of transparency. For database work, I can develop the system using just basic APL and then convert any variables that are going to be changing, into external variables of the same name. These are then sharable; backed up independently; enable me to keep the workspace absolutely fixed; and I don’t need to know where (exactly) everything is. It is also, in emergency, trivial to bring them back into the workspace as standard variables (a single left-arrow does it) when they can be hacked around ad. lib.

The ⎕KITCHENSINK comment is really an attack on the documentation. The different ways of representing a function all do non-trivially different things, but you have to work out the crucial differences for yourself. Personally, I find that the presence of minority-interest goodies makes it much easier to get help from Dyadic over the phone at the practically important level of things like interfacing with Unix files or printers.

### Windows

In workstation mode, it is practical to have separate full-screen windows open on several different jobs (the operating system for when something goes wrong; the APL under development; the editor for writing it up; a routine data-handling job that has to be done at the same time) and flip between them. This makes it practical to document what you are doing as you do it, instead of as an afterthought. Not only does this save a lot of hassle near deadlines, but you get new insights by trying to explain to an unknown reader what you are up to, and then just flip back to the APL window to try them out. The INed editor allows windows into 3 or 4 files at once with text capture from one to another.

Conversely, it is most desirable to run APL in a window, not the main screen, so that you haven’t disabled the alt-keys when you run your next Unix application. You can even run APL inside the mouse-driven Usability Services shell, though I find point-and-grunt systems dreadfully slow.

Personally, I have only noticed delayed response when the machine is definitely busy elsewhere (multi-tasking plus a virtual system means that you can run monstrous background jobs while thinking what to do next). This is a function of a single chip doing many jobs, and as the 386 machines come in even PC users are going to have to get used to it. Certainly the Prefect full-screen I/O utilities run with exemplary efficiency, with the only delays being caused by heavy data-crunching.

### But…

There are quite a few I/O problems. While direct communication with the Proprinter is exemplary for sending character arrays, capturing APL session output is hairy. If you split the output to a monitor file (the standard Unix technique) the result doesn’t have carriage returns at the end of lines and tends to print continuously across the page. Personally I use monitored material inside files sent to the ‘mm’ word-processing package, which gives full pagination and scope to comment, as well as eliminating unprintable characters and adding CRs, but this is the sort of elaboration that gets Unix buffs a bad name.

Similarly, the console doesn’t act as an APL terminal at all. If you view a file with APL characters, they aren’t translated. So if you have a monitor file going, all you get is ASCII on the screen and no session-manager. A terminal emulator is supposed to be on the way, but it will be just my luck if it works splendidly with the VT100 emulator, but not with basic paging through a file.

### Summing Up

My unimproved workstation is vastly better than the University’s new Pyramid mainframe with umpteen MIPS (and no slower, in real life) and I will fight anybody to keep it, but some of its idiosyncrasies seem to demand a dedicated user. However, this also applies to every PC I’ve ever observed.

<p style="margin-left: 2em">Allan Prys-Williams<br><br>Department of Management Science and Statistics<br>University of Wales<br>Swansea.</p>
