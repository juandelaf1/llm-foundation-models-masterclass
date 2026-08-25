# Media & Presentation Guide (PATCH v2.1 §4)

La IA generativa para presentación y vídeo es **apoyo de producción OPCIONAL**.
NUNCA debe ser una dependencia en tiempo de ejecución para entender la lección.

## Roles permitidos
- Gancho de 20–40 s al inicio (Hook).
- Micro-animación conceptual corta (p. ej. cómo un token se convierte en vector).
- Recuerdo/post-clase opcional.

## Roles prohibidos
- Explicación única de un concepto técnico.
- Información que no se pueda recuperar en otro lugar del repo.
- Vídeo más largo de lo que el presupuesto de tiempo permite.
- Contenido AI decorativo sin función de aprendizaje.

## Registro por cada asset generado
Para cualquier asset de media que se añada, registrar en este archivo:
- `why`: por qué existe.
- `objective`: qué objetivo de aprendizaje soporta.
- `duration`: duración.
- `fallback`: qué se muestra si no está disponible.

## Estado actual
El proyecto se entrega con **deck basado en texto** (`slides/`, Marp markdown)
reproducible y editable, sin assets de media generados obligatorios. La
presentación recomendada en la especificación original era Gamma; aquí se
prioriza un artefacto versionable. Si se genera media con Gamma/otra tool,
registrarla arriba y mantener capturas estáticas en `slides/` como fallback.
