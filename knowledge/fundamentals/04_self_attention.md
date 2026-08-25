---
title: "Self-attention: cómo el contexto cambia el significado"
topic: self_attention
source_type: course
provider: na
model_family: na
course_section: anatomia
difficulty: intermediate
updated_at: 2026-08-25
source_url: https://bbycroft.net/llm
---

# Self-attention: cómo el contexto cambia el significado

## Intuición visual antes de la terminología

El problema de un embedding aislado es que **no sabe en qué frase está**. La palabra "banco" significa cosas muy distintas según lo que la rodea. La self-attention es el mecanismo que resuelve eso: permite a cada token **mirar a todos los demás tokens de la secuencia** y *recomputar* su representación en función de ellos.

Piénsalo como una sala donde cada palabra levanta la vista y pregunta: *"¿qué otras palabras de esta frase me ayudan a entenderme a mí misma?"*. El resultado es una representación **contextualizada**: el vector de "banco" ya no es genérico, es "banco-donde-sentarse" o "banco-donde-invertir".

## Ejemplo concreto: el contexto cambia el significado

Frase A: *"El **banco** estaba frío porque la piedra es dura."*
Frase B: *"El **banco** subió los tipos de interés este trimestre."*

El token "banco" es **el mismo número** en ambas frases tras la tokenización y el embedding inicial. Pero tras la self-attention:

- En A, "banco" presta atención a "piedra", "frío", "dura" → representación de *asiento*.
- En B, "banco" presta atención a "tipos", "interés", "trimestre" → representación de *entidad financiera*.

**Esa es la idea central:** el significado de un token se construye *en relación* con los demás, no está grabado de antemano.

## Cómo funciona, en lenguaje llano

Para cada token, la self-attention hace tres pasos conceptuales:

1. **Comparar** ese token con todos los demás para decidir *cuánta atención* prestar a cada uno (un peso de importancia).
2. **Ponderar** las representaciones de los demás según esos pesos.
3. **Combinar** esa información para producir una nueva representación del token, ya contextualizada.

El modelo aprende, durante el entrenamiento, *qué relaciones importan*. No es una regla escrita por un humano ("banco + piedra = asiento"), sino un patrón estadístico aprendido de enormes corpus.

## Capa avanzada opcional: Q / K / V

Si quieres ir un paso más allá (material *no* necesario para la masterclass), la self-attention se implementa con tres proyecciones por token:

- **Q (query / consulta):** "¿qué estoy buscando?"
- **K (key / clave):** "¿a qué tipo de token respondo?"
- **V (value / valor):** "¿qué información aporto?"

La atención es, groso modo, *comparar Q con todas las K para obtener pesos, y usar esos pesos para mezclar las V*. Los bloques suelen tener **varios heads** (multi-head attention) para atender a distintas relaciones a la vez (sintaxis, referencia, orden...). Pero recuerda: **entender Q/K/V es opcional**; lo esencial es la intuición de "cada token mira a los demás y se reescribe según el contexto".

## Por qué importa para la generación

Sin self-attention, el modelo no tendría contexto y predeciría el siguiente token "a ciegas". Con ella, la predicción autoregresiva (ver `05_generacion_autoregresiva.md`) se apoya en toda la historia ya vista.

## Visualización

En [Bbycroft LLM](https://bbycroft.net/llm) puedes ver las líneas de atención entre tokens: cómo "it" en *"The cat chased the dog and it ran"* atiende a "cat" o "dog" según el ejemplo. Pruébalo en la demo.
