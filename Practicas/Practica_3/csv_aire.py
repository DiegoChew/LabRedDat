import pandas as pd


# Lee el archivo CSV
df = pd.read_csv('/home/saul/Desktop/LabRedDat/Practicas/Practica_3/muestra_radiacion.csv', header=None)  # Indica a pandas que no hay una fila de encabezado

# Suponiendo que la columna de interés es la primera columna, puedes seleccionarla por su posición (0)
frecuencia_valores = df.iloc[:, 0].value_counts().reset_index()

# Renombra las columnas
frecuencia_valores.columns = ['Datos', 'Frecuencia']

# Guarda el resultado en un nuevo archivo CSV
frecuencia_valores.to_csv('resultado.csv', index=False)

