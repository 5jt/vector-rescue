---
title: 'Surely there must be a better way: Ambi-valent Functions'
authors:
- David Ziemann
volume: '3'
issue: '3'
page: '111'
unindexed: true
transcribed: 'from page images of VOL.3-NO.3-JANUARY-1987.pdf, pages 113–116 (printed 111–114; APL Trivia, art10011090, follows on p.115); Claude, 2026-10-05'
review: draft
queries:
- "Checked: DIV1 as printed gives 0.5 0 0 for 1 2 0 DIV1 2 0 0, and 0 1 0.5 for DIV1 0 1 2, as printed."
- "Listings in a monospace face; ⍎ is printed as a glyph like ±, read as ⍎; ∆ printed as a solid triangle. DIV2 [2]’s comment ends “Default <A> is” without the 1, as printed. LARG [6] and LARGDEF [6] are printed `∆1←(∆1⍳'[')↑∆1←,(1,1↓⍴∆1)↑ 1 0 ↓∆1←⎕SI` (↑ read from a glyph like ↑ or ↓)."
- "Slips transcribed as printed: “In the other hand”, “execute,but”, “funtion”, “parenthesese”, “iff its undefined”."
---

by David Ziemann
{ .byline }

If you have an APL solution that you feel could be improved upon, but you just can’t quite see how, then send it in to us. In the other hand, you may have found a new solution to an old problem – why not let other people know about it?

Many APL programmers use interpreters that support ambi-valent functions. An ambi-valent function is one whose valence is not fixed. This usually means that it can be called monadically as well as dyadically. By the way, it’s probably better to pronounce ‘ambi-valent’ with the hyphen in mind; the functions don’t feel opposite emotions simultaneously, but rather they demonstrate one of two different combining powers, or valences.

My feelings toward ambi-valent functions are however, definitely ambivalent. They are often used in a way which is likely to lead to code that is difficult to modify, or even worse, that leads to program bugs. This, however is another story, albeit one which I hope to follow up sometime. For the moment, let us say that they should NOT be used for passing ‘control information’ into a function but rather to allow the function to assume a default left argument. Even this practice is dubious, but. . . .

Anyway, the standard way of testing for the presence or absence of the left argument is by using the ‘name-class’ system function, ⎕NC. This is demonstrated by the function DIV1, a modified version of DIV, which acts as a cover function for the divide primitive, but which gives a zero whenever division by zero occurs, rather than a DOMAIN ERROR. If the left argument is missing then the value 1 is substituted and the result is a reciprocal.

```apl
    ∇ Z←A DIV W
[1]   ⍝ Divide <A> by <W> without DOMAIN ERROR
[2]   ⍝ Zeros in <W> give zeros in <Z>
[3]
[4]    Z←Z×A÷W+~Z←W≠0
    ∇

    ∇ Z←A DIV1 W
[1]   ⍝ Divide <A> by <W> without DOMAIN ERROR
[2]   ⍝ Zeros in <W> give zeros in <Z>. Default <A> is 1
[3]
[4]    →(2=⎕NC 'A')/a
[5]    A←1
[6]
[7]   a:
[8]    Z←Z×A÷W+~Z←W≠0
    ∇

      1 2 0 DIV1 2 0 0
0.5 0 0
      DIV1 0 1 2
0 1 0.5
```

If the name-class of the left argument name is 2 then a left argument value was supplied, otherwise it is 0. If you are using a system that supports an APL statement separator then it is possible to tidy this up slightly by coding:

```apl
    ∇ Z←A DIV2 W
[1]   ⍝ Divide <A> by <W> without DOMAIN ERROR
[2]   ⍝ Zeros in <W> give zeros in <Z>. Default <A> is
[3]
[4]    →(2=⎕NC 'A')/a ⋄ A←1
[5]
[6]   a:
[7]    Z←Z×A÷W+~Z←W≠0
    ∇
```

In both cases however, the code is a bit messy, involving a branch arrow, a system function, a label and a pair of parentheses. The next step is to bury the mess inside another function, so that we don’t have to look at it all the time. The function DEFAULT assigns its right argument value to the name on the left only if it doesn’t already have a value.

```apl
    ∇ Z←A DIV3 W
[1]   ⍝ Divide <A> by <W> without DOMAIN ERROR
[2]   ⍝ Zeros in <W> give zeros in <Z>. Default <A> is 1
[3]
[4]    'A' DEFAULT 1
[5]    Z←Z×A÷W+~Z←W≠0
    ∇

    ∇ ∆1 DEFAULT ∆2
[1]   ⍝ If name in <∆1> is not a variable assign it the value <∆2>
[2]
[3]    ⍎(2≠⎕NC ∆1)/∆1,'←∆2'
    ∇
```

Notice that DEFAULT has to use unusual local names in order to reduce the probability of any of them clashing with the calling function’s left argument name. Admittedly, the function trades a branch and a label for an execute,but it is hidden away in a single function. This is preferable to the practice of littering code with ever more complex expressions of the form

```apl
⍎(2≠⎕NC'LEFT')/'LEFT←FOO 2'
```

Apart from the low readability and maintainability of this kind of thing, the call to function FOO would probably not be detected by cross-reference or other workspace documenting programs. Debugging is made easier too, because DEFAULT can be temporarily modified to include your choice of trace or stop expressions.

The DEFAULT function is useful, but if you are lucky enough to be using an APL which has a ⎕SI system function you can do even better. ⎕SI typically produces a character vector or matrix representation of the SI stack as it would appear if you use the )SI system command. By examining the SI stack it’s possible to determine the name of the calling function, and hence if its left argument name (if any) has a value. The function LARG returns a 1 if its calling function was invoked with a left argument, otherwise a 0 is returned. Because it examines the header line of the calling function’s definition, it does not need to have the variable name passed in as an argument.

```apl
    ∇ Z←A DIV4 W
[1]   ⍝ Divide <A> by <W> without DOMAIN ERROR
[2]   ⍝ Zeros in <W> give zeros in <Z>. Default <A> is 1
[3]
[4]    →LARG/a ⋄ A←1
[5]
[6]   a:
[7]    Z←Z×A÷W+~Z←W≠0
    ∇

    ∇ ∆←LARG;⎕IO;∆1
[1]   ⍝ Return 1 if calling function called with left argument, else 0
[2]
[3]    ⎕IO←0
[4]
[5]   ⍝ Get the name of the calling function
[6]    ∆1←(∆1⍳'[')↑∆1←,(1,1↓⍴∆1)↑ 1 0 ↓∆1←⎕SI
[7]
[8]   ⍝ Quit if there is no calling function or calling function locked
[9]    →(0∊⍴∆1←⎕CRL ∆1,'[0]')/∆←0
[10]
[11]  ⍝ Return 1 if the nameclass of the function's left argument is 2
[12]   ∆←2=⎕NC(-(⌽∆1)⍳'←')↓∆1←(∆1⍳' ')↓∆1
    ∇
```

The system function ⎕CRL is used to return the character representation of the function header line. This is available in APL\*PLUS PC, but users of other systems will have to ⎕CR the whole function and extract the header line by indexing.

The use of LARG is not recommended because it may encourage ‘spaghetti logic’. A better approach is to devolve the assignment of the left argument name into a cover function, as in DEFAULT. In this way the module strength of the function (a system design concept) is not compromised to the same extent. The function LARGDEF (Left ARGument DEFault) implements this idea as follows:

```apl
    ∇ Z←A DIV5 W
[1]   ⍝ Divide <A> by <W> without DOMAIN ERROR
[2]   ⍝ Zeros in <W> give zeros in <Z>. Default <A> is 1
[3]
[4]    LARGDEF 1
[5]    Z←Z×A÷W+~Z←W≠0
    ∇

    ∇ LARGDEF ∆2;⎕IO;∆;∆1
[1]   ⍝ Set calling function left argument to <∆2> iff its undefined
[2]
[3]    ⎕IO←0
[4]
[5]   ⍝ Get the name of the calling function
[6]    ∆1←(∆1⍳'[')↑∆1←,(1,1↓⍴∆1)↑ 1 0 ↓∆1←⎕SI
[7]
[8]   ⍝ End if no calling function or function locked
[9]    →(0∊⍴∆1←⎕CRL ∆1,'[0]')/0
[10]
[11]  ⍝ Get the name of the calling function's left argument
[12]   ∆←(-(⌽∆1)⍳'←')↓∆1←(∆1⍳' ')↓∆1
[13]
[14]  ⍝ Assign value iff calling function's left arg. is undefined
[15]   ⍎(0=⎕NC ∆)/∆,'←∆2'
    ∇
```

Now we have a function which can be safely used to provide a default value for a funtion left argument name, and without the visible use of branching, labels, execute, parenthesese or quote marks. LARGDEF will have no effect if its calling function definition is not dyadic or if the SI stack is clear.

No reference to the name of the left argument is made in the application function, so the approach is less liable to bugs resulting from program modifications. For example, if you later wanted to rename your function left argument, you could do so with less chance of introducing a program bug.

Can you see why the phrase ‘0-equal’ is used rather than ‘2-not-equal’ in the last line of LARGDEF?

Please note that the function DIV has only been used as an example to demonstrate these techniques; utilities like LARGDEF would be more usefully employed in application functions rather than common APL utilities.
