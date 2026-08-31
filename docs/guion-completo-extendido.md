# Guion Completo Único — Explorando los LLM por dentro (60 min, palabra por palabra)

> Léelo tal cual para estudiar y dar la clase. Texto único que cubre todos los conceptos teóricos del repo. Repo: https://github.com/juandelaf1/llm-foundation-models-masterclass — Timing canónico: docs/run-of-show.md — No cambia estructura ni duración.

---

## 0:00-0:05 HOOK (Slide 2)
Di: “Buenos días. Os lanzo una pregunta trampa: ¿cuál es el mejor LLM? GPT, Gemini, Claude, Llama, Mistral o DeepSeek. Levantad la mano mentalmente.” Pausa 3s. “No hay uno mejor. La respuesta correcta es: ¿para qué? Un modelo buenísimo para resumir no es el mejor para guardar datos médicos privados. Para decidir tenemos que abrir la caja. La pregunta de toda la hora es: ¿qué ocurre realmente cuando escribo una frase a un LLM?” Pregunta a uno: “¿tú cuál usarías para un hospital?” Transición: “Veamos el viaje por dentro.”

## 0:05-0:07 TOKEN (Slide 5) — Qué debes entender: trozo que lee el modelo, no palabra.
Di: “El modelo no lee palabras, lee trozos llamados tokens. ‘Gato’ suele ser 1 token, ‘corriendo’ se parte en ‘corr’ + ‘iendo’. En inglés 4 letras por token, en español suele gastar más, el código y los emojis se trocean fino. Por eso la misma frase en dos idiomas cuesta distinto y afecta al contexto y al precio.” Analogía: recortar con tijeras. NO digas 1 palabra=1.3 tokens. Pregunta: “¿‘café’ será 1 o 2?”

## 0:07-0:09 EMBEDDING
Di: “Cada token se convierte en un vector, una lista de muchos números. Es su coordenada en un mapa. ‘Rey’ y ‘reina’ quedan cerca, ‘rey’ y ‘avión’ lejos.” Analogía: ciudades en mapa. NO dimensiones. Pregunta: “¿Dónde pondríais ‘gato’ y ‘perro’?”

## 0:09-0:11 CONTEXTUALIZACIÓN
Di: “Ese vector cambia con la frase. ‘Bank’ en ‘The bank approved the loan’ no es el mismo vector que en ‘The bank is next to the river’. Una es dinero, otra es río. Eso es contextualización. Sin ella el modelo no entendería.”

## 0:11-0:16 TRANSFORMER (Slide 6) — Qué debes entender: cadena que se repite, dos estaciones.
Di: “El Transformer es una cadena que se repite 20-30 veces. Cada bloque tiene dos estaciones.”

**Self-Attention (mezcla):** “Cada token mira a todos los demás y decide a quién hacer caso. Secuencia sin fórmula: token → Q/K/V → Q contra K → scores → escalo → máscara causal que tapa el futuro como matriz triangular → softmax reparte 100% → mezclo los V. Resultado: vector contextualizado. Q es lo que busco, K lo que ofreces, V lo que me das. Q·K pesa.” Ejemplo bank loan vs river. Analogía: foco de linterna. NO derives.

**Causal:** “Solo mira hacia atrás, no ve el futuro. Por eso es autoregresivo. Como escribir sin mirar la siguiente página.”

**MLP / Feed-Forward (pule):** Di: “Tras mezclar, una red pequeñita trabaja SOLO en cada posición. Recibe el vector contextual, lo transforma con no-linealidad y lo pule. Si Attention es preguntar a tus compañeros para entender el contexto, MLP es volver a tu mesa a pensar tú solo. Uno mezcla información de otros, otro transforma la tuya. Por eso se alternan. No mezcla tokens entre sí.” Analogía: reunión vs trabajo individual.

**Residual + LayerNorm:** “Residual es un atajo que suma entrada+salida, evita que se pierda señal. LayerNorm es como ajustar el volumen para estabilizar, re-centra y re-escala. Amortiguadores.” NO gradientes ni fórmulas.

## 0:16-0:20 GENERACIÓN AUTOREGRESIVA (Slide 7)
Di: “Al final de todos los bloques salen números brutos llamados logits, uno por palabra del vocabulario. Softmax los convierte en probabilidades que suman 100%. El modelo elige uno y lo añade, y repite: contexto→logits→softmax→elige→añade→repite. Por eso alucina: elige lo más probable, no la verdad. Para variar: Temperature baja = conservador, alta = loco y creativo. Top-k = elige entre k mejores (podio). Top-p = elige entre los que suman p% de probabilidad (bolsa). Pregunta: ¿Para código pondríais temp alta? No, baja.”

## 0:20-0:27 ECOSISTEMA (Slides 8-9) — Referencia clara de los 6 modelos asignados

Di intro: “Todos comparten lo anterior. ¿En qué se diferencian para elegir? Dos mundos: API gestionada (otro lo corre, pagas por token, datos viajan) vs open-weight (te dan los pesos, lo montas tú, datos se quedan, tú pagas GPUs). Ojo: open-weight NO es open source. Open source exige código+datos+proceso abiertos bajo licencia OSI. Muchos open-weight no lo cumplen.”

**Fichas para leer 30s cada una (sin ranking, sin 20 versiones, sin benchmarks):**

**1. GPT — OpenAI** | Tipo: API gestionada (ChatGPT/Plataforma) + open-weight gpt-oss (Apache 2.0, 20B/120B) | Despliegue propio: Sí, vía gpt-oss auto-hospedado con vLLM/Ollama | Licencia: API términos comerciales / gpt-oss Apache 2.0 | Trade-off principal: Comodidad máxima (sin infra) vs control si montas gpt-oss. Fuente: openai.com/index/introducing-gpt-oss

**2. Gemini — Google** | Tipo: API gestionada multimodal (texto+imagen+audio+vídeo) vía AI Studio/Vertex AI, familia Gemma aparte como open-weight | Despliegue propio: No en línea principal (Gemma sí) | Trade-off: Brilla si necesitas multimodal y agentes (Computer Use). No open-weight principal. Fuente: ai.google.dev/gemini-api/docs/models

**3. Claude — Anthropic** | Tipo: API gestionada vía Claude API/Bedrock/Vertex, pesos cerrados (no open-weight) | Despliegue propio: No | Niveles Opus/Sonnet/Haiku | Trade-off: Seguridad y evaluaciones publicadas (system cards), pero 0 control de pesos. Fuente: docs.anthropic.com

**4. Llama — Meta** | Tipo: open-weight (referencia) + Llama API opcional | Despliegue propio: Sí, con HuggingFace/Ollama | Licencia: Llama Community (NO open source), carve-out >700M MAU requiere permiso Meta, con Acceptable Use Policy | Trade-off: Datos se quedan en casa y puedes afinar, pero licencia restrictiva. Fuente: llama.com

**5. Mistral — Mistral AI (Francia)** | Tipo: híbrido open-weight + API La Plateforme | Despliegue propio: Sí | Licencia: Apache 2.0 (permisiva real) | Modelos 14B/8B/3B densos y Large 3 MoE 41B activos/675B totales | Trade-off: Europeo, eficiente y soberanía RGPD. Fuente: mistral.ai/news/mistral-3

**6. DeepSeek — DeepSeek** | Tipo: híbrido open-weight MIT + API | Despliegue propio: Sí | Modelos V4 Pro/Flash 1M contexto | Licencia: MIT (la más permisiva) | Trade-off: Contexto larguísimo y libertad total para tocar pesos. Fuente: api-docs.deepseek.com

Cierra: “No hay uno mejor. Elegir = Requisitos (qué necesito) + Restricciones (dinero/privacidad/latencia) + Evidencia (probar con 50 consultas reales de MI caso, mirar p95 latencia y acierto, no un benchmark de internet).”

## 0:27-0:32 TIKTOKENIZER (Slide 10) — Qué tocar y explicar
Di: “System son instrucciones ocultas, User eres tú, Assistant la respuesta. Token IDs son números internos, Token Count el total. Los especiales son solo formato, no hace falta serialización.” Haz 4 pegados exactos: inglés `Hello, how are you doing today?`, español `Hola, ¿cómo estás hoy?`, código `def add(a, b): return a+b`, emojis `Hola 😊🚀🔥`. Pregunta: “¿Veis? tokens ≠ palabras, español gasta más.” NO lo vendas como calculadora de precios. Si falla, usa captura Slide 10.

## 0:32-0:37 BBYCROFT (4-5 min)
Di al abrir: “Esto es una MAQUETA educativa estilo GPT, no es el interior real de Gemini o Claude actual. Nos sirve para ver el flujo.” Recorrido recomendado tal cual: Embedding → Self-Attention → Q/K/V → causal masking → softmax → MLP → bloques repetidos → output. Usa frases “The bank approved the loan” vs “The bank is next to the river” y “The dog chased the cat” vs “The cat chased the dog”. Muestra: Q/K/V, mask, softmax, MLP, bloques. No muestres heads múltiples si vas justo. Si falla, dibuja en pizarra Embedding→Attention→MLP.

## 0:37-0:50 RETO LLM DETECTIVE (Slide 11 + notebook student)
Di al lanzar: “En parejas, 12 min. Método: Hipótesis → Experimento (cambiando 1 cosa) → Observación → Conclusión. Parte A: hipótesis ‘el español gasta más que el inglés’ y probáis en Tiktokenizer. Parte B: caso asistente documental con información privada, presupuesto limitado, buena latencia, posible infra propia. No elijáis marca, elegid categoría y decid qué probaríais (50 consultas reales).” Qué recoger: 1 hipótesis + 2 observaciones + criterios. Cómo corregir: requisitos → restricciones → criterios → candidatos → benchmark de caso, sin imponer modelo.

## 0:50-0:57 CIERRE (Slide 12)
Di: “1. El modelo opera sobre representaciones, no sobre texto. 2. Elegir es ingeniería, no fe. 3. Evalúa con tu caso (50 consultas reales). ¿Qué caso llevaríais a vuestro proyecto?”

## 0:57-1:00 RAG (3 min) — Qué es y demo
Di: “RAG es: Retrieval busca trozos (chunks) en un índice vectorial, los pega como contexto, Generación responde citando, Grounding separa hecho de inferencia, y si no hay prueba se abstiene. No es fine-tuning, no entrena, no reentrena. En este repo: knowledge/ → ingest → chunks 900c/overlap 120 → embeddings TF-IDF (offline, intercambiable a semántico) → vectors.npy → retrieval top-5 con filtros provider/model_family → generación offline extractiva con citas o LLM si configuras API.” Demo: `python -m rag.app.cli "¿Qué diferencia open-weight de open source?"` (responde con citas) y `¿Cuántos habitantes tiene Tokio?` (se abstiene: No dispongo de evidencia...). Muestra `rag/.index/INDEX_INFO.json` y filtros `--provider meta --model-family llama`.

**Projector (fuera de 60 min, solo si preguntan):** “Un embedding proyectado a 2D con PCA (lineal) o t-SNE/UMAP (no lineal). Cosine mide ángulo (semántica), euclidean distancia recta.”

Plan B: Tiktokenizer caído → captura slide 10. BBycroft caído → pizarra. Sin internet → todo sigue offline. RAG caído → enseña `references/sources.md` y `knowledge/`.

— Fin guion único. Úsalo como texto único para estudiar y relatar. Para archivo de teoría a grandes rasgos ver `knowledge/fundamentals/*.md` y `knowledge/models/*.md` sintetizados aquí.
