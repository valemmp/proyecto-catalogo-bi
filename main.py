import pandas as pd
import datetime
import logging as log
import os

from extractor_atributos import extraer_atributos
from exportador import guardar_catalogo
from proyecto.config import SEPARADOR_CSV
from validaciones import validar_catalogo, validar_columnas
from utils import preparar_carpeta
from procesador_ia import optimizar_productos
from limpiador import limpiar_texto
from config import (CATALOGO,CARPETA_SALIDA,CARPETA_LOGS)

def pipeline():
    print("INICIO DEL PIPELINE")
    # mostrar todas las columnas en la consola
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 1000)

    # crear carpeta de salida
    preparar_carpeta(CARPETA_SALIDA)
    # crear carpeta de logs
    preparar_carpeta(CARPETA_LOGS)

    log.basicConfig(filename=os.path.join(CARPETA_LOGS, "pipeline.log"),level=log.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

    log.info("Inicio del pipeline")
    # leer el catalogo de productos
    try:
        df = pd.read_csv(CATALOGO, sep=SEPARADOR_CSV)
        log.info(f"Catálogo cargado correctamente: {len(df)} productos")
        validar_columnas(df)

    except Exception as e:
        log.error(f"Error leyendo catálogo: {e}")
        raise

    # limpiar los datos
    df["nombre_producto_limpio"] = df["nombre_producto"].apply(limpiar_texto)
    log.info("Limpieza de productos completada")

    # validar los datos
    df_validos, df_errores = validar_catalogo(df)
    log.info(f"Productos listos para IA: {len(df_validos)}")

    if not df_validos.empty:
        log.info("Procesando productos con IA")

        df_validos["descripcion_ia"] = df_validos["nombre_producto_limpio"].apply(optimizar_productos)
        log.info("Optimización con IA completada")

        log.info("Extrayendo atributos de los productos...")
        atributos_data = df_validos["nombre_producto_limpio"].apply(extraer_atributos).tolist()
        df_atributos = pd.DataFrame(atributos_data)

        df_validos = pd.concat([df_validos.reset_index(drop=True), df_atributos.reset_index(drop=True)], axis=1)
        log.info("Extracción de atributos completada")
    else:
        log.info("No hay productos válidos para procesar con IA")


    # unir
    df_final = pd.concat([df_validos, df_errores])

    df_final["descripcion_ia"] = df_final["descripcion_ia"].fillna("Sin optimización")


    fecha_actual = datetime.datetime.now().strftime("%Y-%m")
    df_final["fecha_proceso"] = fecha_actual

    ruta_completa = guardar_catalogo(df_final, CARPETA_SALIDA)

    print(f"Productos procesados: {len(df_final)}")
    print(f"Archivo generado: {ruta_completa}")

    log.info(f"Archivo listo: {ruta_completa}")
    log.info("Proceso finalizado correctamente")
    print("FIN DEL PIPELINE")

if __name__ == "__main__":
    pipeline()