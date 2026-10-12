---
title: Microsoft Announce New APL
volume: '16'
issue: '1'
page: '39'
unindexed: true
transcribed: 'from page images of VOL.16-NO.1-JULY-1999.pdf, pages 41–43 (printed 39–41); Claude, 2026-10-12'
review: draft
tags:
- humour
queries:
- "Unsigned. The piece reprints, under a mock-news headline, documentation of the “APL” (adventure programming language) of Microsoft Flight Simulator, from the web page cited beneath the heading; no comment of the editors’ own is printed."
- "Kept as printed: “indention”; “A space or blank characters”; “in-sensitive”; “hungarian notation”; “Number range only between -32768, and +32767”; “No support of string variables” among the limitations beside “String variables” among the APLC32 features; “So it would be that line in your editor”; “FSFS APL”; the space in “flightsim/ fsconv98.exe”."
---

*http://idt.net/~alstone/fsfsapl.htm#apl_prog_env*

## LANGUAGE FEATURES/LIMITATIONS

### Language features

- BASIC like syntax.
- A command can start anywhere on a line, so indention can easily be applied.
- A space or blank characters can be applied anywhere within the program code. When a space is required by program syntax any number of spaces are allowed (the total number of characters on the line must not exceed 80).
- The Language syntax is case in-sensitive. The variables "TEMP" and "temp" are the same. The compiler converts everything to uppercase anyway (except for string constants). So those who want to employ fancy stuff like hungarian notation, etc. the compiler won't care.
- Support of limited Keyboard interaction.

### Additional APLC32 features

- Support of functions and procedures
- Local variables
- String variables
- Preprocessor directives (include, pragma)
- 64K file size limit does not apply
- Detection of aplc32 compiled adventures
- Line size limit up to 2048 with lexical item limit of 512

### Language limitations

- One command or statement allowed per line
- No support of string variables
- No support of File I/O
- Number range only between -32768, and +32767
- Very little support of flight control manipulation
- 64K binary adventure size limit

## The APL Programming Environment

APL programs can be written in any standard ASCII text file editor. The APLC compiler will compile text files into binary form for FS5. The compiler can be executed from the DOS command prompt. For use with FS6/98 they must either be compiled with the APLC.EXE into .ADV format and converted using the Microsoft (henceforth referred to as MS) supplied converters FSCONV.EXE [1] and FSCONV98.EXE [2] to FS6/98 format or compiled using the Freeware APLC32 compiler [3] (henceforth referred to as APLC32).

```
Syntax:
        APLC   "Input file"  ["Output File"]
```

The first argument after the program name is the name of the APL source file (APLC assumes a ".TXT" file extension, so that is optional). The second argument is the name of the adventure binary file (any extension given is stripped, and ".ADV" is used).

If errors in syntax are encountered during compilation they will be displayed on the screen or console window complete with line numbers. The line number pointing to the location of the error includes blank lines. So it would be that line in your editor, no need to worry about the count being off due to blank lines, they are included in the count.

APLC32 contains extra command line options which can be used at compile time.

| | |
|---|---|
| -c | Check syntax only, do not write the output file |
| -k | Attempt to convert old source file as it is compiled |
| -o | Disable extra optimisations |
| -oo | Disable all optimisations |
| -s | Send error output to stdout rather than stderr |
| -w | Do not produce warnings during compilation |
| -v | Turn off assignment checks for system variables |
| -a | Turn off altitude compensation |
| -fy or -fn | Turn on or off output directory forcing |
| -x | Turn off any extensions, useful to check compatibility |
| -95 | Generate output for FS6 (ver 1.18+). |
| -98 | Generate output for FS98 (ver 1.18+) |

See the APLC32.DOC file in [3] for more details of these command line options.

## The Basic Structure of FSFS APL Programs

APL is a programming language similar to the old DOS GW BASIC Language in format and syntax.

```
Example:

 TITLE "CMI to ORD adventure"
 DESCRIPTION "Champaign to Chicago adventure"
 ;Test adventure
 ;
 DECLARE "variable names"
 ....
 ....  (program code)
 END
```

Unlike languages like C or PASCAL no particular keyword or value is required (like main, start, begin, *etc.*) to successfully compile and execute an adventure. Though none of the keywords listed in the above example are required, we shall consider this the standard format of what should be in every adventure.

> For more information please refer to http://idt.net/~alstone/fsfsapl.htm

## References

1. http://www.microsoft.com/games/fsim/converter.htm
2. ftp://ftp.microsoft.com/deskapps/games/public/flightsim/ fsconv98.exe
3. ftp://ftp.iup.edu/flight-sim/uploads/aplc119.zip
