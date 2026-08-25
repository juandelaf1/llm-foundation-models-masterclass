---
title: "Reto LLM Detective: hipótesis, experimento y criterios"
topic: reto
source_type: course
provider: na
model_family: na
course_section: reto
difficulty: intermediate
updated_at: 2026-08-25
source_url: https://tiktokenizer.vercel.app/
---

# Reto LLM Detective: hipótesis, experimento y criterios

Metodología central del reto (12 min de la sesión). El alumnado actúa como "detective de LLM": formula una hipótesis, la prueba, observa y saca una conclusión. No se trata de memorizar, sino de **razonar como ingeniero**.

## Metodología (aplicar en ambas partes)

```
1. HIPÓTESIS     → "Creo que X pasará porque..."
2. EXPERIMENTO   → "Voy a probar esto cambiando solo una variable"
3. OBSERVACIÓN   → "Lo que realmente ocurrió fue..."
4. CAMBIO VAR    → "Ahora cambio Y y repito"
5. CONCLUSIÓN    → "Esto significa que para este caso conviene..."
```

## Parte A — Tokens y contexto (individual/para)

Objetivo: hacer tangible `01_tokens.md` y `05_generacion_autoregresiva.md`.

- **Hipótesis:** "Un prompt en español ocupa más tokens que su traducción al inglés con el mismo sentido."
- **Experimento:** En [Tiktokenizer](https://tiktokenizer.vercel.app/), cuenta tokens de una frase en ES vs EN (y de un bloque de código). Cambia solo el idioma/código, mantén el sentido.
- **Observación:** Anota el número de tokens en cada caso.
- **Cambio de variable:** Añade un párrafo largo y observa cómo se acerca al límite de contexto de un modelo pequeño.
- **Conclusión:** El coste y la viabilidad dependen de la tokenización → elegir modelo y diseñar prompts es ingeniería, no solo "escribir bien".

## Parte B — Caso: asistente documental privado (en grupo)

**Enunciado:** Hay que construir un asistente que lea documentos internos confidenciales de una empresa, responda preguntas sobre ellos, tenga **buena latencia**, **presupuesto limitado**, y la empresa **podría tener infraestructura propia** (servidores/GPU) pero no está segura.

- Paso 1: Aplica los **criterios de selección** (`models/ecosistema_categorias.md`): capacidad, coste, latencia, contexto/modalidades, **privacidad**, control, despliegue, personalización, licencia.
- Paso 2: Discute **servicio gestionado vs open-weight**:
  - ¿Puede enviar documentos confidenciales a un API gestionado? (privacidad)
  - ¿Tiene sentido auto-hospedar un open-weight para mantener datos en casa? (control, infraestructura)
  - ¿Latencia y presupuesto limitado inclinan hacia modelo pequeño o hacia Flash? 
- Paso 3: **No elijas un modelo concreto como respuesta final**. La entrega esperada es: *"Dadas estas restricciones, la categoría de entrega recomendada es X y los criterios que pesan son Y; dentro de ahí, habría que evaluar opciones con un benchmark de nuestro caso real"*.

> Clave del reto: **nunca elegir por benchmark genérico sin evaluar el caso de uso** (ver también `ethics/criterios_eticos.md`). La conclusión es de método, no de marca.
