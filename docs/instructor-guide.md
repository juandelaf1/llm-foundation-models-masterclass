# Instructor Guide — Explorando los LLM por dentro

Guía para que **otra persona** pueda impartir la clase sin reconstruir la lógica.
Complementa `docs/run-of-show.md` (fuente de verdad del flujo) y
`docs/troubleshooting.md` (fallbacks). Duración núcleo: 60 min.

## Cómo usar este repo
1. Lee `docs/run-of-show.md` (timing y transiciones).
2. Revisa `slides/` y `activities/` antes de la sesión.
3. Abre `notebooks/student/LLM_Detective.ipynb` durante el reto.
4. Ten `references/sources.md` a mano para cualquier dato cambiante.
5. (Opcional) lanza el Learning RAG al cierre: `python -m rag.app.cli "..."`.

## Bucle de aprendizaje por segmento
Cada bloque sigue: **pregunta → intuición → experimento → observación →
concepto → transferencia → siguiente pregunta**. No abras ningún recurso sin
haber formulado la pregunta previa (regla de oro del PATCH v2.1).

## Guía bloque a bloque (versión corta del docente)

### Hook (0–5)
- Qué decir: "¿Cuál es el mejor LLM?" → pausa → "¿Para qué?"
- Qué mostrar: Slide 2 (nombres de familias).
- Pregunta al alumnado: ¿qué modelo votarías y por qué?
- Riesgo/contingencia: si el alumnado se bloquea, da un caso concreto (atención al cliente).

### Anatomía (5–20)
- Versión corta: texto→tokens→embeddings→Transformer (attention+MLP+residual)→distribución→siguiente token.
- Qué mostrar: Slides 3–7, una intuición visual por salto.
- Transición: "El modelo opera sobre representaciones, no sobre texto."

### Ecosistema (20–27)
- Versión corta: servicio gestionado vs open-weight; open source ≠ open-weight.
- Ejes: capacidad, coste, latencia, contexto/modalidades, privacidad, control, despliegue, licencia.
- Transición: "Veamos evidencias con las demos."

### Experimentación (27–37)
- Tiktokenizer: pregunta "¿qué recibe el modelo?" → observar variabilidad.
- BBycroft: pregunta "¿cómo cambia el contexto la representación?" → input→embedding→attention→MLP→output.
- Fallback si caen las webs: capturas en `slides/` + narrar observación esperada.

### Reto LLM Detective (37–50)
- Metodología: Hipótesis→Experimento→Observación→Cambio de variable→Conclusión.
- Parte A (tokens/contexto) + Parte B (caso asistente documental privado).
- El alumnado propone CRITERIOS, no un modelo concreto.
- Fallback: resolver la Parte B en voz alta como ejemplo.

### Transferencia + Cierre (50–60)
- Tres takeaways + pregunta final.
- Demo RAG opcional 2–3 min: "¿Qué modelo investigarías para X?"
- Fallback sin RAG: indicar `references/sources.md`.

## Rehearsal QA (PATCH v2.1 §8)
Antes de dar la clase, verifica en voz alta:
1. Cada demo se introduce con una pregunta.
2. Cada demo termina con una observación.
3. Cada observación produce el concepto del siguiente segmento.
4. Cada transición tiene una frase explícita del docente.
5. Ningún recurso se abre "porque está disponible".
6. El límite de 60 min es realista al hablarlo en voz alta.
7. El docente puede recuperarse de cualquier fallo de demo externa con su fallback.
8. Deck, notebook, demo y RAG usan la misma terminología.
9. Ningún concepto se explica dos veces a niveles distintos sin querer.
10. El alumnado sigue la cadena sin necesitar entender la estructura interna del proyecto.
