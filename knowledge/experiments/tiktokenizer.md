---
title: "Demo Tiktokenizer: ver la tokenización en vivo"
topic: tiktokenizer
source_type: course
provider: na
model_family: na
course_section: demo
difficulty: beginner
updated_at: 2026-08-25
source_url: https://tiktokenizer.vercel.app/
---

# Demo Tiktokenizer: ver la tokenización en vivo

## Qué es

[Tiktokenizer](https://tiktokenizer.vercel.app/) es una herramienta web que **muestra cómo un texto se divide en tokens** para un modelo concreto (puedes elegir el tokenizador, p. ej. de la familia GPT, Claude, Llama, etc.). Es la forma más rápida de hacer *tangible* el concepto de `01_tokens.md`.

## Cómo usarla en la masterclass (5 min)

1. Abre https://tiktokenizer.vercel.app/
2. Selecciona un tokenizador conocido en el desplegable (p. ej. un modelo GPT).
3. Escribe en el cuadro de texto las siguientes secuencias y observa el resaltado de tokens:

   - **Español:** `"El gato persigue al perro por el jardín."`
   - **Inglés:** `"The cat chases the dog through the garden."`
   - **Código:** un bloque Python de ~10 líneas (p. ej. una función con bucle y comentarios).
   - **Emoji / símbolos:** `"🚀🔥 ¡Hola! 😊"`

## Qué observar (y qué conclusiones sacar)

- **La segmentación no es palabra-a-palabra.** Una palabra puede ser 1, 2 o más tokens; un espacio o signo de puntuación cuenta.
- **Varía con el idioma.** El mismo sentido en español suele ocupar *más* tokens que en inglés. Esto ilustra por qué el coste y la ventana de contexto dependen del idioma.
- **Varía con el tokenizador.** Cambia el modelo seleccionado y verás que la misma frase se trocea distinto: no hay "el tokenizador", hay uno por familia.
- **Código y símbolos se fragmentan finamente.** Cada identificador, operador y espacio puede ser su propio token → los prompts con mucho código consumen más contexto.
- **Implicaciones de ingeniería:** coste (por token), latencia y límites de contexto se vuelven concretos al ver los números subir en tiempo real.

## Puente con el resto

Esta demo cierra el primer eslabón del mapa: `texto → tokens`. De ahí se pasa a `02_embeddings.md` (esos tokens se convierten en vectores). En la sesión, tras Tiktokenizer se recomienda pasar a la visualización de Bbycroft (`experiments/bbycroft.md`) para ver el resto del pipeline.
