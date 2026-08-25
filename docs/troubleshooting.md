# Troubleshooting — incidentes típicos (SPEC §14 / SUPERPROMPT §16)

Cada incidente: Síntoma → Causa probable → Solución → Fallback.

| Incidente | Síntoma | Causa probable | Solución | Fallback |
|---|---|---|---|---|
| URL de demo caída | Tiktokenizer/BBycroft no cargan | Caída del servicio o red | Recargar; comprobar status | Capturas estáticas en `slides/` + narrar observación esperada |
| Interfaz de demo cambiante | Los controles no están donde se indicó | La web externa se actualizó | Buscar el equivalente; adaptar al momento | Usar las capturas de `slides/` |
| Dependencia Python incompatible | `pip install` falla | Versiones de numpy/llama-index | Crear venv; fijar versión en `pyproject.toml` | Modo offline solo requiere `numpy`+`python-dotenv` |
| Clave API ausente | El LLM externo no responde | `OPENAI_API_KEY`/`ANTHROPIC_API_KEY` vacías | Rellenar `.env` desde `.env.example` | El RAG funciona en modo offline (respuesta grounded sin API) |
| Límites / cuotas | 429 al llamar a la API | Cuota agotada | Esperar o cambiar de modelo | Modo offline |
| Modelo deprecado | La API rechaza el modelo | El proveedor retiró la versión | Consultar `references/sources.md` y `docs/maintenance.md` | Citar la familia, no la versión |
| Error de embedding | Fallo al generar vectores | Modelo de embedding no instalado | `pip install -e ".[rag]"` | Embedder TF-IDF offline por defecto |
| Colección vectorial vacía | El RAG no recupera nada | No se ejecutó la ingesta | `python -m rag.ingestion.ingest` | — |
| Respuesta RAG sin fuentes | "No hay evidencia" siempre | Corpus vacío o filtro malo | Verificar `knowledge/` y `rag/.index/` | Ampliar `knowledge/` y reindexar |
| Fallo de notebook | Una celda lanza error | Paquete no instalado (p.ej. tiktoken) | `pip install tiktoken` o ignorar la celda | La celda ya tiene `try/except` con fallback al navegador |

**Regla general:** toda demo externa tiene captura y narrativa de respaldo en
`slides/` y `activities/`. El modo offline del RAG garantiza que la clase no
depende de APIs de pago.
