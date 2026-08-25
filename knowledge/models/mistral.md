---
title: "Mistral (Mistral AI): open-weight europeo y API gestionada"
topic: mistral
source_type: official_doc
provider: mistral
model_family: mistral
course_section: ecosistema
difficulty: intermediate
updated_at: 2026-08-25
source_url: https://mistral.ai/news/mistral-3
---

# Mistral (Mistral AI): open-weight europeo y API gestionada

## Qué es Mistral en una frase

Mistral AI es el laboratorio europeo (Francia) detrás de la familia **Mistral**, que combina modelos **open-weight** (descarga y auto-hospedaje) con una **API gestionada** (La Plateforme / Le Chat). Es un referente de eficiencia y soberanía de datos en Europa.

## Contexto verificado en fuentes oficiales (agosto 2026)

Según el anuncio oficial *Introducing Mistral 3* (`mistral.ai/news/mistral-3`, 17 de junio de 2026) y la documentación de modelos (`docs.mistral.ai/models/overview`):

- **Mistral 3** incluye tres modelos densos pequeños (**14B, 8B y 3B**) y **Mistral Large 3**, descrito como el modelo más capaz hasta la fecha: un **MoE (mezcla de expertos) disperso** con **41B parámetros activos y 675B totales**.
- **Todos los modelos de Mistral 3 se publican bajo licencia Apache 2.0** (permisiva: uso comercial, modificación y auto-hospedaje libres). Esto sí cumple la noción de pesos abiertos bajo licencia estándar.
- La documentación lista también modelos especializados (codificación, OCR, moderación, embeddings) y una tabla de **deprecations/retirements** con fechas de cierre por versión.

## Por qué importa Mistral en la comparativa

- Es **open-weight con licencia permisiva real** (Apache 2.0) → buen contraejemplo frente a Llama (licencia comunitaria) y frente a GPT/Gemini/Claude (cerrados).
- Enfoque en **eficiencia** (modelos pequeños y MoE) → interesante para coste/latencia y despliegue edge.
- **Soberanía europea / residencia de datos**: distintivo para despliegues con requisitos regulatorios (RGPD).

## Criterios de ingeniería (resumen)

| Criterio | Nota |
| --- | --- |
| Entrega | Open-weight (Apache 2.0) + API gestionada (La Plateforme) |
| Licencia | Apache 2.0 en la línea Mistral 3 |
| Eficiencia | Modelos densos pequeños + MoE (Large 3) |
| Privacidad | Auto-hospedaje posible; residencia UE |
| Multimodalidad | Cobertura variable por modelo; ver docs |

## Fuentes oficiales

- Anuncio Mistral 3: https://mistral.ai/news/mistral-3
- Modelos/docs: https://mistral.ai/models/  y  https://docs.mistral.ai/models/overview
- Changelog: https://docs.mistral.ai/getting-started/changelog

> **Dato cambiante no verificable aquí:** contexto exacto por modelo, precios de API y nombres de la última generación (p. ej. Small 4 / Medium 3.5). Márcalo como pendiente y verifica en `mistral.ai/models` antes de docencia/producción.
