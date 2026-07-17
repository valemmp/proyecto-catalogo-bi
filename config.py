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
TEMPERATURA_IA = 0

MARCAS_CONOCIDAS = {

    "apple": "Apple",
    "iphone": "Apple",
    "motorola": "Motorola",
    "samsung": "Samsung",
    "xiaomi": "Xiaomi",
    "redmi": "Xiaomi",
    "poco": "POCO",
    "oneplus": "OnePlus",
    "oppo": "OPPO",
    "vivo": "Vivo",
    "realme": "Realme",
    "honor": "Honor",
    "nokia": "Nokia",
    "zte": "ZTE",

    "boya": "Boya",
    "rode": "Rode",
    "zoom": "Zoom",
    "fifine": "Fifine",
    "maono": "Maono",
    "hyperx": "HyperX",
    "shure": "Shure",
    "audio technica": "Audio-Technica",
    "jbl": "JBL",
    "bose": "Bose",
    "marshall": "Marshall",
    "sennheiser": "Sennheiser",
    "akg": "AKG",

    "zhiyun": "Zhiyun",
    "dji": "DJI",
    "gopro": "GoPro",
    "insta360": "Insta360",
    "canon": "Canon",
    "nikon": "Nikon",
    "sony": "Sony",
    "fujifilm": "Fujifilm",
    "panasonic": "Panasonic",

    "logitech": "Logitech",
    "redragon": "Redragon",
    "razer": "Razer",
    "corsair": "Corsair",
    "steelseries": "SteelSeries",
    "cooler master": "Cooler Master",
    "thermaltake": "Thermaltake",
    "nzxt": "NZXT",
    "fantech": "Fantech",
    "cougar": "Cougar",
    "trust": "Trust",
    "glorious": "Glorious",

    "hp": "HP",
    "hewlett packard": "HP",
    "lenovo": "Lenovo",
    "dell": "Dell",
    "asus": "ASUS",
    "acer": "Acer",
    "msi": "MSI",
    "gigabyte": "Gigabyte",
    "vaio": "VAIO",
    "bangho": "Banghó",
    "exxo": "Exo",
    "lg": "LG",

    "intel": "Intel",
    "amd": "AMD",
    "nvidia": "NVIDIA",
    "geforce": "NVIDIA",
    "radeon": "AMD",
    "asrock": "ASRock",
    "biostar": "Biostar",
    "evga": "EVGA",
    "zotac": "Zotac",

    "kingston": "Kingston",
    "crucial": "Crucial",
    "sandisk": "SanDisk",
    "western digital": "Western Digital",
    "wd": "Western Digital",
    "seagate": "Seagate",
    "toshiba": "Toshiba",
    "adata": "ADATA",
    "lexar": "Lexar",
    "teamgroup": "TeamGroup",
    "patriot": "Patriot",

    "brother": "Brother",
    "epson": "Epson",
    "canon": "Canon",
    "lexmark": "Lexmark",
    "xerox": "Xerox",
    "dymo": "Dymo",
    "niimbot": "Niimbot",

    "tp link": "TP-Link",
    "tplink": "TP-Link",
    "mercusys": "Mercusys",
    "tenda": "Tenda",
    "mikrotik": "MikroTik",
    "ubiquiti": "Ubiquiti",
    "cisco": "Cisco",
    "dlink": "D-Link",

    "autel": "Autel",
    "anker": "Anker",
    "baseus": "Baseus",
    "ugreen": "UGREEN",
    "belkin": "Belkin",

    "creality": "Creality",
    "ender": "Ender",
    "anycubic": "Anycubic",
    "elegoo": "Elegoo",
    "artillery": "Artillery",

    "fjeas": "Fjeas",
    "ejeas": "Ejeas",
    "tkstar": "TKStar",
    "fnirsi": "FNIRSI",
    "alta net": "AltaNet",
    "altanet": "AltaNet",
    "hardkraft": "HardKraft",

    "level up": "Level Up",
    "sentey": "Sentey",
    "noga": "Noga",
    "gadnic": "Gadnic",
    "philco": "Philco",
    "genius": "Genius",
    "kolke": "Kolke"
}

CATEGORIAS_CONOCIDAS = {

    "lavalier": "microfono",
    "shotgun": "microfono",
    "microfono": "microfono",

    "gimbal": "estabilizador",
    "estabilizador": "estabilizador",

    "grabadora": "grabadora",

    "mouse": "mouse",
    "teclado": "teclado",

    "scanner": "scanner automotriz",

    "drone": "drone",

    "impresora": "impresora",
    "etiquetas": "impresora etiquetas",

    "camara": "camara",
    "webcam": "camara",

    "eje": "repuesto impresora 3d"
}
ATRIBUTOS_ESPERADOS = {
    "marca": None,
    "categoria": None,
    "modelo": None,
    "color": None,
    "tipo": None,
    "conexion": None
}

COLUMNAS_SALIDA = [
    "id_producto",
    "nombre_producto",
    "precio_venta",
    "costo",
    "estado",
    "marca",
    "categoria",
    "modelo",
    "color",
    "tipo",
    "conexion",
    "nombre_producto_limpio",
    "nombre_optimizado",
    "fecha_proceso",
    "calidad_datos",
    "errores_datos",
    "nivel_calidad"
]

PROMPT_OPTIMIZACION = """
        Sos un especialista en normalización de catálogos eCommerce.
        
        Tu tarea es limpiar y ordenar el título del producto manteniendo exactamente la información original.
        
        NO estás creando un título comercial.
        NO estás haciendo una descripción.
        NO estás agregando información para mejorar ventas.
        
        REGLAS OBLIGATORIAS:
        
        1. Respondé únicamente con el título final.
        
        2. Conservá exactamente:
        - marcas
        - modelos
        - números
        - códigos
        - versiones
        - nombres técnicos
        
        3. NO agregues:
        - usos del producto
        - compatibilidades
        - público objetivo
        - características no mencionadas
        - materiales
        - colores
        - tecnologías
        
        4. NO agregues palabras como:
        - profesional
        - premium
        - para vehículos
        - para celulares
        - para cámaras
        - inalámbrico
        - portátil
        
        salvo que aparezcan en el nombre original.
        
        5. Solo podés:
        - corregir errores ortográficos evidentes;
        - ordenar palabras;
        - agregar una categoría genérica SOLO si está implícita en el nombre.
        
        Ejemplos:
        
        Entrada:
        Boya Lavalier
        
        Salida:
        Boya Lavalier
        
        Entrada:
        Grabadora zoom h1
        
        Salida:
        Grabadora Zoom H1
        
        Entrada:
        eje y ender 3
        
        Salida:
        Ender 3 Eje Y
        
        Si el nombre original ya está correcto, devolvelo sin cambios.
        
        Nombre original:
        {nombre}
"""

PROMPT_EXTRACCION_ATRIBUTOS = """
        Sos un especialista en catalogación de productos tecnológicos.
        
        Analizá ÚNICAMENTE el siguiente nombre de producto:
        
        "{nombre_producto}"
        
        Tu tarea es separar correctamente los atributos existentes.
        
        REGLAS OBLIGATORIAS:
        
        1. La marca y el modelo son atributos diferentes.
        
        2. Si una marca aparece explícitamente en el nombre del producto,
           extraela en "marca".
        
        3. Si una marca NO aparece claramente en el nombre del producto,
           devuelve null.
        
        4. Nunca interpretes palabras genéricas como:
        - eje
        - gimbal
        - impresora
        - intercomunicador
        - grabadora
        - estabilizador
        
        como marcas.
        
        5. El modelo debe contener únicamente el nombre o código presente,
           sin incluir la marca.
        
        6. COPIA EXACTAMENTE:
        - letras
        - números
        - códigos
        - versiones
        
        7. NO corrijas errores ortográficos.
        
        8. NO inventes información externa.
        
        9. Si un atributo no aparece claramente,
           devuelve null.
        10. La categoría debe ser general, no un modelo ni una característica.

        Ejemplos:
        Correcto:
        "Boya Lavalier"
        categoria: "microfono"
        
        Incorrecto:
        categoria: "lavalier"
        
        Correcto:
        "Gimbal Zhiyun V2"
        categoria: "gimbal"
        
        Incorrecto:
        categoria: "V2"
        
        Correcto:
        "Grabadora Zoom H1"
        categoria: "grabadora"
        
        Incorrecto:
        categoria: "H1"
        
        Respondé EXCLUSIVAMENTE con JSON válido:
        
        {{
            "marca": null,
            "categoria": null,
            "modelo": null,
            "color": null,
            "tipo": null,
            "conexion": null
        }}
        
        Producto:
        {nombre_producto}
        """
