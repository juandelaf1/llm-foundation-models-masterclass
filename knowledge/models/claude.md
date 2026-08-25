---
title: "Claude (Anthropic): familia de modelos y acceso por API"
topic: claude
source_type: official_doc
provider: anthropic
model_family: claude
course_section: ecosistema
difficulty: intermediate
updated_at: 2026-08-25
source_url: https://docs.anthropic.com/en/docs/about-claude/models/overview
---

# Claude (Anthropic): familia de modelos y acceso por API

## Qué es Claude en una frase

Claude es la familia de modelos de **Anthropic**, ofrecida como **servicio gestionado** vía la API de Claude (`docs.anthropic.com`, `platform.claude.com`) y también disponible en Amazon Bedrock y Google Cloud. Es un modelo de pesos cerrados (no open-weight).

## Contexto verificado en fuentes oficiales (agosto 2026)

Según la página de *Model system cards* de Anthropic (`anthropic.com/system-cards`) y la *Models overview* de la documentación (`platform.claude.com/docs/en/about-claude/models/overview`):

- La familia se organiza en **niveles** (tiers) de capacidad: **Opus** (el más capaz), **Sonnet** (equilibrio) y **Haiku** (más rápido/económico), con numeración que avanza (p. ej. versiones 4.x y 5.x según los system cards oficiales).
- En junio de 2026, Anthropic listó **Claude Fable 5** (`claude-fable-5`) y **Claude Mythos 5** (`claude-mythos-5`) como los modelos de liberación amplia más capaces, disponibles en la API de Claude, Amazon Bedrock, Google Cloud y Microsoft Foundry.
- Los *system cards* documentan capacidades, evaluaciones de seguridad y decisiones de despliegue responsable, con fechas por modelo (p. ej. Opus 5 en julio de 2026, Sonnet 5 en junio de 2026).

## Qué NO afirmamos aquí

No incluimos benchmarks numéricos ni precios: cambian y son frágiles. Para lo actual, consulta:

- Precios: `platform.claude.com/docs/en/about-claude/pricing`
- Modelos y cutoffs de entrenamiento: `platform.claude.com/docs/en/about-claude/models/overview`
- System cards (seguridad/capacidades): `anthropic.com/system-cards`

## Criterios de ingeniería (resumen)

| Criterio | Nota |
| --- | --- |
| Entrega | API gestionada (Anthropic), Bedrock, Google Cloud |
| Open-weight | No (pesos cerrados) |
| Niveles | Opus / Sonnet / Haiku (capacidad vs coste/latencia) |
| Seguridad | System cards públicos por versión |
| Privacidad | Datos van a Anthropic salvo acuerdos/Bedrock |

## Fuentes oficiales

- Documentación/overview: https://docs.anthropic.com/en/docs/about-claude/models/overview
- Plataforma: https://platform.claude.com/docs/en/about-claude/models/overview
- System cards: https://www.anthropic.com/system-cards

> **Dato cambiante no verificable aquí:** nombres exactos de la última versión estrella, precios y ventanas de contexto. Márcalo como pendiente y verifica en las fuentes oficiales antes de docencia/producción.
