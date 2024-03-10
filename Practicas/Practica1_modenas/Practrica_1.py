import math
import numpy as np
import streamlit as st
import plotly.express as px
import pandas as pd

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
repeat_counts = repeat_counts.reindex(todos_numeros, fill_value=0)

#crear un dataframe para graficar  
df_grafico = pd.DataFrame({'Cantidad de caras por tiro': repeat_counts.index, 'Cantidad de veces que obtivimos el caso': repeat_counts.values})


st.bar_chart(df_grafico, x="Cantidad de caras por tiro", y="Cantidad de veces que obtivimos el caso", color='#CA6F1E') #grafica de barras de la tabla de datos

