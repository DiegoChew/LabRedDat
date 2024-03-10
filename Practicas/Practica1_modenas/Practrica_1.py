import numpy as np
import streamlit as st
import plotly.express as px
import pandas as pd
from scipy import optimize as sco
from scipy.special import comb
import math

def binom(x, n, p):
    x = np.asarray(x)  # Convertir a array si es necesario
    n = int(n)
    comb_vals = comb(n, x)
    p_x = p**x
    q_nx = (1-p)**(n-x)
    return comb_vals * p_x * q_nx

sheet_id='1H943jgKOzqguRgjYEx7BPr5PoyvTXf7lfs9mqdlWBsk'

df=pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

n=st.slider("Ingrese la cantidad de intentos",1,100)


# Seleccionar las primeras n filas y la columna "Diego - Saul"
df_team = df.iloc[:n, :]["Diego - Saul"]

# Calcular cuanto se repite cada valor
repeat_counts = df_team.value_counts()

#Crear un rango de 0 a 10 para agregarlos a la tabla
todos_numeros = range(11)

#Agregando los valores de los numeros que no aparecieron
repeat_counts_index = repeat_counts.reindex(todos_numeros, fill_value=0)

#crear un dataframe para graficar  
df_grafico = pd.DataFrame({'Cantidad de caras por tiro': repeat_counts_index.index, 'Cantidad de veces que obtivimos el caso': repeat_counts_index.values})

#grafica de barras de la tabla de datos
# st.bar_chart(df_grafico, x="Cantidad de caras por tiro", y="Cantidad de veces que obtivimos el caso", color='#CA6F1E')

xD=np.array(repeat_counts.index)
# print(xD)
yD=np.array(repeat_counts.values)
# print(yD)
fit, cdds=sco.curve_fit(binom,repeat_counts_index.index,repeat_counts_index.values,p0=[np.mean(xD), np.mean(yD)/n], bounds=([0, 0], [100, 1]))

n=fit[0]
p=fit[1]


binomial_plot=px.line(x=repeat_counts_index.index,y=binom(repeat_counts_index.index,n,p),title="Binomial ajustada")
binomial_plot.add_bar(x=repeat_counts_index.index,y=repeat_counts_index.values/100, name="Lanzamientos experimentales", marker_color='#CA6F1E')
binomial_plot.update_layout(xaxis_title="Cantidad de caras por tiro", yaxis_title="Cantidad de veces que obtivimos el caso")

st.plotly_chart(binomial_plot)



# print(fit)

