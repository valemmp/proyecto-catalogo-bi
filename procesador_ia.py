# from openai import OpenAI    # <- para activar la api de chatgpt
import ollama
usar_OpenAI = False

def optimizar_productos(nombre):
    if usar_OpenAI:
        # configuración de openAI
        return "Respuesta desde OpenAI"
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
            return f"Error: {e}"