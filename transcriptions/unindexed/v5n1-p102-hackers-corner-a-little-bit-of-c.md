---
title: 'Hacker’s Corner: a little bit of C'
authors:
- Adrian Smith
volume: '5'
issue: '1'
page: '102'
unindexed: true
transcribed: 'from page images of VOL.5-NO.1-JULY-1988.pdf, page 104 (printed 102); Claude, 2026-10-12'
review: draft
tags:
- system interfaces
- programming techniques
queries:
- "The listing is a dot-matrix printout. Its font prints braces much like parentheses, and its asterisk and hash as heavy marks; they are read here by their C sense ({ } * #). The rows of asterisks and equals signs in the banner lines are given at about the printed length, not counted character by character."
- "The “visible | characters” that the program puts in place of tabs are printed as a broken bar; given here as |."
- "The usage message is read as “tf file[>outfile]”; the > is faint."
---

*by Adrian Smith*
{ .byline }

This little program might help you to see how the other half lives! It will take almost anything, and output a file suitable for Word; to my amazement it even ate Allan Gay's piece, which came as an APL component file! It runs in about 5 sec for a typical article.

```c
/****************************************************************************/
/* tf.c   April 1988   by Adrian Smith                                      */
/* Basic text filter ... passes any input file out to STDOUT having ...     */
/*   - ensured CR/LF pairs (to deal with APL quad-edit vectors)             */
/*   - stripped high bits from WordStar output                              */
/*   - removed white space (including all spaces at the end of paragraphs)  */
/*   - made tabs into visible | characters. Word can always put them back!  */
/****************************************************************************/
#include <stdio.h>
#include <ctype.h>

main(argc,argv)     int argc; char *argv[];

{ FILE *fp;
  int ch, in, cr = 13, lf = 10, tab = 9, bl = 0, np = 0;

  if (argc != 2)  {printf("Please use: tf file[>outfile]\n"); exit(1); }

  fp = fopen(argv[1],"rb");                       /* open for binary read     */
  if (!fp) { printf("Can't open file '%s'\n",argv[1]); exit(1); }

  while ((in = fgetc(fp)) != EOF)                 /* Process whole file       */
    {
      ch = toascii(in);                           /* Strip high bits (WStar)  */
      if (ch == lf);                              /* Forget linefeeds         */
        else if (ch == cr)                        /* CR/LF pair               */
         { if (np)                                /*  ... 2nd in a row        */
             { putchar('\n'); np=0; bl=0; }       /*      gives new para.     */
           else
             { np=1; bl=1; }                      /*  ... get ready for para  */

         }
       else if (ch == ' ') bl = 1;                /* Kill multiple blanks     */
       else
         { if (ch == tab) { ch = '|'; bl=0; }     /* Leave recognisable tabs  */
           if (ch == 96) ch = '\'';               /* Dispose of back quotes   */
           if (bl) putchar(' ');                  /* Output pending blank     */
           if (ch > 32) putchar(ch);              /* Ignore control chars     */
           bl=0; np=0;                            /* Output, and kill flags   */
         }
    }
  putchar('\n');                                  /* Finish off               */
} /*=========================== THE END ===================================*/
```
