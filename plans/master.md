# Master plan: Vector Rescue

Goal: recover the entire *Vector* archive and republish it, with every old `art` URL (e.g. `/art10500650`) resolving.

## Principles

- Old URLs are the top priority; every design choice is judged against them.
- Never modify originals. Retrieved sources go in a read-only `sources/` area; all work is on derived copies.
- Record provenance for every article: which source it came from, and any conversion applied.
- Overlaps between sources are decided by examining diffs, possibly article by article.

## Phase 0: Retrieve sources (in progress)

- Search the local machine for Vector content (see `plans/survey.md` once written).
- Await Paul Grosvenor's reply on what he can supply: PHP filetree, WordPress DB export, Word documents.
- Other possible sources: Jake Jacob (current editor), Stephen Taylor (PHP site author), Internet Archive snapshots of archive.vector.org.uk and vector.org.uk, nsl.com and other sites that link to `art` URLs.

## Phase 1: Survey (first deliverable)

Produce `plans/survey.md` covering, for each source found:

- location, size, file types, date range, issues covered
- whether article bodies, XML index, images and Word documents are present
- encoding and pre-Unicode APL font risks
- gaps: issues or articles with no source

Also build an inventory of known `art` IDs (from the index, WP export and inbound links) to measure coverage.

## Phase 2: Understand the formats

- Document the old site's structure: index XML schema, XHTML fragment conventions, how the PHP mapped `artNNNNNNNN` to a fragment.
- Document the WordPress schema as exported: posts, slugs, categories, how old article IDs appear, if at all.
- Catalogue Word-document APL encodings (fonts and mappings) found.

## Phase 3: Build the canonical archive

- Define one canonical article record: ID, title, authors, issue, date, body (XHTML, UTF-8), source, provenance.
- Import the old-site articles first.
- Import WP articles and compare against old-site duplicates; produce a diff report and rule on each, per the README.
- Convert Word documents to Unicode APL for articles with no other source (reusing Ian Clark's earlier work where possible), with human review of the APL mappings.

## Phase 4: Generate the site

- Static generator producing pages from the canonical archive, with chrome and navigation replacing the PHP.
- Output keeps `/artNNNNNNNN` paths exactly. The mapping from the old site's other URLs (issue indexes, etc.) is preserved too.
- Include the `johnbutlerassociates.co.uk` URL form if redirects are feasible at the host.

## Phase 5: Hosting decision and publication

Decide after Phase 4, using the output's URL needs:

- GitHub Pages: no server-side redirects; would need a stub page per old URL (extensionless `art…` paths need care).
- Dyalog Gitea: check what it can serve.
- HTTPD on dyalog.com: full control of rewrites and redirects; the likely fallback.
- DNS: the `archive.vector.org.uk` name currently points at WordPress; changing it needs BAA cooperation.

## Phase 6: Verify and hand over

- Test every known old URL, including inbound links collected in Phase 1.
- Document how to rebuild the site and add future material.
- Agree long-term ownership with the BAA.

## Open questions

- Which hosting option? (Phase 5)
- Who controls the vector.org.uk DNS and the WordPress site?
- Licensing and author permissions for republication.
