# Slide Storyboard (PATCH v2.1 §3)

Metadatos por diapositiva núcleo. La fuente de verdad pedagógica es
`docs/run-of-show.md`; este storyboard alinea el deck con ella.

- slide_id: S01
  title: Portada
  purpose: Presentar la sesión.
  question_in: (ninguna)
  main_message: Masterclass de 60 min sobre modelos fundacionales y open-weight.
  visual: Título grande, sin stock de robots.
  speaker_note: "Bienvenida; avanzar a la pregunta del hook."
  transition_phrase: "Empecemos por una pregunta incómoda."
  question_out: ¿Cuál es el mejor LLM?
  enters_from: inicio
  hands_off_to: S02
  demo_if_any: none
  fallback: leer el título en voz alta.

- slide_id: S02
  title: Hook
  purpose: Problematizar "el mejor modelo".
  question_in: ¿Cuál es el mejor LLM?
  main_message: "Mejor" solo tiene sentido frente a un caso de uso.
  visual: Nombres de familias (GPT/Gemini/Claude/Llama/Mistral/DeepSeek).
  speaker_note: "Votad mentalmente; luego reformulo a ¿para qué?"
  transition_phrase: "Veamos qué ocurre realmente al escribir."
  question_out: ¿Qué ocurre realmente cuando escribo una frase a un LLM?
  enters_from: S01
  hands_off_to: S03
  demo_if_any: none
  fallback: proyectar nombres en texto plano.

- slide_id: S03
  title: Pregunta central
  purpose: Anclar la narrativa.
  question_in: ¿Qué ocurre realmente cuando escribo una frase a un LLM?
  main_message: Toda la clase responde a esta pregunta.
  visual: La pregunta aislada, tipografía grande.
  speaker_note: "Recordad esta pregunta en cada bloque."
  transition_phrase: "Sigamos el recorrido del texto."
  question_out: (mantiene la pregunta central)
  enters_from: S02
  hands_off_to: S04
  demo_if_any: none
  fallback: escribir la pregunta en la pizarra.

- slide_id: S04
  title: Del texto al modelo
  purpose: Mostrar el pipeline completo.
  question_in: ¿Qué ocurre realmente cuando escribo una frase a un LLM?
  main_message: Texto→Tokens→Embeddings→Transformer→Logits→Siguiente token.
  visual: Diagrama de flujo horizontal.
  speaker_note: "Un salto por diapositiva; no lo explico todo aquí."
  transition_phrase: "Empecemos por los tokens."
  question_out: ¿Qué recibe realmente el modelo?
  enters_from: S03
  hands_off_to: S05
  demo_if_any: none
  fallback: dibujar el flujo en la pizarra.

- slide_id: S05
  title: Tokens → Embeddings
  purpose: Diferenciar tokenización y representación.
  question_in: ¿Qué recibe realmente el modelo?
  main_message: Unidades tokenizadas → vectores, no palabras.
  visual: Tokens resaltados + nube de puntos.
  speaker_note: "La segmentación varía con idioma/código/símbolos."
  transition_phrase: "¿Cómo se combinan esas representaciones?"
  question_out: ¿Cómo el contexto cambia la representación?
  enters_from: S04
  hands_off_to: S06
  demo_if_any: none
  fallback: captura de Tiktokenizer en S10.

- slide_id: S06
  title: Transformer
  purpose: Modelo mental mínimo.
  question_in: ¿Cómo se combinan esas representaciones?
  main_message: Attention + MLP + residual/norm + bloques.
  visual: Bloque apilado (attention→MLP→+→norm→repeat).
  speaker_note: "Sin derivar Q/K/V en el núcleo."
  transition_phrase: "Y esto produce tokens uno a uno."
  question_out: ¿Cómo se genera el siguiente token?
  enters_from: S05
  hands_off_to: S07
  demo_if_any: none
  fallback: esquema estático del bloque.

- slide_id: S07
  title: Generación autoregresiva
  purpose: Explicar la generación.
  question_in: ¿Cómo se genera el siguiente token?
  main_message: Contexto→distribución→selección→nuevo contexto→repetición.
  visual: Bucle contexto→token.
  speaker_note: "Logits/sampling como puente a una clase posterior."
  transition_phrase: "Mecanismo común; ahora, ¿qué familias existen?"
  question_out: Si el mecanismo es común, ¿qué diferencias importan?
  enters_from: S06
  hands_off_to: S08
  demo_if_any: none
  fallback: narrar el bucle en voz alta.

- slide_id: S08
  title: Ecosistema
  purpose: Marco comparativo estable.
  question_in: Si el mecanismo es común, ¿qué diferencias importan?
  main_message: Servicio gestionado vs open-weight; open source ≠ open-weight.
  visual: Dos columnas (gestionado | open-weight).
  speaker_note: "Ubicar las 6 familias en el mapa."
  transition_phrase: "Pasemos a la evidencia visible."
  question_out: ¿Podemos ver cómo el contexto cambia las representaciones?
  enters_from: S07
  hands_off_to: S09
  demo_if_any: none
  fallback: capturas de demos en S10.

- slide_id: S09
  title: ¿Qué criterios importan?
  purpose: Ejes de decisión de ingeniería.
  question_in: ¿Podemos ver cómo el contexto cambia las representaciones?
  main_message: Capacidad, coste, latencia, contexto, privacidad, control, despliegue, licencia.
  visual: Lista de ejes como columnas comparativas.
  speaker_note: "Son ejes, no una tabla de ganadores."
  transition_phrase: "Vamos a las demos."
  question_out: (pre-demo) ¿Qué recibe realmente el modelo?
  enters_from: S08
  hands_off_to: S10
  demo_if_any: none
  fallback: leer los ejes en voz alta.

- slide_id: S10
  title: Demo
  purpose: Hacer visible tokenización y contexto.
  question_in: ¿Qué recibe realmente el modelo? / ¿Cómo el contexto cambia la representación?
  main_message: Tiktokenizer (tokens) + BBycroft (pipeline interno).
  visual: Capturas de ambas demos.
  speaker_note: "Tiktokenizer: ES/EN/código/emoji. BBycroft: input→embedding→attention→MLP→output."
  transition_phrase: "Ahora tú: detective."
  question_out: ¿Cómo decidirías tú ante un caso real?
  enters_from: S09
  hands_off_to: S11
  demo_if_any: Tiktokenizer (https://tiktokenizer.vercel.app/) y BBycroft (https://bbycroft.net/llm)
  fallback: capturas en slides/ + narrar la observación esperada.

- slide_id: S11
  title: Reto — LLM Detective
  purpose: Experimentar y decidir.
  question_in: ¿Cómo decidirías tú ante un caso real?
  main_message: Hipótesis→Experimento→Observación→Cambio de variable→Conclusión.
  visual: Pasos del método + caso asistente documental.
  speaker_note: "Parejas, 12 min. Parte A tokens; Parte B caso privado."
  transition_phrase: "Llevémoslo a un caso de empresa."
  question_out: ¿Qué investigarías antes de comprometer un modelo?
  enters_from: S10
  hands_off_to: S12
  demo_if_any: notebooks/student/LLM_Detective.ipynb
  fallback: resolver la Parte B en voz alta.

- slide_id: S12
  title: Cierre
  purpose: Consolidar y transferir.
  question_in: ¿Qué investigarías antes de comprometer un modelo?
  main_message: Representaciones · ingeniería no fe · evalúa antes.
  visual: Tres takeaways + pregunta final.
  speaker_note: "Demo RAG opcional 2–3 min si hay tiempo."
  transition_phrase: "El mapa está en el repo."
  question_out: ¿Qué caso llevarías a tu próximo proyecto?
  enters_from: S11
  hands_off_to: fin
  demo_if_any: Learning RAG (opcional)
  fallback: indicar references/sources.md.
