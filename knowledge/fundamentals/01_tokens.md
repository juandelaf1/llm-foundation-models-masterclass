---
title: "Tokens: la unidad mínima que el modelo realmente lee"
topic: tokens
source_type: secondary
provider: na
model_family: na
course_section: anatomia
difficulty: beginner
updated_at: 2026-08-25
source_url: https://tiktokenizer.vercel.app/
---

# Tokens: la unidad mínima que el modelo realmente lee

## Intuición visual antes de la terminología

Cuando tú escribes *"El gato come pescado"*, **el modelo no ve esa frase como palabras humanas**. La ves tú; el modelo ve una lista de números. El puente entre tu texto y esos números se llama **tokenización**.

Piensa en un libro analógico: tú lo divides en páginas y párrafos, pero una imprenta lo divide en **caracteres tipográficos**. El modelo es la imprenta. Su unidad no es la palabra, es el **token**: un fragmento de texto (a veces una letra, a veces una sílaba, a veces una palabra entera o un símbolo) al que se le asigna un identificador numérico.

```
"I love NLP"   →   [tokens: "I", " love", " NL", "P"]   →   [40, 1234, 891, 72]
```

> El modelo no procesa español, inglés ni código. Procesa **secuencias de tokens (números)**. El significado lo aprende a partir de cómo esos números se relacionan entre sí.

## ¿Por qué importa la segmentación?

La frontera de un token **no es la frontera de una palabra**. Depende de:

- **El idioma.** El vocabulario del tokenizador suele estar optimizado para inglés. Palabras en español, francés o alemán a menudo ocupan *más* tokens que su equivalente en inglés.
- **El código fuente.** Identificadores largos (`MiClaseServicioHTTP`) se trocean de forma distinta a texto natural.
- **Símbolos y emojis.** Un emoji puede ser uno o varios tokens; la puntuación y el espaciado también cuentan.

### Ejemplo concreto (a comprobar en vivo)

Puedes verlo tú mismo en [Tiktokenizer](https://tiktokenizer.vercel.app/):

- `"Hola, ¿cómo estás?"` → quizá ~6-8 tokens.
- `"Hello, how are you?"` → a menudo menos tokens para el mismo sentido.
- Un bloque de Python de 10 líneas → docenas de tokens, uno por fragmento de símbolo/palabra clave.

## Implicaciones de ingeniería (las que importan en tu trabajo)

1. **Coste.** Los servicios gestionados cobran *por token* (entrada + salida). Más tokens = más euros. Un prompt en español puede salir más caro que en inglés por la diferencia de segmentación.
2. **Ventana de contexto.** Cada modelo tiene un límite máximo de tokens (contexto). Si tu documento supera ese límite, no entra entero: hay que truncar, resumir o usar recuperación (RAG).
3. **Latencia.** Más tokens que generar = más tiempo de respuesta. La generación autoregresiva produce un token a la vez (lo verás en `05_generacion_autoregresiva.md`).
4. **Límites de API.** Los proveedores fijan máximos por petición. Diseñar prompts y contextos eficientes no es cosmética: es ingeniería.

## Conexión con el resto del mapa

- Los tokens son la **entrada** del pipeline: `texto → tokens → embeddings → Transformer → atención → generación`.
- El siguiente paso (`02_embeddings.md`) explica cómo esos números se convierten en vectores que el modelo puede "entender" matemáticamente.

## Qué NO inventar aquí

No memorices "1 palabra = 1.3 tokens" ni cifras de vocabulario: **varía con el modelo y el tokenizador**. Lo fiable es el principio: *la segmentación no es palabra-a-palabra, y afecta a coste, contexto y latencia*. Para ver números reales de un modelo concreto, usa su tokenizador oficial (p. ej. Tiktokenizer con el modelo GPT/Claude/Llama seleccionado).
