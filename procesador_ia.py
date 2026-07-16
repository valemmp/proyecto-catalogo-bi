import ollama
import logging as log

from config import MODELO_IA

usar_OpenAI = False


def consultar_ia(prompt):
    try:
        respuesta = ollama.chat(
            model=MODELO_IA,
            messages=[{"role": "user","content": prompt}])

        return respuesta["message"]["content"].strip()

    except Exception as e:
        log.error(f"Error en la comunicación con {MODELO_IA}: {e}")
        return None


def optimizar_productos(nombre):
    if usar_OpenAI:
        return nombre

    prompt = f"""
        Sos un experto en títulos de productos para MercadoLibre Argentina.
        
        Tu tarea es mejorar el título del producto para que sea más claro y fácil de encontrar en búsquedas.
        
        REGLAS ABSOLUTAS:
            1. Respondé únicamente con el título optimizado.
            2. El resultado debe estar completamente en español.
            3. NO traduzcas ninguna palabra.
            4. NO inventes características, usos, compatibilidades o tipos de producto.
            5. NO agregues palabras como "para vehículos", "para smartphones", "para cámaras", "profesional", etc., salvo que aparezcan en el nombre original.
            6. NO cambies el significado de ninguna palabra.
            7. NO reemplaces una palabra técnica por un sinónimo que pueda cambiar su significado.
            8. Conservá exactamente las marcas, modelos, números, letras y códigos.
            9. "Eje X", "Eje Y" y "Eje Z" son nombres técnicos y deben conservarse exactamente.
            10. Solo podés:
               - reordenar palabras;
               - corregir errores ortográficos evidentes;
               - agregar palabras genéricas como "Micrófono", "Grabadora", "Impresora", etc., únicamente cuando la categoría del producto sea evidente por el nombre.
            11. Si no estás seguro de una mejora, devolvé el nombre original.
            12. No agregues información basada en conocimientos externos.
            13. Respondé únicamente con el título final.
            
            Nombre original:
            {nombre}
        """

    respuesta = consultar_ia(prompt)

    if respuesta:
        return respuesta

    return nombre