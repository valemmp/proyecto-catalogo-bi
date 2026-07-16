import os

def preparar_carpeta(carpeta_salida):
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)
        print(f"Carpeta '{carpeta_salida}' creada.")