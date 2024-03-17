import numpy as np
import streamlit as st
import plotly.express as px
import pandas as pd
from scipy import optimize as sco
from scipy.special import comb
import math

# Título de la página
st.title("Práctica 1- Distribución binomial en lanzamientos de moneda")
 # Texto a mostrar
texto = "Esta página tiene como fin graficar un histograma que muestre la distribución de conteos de caras de los primeros n tiros de 10 monedas, donde n va desde 1 a 100 tiros. Está diseñada de tal manera que se puede observar la distribución para cada caso respectivo"
    
# Mostrar el texto
st.write(texto)

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
# Agregue los datos de el fit.
val_fit=[n,p]
tb1=pd.DataFrame(val_fit, columns=["Datos del fit"])
st.table(tb1)
# Agregue un botón para desplegar la tabla de datos a plotear. 
st.write('Para ver la tabla de datos que se graficaron, pulse el botón que esta debajo de este texto')

ver_tabla = st.checkbox("Mostrar/ocultar tabla")

if ver_tabla:
    # Mostrar el DataFrame si el botón está activado
    st.dataframe(df_team)

codigo_latex = r'''P(X ; k) = \binom{n}{k} \cdot p^k \cdot (1-p)^{n-k} '''
def mostrar_vineta():
    # Información e imágenes que deseas mostrar en la viñeta
    st.markdown("sobre la distribución binomial")
    st.write("Defínase la distribución binomial como una distribución de probabilidad discreta que, en pocas palabras, cuenta el número de éxitos de n ensayos independientes entre si con una probabilidad fija p. Estos ensayos son del tpo dicotómico, es decir, solo son posibles dos resultados, el éxito y el fracaso. Naturalmente definimos a consecuencia que el fracaso está dada por q=1-p; Notemos que se satisface p+q=1. Su ecuación viene dada por")
 # Mostrar código LaTeX
    st.latex(codigo_latex)
    st.write(" Mediante esta gráfica puede observar el comportamiento de esta gráfica")
    st.markdown("""
    <style>
        .imagen {
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
""", unsafe_allow_html=True)

    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Binomial_distribution_pmf.svg/325px-Binomial_distribution_pmf.svg.png", caption="Descripción de la imagen", width=400, output_format='PNG', use_column_width=True)

viñeta_visible = False

# Botón para mostrar/ocultar la viñeta
if st.button("Presione acá para tener información acerca de la distribución binomial"):
    viñeta_visible = not viñeta_visible

if viñeta_visible:
    mostrar_vineta()

# print(fit)

