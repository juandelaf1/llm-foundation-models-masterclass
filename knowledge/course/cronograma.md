---
title: "Cronograma de la masterclass (60 minutos)"
topic: cronograma
source_type: course
provider: na
model_family: na
course_section: hook
difficulty: beginner
updated_at: 2026-08-25
source_url: https://bbycroft.net/llm
---

# Cronograma de la masterclass (60 minutos)

Masterclass: **"Explorando los LLM por dentro"** — 60 minutos, alumnado con ~6 meses de formación en IA/DL. Objetivo: construir el mapa mental `texto → tokens → embeddings → Transformer → atención → generación autoregresiva` y criterios de selección de modelo.

## Minutaje

| Minutos | Sección | Actividad |
| --- | --- | --- |
| **0–5** | Hook | Apertura: ¿cómo "lee" un modelo un texto? Pregunta provocadora. Fijar expectativas: no es un catálogo de modelos ni matemáticas de Transformers. |
| **5–20** | Anatomía | Pipeline núcleo con fundamentos `01_tokens.md` → `02_embeddings.md` → `03_transformer.md` → `04_self_attention.md` → `05_generacion_autoregresiva.md`. Intuición visual antes que fórmulas. |
| **20–27** | Ecosistema | Servicios gestionados vs open-weight (`models/ecosistema_categorias.md`) y situar GPT/Gemini/Claude/Llama/Mistral/DeepSeek (`models/*.md`). Matizar open-weight ≠ open source. |
| **27–37** | Experimentación (demos) | En vivo: Tiktokenizer (`experiments/tiktokenizer.md`) + BBycroft (`experiments/bbycroft.md`). Hacer tangible tokenización y pipeline. |
| **37–50** | Reto | Metodología hipótesis→experimento→observación→conclusión (`course/reto_llm_detective.md`). Parte A (tokens/contexto) y Parte B (caso asistente documental privado). |
| **50–60** | Transferencia + Cierre/RAG | Conectar con su práctica: cómo aplicarían estos criterios en un proyecto real; ética breve (`ethics/criterios_eticos.md`) y demo corta opcional del Learning RAG. Recap y preguntas. |

## Reglas de oro para mantener los 60 min

- La sección **Anatomía** es el núcleo: no te extiendas en derivadas de Q/K/V (material opcional).
- La sección **Ecosistema** da nombres reales pero remite a las fichas `models/*.md` para datos cambiantes; no recites precios en vivo.
- La **Demo** debe ser en vivo y breve; si el tiempo aprieta, recorta Projector (es opcional, `experiments/projector.md`).
- El **Reto** es donde el alumnado "hace", no solo escucha: reserva bien esos 12 minutos.

## Recursos por sección

- Hook/Anatomía: `fundamentals/*.md`
- Ecosistema: `models/*.md`
- Demo: `experiments/*.md`
- Reto: `course/reto_llm_detective.md`, `course/learning_outcomes.md`
- Cierre/Ética: `ethics/criterios_eticos.md`
