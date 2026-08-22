from collections import Counter
import pytest
from xpol import Frame, Sampler

PROBLEM = "A neural network overfits; want a new regularisation idea."


@pytest.fixture(scope="module")
def sampler():
    return Sampler(Frame())


def test_frame_levels(sampler):
    st = sampler.frame.stats()
    assert st["domain"] == 4 and st["field"] == 26 and st["topic"] > 4000 and st["keyword"] > st["topic"]


def test_seed_is_reproducible(sampler):
    a, ra = sampler.sample(k=10, seed=123)
    b, rb = sampler.sample(k=10, seed=123)
    assert [s.name for s in a] == [s.name for s in b] and ra["seed"] == 123


def test_os_entropy_when_no_seed(sampler):
    _, ra = sampler.sample(k=3)
    _, rb = sampler.sample(k=3)
    assert ra["seed"] != rb["seed"]


def test_stratified_draw_spreads_domains(sampler):
    seeds, _ = sampler.sample(k=40, seed=1, stratify="domain")
    c = Counter(s.stratum for s in seeds)
    assert len(c) == 4 and max(c.values()) - min(c.values()) <= 1


def test_no_duplicates(sampler):
    seeds, _ = sampler.sample(k=200, seed=5, stratify="none")
    assert len({s.name for s in seeds}) == 200


def test_band_and_home_exclusion(sampler):
    seeds, rec = sampler.sample(k=6, seed=9, problem=PROBLEM, band=(0.5, 0.9))
    assert rec["home"]["field"] == "Computer Science"
    for s in seeds:
        assert 0.5 <= s.distance_pct <= 0.9
        assert not s.path.startswith(f"{s.path.split(' > ')[0]} > Computer Science")


def test_band_requires_problem(sampler):
    with pytest.raises(ValueError):
        sampler.sample(k=2, band=(0.1, 0.2))


def test_keyword_level_carries_parent(sampler):
    seeds, _ = sampler.sample(k=5, seed=3, level="keyword")
    for s in seeds:
        assert s.level == "keyword" and s.path.count(" > ") == 4 and s.description
