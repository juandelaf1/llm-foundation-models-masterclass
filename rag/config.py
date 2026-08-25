"""Configuración del RAG leída desde variables de entorno / .env."""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    # python-dotenv es opcional; el modo offline no lo requiere.
    pass

_ROOT = Path(__file__).resolve().parents[1]


@dataclass
class Settings:
    rag_mode: str = os.getenv("RAG_MODE", "offline")
    embedding_provider: str = os.getenv("EMBEDDING_PROVIDER", "local")
    llm_provider: str = os.getenv("LLM_PROVIDER", "offline")
    llm_model: str = os.getenv("LLM_MODEL", "gpt-4o-mini")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")
    knowledge_dir: Path = Path(os.getenv("KNOWLEDGE_DIR", "knowledge"))
    index_dir: Path = Path(os.getenv("INDEX_DIR", "rag/.index"))

    def resolve(self, p: Path) -> Path:
        return p if p.is_absolute() else (_ROOT / p)


def get_settings() -> Settings:
    return Settings()
