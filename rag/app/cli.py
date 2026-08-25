"""CLI del RAG: `python -m rag.app.cli "¿qué es un token?"`."""
from __future__ import annotations

import argparse
import json
import sys

from rag.app.ask import ask


def main(argv=None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
    p = argparse.ArgumentParser(description="Learning RAG de la masterclass LLM.")
    p.add_argument("query", help="Pregunta libre sobre la masterclass.")
    p.add_argument("--top-k", type=int, default=5)
    p.add_argument("--provider", default=None, help="Filtra por proveedor (openai, google, ...)")
    p.add_argument("--model-family", default=None, help="Filtra por familia (gpt, llama, ...)")
    p.add_argument("--section", default=None, help="Filtra por sección del curso.")
    p.add_argument("--json", action="store_true", help="Salida JSON (para tests/pipelines).")
    args = p.parse_args(argv)

    filters = {k: v for k, v in {
        "provider": args.provider,
        "model_family": args.model_family,
        "course_section": args.section,
    }.items() if v}

    result = ask(args.query, top_k=args.top_k, filters=filters or None)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(result["answer"])
        print("\n---")
        print(f"Modo: {result['mode']} | Fragmentos recuperados: {result['num_retrieved']} | "
              f"Abstinencia: {result['abstained']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
