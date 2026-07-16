# from openai import OpenAI    # <- para activar la api de chatgpt
import ollama
import logging as log
usar_OpenAI = False  # <- cambiar a True en caso de chatgpt


def optimizar_productos(nombre):
    if usar_OpenAI:
        try:
            # OpenAI activada
            return "respuesta"

        except Exception as e:
            log.error(f"Error usando OpenAI: {e}")
            return "No fue posible optimizar el producto"
    else:
        try:
            prompt = f"""
            Sos un experto en SEO de la tecnología. Tu única función es devolver el título optimizado en español.
            Reglas estrictas:
            1. Conservá la marca y modelo real.
            2. NO inventes características técnicas (GB, modelos, etc) si no están en el nombre.
            3. NO respondas con saludos, introducciones ni explicaciones.
            4. Solo devuelve el título, nada más.

            Titulo a optimizar: {nombre}
            """
            respuesta = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
            return respuesta['message']['content'].strip()
        except Exception as e:
            log.error(f"Error optimizando producto {nombre}: {e}")
            return "No fue posible optimizar el producto"