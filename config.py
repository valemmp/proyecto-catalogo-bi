import os
from dotenv import load_dotenv

load_dotenv()

CATALOGO = os.getenv("CATALOGO", "catalogo.csv")
CARPETA_SALIDA = os.getenv("CARPETA_SALIDA", "output")
CARPETA_LOGS = os.getenv("CARPETA_LOGS", "logs")
MODELO_IA = os.getenv("MODELO_IA", "llama3")
ENCODING = os.getenv("ENCODING", "utf-8-sig")
SEPARADOR_CSV = os.getenv("SEPARADOR_CSV", ",")
HILOS = int(os.getenv("HILOS", 5))
PROCESAR_PARALELO = os.getenv("PROCESAR_PARALELO", "True") == "True"
OPTIMIZAR_TITULOS = os.getenv("OPTIMIZAR_TITULOS", "True") == "True"

MARCAS_CONOCIDAS = {
    "ejeas": "Ejeas",
    "fjeas": "Ejeas",
    "boya": "Boya",
    "autel": "Autel",
    "niimbot": "Niimbot",
    "hardkraft": "HardKraft",
    "fnirsi": "Fnirsi",
    "tkstar": "TKStar",
    "altanet": "AltaNet"
}

ATRIBUTOS_ESPERADOS = {
    "marca": None,
    "categoria": None,
    "modelo": None,
    "color": None,
    "tipo": None,
    "conexion": None
}