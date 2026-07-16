import pandas as pd
import datetime
import os
from utils import preparar_carpeta
from procesador_ia import optimizar_productos

# para ver las columnas en python
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
# pd.set_option('display.max_rows', None)

# creacion de la carpeta para el csv de salida
carpeta_salida = 'output'
preparar_carpeta(carpeta_salida)

df = pd.read_csv('catalogo.csv')

# limpieza de los datos
df['nombre_producto_limpio'] = df['nombre_producto'].str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
df['nombre_producto_limpio'] = df['nombre_producto_limpio'].str.replace(r'\s+', ' ', regex=True)
df['nombre_producto_limpio'] = df['nombre_producto_limpio'].str.title()

df['es_valido'] = df['nombre_producto_limpio'].fillna('').str.strip().str.len() > 0

df['margen_positivo'] = df['precio_venta'] > df['costo']
df['precio_valido'] = df['precio_venta'] > 0

df['estado'] = 'OK'
df.loc[~df['es_valido'] | ~df['precio_valido'] | ~df['margen_positivo'], 'estado'] = 'Error'

df_validos = df[df['estado'] == 'OK'].copy()
df_errores = df[df['estado'] == 'Error'].copy()

if len(df_validos) > 0:
    print("Procesando los nombres de los productos con IA...")
    df_validos['descripcion_ia'] = df_validos['nombre_producto_limpio'].apply(optimizar_productos)

df_final = pd.concat([df_validos, df_errores])

df_final['descripcion_ia'] = df_final['descripcion_ia'].fillna('Sin optimización')
df_final['fecha_proceso'] = datetime.datetime.now().strftime("%Y-%m")
mes_actual = datetime.datetime.now().strftime("%Y-%m")
nombre_archivo = f"catalogo_{mes_actual}.csv"
ruta_completa = os.path.join(carpeta_salida, nombre_archivo)
df_final.to_csv(ruta_completa, index=False, encoding='utf-8-sig', sep=';')

print(df_final[['id_producto', 'nombre_producto', 'descripcion_ia', 'estado']])
print('Se creó la carpeta "output" y el archivo .csv')
