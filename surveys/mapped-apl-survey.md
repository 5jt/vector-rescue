# Survey: mapped APL in the held-back articles

Surveyed by Claude on 2026-10-02 for issue #33. Sources were read, never changed.

Before Unicode, APL was typed in fonts that put APL glyphs at the codes of ordinary characters. A Web page set in such a font looked right only with the font installed; its text, read as Windows-1252 (or later converted to UTF-8 as if it were), holds `Œ` for `⎕`, `„` for `←`, `½` for `⍴`. 94 articles are held back for this (68 listed in the old site's `tools/codingprobs.txt`, 18 naming APL fonts, 8 found by the converter's heuristic); dueren113 is held separately for its encoding.

## Short answers

1. **One mapping covers nearly everything: APL2741.** About 85 of the 94 articles declare APL2741 or APLSans (or use their codes without declaring them). The two fonts share one layout; only codes `FD` and `FF` differ.
2. **The fonts themselves are in the recovered tree** (`resource/apl2741.zip`, `apl2741a.ttf`, `aplsans.zip`), so the mapping comes from the glyphs, not from memory: charts of every glyph were rendered and read, and each code checked against how the articles use it. Result: `mappings/apl2741.tsv`, 88 codes, 75 of high confidence (A1, A5, D0, F0, FF confirmed by Stephen Taylor), 11 medium, 2 low. The rest are listed for investigation in #34.
3. **APL2741 changes only codes above 0x7F.** ASCII is untouched (its letters are merely italic).
4. **Mapped text survives in three states,** all recoverable with the same table:
   - Windows-1252 bytes (most cp1252 files: `„` at 0x84 is ←);
   - mapped bytes already turned into Unicode code points by an earlier conversion that treated them as Windows-1252 (UTF-8 files such as `barman.htm`: `Œio„0` is `⎕io←0`);
   - partial conversions by Ian Clark's VARCH tool, where most APL is Unicode but some characters were missed or mistranslated (`mcintyre104_18`: box-drawing `Ú⍲⍲⍲Â` should be `┌───┬`).
5. **The mapping must apply only in APL contexts** (text set in an APL font, `pre`, `tt`, `code`, or classed APL), never in prose, where `é` is an `é`.
6. **Five bytes are undefined in Windows-1252** (81, 8D, 8F, 90, 9D); two are APL2741 symbols (81 `⊣`, 8D `⍞`, 8F `⍙`, 90 `⍫`). The decoder must keep their identity for mapped articles rather than turn them into U+FFFD.

## Fonts in the recovered tree

| Font | File | Kind |
|---|---|---|
| APL2741 | `resource/apl2741.zip` (TrueType), `apl2741a.ttf`, `apl2741p/x` (Type 1) | Mapped: symbol font, APL glyphs at 0x80–0xFF |
| APLSans | `resource/aplsans.zip` | Mapped: same layout as APL2741 except `FD`, `FF` |
| APL385 Unicode | `Apl385.ttf`, `resource/apl385.ttf` | Unicode (not mapped); used for the site's code |
| kapl, jsans | `resource/kapl.ttf`, `jsans.ttf` | K and J fonts (not examined) |
| APLX Upright, APLNet, VectorAPL, ISIAPL | — | Named by 1–2 articles each; not in the tree |

## The held articles, by state

| Group | Articles | What they hold | Approach |
|---|---:|---|---|
| A. APL2741 bytes, assignment at 0x84 | 30 | APL2741 throughout their code | Map |
| B. APL font named, little or no APL seen | 41 | News items and short pieces; some (UTF-8, e.g. `barman.htm`, `dy82.htm`) hold mapped characters as Unicode code points; others may hold none | Map where present; release where there is nothing to map |
| C. Unicode APL already (VARCH and later) | 22 | Mostly correct; residual mapped characters, box-drawing mistranslations | Map residues; review |
| D. `«` where ← was expected | 1 (`kai213`) | On inspection, APL2741 too: ← is at `84` (72 uses); `«` (`AB`) is ⍬ (`MySheet.PrintOut ⍬`) | Map with APL2741 |

Exact lists: run the survey script in the issue (#33) against `build/skipped.json`.

## The APL2741 table

`mappings/apl2741.tsv`: byte, the character it becomes as Windows-1252, the APL character, Unicode code and name, confidence, evidence.

Codes still uncertain (now tracked in #34, with the other mappings):

| Code | Reading | Why uncertain |
|---|---|---|
| `CB` | `∪`? | Glyph resembles ∪, which is also at 9E |
| `FD` | `⍣`? | Three dots in APL2741, ý in APLSans; in De Kerf `→(ý/R)/LAB` suggests ∨, from another font |
| `D2`–`D5` | duplicates of `8C`–`8F` | Same glyphs at two codes |

## Plan

Convert one representative of each state for review (#33), then the rest:

1. Group A: `dan.htm` (16:2, Windows-1252, APL2741 in `<font>` around `pre` and `code`).
2. Group B: `barman.htm` (15:3, UTF-8 holding mapped characters as code points).
3. Group C: `mcintyre104_18.htm` (10:4, VARCH conversion with box-drawing residue).
4. `kai213.htm` (21:3), which confirmed `AB` as ⍬.

The mapping is chosen per article in `corrections.yaml` (`apl: apl2741`), which also releases it from the hold, so every choice is visible and reviewable.

## After review (2026-10-02)

- The four representatives were reviewed by Stephen Taylor: "The converted sections look right."
- Langlet's *Paritons and Cognitons* uses another mapping (ISIAPL or VectorAPL fonts, neither in the tree); it stays held (#34).
- The site's APL font is now APL387 Unicode (`site/assets/fonts/APL387.ttf`, public domain), a later version of APL385 Unicode.
