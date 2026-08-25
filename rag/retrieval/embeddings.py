"""Proveedores de embeddings.

Por defecto se usa un vectorizador TF-IDF en local (sin red, sin modelos
pesados) para que el proyecto sea reproducible en un entorno limpio. Si el
stack opcional está instalado, se puede conmutar a embeddings semánticos reales
vía LlamaIndex configurando EMBEDDING_PROVIDER=openai o =local (sentence-transformers).
"""
from __future__ import annotations

import json
import math
import re
import unicodedata
from pathlib import Path
from typing import List

import numpy as np

from rag.common import load_tfidf_vocab
from rag.config import get_settings

# Palabras vacías (es/en) para reducir ruido en el modo offline.
STOPWORDS = {
    "el", "la", "los", "las", "de", "del", "y", "a", "en", "un", "una", "uno", "unos",
    "unas", "que", "se", "no", "es", "son", "por", "para", "con", "sin", "su", "sus",
    "al", "lo", "le", "como", "mas", "pero", "muy", "me", "te", "nos", "os", "este",
    "esta", "esto", "esos", "esas", "aquel", "ya", "entre", "sobre", "todo", "cada",
    "si", "o", "u", "cual", "que", "como", "cuando", "donde", "quien", "porque",
    "the", "an", "and", "or", "of", "to", "in", "is", "are", "for", "with", "on",
    "that", "this", "it", "as", "by", "from", "at", "be", "was", "were", "you", "we",
    "they", "your",
    # frecuentes en español (interrogativos/verbos) que generan solapamiento espurio
    "cual", "cuales", "cuantos", "cuantas", "quien", "quienes", "tiene",
    "tienen", "hay", "peso", "puede", "pueden", "temperatura", "alta",
    "alto", "baja", "bajo", "son", "fue", "sea", "estan", "esta", "ese",
    "esa", "uno", "una", "cada", "tan", "tanto", "donde", "cuando",
    "como", "asi", "otro", "otra", "parte", "forma", "caso", "ejemplo",
    "tipo", "ver", "aun", "cuyo", "cuya", "ademas", "tambien", "sino",
}


class TfidfEmbedder:
    """TF-IDF trivial sobre el vocabulario del corpus (modo offline)."""

    def __init__(self) -> None:
        self._vocab: dict[str, int] = {}
        self._idf: np.ndarray | None = None
        self._fitted = False

    @staticmethod
    def _tokenize(text: str) -> List[str]:
        # normaliza sin diacríticos para que "cuántos" == "cuantos" (stopword)
        text = "".join(
            c for c in unicodedata.normalize("NFKD", text)
            if not unicodedata.combining(c)
        )
        toks = re.findall(r"[a-z0-9]+", text.lower())
        # conserva tokens de 2+ caracteres y descarta palabras vacías
        return [t for t in toks if len(t) > 1 and t not in STOPWORDS]

    def fit(self, corpus: List[str]) -> "TfidfEmbedder":
        df: dict[str, int] = {}
        for doc in corpus:
            seen = set(self._tokenize(doc))
            for t in seen:
                df[t] = df.get(t, 0) + 1
        self._vocab = {t: i for i, t in enumerate(sorted(df))}
        n = len(corpus)
        self._idf = np.array([math.log((n + 1) / (df[t] + 1)) + 1.0 for t in self._vocab])
        self._fitted = True
        return self

    def save(self, index_dir: str | Path) -> None:
        Path(index_dir).mkdir(parents=True, exist_ok=True)
        data = {"vocab": self._vocab, "idf": self._idf.tolist()}
        (Path(index_dir) / "tfidf_vocab.json").write_text(
            json.dumps(data), encoding="utf-8")

    def load(self, index_dir: str | Path) -> "TfidfEmbedder":
        loaded = load_tfidf_vocab(index_dir)
        if loaded is None:
            raise FileNotFoundError("No se encontró tfidf_vocab.json en el índice.")
        self._vocab, self._idf = loaded
        self._fitted = True
        return self

    def _vector(self, text: str) -> np.ndarray:
        v = np.zeros(len(self._vocab), dtype=np.float32)
        toks = self._tokenize(text)
        if not toks:
            return v
        for t in toks:
            if t in self._vocab:
                v[self._vocab[t]] += 1.0
        # normaliza por frecuencia y aplica idf
        v = v / len(toks)
        v = v * self._idf
        norm = np.linalg.norm(v)
        if norm > 0:
            v = v / norm
        return v

    def embed(self, texts: List[str]) -> np.ndarray:
        if not self._fitted:
            self.fit(texts)
        return np.stack([self._vector(t) for t in texts])


def build_embedder(mode: str | None = None, index_dir: str | Path | None = None):
    settings = get_settings()
    mode = mode or settings.embedding_provider
    if mode == "local" and settings.rag_mode != "offline":
        try:
            from llama_index.embeddings.huggingface import HuggingFaceEmbedding
            return HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
        except Exception:
            pass
    if mode == "openai" and settings.rag_mode != "offline":
        try:
            from llama_index.embeddings.openai import OpenAIEmbedding
            return OpenAIEmbedding(api_key=settings.openai_api_key or None)
        except Exception:
            pass
    emb = TfidfEmbedder()
    idx = Path(index_dir) if index_dir else settings.resolve(settings.index_dir)
    if idx.exists() and (idx / "tfidf_vocab.json").exists():
        emb.load(idx)
    return emb
