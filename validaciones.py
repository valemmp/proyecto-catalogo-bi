import logging as log

def validar_columnas(df):

    columnas_necesarias = ["id_producto","nombre_producto","precio_venta","costo"]

    columnas_faltantes = []

    for columna in columnas_necesarias:
        if columna not in df.columns:
            columnas_faltantes.append(columna)

    if columnas_faltantes:
        mensaje = f"Faltan columnas obligatorias: {columnas_faltantes}"
        log.error(mensaje)
        raise Exception(mensaje)

    log.info("Validación de columnas completada correctamente")

def validar_catalogo(df):
    df["es_valido"] = (df["nombre_producto_limpio"].str.len() > 0)

    df["margen_positivo"] = (df["precio_venta"] > df["costo"])

    df["precio_valido"] = (df["precio_venta"] > 0)

    df["estado"] = "OK"

    df.loc[~df["es_valido"]| ~df["precio_valido"]| ~df["margen_positivo"],"estado"] = "Error"

    validos = df[df["estado"] == "OK"].copy()
    errores = df[df["estado"] == "Error"].copy()

    log.info(
        f"Validación completada. "
        f"Válidos: {len(validos)} | "
        f"Errores: {len(errores)}"
    )

    return validos, errores