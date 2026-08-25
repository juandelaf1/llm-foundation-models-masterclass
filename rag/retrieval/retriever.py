"""Recuperación sobre el índice persistido y generación de respuestas grounded.

El recuperador es agnóstico al embedder: carga vectores y metadata del índice.
La respuesta puede generarse en modo offline (composición a partir de los
fragmentos recuperados, con citas) o delegando a un LLM externo. En ambos casos
se exige grounding: si no hay evidencia suficiente, se abstiene.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import numpy as np

from rag.common import Chunk
from rag.config import get_settings


def load_index(index_dir: str | None = None) -> tuple[list[dict], np.ndarray]:
    settings = get_settings()
    idir = Path(index_dir) if index_dir else settings.resolve(settings.index_dir)
    records = json.loads((idir / "chunks.json").read_text(encoding="utf-8"))
    vectors = np.load(idir / "vectors.npy")
    return records, vectors


def _matches(meta: dict, filters: Optional[dict]) -> bool:
    if not filters:
        return True
    for key, allowed in filters.items():
        val = meta.get(key, "")
        if isinstance(allowed, (list, tuple, set)):
            if str(val) not in {str(a) for a in allowed}:
                return False
        else:
            if str(allowed).lower() not in str(val).lower():
                return False
    return True


def retrieve(query_embedding: np.ndarray, top_k: int = 5,
             filters: Optional[dict] = None, index_dir: str | None = None) -> list[dict]:
    records, vectors = load_index(index_dir)
    sims = vectors @ query_embedding
    order = np.argsort(-sims)
    results = []
    for i in order:
        rec = records[int(i)]
        if not _matches(rec.get("metadata", {}), filters):
            continue
        results.append({**rec, "score": float(sims[int(i)])})
        if len(results) >= top_k:
            break
    return results


def query_has_evidence(results: list[dict], threshold: float = 0.08) -> bool:
    """Criterio de abstinencia: sin fragmentos relevantes -> no hay evidencia."""
    return bool(results) and max(r["score"] for r in results) >= threshold
