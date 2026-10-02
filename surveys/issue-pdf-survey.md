# Survey: article text from the issue PDFs

Surveyed by Claude on 2026-10-02 for issue #37. The PDFs are the whole-issue copies published on vector.org.uk and captured by the Wayback Machine (`sources/wayback/vector.org.uk/wp-content/uploads/`), plus the PHP tree's own `issues/` PDFs.

## Short answers

1. **The PDFs are scans with an OCR text layer**, made with Ghostscript; their single font, `GlyphLessFont`, is the mark of Tesseract OCR. Every issue PDF checked (vols 1–26) is of this kind, except the PHP-era PDFs for vols 24–26, which are typeset.
2. **The OCR prose is readable but not publishable as it stands.** Words run together ("notreally", "Thisis", "Thefailed"), and there are character errors ("1 do think" for "I do think", "APL'PLUS Il" for "APL*PLUS II").
3. **APL does not survive the OCR.** `3 20 FTAIL F` comes out as `3°20 FYAIL F`; APL symbols become `°` or are lost. OCR text is no substitute for the articles' code.
4. **Printed pages can be found in the PDFs.** Each issue's printed page numbers can be read from the OCR; the offset between PDF page and printed page is constant within an issue (2 for most volumes, 4 for 22:4 and 23, 0 for the typeset vols 24–26) and was found for all 94 issue PDFs.
5. **The index's page numbers lead to the article.** Of the 869 index records with no text, 818 are in an issue with a PDF. For 757 of them (93%) the title appears on exactly the computed page, and for 20 more on an adjacent page; 41 did not match, mostly because the OCR garbled the title or the title is generic ("Letters", "Sustaining Members' News").

## Proposal

**A page for every indexed article.** Today the 869 records without text have no `art` page, so their old URLs lead nowhere. Each can have a page with its title, authors, issue and page, a note that its text is not yet online, and a link that opens the issue PDF at the article's first page (`…pdf#page=N`). This makes every `art` URL in the index resolve, the project's first priority, and gives readers the article at once.

The 51 records in issues without a PDF (2:2 and 7:2 never captured; 3:4, 7:4, 16:4 truncated) get the same page without the link.

**OCR text later, if at all.** The OCR could be offered as unedited, searchable text, clearly labelled, or used as a starting point for transcription. It should not be presented as the article: its APL is wrong. That is an editorial decision for later.

## Not checked

- The 41 records whose title was not found near the computed page: wrong page number in the index, OCR errors, or an article that starts mid-page.
- Whether the PDFs from vector.org.uk for vols 1–21 contain every page (page counts are 128–162; no gaps were looked for).
