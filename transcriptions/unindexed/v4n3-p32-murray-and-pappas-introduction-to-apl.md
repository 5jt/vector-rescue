---
title: 'Book Review: An Introduction to APL for the IBM PC & XT by William H. Murray and Chris H. Pappas'
authors:
- Anthony Camacho
volume: '4'
issue: '3'
page: '32'
unindexed: true
transcribed: 'from page images of VOL.4-NO.3-JANUARY-1988.pdf, pages 34–38 (printed 32–36); Claude, 2026-10-12'
review: draft
tags:
- reviews
- education
queries:
- "Contents line “An Introduction to APL for the IBM PC & XT by Murray and Pappas”; the printed heading is “Book Review”, with the book’s full title and authors."
- "The function NUMBERGUESS is quoted from the book, which (the review says) was typeset by someone who did not know the APL symbols; the assignment arrows are printed with a trailing dash (“←-”) and the quad as broken brackets. They are given here as ← and ⎕. Line [4] is wrapped in print and is joined here. Kept as printed: the quote in line [26], printed “DIDN\"T” (as a double quote, where APL needs two single quotes); the spaces inside parentheses."
- "Kept as printed: “Price £21:70.”; “Their example of high minus 359 minus high minus 57”; “Rounding is explained as the floor of 0.555 +” (the reviewer’s point); the underlining of “after” in the F6 quotation and in the reviewer’s comment is given as italics."
---

## Book Review

### An Introduction to APL for the IBM PC & XT by William H. Murray and Chris H. Pappas,

> Paperback, 167pp text plus 50pp appendices index etc<br>
> Published by Brady Communications Co,<br>
> Price £21:70.

*Reviewed by Anthony Camacho*
{ .byline }

I believe this is a very bad book. In fairness I should add that not everyone will agree with my opinion and if you don't I hope you will be able to tell from what I write whether you would like it better than I do. The rest of this review is devoted to a description of the book and justification of my opinion.

The authors try to cover two popular APLs for the PC XT (& AT); STSC's APL\*PLUS/PC and IBM's APL/PC. There is no mention of Sharp APL or PortaAPL.

They begin by relegating the set up of the machine to the appendix. The fourth paragraph of the introduction reads: "If you do not desire to install the keyboard labels, or if you plan to move your APL from one computer to another, you will need the keyboard overlay provided with this book. Carefully remove the overlay, prepare it according to the directions and place it over your keyboard." - there are no directions; the "overlay" is a cardboard sheet with a sort of perspective drawing of the IBM keyboard on one side and the STSC keyboard on the other; the keys are not marked consistently and some of the markings are wrong. Iota is marked as a mirror image "S"!

The chapters are:

> 1 - Instant APL<br>
> 2 - Simple APL programming<br>
> 3 - Edit, print & file<br>
> 4 - Introduction to function writing and workspaces<br>
> 5 - System functions, variables and special features<br>
> 6 - Workspaces and libraries<br>
> 7 - Making music<br>
> 8 - Creative graphics in IBM & STSC APL<br>
> 9 - Towards more advanced APL programming<br>
> A - Installing the APL system<br>
> B - Optional diskette package<br>
> C - Graphics with STSC's PocketAPL<br>
> D - Using the Microsoft mouse with APL<br>
> Index

As you can see from this list, chapters 1-6 are about the basics of APL in STSC's and IBM's implementations and chapters 7 & 8 are a bit of time off to play with sound and graphics. The chapter on sound tries also to be a music primer and includes MARYSLAMB and FURELISE. The chapter on graphics puts the words "Graphics is Great" in a box and draws a sine wave (misprinted by rotating it 30 degrees) and a synthesised square wave. Chapter 9 has a subtitle "Additional examples" and contains examples of encode, decode, matrix division and the equals outer product. It also contains a very elementary telephone directory function of over a hundred lines.

Now you know what's in the book I will deal with some niggles and then with my major objections.

### Niggles

#### 1. Typesetting

The book is wholly set by a professional typesetter who doesn't understand what shapes the APL symbols are. He matches them as well as he can from his stock of standard symbols, so the quad is square, the circle is much too big, log is printed as circle overstruck with multiply and there is no consistency in the size of jot in lamp, execute, format or on its own (when it is sometimes printed as a degree). In short the typesetting is bad.

#### 2. Proofreading

In several places the instructions to the typesetters have been set and left in the text (eg"do not wrap function lines"). In many places a matrix result is split between two pages. On page 75 a line of BASIC which was intended to set Y to the cube of I is typeset as I and 3. Rounding is explained as the floor of 0.555 + (I do hope this is a proofreading error!). On page 5 the text has 18 percent when the function has .015. A vital branch arrow is omitted on page 49. A good many of these and other errors make nonsense of the text. Perhaps a learner would not be able to puzzle them out.

#### 3. Incomplete explanations

Many explanations are ambiguous or incomplete or fail to make the point. Their example of high minus 359 minus high minus 57 would give the same result with two subtractions. The paragraphs on monadic domino only cover square matrices and in my view fail to explain them. Incidentally the only conditional branch I could find in the examples was of the form 'branch to label times iota result of test': there is no explanation that label is assigned the value of its line count on opening the function and that the iota ensures that (in index origin one) multiplication will be by one or the empty vector; nor do they explain the effect of index origin zero on this construct. Nowhere could I find the essential part of the explanation: that a branch to the empty vector is parsed as 'branch to nowhere; ie don't branch'.

### Serious Weaknesses

The two serious weaknesses are that the authors do not use words carefully enough and that the book sets a bad example.

First the words:

> "You will soon discover that many of the APL symbols have both a dyadic and monadic use of operation."

> "Since our right argument will have two dimensions our left argument must also have two dimensions."

(This is about take and drop! It continues: "You will use a two element vector.") Notice the slide from "our left argument" to "You will use". The point of view from which the book is written changes unpredictably. Some function keys "Move you to . . " some "Allow you to . . " some "Enable you to . . ".

"F6 Allows you to copy a line. First you move the cursor to the line you want copied and press F&. Be patient. Many of the F(n) commands take several seconds to perform their operations. After several seconds, if you look very carefully at the bottom of your screen, you will see that the 6:COP command prompt has changed to 6:COP\*. This is to indicate that the copy option has been turned on. Next move the cursor to the line *after* the line that is to be copied and press F6 a second time. Again after several seconds the, 6:COP\*, command prompt will return to its original state, 6:COP, and finally the line will be copied."

(sic Explanation of F6 in IBM editing). I think they mean "*after* the place where you want the line copied to . . "

"<Ctrl-A> Allows you to alter the structure of the object you are defining, or editing. In our example above, the bottom line of the screen should now look like this: Editing: FIBONACCI[V]6 The V inside [] indicates that you are defining a vector. Press <Ctrl-A>. You will notice that at the bottom of the screen there is now a prompt asking you to define the definition of this object. Now press the letter F for function. Immediately you return to the original screen and if you notice, the bottom of the screen has changed to: Editing: FIBONACCI[F]6 <Ctrl-A> allows you to define a (F)unction, (M)atrix, or a (V)ector."

(sic From the explanation of STSC editing).

Second the examples:

Here is part of the introduction to the function TELEPHONE (IBM version 105 lines; STSC version 101 lines):

"True believers in APL would probably have preferred that we broke this large function down into several smaller, independent functions. We could have done that - and would have done that - except that we felt some clarity might have been lost in having to look at numerous functions."

One wonders how they come to think that a 100 line function is clearer than ten 10 line functions. These functions are just like BASIC with branches to labels (like GETIT or TOHERE) at the head of subroutines.

Here is a final example - the function NUMBERGUESS from halfway through the book.

```apl
[0]  NUMBERGUESS
[1]   ⎕IO←1
[2]   MYSCORE←0
[3]   COMPSCORE←0
[4]  AGAIN:'I WILL PICK A NUMBER FROM 0 TO 10   YOU HAVE THREE GUESSES.'
[5]   NUMBER←(?11) - 1
[6]   'ENTER YOUR FIRST GUESS'
[7]   MYGUESS←⎕
[8]   →HWIN × ⍳(NUMBER = MYGUESS )
[9]   'ENTER YOUR SECOND GUESS'
[10]  MYGUESS←⎕
[11]  →MWIN × ⍳(NUMBER = MYGUESS )
[12]  'ENTER YOUR THIRD GUESS'
[13]  MYGUESS←⎕
[14]  →LWIN × ⍳(NUMBER = MYGUESS )
[15]  COMPSCORE←COMPSCORE + 10
[16]  →SORRY
[17] HWIN:MYSCORE←MYSCORE + 10
[18]  →REPORT
[19] MWIN:MYSCORE←MYSCORE + 7
[20]  COMPSCORE←COMPSCORE + 3
[21]  →REPORT
[22] LWIN:MYSCORE←MYSCORE + 3
[23]  COMPSCORE←COMPSCORE + 7
[24] REPORT:'YOU GOT IT (',(⍕NUMBER ),') -- THE SCORE IS:'
[25]  →SCORE
[26] SORRY:'YOU DIDN"T GUESS IT, IT WAS ',⍕NUMBER
[27] SCORE:'YOU: ',(⍕MYSCORE ),'      COMPUTER : ',(⍕COMPSCORE )
[28]  ' '
[29]  ' '
[30]  →AGAIN
```

In short, apart from the niggles, what is wrong with this book is that it sees APL purely as a programming language similar to BASIC with a few minor differences such as array variables, yet it fails to give any idea of APL's power and range in that role.

If your view is that APL is a commercial programming language and you bought a commercial interpreter for your PC then you will want to use it for a better class of work than you get here: this half-baked introduction is no way to begin down that road.

If you agree with me that APL should be seen primarily as a notation (in my view that leads to better programs too) then the failure of this book to provide the fundamental groundwork or to cover the behaviour of functions with unexpected (eg empty) arguments, disqualifies it. Paul Berry and Gilman and Rose still rule - OK?
