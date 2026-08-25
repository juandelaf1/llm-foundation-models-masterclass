---
title: "Gemini (Google): modelo multimodal y ecosistema de APIs"
topic: gemini
source_type: official_doc
provider: google
model_family: gemini
course_section: ecosistema
difficulty: intermediate
updated_at: 2026-08-25
source_url: https://ai.google.dev/gemini-api/docs/models
---

# Gemini (Google): modelo multimodal y ecosistema de APIs

## Qué es Gemini en una frase

Gemini es la familia de modelos de Google DeepMind, accesible vía la **Gemini API** (`ai.google.dev`) y también desplegada en Google Cloud (Vertex AI / Gemini Enterprise Agent Platform). Es la opción "servicio gestionado" de Google, con fuerte enfoque **multimodal** (texto, imagen, audio, vídeo).

## Contexto verificado en fuentes oficiales (agosto 2026)

Según la documentación oficial de modelos de Gemini (`ai.google.dev/gemini-api/docs/models`, actualizada 2026-08-14) y las notas de cambios (`ai.google.dev/gemini-api/docs/changelog`):

- La **serie Gemini 3** es la línea actual. La documentación referencia **Gemini 3.1 Pro** y modelos Flash (p. ej. **Gemini 3.5 Flash**, GA el 19 de mayo de 2026; **Gemini 3.7 Flash** referenciado en agosto de 2026).
- Hay variantes y agentes especializados en la plataforma: p. ej. *Computer Use* (modelo que "ve" la pantalla y ejecuta acciones UI), *Deep Research* (agente de investigación), e *Antigravity Agent* (agente gestionado).
- Google también publica modelos **Gemma** (familia open-weight más pequeña) y modelos de embedding multimodal (`gemini-embedding-2-preview`), según las notas de cambio.

## Deprecaciones (importante para ingeniería)

La documentación oficial mantiene una página de **deprecations**. Ejemplos verificados en las release notes:

- `gemini-2.0-flash`, `gemini-2.0-flash-lite` y variantes indicadas como **apagadas el 1 de junio de 2026**; se recomienda migrar a `gemini-3.5-flash` / `gemini-3.1-flash-lite`.
- Varios modelos de imagen/vídeo (Imagen 4, Veo 2/3) con fechas de cierre programadas.

> Las políticas de deprecación cambian; consulta siempre `ai.google.dev/gemini-api/docs/deprecations` antes de fijar una versión en producción.

## Criterios de ingeniería (resumen)

| Criterio | Nota |
| --- | --- |
| Multimodalidad | Fuerte (texto/imagen/audio/vídeo) |
| Entrega | API gestionada (Google); no es open-weight la línea principal |
| Contexto | Varía por versión; ver docs oficiales (no afirmamos cifra aquí) |
| Privacidad | Datos van a Google salvo acuerdos/Vertex con controles |
| Agentes | Soporte de Computer Use, Deep Research, Managed Agents |

## Fuentes oficiales

- Modelos: https://ai.google.dev/gemini-api/docs/models
- Release notes: https://ai.google.dev/gemini-api/docs/changelog
- Deprecations: https://ai.google.dev/gemini-api/docs/deprecations
- DeepMind: https://deepmind.google/models/gemini/

> **Dato cambiante no verificable aquí:** ventanas de contexto exactas, precios y el "último" modelo estrella de Gemini. Márcalo como pendiente y verifica en `ai.google.dev/gemini-api/docs/models` antes de docencia/producción.
