"""Issue #23: curated corrections for source defects.

Defects that need human judgement are corrected here, not guessed at by
converter rules: corrections.yaml lists, per article, text replacements
applied to the decoded source before parsing, an encoding override, or a
decision to hold back or release an article; and corrections to the issue
catalogue. Every entry says why and who decided. A replacement whose text
is no longer found is reported as stale.
"""

import re
from pathlib import Path

import yaml


class CorrectionError(ValueError):
    pass


def _check(entry, where):
    for k in ("why", "decided"):
        if not entry.get(k):
            raise CorrectionError(f"{where}: every correction needs '{k}'")


class Corrections:
    def __init__(self, data=None):
        data = data or {}
        self.articles = {str(k): v for k, v in (data.get("articles") or {}).items()}
        self.catalogue = {str(k): v for k, v in (data.get("catalogue") or {}).items()}
        for vid, entries in self.articles.items():
            for e in entries:
                _check(e, f"article {vid}")
        for key, e in self.catalogue.items():
            _check(e, f"issue {key}")

    @classmethod
    def from_text(cls, text):
        return cls(yaml.safe_load(text))

    @classmethod
    def load(cls, path):
        path = Path(path)
        return cls.from_text(path.read_text(encoding="utf-8")) if path.is_file() else cls()

    def _entries(self, vid, key):
        return [e for e in self.articles.get(str(vid), []) if key in e]

    def apply_text(self, vid, text, notes):
        for e in self._entries(vid, "find"):
            find, new, nth = e["find"], e.get("replace", ""), e.get("nth")
            if nth:  # only the nth occurrence
                parts = text.split(find)
                if len(parts) > nth:
                    text = find.join(parts[:nth]) + new + find.join(parts[nth:])
                    notes.append({"kind": "corrected", "why": e["why"], "decided": e["decided"]})
                    continue
            elif find in text:
                text = text.replace(find, new, e.get("count", -1))
                notes.append({"kind": "corrected", "why": e["why"], "decided": e["decided"]})
                continue
            notes.append({"kind": "correction-stale", "find": find})
        return text

    def encoding(self, vid):
        found = self._entries(vid, "encoding")
        return found[0]["encoding"] if found else None

    def held(self, vid):
        found = [e for e in self._entries(vid, "hold") if e["hold"]]
        return found[0]["why"] if found else None

    def released(self, vid):
        return any(e["release"] for e in self._entries(vid, "release")) or bool(self.apl(vid))

    def boxes(self, vid):
        """How to repair an article's box drawings, if they need it."""
        found = self._entries(vid, "boxes")
        return found[0]["boxes"] if found else None

    def apl(self, vid):
        """The mapping table for an article's APL, if it was typed in a mapped font."""
        found = self._entries(vid, "apl")
        return found[0]["apl"] if found else None

    def apply_catalogue(self, issues):
        issues = [dict(i) for i in issues]
        by = {(i["volume"], i["issue"]): i for i in issues}
        for key, e in self.catalogue.items():
            vol, no = key.split(":")
            issue = by.get((vol, no))
            if issue is None:
                issue = {"volume": vol, "issue": no, "year": None, "month": None, "title": None,
                         "span": 1, "numbers": [no], "pdf": None, "doc": None}
                issues.append(issue)
                by[(vol, no)] = issue
            for k in ("year", "month", "title", "pdf", "doc"):
                if k in e:
                    issue[k] = e[k]
            if "title" in e and re.match(r"Nos?\.", e["title"]):
                issue["numbers"] = re.findall(r"\d+", e["title"])
                issue["span"] = len(issue["numbers"])
        return issues
