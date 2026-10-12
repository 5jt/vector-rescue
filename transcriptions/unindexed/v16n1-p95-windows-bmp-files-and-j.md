---
title: Windows BMP Files and J
authors:
- Brook Anthony Schofield
volume: '16'
issue: '1'
page: '95'
unindexed: true
transcribed: 'from page images of VOL.16-NO.1-JULY-1999.pdf, pages 97–108 (printed 95–106); Claude, 2026-10-12'
review: draft
tags:
- programming techniques
- graphics
- data and files
queries:
- "The article ends on printed 106; printed 107 is the untranscribed introduction and contents list of the Technical Section, before Hacker’s Corner on printed 108."
- "Following the project rule for individuals’ contact details, the author’s personal e-mail address, printed beneath the byline, is omitted."
- "J code is given glyph by glyph as printed. In the printed monospaced face the tilde is drawn low and flat, much like a hyphen (e.g. in “chop =: }.~ 2&[”, “writing =: write~ \"1 bd @ hd” and “,\"1~”); it is given here as ~ throughout, as J requires and as it is clearly drawn in “mt =: }.~ matches”."
- "In the Appendix one comment line is printed broken over two lines (“… the presented data for” / “iteration”); it is joined here so that “iteration” does not read as a line of code."
- "The boxed-data displays (Table-6 and the two displays on printed 102) are given as one-row tables, the left and right boxes as cells."
- "Kept as printed: “Nd@tl” with a capital N in the Appendix definitions of head2rle and head2bmp (lower-case “nd@tl” on printed 98, and nd is defined lower-case); “the 30th bit … i.e. the 16th bit of the information header after the 12-bit file header”; “to either 0 or 1 when converting from run length encoding or uncompressed bitmaps respectively”; “1 4 8 or 24”; “pallet”; “biClImportant”; in Table-4 the expanded data “0 4 0”, “1 E 1 E 1 E 1 E 1”, “0 6 0 6 0” and “4 5 5 6 6 7”, and “00 06 45 56 67 00” against Table-5’s “00 03 45 56 67 00”; “32-byte boundaries”; “an 8-byte value”; “In order to process and bitmap”; “if they where used”; “I don’t know how do it”; “Windows BMP Bitmap Files and APL” in the Introduction but “Windows BMP Files and APL” in the Acknowledgements; the unbalanced quotation marks in the last paragraph of the Acknowledgements."
---

*by Brook Anthony Schofield*
{ .byline }

## Introduction

The purpose of this article is to describe my adventures with J in an attempt to create a script to run length encode (RLE) a Windows Device Independent Bitmap (DIB) file, which is more commonly known as a Bitmap or BMP.

The adventure began during a unit while studying for the final year of my degree. An exercise was proposed to explore functional programming and create a script that can functionally perform a task in the style used by the J programming language rather than the classical imperative programming that is usually taught. The task I selected, as described above, was to run length encode a bitmap image file.

Since J is designed along the same lines as APL as an array processing language I thought that a functional implementation of RLE would be relatively easy especially since a bitmap is described as “an image stored as an array of bits” by the Windows User Guide.

For avid readers of Vector you may notice that the title of this article is similar to one which appeared in Vector Volume 10, No.1, p.80 by Ray Cannon, entitled “Windows BMP Bitmap Files and APL”.

While this article isn’t a re-implementation of the topics covered in Ray’s article it is based on a sentence from it:

> “Since compressing and expansion of bitmaps is best carried out in a compiled language, it is not discussed further.”

While it may be best carried out in a compiled language, run length encoding is one of the simplest forms of compression and with the array processing features of the J programming language the tasks to implement this form of compression should be relatively simple.

This article starts with an outline of the structure of Microsoft Windows device independent bitmap files (BMP) and the format for run length encoding (RLE). This is followed by examples of J functions used for the manipulation of images in relation to the Windows Bitmap specifications for run length encoding.

## Bitmaps

Microsoft Windows version 3.0 defined a standard for bitmap files and it has been in use ever since. There is also a bitmap “standard” for OS/2 machines, which is only slightly different from the Microsoft specification. These differences make the functions, described in this article, incompatible with the OS/2 format at the current time.

## The Windows Device Independent Bitmap Format

Windows supports 4 different levels of colour in its Bitmaps:

- 1-bit, providing 2 colours which is often monochrome.
- 4-bit, providing 16 colours.
- 8-bit, providing 256 colours.
- 24-bit, providing 16.7 million colours.

Only 4 and 8-bit images allow compression using run length encoding and only 8-bit images have been used for the implementation of run length encoding within this article.

Both 4 and 8-bit encoding methods are described, with emphasis on the 8-bit method and how it relates to the J functions used for RLE image compression.

### Bitmap data structures

Each Windows BMP file contains a file header, an information header, a colour table and bitmap bits; each of these are described below.

| Offset | Size | Microsoft name | Description |
|--:|--:|---|---|
| 0 | 2 | bfType | The character BM for bitmap (66 77) |
| 2 | 4 | bfSize | The total size of the file |
| 6 | 4 | bfReserved1/2 | Reserved, must be set to zero |
| 10 | 4 | bfOffBits | The offset to the bitmap bits from the beginning of the file. |

**Table-1: Windows Bitmap File Header**

The purpose of the Windows Bitmap file header is to store the file type, size of the image and an offset to the start of the image data.

The Windows Bitmap file header doesn’t need to be modified within the context of the Bitmap to RLE conversion, or vice-versa.

The `bfSize` double-word is based on the uncompressed size of the image, and since it is already set within the file it does not need to be modified, no matter whether the file is being compressed or decompressed.

The Windows Bitmap information header is modified within the manipulation functions because the information header contains a flag for the compression scheme. Although it is a 4-byte field there is only the option for uncompressed bitmaps or RLE images, represented by a 0 or 1 respectively, on the 16<sup>th</sup> bit.

| Offset | Size | Microsoft name | Description |
|--:|--:|---|---|
| 0 | 4 | biSize | The size of this structure in bytes |
| 4 | 4 | biWidth | The width of the bitmap in pixels |
| 8 | 4 | biHeight | The height of the bitmap in pixels |
| 12 | 2 | biPlanes | Number of colour planes, set to 1 |
| 14 | 2 | biBitCount | Colour bits per pixel. 1 4 8 or 24 |
| 16 | 4 | biCompression | Code for the compression scheme |
| 20 | 4 | biSizeImage | Size of the bitmap bits in bytes |
| 24 | 4 | biXPelsPerMeter | Horizontal resolution in pixels per metre |
| 28 | 4 | biYPelsPerMeter | Vertical resolution in pixels per metre |
| 32 | 4 | biClrUsed | Number of colours defined in the pallet |
| 36 | 4 | biClImportant | Number of important colours in the image |

**Table-2: Windows Bitmap Information Header**

The function below uses `toRLE` to manipulate the header to set the 30<sup>th</sup> bit to 1, *i.e.* the 16<sup>th</sup> bit of the information header after the 12-bit file header.

```j
toRLE =: 1&}
head2rle =: (30 toRLE @(header {. nd@tl));header }. nd @ tl
```

The `head2rle` copies the header information to the left hand side (LHS) of the boxed values so they will not be altered by the encoding or decoding process as they are applied to the remaining boxed data. As stated, it sets the 30<sup>th</sup> element of the header (`biCompression`) to either 0 or 1 when converting from run length encoding or uncompressed bitmaps respectively.

The `biSize` is 40 for Windows DIBs and 12 for OS/2 DIBs, this causes an incompatibility between the current scripts if used with OS/2 bitmap files.

The colour table is used to specify the colours used within a bitmap image. This table is of no importance to the compression or decompression of bitmap images, but the integrity of the table has to be maintained. This is handled by the `header` function when called by the `head2bmp` or `head2rle` functions.

```j
header =: 54 & [ + 4 & [ * 2 & [  ^ 28&{ @ nd @ tl
```

The header function calculates the offset to the bitmap data by determining the bit depth of the image and then bytes that the colour table consumes. For 8-bit images the colour table is always static, but this allows the scripts to be used with 4-bit images to make this function more general.

| Offset | Size | Microsoft name | Description |
|--:|--:|---|---|
| 0 | 1 | rgbBlue | Blue intensity in the range 0-255 |
| 1 | 1 | rgbGreen | Green intensity in the range 0-255 |
| 2 | 1 | rgbRed | Red intensity in the range 0-255 |
| 3 | 1 | rgbReserved | Set to 0 |

**Table-3: Windows Bitmap Colour Table**

OS/2 DIBs use an RGB triplet rather than the Windows 4-byte entry. This also causes a problem to the current scripts, if they where used on OS/2 bitmaps.

## Run Length Encoding of Bitmap Files

Run Length Encoding (RLE) is only available for 4-bit and 8-bit images within the Windows BMP Specification. There are two forms of encoding within RLE:

- Encoded Mode
- Absolute Mode

Encoded Mode consists of two bytes, the first specifying the number of consecutive pixels to be drawn using the colour index which is specified by the second byte.

Absolute Mode is an escape sequence from Encoded Mode where the first byte is zero. The succeeding byte specifies one of four actions:

0. End of Line
1. End of Bitmap
2. A delta designated by two bytes which form unsigned values for the horizontal and vertical offsets to the next pixel from the current position. The area skipped is drawn in the background colour of the image.
3. Any value that is three or greater is taken as the number of bytes to be drawn verbatim, since there is no run of common pixels.

| Compressed Data | Expanded Data |
|---|---|
| 03 04 | 0 4 0 |
| 09 1E | 1 E 1 E 1 E 1 E 1 |
| 05 06 | 0 6 0 6 0 |
| 00 00 | End of Line |
| 00 01 | End of RLE bitmap |
| 00 02 05 01 | Move 5 right and 1 down |
| 00 06 45 56 67 00 | 4 5 5 6 6 7 |

**Table-4: 4-bit Run Length Encoded Data**

The third (number 2) absolute mode option is not implemented within this article and the fourth option is only implemented for decompression, not encoding.

Below is an example of some bitmap data in compressed and expanded format. The data in Table-4 is for 4-bit bitmap image data. The main difference between 4 and 8-bit image data is that the latter is stored per byte, while the former is stored per nibble. A nibble being the high and low order 4-bits of a byte.

```j
nibbles =: 16 16 & #:
```

The above function can be used to split the high and low order nibbles of a byte so that they can be treated separately. 4-bit images will not be the topic of any further discussion.

The data for 8-bit images, which is the format catered for by the script, allows each byte to represent either a pixel (uncompressed bitmap) or an encoded mode control which will ultimately represent a pixel.

| Compressed Data | Expanded Data |
|---|---|
| 03 04 | 04 04 04 |
| 09 1E | 1E 1E 1E 1E 1E 1E 1E 1E 1E |
| 05 06 | 06 06 06 06 06 |
| 00 00 | End of Line |
| 00 01 | End of RLE bitmap |
| 00 02 05 01 | Move 5 right and 1 down |
| 00 03 45 56 67 00 | 45 56 67 |

**Table-5: 8-bit Run Length Encoded Data**

## Handling Files

File handling is performed using the `read` and `write` functions:

```j
read =: 1!:1@<

boxed =: '' &; @ read

write =: 1!:2<

writing =: write~ "1 bd @ hd
```

These functions read in the data from a specified file name and box the data as explained in the *Iteration* section below. The *writing* of the data calls on a utility function to return a binary version of the data from numeric data.

## Utility Functions

Various utility functions are used throughout the J script. The explanation given to each within the Appendix is sufficient for their operation, they will be explained further in their appropriate sections.

## Iteration

Iteration is used extensively within the script to automate the encoding/decoding of arrays of data. This is accomplished by executing a function to the power of infinity. The stopping condition for this is achieved when the same result is returned twice by the function. This is demonstrated in the example below:

```j
bmp2rle =: writing ]`do_encode@.(*@#@tl)^:_ @ head2rle @ boxed
```

The `do_encode` function is called via the use of a gerund (`` ` ``). The gerund is triggered by returning the signum of the tally of the tail of the input data. When data is present in the right hand side (RHS) of the boxed data the function will be called repeatedly. Once the data on the RHS has become exhausted the gerund will call the `]` operator which will simply return the previous value and therefore halt the otherwise infinite loop. This style of iteration is used throughout the script.

| | 66 77 86 82 0 0 0 0 0 0 54 4 0 0 40 0 0 0 200 0 0 0 100 0 0 0 1 0 8 0 1 0 0 0 32 78 |
|---|---|

**Table-6: Boxed Data Structure For Iteration**

Above is a boxed version of the input data (being displayed in numerical data format rather than binary). The left hand side (LHS) box is initially empty. As data is transferred from one side of boxed list to the other, the function is re-called, with the result being further encoded data added to the LHS of the boxed data and fewer elements remaining in the RHS of the data.

## Bitmap Compression

The functions used for the compression of the bitmap data match the elements in the data to be processed, up to a maximum of 255 matches, as that is the largest value that can be stored as an 8-byte value.

```j
match =: E.~ {.

matches =: 255 &<. @ i. & 0 @ match
```

These matches are combined with the element that they are matching on, to form a run length encoded pixel representation.

| …12 182 | 34 34 34 34 34 255 255 192 13 52 52 52 182 182 52 182 17 17 17 63 63 63… |
|---|---|

Taking the example above, the boxed data contains some encoded data on the LHS and some uncompressed data on the right hand side (RHS). The matching process will return five instances of 34, so after the next iteration of the function the data will be as follows:

| …12 182 5 34 | 255 255 192 13 52 52 52 182 182 52 182 17 17 17 63 63 63 63 63 63… |
|---|---|

These functions are combined to create an *encode* function which is passed a boxed version of a single line of the bitmap image which is then iterated upon within the `inner_loop` function.

```j
mh =: matches , {.

mt =: }.~ matches

mtotalhd =: (mh @ tl ,@:(,"1~) hd);mt @ tl

inner_loop =: (]`mtotalhd@.(*@#@tl) ^:_)
```

The `inner_loop` function is called from another iterative loop, on the `do_encode` function. The result of each iteration is a boxed version of the data, which is slightly modified through the matching of the data at the head of the RHS and then removing that data from the next instance of the boxed data.

```j
convert_a_line =: 0 0&[ ,"1~ hd,"1 hd@inner_loop@boxw

remove_a_line =:  padding4 @ getw }. tl

do_encode =: convert_a_line ; remove_a_line
```

The `padding` utility function is used in the `remove_a_line` function to ensure that any padding material is removed from the RLE image. Bitmap images have to end their lines on 32-byte boundaries and therefore there can be up to 3-bytes of data that is unwanted from each line of an image. Padding data is generally random, taken from undefined memory locations.

## Bitmap Decompression

The decoding of a RLE bitmap image is more time and memory consuming than the encoding of it. The reason being that while you know the width of the BMP image you don’t know how many elements you will need to process until you have reached the end of a line. Remembering that bitmap images must have their lines end on a 32-byte boundary.

The `copy` functions below are used to remove elements from the RHS of the boxed data, usually in groups of two, and expand them to their original values.

```j
lit =: ({.2&}.)~ {. @ }.

cpy =: {. # {. @ }.

copy =: lit`cpy@.(*@{.)
```

The cut functions have to remove the same number of elements from the RHS of the data, that are being copied into the expanded data box.

```j
chop =: }.~ 2&[ + padding2 @ {. @ }.

trunc =: 2&}.

cut =: chop`trunc@.(*@{.)
```

The `chop` command is taking into account the *Absolute Mode* options for replication of uncompressed data and removing any padding data that may exist.

```j
padit =: padbmp`empty@.((1&{ *@>. 0&{)@tl)

padbmp =: 1&[ #~ pad4 @ getw

empty =: ''&[
```

The added complexity of the `padit` function is to cater for the instance where End of Line (zero zero) is found so that the image can be padded out to the correct number of bytes.

```j
do_decode =: (copy @ tl ,@:(,"1~) hd , padit); cut @ tl
```

The entire `do_decode` function is shown above, which encompasses all the described decoding functions.

## Processing the Bitmap Image Information

In order to process and bitmap or run length encode bitmap files the following functions can be executed:

```j
'output.bmp' bmp2rle 'input.bmp'
```

`bmp2rle` will process an uncompressed bitmap file in *input.bmp* and encode the data and output a valid run length encoded bmp image into *output.bmp.*

```j
'output.bmp' rle2bmp 'input.bmp'
```

`rle2bmp` will process a compressed bitmap file in *input.bmp* and decode the data and output a valid bitmap image into *output.bmp.*

## Notes on J

The code was written using J version 4.01a and uses some operators that do not work under older versions of J, such as version 3.

The code does not require you to run under Microsoft Windows™, in fact all testing was performed on a Macintosh™. This is why example file paths are incomplete, as they will need to be localised for your system type.

It is recommended that you have a bitmap image viewer/manipulator available if you wish to test the code and view the output files.

All the code was written functionally, and it is intended that you use the functions interactively for the processing of your images. Also note that the process can be time-consuming depending on your machine type and the size of the image that you are attempting to manipulate.

## Conclusion

Microsoft Device Independent Bitmaps are relatively simple in format and can be easily converted from uncompressed to compressed versions for both 4 and 8 bit images which support compression.

As a further exercise to the reader, you may like to attempt the implementation of 4-bit RLE of bitmaps based on the principles described in this article, the author would love to hear of any attempts made. Also since the functions do not support OS/2 DIBs, modifications to the functions to support these, and possibly other file formats, would be a worth while exercise.

## Acknowledgements

I would like to thank Ray Cannon and Adrian Smith for their assistance in providing me with a copy of the article “Windows BMP Files and APL” when the library resources that I had access to were lacking.

Thanks also to Mark Feldman from the PC Game Programmers Encyclopaedia (PC-GPE) for his information on the Windows BMP File format.

And to quote from Ray Cannon’s article again “However, the reverse process, conversion from Bitmap to Metafile, is “not trivial”. (“Not trivial” is a euphemism for “I don’t know how do it”!)

## Appendix – Code

```j
NB. File Input Output
NB. read in data from a file and box it up
read =: 1!:1@<
boxed =: '' &; @ read
NB. write unboxed binary data to a file
write =: 1!:2<
writing =: write~ "1 bd @ hd


NB. Utility Functions
NB. get the head (first box) or tail (second box)
hd =: ,@ (>@}:)
tl =: ,@ (>@{:)
NB. returns 'numeric data' for comparison operations
nd =: a.&i.
NB. translates 'numeric data' back into binary data
bd =: { & a.
NB. get the width of the image from the 18th element of the header
getw =: 18&{ "1 @ hd
NB. get a boxed version of width elements of the data
boxw =: ''&[;getw {. tl
NB. pad the data out to two or four bytes for various functions
pad4 =: (0 3 2 1&[) {~ 4&|
padding4 =: + pad4
pad2 =: (0 1&[) {~ 2&|
padding2 =: + pad2


NB. Header File Processing
NB. The first 54 bytes are BMP header information followed by a colour table
NB. the colour tables size is:   4 * 2^bit depth
header =: 54 & [ + 4 & [ * 2 & [  ^ 28&{ @ nd @ tl
NB. change the header information so that the image is a RLE or BMP image
toRLE =: 1&}
head2rle =: (30 toRLE @(header {. Nd@tl));header }. nd @ tl
toBMP =: 0&}
head2bmp =: (30 toBMP @ (header {. Nd@tl));header }. nd @ tl


NB. RLE8 -> BMP8
NB. function for processing a file from a RLE encoded image to a BMP image.
rle2bmp =: writing ]`do_decode@.(*@#@tl)^:_ @ head2bmp @ boxed


NB. decode the RLE bit patterns which are either literal or copied
lit =: ({.2&}.)~ {. @ }.
cpy =: {. # {. @ }.
copy =: lit`cpy@.(*@{.)
NB. cut the decoded lines from the data to be processed
chop =: }.~ 2&[ + padding2 @ {. @ }.
trunc =: 2&}.
cut =: chop`trunc@.(*@{.)
NB. place padding bits for 32bit word at the end of the line for a BMP
padit =: padbmp`empty@.((1&{ *@>. 0&{)@tl)
padbmp =: 1&[ #~ pad4 @ getw
empty =: ''&[
NB. encapsulate the processing so that it can be iterated upon
do_decode =: (copy @ tl ,@:(,"1~) hd , padit); cut @ tl


NB. BMP8 -> RLE8
NB. function for processing a file from a BMP image to a RLE encoded image.
bmp2rle =: writing ]`do_encode@.(*@#@tl)^:_ @ head2rle @ boxed
NB. determine the value to match on for a run of data, maximum 255 matches
match =: E.~ {.
matches =: 255 &<. @ i. & 0 @ match
NB. the number of matches at the head and the value matched on
mh =: matches , {.
NB. drop the number of matches from the tail/input data
mt =: }.~ matches
NB. the match head total should be boxed the same as the presented data for iteration
mtotalhd =: (mh @ tl ,@:(,"1~) hd);mt @ tl
inner_loop =: (]`mtotalhd@.(*@#@tl) ^:_)
NB. return the new head of the box
convert_a_line =: 0 0&[ ,"1~ hd,"1 hd@inner_loop@boxw
NB. return the new tail of the box
remove_a_line =:  padding4 @ getw }. tl
NB. encapsulate the processing so that it can be iterated upon
do_encode =: convert_a_line ; remove_a_line
```
