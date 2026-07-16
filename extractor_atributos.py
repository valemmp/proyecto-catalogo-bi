import json
import logging as log
import time

from procesador_ia import consultar_ia

def extraer_atributos(nombre_producto):
    time.sleep(0.1)
    prompt = f"""
    Sos un especialista en catalogación de productos tecnológicos.
    
    Tu objetivo es extraer datos técnicos estructurados a partir del nombre del producto: "{nombre_producto}".

    Reglas estrictas:
    1. Extraé solo datos presentes en el nombre.
    2. Todo producto tiene una marca. Si el nombre es ambiguo, investigá/deducí la marca real del mercado tecnológico (ej: si dice "MX900", inferí "Autel").
    3. Si un atributo no existe o no estás seguro, devolvé null.
    4. NO inventes información técnica (especificaciones que no estén).
    5. Respondé EXCLUSIVAMENTE un JSON válido, sin texto adicional. Nada de saludos ni nada mas.
    Por ejemplo: Hay marcas como "Autel", "Boya", "HardKraft", "Ejeas", "Nimbot", "AltaNet", "Fnirsi", "TKStar", etc. 
    Formato JSON:

    {{
        "marca": null,
        "categoria": null,
        "modelo": null,
        "color": null,
        "tipo": null,
        "conexion": null
    }}

    Producto:{nombre_producto}
    """

    respuesta = consultar_ia(prompt)

    if respuesta:
        try:
            respuesta = respuesta.replace("```json", "").replace("```", "")
            return json.loads(respuesta)
        except Exception as e:
            log.error(f"Error parseando JSON: {e}")

    return {"marca": None, "categoria": None, "modelo": None, "color": None, "tipo": None, "conexion": None}