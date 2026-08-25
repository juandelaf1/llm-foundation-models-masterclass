# SUPERPROMPT NINJA WARRIOR — AGENTE DE DESARROLLO
## Proyecto: Masterclass “Explorando los LLM por dentro”

Tu misión es diseñar y construir un proyecto docente completo, reproducible y mantenible para una masterclass técnica de **máximo 60 minutos** sobre modelos fundacionales comerciales y modelos abiertos/open-weight de alto impacto.

No estás creando simplemente unas diapositivas. Estás construyendo una **experiencia de aprendizaje ejecutable**, respaldada por GitHub, notebooks, experimentos interactivos, documentación y un Learning RAG.

---

## 0. REGLAS INNEGOCIABLES

1. La sesión núcleo debe poder impartirse completamente en 60 minutos.
2. La estructura debe respetar los cuatro bloques exigidos por la guía docente de referencia: contextualización/intución, demo/live coding o demostración técnica, reto de aplicación y code review/cierre técnico. Debes adaptar “live coding” a una demostración interactiva cuando programar no aporte valor pedagógico.
3. No conviertas la clase en un catálogo de modelos ni en una clase matemática avanzada de Transformers.
4. No subestimes al alumnado: tiene aproximadamente 6 meses de formación en IA y conoce redes neuronales, Deep Learning y el ecosistema actual de IA generativa.
5. Debes ser técnicamente riguroso, pero explicar cada concepto complejo con una intuición visual antes de entrar en terminología.
6. No uses “open source” como sinónimo automático de “open-weight”. Debes diferenciar ambos términos.
7. Las afirmaciones actuales sobre modelos, versiones, capacidades, licencias, despliegue o disponibilidad deben verificarse con fuentes oficiales y tener fecha de revisión.
8. No inventes benchmarks, capacidades, ventanas de contexto, precios, licencias ni características.
9. Si una afirmación no puede verificarse con una fuente primaria fiable, márcala como pendiente o elimínala.
10. La presentación debe servir de soporte al docente, no convertirse en un documento que el alumno tenga que leer.
11. Las demos son parte de la explicación, no un apéndice.
12. El RAG debe responder con grounding y referencias a las fuentes recuperadas. Si no tiene evidencia suficiente, debe decirlo.
13. No construyas un “agente multi-agent” innecesariamente complejo. Prioriza un RAG sencillo, evaluable, reproducible y útil.
14. Todo el proyecto debe poder ser mantenido por otra persona distinta del autor original.
15. El repositorio debe incluir instrucciones de ejecución, troubleshooting y criterios de aceptación.

---

## 1. OBJETIVO FORMATIVO

Al terminar la sesión, una persona del alumnado debe poder:

- explicar, a nivel conceptual-intermedio, el recorrido desde texto hasta generación de tokens;
- diferenciar tokenización, embeddings, Transformer, self-attention y generación autoregresiva;
- situar conceptualmente GPT, Gemini, Claude, Llama, Mistral y DeepSeek dentro del ecosistema actual;
- distinguir servicio/API gestionado de pesos descargables/open-weight;
- identificar los criterios de ingeniería relevantes al elegir un modelo;
- experimentar con tokenización y con representaciones/contexto/attention mediante herramientas visuales;
- justificar qué investigaría antes de seleccionar un modelo para un caso de uso.

No es objetivo que el alumnado memorice versiones, benchmarks ni tablas de parámetros.

---

## 2. IDEA PEDAGÓGICA CENTRAL

Toda la clase debe responder a una única pregunta:

> ¿Qué ocurre realmente cuando escribo una frase a un LLM?

La narrativa obligatoria:

Texto → Tokenización → Tokens → Embeddings → Transformer → Atención/MLP → Logits/Probabilidades → Siguiente token → nuevo contexto → generación.

La segunda pregunta es:

> Si esta idea es común a muchos LLM, ¿qué diferencias importan realmente al elegir un modelo?

Conclusión:

> Elegir un LLM es un problema de ingeniería: capacidades + restricciones + evaluación + coste + control + despliegue.

---

## 3. DURACIÓN Y MINUTAJE OBLIGATORIO

### 0–5 min — Hook
Pregunta: “¿Cuál es el mejor LLM?” → “¿Para qué?”

### 5–20 min — Bloque 1: Anatomía
Texto → tokens → embeddings → Transformer → generación.

### 20–30 min — Bloque 2: Ecosistema
GPT, Gemini, Claude, Llama, Mistral, DeepSeek. Comparación conceptual, no catálogo.

### 30–40 min — Bloque 3: Experimentación
Tiktokenizer + BBycroft.

### 40–52 min — Bloque 4: Reto “LLM Detective”
Dos experimentos breves + un caso de decisión.

### 52–58 min — Decisión y transferencia
Caso de uso empresarial. Criterios de selección.

### 58–60 min — Cierre
Tres takeaways y una pregunta final.

Cualquier material adicional debe quedar como “Advanced / Optional”, sin ser necesario para completar la sesión.

---

## 4. CONTENIDO TÉCNICO MÍNIMO

### 4.1 Tokenización
Explicar que el modelo procesa unidades tokenizadas, no directamente “palabras humanas”. Mostrar que el número y segmentación de tokens varían con idioma, código, símbolos y otros inputs.

### 4.2 Embeddings
Explicar que los tokens se representan mediante vectores de alta dimensión y conectar con la idea de representación aprendida.

### 4.3 Transformer
Explicar de forma visual y progresiva:
- self-attention;
- MLP/feed-forward;
- residual connections;
- normalization;
- apilado de bloques.

No convertir la sesión en una derivación matemática completa de Q/K/V.

### 4.4 Self-attention
Usar una frase donde el contexto altere la interpretación. Introducir Q/K/V solo como capa avanzada opcional si el tiempo lo permite.

### 4.5 Generación autoregresiva
Explicar:
contexto → distribución sobre siguiente token → selección → actualización del contexto → repetición.

### 4.6 Ecosistema
Presentar familias, pero enseñar sobre todo el marco de comparación:
- capacidades;
- modalidades;
- contexto;
- razonamiento;
- herramientas/agentes;
- latencia;
- coste;
- privacidad;
- control y personalización;
- despliegue;
- licencia y disponibilidad de pesos.

---

## 5. MODELOS: PRINCIPIO DE ACTUALIDAD

La presentación debe evitar comparaciones rígidas del tipo “X es el mejor”.

Debe hablar de familias y criterios estables.

En el material actual del proyecto, verifica antes de publicar:
- modelos y variantes actuales de OpenAI;
- modelos actuales de Gemini;
- familias actuales de Claude;
- modelos Llama actuales;
- modelos Mistral actuales;
- modelos DeepSeek actuales.

Para afirmaciones de OpenAI sobre open-weight, la fuente primaria actual es la documentación oficial de gpt-oss. Para Gemini, utiliza la documentación oficial de modelos y deprecaciones. Para las demás familias, usa sus portales oficiales de modelos/documentación.

Nunca copies a la clase una tabla de modelos sin registrar:
- fecha de consulta;
- URL primaria;
- modelo/versión concreta;
- alcance de la afirmación.

---

## 6. EXPERIMENTOS OBLIGATORIOS

### Experimento A — Tiktokenizer
URL: https://tiktokenizer.vercel.app/

Objetivo: hacer visible la tokenización.

Inputs mínimos:
1. una frase en español;
2. la misma idea en inglés;
3. un fragmento de código;
4. una secuencia con emoji/símbolos.

Preguntas:
- ¿cuántos tokens aparecen?
- ¿cómo se segmenta el texto?
- ¿qué implicaciones tiene para contexto/coste/latencia?

### Experimento B — BBycroft LLM Visualization
URL: https://bbycroft.net/llm

Objetivo: hacer visible la anatomía conceptual de un LLM.

Usar ejemplos donde cambie el contexto:
- “Apple” / “I ate an apple” / “Apple released a new product”;
- “The dog chased the cat” / “The cat chased the dog”.

No es obligatorio recorrer toda la interfaz. Prioriza embedding → attention → MLP → output.

### Material opcional — TensorFlow Projector
URL: https://projector.tensorflow.org/

No pertenece al núcleo de 60 minutos. Documentarlo como extensión para embeddings/visualización.

### Material descartado para el núcleo — Captum
URL: https://captum.ai/

No usar como ejercicio principal. Guardarlo como extensión de interpretabilidad avanzada.

---

## 7. RETO “LLM DETECTIVE”

Formato: parejas, máximo 12 minutos.

Metodología:

Hipótesis → Experimento → Observación → Cambio de variable → Conclusión.

El reto debe tener dos partes:

### Parte A — Tokens/contexto
Explorar dos o tres entradas y comparar segmentación/contexto.

### Parte B — Decisión de ingeniería
Caso:
“Una empresa quiere un asistente documental con información privada, presupuesto limitado, necesidad de buena latencia y posibilidad de desplegar parte de la solución en infraestructura propia.”

El alumnado debe proponer:
- requisitos;
- restricciones;
- criterios de evaluación;
- qué familias/modelos investigaría;
- qué experimento/benchmark diseñaría antes de elegir.

No exigir una respuesta única.

---

## 8. DIAPOSITIVAS

Crear 10–12 diapositivas núcleo. No superar 16 contando extensiones opcionales.

### Slide 1 — Portada
Explorando los LLM por dentro.

### Slide 2 — Hook
GPT / Gemini / Claude / Llama / Mistral / DeepSeek.
Pregunta: “¿Cuál es el mejor?”
Remate: “¿Para qué?”

### Slide 3 — Pregunta central
“¿Qué ocurre realmente cuando escribo una frase a un LLM?”

### Slide 4 — Del texto al modelo
Diagrama completo.

### Slide 5 — Tokens → embeddings
Representación visual, poco texto.

### Slide 6 — Transformer
Attention + MLP + residual + normalization + repetición.

### Slide 7 — Generación
Contexto → probabilidades → token → nuevo contexto.

### Slide 8 — Ecosistema
Servicios/API gestionados vs modelos con pesos disponibles/open-weight.
Matizar “open source” vs “open-weight”.

### Slide 9 — ¿Qué criterios importan?
Capacidad, coste, latencia, control, privacidad, despliegue, multimodalidad.

### Slide 10 — Demo
Tiktokenizer + BBycroft.

### Slide 11 — Reto
LLM Detective.

### Slide 12 — Cierre
Tres ideas clave + pregunta final.

Cada slide debe responder una sola pregunta. No uses párrafos largos.

---

## 9. PRESENTACIÓN Y DISEÑO

Herramienta recomendada para generación/maquetación: Gamma.

Uso esperado:
- usar Gamma para crear/maquetar el deck;
- revisar manualmente contenido y exactitud;
- exportar a PPTX/PDF;
- mantener en el repositorio una fuente editable o un artefacto reproducible si es posible.

La presentación debe ser visual:
- diagramas;
- flujos;
- bloques;
- comparaciones simples;
- capturas o esquemas mínimos de las demos;
- poco texto;
- tipografía grande.

Evitar:
- stock de robots/cerebros;
- slides saturadas;
- cronologías interminables;
- benchmarks sin contexto;
- tablas con 30 filas;
- exceso de iconos.

---

## 10. LEARNING RAG

Construir un RAG sencillo, reproducible y útil para el alumnado.

Objetivo:
“Pregunta sobre la masterclass y recibe una respuesta grounded en las fuentes del curso, con referencias.”

Funciones mínimas:
1. Pregunta libre.
2. Respuesta con citas/fragmentos de origen.
3. Si falta evidencia: decirlo explícitamente.
4. Filtros por categoría.
5. Comparación de modelos basada en fuentes.
6. Modo de estudio/preguntas.

Modos de interfaz recomendados:
- Aprender un concepto.
- Investigar un modelo.
- Comparar modelos.
- Ponme a prueba.
- Buscar en fuentes.

No construir en la primera versión:
- multi-agent;
- memoria compleja;
- browsing autónomo;
- workflows excesivos.

Stack inicial recomendado:
- Python;
- LlamaIndex o framework RAG equivalente sencillo;
- Chroma o vector DB equivalente sencilla;
- Streamlit o Gradio.

El diseño debe permitir cambiar modelo de embedding, LLM y vector store mediante configuración, no mediante código duplicado.

---

## 11. KNOWLEDGE BASE DEL RAG

Estructura recomendada:

knowledge/
- fundamentals/
- models/
- experiments/
- course/
- ethics/

Cada documento/chunk debe registrar metadata suficiente para filtrar:
- topic;
- source_type;
- provider;
- model_family;
- course_section;
- difficulty;
- publication/update date;
- source_url.

Prioridad de fuentes:
1. documentación oficial;
2. papers originales;
3. documentación del proyecto;
4. fuentes secundarias de alta calidad;
5. nunca usar blogs anónimos como autoridad cuando exista fuente primaria.

---

## 12. RAG: REGLAS DE RESPUESTA

El sistema debe:
- responder usando contexto recuperado;
- citar las fuentes usadas;
- distinguir hechos de inferencias;
- indicar incertidumbre;
- no fingir acceso a documentación no indexada;
- no afirmar capacidades actuales sin fuente fechada cuando el tema pueda haber cambiado;
- mostrar, cuando sea posible, el título/URL y fragmento relevante de la fuente.

Prompt del RAG: debe instruir al sistema a preferir evidencia del corpus, abstenerse cuando no hay evidencia suficiente y separar “hecho” de “inferencia”.

---

## 13. EVALUACIÓN DEL RAG

Crear un pequeño dataset de evaluación con al menos:
- 10 preguntas factuales del curso;
- 5 preguntas de comparación;
- 5 preguntas de conceptos;
- 5 preguntas donde la respuesta correcta sea “no hay suficiente evidencia”.

Evaluar al menos:
- relevancia de retrieval;
- fidelidad a fuentes;
- completitud de la respuesta;
- calidad de citas;
- tasa de abstención correcta.

No afirmar que el RAG está “evaluado” solo porque funciona con preguntas manuales.

---

## 14. NOTEBOOKS

Crear dos notebooks:

### Student
`notebooks/student/LLM_Detective.ipynb`

Debe incluir:
- contexto del ejercicio;
- instrucciones breves;
- preguntas;
- espacios para hipótesis/observaciones/conclusiones;
- celdas marcadas TODO solo cuando tenga sentido técnico;
- enlaces a las demos web.

### Solution
`notebooks/solution/LLM_Detective_solution.ipynb`

Debe incluir:
- resolución completa;
- comentarios pedagógicos;
- respuestas orientativas;
- interpretación de resultados.

No convertir el notebook en una clase de Python sobre Transformers.

---

## 15. GUÍA DEL INSTRUCTOR

Crear `docs/instructor-guide.md` con:
- objetivo de cada bloque;
- qué decir;
- qué mostrar;
- pregunta al alumnado;
- transición al siguiente bloque;
- riesgo/contingencia si la demo falla;
- versión corta de cada explicación;
- tiempo objetivo y tiempo máximo por bloque.

Debe permitir que otra persona imparta la clase.

---

## 16. TROUBLESHOOTING

Crear `docs/troubleshooting.md` con problemas típicos:
- URL de demo caída;
- interfaz de demo cambiante;
- dependencia Python incompatible;
- clave API ausente;
- límites/cuotas;
- modelo deprecado;
- error de embedding;
- colección vectorial vacía;
- respuesta RAG sin fuentes;
- fallo de notebook.

Cada incidente debe tener:
Síntoma → Causa probable → Solución → Fallback.

---

## 17. ÉTICA

Crear `docs/ethical-criteria.md` con una ficha breve que cubra:
- sesgo;
- alucinaciones/limitaciones;
- privacidad;
- licencia/condiciones;
- datos de entrenamiento cuando estén documentados;
- riesgo de selección por benchmark sin evaluar el caso de uso;
- impacto del despliegue local/privado vs servicio gestionado.

Debe utilizar lenguaje concreto, no moralizante.

---

## 18. ESTRUCTURA DEL REPOSITORIO

Crear como mínimo:

llm-foundation-models-masterclass/
├── README.md
├── LICENSE
├── pyproject.toml o requirements.txt
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

No guardar claves, secretos, tokens ni credenciales en Git.

---

## 19. README PRINCIPAL

Debe explicar:
- qué es el proyecto;
- objetivos de aprendizaje;
- duración;
- estructura;
- cómo abrir los notebooks;
- cómo ejecutar el RAG;
- variables de entorno;
- cómo actualizar las fuentes;
- cómo regenerar índices;
- cómo ejecutar evaluación;
- cómo contribuir;
- licencia;
- limitaciones conocidas.

---

## 20. FUENTES Y REFERENCIAS

Crear `references/sources.md`.

Cada fuente debe tener:
- nombre;
- proveedor;
- tipo;
- URL;
- fecha de consulta;
- qué afirmación respalda;
- si es obligatoria u opcional.

Fuentes iniciales del proyecto:
- guía PDF proporcionada por el usuario;
- vídeo YouTube proporcionado por el usuario: https://www.youtube.com/watch?v=FdZ8LKiJBhQ
- Tiktokenizer: https://tiktokenizer.vercel.app/
- BBycroft LLM visualization: https://bbycroft.net/llm
- TensorFlow Embedding Projector: https://projector.tensorflow.org/
- Captum: https://captum.ai/
- documentación oficial de cada proveedor de modelos.

No asumir que una URL sigue vigente: comprobarla durante el build/release.

---

## 21. CONTROL DE ACTUALIDAD

Crear un proceso/README de mantenimiento que indique:
- fecha de última verificación de modelos;
- fecha de última indexación del RAG;
- fuentes con versiones/model IDs;
- deprecaciones conocidas;
- próxima revisión.

Separar:

A. CONCEPTOS ESTABLES
Tokens, embeddings, attention, Transformer, autoregresión.

B. DATOS CAMBIANTES
Modelos, versiones, endpoints, precios, context windows, licencias, disponibilidad.

La presentación debe depender poco de B. El RAG puede absorber gran parte de B.

---

## 22. CRITERIOS DE CALIDAD

El resultado final debe ser:

### Pedagógicamente
- claro;
- progresivo;
- técnico sin ser árido;
- activo;
- visual;
- orientado a decisiones.

### Técnicamente
- reproducible;
- modular;
- documentado;
- verificable;
- sin secretos;
- con dependencias fijadas cuando sea razonable.

### Como experiencia
- no más de 60 minutos de núcleo;
- demos cortas y robustas;
- fallback para cada demo;
- reto realizable en pareja;
- cierre con transferencia a casos reales.

---

## 23. DEFINITION OF DONE

El proyecto NO se considera terminado hasta que:

[ ] La sesión núcleo cabe en 60 minutos.
[ ] La guía de estructura de la sesión está respetada.
[ ] Existe deck de 10–12 slides núcleo.
[ ] Existe instructor guide.
[ ] Existe notebook student.
[ ] Existe notebook solution.
[ ] Tiktokenizer está integrado como demo.
[ ] BBycroft está integrado como demo.
[ ] Projector está documentado como extensión.
[ ] Existe reto LLM Detective.
[ ] Existe criterio ético.
[ ] Existe troubleshooting.
[ ] Existe RAG funcional.
[ ] RAG devuelve fuentes/citas.
[ ] RAG tiene conjunto de evaluación.
[ ] Existen rutas de fallback para demos.
[ ] Todas las afirmaciones cambiantes tienen fuente oficial y fecha.
[ ] No hay secretos en el repositorio.
[ ] README permite que una persona nueva ejecute el proyecto.
[ ] Se ha probado desde un entorno limpio.
[ ] Se ha hecho una revisión pedagógica del flujo minuto a minuto.
[ ] Se ha comprobado que la clase sigue siendo comprensible sin material opcional.

---

## 24. PROCEDIMIENTO DE EJECUCIÓN DEL AGENTE

Ejecuta el proyecto en este orden:

FASE 1 — Analizar requisitos y extraer constraints.
FASE 2 — Crear estructura del repositorio.
FASE 3 — Preparar y verificar fuentes.
FASE 4 — Crear la especificación de contenidos.
FASE 5 — Crear el instructor guide.
FASE 6 — Crear los notebooks.
FASE 7 — Crear la primera versión de slides.
FASE 8 — Crear demos y fallback.
FASE 9 — Construir RAG.
FASE 10 — Crear evaluación del RAG.
FASE 11 — Ejecutar tests técnicos.
FASE 12 — Hacer revisión pedagógica.
FASE 13 — Revisar actualidad y fuentes.
FASE 14 — Crear artefactos finales y documentación.

No te detengas en una fase solo porque una herramienta externa no esté disponible: construye el fallback local/documental y deja el punto de integración preparado.

Cuando exista una decisión ambigua, prioriza:
1. coherencia pedagógica;
2. simplicidad operativa;
3. trazabilidad de fuentes;
4. reproducibilidad;
5. mantenibilidad.

El resultado final debe sentirse como un **proyecto docente de ingeniería de IA**, no como un conjunto de archivos generados automáticamente.
