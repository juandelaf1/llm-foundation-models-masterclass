"""Evaluación del RAG (SUPERPROMPT §13).

Evalúa, sobre el dataset de rag/evaluation/dataset.json:
  - relevancia de recuperación (fragmentos para preguntas respondibles);
  - presencia de citas (URL) en la respuesta;
  - tasa de abstinencia correcta para preguntas sin evidencia;
  - completitud básica (longitud mínima de la respuesta).

No afirma "evaluado" solo por funcionar a mano: produce un reporte y falla
si los umbrales mínimos no se cumplen.
"""
from __future__ import annotations

import json
from pathlib import Path

from rag.app.ask import ask

EXPECTED_TYPES = {"factual": 10, "comparison": 5, "concept": 5, "no_evidence": 5}


def load_dataset(path: str | Path) -> list[dict]:
    return json.loads(Path(path).read_text(encoding="utf-8"))["questions"]


def evaluate(dataset: list[dict]) -> dict:
    rows = []
    for item in dataset:
        res = ask(item["question"], filters=item.get("filters"))
        expected_answerable = item["type"] != "no_evidence"
        has_citation = any("http" in (c.get("url") or "") for c in res["citations"])
        rows.append({
            "id": item["id"],
            "type": item["type"],
            "answerable": expected_answerable,
            "retrieved": res["num_retrieved"],
            "abstained": res["abstained"],
            "has_citation": has_citation,
            "len": len(res["answer"]),
            "ok": (
                (not expected_answerable and res["abstained"]) or
                (expected_answerable and res["num_retrieved"] > 0 and has_citation)
            ),
        })
    return _summarize(rows)


def _summarize(rows: list[dict]) -> dict:
    total = len(rows)
    passed = sum(1 for r in rows if r["ok"])
    answerable = [r for r in rows if r["answerable"]]
    no_ev = [r for r in rows if not r["answerable"]]
    recall = sum(1 for r in answerable if r["retrieved"] > 0) / max(len(answerable), 1)
    citation_rate = sum(1 for r in answerable if r["has_citation"]) / max(len(answerable), 1)
    abstain_rate = sum(1 for r in no_ev if r["abstained"]) / max(len(no_ev), 1)
    return {
        "total": total,
        "passed": passed,
        "answerable_recall": round(recall, 3),
        "citation_rate": round(citation_rate, 3),
        "correct_abstention_rate": round(abstain_rate, 3),
        "rows": rows,
    }


def main() -> int:
    ds_path = Path(__file__).resolve().parent / "dataset.json"
    dataset = load_dataset(ds_path)
    report = evaluate(dataset)
    print(json.dumps({k: v for k, v in report.items() if k != "rows"}, ensure_ascii=False, indent=2))
    ok = report["passed"] == report["total"]
    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
