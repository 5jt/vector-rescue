"""Write the post_content of WordPress posts to WORK/posts/<art ID>.html.

usage: export.py WORK
IDS maps WordPress post ID to art ID (surveys/wordpress-survey.md)."""
import sqlite3, sys
from pathlib import Path

S = Path(sys.argv[1])
IDS = {170: '10501790', 763: '10501800', 965: '10501810', 1458: '10501820', 1496: '10501830', 1966: '10501840',
       2041: '10501850', 2240: '10501860', 2293: '10501870', 2473: '10501880', 2666: '10501890'}
db = sqlite3.connect(S / 'wp.db')
(S / 'posts').mkdir(exist_ok=True)
for pid, vid in IDS.items():
    c, = db.execute("select post_content from wp_posts where ID=?", (pid,)).fetchone()
    (S / 'posts' / f'{vid}.html').write_text(c, encoding='utf-8')
print(len(IDS), "posts written")
