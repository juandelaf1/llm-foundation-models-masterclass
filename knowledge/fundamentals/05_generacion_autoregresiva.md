---
title: "Generación autoregresiva: predecir un token tras otro"
topic: generacion
source_type: course
provider: na
model_family: na
course_section: anatomia
difficulty: intermediate
updated_at: 2026-08-25
source_url: https://bbycroft.net/llm
---

# Generación autoregresiva: predecir un token tras otro

## Intuición visual antes de la terminología

Un LLM no "escribe un párrafo completo de golpe". Escribe **un token a la vez**, y cada token nuevo se basa en todo lo anterior. Es un proceso en bucle, como adivinar la siguiente palabra de un cuento sabiendo solo lo que llevas escrito.

A esto se le llama **generación autoregresiva**: la salida en el paso *t* se convierte en parte de la entrada del paso *t+1*.

## El bucle, paso a paso

```
contexto actual = [tokens del prompt y lo ya generado]
        │
        ▼
   Transformer procesa el contexto  →  logits (un valor por cada token del vocabulario)
        │
        ▼
   softmax(logits)  →  distribución de probabilidad sobre el siguiente token
        │
        ▼
   SELECCIÓN:  ¿tomamos el más probable? ¿muestreamos al azar?  →  token_siguiente
        │
        ▼
   contexto = contexto + token_siguiente
        │
        ▼
   ¿hemos terminado? (token de parada / longitud máxima)  ── no ──► repetir
```

### Qué significa cada pieza (el puente con lo anterior)

- **Logits:** el Transformer produce, para cada posible token del vocabulario, un número "crudo" que indica qué tan favorable es. No son probabilidades todavía.
- **Distribución (`softmax`):** se convierten esos números en probabilidades que suman 1. El modelo "dice": "dado lo que llevo, la siguiente palabra tiene un 22% de ser 'casa', 11% 'perro', etc."
- **Selección / sampling:** aquí entra el comportamiento del modelo:
  - *Greedy* (siempre el más probable) → determinista pero repetitivo.
  - *Temperatura / top-k / top-p* → introducen variedad controlada; temperatura alta = más creativo/arriesgado, baja = más conservador.
- **Actualización de contexto:** el token elegido se añade y el bucle continúa. Por eso **la latencia crece con la longitud de la respuesta** (un token por inferencia).

## Por qué importa esto para ti (ingeniería)

1. **Coste y latencia son lineales en tokens de salida.** Más largo = más caro y más lento. Diseñar respuestas acotadas importa.
2. **El contexto se "agota".** Recuerda `01_tokens.md`: cada modelo tiene un límite de ventana. En un bucle largo, los tokens iniciales pueden salir del contexto (o encarecerlo).
3. **El muestreo explica el comportamiento.** Alucinaciones, repeticiones o creatividad no son "errores mágicos": salen de cómo se muestrea esa distribución.
4. **"Autoregresivo" distingue a los LLM de otros modelos.** No generan en paralelo todo el texto; lo deciden secuencialmente, condicionado a lo ya dicho.

## Conexión con el mapa completo

`texto → tokens → embeddings → Transformer (con self-attention) → logits → distribución → selección → (se añade al contexto) → repetir`.

Has cerrado el ciclo. A partir de aquí, la pregunta ya no es *cómo funciona por dentro* (anatomía) sino *cuál modelo usar* (ecosistema, ver `models/ecosistema_categorias.md`).

## Visualización

En [Bbycroft LLM](https://bbycroft.net/llm) se aprecia cómo, al generar, cada nuevo token se alimenta de nuevo al modelo. Úsalo en la demo.
