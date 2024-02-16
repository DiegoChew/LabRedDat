# Para correr como pagina en Streamlit usar:
# streamlit run introduccion.py

import pandas as pd
from plotly import express as px
import streamlit as st

data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')
grafica=px.scatter(data,'bill_depth_mm','flipper_length_mm','species',)

st.title('Clasificación de pingüinos')
st.write('Clasificación de pungüinos por profundidad del pico y la longitud de su aleta según su especie.')
st.plotly_chart(grafica)


