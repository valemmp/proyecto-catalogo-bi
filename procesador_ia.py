import ollama
import logging as log

from config import MODELO_IA, PROMPT_OPTIMIZACION,TEMPERATURA_IA
usar_OpenAI = False


def consultar_ia(prompt):
    try:
        respuesta = ollama.chat(
            model=MODELO_IA, options={"temperature": TEMPERATURA_IA},
            messages=[{"role": "user","content": prompt}])

        return respuesta["message"]["content"].strip()

    except Exception as e:
        log.error(f"Error en la comunicación con {MODELO_IA}: {e}")
        return None


def optimizar_productos(nombre):
    if usar_OpenAI:
        return nombre

    prompt = PROMPT_OPTIMIZACION.format(nombre=nombre)

    respuesta = consultar_ia(prompt)

    if respuesta:
        return respuesta

    return nombre