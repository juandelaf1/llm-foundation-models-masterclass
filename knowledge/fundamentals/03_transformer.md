---
title: "El Transformer: el modelo mental mínimo (sin matemáticas)"
topic: transformer
source_type: course
provider: na
model_family: na
course_section: anatomia
difficulty: intermediate
updated_at: 2026-08-25
source_url: https://bbycroft.net/llm
---

# El Transformer: el modelo mental mínimo (sin matemáticas)

## Intuición visual antes de la terminología

Imagina una **cadena de montaje**. Una caja de tokens-entrada entra por un extremo. Pasa por varias estaciones idénticas (los "bloques"), y sale por el otro lado una representación ya procesada de la que se deduce el siguiente token.

Ese es el Transformer: no un solo cálculo mágico, sino **capas apiladas que repiten el mismo tipo de operación**, refinando poco a poco la representación de cada token.

## El modelo mental que debes guardar

No hace falta derivar fórmulas. Memoriza este esquema de un **bloque** típico:

```
Input representation (embeddings + posición)
        │
        ▼
   ┌─────────────── Bloque Transformer ───────────────┐
   │                                                   │
   │   Self-Attention  ──┐                             │
   │                     ├──►  + (conexión residual)   │
   │   MLP (red feed-forward) ──┐                      │
   │                            ├──►  + (residual)     │
   │   Layer Norm (normalización)                      │
   │                                                   │
   └───────────────────────────────────────────────────┘
        │
        ▼
   (se repite N veces: bloque → bloque → ... → bloque)
        │
        ▼
   Output head  →  distribución sobre el siguiente token
```

Componentes clave, en lenguaje llano:

- **Input representation:** los embeddings de `02_embeddings.md` más una señal de **posición** (el modelo necesita saber *en qué orden* están los tokens; a diferencia de una palabra, el vector aislado no sabe su lugar).
- **Self-Attention:** permite a cada token "mirar" a los demás tokens y ajustar su representación según el contexto. (Lo desarrollamos en `04_self_attention.md`.)
- **MLP:** una red neuronal pequeña que transforma cada representación de forma independiente.
- **Conexión residual + Layer Norm:** atajos que estabilizan el entrenamiento y dejan que la información fluya sin degradarse a través de muchas capas. Por eso se pueden apilar *decenas* de bloques.
- **Bloques repetidos:** la profundidad del modelo es, en esencia, cuántas veces se aplica este bloque. Más bloques = más capacidad (y más coste).
- **Output head:** al final, del último vector se obtiene una **distribución de probabilidad sobre qué token viene a continuación** (puente con `05_generacion_autoregresiva.md`).

## Lo que NO necesitas aquí

- No hace falta escribir la fórmula de atención escalada por producto punto.
- No hace falta entender multi-head como matemática; basta con "el modelo atiende a varias relaciones a la vez".
- No confundas Transformer con "un modelo concreto": **GPT, Gemini, Claude, Llama, Mistral y DeepSeek son todos Transformers** (con variaciones de arquitectura como MoE, GQA, etc.).

## Por qué este mapa mental basta para la masterclass

El objetivo no es que derives Q/K/V, sino que cuando alguien diga "el modelo necesita contexto", entiendas que eso se resuelve en la etapa de **self-attention**; y cuando digan "cuesta porque es grande", entiendas que es por el **número de bloques y parámetros** que se ejecutan en cada token.

## Visualización recomendada

[LLM visualization de Bbycroft](https://bbycroft.net/llm) muestra exactamente este pipeline: input → embedding → attention → MLP → output, capa a capa. Usalo en la demo (ver `experiments/bbycroft.md`).

## Conexión

- Anterior: `02_embeddings.md` (de dónde sale la representación de entrada).
- Siguiente: `04_self_attention.md` (qué ocurre dentro de la caja "Self-Attention").
- Y luego: `05_generacion_autoregresiva.md` (qué hace el modelo con el output head).
