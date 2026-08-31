---
title: "Demo opcional Projector: explorar espacios de embeddings"
topic: projector
source_type: course
provider: na
model_family: na
course_section: demo
difficulty: beginner
updated_at: 2026-08-25
source_url: https://projector.tensorflow.org/
---

# Demo opcional Projector: explorar espacios de embeddings

## Qué es

[Embedding Projector de TensorFlow](https://projector.tensorflow.org/) es una herramienta que muestra embeddings proyectados a 2D/3D. Un embedding es un vector; para verlo proyectamos a 2D/3D con **PCA** (lineal), **t-SNE** o **UMAP** (no lineales). **Cosine similarity** mide ángulo (semántica), **euclidean** mide distancia recta. Es extensión **opcional**, fuera de los 60 min.

## Por qué merece la pena (si hay tiempo)

- Hace tangible que **palabras con significado parecido caen cerca en el espacio vectorial**.
- Permite buscar un término y ver sus vecinos semánticos (p. ej. cerca de "king" aparecen "queen", "prince", "monarch").
- Ilustra relaciones de analogía (el famoso "king − man + woman ≈ queen") como geometría, no como regla.

## Cómo usarla (autónomo, 5 min)

1. Abre https://projector.tensorflow.org/
2. Carga un conjunto de ejemplo (p. ej. word embeddings pretrained) o sube tus propios vectores.
3. Prueba:
   - **Buscar** un término y observar el cluster de vecinos.
   - Cambiar el método de proyección (t-SNE / PCA / UMAP) y ver cómo se reorganizan los grupos.
   - **Aislar** una palabra y ver sus "k vecinos más cercanos".

## Qué observar

- Los embeddings son **aprendidos y continuos**: no hay una etiqueta por dimensión, pero la *estructura global* codifica semántica.
- La proximidad es útil: coseno/dot-product entre embeddings da similitud, base de buscadores semánticos y RAG.

## Puente con el resto

Conecta con `02_embeddings.md` (la teoría) y con `models/ecosistema_categorias.md` (los embeddings de fragmentos se usan en recuperación para modelos gestionados u open-weight). Es material de ampliación, no obligatorio para la sesión principal.
