import json
import logging as log
import time
import re

from procesador_ia import consultar_ia
from config import MARCAS_CONOCIDAS, ATRIBUTOS_ESPERADOS

def normalizar_atributos(datos, marca_detectada):
    atributos = ATRIBUTOS_ESPERADOS.copy()

    for clave in atributos:
        if clave in datos:
            atributos[clave] = datos[clave]

    if marca_detectada:
        atributos["marca"] = marca_detectada
    else:
        atributos["marca"] = None

    return atributos

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
        2. Si una marca aparece explícitamente en el nombre del producto, debes extraerla en "marca".
        3. Si una marca NO aparece claramente en el nombre del producto, devuelve null.
           NO inventes marcas.
        4. Nunca interpretes palabras genéricas como "eje", "gimbal", "impresora",
           "intercomunicador", "grabadora" o "estabilizador" como marcas.
        5. Nunca incluyas la marca dentro del valor de "modelo".
        6. El modelo debe contener únicamente el nombre o código del modelo,
           sin la marca.
        7. COPIA EXACTAMENTE los nombres, letras, números y códigos técnicos
           presentes en el producto original.
        8. NO corrijas errores ortográficos del nombre del producto.
        9. NO cambies letras, números ni códigos.
           Por ejemplo:
           "Ender 3" nunca puede convertirse en "Endeer 3".
           "Boya" nunca puede convertirse en "Boia".
           "V2" nunca puede convertirse en "V3".
        10. NO inventes información.
        11. Si un atributo no aparece claramente en el nombre original, devuelve null.
        12. Solo puedes separar la información existente en el nombre original.
            No puedes agregar información externa.
        13. Respondé EXCLUSIVAMENTE con un JSON válido.
        14. No agregues explicaciones ni texto adicional.
        
        Para cada atributo:

        - marca: solo una marca explícitamente presente en el nombre.
        - categoria: categoría claramente identificable a partir del nombre.
        - modelo: nombre o código del modelo presente literalmente en el nombre.
        - color: solo si aparece explícitamente.
        - tipo: solo si aparece explícitamente.
        - conexion: solo si aparece explícitamente.
        
        Si no podés identificar un atributo con seguridad a partir del nombre,
        devuelve null.
    
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
    dict_vacio = normalizar_atributos({}, marca_detectada)

    if respuesta:
        try:
            datos = extraer_json_de_texto(respuesta)
            if not datos:
                respuesta_limpia = respuesta.replace("```json", "").replace("```", "").strip()
                datos = json.loads(respuesta_limpia)

            if datos:
                return normalizar_atributos(datos, marca_detectada)
            return dict_vacio


        except Exception as e:
            log.error(f"Error parseando JSON para {nombre_producto}: {e}")
            return dict_vacio
    return dict_vacio

def detectar_marca(nombre_producto):

    nombre = nombre_producto.lower()
    for clave, marca in MARCAS_CONOCIDAS.items():
        patron = rf"\b{re.escape(clave)}\b"
        if re.search(patron, nombre):
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