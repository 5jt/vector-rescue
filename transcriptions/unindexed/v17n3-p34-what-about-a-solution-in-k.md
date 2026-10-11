---
title: What about a solution in K?
authors:
- Stefano Lanzavecchia
volume: '17'
issue: '3'
page: '34'
unindexed: true
transcribed: 'from page images of VOL.17-NO.3-JANUARY-2001.pdf, pages 36–38 (printed 34–36; within Zark Newsletter Extracts, after “Vector Update”); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- data and files
- language design
queries:
- "The last item in the Zark Newsletter Extracts, printed under the heading “What about a solution in K? (by Stefano Lanzavecchia)”: a K solution to the comma-delimited data task of 17:2. The K was not run."
- "Kept as printed: “In won’t claim”, “which is composed by 3 fields”; the result `6 4` of `fieldw[sep,tq;data]`; `fieldw[sep,tq;a]` in the matrix expression, where the other calls name `data`."
---

In won’t claim I did it all by myself, not because I couldn’t but simply because I remembered before starting that in the mail-list dedicated to K developers a solution to a similar problem had appeared in the past.

I will use this message (http://www.kx.com/listbox/k/msg00544.html) as base and will adapt it to the problem as described in Vector 17.2. I won’t claim anyway that my solution is an example of good coding in K nor that it is an example of solving the problem with a fast K algorithm.

For a similar tutorial have a look at: http://www.kx.com/a/k/examples/tab.k

First of all: in K files are not read but mapped to a variable name. If the mapping is done using the operators that operate on text, the variable will be seen as a list of strings properly split at the end-of-line markers. Handy. Therefore, if I take for my example a file with 14 lines the following will apply:

```
    data: 0:"file.csv"
    #data
14
```

Now, since in comma-separated files, a text qualifier is used to allow fields to contain the separator, let’s define two variables with the text qualifier and the separator

```
    tq: "\""
    sep: ","
```

This will allow us to interpret properly lines such as

```
"Fred,Jane",10,UK
```

which is composed by 3 fields, the first one being

```
Fred,Jane
```

without the quotes. This makes the problem slightly more interesting and realistic, since most Spreadsheet and Database programs will export CSV files in this format.

Let’s define a verb to mark the section of each line not enclosed in quotes (notice that in K the backslash is used to escape a quote inside a string):

```
    uq: {~b[0]|':b:(~=)\y=x} \ dyadic verb:first argument is
                               the text qualifier
    uq[tq;"\"Fred,Jane\",10,UK"]
0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1
```

We also need a verb to remove quotes:

```
    nq:_dv[;tq]
    nq "\"Fred,Jane\",10,UK"
"Fred,Jane,10,UK"
```

Please notice that in K strings are always printed with quotes surrounding them, but they are not part of the string itself.

We are almost there. We now need a function to cut a line at every separator taking into account the text qualifiers and removing unnecessary quotes.

```
    cut:{(nq 1_)'(&uq[x[1];d]&d=x[0])_ d:(x[0]),y}
```

Once again the first argument is now the separator, followed by the text qualifier:

```
    cut[sep,tq;"\"Fred,Jane\",10,UK"]
("Fred,Jane"
 "10"
 "UK")
```

All we need to do is to repeat the cut on each line and calculate the max width of each column:

```
    csv: {cut[x;]'y}
    fieldw: {|/#:''csv[x;y]}
    fieldw[sep,tq;data]
6 4
```

Now to generate a matrix as requested in the problem description we can use:

```
    ,/'(-fieldw[sep,tq;a])$/:csv[sep,tq;data]
```

Since `fieldw` calls `csv`, we are actually wasting quite a lot of work. We could factor the expression as follows:

```
    COMMAdeltaMAT: {,/'{$[#[#x;,-|/#:''x];x]}csv[x;y]}
```

Actually, it doesn’t make a lot of sense to repackage the result of `csv` (already nicely cut field per field) into a matrix, but since this was part of the original problem statement, I decided to include this last step.

Exercises for the reader:

- extend the verb `cut` so that a quote inside a quoted string can be expressed as a double quote;
- make `fieldw` work in the case when in the original file not all the lines contain the same number of fields.

Since K is geared more and more towards supporting Kdb, one would expect a built-in operator to handle CSV files directly. Sure enough, with a little bit of patience, scavenging the terse documentation on the web site, I found that, given “nf” the number of fields per line, the verb I called `csv` can be rewritten as

```
    nq''+((nf#"C");sep)0:"file.csv"
```

More, if one knows that the first 2 fields are integers, the third is a string, and the fourth is a floating point, one can write expressions like:

```
    +("IICF";sep) 0:"file.csv"
```

and have the data automatically converted to the native types.

Download your copy of K from http://www.kx.com/ and have fun.
