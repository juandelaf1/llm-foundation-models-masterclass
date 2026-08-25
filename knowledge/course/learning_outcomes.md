---
title: "Learning outcomes de la masterclass"
topic: objetivos
source_type: course
provider: na
model_family: na
course_section: hook
difficulty: beginner
updated_at: 2026-08-25
source_url: https://bbycroft.net/llm
---

# Learning outcomes de la masterclass

Al finalizar la sesión de 60 minutos, el alumnado debe ser capaz de:

1. **Explicar el pipeline completo:** describir el recorrido `texto → tokens → embeddings → Transformer → self-attention → generación autoregresiva` con sus propias palabras y en el orden correcto.
2. **Diferenciar tokenización, embedding y contextualización:** saber que el modelo no lee palabras, que los tokens se convierten en vectores (embeddings) y que la self-attention los contextualiza según el resto de la secuencia.
3. **Explicar la self-attention:** articular cómo cada token "mira" a los demás para reconstruir su significado en contexto (con un ejemplo de frase donde el contexto cambia el sentido).
4. **Explicar la generación autoregresiva:** describir el bucle contexto → distribución sobre el siguiente token → selección → actualización de contexto → repetición, e identificar logits/sampling como puente.
5. **Situar los modelos principales:** ubicar GPT (OpenAI), Gemini (Google), Claude (Anthropic), Llama (Meta), Mistral (Mistral AI) y DeepSeek en el ecosistema, sabiendo su proveedor y modelo de entrega.
6. **Distinguir open-weight de open source:** matizar que no son sinónimos y reconocer qué implica cada licencia (p. ej. Llama Community License vs Apache 2.0 de Mistral 3 vs MIT de DeepSeek).
7. **Aplicar criterios de selección:** usar los ejes de capacidad, coste, latencia, contexto/modalidades, privacidad, control, despliegue, personalización y licencia para comparar opciones.
8. **Formular hipótesis y experimentar:** aplicar la metodología hipótesis → experimento → observación → cambio de variable → conclusión (reto LLM Detective).
9. **Proponer una evaluación de caso:** ante un caso real (p. ej. asistente documental privado), proponer criterios y un plan de evaluación propio en lugar de elegir un modelo por un benchmark genérico.

## Cómo mapear estos outcomes a la sesión

| Outcome | Sección de la sesión |
| --- | --- |
| 1, 2, 3, 4 | Anatomía (5–20 min) + Demo (30–40 min) |
| 5, 6, 7 | Ecosistema (20–30 min) |
| 8, 9 | Reto (40–52 min) |
| Transversal | Cierre/Ética (52–60 min) |

> Estos outcomes guían el diseño; no son un examen. La sesión los trabaja de forma experiencial, no memorística.
