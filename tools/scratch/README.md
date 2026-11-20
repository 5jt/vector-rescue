# Scratch tools for the First Pass

Ad-hoc helpers used while transcribing from the scans. Not part of the build; not tested.
Run from the project root.

| Tool | Use |
|---|---|
| `todo.py vVnN` | List the stub articles in an issue that still need a scan transcription: `uv run python tools/scratch/todo.py v16n1` |
| `z6.py PDF PAGE x0 y0 x1 y1 out.png` | Crop a 600 dpi render to check glyphs, using coordinates from a 200 dpi page image: `uv run -q --with pillow python tools/scratch/z6.py …` |
| `shot2.py PDF PAGE x0 y0 x1 y1 out.jpg` | Crop a figure at 300 dpi (greyscale JPEG) for `transcriptions/artNNN/` |
| `apldisp.py` | `disp(x)`: draw an APL `]display` box for nested Python lists/strings/ints |
| `dbox.py` | DISP-style boxes: cell = str, list of lines, `('row', cells)` or `('grid', rows)` |
| `matdisp.py` | `]display` boxes for character vectors and matrices of boxed strings |
| `jbox.py` | J-style boxed display of nested lists |

Page images: `pdftoppm -r 200 -png PDF DIR/p` (PDF page = printed page + 2 in most issues).
Keep page images and renders in the Claude session scratchpad, never outside the project and scratchpad: render pages there, and set `VEC_CACHE` to it for `z6.py` and `shot2.py` (they refuse to run without it).

## WordPress (`wordpress/`, #316, #326)

Used to catalogue and convert the vector.org.uk WordPress dump (`surveys/wordpress-survey.md`). Keep the work directory (WORK) in the session scratchpad: the dump and `wp.db` never enter the repository. In order:

| Tool | Use |
|---|---|
| `parse.py DUMP.sql WORK/wp.db` | Content tables only, into SQLite |
| `match.py WORK` | Score each post against the held texts (after `make all`) → `WORK/match.json` |
| `export.py WORK` | Write the 11 new posts' HTML to `WORK/posts/<art ID>.html` |
| `wp2md.py WORK/posts/V.html WORK/md/V.md transcriptions/artV artV` | Convert one post; fetch its images |
| `assemble.py WORK` | Write `transcriptions/art<ID>.md` with front matter and hand fixes. Overwrites the published files: a record, not to be rerun blindly |

`wp2md.py` needs pandoc.
