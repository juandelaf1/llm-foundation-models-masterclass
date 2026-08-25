---
title: "Demo Bbycroft LLM: visualizar el pipeline del modelo"
topic: bbycroft
source_type: course
provider: na
model_family: na
course_section: demo
difficulty: beginner
updated_at: 2026-08-25
source_url: https://bbycroft.net/llm
---

# Demo Bbycroft LLM: visualizar el pipeline del modelo

## Qué es

[LLM visualization de Bbycroft](https://bbycroft.net/llm) es una animación interactiva que muestra, capa a capa, cómo un Transformer **pequeño** procesa texto: `input → embedding → attention → MLP → output`. Es la mejor forma de hacer *visible* lo que explican `03_transformer.md`, `04_self_attention.md` y `05_generacion_autoregresiva.md`.

## Cómo usarla en la masterclass (5–10 min)

1. Abre https://bbycroft.net/llm
2. Explora el modelo de ejemplo (un nano-Transformer entrenado para predecir el siguiente carácter/palabra).
3. Observa el flujo:
   - **Input representation:** los tokens entran como embeddings.
   - **Attention:** aparecen las líneas de atención entre tokens; cada token "mira" a otros.
   - **MLP / bloques:** la información se transforma y pasa de capa en capa.
   - **Output:** se genera la distribución sobre el siguiente token.

## Ejemplos recomendados para mostrar

- **"Apple"**: observa cómo la atención y la predicción dependen del contexto local; úsalo para ilustrar que el modelo opera sobre representaciones, no "significados" simbólicos.
- **"The dog chased the cat" vs "The cat chased the dog"**: la única diferencia es el orden de "dog" y "cat". Muestra cómo cambian las líneas de atención y, por tanto, la representación contextualizada de cada palabra. Es el ejemplo perfecto de `04_self_attention.md` ("el contexto cambia el significado").
- **Generación paso a paso:** deja que el modelo prediga carácter a carácter para ilustrar lo *autoregresivo* de `05_generacion_autoregresiva.md`.

## Qué observar (conclusiones para el alumnado)

- El modelo es **determinista dado el peso y la entrada** en este nivel: no "piensa" como humano, solo transforma vectores.
- La **atención es localizable**: puedes ver *a qué tokens atiende* cada uno.
- El **tamaño importa**: esto es un modelo minúsculo; los GPT/Gemini/Claude/Llama/Mistral/DeepSeek son los mismos bloques, pero con millones de veces más parámetros y muchas más capas. La cualidad es la misma, la escala es la diferencia.

## Puente con el resto

Esta demo es el corazón de la sección "Anatomía + Demo". Tras ver el pipeline, el alumnado tiene el mapa mental completo y está listo para la sección "Ecosistema" (`models/ecosistema_categorias.md`) y el reto (`course/reto_llm_detective.md`).
