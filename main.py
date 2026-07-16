import pandas as pd
import datetime
import logging as log

from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from extractor_atributos import extraer_atributos
from exportador import guardar_catalogo
from proyecto.config import SEPARADOR_CSV
from validaciones import validar_catalogo, validar_columnas
from utils import preparar_carpeta
from procesador_ia import optimizar_productos
from limpiador import limpiar_texto
from logs_config import configurar_log
from config import (CATALOGO,CARPETA_SALIDA,CARPETA_LOGS, HILOS, PROCESAR_PARALELO, OPTIMIZAR_TITULOS)

def pipeline():
    print("INICIO DEL PIPELINE")
    # mostrar todas las columnas en la consola
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 1000)

    # crear carpeta de salida
    preparar_carpeta(CARPETA_SALIDA)
    # crear carpeta de logs
    preparar_carpeta(CARPETA_LOGS)

    # log.basicConfig(filename=os.path.join(CARPETA_LOGS, "pipeline.log"),level=log.INFO,format="%(asctime)s - %(levelname)s - %(message)s")
    configurar_log()

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
        if PROCESAR_PARALELO:
            log.info(f"Modo de procesamiento: Paralelo")
            with ThreadPoolExecutor(max_workers=HILOS) as executor:

                productos = df_validos["nombre_producto_limpio"].tolist()

                atributos_data = list(
                    tqdm(executor.map(extraer_atributos, productos),total=len(productos),desc="Extrayendo atributos",unit="producto"))

                if OPTIMIZAR_TITULOS:
                    titulos_optimizados = list(
                        tqdm(executor.map(optimizar_productos, productos),total=len(productos),desc="Optimizando nombres",unit="producto"))
        else:
            log.info(f"Modo de procesamiento: Serie")
            atributos_data = [extraer_atributos(prod) for prod in df_validos["nombre_producto_limpio"]]

            if OPTIMIZAR_TITULOS:
                titulos_optimizados = [optimizar_productos(prod) for prod in df_validos["nombre_producto_limpio"]]

        df_atributos = pd.DataFrame(atributos_data).reset_index(drop=True)
        df_validos = df_validos.reset_index(drop=True)

        df_atributos = df_atributos.rename(columns={"marca": "marca_extraida","categoria": "categoria_extraida"})

        df_validos = pd.concat([df_validos, df_atributos],axis=1)

        if OPTIMIZAR_TITULOS:
            df_validos["nombre_optimizado"] = titulos_optimizados

        log.info("Extracción de atributos completada")
    else:
        log.info("No hay productos válidos para procesar con IA")
        df_validos["nombre_optimizado"] = "Sin optimización"


    df_validos = df_validos.reset_index(drop=True)
    df_errores = df_errores.reset_index(drop=True)

    df_final = pd.concat([df_validos, df_errores],ignore_index=True)

    if "nombre_optimizado" not in df_final.columns:
        df_final["nombre_optimizado"] = "Sin optimización"
    else:
        df_final["nombre_optimizado"] = df_final["nombre_optimizado"].fillna("Sin optimización")

    fecha_completa = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    df_final["fecha_proceso"] = fecha_completa

    ruta_completa = guardar_catalogo(df_final, CARPETA_SALIDA)

    print(f"Productos procesados: {len(df_final)}")
    print(f"Archivo generado: {ruta_completa}")

    log.info(f"Archivo listo: {ruta_completa}")
    log.info("Proceso finalizado correctamente")
    print("FIN DEL PIPELINE")

if __name__ == "__main__":
    pipeline()