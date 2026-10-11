---
title: A Note on CPU Time Monitoring
authors:
- Joseph L.F. De Kerf
volume: '8'
issue: '3'
page: '136'
unindexed: true
transcribed: 'from page images of VOL.8-NO.3-JANUARY-1992.pdf, pages 142–144 (printed 136–138; the first letter in Technical Correspondence, before Horner’s Method); Claude, 2026-10-11'
review: draft
tags:
- performance
- implementations
- standards
queries:
- "A letter in Technical Correspondence, From: Joseph L.F. De Kerf, 25 November 1991. The table has no caption or headings in print."
- "The street address under the signature (two lines, after “AD Informatics”) is omitted."
---

*From: Joseph L.F. De Kerf, 25 November 1991*
{ .byline }

In a paper published in Vector [1], Ray Cannon convincingly demonstrates the advantages of the availability of the CPU time monitoring function in APL. Unfortunately, this paper gives the unintended impression CPU time monitoring is a new facility only made available in STSC’s APL\*PLUS System Function `⎕MF`.

In fact, the facility was already made available in the seventies, by Control Data CDC with the system function `⎕LTIME` [2], and by Burroughs, with the system functions `⎕SM` - `⎕RM` - `⎕QM`, the results of the monitor being made available through the system functions `⎕MC` and/or `⎕MV` [3]. Later on the facility was made available in VAX APL and Dyalog APL through the system function `⎕MONITOR` and in APL\*PLUS and SHARP APL through the system functions `⎕FM` and/or `⎕MF`. An overview is given in the accompanying table, the year giving the approximate date of the implementation of the facility.

The most user-friendly implementation seems to me to be that based on the system function `⎕MONITOR`. In VAX APL V-2/3/4, the dyadic form of `⎕MONITOR` sets the monitor for the unlocked defined functions/operators specified by the right argument vector or matrix, each row specifying one operation name. The left argument specifies the lines of the operations on which the monitor is to be set. If the left argument contains a zero, the monitor is set to the entire operation. The monitor may be disabled by specifying an empty left argument. The explicit result is a boolean vector, specifying whether the monitor has been set. The monadic form of `⎕MONITOR` returns an n by 3 matrix, where n is the number of monitored lines. The columns give the monitored line numbers, the execution count, and the cumulative CPU time in milliseconds.

In Dyalog APL V-5 and DOS/UNIX, the `⎕MONITOR` behaves about the same, the right argument of the dyadic form however being restricted to the specification of one operation and the explicit result being a vector specifying the line numbers on which the monitor has been set. On the other hand, the monadic form returns an n by 5 matrix, the columns giving the monitored line numbers, the execution count, the cumulative CPU time, and the elapsed time, both in milliseconds. The fifth column is provisionally reserved and gives zeros.

An example of the use of the `⎕MONITOR` with VAX APL V-2/3/4 is given below. The defined function `FIB N` returns as explicit result the `N` first terms of the Fibonacci Series. Calculation is based on the recursive generator F(1) = 1, F(2) = 1, and F(N) =F(N-2)+F(N-1). N is set to 100.

| | | | |
|---|---|---|---|
| Bull-Honeywell | APL 64 | 1980 | `⎕SM ⎕RM ⎕MV` |
| Bull-Honeywell | APL 7 | 1985 | `⎕SM ⎕RM ⎕RV` |
| Burroughs/Unisys | APL/700 | 1974 | `⎕SM ⎕RM ⎕QM ⎕MC ⎕MV` |
| Control Data | APL 2.0 CN | 1976 | `⎕LTIME` |
| Control Data | NOS/VE APL | 1984 | `⎕LTIME` |
| Digital Equipment | VAX APL V2 | 1985 | `⎕MONITOR` |
| Digital Equipment | VAX APL V3 | 1987 | `⎕MONITOR` |
| Dyadic systems | Dyalog APL | 1986 | `⎕MONITOR` |
| General Electric | OS4000 APL | 1979 | `⎕SM ⎕RM ⎕MC` |
| Hewlett-Packard | APL\3000 | 1976 | `⎕SM ⎕RM ⎕QM ⎕MV` |
| IPSA (Reuter) | Sharp APL | 1987 | `⎕FM` |
| IPSA (Reuter) | Sharp SAX | 1988 | `⎕MF` |
| SLIGOS/BARTS | APL-NET | 1978 | `⎕SM ⎕RM ⎕QM` |
| STSC | APL\*PLUS | 1985 | `⎕MF` |

```apl
     ∇R←FIB N
[1]   →(N≤2)/0,R←(2⌊N)⍴1
[2]   END:→(N>⍴R←R,+/¯2↑R)/END
     ∇

      0 1 2 ⎕MONITOR'FIB'
1
      R←FIB 100
      ⎕MONITOR'FIB'
0  1 2050
1  1   20
2 98 1940
```

But once again - there is a proliferation of implementing new system commands and system variables/functions. A list of about three hundred system commands and a list of about eight hundred system variables/functions, supported by current implementations, have been published recently [4][5]. Most of the facilities made available, e.g. monitoring CPU time, prove to be valuable enhancements. Unfortunately, the same facility is often implemented in most divergent ways, leading to an inconvenient plethora of synonyms and homonyms. And even if the same distinguished name is used for the same facility, this does not mean that syntax and/or output are the same.

The situation does not only confuse the declared user, but also doesn’t inspire confidence on behalf of the potential newcomer, and is a serious obstacle for the future of our language APL. ISO APL and the draft ISO APL Extended only specify a small set of system variables/functions and do not resolve the problems quoted. The main objective of a standard is to promote portability and as such should support those facilities which are common practice. Everybody knows all these things, but “something has to be done on it!”.

Joseph De Kerf<br>
Agfa-Gevaert NV<br>
AD Informatics

## References

1. R. Cannon; *How STSC’s ⎕MF can help in testing APL workspaces*; Vector, Vol. 8, No. 2, October 1991, pp. 135-136.
2. R. Mayforth; *APLUM-APL at the University of Massachusetts*; APL Quote Quad, Vol. 6, No. 1, Spring 1975, pp. 15-21.
3. L. Ryan; *Application Diagnostic Aids in APL/700*; APL 76 Conference Proceedings, Ottawa, Canada, 22-24 September 1976; Edited by G.T. Hunter; Association for Computing Machinery, New York, 1976; pp. 343-345.
4. J.L.F. De Kerf; *System Commands and APL - A Survey*; APL-CAM Journal, Vol. 13, No. 2, 16 April 1991, pp. 449-455.
5. J.L.F. De Kerf; *APL System Variables and System Functions - A Survey*; APL-CAM Journal, Vol. 13, No. 3, 10 July 1991, pp 744-766.
