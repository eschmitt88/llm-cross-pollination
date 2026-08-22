"""The sampler. Randomness is external to the model (OS entropy or a logged
seed); stratification keeps a batch spread across domains; an optional
distance band restricts the population to "far but not too far" from a
problem statement — the RNG still picks within the band."""
from __future__ import annotations

import secrets
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict

import numpy as np

from .frame import Frame, Entry, LEVELS


@dataclass
class Seed:
    level: str
    name: str
    path: str
    description: str
    keywords: list[str]
    distance: float | None      # cosine distance to the problem, if given
    distance_pct: float | None  # percentile of that distance within the population
    stratum: str


class Sampler:
    def __init__(self, frame: Frame | None = None):
        self.frame = frame or Frame()
        self._emb = None

    # ------------------------------------------------------------------ core
    def sample(self, k: int = 5, level: str = "topic", seed: int | None = None,
               stratify: str | None = "domain", problem: str | None = None,
               band: tuple[float, float] | None = None, exclude_home: bool = True,
               exclude_fields: list[str] | None = None) -> tuple[list[Seed], dict]:
        """Return k seeds plus a record of exactly how they were drawn."""
        if level not in LEVELS:
            raise ValueError(f"level must be one of {LEVELS}")
        if seed is None:
            seed = secrets.randbits(63)
        rng = np.random.default_rng(seed)
        pop = self.frame.entries(level)

        record = {"seed": seed, "level": level, "k": k, "stratify": stratify,
                  "population": len(pop), "band": band, "exclude_home": exclude_home}

        dist = pct = None
        home = {}
        if problem:
            pvec = self._embed_problem(problem)
            emb = self._topic_emb()
            dist_topic = 1.0 - emb @ pvec                      # cosine distance per topic
            dist = np.array([dist_topic[e.idx] for e in pop])  # inherit parent topic's distance
            order = dist.argsort()
            pct = np.empty(len(pop)); pct[order] = np.linspace(0, 1, len(pop))
            near = [self.frame.topics[i] for i in dist_topic.argsort()[:10]]
            home = {"field": Counter(t.field for t in near).most_common(1)[0][0],
                    "subfield": Counter(t.subfield for t in near).most_common(1)[0][0],
                    "nearest_topics": [t.name for t in near[:5]]}
            record["home"] = home

        mask = np.ones(len(pop), dtype=bool)
        if problem and exclude_home and level != "domain":
            mask &= np.array([e.field != home["field"] for e in pop])
        if exclude_fields:
            ex = {f.lower() for f in exclude_fields}
            mask &= np.array([e.field.lower() not in ex and e.name.lower() not in ex for e in pop])
        if band is not None:
            if pct is None:
                raise ValueError("band requires a problem statement to measure distance from")
            lo, hi = band
            mask &= (pct >= lo) & (pct <= hi)
        idx_all = np.flatnonzero(mask)
        if len(idx_all) < k:
            raise ValueError(f"only {len(idx_all)} candidates after filtering; loosen band/exclusions")
        record["eligible"] = int(len(idx_all))

        chosen = self._draw(idx_all, pop, k, rng, stratify)
        seeds = []
        for i in chosen:
            e = pop[i]
            seeds.append(Seed(
                level=e.level, name=e.name, path=e.path,
                description=(e.description or self._parent_desc(e)),
                keywords=(e.keywords or self._parent_keywords(e))[:6],
                distance=None if dist is None else round(float(dist[i]), 4),
                distance_pct=None if pct is None else round(float(pct[i]), 3),
                stratum=getattr(e, stratify) if stratify and stratify != "none" else "",
            ))
        return seeds, record

    # --------------------------------------------------------------- helpers
    def _draw(self, idx_all, pop, k, rng, stratify):
        if not stratify or stratify == "none":
            return list(rng.choice(idx_all, size=k, replace=False))
        groups = defaultdict(list)
        for i in idx_all:
            groups[getattr(pop[i], stratify)].append(i)
        names = sorted(groups)
        # round-robin over strata in a random order, uniform within stratum
        chosen, used = [], set()
        order = list(rng.permutation(names))
        j = 0
        while len(chosen) < k:
            g = groups[order[j % len(order)]]
            avail = [i for i in g if i not in used]
            if avail:
                pick = int(rng.choice(avail))
                chosen.append(pick); used.add(pick)
            j += 1
            if j > 10 * k * len(order):
                break
        return chosen

    def _topic_emb(self):
        if self._emb is None:
            from .embed import topic_embeddings
            self._emb = topic_embeddings(self.frame)
        return self._emb

    def _embed_problem(self, problem: str):
        from .embed import embed
        return embed([problem])[0]

    def _parent_desc(self, e: Entry) -> str:
        if e.level == "keyword":
            return self.frame.topics[e.idx].description
        return ""

    def _parent_keywords(self, e: Entry) -> list[str]:
        return self.frame.topics[e.idx].keywords if e.idx >= 0 else []


def seeds_to_dicts(seeds: list[Seed]) -> list[dict]:
    return [asdict(s) for s in seeds]
