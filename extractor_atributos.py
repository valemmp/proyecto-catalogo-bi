import json
import logging as log
import time
import re

from procesador_ia import consultar_ia
from config import MARCAS_CONOCIDAS

def extraer_atributos(nombre_producto):
    time.sleep(0.1)
    marca_detectada = detectar_marca(nombre_producto)
    prompt = f"""
    Sos un especialista en catalogación de productos tecnológicos.

    Analizá ÚNICAMENTE el siguiente nombre de producto:
    
    "{nombre_producto}"
    
    Tu tarea es separar correctamente la MARCA del MODELO.
    
    REGLAS OBLIGATORIAS:
    
    1. La marca y el modelo son atributos diferentes.
    2. Si una marca aparece explícitamente en el nombre, debes extraerla en "marca".
    3. Nunca incluyas la marca dentro del valor de "modelo".
    4. El modelo debe contener únicamente el nombre o código del modelo, sin la marca.
    5. NO inventes información.
    6. Si un atributo no aparece claramente, devuelve null.
    7. Conservá los nombres y códigos de modelo presentes en el producto.
    8. Respondé EXCLUSIVAMENTE con un JSON válido.
    9. No agregues explicaciones ni texto adicional.
    
    EJEMPLOS:
    
    Producto:
    "intercomunicador ejeas v6 pro"
    
    Respuesta:
    {{
        "marca": "Ejeas",
        "categoria": "intercomunicador",
        "modelo": "V6 Pro",
        "color": null,
        "tipo": null,
        "conexion": null
    }}
    
    Producto:
    "microfono inalambrico boya v20 usb c"
    
    Respuesta:
    {{
        "marca": "Boya",
        "categoria": "microfono",
        "modelo": "V20",
        "color": null,
        "tipo": "inalambrico",
        "conexion": "USB-C"
    }}
    
    Producto:
    "scanner automotriz autel mx808s"
    
    Respuesta:
    {{
        "marca": "Autel",
        "categoria": "scanner automotriz",
        "modelo": "MX808S",
        "color": null,
        "tipo": null,
        "conexion": null
    }}
    
    FORMATO OBLIGATORIO:
    
    {{
        "marca": null,
        "categoria": null,
        "modelo": null,
        "color": null,
        "tipo": null,
        "conexion": null
    }}
    
    Producto:
    {nombre_producto}
    """

    respuesta = consultar_ia(prompt)
    dict_vacio = {"marca": marca_detectada, "categoria": None, "modelo": None, "color": None, "tipo": None, "conexion": None}

    if respuesta:
        try:
            datos = extraer_json_de_texto(respuesta)
            if not datos:
                respuesta_limpia = respuesta.replace("```json", "").replace("```", "").strip()
                datos = json.loads(respuesta_limpia)

            if datos:
                if marca_detectada:
                    datos["marca"] = marca_detectada
                return datos
            return dict_vacio


        except Exception as e:
            log.error(f"Error parseando JSON para {nombre_producto}: {e}")
            return dict_vacio
    return dict_vacio

def detectar_marca(nombre_producto):
    nombre = nombre_producto.lower()
    for clave, marca in MARCAS_CONOCIDAS.items():
        if clave in nombre:
            return marca
    return None

def extraer_json_de_texto(texto):
    match = re.search(r'\{.*\}', texto, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except:
            return None
    return None