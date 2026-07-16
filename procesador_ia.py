# from openai import OpenAI    # <- para activar la api de chatgpt
import ollama
import logging as log
import json
from config import MODELO_IA

usar_OpenAI = False  # <- cambiar a True en caso de chatgpt

def consultar_ia(prompt):
    try:
        respuesta = ollama.chat(model=MODELO_IA, messages=[{'role': 'user', 'content': prompt}])
        return respuesta['message']['content'].strip()
    except Exception as e:
        log.error(f"Error en la comunicación con {MODELO_IA}: {e}")
        return None


def optimizar_productos(nombre):
    if usar_OpenAI:
        # futura conexión con openAI
        return "respuesta"

    prompt = f"""
    Sos un experto en SEO de la tecnología. Tu única función es devolver el título optimizado en español.
    Reglas estrictas:
    1. Conservá la marca y modelo real.
    2. NO inventes características técnicas.
    3. NO respondas explicaciones.
    4. Solo devuelve el título. Nada más.

    Titulo a optimizar: {nombre}
    """
    respuesta = consultar_ia(prompt)
    if respuesta:
        return respuesta
    else:
        return "No fue posible optimizar el producto"