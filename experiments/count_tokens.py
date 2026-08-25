"""Utilidad opcional de experimentación: contar tokens con tiktoken.

No es necesaria para la sesión núcleo; la demo web Tiktokenizer es el recurso
principal. Este script sirve para experimentar desde código y como apoyo al
reto LLM Detective. Requiere `pip install tiktoken` (tiene fallback claro).
"""
from __future__ import annotations


def count_tokens(text: str, encoding: str = "cl100k_base") -> int:
    try:
        import tiktoken
        enc = tiktoken.get_encoding(encoding)
        return len(enc.encode(text))
    except Exception:
        # Fallback sin dependencias: aproximación muy gruesa (~4 chars/token).
        return max(1, len(text) // 4)


if __name__ == "__main__":
    samples = {
        "español": "El modelo procesa tokens, no palabras humanas.",
        "inglés": "The model processes tokens, not human words.",
        "código": "def f(x):\n    return x * 2",
        "emoji": "¡Hola! 🚀🔥",
    }
    for name, txt in samples.items():
        print(f"{name:8} -> {count_tokens(txt)} tokens | texto: {txt}")
