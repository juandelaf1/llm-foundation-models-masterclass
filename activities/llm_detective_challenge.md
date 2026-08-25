# Actividad — LLM Detective (reto de la sesión)

Duración: 12 min máximo · En parejas · Metodología:
**Hipótesis → Experimento → Observación → Cambio de variable → Conclusión.**

## Parte A — Tokens y contexto
1. Abre https://tiktokenizer.vercel.app/
2. Introduce, por turnos:
   - una frase en español;
   - la misma idea en inglés;
   - un fragmento de código;
   - una secuencia con emoji/símbolos.
3. Anota la hipótesis ("¿cuántos tokens saldrán?") ANTES de ver el resultado.
4. observa la segmentación y discute: contexto, coste y latencia.

## Parte B — Decisión de ingeniería
Caso: *"Empresa quiere un asistente documental con información privada,
presupuesto limitado, necesidad de buena latencia y posible despliegue en
infraestructura propia."*

Proponed, sin elegir un modelo fijo:
- requisitos;
- restricciones;
- criterios de evaluación;
- qué familias/modelos investigaríais;
- qué experimento o benchmark diseñarías antes de elegir.

## Entrega
Usad `notebooks/student/LLM_Detective.ipynb` para registrar hipótesis,
observaciones y conclusiones.
