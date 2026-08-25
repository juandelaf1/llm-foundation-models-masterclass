---
title: "DeepSeek: open-weight con licencia MIT y API gestionada"
topic: deepseek
source_type: official_doc
provider: deepseek
model_family: deepseek
course_section: ecosistema
difficulty: intermediate
updated_at: 2026-08-25
source_url: https://api-docs.deepseek.com/news/news260424
---

# DeepSeek: open-weight con licencia MIT y API gestionada

## Qué es DeepSeek en una frase

DeepSeek es el laboratorio detrás de la familia **DeepSeek**, conocida por modelos **open-weight** de alto rendimiento y bajo coste, con licencia **MIT** (muy permisiva), y también ofrecida vía **API gestionada** (`platform.deepseek.com`).

## Contexto verificado en fuentes oficiales (agosto 2026)

Según las notas oficiales de la API de DeepSeek (`api-docs.deepseek.com`, incluyendo el anuncio *DeepSeek V4 Preview* del 24 de abril de 2026 y la página de actualizaciones):

- **DeepSeek V4** se anunció como *preview* el 24 de abril de 2026, con dos IDs de API: **`deepseek-v4-pro`** (razonamiento/agentes) y **`deepseek-v4-flash`** (más rápido/económico).
- Soporta **1M de contexto** y modos duales *Thinking / Non-Thinking*; es compatible con las APIs de ChatCompletions y Anthropic.
- Los **pesos open-weight** de V4 se publican con licencia **MIT** en la colección oficial de Hugging Face de DeepSeek (`huggingface.co/deepseek-ai`), con rutas de despliegue local (Transformers, vLLM, SGLang, etc.).
- Modelos legacy (`deepseek-chat`, `deepseek-reasoner`) fueron marcados como retirados tras el 24 de julio de 2026, enrutando a V4 Flash.

## Por qué importa en la comparativa

- Es **open-weight con licencia MIT** → el estándar más permisivo; buen contraejemplo de "pesos abiertos de verdad".
- Fuerte enfoque en **coste-eficiencia** y contexto largo (1M), atractivo para despliegue propio y RAG.
- Historia previa relevante: V3 y **R1** (razonamiento) fueron hitos open-weight; la arquitectura MoE es recurrente en la familia.

## Criterios de ingeniería (resumen)

| Criterio | Nota |
| --- | --- |
| Entrega | Open-weight (MIT) + API gestionada |
| Licencia | MIT (permisiva, uso comercial libre) |
| Contexto | Hasta 1M tokens (según anuncio V4) |
| Coste | API por token; pesos gratis para auto-hospedaje |
| Privacidad | Auto-hospedaje posible; API envía datos a DeepSeek |

## Fuentes oficiales

- Anuncio V4: https://api-docs.deepseek.com/news/news260424
- Documentación/actualizaciones: https://api-docs.deepseek.com/updates/
- Web: https://www.deepseek.com/  y  https://platform.deepseek.com/
- Hugging Face: https://huggingface.co/deepseek-ai

> **Dato cambiante no verificable aquí:** precios exactos de API por millón de tokens, parámetros arquitectónicos de V4 y nombres de futuras versiones. Márcalo como pendiente y verifica en `api-docs.deepseek.com/quick_start/pricing` antes de docencia/producción.
