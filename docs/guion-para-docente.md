# Guion para el docente — "Explorando los LLM por dentro"

No necesitas saber matemáticas de Transformers para dar esta clase. Aquí está
TODO lo que dices, con los conceptos explicados en lenguaje sencillo. Léelo
antes de clase; el día del examen (la clase) solo proyectas y hablas.

---

## PARTE 0 — Los conceptos que tú debes entender

### ¿Qué es un LLM?
Un "Modelo de Lenguaje de Gran Escala" (LLM): un programa entrenado con
montones de texto que, dado un texto inicial, **predice el siguiente trozo de
texto**. Ejemplos: ChatGPT, Gemini, Claude, Llama, Mistral, DeepSeek.

### ¿Qué es un token?
El modelo NO recibe "palabras" tal cual. Recibe **tokens**: pedacitos de texto.
- Un token puede ser una palabra entera, parte de una palabra, o un símbolo.
- "gato" suele ser 1 token; "corriendo" a veces se parte en 2.
- En inglés ~4 letras = 1 token; en español y otros idiomas a veces más.
- El **código** y los **emojis** se trocean de forma rara.
Consecuencia: el mismo mensaje en distintos idiomas cuesta distinto número de
tokens → eso afecta **precio** y **límite de contexto**.

### ¿Qué es un embedding?
Cada token se convierte en un **vector** (una lista de números, p.ej. 1536
números) en un espacio de muchas dimensiones. Textos parecidos quedan "cerca"
en ese espacio. Esa es la **representación** con la que el modelo calcula, no
el texto en sí.

### ¿Qué es un Transformer?
La arquitectura base de estos modelos. Cuatro piezas que se repiten:
1. **Self-attention** (auto-atención): cada token "mira" a los demás y decide
   cuánta atención prestarle según el contexto.
2. **MLP** (capa feed-forward): procesa esa información.
3. **Conexiones residuales + normalización**: estabilizan el entrenamiento.
4. **Bloques apilados**: eso se repite muchas capas (por eso son "grandes").
No necesitas la fórmula de Q/K/V para esta clase.

### ¿Qué es self-attention? (la idea clave)
El significado de una palabra cambia con el contexto. Ejemplo con "Apple":
- "Me comí una **Apple**" → la representación apunta a la fruta.
- "**Apple** presentó un iPhone" → apunta a la empresa.
El modelo ajusta la representación según las palabras de alrededor. Eso es atención.

### ¿Qué es generación autoregresiva?
El modelo no escribe todo de golpe. Mira el contexto hasta ahora → calcula
**probabilidades para el siguiente token** → elige uno (el más probable o
muestreando) → lo añade al contexto → repite. De ahí que pueda **alucinar**
(inventar): elige el token más probable, no la "verdad".

### El ecosistema (familias)
- **GPT** (OpenAI): sobre todo API gestionada; también tiene pesos abiertos (gpt-oss).
- **Gemini** (Google): API gestionada, multimodal.
- **Claude** (Anthropic): API gestionada.
- **Llama** (Meta): **open-weight** con licencia comunitaria.
- **Mistral**: **open-weight**, licencia Apache.
- **DeepSeek**: **open-weight**, licencia MIT.

**Diferencia clave que debes soltar:**
- *Servicio / API gestionada*: otro corre el modelo; tú pagas por uso; tus datos
  viajan a sus servidores.
- *Open-weight*: te dan los pesos; tú lo corres donde quieras (más privado y
  controlable), pero tú pones la infraestructura.
- *Open source* estricto es **más** que open-weight (código, datos y proceso
  abiertos). No digas "open source" si solo es open-weight.

### Criterios para elegir un modelo (la conclusión)
Capacidad, coste, latencia, contexto/modalidades, privacidad, control,
despliegue y licencia. **Elegir es ingeniería, no fe.**

---

## PARTE 1 — GUION HABLADO (60 minutos)

### 0:00–0:05 — HOOK (Slide 2)
> "Hoy vamos a abrir la caja negra de los LLM. Empiezo con una pregunta:
> ¿cuál es el mejor LLM? ChatGPT, Gemini, Claude, Llama, Mistral, DeepSeek...
> levantad la mano mentalmente. (pausa) La respuesta es: depende. ¿Para qué?
> Un modelo 'mejor' para escribir código no lo es para datos súper privados.
> Hoy veremos qué ocurre realmente cuando escribís una frase a uno de estos."

### 0:05–0:20 — ANATOMÍA (Slides 3–7)
- Slide 3 (pregunta central): "La pregunta que responde toda la clase: ¿qué
  ocurre realmente cuando escribo una frase a un LLM?"
- Slide 4 (pipeline): "El viaje es: Texto → Tokens → Embeddings → Transformer
  → Atención/MLP → Logits (probabilidades) → Siguiente token."
- Slide 5 (tokens→embeddings): "El modelo no lee palabras. Recibe tokens, y
  cada token se vuelve un vector. No son letras, es una representación
  matemática."
- Slide 6 (Transformer): "El Transformer tiene atención (cada token mira a los
  demás), una capa MLP, y se apila muchas veces. Por eso es 'grande'."
- Slide 7 (generación): "No escribe todo a la vez: predice un token, lo añade,
  y repite. Por eso a veces inventa: elige el más probable, no la verdad."

### 0:20–0:27 — ECOSISTEMA (Slides 8–9)
- Slide 8: "Hay dos grandes formas de usarlos: API gestionada (otro corre el
  modelo) u open-weight (te dan los pesos, tú lo corres). Ojo: open source NO
  es lo mismo que open-weight."
- Slide 9: "Para elegir miras ejes: capacidad, coste, latencia, contexto,
  privacidad, control, despliegue, licencia. No un solo benchmark."

### 0:27–0:37 — DEMOS (Slide 10 + webs)
Ver la parte "Demos paso a paso" abajo.

### 0:37–0:50 — RETO LLM DETECTIVE (Slide 11 + notebook)
"En parejas, 12 minutos. Método: Hipótesis → Experimento → Observación →
Cambio de variable → Conclusión.
- Parte A: comparad la tokenización de un texto en español, inglés, código y
  emoji en Tiktokenizer. ¿Cuántos tokens salen? ¿Por qué importa?
- Parte B: una empresa quiere un asistente con información privada, presupuesto
  limitado, buena latencia y posible infra propia. ¿Qué criterios pondríais?
  (No digáis un modelo concreto; decid cuándo investigar cada opción.)"

### 0:50–1:00 — CIERRE (Slide 12)
"Tres ideas: 1) el modelo opera sobre representaciones, no sobre texto crudo;
2) elegir un LLM es ingeniería, no fe; 3) evaluad antes de comprometeros.
Pregunta final: ¿qué caso llevaríais a vuestro próximo proyecto?"

---

## PARTE 2 — DEMOS paso a paso

### Tiktokenizer (https://tiktokenizer.vercel.app/)
1. Escribe en la caja: *"El modelo procesa tokens, no palabras."*
2. Pregunta a la clase: "¿cuántos tokens creéis?" — que contesten.
3. Mostrad el resultado. Luego pegad la MISMA idea en inglés y comparad.
4. Probad un fragmento de **código** y un **emoji/símbolo**.
5. Observación que deben sacar: la segmentación no son palabras humanas; varía
   con idioma/código/símbolos → afecta contexto, coste y latencia.

### BBycroft (https://bbycroft.net/llm)
1. Escribid: *"The dog chased the cat"*.
2. Luego: *"The cat chased the dog"*.
3. Enseñad cómo cambia la representación interna al cambiar el contexto.
4. Recorred visualmente: input → embedding → attention → MLP → output.
5. Observación: el contexto altera el cálculo dentro del modelo.

### Si una web falla
Tenéis capturas en `slides/` y el guión de qué decir en `docs/troubleshooting.md`.
Narrá la observación esperada y seguid.

---

## PARTE 3 — Fallbacks (por si algo falla)
- Demo caída → usáis capturas en `slides/` y narráis la observación esperada.
- Sin proyector → leéis las preguntas en voz alta desde `docs/run-of-show.md`.
- El RAG no hace falta en la clase núcleo; es para después.

## PARTE 4 — Qué NO explicar (para no liar)
- No derivéis Q/K/V ni backpropagation.
- No recitéis precios ni versiones (caducan); remitid a `references/sources.md`.
- No tratéis los modelos como un catálogo de ganadores.
