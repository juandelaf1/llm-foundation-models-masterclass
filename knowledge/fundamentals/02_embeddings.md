---
title: "Embeddings: convertir tokens en puntos de un espacio que el modelo entiende"
topic: embeddings
source_type: course
provider: na
model_family: na
course_section: anatomia
difficulty: beginner
updated_at: 2026-08-25
source_url: https://projector.tensorflow.org/
---

# Embeddings: convertir tokens en puntos de un espacio que el modelo entiende

## Intuición visual antes de la terminología

Ya sabemos que el texto se parte en **tokens** (números). Pero un número suelto, p. ej. `891`, no dice nada sobre significado. Necesitamos una representación que capture *relaciones*: que "rey" esté cerca de "reina", y "rey − hombre + mujer ≈ reina".

Eso es un **embedding**: un vector de alta dimensión (una lista de cientos o miles de números reales) que representa el significado de un token en un espacio vectorial.

```
"gato"  →  [0.21, -1.04, 0.88, ..., 0.03]   ∈ ℝ^1024
"perro" →  [0.19, -0.98, 0.91, ..., 0.05]
"coche" →  [-0.77, 0.42, -0.30, ..., 1.10]
```

Si dibujáramos (en 2D, por simplificar) esos vectores, "gato" y "perro" caerían cerca; "coche" quedaría lejos. **La semejanza de significado se convierte en cercanía geométrica.**

## Lo que ya conoces se aplica aquí

Si has trabajado con visión por computador o reducción de dimensionalidad, ya has visto "espacios vectoriales":

- En CNNs/clasificación, una imagen se proyecta a un vector de *features*.
- En PCA/t-SNE, proyectas datos a un espacio donde la distancia importa.

Un embedding es lo mismo, pero **aprendido**: no lo diseña un humano, sino que **el modelo lo aprende durante el entrenamiento** para que posiciones cercanas correspondan a significados o usos parecidos. No es una tabla fija de sinónimos: es una representación densa y continua.

## Por qué es el corazón del pipeline

El Transformer no opera sobre letras ni sobre palabras: opera sobre estos vectores. El embedding es el **punto de partida** que convierte cada token en algo sobre lo que se pueden hacer productos matriciales, distancias y atención.

```
tokens (números) → capa de embedding → matriz de vectores → Transformer
```

## Matizar: embeddings de token vs. de fragmento

- En la arquitectura base, cada **token** recibe un embedding.
- En tareas de recuperación (RAG, búsqueda semántica), se usan **embeddings de fragmentos de texto completos** (frases, párrafos) para buscar "por significado" y no "por palabra clave exacta".
- Herramientas como [TensorFlow Embedding Projector](https://projector.tensorflow.org/) permiten *visualizar* estos espacios y ver clusters de palabras relacionadas.

## Implicaciones de ingeniería

1. **La distancia es útil.** Coseno/dot-product entre embeddings da similitud semántica: base de buscadores, recomendadores y detectores de duplicados.
2. **No son explicables palabra a palabra.** Cada dimensión no es "género" o "tense" de forma legible; es un patrón aprendido y difuso.
3. **Dependende del modelo.** Distintos modelos producen embeddings distintos; no son intercambiables sin recalibrar.

## Conexión

- Entrada del flujo: `texto → tokens → embeddings → Transformer → atención → generación`.
- El siguiente paso (`03_transformer.md`) coloca estos vectores dentro del bloque que los transforma: atención + MLP + residuo.
