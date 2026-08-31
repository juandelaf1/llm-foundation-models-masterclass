# Guion para el docente — "Explorando los LLM por dentro" — Versión literal

Léelo tal cual mañana. No necesitas saber matemáticas. Todo lo que dices está entre comillas.

---

## 0:00-0:05 HOOK — Slide 2
Di: “Buenos días. Os lanzo una pregunta trampa: ¿cuál es el mejor LLM? ¿GPT, Gemini, Claude, Llama, Mistral o DeepSeek? Levantad la mano mentalmente.” Pausa 3s. “No hay uno mejor. La respuesta correcta es: ¿para qué? Un modelo buenísimo para escribir emails no es el mejor para guardar datos médicos privados. Hoy vamos a abrir la caja negra y ver qué pasa cuando escribes una frase.”

Haz: Muestra Slide 2. Pregunta a 1 alumno: “¿tú cuál usarías para copiar en un examen? ¿y para un hospital?” NO digas ranking. Transición: “Para decidir, primero veamos qué hace por dentro.”

## 0:05-0:08 TOKEN — Slide 5
Di: “El modelo no lee palabras, lee trozos llamados tokens. Como si recortas ‘corriendo’ en ‘corr’ + ‘iendo’. ‘Gato’ puede ser 1 token, ‘corriendo’ 2. En inglés ~4 letras por token, en español suele gastar más, el código y los emojis se trocean raro. Por eso la misma frase en dos idiomas cuesta distinto y afecta al contexto y al precio.” NO digas 1 palabra=1.3 tokens. Pregunta: “¿‘café’ será 1 o 2 tokens? Lo veremos.”

## 0:08-0:11 EMBEDDING + CONTEXTUALIZACIÓN — Slide 5
Di: “Cada token se convierte en un vector, una lista de muchos números. Es su coordenada en un mapa. ‘Rey’ y ‘reina’ quedan cerca, ‘rey’ y ‘avión’ lejos. Y lo clave: ese vector cambia con el contexto. ‘bank’ en ‘The bank approved the loan’ no es el mismo vector que en ‘The bank is next to the river’. Una es dinero, otra es río. Eso es contextualización.” NO expliques dimensiones.

## 0:11-0:18 TRANSFORMER — Slide 6
Di: “El Transformer es una cadena que se repite muchas veces. Cada bloque tiene dos estaciones. Primera: Self-Attention — cada token mira a todos los demás y decide a quién hacer caso. Segunda: MLP — una red pequeñita que trabaja SOLO en cada posición, la pule. Si Attention es preguntar a tus compañeros para entender el contexto, MLP es volver a tu mesa a pensar tú solo. Uno mezcla, otro transforma. Por eso se alternan. Luego hay dos cables: Residual (atajo que deja pasar la señal) y LayerNorm (ajusta volumen para estabilizar). Se apila 20-30 veces.”

Para Q/K/V di sin fórmula: “Cada token hace tres papeles: Q lo que busco, K lo que ofreces, V lo que me das. Hago Q contra K, me da un score, escalo, aplico máscara causal — solo miro hacia atrás, no veo el futuro, como matriz triangular — paso por softmax que reparte 100% y con eso mezclo los V. Resultado: vector ya contextualizado.” Si te preguntan, repite Q=busco, K=ofreces, V=das.

## 0:18-0:20 GENERACIÓN — Slide 7
Di: “Al final salen números brutos llamados logits. Softmax los convierte en probabilidades que suman 100%. El modelo elige uno — con Temperature, Top-k, Top-p lo haces más creativo o más seguro: Temperature baja = conservador, alta = loco; Top-k = entre k mejores; Top-p = entre los que suman p% — lo añade al texto y repite. Por eso alucina: elige lo más probable, no la verdad.” NO derives softmax.

## 0:20-0:27 ECOSISTEMA — Slides 8-9
Lee fichitas sin improvisar, 30s cada una:
“GPT (OpenAI): API de pago, también gpt-oss si lo montas tú. Trade-off comodidad.”
“Gemini (Google): API multimodal foto+audio. Trade-off si necesitas multimodal.”
“Claude (Anthropic): API cerrada muy auditada. Trade-off seguridad.”
“Llama (Meta): open-weight, lo montas tú, datos se quedan en casa, pero licencia con límite 700M usuarios. NO es open source.”
“Mistral: open-weight Apache, europeo y eficiente.”
“DeepSeek: open-weight MIT, 1M contexto, el más permisivo.”
Di: “No hay uno mejor. Elegir = Requisitos (qué necesito) + Restricciones (dinero/privacidad/latencia) + Evidencia (probar con 50 consultas reales de MI caso, mirar p95 latencia y acierto, no un benchmark de internet).”

## 0:27-0:32 TIKTOKENIZER
Di: “System son instrucciones ocultas, User eres tú, Assistant la respuesta. Token IDs son números internos.” Haz 4 pegados tal cual: inglés `Hello, how are you doing today?`, español `Hola, ¿cómo estás hoy?`, código `def add(a, b): return a+b`, emojis `Hola 😊🚀🔥`. Pregunta: “¿Veis? tokens ≠ palabras.” No lo vendas como calculadora de precios. Si falla, enseña captura Slide 10.

## 0:32-0:37 BBYCROFT
Di al abrir: “Esto es una MAQUETA educativa estilo GPT, no es el interior real de Gemini o Claude actual.” Recorrido tal cual: Embedding → Self-Attention → Q/K/V → máscara causal → softmax → MLP → bloques repetidos → output. Usa frases “The bank approved the loan” vs “The bank is next to the river” y “The dog chased the cat” vs “The cat chased the dog”. No enseñes heads múltiples si vas justo.

## 0:37-0:50 RETO LLM DETECTIVE — Slide 11
Di al lanzar: “En parejas, 12 min. Método: Hipótesis → Experimento (cambiando 1 cosa) → Observación → Conclusión. Parte A: hipótesis ‘el español gasta más tokens que el inglés’ y probáis en Tiktokenizer. Parte B: caso asistente documental privada, presupuesto limitado, buena latencia, posible infra propia. No elijáis marca, elegid categoría y decid qué probaríais (50 consultas reales).” Qué recoger: 1 hipótesis + 2 observaciones + criterios. Cómo corregir: requisitos → restricciones → criterios → candidatos → benchmark de caso, sin imponer modelo.

## 0:50-0:57 CIERRE — Slide 12
Di 3 takeaways: “1. El modelo opera sobre representaciones. 2. Elegir es ingeniería, no fe. 3. Evalúa con tu caso.” Pregunta final: “¿Qué caso llevaríais a vuestro proyecto?”

## 0:57-1:00 RAG 3 MIN
Di: “Esto es RAG: Retrieval busca trozos (chunks) en un índice, los pega como contexto, Generación responde citando, Grounding separa hecho de inferencia, y si no hay prueba se abstiene. No es fine-tuning, no entrena.” Demo: `python -m rag.app.cli "¿Qué diferencia open-weight de open source?"` (responde) y `¿Cuántos habitantes tiene Tokio?` (se abstiene). Muestra `rag/.index` y filtros.

Plan B: Tiktokenizer caído → captura slide 10. BBycroft caído → dibuja en pizarra Embedding→Attention→MLP. Sin internet → todo sigue (RAG offline). RAG caído → enseña references/sources.md. NO recites precios ni Q/K/V con fórmula.
