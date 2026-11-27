The Vector Archive
==================

The archive of *Vector*, the journal of the British APL Association, 1984–2022: every issue's contents, the articles as text, and the scans of the printed issues.

Published at https://britapl.github.io/VectorArchive/

What is here
------------

- `docs/`: the site's pages in Markdown, with the images and the PDF scans they link to
- `overrides/`: Zensical template overrides
- `zensical.toml`: the site configuration, including the navigation
- `scripts/lift_bylines.py`: a step run after the build, setting each article's byline under its title
- `.github/workflows/publish.yml`: builds the site with [Zensical](https://zensical.org) and publishes it to GitHub Pages (run by hand until Pages is enabled; then on every push to `main`)

Generated: do not edit by hand (yet)
------------------------------------

For now this repository is generated. The archive was recovered and transcribed in [5jt/vector-rescue](https://github.com/5jt/vector-rescue), whose pipeline writes everything here; each commit names the vector-rescue commit it was generated from. Edits made here would be overwritten by the next generation. Report corrections as issues instead.

When the recovery work is finished, this repository becomes the archive's single source of truth, vector-rescue is archived, and the pages here are edited directly. This README will then say how.

Building locally
----------------

    pip install zensical==0.0.67
    zensical build
    python scripts/lift_bylines.py site

The site is written to `site/`.
