# Maintenance & Freshness Control (SUPERPROMPT §21 / PATCH v2.1 §6)

Separar lo estable de lo cambiante. La presentación depende poco de lo
cambiante; el RAG absorbe gran parte de la volatilidad.

## Última verificación
- Última verificación de modelos: **2026-08-25** (ver `references/sources.md`).
- Última indexación del RAG: ejecutar `python -m rag.ingestion.ingest` y
  consultar `rag/.index/INDEX_INFO.json`.
- Próxima revisión recomendada: **2026-11-25** (trimestral) o ante cualquier
  lanzamiento relevante de los proveedores cubiertos.

## Datos cambiantes (B) — fuentes con versión / model ID
| Proveedor | Fuente viva | Qué vigilar |
|---|---|---|
| OpenAI | help.openai.com gpt-oss | model IDs open-weight, disponibilidad API |
| Google | ai.google.dev/gemini-api/docs/models + /deprecations | versiones estables/preview, deprecaciones |
| Anthropic | docs.anthropic.com | familias Claude, precios |
| Meta | llama.com | variantes Llama, licencia de pesos |
| Mistral | docs.mistral.ai | variantes, licencias |
| DeepSeek | api-docs.deepseek.com | variantes, contexto, licencia |

## Deprecaciones conocidas
- Registrar aquí cualquier retirada confirmada al revisar las fuentes oficiales
  (p. ej. modelos marcados "deprecated" en la página de deprecaciones de Google).

## Conceptos estables (A) — no requieren revisión frecuente
Tokens, embeddings, self-attention, Transformer, generación autoregresiva,
diferencia open-weight vs open source, método de selección por criterios.

## Procedimiento de actualización
1. Revisar las 8 fuentes oficiales de la tabla B.
2. Actualizar el `updated_at` y `source_url` de los docs afectados en
   `knowledge/models/`.
3. Reindexar: `python -m rag.ingestion.ingest`.
4. Reejecutar evaluación: `python -m rag.evaluation.eval`.
5. Anotar en este archivo la fecha y los cambios.
