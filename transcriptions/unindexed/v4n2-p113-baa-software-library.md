---
title: 'The British APL Association Software Library: Call for Software; Full Catalogue'
authors:
- Dave Ziemann
volume: '4'
issue: '2'
page: '113'
unindexed: true
transcribed: 'from page images of VOL.4-NO.2-OCTOBER-1987.pdf, pages 115–124 (printed 113–122); Claude, 2026-10-06'
review: draft
queries:
- "The catalogue is typewritten; transcribed as preformatted text, keeping its layout. The submission form and order form that follow (printed pp.124–126) are not transcribed."
- "Disk 15 is not listed: the catalogue goes from 14 to 16."
- "Disk 7’s “Software required” line and Disk 9’s missing “Disk donated” line are as printed; Disk 1 gives no software requirement."
- "Slips transcribed as printed: “primarilly”, “transfering”, “in he APL style”, “Elsewhere The BAASL” (missing full stop)."
---

by Dave Ziemann
{ .byline }

## Call for Software

### Purpose

The purpose of the British APL Association Software Library (BAASL) is to provide useful software to the APL community. In order to achieve a high level of service, we need a good supply of quality software.

### What kind of software?

We are looking for anything that could be of interest to the APL programmer, user or manager. It might be a tool for migrating APL workspaces between different interpreters, general APL utilities, APL2 functions for simulating component files, a reverse Polish model of APL or even a DOS adventure game. Each of these examples is an actual disk from the library.

There are no restrictions on the type of software, type of APL or the type of machine on which the software is to be run. As long as it is of interest to APLers, then it is worthy for consideration. The programs do not even have to be written in APL, although we do not want to fill the library with software which is easily available elsewhere The BAASL is primarilly concerned with offering ‘public domain’ software, which should normally include unlocked source code wherever possible. Bona-fide ‘shareware’ software is acceptable, and we are also happy to carry ‘demonstration disks’, which advertise commercially available software, provided that this is made quite clear.

If you are considering creating software for the library, read the software submission form first, so that you know what is expected of you. Please share the fruits of your work with others.

### Transfer medium

The transfer medium for the BAASL is currently the DOS-format five-and-a-quarter inch floppy diskette. If you can get it onto a floppy disk, then we can make it available to others. If the target machine is not a PC, then appropriate transfer instructions should be included on the disk.

### Documentation

The library will not currently handle any medium other than the floppy disk. In particular, we do not undertake to distribute paper documentation of any kind.

All disks must therefore include sufficient user documentation to permit effective use of the software. The donor may include an address where paper documentation can be obtained, possibly at a nominal cost.

### Charges

It is not intended that the BAASL make a profit. Our charging policy is designed to cover the cost of materials, postage and handling, although we do make a reduced charge to BAA members in order to encourage membership.

A BAASL software donor must not require payment from the user, although reasonable charges for registration or paper documentation may be advertised on the disk. Disks that demonstrate commercially available products are acceptable, provided that this is made clear.

### Liability

A signature is required to declare the donor’s right to allow the BAA to copy the software, and to permit anyone to copy and use it. Software is accepted by the BAA on good faith, and we do not vouch for or make any claims regarding donated software.

The BAA cannot be held responsible or liable for any damage, however caused, by the use or misuse of library software, and shall not be liable in any way in the event that submitted material proves to be the subject of third party copyright.

### Reviewers

Unfortunately, we do not have the time to study each submitted disk in detail, although we check that disks do roughly what they claim to, and that they appear to work. We would like to publish reviews of library software in VECTOR, and so we welcome offers from all you keen reviewers out there. In fact we will even send your disks free of charge, if you write a review for VECTOR!

In any event, please write to tell us what you think of a particular BAASL disk, and how you found it useful. If you find glaring holes in the library, let us know what is missing and we will try to plug the gap. Better still, write it yourself.

## Full Catalogue

```text
DISK 1            The game of LIFE
SIZE=113K         DONOR: Paul Chapman

Hardware required: PC
Software required:
     Disk donated: July 1986

README   001  THE FILE YOU ARE READING
LIFE     EXE  Program file
LIFE     DOC  Documentation

GGUN     LIF  CYCLIC30 LIF  FIG11A   LIF  SHM      LIF
ACORN    LIF  BG1      LIF  FIG11B   LIF  SHS      LIF   these
PUFFER   LIF  BG2      LIF  FIG11C   LIF  S9       LIF   files
SCHICK   LIF  BG3      LIF  FIG11D   LIF  S10      LIF   are
PREGUN   LIF  BG4      LIF  FIG11E   LIF  SHUTTLE  LIF   stored
MSHIPFAC LIF  FIG15    LIF  FIG11F   LIF  SRING2X2 LIF   LIFE
TRIPWIRE LIF  FIG13A   LIF  S1       LIF  SRING1X1 LIF   patterns
GRIDGLID LIF  FIG13B   LIF  S2       LIF  GFRING1  LIF   for
GR1      LIF  FIG14    LIF  S3       LIF  GFRING2  LIF   you
GR1T2    LIF  FIG10A   LIF  S4       LIF  NEWGUN   LIF   to
GR1B     LIF  FIG10B   LIF  S5       LIF  MSHIP1   LIF   explore.
GR1C     LIF  FIG10C   LIF  S6       LIF  MSHIP2   LIF
CYCLIC1  LIF  FIG10D   LIF  S7       LIF  REFL90   LIF
CYCLIC2  LIF  FIG10F   LIF  S8       LIF  XLATE4   LIF
CYCLIC3  LIF  FIG10E   LIF  SHL      LIF

The large 65532 by 65532 universe is represented as a run-coding.
This means that the speed to calculate the next generation is
proportional to the number of live cells rather than the universe size.

The program was prototyped using APL*PLUS PC, and then hand-coded in
assembler. The development of the software is described in Paul's paper
in the APL86 Tutorial Volume.

Extremely good fun, and a must for serious 'LIFE' researchers.


DISK 2            Fluctuation analysis for multichannel spectra
SIZE=9K           DONOR: Claude Bastian

Hardware required: PC
Software required: APL*PLUS PC
     Disk donated: July 1986

README   002  THE FILE YOU ARE READING
WALSH    AWS

Further description in the APL86 Conference Proceedings,
on pages 50 to 58.


DISK 3            Free software from APL385
SIZE=282K         DONOR: Adrian Smith

Hardware required: PC
Software required: APL*PLUS PC
     Disk donated: July 1986

README   003  THE FILE YOU ARE READING
READ     ME
FLIST    PAS  Pascal source code for
FLIST    COM  DOS file lister
SUPERMAN AWS  Expert system shell
PHONES   AWS  Demo of DB/385 routines
APL385   AWS  Screen design and assorted functions
DL       AWS  Selected DownLoad and char design for FX-80
INIO     AWS  Straighten out text keyboard
UTIL     AWS  Useful file utilities and odds and ends
DL       PDL  Handy set of APL download symbols
HANDOUT  PRN  Type this to your Epson!
READ     ME2  APL-385 license arrangements
CUCKOO   AWS  Digital cuckoo clock (honest)!

Documentation available for 50 Pounds or 75 US Dollars.


DISK 4            Piano
SIZE=4K           DONOR: Gerard Langlet

Hardware required: PC
Software required: APL*PLUS PC
     Disk donated: July 1986

README   004  THE FILE YOU ARE READING
PIANO    AWS


DISK 5            Pianoman
SIZE=355K         DONOR: Stuart Yarus                     *SHAREWARE*

Hardware required: PC
Software required:
     Disk donated: July 1986

README   005  THE FILE YOU ARE READING
PLAYRPNO COM
PIANOMAN COM
PIANOALT COM
MACROS   ARC
TUNES    ARC
TUNES2   ARC
COMTUNES ARC
COMTUNES DIR
TUNES    DIR
TUNES2   DIR
MACROS   DIR
READTHIS IST
PIANOMAN DOC
ARCX     COM

Contribution of 25 US Dollars requested.


DISK 6            FRAME - Multidimensional numeric array editor
SIZE=69K          DONOR: Robert Pullman

Hardware required: PC
Software required: Sharp APL/PC
     Disk donated: July 1986

README   006  THE FILE YOU ARE READING
FRAME--- SAW
FRAMES-- SAF

Full-screen multidimensional numeric spreadsheet, with names for
each dimension and column/row/plane etc.


DISK 7            Get/Put files for filing data by name
SIZE=21K          DONOR: M Kent

Hardware required: PC
Software required: APL*PLUS PC
     Disk donated: July 1986

README   007  THE FILE YOU ARE READING
GP       AWS  Get/Put workspace
GPHOW    ASF  Documentation (incomplete)

Functions for accessing filed data by item name rather than
component number.


DISK 8            Binary Combinations
SIZE=3K           DONOR: Otway Pardee

Hardware required: PC
Software required: APL*PLUS PC
     Disk donated: July 1986

README   008  THE FILE YOU ARE READING
COMB     AWS

Very fast method for generating the binary image of combinations.


DISK 9            Workspace Lister for APL*PLUS PC
SIZE=16K          DONOR: Roger Harper

Hardware required: PC, Epson LQ1500 printer
Software required: APL*PLUS PC

README   009  THE FILE YOU ARE READING
PCTYPE   AWS

Pretty-prints variables and functions, with index and pagination.
Assumes LQ1500 printer.


DISK 10           TEXT - Typesetting for the IBM PC using APL*PLUS PC
SIZE=343K         DONOR: Ian Feldberg

Hardware required: PC
Software required: APL*PLUS PC

README   010  THE FILE YOU ARE READING
FGRK     AWS
FENG     AWS
FGOTH    AWS
FSCPT    AWS
FITAL    AWS
FMISC    AWS
TEXT     AWS

Requires BAA PDSL Disk 11 - GRAPHPAK for the IBM PC.
Documented in APL86 conference proceedings.


DISK 11           PCPAK - GRAPHPAK for the IBM PC
SIZE=33K          DONOR: Ian Feldberg

Hardware required: PC
Software required: APL*PLUS PC
     Disk donated: June 1986

README   011  THE FILE YOU ARE READING
PCPAK    AWS  Driver
POLAR    AWS  Polar coordinates
HP7550   AWS  HP plotter software

Plot on a PC graphics board or HP7550 plotter.


DISK 12           Functions for Linear Algebra
SIZE=57K          DONOR: Garry Helzer

Hardware required: PC
Software required: APL*PLUS PC
     Disk donated: July 1986

README   012  THE FILE YOU ARE READING
LINALG   AWS

Functions described in Helzer's book Applied Linear Algebra,
published by Little, Brown and Co., Boston 1983.


DISK 13           DOS utilities
SIZE=57K          DONOR: Timo Kiravi

Hardware required: PC
Software required:
     Disk donated: July 1986

README   013  THE FILE YOU ARE READING
BROWSE   COM  View text files
CWEEP    EXE  Mass copy files, etc
D        COM  Formatted disk directory
DOSEDIT  COM  Command line editor


DISK 14           APL to Reverse Polish Translation
SIZE=311K         DONOR: Richard J Naugle

Hardware required: PC
Software required: APL*PLUS, IBM, SHARP or PortaAPL
     Disk donated: July 1986

README   014  THE FILE YOU ARE READING
CRCK4    DAT  Checksums for each file on disk
IMPORT-- SAW  Sharp APL ws for importing WSI files
APLDEMO  EXE  PortaAPL demonstration APL. File save disallowed
XLATE    APL  PortaAPL ws of APL to Reverse Polish translation
XLATE    AWS  APL*PLUS ws of APL to Reverse Polish translation
XLATE___ APL  IBM APL Vnl ws of APL to Reverse Polish translation
XLATEDEM BAT  Batch command for APL to Reverse Polish demonstration
CRCK4    COM  Produces checksums of files
XLATE    WSI  )EXPORT of PortaAPL APL to Reverse Polish workspace
IMPORT__ APL  IBM APL workspace to import WSI workspace
README   PFS  PFS write file of README.1ST (Need PFS Write to use)
TDROM1        Used by APLDEMO when the PC contains an STSC ROM
XLATEDEM IN   Input commands to PortaAPL for the demonstration
IMPORT   AWS  APL*PLUS workspace to import WSI workspace
README   1ST  ASCII documentation file

An APL model for translating APL statements to RL2 reverse polish
expressions. As described in the APL Conference Proceedings.
Workspaces supplied in four flavours, as above. A public domain
version of PortaAPL that does not allow the saving of files is
included.

NB: If you wish to check your disk by running the supplied checksum
    program CRCK4.COM, you must first erase the files README.014
    and CRCK4.DAT from a copy of your disk.


DISK 16           F83VEC Demonstration
SIZE=318K         DONOR: Richard Naugle

Hardware required: IBM PC
Software required:
     Disk donated: July 1986

README   016  THE FILE YOU ARE READING
CRCK4    DAT  Cyclic checksums for each file
README   PFS  PFS WRITE format of README file
APLDEMO  EXE  PortaAPL public domain demonstration
PLOTDEM  APL  PortaAPL parabola plotting workspace
PLOTDEM  BAT  Batch file for PortaAPL parabola plotting ws
MUSICDEM WSI  Workspace Standard Interchange format for below
MUSICDEM APL  PortaAPL Greensleeves playing workspace
CRCK4    COM  Program that produces file checksums
PLOTDEM  WSI  Workspace Standard Interchange format for plot demo
IMPORT-- SAW  Workspace used to import .WSI wss into Sharp APL
IMPORT   AWS  Workspace used to import .WSI wss into APL*PLUS
README   DEM  Instructions for running plot and music demos
TDROM1        PortaAPL support file for using STSC APL ROM
F83VEC   COM  Forth object that extends F83 to use APL symbols
EXAMPLES 4TH  Forth examples that may be run under F83VEC
DRIVERS  4TH  Forth source to support display adaptor with IBM ROM
MUSICDEM BAT  Batch file for PortaAPL Greensleeves playing ws
README   VEC  Documentation for F83VEC

This disk demonstrates the object code for an extension of FORTH
that uses APL symbols and processes vectors in he APL style.


DISK 17           APL Migrate
SIZE=268K         DONOR: Richard Naugle

Hardware required: IBM PC
Software required: Sharp, IBM, Porta or APL*PLUS APL
     Disk donated: February 1987

README.017         THE FILE YOU ARE READING
README             Overall instructions for APL migrate.
ECO                Changes since last version.
NEC2050.COM        Command prints or displays DOS ASCII+APL 1.0 files.
CRCK4.COM          Checksum command.
CRCK4.DAT          Root dir checksums produced by CRCK4 *.* >CRCK4.dat
PORTA\README       Instructions for the PORTA directory.
PORTA\OUT.APL      Migrates PortaAPL workspace to a ASCII+APL 1.0 file.
PORTA\IN.APL       Migrates ASCII+APL 1.0 file to a PortaAPL workspace.
PORTA\EXPORT.APL   Migrates PortaAPL workspace to a WSIS 0 file.
PORTA\IMPORT.APL   Migrates a WSIS 0 file to a PortaAPL workspace.
PORTA\OUT.WAA      ASCII+APL 1.0 file image of PORTA\OUT.APL.
PORTA\IN.WAA       ASCII+APL 1.0 file image of PORTA\IN.APL.
PORTA\EXPORT.WAA   ASCII+APL 1.0 file image of PORTA\EXPORT.APL.
PORTA\IMPORT.WAA   ASCII+APL 1.0 file image of PORTA\IMPORT.APL.
PORTA\CRCK4.COM    Checksum command.
PORTA\CRCK4.DAT    Porta directory checksums from CRCK4 *.* >CRCK4.dat
STSC\README        Instructions for the STSC directory.
STSC\OUT.AWS       Migrates STSC APL workspace to a ASCII+APL 1.0 file.
STSC\IN.AWS        Migrates ASCII+APL 1.0 file to a STSC APL workspace.
STSC\EXPORT.AWS    Migrates STSC APL workspace to a WSIS 0 file.
STSC\IMPORT.AWS    Migrates a WSIS 0 file to a STSC APL workspace.
STSC\OUT.WAA       ASCII+APL 1.0 file image of STSC\OUT.AWS.
STSC\IN.WAA        ASCII+APL 1.0 file image of STSC\IN.AWS.
STSC\EXPORT.WAA    ASCII+APL 1.0 file image of STSC\EXPORT.AWS.
STSC\IMPORT.WAA    ASCII+APL 1.0 file image of STSC\IMPORT.AWS.
STSC\CRCK4.COM     Checksum command.
STSC\CRCK4.DAT     STSC directory checksums from CRCK4 *.* >CRCK4.DAT
IBM\README         Instructions for the IBM directory.
IBM\OUT---.AIO     Migrates IBM APL workspace to a ASCII+APL 1.0 file.
IBM\IN----.AIO     Migrates ASCII+APL 1.0 file to a IBM APL workspace.
IBM\EXPORT.AIO     Migrates IBM APL workspace to a WSIS 0 file.
IBM\IMPORT.AIO     Migrates a WSIS 0 file to a IBM APL workspace.
IBM\OUT.WAA        ASCII+APL 1.0 file image of IBM\OUT---.AIO.
IBM\IN.WAA         ASCII+APL 1.0 file image of IBM\IN----.AIO.
IBM\EXPORT.WAA     ASCII+APL 1.0 file image of IBM\EXPORT.AIO.
IBM\IMPORT.WAA     ASCII+APL 1.0 file image of IBM\IMPORT.AIO.
IBM\CRCK4.COM      Checksum command.
IBM\CRCK4.DAT      IBM directory checksums from CRCK4 *.* >CRCK4.DAT
SHARP\README       Instructions for the SHARP directory.
SHARP\OUT___.SAW   Migrates Sharp APL workspace to a ASCII+APL 1.0 file.
SHARP\IN____.SAW   Migrates ASCII+APL 1.0 file to a Sharp APL workspace.
SHARP\EXPORT.SAW   Migrates Sharp APL workspace to a WSIS 0 file.
SHARP\IMPORT.SAW   Migrates a WSIS 0 file to a Sharp APL workspace.
SHARP\OUT.WAA      ASCII+APL 1.0 file image of SHARP\OUT___.SAW.
SHARP\IN.WAA       ASCII+APL 1.0 file image of SHARP\IN____.SAW.
SHARP\EXPORT.WAA   ASCII+APL 1.0 file image of SHARP\EXPORT.SAW.
SHARP\IMPORT.WAA   ASCII+APL 1.0 file image of SHARP\IMPORT.SAW.
SHARP\CRCK4.COM    Checksum command.
SHARP\CRCK4.DAT    Sharp directory checksums from CRCK4 *.* >CRCK4.dat

Contains workspaces to migrate Sharp APL, IBM, PortaAPL and APL*PLUS
to DOS files in WSIS 0 and WSIS ASCII+APL 1.0 formats, in both
directions. Also includes NEC Spinwriter printing software.


DISK 18           FFILES - Component files for APL2
SIZE=48K          DONOR: A N Wiggins

Hardware required: PC, MAINFRAME
Software required: APL*PLUS PC, APL2
     Disk donated: March 1987

README   018  THE FILE YOU ARE READING
FFILES   AWS  File utility. Similar to APL*PLUS sharefile.

Uses AP121 under APL2 to simulate an APL*PLUS-type component filing
system. The functions are stored on this disk in an APL*PLUS PC
workspace. Instructions for transfering the software to the mainframe
are NOT included. The functions in the workspace are as follows:

 FCREATE   Creates a new file
 FTIE      Ties the filename to a unique number
 FAPPEND   Appends data to the end of a tied file
 FDIR      Outputs the names of files
 FDROP     Replaces a component with ⍳0
 FERASE    Erases the tied file
 FLIB      Shows the contents of the 'fnums' variable
 FNAMES    Shows the file names held in 'fnums'
 FNUMS     Shows the tie numbers currently in 'fnums'
 FREAD     Reads a specified record in the specified file
 FREPLACE  Replaces a specified record in a specified file
 FUNTIE    Unties the specified file
 FRECORDS  Counts the number of records in the specified file


DISK 19           CAVEDOS - Adventure front-end to DOS
SIZE=83K          DONOR: Mark Bassett

Hardware required: PC
Software required: APL*PLUS PC 6.0
     Disk donated: March 1987

README   019  THE FILE YOU ARE READING
CAVEDOS  AWS  APL DOS-adventure game
CAVEDOS  DOC  Brief guide to play

Now you can really explore your hard disk: but beware of dragons,
pirates and dwarves! The more DOS commands you master, the higher
your score. Hints, answers or full solution available by sending
an S.A.E to the author.

The APL functions are locked.
```
