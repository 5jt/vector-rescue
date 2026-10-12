---
title: IBM’s APL2.5 for the RS/6000 and Microwriter AgendA
authors:
- Adrian Smith
volume: '6'
issue: '4'
page: '58'
unindexed: true
transcribed: 'from page images of VOL.6-NO.4-APRIL-1990.pdf, pages 60–61 (printed 58–59); Claude, 2026-10-12'
review: draft
tags:
- humour
- reviews
queries:
- "Contents line “APL2.5 for the Microwriter AgendA”; the printed heading is “IBM's APL2.5 for the RS/6000 and Microwriter AgendA”, “reviewed by Adrian Smith”. An April Fool: the product is fictitious (released “1st April”, “UK and Rockall only”, contact “I. Phelfritt”); the contact address and telephone are those of APL-385 in the issue’s Product Guide."
- "In the examples on printed 59, the input line `2 PLUS (2 4)[1.2]` is printed without the usual six-space indent; kept as printed. The examples describe fictitious behaviour and were not run."
---

*reviewed by Adrian Smith*
{ .byline }

## Technical Breakthrough

One of the major advantages of generating your APL systems using a high level Intermediate Language (IL) is that you can quickly port your interpreter across a wide variety of operating systems. This technology was first exploited in 1979 with an APL for the IBM System-7 minicomputer, and has subsequently been applied to good effect by Dave Selby and Manuel Alfonseca in shipping APL2/PC in both 16-bit and 32-bit versions.

IBM have exploited the same technique in their April announcement of APL2.5 simultaneously across two widely differing platforms: the top-end RS/6000 workstation (maximum workspace 3.7 Gbyte) and the Microwriter AgendA. It is also fascinating to see the use of Display PostScript exploited for an APL development environment which looks remarkably like Presentation Manager. Again, the device-independence is fully exploited in providing similar facilities on the ultra-high resolution workstation monitor, and the 4x20 character LCD display of the Microwriter.

## New Features of APL2.5

As its name implies, a major enhancement of APL2.5 is Array Interpolation. Just as you can join arrays on intermediate axes with Laminate, you can now index arrays and vectors between existing elements:

```apl
      MAT←(⍳12),[1.5] 12⍴1 2 3      ⍝ Standard APL

      VEC←1+⍳12

      VEC[2 2.5 3]                  ⍝ APL2.5
3 3.5 4
```

APL2.5 uses natural cubic splines to interpolate in more complex cases. An obvious use of this facility is to plot smooth curves through a series of points (similar to the GDDM option 'CURVE').

Rather than continue the controversy over the 'best' APL keyboard layout (see the notes on the Falkoff Dual keyboard on page 92), IBM have chosen to bypass the problem completely, and are shipping the MicroWriter keyboard as an essential component of the system. They also provide an optional AP to allow voice recognition of APL expressions.

This is probably the first 'Environmentally Friendly' APL to hit the market. It justifies its distinctive green packaging with an enhanced `⎕EA`; when used with a numeric left argument, this gives the user the option of 'Environmentally Aware' execution. For example at `2 ⎕EA 'expression'` any attempt to produce printout will give a `DOMAIN ERROR`, and at `⎕EA` levels above 5, the processor switches to progressively more energy-efficient algorithms, until by `10 ⎕EA` it spends most of its time asleep.

Finally, supporters of I-APL will be delighted to see that not only is Direct Definition supported for functions, but that APL2.5 also has direct definition of Operators:

```apl
      PLUS:⍺+⍵
2 PLUS (2 4)[1.2]             ⍝ Note the need for ()
4.4

      ELSE:  ⍵ : β : ⍺
      1 -ELSE÷ 5
¯5
      0 -ELSE÷ 5
0.2
```

Note the extension of the conventional syntax to include β as the 'data' operand, in addition to ⍺ and ⍵ as the function operands. Readers might like to compare the simplicity of this new style of operator definition with the same `ELSE` operator in John Scholes's workshop on page 66.

## Price and Availability

APL2.5 is shipped on a single 3.5" optical disk, and will be available exclusively from APL-385 from 1st April (UK and Rockall only). The cost is £99.99 (excl VAT), inclusive of the 64-bit packager.

For more details, contact:

> I. Phelfritt<br>
> Brook House, Gilling East, York<br>
> Tel: 04393-385
