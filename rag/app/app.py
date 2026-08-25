"""App Streamlit del Learning RAG.

Modos de interfaz (SUPERPROMPT §10):
  - Aprender un concepto
  - Investigar un modelo
  - Comparar modelos
  - Ponme a prueba
  - Buscar en fuentes

Ejecutar:  streamlit run rag/app/app.py
Requiere el paquete opcional `ui` (pip install -e ".[ui]"). La recuperación y
el modo offline funcionan sin credenciales.
"""
from __future__ import annotations

import os

import streamlit as st

from rag.app.ask import ask
from rag.config import get_settings

st.set_page_config(page_title="Learning RAG — LLM por dentro", page_icon="🧠")

MODES = {
    "Aprender un concepto": {},
    "Investigar un modelo": {"model_family": None},
    "Comparar modelos": {},
    "Ponme a prueba": {},
    "Buscar en fuentes": {},
}

st.title("🧠 Learning RAG — Explorando los LLM por dentro")
st.caption("Respuestas grounded en las fuentes del curso. Sin evidencia, el sistema se abstiene.")

mode = st.sidebar.selectbox("Modo", list(MODES))
query = st.text_area("Tu pregunta", height=100, placeholder="¿Qué ocurre cuando escribo una frase a un LLM?")

filters = {}
if mode == "Investigar un modelo":
    fam = st.sidebar.text_input("Familia (gpt, gemini, llama, ...)")
    if fam:
        filters["model_family"] = fam

if st.button("Preguntar") and query.strip():
    with st.spinner("Recuperando contexto..."):
        res = ask(query, filters=filters or None)
    st.markdown(res["answer"])
    if res["citations"]:
        st.subheader("Citas")
        for c in res["citations"]:
            st.markdown(f"- [{c.get('title')}]({c.get('url')})")
    st.caption(f"Modo: {res['mode']} · fragmentos: {res['num_retrieved']} · "
               f"abstinencia: {res['abstained']}")
else:
    st.info("Escribe una pregunta y pulsa Preguntar. Configura LLM/embeddings en `.env`.")
