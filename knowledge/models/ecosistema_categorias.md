---
title: "Ecosistema de LLM: servicios gestionados vs modelos open-weight"
topic: ecosistema
source_type: course
provider: na
model_family: na
course_section: ecosistema
difficulty: intermediate
updated_at: 2026-08-25
source_url: https://www.llama.com/
---

# Ecosistema de LLM: servicios gestionados vs modelos open-weight

## Intuición visual antes de la terminología

Al elegir un LLM no eliges solo "un nombre". Estás eligiendo **un modelo de entrega**. La distinción más importante, y la que condiciona todo lo demás (coste, privacidad, despliegue), es:

> ¿Consumes el modelo como un **servicio gestionado (API)**, o descargas los **pesos del modelo** para ejecutarlo tú?

## 1. Servicios / API gestionadas

El proveedor entrena, aloja y sirve el modelo. Tú pagas por uso (normalmente por token) y llamas a una API.

- **Ejemplos:** la API de OpenAI (GPT), la API de Gemini (Google), la API de Claude (Anthropic), la API de Mistral (La Plateforme), la API de DeepSeek.
- **Ventajas:** sin infraestructura, actualizaciones automáticas, escalado, soporte.
- **Costes/riesgos:** coste por token recurrente, dependencia del proveedor (vendor lock-in), y—crítico—**tus datos viajan a sus servidores** (salvo acuerdos especiales).

## 2. Modelos open-weight (pesos abiertos)

El desarrollador publica los **pesos entrenados**. Tú los descargas y los ejecutas donde quieras (tu portátil, un servidor, la nube).

- **Ejemplos:** Llama (Meta), Mistral (open-weight), DeepSeek (open-weight, MIT), gpt-oss (OpenAI, open-weight Apache 2.0).
- **Ventajas:** control total, privacidad (datos no salen), personalización/fine-tuning, despliegue on-premise o edge.
- **Costes/riesgos:** tú provees la infraestructura (GPU/RAM), operas el servidor de inferencia (vLLM, Ollama...), y tú gestionas actualizaciones y seguridad.

## ⚠️ "Open source" ≠ "open-weight" (matización clave)

No son sinónimos:

- **Open-weight** significa que los *pesos* (el resultado del entrenamiento) se publican. Pero eso **no garantiza** que todo el ecosistema sea abierto: el código de entrenamiento, los datos de entrenamiento, la receta completa o las herramientas pueden no estar disponibles. La licencia puede imponer restricciones (uso comercial, tamaño de la empresa, región).
- **Open source (estricto)** implicaría también código, datos y proceso abiertos bajo una licencia estándar (p. ej. Apache 2.0). Muchos "open-weight" no cumplen la definición completa de open source de la OSI.

> Regla práctica para la masterclass: habla de **open-weight**, no de "open source", salvo que el modelo cumpla realmente (p. ej. DeepSeek V4 bajo MIT, Mistral 3 bajo Apache 2.0). Llama usa una *licencia comunitaria propia*, no una licencia open source estándar.

## Criterios de selección (la herramienta de ingeniería)

Para elegir entre opciones, evalúa estos ejes —nunca un solo benchmark:

1. **Capacidad / calidad** para tu tarea (razonamiento, código, idioma, multimodalidad).
2. **Coste** (por token o por infraestructura propia).
3. **Latencia** (tiempo de respuesta; clave en interfaces en tiempo real).
4. **Ventana de contexto y modalidades** (¿solo texto? ¿imagen/audio/vídeo? ¿cuántos tokens cabe?).
5. **Privacidad** (¿los datos salen a un tercero? ¿cumple normativa?).
6. **Control** (¿puedes inspeccionar/ajustar el comportamiento?).
7. **Despliegue** (API gestionada vs self-hosted vs edge).
8. **Personalización** (fine-tuning, LoRA, prompts).
9. **Licencia y condiciones** (uso comercial permitido, restricciones, atribución).

## Cómo usar esto en la práctica

El reto de la masterclass (`course/reto_llm_detective.md`) aplica estos criterios a un caso real. La conclusión esperada **no es "el modelo X es el mejor"**, sino *"para este caso, dadas estas restricciones, esta categoría de entrega y estos criterios encajan mejor"*.

## Fuentes para verificar lo cambiante

Los nombres de modelo y precios cambian constantemente. Antes de afirmar algo, consulta las fuentes oficiales que enlazamos en cada ficha (`models/gpt.md`, `gemini.md`, `claude.md`, `llama.md`, `mistral.md`, `deepseek.md`).
