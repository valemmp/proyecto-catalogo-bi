import os
import datetime
import logging as log
from config import ENCODING, SEPARADOR_CSV

def guardar_catalogo(df, carpeta_salida):

    try:
        fecha_actual = datetime.datetime.now().strftime("%Y-%m")

        nombre_archivo = f"catalogo_{fecha_actual}.csv"

        ruta_completa = os.path.join(carpeta_salida, nombre_archivo)

        df.to_csv(ruta_completa,index=False,encoding=ENCODING,sep=SEPARADOR_CSV)

        log.info(f"Archivo generado correctamente: {ruta_completa}")

        return ruta_completa

    except Exception as e:
        log.error(f"Error exportando catálogo: {e}")
        raise