"""Motor de consulta del RAG: une recuperación y generación.

Expone `ask()` usado tanto por la CLI como por la app Streamlit. Soporta
filtros por metadata (provider, model_family, course_section, difficulty...)
para los modos "investigar modelo" y "comparar".
"""
from __future__ import annotations

from typing import Optional

import numpy as np

from rag.config import get_settings
from rag.retrieval.embeddings import TfidfEmbedder, build_embedder, expand_query
from rag.retrieval.llm import build_generator
from rag.retrieval.retriever import query_has_evidence, retrieve


def _distinctive_overlap(query: str, results: list[dict], embedder) -> bool:
    """Puerta de abstinencia: la consulta debe compartir al menos un token
    *distintivo* (alta IDF) con el fragmento superior. Los tokens muy frecuentes
    en el corpus (verbos/comodines) no cuentan, para evitar similitud espuria.
    """
    if not results:
        return False
    q_tokens = TfidfEmbedder._tokenize(query)
    vocab, idf = getattr(embedder, "_vocab", {}), getattr(embedder, "_idf", None)
    distinctive = set()
    if vocab and idf is not None:
        threshold = 1.5
        for t in q_tokens:
            if t in vocab and idf[vocab[t]] >= threshold:
                distinctive.add(t)
    else:
        distinctive = set(q_tokens)
    if not distinctive:
        return False
    doc_tokens = set()
    for r in results:
        doc_tokens |= set(TfidfEmbedder._tokenize(r["text"]))
    return bool(distinctive & doc_tokens)


def ask(query: str, top_k: int = 5, filters: Optional[dict] = None,
        index_dir: str | None = None) -> dict:
    settings = get_settings()
    embedder = build_embedder(index_dir=index_dir)
    expanded = expand_query(query)
    q_vec = embedder.embed([expanded])[0]
    results = retrieve(np.asarray(q_vec, dtype=np.float32), top_k=top_k,
                       filters=filters, index_dir=index_dir)
    if not (query_has_evidence(results) and _distinctive_overlap(expanded, results, embedder)):
        results = []  # abstinencia: sin evidencia suficiente
    generator = build_generator()
    out = generator.answer(query, results)
    out["query"] = query
    out["filters"] = filters or {}
    out["num_retrieved"] = len(results)
    return out
