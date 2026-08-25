---
title: "Criterios éticos para elegir y usar LLM"
topic: etica
source_type: course
provider: na
model_family: na
course_section: cierre
difficulty: beginner
updated_at: 2026-08-25
source_url: https://www.llama.com/
---

# Criterios éticos para elegir y usar LLM

Ficha breve y práctica para cerrar la sesión. Lenguaje concreto, no moralizante: son **riesgos de ingeniería** que afectan a producto, usuario y cumplimiento.

## 1. Sesgos

Los modelos aprenden de corpus enormes con sesgos sociales, culturales y lingüísticos. Una salida puede reflejar estereotipos o desequilibrios (p. ej. subrepresentación de ciertos idiomas o grupos). No es mala voluntad del modelo: es el datos de entrenamiento y la distribución aprendida. **Mitigación:** evaluar en tu dominio, no asumir neutralidad.

## 2. Alucinaciones y limitaciones

El modelo optimiza coherencia, no verdad. Puede inventar hechos, citas o código plausible pero falso (ya lo viste en `05_generacion_autoregresiva.md`: muestrea de una distribución). **Mitigación:** no usar salidas sin verificación en decisiones críticas; combinar con recuperación (RAG) y validación humana.

## 3. Privacidad

Si usas un **servicio gestionado**, los datos de entrada pueden procesarse en servidores del proveedor. Para documentos confidenciales (el caso del reto), eso es un riesgo real. Los modelos **open-weight auto-hospedados** mantienen los datos en tu infraestructura. **Mitigación:** clasificar sensibilidad de datos antes de elegir entrega.

## 4. Licencia y condiciones

No todos los "abiertos" lo son por igual (ver `models/ecosistema_categorias.md`):
- **Llama:** licencia comunitaria con restricciones (MAU, uso aceptable, atribución).
- **Mistral 3 / gpt-oss:** Apache 2.0 (permisiva).
- **DeepSeek:** MIT (permisiva).
- **GPT/Gemini/Claude API:** servicios con términos de uso; los pesos no se entregan.

Incumplir la licencia (p. ej. superar el umbral de MAU de Llama sin acuerdo) tiene consecuencias legales. **Mitigación:** leer la licencia antes de producir.

## 5. Datos de entrenamiento (cuando se documentan)

Algunos proveedores publican *model cards* o notas de datos (p. ej. system cards de Anthropic, model cards de OpenAI/Meta). Ahí se declaran recortes de conocimiento (*knowledge cutoff*) y alcance. Cuando no se documentan, **no asumas**; trátalo como información no verificable.

## 6. Riesgo de elegir por benchmark sin evaluar el caso

Un modelo que lidera un benchmark genérico puede fallar en tu tarea concreta (idioma, jurisdicción, formato). **Mitigación:** define tu propia evaluación con datos reales de tu caso (como en el reto, Parte B).

## 7. Despliegue local/privado vs servicio gestionado

- **Local/privado (open-weight):** más control y privacidad, pero tú asumes infraestructura, coste operativo, seguridad y mantenimiento.
- **Gestionado:** menos fricción, pero menos control y posible exposición de datos.

La decisión ética y técnica suelen coincidir: se trata de **ajustar el riesgo al contexto**, no de "lo abierto es bueno y lo cerrado mal".

## Cierre

La ética aquí es ingeniería aplicada: licencia correcta, datos protegidos, evaluación propia y verificación humana. Eso cierra el mapa mental de la masterclass.
