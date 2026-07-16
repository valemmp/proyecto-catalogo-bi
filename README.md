# Pipeline de Automatización para Catálogo eCommerce

Este proyecto consiste en un „pipeline de datos automatizado" diseñado para procesar, validar y optimizar catálogos de productos. 
Es una herramienta diseñado para integrarse en flujos de Business Intelligence, permitiendo preparar los datos brutos para su posterior visualización en herramientas como Power BI.

## Características principales
- Limpieza de datos: Normalización de texto, eliminación de acentos y caracteres especiales mediante `Regex`.
- Validación de negocio: Control de calidad de datos (verificación de márgenes, precios válidos y estructura de columnas).
- Optimización con IA: Integración con modelos de lenguaje (Ollama/OpenAI) para normalizar y mejorar la consistencia de los nombres de los productos antes de su exportación.
- Trazabilidad: Sistema completo de `logging` para monitoreo de procesos en cada etapa.
- Arquitectura Modular: Separación de responsabilidades mediante módulos independientes.

## Tecnologías utilizadas
- **Lenguaje:** Python 3.x
- **Manipulación de datos:** Pandas
- **IA/LLMs:** Ollama (Llama3) / OpenAI API
- **Logs:** Librería estándar `logging`
- **Control de versiones:** Git

## Estructura del Proyecto
```text
proyecto/
├── main.py              # Orquestador del pipeline
├── limpiador.py         # Funciones de normalización de texto
├── validaciones.py      # Reglas de negocio y validación de datos
├── procesador_ia.py     # Integración con modelos de lenguaje
├── exportador.py        # Gestión de salida y formato CSV
├── utils.py             # Funciones auxiliares
├── catalogo.csv         # Archivo de entrada (datos brutos)
├── requirements.txt     # Dependencias del proyecto
└── logs/                # Historial de ejecución
└── config.py            # Setear el modelo de la API y configuraciones.

## Flujo del Pipeline

CSV de entrada
        │
        v
Limpieza y normalización
        │
        v
Validaciones de negocio
        │
        v
Optimización con IA
        │
        v
Generación del CSV final
        │
        v
Power BI / Análisis


## Objetivos

- Automatizar la preparación de catálogos para eCommerce.
- Reducir errores manuales en la carga de productos.
- Mejorar la calidad de los datos antes de su consumo por herramientas BI.
- Facilitar la generación de títulos consistentes mediante IA.
- Mantener un pipeline modular, escalable y fácil de mantener.

## Próximas mejoras

- Consulta de precios desde APIs de eCommerce para detectar variaciones.
- Integración directa con bases de datos relacionales (SQL Server, PostgreSQL) para reemplazar el CSV.
- Despliegue del pipeline en un contenedor Docker para ejecución programada en servidores.