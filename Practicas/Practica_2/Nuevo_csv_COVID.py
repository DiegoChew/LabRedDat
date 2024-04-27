import pandas as pd

# Cargar el archivo CSV original
df_original = pd.read_csv('/home/diego/Documentos/LabRedDat/Practicas/Practica_2/confirmados_fecha.csv')

# Seleccionar las dos columnas que deseas conservar
columnas_deseadas = ['fecha', 'Casos por fecha de emisión de resultados']  # Cambia estos nombres por los de tus columnas deseadas

df_nuevo = df_original[columnas_deseadas].copy()

df_nuevo['fecha']=pd.to_datetime(df_nuevo['fecha'])

rango_fechas_completo = pd.date_range(start=df_nuevo['fecha'].min(), end=df_nuevo['fecha'].max())

df_nuevo_filtrado=df_nuevo.set_index('fecha').reindex(rango_fechas_completo, fill_value=0).reset_index()

df_nuevo_filtrado = df_nuevo.rename(columns={'index': 'fecha'})

<<<<<<< HEAD
<<<<<<< HEAD
df_nuevo_filtrado.insert(0, 'Nueva Columna', range(1, len(df_nuevo_filtrado) + 1))

df_nuevo_filtrado.to_csv('csv_filtrado.csv', index=False)
=======
df_nuevo_filtrado.to_csv('csv_filtrado_2.csv', index=False)
>>>>>>> f187724 (Nuevo csv)
=======
df_nuevo_filtrado.insert(0, 'Nueva Columna', range(1, len(df_nuevo_filtrado) + 1))

df_nuevo_filtrado.to_csv('csv_filtrado.csv', index=False)
>>>>>>> 70ca94c (Listones)
