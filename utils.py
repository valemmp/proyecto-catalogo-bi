import os
import logging as log


def preparar_carpeta(carpeta):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
        log.info(f"Carpeta creada: {carpeta}")