# Explorando los LLM por dentro — Masterclass (60 min)

Experiencia docente reproducible sobre modelos fundacionales comerciales y
modelos abiertos/open-weight. No es solo un deck: incluye **diapositivas +
experimentos + notebooks + Learning RAG + documentación + evaluación**.

> Principio de producto (del Agent Pack): la entrega es una experiencia docente
> reproducible, no sólo unas diapositivas.

## Objetivos de aprendizaje
Al finalizar, el alumnado puede:
1. Explicar el pipeline texto → tokens → embeddings → Transformer → distribución → siguiente token.
2. Diferenciar tokenización, embedding y contextualización.
3. Explicar la intuición de self-attention y su relación con el contexto.
4. Explicar generación autoregresiva a nivel conceptual.
5. Situar GPT, Gemini, Claude, Llama, Mistral y DeepSeek en el ecosistema actual.
6. Diferenciar servicio/API gestionado, open-weight y open source (no son sinónimos).
7. Enumerar criterios de selección: capacidad, coste, latencia, contexto/modalidades, privacidad, control, despliegue, personalización y licencia.
8. Formular y probar una hipótesis sobre el comportamiento de un LLM.
9. Proponer un procedimiento de evaluación antes de elegir un modelo.

## Duración
**60 minutos máximo** (núcleo). Ver `docs/run-of-show.md` para el minutaje y
las transiciones. Todo lo opcional vive fuera de ese presupuesto.

## Estructura del repositorio
```
llm-foundation-models-masterclass/
├── README.md
├── LICENSE
├── pyproject.toml
├── .env.example
├── docs/            # run-of-show, instructor-guide, media-presentation-guide,
│                   # ethical-criteria, troubleshooting, maintenance
├── slides/          # deck.md (Marp) + storyboard.md
├── notebooks/       # student/ y solution/ (LLM Detective)
├── experiments/     # utilidad opcional de conteo de tokens
├── activities/      # reto LLM Detective (imprimible)
├── rag/             # ingesta, recuperación, prompts, evaluación, app
│   ├── ingestion/ retrieval/ prompts/ evaluation/ app/
├── knowledge/       # corpus del RAG (fundamentals, models, experiments,
│                   # course, ethics) con metadata y fuentes
├── references/      # sources.md
└── tests/           # tests del RAG
```

## Requisitos
- Python >= 3.10.
- Para el modo **offline** (por defecto, sin red): solo `numpy` + `python-dotenv`.
- Opcional, para semantic embeddings / LLM externo / UI:
  `pip install -e ".[rag,ui,dev]"`.

## Puesta en marcha
```bash
git clone <repo> && cd <repo>
python -m venv .venv && .venv\Scripts\activate   # o: source .venv/bin/activate
pip install -e ".[dev]"            # mínimo para tests + modo offline
cp .env.example .env               # opcional: añade API keys solo si quieres LLM externo
```

## Cómo abrir los notebooks
```bash
jupyter lab notebooks/student/LLM_Detective.ipynb
# o la versión solución: notebooks/solution/LLM_Detective_solution.ipynb
```

## Cómo ejecutar el Learning RAG
```bash
# 1) Indexar el corpus (obligatorio antes de consultar)
python -m rag.ingestion.ingest

# 2) Preguntar (modo offline: respuesta grounded sin API)
python -m rag.app.cli "¿Qué significa open-weight y cómo difiere de open source?"

# 3) (Opcional) App Streamlit
pip install -e ".[ui]"
streamlit run rag/app/app.py
```
El RAG responde desde las fuentes del curso, **cita** lo recuperado y se
**abstiene** cuando no hay evidencia suficiente. Modos: aprender concepto,
investigar modelo, comparar, ponerme a prueba y buscar fuentes.

### Variables de entorno (`.env`)
- `RAG_MODE`: `offline` (por defecto) o `llama_index`.
- `EMBEDDING_PROVIDER` / `LLM_PROVIDER`: `offline` | `openai` | `anthropic` | `local`.
- `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: opcionales (no se commitean).

## Cómo actualizar las fuentes y regenerar índices
1. Edita los documentos en `knowledge/` (respeta el frontmatter de metadata).
2. Reindexa: `python -m rag.ingestion.ingest`.
3. Reejecuta la evaluación: `python -m rag.evaluation.eval`.
4. Anota la revisión en `docs/maintenance.md`.

## Cómo ejecutar la evaluación
```bash
python -m rag.evaluation.eval     # 25 preguntas: factuales, comparación,
                                  # concepto y "sin evidencia"
python -m pytest                  # tests técnicos del RAG
```
La evaluación exige: recuperación relevante, citas, y tasa de abstinencia
correcta. No se considera "evaluado" solo porque funcione a mano.

## Contribuir
- Mantén las fuentes cambiantes (modelos, precios, licencias) en `knowledge/models/`
  con `updated_at` y `source_url` oficiales.
- No commitees secretos (ver `.gitignore`).
- Actualiza `docs/maintenance.md` al cambiar datos vivos.

## Licencia
MIT (ver `LICENSE`). El contenido de las fuentes oficiales citadas pertenece a
sus respectivos dueños; se usa con fines docentes y se enlaza a la fuente.

## Limitaciones conocidas
- El modo offline usa recuperación TF-IDF (sin red). Para abstinencia y
  semantic search robustos, configura embeddings semánticos (`EMBEDDING_PROVIDER=local`
  con `llama_index` o `openai`).
- Las afirmaciones sobre modelos/versiones/precios se revisaron el 2026-08-25;
  consúltalas en `references/sources.md` y `docs/maintenance.md` antes de usarlas.
