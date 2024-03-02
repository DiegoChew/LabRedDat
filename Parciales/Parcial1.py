# parcial1.py
# librerias
import math
import numpy as np
import streamlit as st
import plotly.express as px
import pandas as pd

#cuerpo del streaalit
st.caption('Parcial 1 Diego Garcia 202103317')
st.header(':blue[Graficadora de distribuciones binomiales]')
text='''Cuando queremos encontrar la distribución de probabilidad que cuente el número de
exitos en una secuencia de n intentos con dichos exitos dependiente de una 
probabilidad  p fija podemos considerar la distrubución binomial.

Esta considera dos resultados posibles, exito o fracaso donde la probabilidad 
de exito es p y el fracaso 1-p. Esta se plantea de la forma:'''

st.text(text)

st.latex(r'''P_B=\begin{pmatrix}
   n  \\
   x 
\end{pmatrix}p^x(1-p)^{n-x}''')

st.text('''La cuál tiene como significado la probabilidad de tener x exitos en una repetición 
de n experimentos.''')

st.text('''Para la graficadora tenemos 3 parametros a considerar:
            (1) Cantidad de elementos en una repetición [n].
            (2) Cantidad de valores que puede tener cada elemento de la repetición.
            (3) Cantidad de valores que consideramos como exito de cada elemento. ''')
st.divider()
st.markdown(''':red[Ejemplo:]''')
st.text('''Si quisieramos considerar 30 tiros por experimento de un dado de 6 caras y 
        queremos la probabilidad en la que de esos 30 tiros sean 2 de esas 6 caras 
        tenemos que considerar los siguientes parametros:''' )
st.text('''Para la graficadora tenemos 3 parametros a considerar: (1) 30. (2) 6. (3) 2. ''')

st.text('''Con dicho ejemplo podemos ver la probabilidad más grande es que 10 de los 30 dados
tengan al menos una de las dos lados que tomamos como exito.''')
st.divider()

#ingreso de datos por streamlit
n=st.slider("(1) Ingrese la cantidad de elementos por experimento [n].",1,100)
p=st.slider("(2) Ingrese la cantidad de valores posibles de cada item del experimento.",2,100)
p_1=st.slider("(3) Ingrese la cantidad de valores deseados de cada item del experimento.",1,p)

#posicion de los valores de la cantidad de valores deseados (eje x de la grafica)
x=np.arange(n+1)

# lista de probabilidades
prob=[]

for x in range (n+1): # un ciclo que va de 0 a n 
    binom=math.comb(n,x) # binomial para un n fijo y x dependiendo del for
    p_x=(p_1/p)**x #probabilidad de cada bloque de obtener lo deseado
    q_nx=(1-(p_1/p))**(n-x) #probabilidad restante
    prob.append(binom*p_x*q_nx) #agragar a la lista prob el resultado de la probabilidad por cada valor de x


x=np.arange(n+1)#regresamos a una lista x
df=pd.DataFrame({"Cantidad de valores deseados por experimento":x,'Probabilidad de exito':prob}) #tabla de datos


st.bar_chart(data=df, x="Cantidad de valores deseados por experimento", y="Probabilidad de exito", color='#CA6F1E') #grafica de barras de la tabla de datos

st.text('''Se consideró un deslizadores para el ingreso de datos dado que la grafica tendrá más "vida"
a la hora de selecionar los datos, ya que esta se estaria actualizando continuamente al deslizar, 
además facilita el contról de los parametros permitidos. ''')