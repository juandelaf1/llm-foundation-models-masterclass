# FAQ del Profesor — Respuestas preparadas

¿Qué es un token? Trozo de texto que lee el modelo, no siempre palabra. Ej. “corriendo” → “corr”+“iendo”.
¿Qué diferencia hay entre token y palabra? Token es unidad técnica del tokenizador; palabra es lingüística. Tokens ≠ palabras.
¿Qué es un embedding? Vector (coordenada) de cada token donde cerca = significado parecido.
¿Qué es contextualización? Mismo token da vectores distintos según frase. Ej. bank loan vs bank river.
¿Qué hace attention? Cada token mira a los demás y decide peso.
¿Qué son Q/K/V? Q lo que busco, K lo que ofreces, V lo que me das. Q·K pesa, con eso mezclo V.
¿Qué hace el MLP? Red pequeña que pule cada posición por separado. Attention mezcla, MLP transforma.
¿Para qué sirve LayerNorm? Estabiliza, re-centra y re-escala, como ajustar volumen.
¿Qué hacen las residual connections? Atajo que suma entrada+salida, evita perder señal.
¿Qué es causal attention? Solo mira hacia atrás, tapa el futuro. Hace el modelo autoregresivo.
¿Qué es un logit? Número bruto antes de probabilidad, uno por palabra del vocabulario.
¿Qué hace softmax? Convierte logits en probabilidades que suman 100%.
¿Qué es la generación autoregresiva? Bucle predice uno, lo añade y repite.
¿Qué hace temperature? Termostato creatividad: baja conservador, alta loco.
¿Qué hace top-k? Elige solo entre k mejores.
¿Qué hace top-p? Elige entre los que suman p% de probabilidad.
¿Qué diferencia hay entre GPT y Llama? GPT API gestionada (pagas, datos viajan) vs Llama open-weight (montas tú, datos se quedan, licencia 700M).
¿Qué significa open-weight? Te dan los pesos para montar tú.
¿Open-weight significa open source? No. Open source exige código+datos+proceso abiertos. Muchos open-weight no lo cumplen.
¿Qué son los parámetros? Pesos aprendidos (números) del modelo.
¿Qué diferencia hay entre training e inference? Training aprende pesos, inference usa pesos para predecir.
¿RAG es fine-tuning? No. RAG busca docs y cita, no reentrena.
¿RAG entrena el modelo? No.
¿Por qué usar RAG? Conocimiento externo actualizable, con citas y sin reentrenar.
¿Por qué no preguntar directamente a un LLM general? Alucina, no cita tu curso, no se abstiene y envía datos fuera.
