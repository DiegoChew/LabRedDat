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
    return len(extractor.find_urls(texto))

# Función para contar palabras clave en el texto
def contar_palabras(texto):
    patron_palabras = r'\b(?:win|free|won|txt|call|now|claim|winner|stop)\b'
    return len(re.findall(patron_palabras, texto, flags=re.IGNORECASE))

# Función para contar caracteres numéricos en el texto
def contar_caracteres_numericos(texto):
    return len(re.findall(r'\d', texto))

# Función para contar palabras en mayúsculas
def contar_palabras_mayusculas(texto):
    return len(re.findall(r'\b[A-Z]+\b', texto))

def contar_palabras_minusculas(texto):
    return len(re.findall(r'\b[a-z]+\b', texto))

def media_palabras(texto):
    minusculas = contar_palabras_minusculas(texto)
    mayusculas = contar_palabras_mayusculas(texto)
    if mayusculas != 0:
        return minusculas / mayusculas
    else:
        return 0

def contar_caracteres_especiales(texto):
    patron_especiales = r'[!@#$%^&*()_+\-=\[\]{};:.,"\\|<>\/?]'
    return len(re.findall(patron_especiales, texto))

# Aplicar funciones de conteo a cada fila del DataFrame
conteo_enlaces_por_fila = df['Message'].apply(contar_enlaces)
conteo_palabras_por_fila = df['Message'].apply(contar_palabras)
conteo_palabras_media = df['Message'].apply(media_palabras)
conteo_digitos = df['Message'].apply(contar_caracteres_numericos)
conteo_especiales = df['Message'].apply(contar_caracteres_especiales)

# Combinar los datos en una matriz numérica
datos_numericos = np.column_stack((conteo_enlaces_por_fila, conteo_palabras_por_fila, conteo_digitos, conteo_palabras_media,conteo_especiales))

# Crear un nuevo DataFrame con los datos numéricos
nuevo_df = pd.DataFrame()
nuevo_df['Category'] = df['Category']
# nuevo_df['Vector'] = datos_numericos.tolist()
nuevo_df['Vector'] = [np.array(vec) for vec in datos_numericos]

nuevo_df['Category'] = nuevo_df['Category'].map({'ham': 1, 'spam': -1})
# Imprimir el nuevo DataFrame
print("Nuevo DataFrame con datos numéricos:")
print(nuevo_df)

nuevo_df.to_csv('nuevo_ds.csv', index=False)
# Entrenamiento del modelo
max_iterations = 100
W_training = np.zeros(5)

for iteration in range(max_iterations):
    mean_loss = np.mean([loss_sq(W_training, tds_i[1], tds_i[0]) for tds_i in nuevo_df.to_numpy()])
    mean_grad_loss = np.mean([grad_loss_sq(W_training, tds_i[1], tds_i[0]) for tds_i in nuevo_df.to_numpy()], axis=0)

    W_training -= mean_grad_loss * 0.01

print("Final weights:", W_training)
# max_iterations = 500
X = np.array([vec[:3] for vec in nuevo_df['Vector']])
y = nuevo_df['Category'].values

# Crear el scatter plot 3D
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
colors = {1: 'green', -1: 'red'}

for category in np.unique(y):
    ix = np.where(y == category)
    ax.scatter(X[ix, 0], X[ix, 1], X[ix, 2], c=colors[category], label=f'Category {category}', alpha=0.6)

ax.set_xlabel('Dimensión 1')
ax.set_ylabel('Dimensión 2')
ax.set_zlabel('Dimensión 3')
ax.set_title('Scatter plot de las primeras tres dimensiones del vector')
ax.legend()



# Dibujar el vector de peso encontrado
origin = np.zeros(3)
ax.quiver(*origin, *W_training[:3], color='blue', length=10, normalize=True, label='Vector de peso')
ax.legend()

plt.show()


predictions = np.array([get_y_prediction(W_training, vec) for vec in nuevo_df['Vector']])
accuracy = np.mean(predictions == nuevo_df['Category'])

print(f'Accuracy: {accuracy * 100:.2f}%')

# Matriz de confusión
confusion_matrix = pd.crosstab(nuevo_df['Category'], predictions, rownames=['Actual'], colnames=['Predicted'], margins=True)
print('Confusion Matrix:')
print(confusion_matrix)

###############################
# Predicciones del modelo
predictions = np.array([get_y_prediction(W_training, vec) for vec in nuevo_df['Vector']])
actual = nuevo_df['Category'].values
