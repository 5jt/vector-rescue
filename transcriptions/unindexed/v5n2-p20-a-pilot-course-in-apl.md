---
title: A Pilot Course in APL
authors:
- Bruce Dickson
volume: '5'
issue: '2'
page: '20'
unindexed: true
transcribed: 'from page images of VOL.5-NO.2-NOVEMBER-1988.pdf, pages 22–24 (printed 20–22); Claude, 2026-10-12'
review: draft
tags:
- education
queries:
- "The Contents page gives page 24; the worksheet begins on printed 20 under the heading “An APL Pilot Course”, directly after Bruce Dickson’s note “APL at Mill Hill School” (unindexed/v5n2-p20-apl-at-mill-hill-school.md), and ends on printed 22. The Contents line’s page is corrected to 20. No byline is printed with the worksheet; the author is Dickson’s, from his note."
- "In the typewriter font of the examples the digit 1 sometimes prints like a capital I (“PAGE+I00”, “ρI 4 8 ρ100 100”, “5 I2ρLIST2”); transcribed as 1. Iota prints as a small ι-like glyph and is transcribed ⍳; the left arrow prints like + and is transcribed ←, as the text calls it “The left arrow”."
- "“ρ⍳10 ρ1000 2 ρ⍳100 ρ1 4 8 ρ100 100 ρ⍳53” is printed run into the sentence; the spacing between the expressions is kept approximately."
- "Kept as printed: “programmer!.”; “PAGE-100” printed with a hyphen-like minus."
---

## An APL Pilot Course

Put in the APL disc and call up APL with the command \*APL. The message CLEAR WS tells us that there is an empty workspace that can be filled with functions and variables.

Check that the Caps Lock light is on. Then hold SHIFT and touch 'I'; the squiggle is called iota; it affects the single number that follows it. Enter `⍳100` and `⍳1000` and any other values you care to try.

Holding SHIFT and pressing 'R' produces the greek letter `ρ`. It can be used to find how many numbers there are in a list of numbers like the ones you have just created. Try this with: `ρ⍳10`   `ρ1000 2 ρ⍳100`   `ρ1 4 8 ρ100 100`   `ρ⍳53`.

These APL commands give quick results that are printed on the next line. Some results do not fit onto one line: try

```apl
2 5ρ10      (THE 2 5 RESHAPE OF 10)
2 5ρ⍳10     (THE 2 5 RESHAPE OF IOTA 10)
20 1ρ⍳20    (THE 20 1 RESHAPE OF IOTA 20)
```

To save typing time, parts of commands can be copied with the COPY and arrow keys; the whole of the last command can be repeated by using the right bracket ')'.

Now try `2 5 8ρ⍳50 4 5 8ρ⍳100`

Note that if reshape runs out of information to use, it just starts at the beginning again as often as necessary to fill the pattern.

Try `2 3 4 20ρ⍳480`

You must be sick of `ρ` by now.

The left arrow `←` is called "gets". Print it with SHIFT 'P' Now enter ...

```apl
PAGE2←3 4 20ρ⍳480
```

Nothing happens until you enter PAGE again. Try typing PAGE and the following commands:

```apl
PAGE+2
PAGE+100
PAGE-100
```

(Note the high minus used to display negative numbers.)

```apl
PAGE1←PAGE+5
PAGE2←PAGE-5
PAGE1+PAGE2
ρPAGE
20 18ρPAGE
ρ20 18ρPAGE      (THE SHAPE OF THE 20 18 RESHAPE OF PAGE).
```

### Exercise

Experiment with different numbers all through this course. If you have stuck with us so far, you will make a good APL programmer!. All that it takes is the familiarity that comes with practice.

### A First Database

Make a list of five surnames and enter them as:

```apl
LIST1←'SMITH JACKSON DICKSON DUCKWORTH GRAHAM'
```

Check with LIST1 that the spelling is O.K. Improve it to LIST2 by putting enough spaces in between the names so that there are 12 characters for each name, i.e. 'SMITH' must have 7 spaces before 'JACKSON' starts, which is then followed by 5 spaces and so on.

Now try

```apl
5 12ρLIST2 (THE 5 12 RESHAPE OF LIST2)
```

If all is well, you should get

```apl
SMITH
JACKSON
DICKSON
DUCKWORTH
GRAHAM
```

against the left margin. If not, make LIST2 again counting spaces carefully.

Make this into LIST3 with

```apl
LIST3←5 12ρLIST2
```

The expression `5 1ρ⍳5` makes a column of numbers from 1 to 5. Before we can make a numbered list, we have to change this column of numbers to a column of characters. This is done with the 'format' symbol '`⍕`' obtained using SHIFT and 'H'. Type in

```apl
(⍕5 1ρ⍳5),LIST3
```

To put spaces between the numbers and names, enter

```apl
LIST4←(⍕5 1ρ⍳5),' ',LIST3
```

and check that all is well again by typing LIST4.

Finally try `,LIST4` . The comma unravels the table (matrix) of characters.

### Exercises

1. Change SMITH in LIST4 to your surname. Hint: use ,LIST4, change it, call it LIST5 and then reshape it with `LIST6←5 12ρLIST5`
2. Make a new numbered list with at least three of your friends' names.
3. (More difficult) Can you make a numbered list of your friends' surnames and first names in three columns?

N.B. To see what lists we have made so far in this workspace, enter )VARS.
