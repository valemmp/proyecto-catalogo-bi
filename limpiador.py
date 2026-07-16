import re
import unicodedata
import pandas as pd

def quitar_acentos(texto):
    texto = unicodedata.normalize("NFKD", texto)

    texto_sin_acentos = ""

    for c in texto:
        if not unicodedata.combining(c):
            texto_sin_acentos += c

    return texto_sin_acentos

def limpiar_texto(texto):
    if pd.isna(texto):
        return ""

    texto = texto.lower()
    texto = quitar_acentos(texto)

    texto = re.sub(r"[^\w\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto)

    return texto.strip()