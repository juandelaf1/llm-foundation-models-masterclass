---
title: "Llama (Meta): la línea open-weight y su licencia comunitaria"
topic: llama
source_type: official_doc
provider: meta
model_family: llama
course_section: ecosistema
difficulty: intermediate
updated_at: 2026-08-25
source_url: https://www.llama.com/
---

# Llama (Meta): la línea open-weight y su licencia comunitaria

## Qué es Llama en una frase

Llama es la familia de modelos de **Meta**, distribuida como **open-weight**: descargas los pesos y los ejecutas donde quieras. Es el ejemplo de referencia de "pesos abiertos" en el ecosistema (`models/ecosistema_categorias.md`), aunque **no es open source estricto** (ver licencia abajo).

## Contexto verificado en fuentes oficiales (agosto 2026)

Según la documentación y repositorios oficiales de Meta (`llama.com`, `huggingface.co/meta-llama`, `github.com/meta-llama/llama-models`):

- **Llama 4** es la generación actual (anunciada abril de 2025). La organización de Hugging Face de Meta describe a Llama 4 como modelos **nativamente multimodales** (texto e imagen) que usan arquitectura **Mixture-of-Experts (MoE)**, con variantes como **Maverick** y **Scout**.
- **Llama 3** sigue disponible y es ampliamente usado en la comunidad (variantes de 8B, 70B, etc., según los repos oficiales).
- Meta también ofrece una **Llama API** (primera opción alojada de primera parte) y el modelo está disponible vía Hugging Face y otros proveedores de inferencia.

## Licencia: matización crítica

Llama **no** usa una licencia open source estándar. Utiliza la **Llama 4 Community License** (y la equivalente de Llama 3):

- Es una licencia **personalizada** (no Apache/MIT). Permite uso, modificación y redistribución, **incluido uso comercial**, pero con condiciones.
- Incluye un **carve-out de >700M MAU**: si tu producto supera ~700 millones de usuarios mensuales, debes solicitar licencia a Meta.
- Incorpora por referencia una **Acceptable Use Policy** (política de uso aceptable), que además impone restricciones regionales (p. ej. ciertas exclusiones aplicables en la UE, según la política de uso).
- Requiere conservar la atribución ("Llama 4 is licensed under the Llama 4 Community License, Copyright © Meta").

> Conclusión para la masterclass: Llama es **open-weight con licencia comunitaria restringida**, no "open source" en sentido estricto. Cita siempre `llama.com/license` para los términos vigentes.

## Criterios de ingeniería (resumen)

| Criterio | Nota |
| --- | --- |
| Entrega | Open-weight (descarga) + Llama API gestionada opcional |
| Licencia | Llama Community License (no estándar open source) |
| Multimodalidad | Llama 4 nativamente multimodal (texto+imagen) |
| Privacidad | Alta en auto-hospedaje; datos no salen |
| Infraestructura | Tú provees GPU/RAM; comunidad GGUF/Ollama |

## Fuentes oficiales

- Web/Licencia: https://www.llama.com/  y  https://www.llama.com/license
- Hugging Face: https://huggingface.co/meta-llama
- Licencia Llama 4 (repo): https://github.com/meta-llama/llama-models/blob/main/models/llama4/LICENSE

> **Dato cambiante no verificable aquí:** tamaños de parámetros exactos de cada variante Llama 4, ventanas de contexto y si Meta amplía su línea a modelos de pesos totalmente abiertos tipo Apache. Márcalo como pendiente y verifica en `llama.com` antes de docencia/producción.
