import logging as log
import pandas as pd

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


def evaluar_calidad(producto):
    puntos = 0
    errores = []

    if producto.get("estado") == "Error":
        puntos -= 50
        errores.append("Producto rechazado")

    reglas = {
        "nombre_producto": 25,
        "marca": 25,
        "categoria": 20,
        "modelo": 15,
        "precio_venta": 15
    }

    for campo, peso in reglas.items():
        valor = producto.get(campo)

        if pd.notna(valor) and str(valor).strip() != "":
            puntos += peso
        else:
            errores.append(f"Falta {campo}")

    return puntos, ", ".join(errores)


def agregar_calidad_datos(df):
    resultados = df.apply(evaluar_calidad, axis=1)

    df["calidad_datos"] = resultados.apply(lambda x: x[0])
    df["errores_datos"] = resultados.apply(lambda x: x[1])

    return df

def clasificar_calidad(valor):
    if valor >= 90:
        return "Excelente"
    elif valor >= 70:
        return "Bueno"
    elif valor >= 40:
        return "Revisar"
    else:
        return "Crítico"