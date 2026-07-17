import json
import logging as log
import time
import re

from procesador_ia import consultar_ia
from config import ATRIBUTOS_ESPERADOS, PROMPT_EXTRACCION_ATRIBUTOS, MARCAS_CONOCIDAS, CATEGORIAS_CONOCIDAS


def detectar_marca(nombre_producto):
    nombre = nombre_producto.lower()

    for clave, marca in sorted(MARCAS_CONOCIDAS.items(), key=lambda x: len(x[0]), reverse=True):
        if re.search(rf"\b{re.escape(clave)}\b", nombre):
            return marca

    return None


def detectar_categoria(nombre_producto):
    nombre = nombre_producto.lower()

    for clave, categoria in sorted(CATEGORIAS_CONOCIDAS.items(), key=lambda x: len(x[0]), reverse=True):
        if re.search(rf"\b{re.escape(clave)}\b", nombre):
            return categoria

    return None


def normalizar_atributos(datos):
    atributos = ATRIBUTOS_ESPERADOS.copy()

    for clave in atributos:
        if clave in datos:
            atributos[clave] = datos[clave]

    return atributos


def extraer_atributos(nombre_producto):
    time.sleep(0.1)
    marca_detectada = detectar_marca(nombre_producto)
    categoria_detectada = detectar_categoria(nombre_producto)
    prompt = PROMPT_EXTRACCION_ATRIBUTOS.format(nombre_producto=nombre_producto)

    respuesta = consultar_ia(prompt)
    dict_vacio = normalizar_atributos({})

    if respuesta:
        try:
            datos = extraer_json_de_texto(respuesta)
            if not datos:
                respuesta_limpia = respuesta.replace("```json", "").replace("```", "").strip()
                datos = json.loads(respuesta_limpia)

            if datos:
                datos = normalizar_atributos(datos)

                if marca_detectada:
                    datos["marca"] = marca_detectada
                if categoria_detectada:
                    datos["categoria"] = categoria_detectada

                return datos
            return dict_vacio



        except Exception as e:
            log.error(f"Error parseando JSON para {nombre_producto}: {e}")
            if marca_detectada:
                dict_vacio["marca"] = marca_detectada

            return dict_vacio
    return dict_vacio


def extraer_json_de_texto(texto):
    match = re.search(r'\{.*\}', texto, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except Exception:
            return None
    return None
