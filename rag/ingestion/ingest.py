"""Ingesta reproducible del corpus de conocimiento.

Lee `knowledge/`, trocea los documentos, genera embeddings (TF-IDF offline por
defecto) y persiste el índice en `rag/.index/`. Reejecutar tras añadir o
actualizar documentos de knowledge/.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from rag.common import chunk_document, load_knowledge_dir
from rag.config import get_settings
from rag.retrieval.embeddings import build_embedder


def run(knowledge_dir: str | None = None, index_dir: str | None = None) -> dict:
    settings = get_settings()
    kdir = Path(knowledge_dir) if knowledge_dir else settings.resolve(settings.knowledge_dir)
    idir = Path(index_dir) if index_dir else settings.resolve(settings.index_dir)
    idir.mkdir(parents=True, exist_ok=True)

    docs = load_knowledge_dir(kdir)
    if not docs:
        raise SystemExit(f"No se encontraron documentos en {kdir}")

    chunks = []
    for doc in docs:
        chunks.extend(chunk_document(doc))

    texts = [c.text for c in chunks]
    embedder = build_embedder()
    if hasattr(embedder, "fit"):
        embedder.fit(texts)
    matrix = np.asarray(embedder.embed(texts), dtype=np.float32)

    records = [c.to_record() for c in chunks]
    meta_path = idir / "chunks.json"
    vec_path = idir / "vectors.npy"
    meta_path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    np.save(vec_path, matrix)
    if hasattr(embedder, "save"):
        embedder.save(idir)

    # registro de actualidad del índice
    (idir / "INDEX_INFO.json").write_text(
        json.dumps({
            "num_chunks": len(chunks),
            "num_docs": len(docs),
            "embedder": type(embedder).__name__,
            "indexed_at": _now(),
        }, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return {"chunks": len(chunks), "docs": len(docs), "index_dir": str(idir)}


def _now() -> str:
    from datetime import datetime
    return datetime.now().isoformat(timespec="seconds")


if __name__ == "__main__":
    summary = run()
    print("Índice generado:", summary)
