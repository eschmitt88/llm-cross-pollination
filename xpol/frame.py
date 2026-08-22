"""Sampling frame: the OpenAlex topic taxonomy (domain > field > subfield >
topic > keyword). The frame is explicit and finite so that "uniform" means
something and so the model's own picks can be compared against it."""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

LEVELS = ("domain", "field", "subfield", "topic", "keyword")
DATA = Path(__file__).resolve().parent.parent / "data" / "openalex_topics.json"


@dataclass
class Entry:
    level: str
    name: str
    domain: str
    field: str
    subfield: str
    topic: str | None = None          # parent topic for keyword-level entries
    description: str = ""
    keywords: list[str] = field(default_factory=list)
    works_count: int = 0
    idx: int = -1                     # row in the topic table (for embeddings)

    @property
    def path(self) -> str:
        parts = [self.domain, self.field, self.subfield]
        if self.level in ("topic", "keyword"):
            parts.append(self.topic or self.name)
        if self.level == "keyword":
            parts.append(self.name)
        return " > ".join(parts)

    def text(self) -> str:
        """Text used for embedding."""
        if self.level == "keyword":
            return f"{self.name} ({self.topic}; {self.subfield})"
        if self.level == "topic":
            return f"{self.name}. {self.description} Keywords: {', '.join(self.keywords[:8])}."
        return f"{self.name} ({self.level} of {self.domain})"


class Frame:
    def __init__(self, path: Path = DATA):
        raw = json.loads(Path(path).read_text())
        self.topics: list[Entry] = [
            Entry("topic", t["name"], t["domain"], t["field"], t["subfield"],
                  topic=t["name"], description=t["description"],
                  keywords=t["keywords"], works_count=t["works_count"], idx=i)
            for i, t in enumerate(raw)
        ]

    def entries(self, level: str) -> list[Entry]:
        if level == "topic":
            return self.topics
        if level == "keyword":
            out, seen = [], set()
            for t in self.topics:
                for k in t.keywords:
                    key = (k.lower(), t.name)
                    if key in seen:
                        continue
                    seen.add(key)
                    out.append(Entry("keyword", k, t.domain, t.field, t.subfield,
                                     topic=t.name, idx=t.idx))
            return out
        # coarse levels: one entry per distinct name, idx = first topic under it
        out, seen = [], {}
        for t in self.topics:
            name = getattr(t, level)
            if name in seen:
                seen[name].works_count += t.works_count
                continue
            e = Entry(level, name, t.domain, t.field if level != "domain" else "",
                      t.subfield if level == "subfield" else "", idx=t.idx)
            e.works_count = t.works_count
            seen[name] = e
            out.append(e)
        return out

    def stats(self) -> dict:
        return {lvl: len(self.entries(lvl)) for lvl in LEVELS}
