import logging as log
import os
import datetime
from config import CARPETA_LOGS


def configurar_log():
    if not os.path.exists(CARPETA_LOGS):
        os.makedirs(CARPETA_LOGS)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_log = f"pipeline_{timestamp}.log"
    ruta_log = os.path.join(CARPETA_LOGS, nombre_log)

    for handler in log.root.handlers[:]:
        log.root.removeHandler(handler)

    log.basicConfig(
        filename=ruta_log,
        level=log.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return ruta_log