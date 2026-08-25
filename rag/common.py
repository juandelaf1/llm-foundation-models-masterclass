"""Contratos y utilidades compartidas del RAG.

Define el esquema de metadata que DEBE cumplir todo documento de `knowledge/`
y las funciones de parseo y troceado reutilizadas por ingesta y recuperación.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional

import numpy as np

# ---------------------------------------------------------------------------
# Esquema de metadata mínimo exigido por la especificación (MASTERCLASS_SPEC §9)
# ---------------------------------------------------------------------------
REQUIRED_META_KEYS = [
    "topic",          # tema/concepto principal
    "source_type",    # official_doc | paper | course | secondary
    "provider",       # openai | google | anthropic | meta | mistral | deepseek | na
    "model_family",   # gpt | gemini | claude | llama | mistral | deepseek | na
    "course_section", # hook | anatomia | ecosistema | demo | reto | cierre
    "difficulty",     # beginner | intermediate | advanced
    "updated_at",     # YYYY-MM-DD (fecha de verificación de la fuente)
    "source_url",     # URL primaria de la afirmación
]

_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Devuelve (metadata, cuerpo) parseando un bloque YAML mínimo al inicio.

    Soporta escalares y listas en línea: ``key: [a, b]`` o ``key: a, b``.
    No es un parser YAML completo; basta para los documentos de knowledge/.
    """
    meta: dict = {}
    body = text
    m = _FRONTMATTER_RE.match(text)
    if m:
        block = m.group(1)
        body = text[m.end():]
        for line in block.splitlines():
            if ":" not in line:
                continue
            key, _, raw = line.partition(":")
            key = key.strip()
            val = raw.strip()
            if val.startswith("[") and val.endswith("]"):
                val = val[1:-1]
            if "," in val:
                meta[key] = [v.strip() for v in val.split(",") if v.strip()]
            else:
                meta[key] = val
    return meta, body


def validate_metadata(meta: dict, source: str) -> list[str]:
    """Devuelve lista de claves faltantes (vacía si todo ok)."""
    missing = [k for k in REQUIRED_META_KEYS if not meta.get(k)]
    if missing:
        return [f"{source}: falta metadata '{k}'" for k in missing]
    return []


@dataclass
class Document:
    id: str
    title: str
    text: str
    metadata: dict = field(default_factory=dict)
    source_path: str = ""


@dataclass
class Chunk:
    id: str
    doc_id: str
    text: str
    title: str
    metadata: dict = field(default_factory=dict)
    source_path: str = ""

    def to_record(self) -> dict:
        rec = asdict(self)
        rec["metadata"] = self.metadata
        return rec


def load_tfidf_vocab(index_dir: str | Path):
    """Carga vocabulario+idf persistidos por la ingesta (modo offline)."""
    p = Path(index_dir) / "tfidf_vocab.json"
    if not p.exists():
        return None
    data = json.loads(p.read_text(encoding="utf-8"))
    return data["vocab"], np.array(data["idf"], dtype=np.float32)


def _split_sentences(body: str) -> list[str]:
    # Heurística simple; suficiente para texto técnico en español/inglés.
    parts = re.split(r"(?<=[\.\?\!])\s+|\n+", body)
    return [p.strip() for p in parts if p.strip()]


def chunk_document(doc: Document, max_chars: int = 900, overlap: int = 120) -> list[Chunk]:
    """Trocea el cuerpo de un documento en fragmentos con solapamiento.

    Conserva la metadata del documento para permitir filtros en recuperación.
    """
    sentences = _split_sentences(doc.text)
    chunks: list[Chunk] = []
    buffer = ""
    idx = 0
    for sent in sentences:
        if buffer and len(buffer) + len(sent) > max_chars:
            chunks.append(_make_chunk(doc, idx, buffer))
            buffer = buffer[-overlap:] + " " + sent if overlap else sent
            idx += 1
        else:
            buffer = (buffer + " " + sent).strip() if buffer else sent
    if buffer:
        chunks.append(_make_chunk(doc, idx, buffer))
    return chunks


def _make_chunk(doc: Document, idx: int, text: str) -> Chunk:
    return Chunk(
        id=f"{doc.id}#{idx}",
        doc_id=doc.id,
        text=text,
        title=doc.title,
        metadata=dict(doc.metadata),
        source_path=doc.source_path,
    )


def load_knowledge_dir(knowledge_dir: str | Path) -> list[Document]:
    """Carga todos los .md de knowledge/ como Document con metadata validada."""
    root = Path(knowledge_dir)
    docs: list[Document] = []
    errors: list[str] = []
    if not root.exists():
        return docs
    for path in sorted(root.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        errs = validate_metadata(meta, str(path))
        errors.extend(errs)
        doc_id = str(path.relative_to(root)).replace("/", "_").replace(".md", "")
        title = meta.get("title") or path.stem
        docs.append(Document(id=doc_id, title=title, text=body, metadata=meta, source_path=str(path)))
    if errors:
        import warnings
        warnings.warn("Metadata incompleta:\n" + "\n".join(errors))
    return docs
