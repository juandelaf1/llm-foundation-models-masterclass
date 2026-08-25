# MASTERCLASS SPEC — Explorando los LLM por dentro
## Especificación canónica del proyecto

**Versión:** 1.0
**Duración núcleo:** 60 min máximo
**Audiencia:** alumnado con ~6 meses de formación en IA, ML, redes neuronales y Deep Learning
**Formato:** masterclass técnica + demostraciones interactivas + reto breve + Learning RAG

## 1. Propósito

La sesión pretende aterrizar el concepto de modelo fundacional sin reducirlo a una explicación superficial ni convertirlo en un catálogo de proveedores. El alumnado debe construir un mapa mental operativo: qué recibe un LLM, cómo transforma ese input y qué criterios importan al elegir una familia/modelo para un problema real.

La guía docente entregada como fuente base exige cuatro bloques: contextualización/intución, demo/live coding, reto y cierre técnico, con duración total entre 60 y 90 minutos. Esta implementación usa el mínimo permitido: 60 minutos. [Fuente: guía proporcionada por el usuario.]

## 2. Learning outcomes

Al finalizar, el alumnado podrá:

1. Explicar el pipeline texto → tokens → embeddings → Transformer → distribución → siguiente token.
2. Diferenciar tokenización, embedding y contextualización.
3. Explicar la intuición de self-attention y su relación con el contexto.
4. Explicar generación autoregresiva a nivel conceptual.
5. Situar GPT, Gemini, Claude, Llama, Mistral y DeepSeek en el ecosistema de servicios/modelos actuales.
6. Diferenciar “servicio/API gestionado”, “open-weight” y “open source” sin tratarlos como equivalentes.
7. Enumerar criterios de selección: capacidad, coste, latencia, contexto/modalidades, privacidad, control, despliegue, personalización y licencia.
8. Formular y probar una hipótesis sobre el comportamiento de un LLM.
9. Proponer un procedimiento de evaluación antes de elegir un modelo para un caso de uso.

## 3. Principio de diseño

La pregunta central debe repetirse a lo largo de la clase:

> ¿Qué ocurre realmente cuando escribo una frase a un LLM?

La sesión no debe responder esta pregunta mediante una única explicación larga, sino mediante una secuencia de:

**explicación → visualización → experimento → discusión → aplicación.**

## 4. Cronograma

| Min | Bloque | Objetivo | Artefacto |
|---:|---|---|---|
| 0–5 | Hook | Activar intuición y problematizar “el mejor modelo” | Slide 2 |
| 5–20 | Anatomía | Comprender pipeline interno | Slides 3–7 |
| 20–30 | Ecosistema | Dar marco comparativo | Slides 8–9 |
| 30–40 | Demo | Hacer visible tokenización y contexto | Tiktokenizer + BBycroft |
| 40–52 | Reto | Experimentar y decidir | LLM Detective |
| 52–58 | Transferencia | Pensar como ingeniero/a | Caso de selección |
| 58–60 | Cierre | Consolidar | Slide 12 |

## 5. Contenido técnico

### 5.1 Tokens
Explicar como unidades de procesamiento. No decir que “un token equivale a una palabra”. La demo debe mostrar variabilidad real.

### 5.2 Embeddings
Vectorización aprendida de tokens/representaciones. Conectar con el conocimiento del alumnado sobre espacios vectoriales sin entrar en entrenamiento de embeddings en detalle.

### 5.3 Transformer
Modelo mental mínimo:

Input representation → Attention → MLP → Residual/Norm → repeated blocks → output representation.

Puede mencionarse Q/K/V como “capa avanzada”, pero no requiere derivación en la sesión núcleo.

### 5.4 Generación
Presentar la generación como proceso autoregresivo y, si el tiempo lo permite, mencionar logits y sampling como puente hacia una clase posterior.

## 6. Ecosistema

### 6.1 Categorías
- Servicios/API gestionados.
- Modelos con pesos disponibles/open-weight.

### 6.2 Familias a cubrir
- GPT.
- Gemini.
- Claude.
- Llama.
- Mistral.
- DeepSeek.

### 6.3 Regla de actualidad
Las diapositivas no deben depender de nombres de versiones concretas salvo cuando sean necesarios para una demo. Para hechos cambiantes, el RAG y el registro de fuentes son la capa viva.

### 6.4 Fuentes oficiales de referencia
OpenAI ha documentado modelos open-weight gpt-oss y diferencia explícitamente su despliegue controlado de los modelos servidos por la API. [Fuente oficial: OpenAI gpt-oss, 2025–2026.] Google mantiene una guía dinámica de modelos Gemini y una página específica de deprecaciones; su catálogo actual cambia con frecuencia. [Fuentes oficiales Google AI.] Las demás familias deben documentarse con sus páginas oficiales durante el build.

## 7. Demos

### 7.1 Tiktokenizer
Objetivo: tokenización visible.

Secuencia:
1. español;
2. inglés;
3. código;
4. emoji/símbolos.

Output esperado: discusión sobre unidades, contexto, coste y eficiencia.

### 7.2 BBycroft
Objetivo: visualizar el pipeline de un LLM.

Secuencia:
1. input;
2. embedding;
3. attention;
4. MLP;
5. output.

Inputs recomendados:
- Apple;
- The dog chased the cat / The cat chased the dog;
- un caso donde el contexto desambigüe una palabra.

### 7.3 Projector
Extensión opcional para embeddings y visualización de espacios vectoriales.

## 8. Reto

Título: **LLM Detective**

Duración: 12 min máximo.

Metodología:

Hipótesis → experimento → observación → cambio de variable → conclusión.

La segunda parte del reto debe trasladar el aprendizaje a una decisión de ingeniería:

“asistente documental con información privada, presupuesto limitado, buena latencia y posible infraestructura propia.”

El alumnado debe elegir criterios, no necesariamente un modelo concreto.

## 9. Learning RAG

### Objetivo
Consolidar contenidos y permitir consulta interactiva después y durante la clase.

### Modos
1. Aprender concepto.
2. Investigar modelo/familia.
3. Comparar modelos.
4. Ponme a prueba.
5. Buscar fuentes.

### Grounding
Toda respuesta factual debe poder apuntar a documentos recuperados. La aplicación debe abstenerse cuando no haya evidencia.

### Metadatos mínimos
`topic`, `source_type`, `provider`, `model_family`, `course_section`, `difficulty`, `updated_at`, `source_url`.

## 10. Estructura de repositorio

```text
llm-foundation-models-masterclass/
├── README.md
├── LICENSE
├── pyproject.toml
├── .env.example
├── docs/
├── slides/
├── notebooks/
│   ├── student/
│   └── solution/
├── experiments/
├── activities/
├── rag/
│   ├── ingestion/
│   ├── retrieval/
│   ├── prompts/
│   ├── evaluation/
│   └── app/
├── knowledge/
├── references/
└── tests/
```

## 11. Requisitos funcionales

### Presentación
- 10–12 slides núcleo.
- Visual.
- Sin saturación.
- Compatible con demo en directo.

### Notebook alumno
- hipótesis;
- observaciones;
- preguntas;
- enlaces a demos;
- ejercicios breves.

### Notebook solución
- respuestas;
- interpretación;
- comentarios del instructor.

### RAG
- ingesta reproducible;
- retrieval;
- respuesta grounded;
- citas;
- filtros;
- comparación;
- modo quiz;
- evaluación básica.

## 12. Requisitos no funcionales

- No secrets en Git.
- Configuración mediante `.env`/config.
- Dependencias versionadas cuando sea razonable.
- README desde cero.
- Fallback para demos externas.
- Fuentes fechadas.
- Separación entre contenido estable y cambiante.

## 13. Ética

Debe existir una ficha breve sobre sesgos, limitaciones, privacidad, licencias, datos de entrenamiento cuando haya información pública, y riesgos de elegir modelos solo por benchmark.

## 14. Troubleshooting

Cada dependencia externa debe tener:
- síntoma;
- causa;
- solución;
- fallback.

## 15. Definition of Done

El repositorio está terminado cuando:

- la clase cabe en 60 min;
- el flujo respeta los cuatro bloques de la guía docente;
- el deck, notebooks, demos y RAG están conectados;
- el RAG produce citas y puede abstenerse;
- existe evaluación del RAG;
- todas las afirmaciones cambiantes tienen fuente y fecha;
- no hay secretos;
- una persona nueva puede ejecutar el proyecto;
- se ha probado la experiencia completa de principio a fin.
