import numpy as np
import streamlit as st
import plotly.express as px
import pandas as pd
from scipy import optimize as sco
from scipy.special import comb
import math

def binom(x, n, p):
    comb_vals = comb(n, x)
    p_x = p**x
    q_nx = (1-p)**(n-x)
    return comb_vals * p_x * q_nx
# Título de la página
st.caption("Práctica 1")
st.title("Distribución binomial en lanzamientos de monedas")
 # Texto a mostrar
st.header("Objetivo general")
st.markdown(":coin: Corrobrar la relación de probabilidad en los lanzamientos de monedas con la distribución binomial.")
st.subheader("Objetivos secundarios")
st.markdown(":coin: Corrobrar la relación de probabilidad entre la cantidad de lanzamientos.")
st.markdown(":coin: Corrobrar la necesidad de cantidad de datos para una mejor interpretación.")
st.divider()
# texto = "Esta página tiene como fin graficar un histograma que muestre la distribución de conteos de caras de los primeros n tiros de 10 monedas, donde n va desde 1 a 100 tiros. Está diseñada de tal manera que se puede observar la distribución para cada caso respectivo"

# Mostrar el texto
# st.write(texto)

st.markdown("Para esta practica se consideró dos distribuciones de datos, para la primera tendremos 100 datos donde en cada dato se lanzó 10 monedas y se contabilizó la cantidad de caras obtenidas, "
            "esta distribución se utilizará un deslizador que va contabilizando lo obtenido por cada tiro, encontrando su ajuste a la binomial, su desviación estándar por los datos medidos y por el ajuste encontrado"
            ". Para la segunda distribución se consideró 600 datos en loa cuales se lanzaron 10 monedas y se realizará lo mismo que se atrató anteriormente con el detalle que no tendremos el deslizador.")

sheet_id='1H943jgKOzqguRgjYEx7BPr5PoyvTXf7lfs9mqdlWBsk'

df=pd.read_csv('ConteosDeCarasPorPareja.csv')

on=st.toggle("Primera distribución")
if on:
    st.subheader("Primera distribución")
    m=st.slider("Ingrese la cantidad de intentos que desee contabilizar",1,100)
#

# Seleccionar las primeras m filas y la columna "Diego - Saul"
    df_team = df.iloc[:m, :]["Diego - Saul"]

# Calcular cuanto se repite cada valor
    repeat_counts = df_team.value_counts()

#Crear un rango de 0 a 10 para agregarlos a la tabla
    todos_numeros = range(11)

#Agregando los valores de los numeros que no aparecieron
    repeat_counts_index = repeat_counts.reindex(todos_numeros, fill_value=0)

    fit, cdds=sco.curve_fit(binom,repeat_counts_index.index,repeat_counts_index.values, [10,0.5], bounds=([0, 0], [100, 1]))

    n=fit[0]
    p=fit[1]


# print(n2)
# print(p2)
    listaDS=np.array(df_team)

    promDS=np.mean(listaDS)
    standardDS=np.std(listaDS)

    binomial_plot=px.line(x=repeat_counts_index.index,y=binom(repeat_counts_index.index,n,p),title=f"Binomial ajustada para {m} tiros", color_discrete_sequence=['#920A0A'])
    binomial_plot.add_bar(x=repeat_counts_index.index,y=repeat_counts_index.values/m, name="Lanzamientos", marker_color='#EFB810')
    binomial_plot.update_layout(xaxis_title="Cantidad de caras por tiro", yaxis_title="Cantidad de veces que obtivimos el caso")

    st.plotly_chart(binomial_plot)

    listbin_DS=np.array(binom([1,2,3,4,5,6,7,8,9,10],n,p))
    binDS=np.std(listbin_DS*10)
    print(listaDS)
    print(listbin_DS*m)
    print(repeat_counts.index)
    st.metric(label="Cantidad de elementos por tiro [n] obtenido por el fit", value=np.around(n,3))
    st.metric(label="Probabilidad de cada moneda obtenida [p] por el fit", value=np.around(p,3))
    st.metric(label=f"Promedio calculado por {m} tiros", value=np.around(promDS,3))
    st.metric(label=f"Desviación estandar calculada en {m} tiros de manera experimental", value=np.around(standardDS,3))
    st.metric(label=f"Desviación estandar calculada en {m} tiros considerando n={np.around(n,2)} y p={np.around(p,2)} ", value=np.around(binDS,3))

    ver_tabla = st.checkbox("Datos graficados en la primera distribución")

    if ver_tabla:
    # Mostrar el DataFrame si el botón está activado
        st.dataframe(df_team)

on2=st.toggle("Segunda distribución")
if on2:
    columns=['Lobsang - Rebeca','Guillermo - Shawn','Diego - Saul','Giovanna - Mario','Dessiré - Fabricio','Jacobo - Cesar']
    filter_columns=df[columns]

    melted_df = filter_columns.melt(var_name='column_name', value_name='value')

# Ordenar el DataFrame resultante
    sorted_df = melted_df.sort_values(by=['column_name'])

# print(sorted_df)

    values_g=sorted_df['value']

# print(values_g)

    repeat_values= values_g.value_counts()

# print(repeat_values)

    sorted_repeat_values=repeat_values.sort_index()

# print(sorted_repeat_values)

    fit2, cdds2=sco.curve_fit(binom,sorted_repeat_values.index,sorted_repeat_values.values, [10,0.5], bounds=([0, 0], [100, 1]))

    n2=fit2[0]
    p2=fit2[1]
    
    binomial_plot2=px.line(x=sorted_repeat_values.index,y=binom(sorted_repeat_values.index,n2,p2),title="Binomial ajustada", color_discrete_sequence=['#920A0A'])
    binomial_plot2.add_bar(x=sorted_repeat_values.index,y=sorted_repeat_values.values/600, name="Lanzamientos experimentales", marker_color='#EFB810')
    binomial_plot2.update_layout(xaxis_title="Cantidad de caras por tiro", yaxis_title="Cantidad de veces que obtivimos el caso")

    st.plotly_chart(binomial_plot2)
    prom=np.array(values_g)
    promT=np.mean(prom)
    standarT=np.std(prom)
    print(values_g)
    listbin_T=np.array(binom([1,2,3,4,5,6,7,8,9,10],n2,p2))
    binT=np.std(listbin_T*10)
    st.metric(label="Cantidad de elementos por tiro [n] obtenido por el fit", value=np.around(n2,3))
    st.metric(label="Probabilidad de cada moneda obtenida [p] por el fit", value=np.around(p2,3))
    st.metric(label=f"Promedio calculado por 600 tiros", value=np.around(promT,3))
    st.metric(label=f"Desviación estandar calculada en 600 tiros de manera experimental", value=np.around(standarT,3))
    st.metric(label=f"Desviación estandar calculada en 600 tiros considerando n={np.around(n2,2)} y p={np.around(p2,2)} ", value=np.around(binT,3))
    ver_tabla2 = st.checkbox("Datos graficados en la segunda distribución")

    if ver_tabla2:
    # Mostrar el DataFrame si el botón está activado
        st.dataframe(filter_columns)
st.divider()

st.subheader("Conclusiones")
st.markdown(":coin: Al considerar la primera distribución podemos notar una correlación de los datos graficados con la forma de una distribución binomial.")
st.markdown(":coin: El fit realizado en las distribuciones logra optener mejores resultados entre mayores datos tengamos.")
st.markdown(":coin: En ambas distribuciones se puede ver una clara correlación en la probabilidad de las monedas y una distribución binomal que va mejorando entre mayores datos tengamos.")
st.markdown(":coin: La distribución binomial al no ser una función continua tenemos un mayor error al encontrar nuestro fit.")

codigo_latex = r'''P(n ; k) = \binom{n}{k} \cdot p^k \cdot (1-p)^{n-k} '''
def mostrar_vineta():
    # Información e imágenes que deseas mostrar en la viñeta
    # st.markdown("sobre la distribución binomial")
    st.write("La distribución binomial como una distribución de probabilidad discreta, cuenta el número de éxitos de n ensayos con probabilidad fija 'p' independientes entre si. Estos ensayos son del tipo dicotómico, es decir, solo son posibles dos resultados, el éxito o fracaso. Naturalmente se define el fracaso como q=1-p; Notemos que la suma de probabilidades es igual a 1, p+q=1. La ecuación de la binomial viene dada por:")
 # Mostrar código LaTeX
    st.latex(codigo_latex)
#     st.write(" Mediante esta gráfica puede observar el comportamiento de esta gráfica")
#     st.markdown("""
#     <style>
#         .imagen {
#             display: block;
#             margin-left: auto;
#             margin-right: auto;
#         }
#     </style>
# """, unsafe_allow_html=True)

#     st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Binomial_distribution_pmf.svg/325px-Binomial_distribution_pmf.svg.png", caption="Descripción de la imagen", width=400, output_format='PNG', use_column_width=True)

viñeta_visible = False

# Botón para mostrar/ocultar la viñeta
if st.button("Presione acá para tener información acerca de la distribución binomial"):
    viñeta_visible = not viñeta_visible

if viñeta_visible:
    mostrar_vineta()

# print(fit)


