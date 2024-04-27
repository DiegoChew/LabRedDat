import numpy as np
from scipy.stats import chi2

# Definir la función f(x)
def f(x):
    return (63.57) * np.exp(-((x - 2.188) / 1.6) ** 2 / 2)

# Cargar los datos desde el archivo CSV
datos = np.loadtxt('muestra_radiacion.csv', delimiter=',', usecols=[0], skiprows=1)  # Suponiendo que la primera columna contiene los datos

# Calcular las frecuencias esperadas
frecuencias_esperadas = np.array([f(x) for x in datos])

# Calcular las frecuencias observadas
frecuencias_observadas, _ = np.histogram(datos, bins='auto')

# Calcular el estadístico de chi-cuadrado
chi2_statistic = np.sum((frecuencias_observadas - frecuencias_esperadas) ** 2 / frecuencias_esperadas)

# Calcular los grados de libertad
grados_libertad = len(frecuencias_observadas) - 1

# Calcular el valor p
p_valor = 1 - chi2.cdf(chi2_statistic, grados_libertad)

# Imprimir resultados
print("Estadístico de Chi-cuadrado:", chi2_statistic)
print("Grados de libertad:", grados_libertad)
print("Valor p:", p_valor)
