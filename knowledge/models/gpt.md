---
title: "GPT (OpenAI): API gestionada y familia open-weight gpt-oss"
topic: gpt
source_type: official_doc
provider: openai
model_family: gpt
course_section: ecosistema
difficulty: intermediate
updated_at: 2026-08-25
source_url: https://openai.com/index/introducing-gpt-oss/
---

# GPT (OpenAI): API gestionada y familia open-weight gpt-oss

## Dos caras de "GPT" que debes distinguir

OpenAI ofrece GPT en **dos modelos de entrega** distintos, y confundirlos es un error frecuente:

1. **API gestionada (servicio cerrado):** accedes a los modelos GPT a través de la API de OpenAI (o Azure OpenAI). No descargas pesos; pagas por uso. Es la opción "servicio gestionado" del ecosistema (`models/ecosistema_categorias.md`).
2. **gpt-oss (open-weight):** OpenAI publicó pesos abiertos bajo licencia **Apache 2.0**. Tú los ejecutas donde quieras.

## gpt-oss (open-weight) — verificado en fuente oficial

Según el anuncio oficial de OpenAI (5 de agosto de 2025, `openai.com/index/introducing-gpt-oss/` y el centro de ayuda `help.openai.com/en/articles/11870455`):

- Se lanzaron **dos modelos open-weight**: `gpt-oss-120b` y `gpt-oss-20b`.
- Están pensados para **razonamiento, tareas agenticas y uso general de desarrollador**, con buen rendimiento a bajo coste.
- Licencia **Apache 2.0** (permisiva; permite uso comercial, modificación y auto-hospedaje).
- Se ejecutan **en infraestructura que controlas** o vía proveedores de hosting.
- Arquitectura: Transformer basado en **Mixture-of-Experts (MoE)** con **Grouped Query Attention (GQA)**; contexto de **131.072 tokens**; tokenizador `o200k_harmony`. (Datos del modelo card oficial / repositorio GitHub `openai/gpt-oss`.)
- El modelo card oficial indica un conocimiento hasta ~junio de 2024 (knowledge cutoff). Verifica siempre el card para detalles actuales.

> Nota: no inventamos aquí benchmarks numéricos. El posicionamiento declarado por OpenAI es "strong real-world performance at low cost" y "outperform similarly sized open models on reasoning". Para cifras, consulta el modelo card oficial, que cambia.

## API gestionada (GPT)

OpenAI mantiene una línea de modelos de acceso por API (la familia GPT de los servicios de ChatGPT/API). Los nombres y versiones **cambian con frecuencia**; no afirmamos aquí números de parámetros ni precios porque son frágiles y variables. Para lo actual:

- Documentación de modelos y precios: `platform.openai.com/docs/models` (fuente oficial).
- La API es compatible con el formato estándar de chat completions; existen también modalidades/agentes específicos que evolucionan.

## Criterios de ingeniería (resumen)

| Criterio | API gestionada | gpt-oss (open-weight) |
| --- | --- | --- |
| Privacidad | datos van a OpenAI (salvo acuerdos) | datos se quedan en tu infra |
| Infraestructura | ninguna | tú provees GPU/RAM |
| Coste | por token | CAPEX/OPEX propio + libre Apache 2.0 |
| Actualizaciones | automáticas | tú gestionas |
| Licencia | servicio | Apache 2.0 |

## Fuentes oficiales a consultar

- Anuncio gpt-oss: https://openai.com/index/introducing-gpt-oss/
- Centro de ayuda gpt-oss: https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss
- Repositorio/model card: https://github.com/openai/gpt-oss
- Modelos API: https://platform.openai.com/docs/models

> **Dato cambiante no verificable en este documento:** números de parámetros exactos, precios de API y nombres de la última generación GPT de acceso gestionado. Márcalo como pendiente y verifica en `platform.openai.com/docs/models` antes de usarlo en producción/docencia.
