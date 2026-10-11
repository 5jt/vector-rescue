---
title: 'Limbering Up: Polyadic Functions'
authors:
- Gary A. Bergquist
volume: '18'
issue: '1'
page: '37'
unindexed: true
transcribed: 'from page images of VOL.18-NO.1-JULY-2001.pdf, pages 39–40 (printed 37–38; follows art10014440); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
queries:
- "Within the Zark Newsletter Extracts, introduced by Jon Sandles; printed as “LIMBERING UP: Polyadic Functions”. The column is unsigned; it is attributed to Gary Bergquist as the index attributes the Utility Corner columns of the series. The reprint note at the foot of p.38, which closes the extract, is included here."
- "Kept as printed: “What will be payment be?”."
---

(The purpose of this column is to work some flab off your APL midsection. Like muscles, your APL skills can atrophy if not exercised with adequate frequency and variety. This column presents a task for you to perform. Set aside a few minutes from your busy schedule and work the task. Mail in your solution and stay tuned for the results.)

To buy a house, you need to borrow 90000. The bank will lend you the money at 9% interest, provided you agree to repay the loan in equal monthly payments for the next 30 years. What will be payment be?

Your task is to write a function named `MORTGAGE` that returns the monthly repayment amount for any specified loan amount (90000), interest rate (.09), and term (30). (In this example, the monthly amount is 724.16.)

So you don’t have to waste time looking up the formula, here it is:

```apl
V←÷1+INT÷12 ⍝ Monthly discount rate
PMT←PRIN÷(V-V*1+12×TERM)÷1-V
```

| | |
|---|---|
| `INT`: | Nominal annual interest rate |
| `PRIN`: | Principal (amount borrowed) |
| `TERM`: | Number of years of loan |
| `PMT`: | Monthly payment |

Wait a minute!! Since the APL code is already written, where’s the limbering?

Glad you asked. This is a design task, not a coding task. This function requires three arguments (`INT`, `PRIN`, `TERM`), not one or two. Since APL permits monadic or dyadic functions, but is a bit weak at triadic functions, what function syntax should you use?

Whatever design you choose, test your function on the following problems:

1. Interest is 9%; principal is 90000; term is 30.
2. Interest is 9%; principal is 90000; term is 15, 20, 25, 30 (4-element vector result)
3. Interest is 8%, 9%, 10%; principal is 90000; term is 20, 25, 30 (3-element vector result).
4. Interest is 8%, 9%, 10%; principal is 90000; term is 15, 20, 25, 30 (3 by 4 matrix result).
5. You get the idea.

Mail your solution to:

> Vector Production<br>
> Brook House<br>
> Gilling East<br>
> YORK YO62 4JJ<br>
> UK

---

*Reprinted with kind permission from Zark APL Tutor News, a quarterly publication of Zark Incorporated 23 Ketchbrook Lane, Ellington, CT06029, USA*
