# Instructor Guide — Explorando los LLM por dentro

Guía para que **otra persona no experta** pueda impartir la clase con seguridad. Complementa `docs/run-of-show.md` (fuente de verdad del flujo) y `docs/guion-para-docente.md` (guion literal). Duración núcleo: 60 min. No cambia estructura ni slides.

## Cómo usar este repo
1. Lee `docs/run-of-show.md` (timing y transiciones).
2. Revisa `slides/` y `activities/` antes de la sesión.
3. Abre `notebooks/student/LLM_Detective.ipynb` durante el reto.
4. Ten `references/sources.md` a mano para cualquier dato cambiante.
5. (Opcional) lanza el Learning RAG al cierre: `python -m rag.app.cli "..."`.

## Bucle de aprendizaje por segmento
Cada bloque sigue: **pregunta → intuición → experimento → observación → concepto → transferencia → siguiente pregunta**. No abras ningún recurso sin haber formulado la pregunta previa.

---

## Fichas de conceptos — qué debe entender el profesor

> No proyectes esto. Es tu chuleta. Cada ficha: qué entender, explicación sencilla, qué decir, analogía, qué NO decir, pregunta al alumnado, transición. Sin matemáticas.

### 1. Token
- **Entender:** Unidad que lee el modelo, no palabra humana. Frontera depende del tokenizador/idioma/tipo.
- **Sencillo:** Trozo de texto (palabra entera, mitad o símbolo).
- **Di:** “El modelo no lee palabras, lee tokens. ‘Hola’ puede ser 1, ‘corriendo’ 2.”
- **Analogía:** Recortar “corriendo” en “corr”+“iendo”.
- **NO:** 1 palabra = 1.3 tokens, ni BPE.
- **Pregunta:** “¿‘café’ será 1 o 2 tokens?”
- **Transición:** “¿Y qué hace con esos trozos?”

### 2. Embedding
- **Entender:** Vector denso (lista números) que sitúa el token en un espacio semántico.
- **Sencillo:** Coordenada en un mapa donde cerca = significado parecido.
- **Di:** “Cada token se vuelve un vector. ‘rey’ y ‘reina’ quedan cerca.”
- **Analogía:** Ciudades en un mapa.
- **NO:** Dimensiones (1536), entrenar embeddings.
- **Pregunta:** “¿Dónde pondríais ‘gato’ y ‘perro’?”
- **Transición:** “¿Quién mueve esos puntos?”

### 3. Contextualización
- **Entender:** El vector de un token cambia según los que le rodean.
- **Sencillo:** Misma palabra, significado distinto según frase.
- **Di:** “‘bank’ en ‘bank approved loan’ vs ‘bank by the river’ da dos vectores distintos.”
- **Analogía:** Misma persona con diferente ropa según fiesta.
- **NO:** Entrar en entrenamiento.
- **Pregunta:** “¿En cuál ‘bank’ es dinero?”
- **Transición:** “Eso lo hace la atención.”

### 4. Transformer
- **Entender:** Cadena que se repite: Attention + MLP + Residual/Norm, apilado N veces.
- **Sencillo:** Fábrica con dos estaciones que se repite.
- **Di:** “Cada bloque tiene atención (mezcla) y MLP (pule). Se apila 20-30 veces.”
- **Analogía:** Cadena de montaje.
- **NO:** Número exacto de capas/cabezas.
- **Pregunta:** “¿Qué pasa si apilo más bloques?”
- **Transición:** “Veamos la primera estación.”

### 5. Self-Attention
- **Entender:** Cada token mira a todos y decide cuánto peso darles.
- **Sencillo:** Preguntar a los compañeros para entenderte.
- **Di:** Secuencia: `token → Q/K/V → Q·K → scores → scaling → máscara causal → softmax → pesos → mezcla de V → vector contextual`. Sin fórmula. Ejemplo `The bank approved the loan` vs `The bank is next to the river` — misma palabra, atención a `loan` vs `river`.
- **Analogía:** Foco de linterna que ilumina palabras clave.
- **NO:** Derivación escalada ni multi-head math.
- **Pregunta:** “¿A qué palabra mira ‘bank’ en cada frase?”
- **Transición:** “Veamos esos tres papeles.”

### 6. Q / K / V
- **Entender:** Tres proyecciones del mismo vector con roles distintos.
- **Sencillo:** Q=lo que busco, K=lo que ofreces, V=lo que me das.
- **Di:** “Q pregunta, K responde, V aporta. Q·K dice cuánto atiendo, con eso mezclo V.”
- **Analogía:** Pregunta de examen / índice del libro / contenido de la página.
- **NO:** Matrices ni dimensiones.
- **Pregunta:** “Si Q es ‘busco préstamo’, ¿qué K pesa más?”
- **Transición:** “¿Y por qué no ve el futuro?”

### 7. Causal Attention (máscara causal)
- **Entender:** Solo mira hacia atrás, nunca adelante. Hace el modelo autoregresivo.
- **Sencillo:** No hacer trampa mirando la respuesta.
- **Di:** “La máscara tapa el futuro, como matriz triangular. Solo ve lo ya escrito.”
- **Analogía:** Escribir sin mirar la siguiente página.
- **NO:** Dibujar matriz.
- **Pregunta:** “¿Podría ver la palabra 10 si va por la 5?”
- **Transición:** “La segunda estación.”

### 8. MLP / Feed-Forward
- **Entender:** Red pequeña que transforma cada posición por separado, no mezcla tokens.
- **Sencillo:** Pule cada vector tras mezclar contexto.
- **Di:** “Attention trae info de otros; MLP transforma en cada posición. Uno mezcla, otro pule.”
- **Analogía:** Tras reunión (attention), cada uno vuelve a su mesa a trabajar (MLP).
- **NO:** Pesos, activación, dimensiones.
- **Pregunta:** “¿Mezcla MLP tokens entre sí?”
- **Transición:** “¿Cómo no se rompe al apilar?”

### 9. Residual Connection
- **Entender:** Atajo que suma entrada + salida del bloque.
- **Sencillo:** Puente que evita que se pierda señal.
- **Di:** “Como un carril extra que deja pasar la info original.”
- **NO:** Gradientes.
- **Pregunta:** “¿Qué pasa sin atajo en 30 capas?”
- **Transición:** “Y para estabilizar...”

### 10. LayerNorm
- **Entender:** Normaliza cada vector para estabilizar.
- **Sencillo:** Re-centra y re-escala para que nada explote.
- **Di:** “Pone a todos en la misma escala, como ajustar volumen.”
- **NO:** Fórmula.
- **Pregunta:** “¿Qué pasaría con números gigantes?”
- **Transición:** “Al final, ¿cómo elige palabra?”

### 11. Logits
- **Entender:** Números brutos antes de probabilidad, uno por token del vocabulario.
- **Sencillo:** Puntuación sin normalizar.
- **Di:** “Logits son las notas brutas, aún no son porcentajes.”
- **NO:** Vocab size.
- **Pregunta:** “¿Son ya probabilidades?”
- **Transición:** “Hay que convertirlos.”

### 12. Softmax
- **Entender:** Convierte logits en probabilidades que suman 1.
- **Sencillo:** De notas a porcentajes.
- **Di:** “Softmax exprime y reparte 100% entre todas las palabras.”
- **NO:** Exponencial.
- **Pregunta:** “¿Cuánto suman todas?”
- **Transición:** “¿Cómo elige?”

### 13. Autoregressive Generation
- **Entender:** Bucle contexto→logits→softmax→elige→añade→repite.
- **Sencillo:** Escribe de uno en uno mirando lo ya escrito.
- **Di:** “Predice uno, lo pega y vuelve a mirar. Por eso alucina: elige lo más probable, no lo verdadero.”
- **NO:** Beam search.
- **Pregunta:** “¿Escribe todo a la vez?”
- **Transición:** “¿Y si quiero más variedad?”

### 14. Temperature
- **Entender:** Controla aleatoriedad. Baja = conservador, alta = creativo.
- **Sencillo:** Termostato de creatividad.
- **Di:** “Temp 0 = siempre el mejor; 1.2 = más loco y variado.”
- **NO:** Fórmula.
- **Pregunta:** “¿Para código pondrías temp alta?”
- **Transición:** “Otras formas de recortar...”

### 15. Top-k
- **Entender:** Solo elige entre los k mejores.
- **Sencillo:** Podio de k candidatos.
- **Di:** “Top-k=20 → solo mira los 20 más probables.”
- **NO:** Comparar con nucleus.
- **Pregunta:** “¿k=1 qué hace?”
- **Transición:** “¿Y si quiero porcentaje?”

### 16. Top-p (nucleus)
- **Entender:** Elige entre los que suman p% de probabilidad.
- **Sencillo:** Bolsa que acumula hasta p.
- **Di:** “Top-p=0.9 → coge los que suman 90%, ignora la cola larga.”
- **NO:** Matemáticas.
- **Pregunta:** “¿p bajo es más seguro?”
- **Transición:** “Todo esto vive en un ecosistema.”

### 17. RAG
- **Entender:** Retrieval busca trozos (chunks) en índice, los pega como contexto, Generación responde citando, Grounding separa hecho de inferencia, Abstención si no hay prueba. No es fine-tuning, no entrena.
- **Sencillo:** Biblioteca que busca y cita.
- **Di:** “RAG no entrena, solo busca papeles y responde con ellos delante.”
- **NO:** Inventar re-ranker que el repo no usa.
- **Pregunta:** “¿RAG entrena el modelo?”
- **Transición:** “Vamos a verlo 3 min.”

---

## Guía bloque a bloque (60 min)

### Hook (0–5)
- Di: "¿Cuál es el mejor LLM?" → pausa → "¿Para qué?"
- Muestra Slide 2. Pregunta: ¿qué modelo votarías y por qué? Fallback: caso atención al cliente.

### Anatomía (5–20)
- Di pipeline texto→tokens→embeddings→Transformer→logits/softmax→siguiente token.
- Muestra Slides 3–7, una intuición por salto. Usa fichas 1-16 arriba.
- Transición: "El modelo opera sobre representaciones."

### Ecosistema (20–27)
- Fichas breves (lee, no improvises):
  *GPT (OpenAI, API + gpt-oss open-weight Apache, trade-off comodidad), Gemini (Google, multimodal), Claude (Anthropic, cerrado auditado), Llama (Meta open-weight licencia 700M, NO open source), Mistral (Apache, europeo eficiente), DeepSeek (MIT 1M contexto permisivo).*
- Fórmula: Elección = Requisitos (qué necesito) + Restricciones (dinero/privacidad/latencia) + Evidencia (probar con mi caso, 50 consultas reales).
- No rankings, no 20 versiones. Fuente: `references/sources.md`.

### Experimentación (27–37)
- Tiktokenizer (ver sección dedicada abajo) y BBycroft (ver sección dedicada). Fallback capturas `slides/` + narrar.

### Reto LLM Detective (37–50)
- Lanza: "En parejas, 12 min. Hipótesis→Experimento→Observación→Conclusión. Parte A tokens, Parte B caso asistente documental." Entregan 1 hipótesis + 2 observaciones + criterios. Corrige con solución modelo sin imponer marca.

### Transferencia + Cierre (50–60)
- Tres takeaways + pregunta final. Demo RAG opcional 3 min. Fallback sin RAG: `references/sources.md`.

---

## Cómo usar BBycroft en 4–5 minutos
Qué es: maqueta educativa estilo GPT que anima un Transformer nano. Qué representa: flujo Embedding→Self-Attention→Q/K/V→causal mask→softmax→MLP→bloques→output. Qué NO representa: interior literal de GPT/Gemini/Claude/Llama/Mistral/DeepSeek actuales. Config recomendada: modelo nano por defecto, frase `The bank approved the loan` vs `The bank is next to the river`. Mostrar: Embedding, Attention (pesos), Q/K/V, mask, softmax, MLP, bloques repetidos, output logits. No mostrar: heads múltiples si vas justo.

## Cómo usar Tiktokenizer (demo corta)
System=instrucciones ocultas, User=tú, Assistant=respuesta, Token IDs=números internos, Count=total. Haz 4 pegados: inglés `Hello, how are you?`, español `Hola, ¿cómo estás?`, código `def add(a,b): return a+b`, emojis `Hola 😊🚀`. Objetivo: tokens ≠ palabras, depende del contenido. No es calculadora de precios.

## TensorFlow Projector (opcional, fuera de 60min)
Qué es embedding proyectado a 2D/3D, por qué (ver cercanía), PCA (lineal), t-SNE/UMAP (no lineal), cosine (ángulo) vs euclidean (distancia). No demo obligatoria.

## FAQ y Plan B
Ver `docs/faq-profesor.md` (24 preguntas preparadas) y `docs/troubleshooting.md` (si falla Tiktokenizer/BBycroft/internet/RAG → captura alternativa).

## Rehearsal QA
Verifica en voz alta los 10 puntos de `docs/run-of-show.md` antes de dar clase.
