"""Embeddings for distance-banded sampling. CPU by default — the sampler must
work on a shared box; 4.5k short texts take well under a minute."""
from __future__ import annotations

import os
from pathlib import Path

import numpy as np

MODEL = os.environ.get("XPOL_EMBED_MODEL", "BAAI/bge-small-en-v1.5")
CACHE = Path(__file__).resolve().parent.parent / "data" / "topic_embeddings.npy"

_model = None


def _get_model():
    global _model
    if _model is None:
        os.environ.setdefault("HF_HOME", os.path.expanduser("~/projects/.cache/huggingface"))
        os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")
        os.environ.setdefault("TRANSFORMERS_VERBOSITY", "error")
        from sentence_transformers import SentenceTransformer
        _model = SentenceTransformer(MODEL, device=os.environ.get("XPOL_DEVICE", "cpu"))
    return _model


def embed(texts: list[str]) -> np.ndarray:
    v = _get_model().encode(texts, normalize_embeddings=True, batch_size=64,
                            show_progress_bar=False)
    return np.asarray(v, dtype=np.float32)


def topic_embeddings(frame, cache: Path = CACHE) -> np.ndarray:
    if cache.exists():
        arr = np.load(cache)
        if arr.shape[0] == len(frame.topics):
            return arr
    arr = embed([t.text() for t in frame.topics])
    cache.parent.mkdir(parents=True, exist_ok=True)
    np.save(cache, arr)
    return arr
