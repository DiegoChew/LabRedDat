#aprendiendomachin.py

import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt
import re 
from urlextract import URLExtract

def get_y_prediction(W, phi):
    score = np.dot(W, phi)
    if score > 0:
        y_predict = 1
    elif score == 0:
        y_predict = np.nan
    elif score < 0:
        y_predict = -1

    return y_predict

def loss_sq(W, phi, y):

    score = np.dot(W, phi)
    pepi2 = score - y

    return pepi2**2

def grad_loss_sq(W, phi, y):
    # Se realiza el calculo algebraico del gradiente para llegar a esta funcion:
    score = np.dot(W, phi)
    pepi2 = score - y

    return 2*pepi2*phi

df = pd.read_csv('t_ds.csv')

extractor = URLExtract()
def contar_enlaces(texto):
    # Extrae todas las URL del texto y devuelve el número de coincidencias
    return len(extractor.find_urls(texto))

def contar_palabras(texto):
    # Patrón de expresión regular para buscar las palabras clave
    patron_palabras = r'\b(?:win|free|won|txt|call|now|claim|winner)\b'
    # Buscar coincidencias de palabras clave en el texto y devolver el número de coincidencias
    return len(re.findall(patron_palabras, texto, flags=re.IGNORECASE))

def contar_caracteres_numericos(texto):
    # Usar una expresión regular para encontrar todos los dígitos en la cadena
    digitos = re.findall(r'\d', texto)
    # Contar el número de dígitos encontrados
    return len(digitos)

def contar_palabras_mayusculas(texto):
    # Encuentra todas las palabras en mayúsculas en la cadena
    palabras_mayusculas = re.findall(r'\b[A-Z]+\b', texto)
    palabras_minusculas = re.findall(r'\b[a-z]+\b', texto)
    palabras_mayusculas/(palabras_minusculas-1)
    # Devuelve el número de palabras en mayúsculas encontradas
    return len(palabras_mayusculas)


conteo_enlaces_por_fila = df['Message'].apply(lambda x: contar_enlaces(x))
conteo_palabras_por_fila = df['Message'].apply(lambda x: contar_palabras(x))
conteo_digitos=df['Message'].apply(lambda x: contar_caracteres_numericos(x))

datos_numericos = np.column_stack((conteo_enlaces_por_fila, conteo_palabras_por_fila,conteo_digitos))


nuevo_df = pd.DataFrame()
nuevo_df['Category'] = df['Category']
nuevo_df['Vector'] = datos_numericos.tolist()

print("Nuevo DataFrame con datos numéricos:")
print(nuevo_df)



