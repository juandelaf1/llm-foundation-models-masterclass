# Run of Show — Explorando los LLM por dentro

**Documento canónico de la sesión** (INTEGRATION PATCH v2.1 §2). La presentación
y los notebooks son derivados; este archivo es la fuente de verdad pedagógica.

Tiempo núcleo: **60 minutos máximo**. La clase es UNA experiencia de
aprendizaje continua, no una colección de recursos. Bucle por segmento:

```text
QUESTION → INTUITION → EXPERIMENT → OBSERVATION → CONCEPT → TRANSFER → NEXT QUESTION
```

**Regla de oro:** nunca abras una demo, web, vídeo, notebook o el RAG sin
haber formulado PRIMERO la pregunta que ese recurso investiga.

## Presupuesto de tiempo (core)

| Segmento | Inicio | Fin | Min |
|---|---:|---:|---:|
| Hook | 0 | 5 | 5 |
| Anatomía | 5 | 20 | 15 |
| Ecosistema | 20 | 27 | 7 |
| Experimentación (demos) | 27 | 37 | 10 |
| Reto LLM Detective | 37 | 50 | 13 |
| Transferencia + Cierre/RAG | 50 | 60 | 10 |
| **Total** | | | **60** |

Todo lo opcional (Projector, Captum, vídeos) vive FUERA de este presupuesto.

## Segmentos (capa de transición estructurada)

Cada segmento expone los campos que el docente necesita para enseñar sin
reconstruir la lógica.

### S1 — Hook
- `time_start`: 0 · `time_end`: 5 · `screen_or_resource`: Slide 2
- `learning_goal`: problematizar "el mejor modelo".
- `question_in`: ¿Cuál es el mejor LLM?
- `instructor_action`: proyectar Slide 2 con los logotipos/nombres. Responder "depende" y reformular.
- `student_action`: votar mentalmente un modelo.
- `observation_expected`: el alumnado asume que hay un ganador universal.
- `conceptual_takeaway`: "Mejor" sólo tiene sentido frente a un caso de uso.
- `transition_phrase`: "Veamos para qué, y qué ocurre realmente cuando escribimos."
- `question_out`: ¿Qué ocurre realmente cuando escribo una frase a un LLM?
- `hands_off_to`: S2 · `fallback`: si no hay proyector, leer la pregunta en voz alta.

### S2 — Anatomía (Bloque 1)
- `time_start`: 5 · `time_end`: 20 · `screen_or_resource`: Slides 3–7
- `learning_goal`: recorrer texto → tokens → embeddings → Transformer → generación.
- `question_in`: ¿Qué ocurre realmente cuando escribo una frase a un LLM?
- `instructor_action`: narrar el pipeline (Slide 4), luego una diapositiva por concepto (5–7).
- `student_action`: seguir el diagrama; anotar la pregunta de cada salto.
- `observation_expected`: los tokens no son palabras; el contexto cambia la representación.
- `conceptual_takeaway`: el modelo opera sobre representaciones, no sobre texto crudo.
- `transition_phrase`: "Ya vimos qué entra y qué hace el modelo. ¿Cómo lo elegimos?"
- `question_out`: Si el mecanismo es común, ¿qué diferencias importan al elegir?
- `hands_off_to`: S3 · `fallback`: si falla la proyección, dibujar el pipeline en la pizarra.

### S3 — Ecosistema (Bloque 2)
- `time_start`: 20 · `time_end`: 27 · `screen_or_resource`: Slides 8–9
- `learning_goal`: marco comparativo estable (no catálogo de versiones).
- `question_in`: Si el mecanismo es común, ¿qué diferencias importan al elegir?
- `instructor_action`: diferenciar servicio gestionado vs open-weight; matizar open source ≠ open-weight; mostrar ejes de criterio.
- `student_action`: ubicar GPT/Gemini/Claude/Llama/Mistral/DeepSeek en el mapa.
- `observation_expected`: las familias comparten base pero difieren en control/privacidad/despliegue.
- `conceptual_takeaway`: elegir es un problema de ingeniería (capacidad + restricciones + evaluación).
- `transition_phrase`: "Hablemos de evidencias: vamos a ver el pipeline con nuestros ojos."
- `question_out`: ¿Podemos ver cómo el contexto cambia las representaciones?
- `hands_off_to`: S4 · `fallback`: usar capturas estáticas de las demos en slides/.

### S4 — Experimentación (Bloque 3: demos)
- `time_start`: 27 · `time_end`: 37 · `screen_or_resource`: Tiktokenizer + BBycroft
- `learning_goal`: hacer visible tokenización y contexto.
- `question_in`: ¿Podemos ver cómo el contexto cambia las representaciones?
- `instructor_action`:
  - Tiktokenizer (pre-pregunta "¿Qué recibe realmente el modelo?"): español→inglés→código→emoji. Observación: la segmentación no son palabras.
  - BBycroft (pre-pregunta "¿Podemos ver cómo el contexto cambia la representación?"): input→embedding→attention→MLP→output con "The dog chased the cat / The cat chased the dog".
- `student_action`: predecir número de tokens antes de mostrarlos.
- `observation_expected`: tokenización variable; el contexto altera la computación interna.
- `conceptual_takeaway`: lo invisible se vuelve tangible; el contexto es parte del cálculo.
- `transition_phrase`: "Ahora tú: investiga como detective."
- `question_out`: ¿Cómo decidirías tú ante un caso real?
- `hands_off_to`: S5 · `fallback`: capturas en `slides/` + `activities/`; si todo falla, narrar la observación esperada.

### S5 — Reto LLM Detective (Bloque 4)
- `time_start`: 37 · `time_end`: 50 · `screen_or_resource`: Notebook alumno + diapositiva 11
- `learning_goal`: experimentar (hipótesis→experimento→observación→cambio de variable→conclusión) y decidir.
- `question_in`: ¿Cómo decidirías tú ante un caso real?
- `instructor_action`: proyectar diapositiva 11; repartir parejas; guiar Parte A (tokens/contexto) y Parte B (caso asistente documental: privado, presupuesto limitado, buena latencia, posible infraestructura propia).
- `student_action`: formular hipótesis, contrastar en Tiktokenizer/BBycroft, proponer criterios (no un modelo fijo).
- `observation_expected`: la decisión depende de restricciones, no de "el mejor".
- `conceptual_takeaway`: la ingeniería evalúa antes de elegir.
- `transition_phrase`: "Llevémoslo a un caso de empresa."
- `question_out`: ¿Qué investigarías antes de comprometer un modelo?
- `hands_off_to`: S6 · `fallback`: resolver la Parte B en voz alta como ejemplo.

### S6 — Transferencia + Cierre / RAG
- `time_start`: 50 · `time_end`: 60 · `screen_or_resource`: Slide 12 + RAG (demo corta opcional 2–3 min)
- `learning_goal`: consolidar y transferir a decisiones reales.
- `question_in`: ¿Qué investigarías antes de comprometer un modelo?
- `instructor_action`: tres takeaways; preguntar "¿para qué usarías un LLM mañana?"; si hay tiempo, consulta corta al Learning RAG.
- `student_action`: formular una pregunta de selección de modelo.
- `observation_expected`: el alumnado puede enmarcar un caso con criterios.
- `conceptual_takeaway`: elegir LLM = capacidades + restricciones + evaluación + coste + control + despliegue.
- `transition_phrase`: "El mapa está en el repo; el RAG responde tus dudas después."
- `question_out`: (abierta, cierre) ¿Qué caso llevarías a tu próximo proyecto?
- `hands_off_to`: fin · `fallback`: sin RAG, indicar `references/sources.md`.

## QA de ensayo (PATCH v2.1 §8)
Ver CHECKLIST en `docs/instructor-guide.md` (sección "Rehearsal QA").
