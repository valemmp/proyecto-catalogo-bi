import pandas as pd
import os
import logging as log


def generar_reporte_calidad(df, carpeta_salida):

    total_productos = len(df)

    productos_error = len(df[df["estado"] == "Error"])

    productos_ok = len(df[df["estado"] == "OK"])

    calidad_promedio = round(df["calidad_datos"].mean(),2)


    reporte_general = pd.DataFrame([
        {
            "productos_total": total_productos,
            "productos_ok": productos_ok,
            "productos_error": productos_error,
            "calidad_promedio": calidad_promedio
        }
    ])


    ruta = os.path.join(
        carpeta_salida,
        "reporte_calidad.csv"
    )

    reporte_general.to_csv(
        ruta,
        index=False,
        encoding="utf-8-sig"
    )


    log.info("Reporte de calidad generado")

    return ruta

def generar_reporte_errores(df, carpeta_salida):

    errores = df[
        df["errores_datos"].notna()
        &
        (df["errores_datos"] != "")
    ]

    columnas = [
        "id_producto",
        "nombre_producto",
        "errores_datos"
    ]


    errores = errores[columnas]


    ruta = os.path.join(carpeta_salida,"errores_catalogo.csv")


    errores.to_csv(ruta,index=False,encoding="utf-8-sig")


    return ruta