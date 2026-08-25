"""Tests del RAG, ejecutables en un entorno limpio.

Usan un corpus temporal para no depender del contenido de knowledge/ en tiempo
de test. Verifican: parseo de frontmatter, troceo, ingesta, recuperación,
abstinencia y citas.
"""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import numpy as np

from rag.common import chunk_document, parse_frontmatter, validate_metadata, Document
from rag.ingestion.ingest import run as ingest_run
from rag.retrieval.embeddings import build_embedder
from rag.retrieval.retriever import load_index, query_has_evidence, retrieve
from rag.retrieval.llm import OfflineGrounder

SAMPLE = """---
title: Tokens de ejemplo
topic: tokens
source_type: official_doc
provider: openai
model_family: na
course_section: anatomia
difficulty: beginner
updated_at: 2026-08-25
source_url: https://example.com/tokens
---
La tokenización divide el texto en unidades. Un token no es siempre una palabra.
El número de tokens varía con el idioma, el código y los símbolos.
"""

SAMPLE2 = """---
title: Ecosistema
topic: ecosistema
source_type: course
provider: na
model_family: na
course_section: ecosistema
difficulty: intermediate
updated_at: 2026-08-25
source_url: https://example.com/eco
---
Existen servicios gestionados y modelos open-weight. Open-weight no es open source.
"""


def _make_corpus(root: Path) -> Path:
    d = root / "knowledge"
    (d / "fundamentals").mkdir(parents=True)
    (d / "models").mkdir(parents=True)
    (d / "fundamentals" / "tokens.md").write_text(SAMPLE, encoding="utf-8")
    (d / "models" / "eco.md").write_text(SAMPLE2, encoding="utf-8")
    return d


def test_frontmatter_and_validate():
    meta, body = parse_frontmatter(SAMPLE)
    assert meta["topic"] == "tokens"
    assert validate_metadata(meta, "x") == []


def test_chunk_document():
    doc = Document(id="d", title="t", text=SAMPLE.split("---", 2)[-1], metadata={"topic": "tokens"})
    chunks = chunk_document(doc)
    assert len(chunks) >= 1
    assert all(c.metadata["topic"] == "tokens" for c in chunks)


def test_ingest_retrieve_ask(tmp_path):
    kdir = _make_corpus(tmp_path)
    idir = tmp_path / "index"
    summary = ingest_run(knowledge_dir=str(kdir), index_dir=str(idir))
    assert summary["docs"] == 2
    assert (idir / "chunks.json").exists()

    records, vectors = load_index(str(idir))
    assert len(records) == summary["chunks"]

    emb = build_embedder(index_dir=str(idir))
    q = emb.embed(["¿Qué es la tokenización?"])[0]
    res = retrieve(np.asarray(q, dtype=np.float32), top_k=3, index_dir=str(idir))
    assert query_has_evidence(res)
    assert res[0]["metadata"]["topic"] == "tokens"

    gen = OfflineGrounder()
    out = gen.answer("¿Qué es la tokenización?", res)
    assert not out["abstained"]
    assert any("http" in (c.get("url") or "") for c in out["citations"])


def test_abstention_on_unrelated(tmp_path):
    kdir = _make_corpus(tmp_path)
    idir = tmp_path / "index"
    ingest_run(knowledge_dir=str(kdir), index_dir=str(idir))
    emb = build_embedder(index_dir=str(idir))
    q = emb.embed(["¿Cuál es la receta del tiramisú?"])[0]
    res = retrieve(np.asarray(q, dtype=np.float32), top_k=3, index_dir=str(idir))
    # sin evidencia relevante -> se abstiene
    assert not query_has_evidence(res)
