"""Assemble transcriptions/art<ID>.md for the 11 WordPress articles (#316).

usage: assemble.py WORK (run from the project root)
OVERWRITES the published transcriptions, including any edits made since
2026-11-19: a record of how they were made, not to be rerun blindly."""
import re, sys, yaml, sqlite3

S = sys.argv[1]
db = sqlite3.connect(S + '/wp.db')
date = lambda id: db.execute("select substr(post_date,1,10) from wp_posts where ID=?", (id,)).fetchone()[0]


def body(v):
    return open(f'{S}/md/{v}.md').read()


def sub(b, pairs):
    for a, c in pairs:
        assert a in b, a
        b = b.replace(a, c)
    return b


LOST = "*[Figure lost: the image file is no longer on vector.org.uk and no copy has been found.]*"
A = {}

b = sub(body('10501790'), [("\n\n*The autumn", "\n\nThe autumn"), ("news).*", "news).")])
A['10501790'] = (170, "APL Germany Autumn Meeting", ["Stephen Taylor"], ["APL community"], b,
                 ["A two-line notice, posted in category In Press; the meeting’s date is not given."])

b = sub(body('10501800'), [
    ("'f.SF'?WC'SubForm' (sz?size-", "'f.SF'⎕WC'SubForm' (sz←size-"),
    ("[919] botright?'Attach'", "[919] botright←'Attach'"),
    ("[71] sz?abc+123 ? add 123 to abc", "[71] sz←abc+123 ⍝ add 123 to abc"),
    ("a delta (?)", "a delta (∆)"),
    ("this is regular code ? This is a comment", "this is regular code ⍝ This is a comment"),
    ("| `?` | a lamp symbol |", "| `⍝` | a lamp symbol |"),
    ("|?.*$)?", "|⍝.*$)?"),
    ("(?i:??|?|??|?|", "(?i:⍺⍺|⍺|⍵⍵|⍵|"),
    ("(?<![?0-9a-z_??])[a-z_??][a-z_??0-9]*))?¯?\\d+", "(?<![⎕0-9a-z_∆⍙])[a-z_∆⍙][a-z_∆⍙0-9]*))←¯?\\d+")])
A['10501800'] = (763, "Finding text in files", ["Dan Baronet"], ["programming techniques", "data and files"], b, [
    "WordPress lost the post’s APL characters in some code samples and one table row, storing each as “?” (the live page shows them so). Restored where the syntax leaves no doubt: ← in the assignments `sz←size-…`, `botright←'Attach'…` and `sz←abc+123`; ⍝ for the comment and the lamp in the regular expressions and the table; `⎕WC`; the delta “(∆)”; and the last regular expression, which repeats the one given correctly earlier in the article, with ← before `¯?\\d+` (“assignment of a number”).",
    "Not restored: the rows of “?” under the matches in the two `]find` outputs (`????????` under botright, `??? ???` under abc), probably markers of the matched text, and their column positions; left as the post has them.",
    "WordPress also double-escaped < in the regular expressions (`(?&lt;!`); shown as <.",
    "The post’s first line, “User commands ]FIND and ]REPLACE in Dyalog APL with regular expressions”, is kept as its opening line."])

b = body('10501810').replace("![](https://vector.org.uk/wp-content/uploads/2019/04/figure1.png)", LOST)
b = re.sub(r"\[\\\[(\d+)\\\]\]\(#ref\)", r"[\1]", b)
A['10501810'] = (965, "Reflections on Langlet’s APL Theory of Human Vision", ["Stuart Smith"],
                 ["mathematics and statistics", "APL in perspective"], b, [
    "The first figure, from Langlet’s presentation (`2019/04/figure1.png`), is lost: vector.org.uk no longer serves it and the Wayback Machine has no copy. Jake Jacob’s copy of the site’s uploads may have it.",
    "References in the text linked to an anchor (#ref) the post lacks; shown as plain numbers."])

b = sub(body('10501820'), [
    ("*Nicolas Delcros*\n\n", ""),
    ("- ![](art10501820/Kamakura_Budda_Daibutsu_front_1885-768x1024.jpg)\n  Buddha Daibutsu, Kamakura",
     "![Buddha Daibutsu, Kamakura](art10501820/Kamakura_Budda_Daibutsu_front_1885-768x1024.jpg)\n\n*Buddha Daibutsu, Kamakura*")])
A['10501820'] = (1458, "Making images and videos of the Buddhabrot", ["Nicolas Delcros"], ["graphics", "mathematics and statistics"], b,
                 ["The byline at the head of the post is the author’s name; WordPress records him as “Nicholas Delcros”, the post as Nicolas."])

A['10501830'] = (1496, "APLX is out, long live APL", ["Dan Baronet"], ["development practice", "implementations"], body('10501830'), [])

b = sub(body('10501840'), [
    ("*by Adám Brudzewsky, Jay Foad & Roger Hui*\n\n", ""),
    ("""      (0 4⍴'a')cmp(4 0⍴0) ←→ (4 4⍴β)cmp(4 4⍴β) ←→ 0

  This is incorrect if the original arrays do not match.""",
     """    ```
    (0 4⍴'a')cmp(4 0⍴0) ←→ (4 4⍴β)cmp(4 4⍴β) ←→ 0
    ```

    This is incorrect if the original arrays do not match."""),
    ("""            'short' cmp 'sesquipedalian'
      1
            1 2 3 cmp 1 2 3 ¯4 ¯5
      ¯1
            (x⍪8) cmp (x,8) ⊣ x←2 2⍴1 2 3 4
      ¯1""",
     """    ```
          'short' cmp 'sesquipedalian'
    1
          1 2 3 cmp 1 2 3 ¯4 ¯5
    ¯1
          (x⍪8) cmp (x,8) ⊣ x←2 2⍴1 2 3 4
    ¯1
    ```""")])
A['10501840'] = (1966, "TAO Axioms", ["Adám Brudzewsky", "Jay Foad", "Roger Hui"], ["language design"], b, [
    "Byline from the head of the post (“by Adám Brudzewsky, Jay Foad & Roger Hui”); WordPress records only Hui and Brudzewsky as authors.",
    "The definition of `cmp` is a borderless HTML table in the post; kept as a table."])

A['10501850'] = (2041, "The doctor and the doc", ["Stephen Taylor"], ["APL in perspective", "development practice"], body('10501850'), [])

b = body('10501860')
b = b[:b.index("## Table of Contents")] + b[b.index("## Introduction"):]
b = sub(b, [("![pivot](https://vector.org.uk/wp-content/uploads/2020/09/pivotWithTotal.png)", LOST)])
A['10501860'] = (2240, "Powerful CSV processing with kdb+", ["Ferenc Bodon"], ["data and files", "performance"], b, [
    "Converted from the post as published. The post also keeps an earlier Markdown source, which lacks the section “Selecting columns, filtering, sorting”.",
    "The post’s table of contents is left out: the page has its own, and its links depended on WordPress’s heading anchors.",
    "The figure of the pivot table with totals (`2020/09/pivotWithTotal.png`) is lost: vector.org.uk no longer serves it and the Wayback Machine has no copy."])

b = re.sub(r"^(#{1,5}) ", lambda m: "#" + m.group(1) + " ", body('10501870'), flags=re.M)
A['10501870'] = (2293, "Book review — Fun Q: A Functional Introduction to Machine Learning in Q", ["Daniel Krizian"],
                 ["reviews", "mathematics and statistics"], b, [
    "The post names no reviewer; WordPress records Nick Psaris (the book’s author) and Daniel Krizian as authors. Daniel Krizian is taken to be the reviewer: to be confirmed.",
    "The post’s headings are one level higher than the page allows; each is lowered by one."])

A['10501880'] = (2473, "A Vendor-Agnostic Logo for APL", ["Adám Brudzewsky"], ["APL community", "graphics"], body('10501880'),
                 ["In the post the figures float beside the text, alternately left and right; here each follows its paragraph, with its caption below."])

A['10501890'] = (2666, "Hacker’s Corner: JPEG_Comments", ["Nicholas Small"], ["programming techniques", "data and files"], body('10501890'), [
    "Title: the post’s is “HackersCorner - JPEG_Comments”; given here in the form of Vector’s earlier Hacker’s Corner titles.",
    "Kept as written: “The Exit data is indexed” (for Exif); the search key `'99CC'` in line [3], where the text says the row starts with 0x9C9C."])

IN_PRESS = (170, 763, 965, 1458, 1496, 1966)
for v, (pid, title, authors, tags, b, queries) in A.items():
    fm = {"vid": v, "title": title, "authors": authors, "online": date(pid), "in_press": True,
          "added": f"WordPress post {pid} (category {'In Press' if pid in IN_PRESS else 'Volume 27, No. 1'}), from the database dump of 2026-11-17 (#316)",
          "transcribed": f"converted from the HTML of vector.org.uk WordPress post {pid}, images from vector.org.uk; Claude, 2026-11-19",
          "review": "draft", "tags": tags}
    if queries:
        fm["queries"] = queries
    open(f'transcriptions/art{v}.md', 'w').write("---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=10000)
                                                  + "---\n\n" + b.strip() + "\n")
print(len(A), "written")
