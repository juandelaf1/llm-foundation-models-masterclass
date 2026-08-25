"""Generadores de respuesta (answer synthesis).

- OfflineGrounder: compone la respuesta a partir de los fragmentos recuperados
  con sus citas. No requiere red ni API y es el modo por defecto.
- OpenAIGenerator / AnthropicGenerator: generan respuesta con un LLM externo
  usando el SYSTEM_PROMPT de rag.prompts.system (grounding + abstinencia).
"""
from __future__ import annotations

from typing import List

from rag.config import get_settings
from rag.prompts.system import GROUNDED_OFFLINE_TEMPLATE, SYSTEM_PROMPT


def _as_str(value) -> str:
    if isinstance(value, (list, tuple)):
        return ", ".join(str(v) for v in value)
    return str(value)


def _context_block(results: List[dict]) -> str:
    lines = []
    for i, r in enumerate(results, 1):
        meta = r.get("metadata", {})
        url = _as_str(meta.get("source_url", "n/a"))
        title = _as_str(r.get("title", "fragmento"))
        lines.append(f"[{i}] {title} ({url})\n{r['text']}\n")
    return "\n".join(lines)


def _sources_block(results: List[dict]) -> str:
    seen = set()
    out = []
    for r in results:
        meta = r.get("metadata", {})
        url = _as_str(meta.get("source_url", "n/a"))
        title = _as_str(r.get("title", "fragmento"))
        key = (title, url)
        if key in seen:
            continue
        seen.add(key)
        out.append(f"- {title}: {url}")
    return "\n".join(out)


class OfflineGrounder:
    def answer(self, query: str, results: List[dict]) -> dict:
        if not results:
            return {
                "answer": "No dispongo de evidencia suficiente en las fuentes del curso "
                          "para responder esto. Revisa la sección correspondiente o amplía "
                          "el corpus en knowledge/.",
                "citations": [],
                "abstained": True,
                "mode": "offline",
            }
        answer = GROUNDED_OFFLINE_TEMPLATE.format(
            context_block=_context_block(results),
            sources_block=_sources_block(results),
        )
        return {
            "answer": answer,
            "citations": [{"title": r.get("title"), "url": r.get("metadata", {}).get("source_url")} for r in results],
            "abstained": False,
            "mode": "offline",
        }


class OpenAIGenerator:
    def answer(self, query: str, results: List[dict]) -> dict:
        from openai import OpenAI
        settings = get_settings()
        client = OpenAI(api_key=settings.openai_api_key or None)
        ctx = _context_block(results) or "(sin contexto recuperado)"
        resp = client.chat.completions.create(
            model=settings.llm_model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Pregunta: {query}\n\nContexto:\n{ctx}"},
            ],
        )
        text = resp.choices[0].message.content
        abstained = "no dispongo de evidencia" in text.lower()
        return {
            "answer": text,
            "citations": [{"title": r.get("title"), "url": r.get("metadata", {}).get("source_url")} for r in results],
            "abstained": abstained,
            "mode": "openai",
        }


class AnthropicGenerator:
    def answer(self, query: str, results: List[dict]) -> dict:
        import anthropic
        settings = get_settings()
        client = anthropic.Anthropic(api_key=settings.anthropic_api_key or None)
        ctx = _context_block(results) or "(sin contexto recuperado)"
        resp = client.messages.create(
            model="claude-3-5-sonnet-latest",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": f"Pregunta: {query}\n\nContexto:\n{ctx}"}],
        )
        text = "".join(b.text for b in resp.content if b.type == "text")
        abstained = "no dispongo de evidencia" in text.lower()
        return {
            "answer": text,
            "citations": [{"title": r.get("title"), "url": r.get("metadata", {}).get("source_url")} for r in results],
            "abstained": abstained,
            "mode": "anthropic",
        }


def build_generator() -> object:
    settings = get_settings()
    if settings.llm_provider == "openai" and settings.openai_api_key:
        return OpenAIGenerator()
    if settings.llm_provider == "anthropic" and settings.anthropic_api_key:
        return AnthropicGenerator()
    return OfflineGrounder()
