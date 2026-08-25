# Criterios éticos — ficha breve (SPEC §13 / SUPERPROMPT §17)

Lenguaje concreto, no moralizante. Úsala en el cierre o como lectura de apoyo.

## Sesgos
Los modelos aprenden de datos con sesgos sociales e históricos; pueden
reproducirlos en la salida. No son árbitros neutrales. Mitigación: evaluar en
el caso de uso, no fiarse de la demo aislada.

## Alucinaciones y limitaciones
Un LLM produce el token más probable, no "la verdad". Puede inventar hechos
con fluidez. Diseña con verificación humana o retrieval (como este RAG) cuando
la exactitud importa.

## Privacidad
Datos de entrada pueden usarse para entrenar o registrarse en servicios
gestionados. Para información sensible (caso asistente documental privado),
valora despliegue propio / open-weight y acuerdos de tratamiento (DPA).

## Licencia y condiciones
"Open source" ≠ "open-weight". Un modelo de pesos abiertos puede tener
licencias con restricciones de uso/comercialización (revisa la licencia
concreta: Apache 2.0, MIT, o licencias comunitarias con cláusulas). Una API
gestionada tiene términos de servicio y puede cambiar sin aviso.

## Datos de entrenamiento
Algunos proveedores publican resúmenes de datos de entrenamiento; otros no.
No asumas transparencia total. Cita la fuente oficial cuando exista.

## Riesgo de elegir por benchmark
Los benchmarks no son el caso de uso. Elegir "el que gana en un líderboard"
sin evaluar tu tarea concreta es un sesgo de selección. Diseña un experimento
(propio) antes de comprometerte.

## Despliegue local/privado vs servicio gestionado
Local/open-weight: más control y privacidad, pero requiere infraestructura y
operación. Gestionado: menos fricción, pero menos control y posibles
restricciones de datos. La decisión es de ingeniería, no de fe.
