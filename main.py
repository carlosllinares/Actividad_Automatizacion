import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import openpyxl
# Importar archivo excel
# Ruta del archivo Excel
archivo = r'C:\Users\carlo\iCloudDrive\BI\9- Tendencias de automatización\Actividades\Actividad 1\Actividad1_datos_mantenimiento_predictivo.xlsx'

# Campos
columnas_deseadas = [
    'Temperatura_C',
    'Vibracion_mms',
    'Presion_bar',
    'Humedad_%',
    'Horas_funcionamiento',
    'Fallo_detectado'
]

# Leer todas las hojas del archivo Excel
excel = pd.ExcelFile(archivo)
df_list = []

for nombre_hoja in excel.sheet_names:
    # Leer la hoja
    df_hoja = pd.read_excel(archivo, sheet_name=nombre_hoja)
    # Filtrar las columnas deseadas
    df_hoja = df_hoja[columnas_deseadas]
    # Añadir el nombre de la hoja como columna ID_Motor
    df_hoja['ID_Motor'] = nombre_hoja
    # Añadir a la lista
    df_list.append(df_hoja)

# Unificar todo en un solo DataFrame
df_final = pd.concat(df_list, ignore_index=True)

# Reordenar columnas para que 'ID_Motor' sea la primera
cols = ['ID_Motor'] + columnas_deseadas
df_final = df_final[cols]

# Mostrar el DataFrame resultante
print(df_final)