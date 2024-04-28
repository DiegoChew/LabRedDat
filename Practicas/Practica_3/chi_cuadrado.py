# Para usar el código, modifique el archivo .csv a examinar, la columna a usar
# Los parámetros de la función a realizar el chi.
# La función evidentemente.
# Y luego el número de términos que desea eliminar desde la derecha hacia la izquierda para 
# el chi reduciodo.
# Se toma la división al cuadrado del valor teórico en el cálculo del chi.
import numpy as np
import math

# Datos de columna a analizar y .csv
datos = np.genfromtxt('resultado_aire.csv', delimiter=',', skip_header=1)

columna = datos[:, 0]
columna_2=datos[:,1]

# Convertir la columna en un array de NumPy
array_air = np.array(columna)
x=array_air
y=np.array(columna_2)

# Parametros para funcion
A               = 63.5732          
u               = 2.18871          
r               = 1.59884      
                   

# Defina la funcion 
def f(x):
    return  A*np.exp(-((x-u)/r)**2/2)

# Tabla de la función
resultado_bino_air = np.vectorize(f)(x)

# Con esto he calculado cada cálculo de los chi de las entradas
chi_cuadrado_bino_air_entradas= ((resultado_bino_air-y)**2)/(resultado_bino_air)
 #  sumando cada entrada, debería de obtener el chi
chi_cuadrado_bino_air= np.sum(chi_cuadrado_bino_air_entradas)
# Pondre el interval deseado
intervalo_bino_air=len(chi_cuadrado_bino_air_entradas)-3
chi_reducido_bino_air=np.sum(chi_cuadrado_bino_air_entradas[: intervalo_bino_air])


# print('longitud de lista de datos', len(columna))
# print('Longitud de lista de datos modificada', intervalo_bino_air)
print('tabla de f(x), relevante para entender el intervalo a quitar',resultado_bino_air)
print('',y)
print('',resultado_bino_air-y)
print('Entradas del chi cuadrado resultante de cada sub indice',chi_cuadrado_bino_air_entradas)
print('Valor esperado de chi considerando todo el intervalo.',chi_cuadrado_bino_air)
print('Valor esperado de chi reduciendo el intervalo de análisis', chi_reducido_bino_air)
