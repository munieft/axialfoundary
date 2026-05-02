from __future__ import annotations

import json
import math
from pathlib import Path
from typing import List

from django.conf import settings


_chunks: list[str] | None = None
_embeddings: list[list[float]] | None = None
_norms: list[float] | None = None


def _load() -> None:
    """Load the JSON-cached chunks + embeddings on first use."""
    global _chunks, _embeddings, _norms
    if _chunks is not None:
        return
    path = Path(settings.CHROMA_DB_PATH) / 'embeddings.json'
    if not path.exists():
        _chunks, _embeddings, _norms = [], [], []
        return
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    _chunks = list(data.get('chunks') or [])
    _embeddings = [list(v) for v in (data.get('embeddings') or [])]
    _norms = [math.sqrt(sum(x * x for x in v)) or 1.0 for v in _embeddings]


def retrieve(query: str, top_k: int = 4) -> List[str]:
    """Embed the query via Gemini and return the top_k most similar chunks (cosine)."""
    _load()
    if not _chunks or not _embeddings:
        return []

    from .embedder import embed_query

    try:
        q = embed_query(query)
    except Exception:
        # If embedding fails (network, quota, etc.), fall back to no context — the
        # prompt still answers gracefully via its "I don't have details" rule.
        return []

    q_norm = math.sqrt(sum(x * x for x in q)) or 1.0

    # Cosine similarity in pure Python — fast enough for KBs up to a few thousand chunks.
    scored: list[tuple[float, int]] = []
    for i, vec in enumerate(_embeddings):
        dot = 0.0
        for a, b in zip(q, vec):
            dot += a * b
        sim = dot / (q_norm * _norms[i])
        scored.append((sim, i))

    scored.sort(key=lambda t: t[0], reverse=True)
    return [_chunks[i] for _, i in scored[:top_k]]
