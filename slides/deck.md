---
marp: true
theme: default
paginate: true
title: Explorando los LLM por dentro
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Explorando los LLM por dentro

Masterclass de 60 min · Modelos fundacionales y open-weight

---

# ¿Cuál es el mejor LLM?

GPT · Gemini · Claude · Llama · Mistral · DeepSeek

> "¿Para qué?"

---

# ¿Qué ocurre realmente cuando escribo una frase a un LLM?

La pregunta que recorre toda la clase.

---

# Del texto al modelo

```text
Texto → Tokens → Embeddings → Transformer
      → Atención/MLP → Logits → Siguiente token
```

---

# Tokens → Embeddings

- El modelo recibe **unidades**, no palabras humanas.
- Cada token → vector de alta dimensión (embedding).
- Visual: nubes de puntos, no texto.

---

# Transformer

- Self-attention (contexto).
- MLP / feed-forward.
- Conexiones residuales + normalización.
- Bloques apilados.

---

# Generación autoregresiva

Contexto → distribución sobre el siguiente token → selección →
actualiza contexto → repite.

---

# Ecosistema

- **Servicio / API gestionada** vs **open-weight**.
- "Open source" ≠ "open-weight".
- Mismos mecanismos, distinto control.

---

# ¿Qué criterios importan?

Capacidad · coste · latencia · contexto/modalidades ·
privacidad · control · despliegue · licencia.

---

# Demo

- Tiktokenizer: ¿qué recibe el modelo?
- BBycroft: ¿cómo el contexto cambia la representación?

---

# Reto — LLM Detective

Hipótesis → Experimento → Observación →
Cambio de variable → Conclusión.

---

# Cierre

1. El modelo opera sobre representaciones.
2. Elegir es ingeniería, no fe.
3. Evalúa antes de comprometerte.

¿Qué caso llevarías a tu próximo proyecto?
