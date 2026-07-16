# Pipeline de Automatización para Catálogo eCommerce

Este proyecto consiste en un **pipeline de datos automatizado** diseñado para procesar, limpiar, validar y optimizar catálogos de productos para eCommerce.

La herramienta permite transformar datos brutos de productos en un catálogo estructurado y listo para ser utilizado en procesos de análisis y Business Intelligence mediante herramientas como Power BI.

El pipeline combina técnicas de **ingeniería de datos, automatización, procesamiento de lenguaje natural e inteligencia artificial** para mejorar la calidad y consistencia de la información de los productos.

---

## Flujo general del proyecto

```text
Datos brutos
    │
    v
Extracción de información
    │
    v
Limpieza y normalización
    │
    v
Extracción de atributos
    │
    v
Validación de datos
    │
    v
Optimización mediante IA
    │
    v
Generación del catálogo final
    │
    v
Power BI / Business Intelligence
```

---

## Características principales

### Limpieza y normalización de datos

Normalización de textos mediante expresiones regulares (Regex), eliminación de caracteres especiales y estandarización de la información de los productos.

### Extracción de atributos

Identificación y extracción de atributos relevantes de los productos, como:

- Marca
- Categoría
- Características específicas
- Información técnica

Estos atributos son utilizados posteriormente para mejorar la estructura y el análisis del catálogo.

### Validación de datos

Implementación de reglas de negocio para controlar la calidad y consistencia de los datos.

Entre las validaciones se incluyen:

- Verificación de precios válidos.
- Control de costos.
- Cálculo y validación de márgenes.
- Validación de columnas requeridas.
- Control de registros incompletos o inconsistentes.

### Optimización con Inteligencia Artificial

Integración con modelos de lenguaje para mejorar la consistencia y calidad de los nombres de los productos.

El sistema puede utilizar:

- Ollama con modelos locales como Llama 3.

La IA permite normalizar y optimizar los nombres de los productos de manera automatizada.

### Trazabilidad y logging

Sistema de registro de eventos para monitorear la ejecución del pipeline y facilitar la detección de errores.

La configuración del sistema de logs se centraliza en `logs_config.py`, permitiendo mantener un sistema uniforme de registros en los diferentes módulos.

### Arquitectura modular

El proyecto utiliza una arquitectura modular en la que cada componente tiene una responsabilidad específica.

Esto facilita:

- El mantenimiento del código.
- La reutilización de funciones.
- La incorporación de nuevas funcionalidades.
- La escalabilidad del pipeline.

---

## Tecnologías utilizadas

- **Lenguaje:** Python 3.x
- **Manipulación de datos:** Pandas
- **Procesamiento de texto:** Expresiones regulares (Regex)
- **Inteligencia Artificial:** Ollama
- **Modelos de lenguaje:** Llama 3
- **Visualización y Business Intelligence:** Microsoft Power BI
- **Logging:** Librería estándar logging
- **Control de versiones:** Git / GitHub

---

## Estructura del proyecto

```text
proyecto/
│
├── main.py
│   └── Orquestador principal del pipeline.
│
├── extractor_atributos.py
│   └── Extracción de atributos relevantes de los productos.
│
├── limpiador.py
│   └── Limpieza y normalización de los datos.
│
├── validaciones.py
│   └── Reglas de negocio y validación de datos.
│
├── procesador_ia.py
│   └── Integración con modelos de lenguaje para optimización de productos.
│
├── exportador.py
│   └── Generación y exportación del catálogo final.
│
├── logs_config.py
│   └── Configuración centralizada del sistema de logging.
│
├── utils.py
│   └── Funciones auxiliares y utilidades generales.
│
├── config.py
│   └── Configuración del modelo de IA y parámetros del proyecto.
│
├── catalogo.csv
│   └── Archivo de entrada con los datos brutos de los productos.
│
├── requirements.txt
│   └── Dependencias necesarias para ejecutar el proyecto.
│
├── dashboards/
│   └── Dashboard desarrollado en Power BI.
│
├── screenshots/
│   └── Capturas de pantalla del dashboard.
│
└── logs/
    └── Historial de ejecución del pipeline.
```

---

## Flujo del pipeline

### 1. Ingreso de datos

El proceso comienza con un archivo CSV que contiene la información bruta de los productos.

```text
catalogo.csv
```

### 2. Limpieza y normalización

Los datos son procesados para:

- Normalizar textos.
- Eliminar caracteres innecesarios.
- Corregir formatos.
- Estandarizar la información.

### 3. Extracción de atributos

Se identifican atributos relevantes de cada producto, como la marca y la categoría.

Estos datos permiten estructurar mejor la información y facilitar su posterior análisis.

### 4. Validación de datos

El pipeline verifica que los registros cumplan con las reglas de negocio definidas.

Por ejemplo:

- Que los precios sean válidos.
- Que los costos sean coherentes.
- Que existan las columnas necesarias.
- Que los márgenes sean calculables.

### 5. Optimización mediante IA

Los nombres de los productos pueden ser procesados mediante modelos de lenguaje para mejorar su consistencia y legibilidad.

La integración se realiza actualmente mediante Ollama, permitiendo ejecutar modelos de lenguaje localmente.

### 6. Exportación

Una vez finalizado el procesamiento, se genera un catálogo limpio y estructurado en formato CSV.

Este archivo puede ser utilizado posteriormente por herramientas de análisis y Business Intelligence.

### 7. Visualización en Power BI

El catálogo procesado se utiliza como fuente de datos para un dashboard desarrollado en Power BI.

---

## Dashboard de Business Intelligence

El proyecto incluye un dashboard desarrollado en Power BI para analizar el catálogo de productos.

El dashboard permite analizar:

- Cantidad de productos por marca.
- Cantidad de productos por categoría.
- Precios de venta.
- Costos.
- Márgenes de rentabilidad.
- Distribución de productos por categoría.
- Filtros interactivos por marca y categoría.

### Principales métricas

El dashboard incluye indicadores como:

- Suma total de costos.
- Suma total de precios de venta.
- Margen porcentual.
- Cantidad de productos.

El archivo de Power BI se encuentra en:

```text
dashboards/dashboard-catalogo-productos.pbix
```

### Vista del dashboard

![Dashboard del catálogo](screenshots/dashboard-general.png)

---

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/valemmp/proyecto-catalogo-bi.git
```

Ingresar al directorio del proyecto:

```bash
cd proyecto-catalogo-bi
```

Crear un entorno virtual:

```bash
python -m venv venv
```

Activar el entorno virtual en Windows:

```bash
venv\Scripts\activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```
---

## Configuración

La configuración del modelo de Inteligencia Artificial y de los parámetros principales del proyecto se encuentra centralizada en:

```text
config.py
```

No se deben subir claves API ni información sensible al repositorio.

---

## Ejecución

Para ejecutar el pipeline:

```bash
python main.py
```

El proceso realizará las diferentes etapas de procesamiento y generará el catálogo final.

Los eventos de ejecución y posibles errores serán registrados mediante el sistema de logging.

---

## Objetivos del proyecto

- Automatizar la preparación de catálogos para eCommerce.
- Reducir errores manuales en la carga de productos.
- Mejorar la calidad de los datos antes de su consumo por herramientas de Business Intelligence.
- Facilitar la generación de nombres de productos consistentes mediante Inteligencia Artificial.
- Extraer atributos relevantes de los productos.
- Mantener un pipeline modular, escalable y fácil de mantener.
- Integrar procesos de ingeniería de datos con herramientas de análisis y visualización.

---

## Próximas mejoras

- Consulta de precios desde APIs de eCommerce para detectar variaciones.
- Integración directa con bases de datos relacionales como SQL Server o PostgreSQL.
- Reemplazo del almacenamiento mediante CSV por una base de datos.
- Despliegue del pipeline en un contenedor Docker.
- Ejecución programada en servidores.
- Automatización de la actualización del dashboard de Power BI.
- Incorporación de más reglas de validación de calidad de datos.
- Implementación de pruebas automatizadas.
- Incorporación de nuevos modelos de Inteligencia Artificial.

---

## Autor

**Valentín Mansilla**

Estudiante de Ingeniería en Sistemas de Información - UTN FRC.

Intereses:

- Python
- Data Engineering
- Business Intelligence
- Inteligencia Artificial
- Automatización
- Procesamiento y análisis de datos
