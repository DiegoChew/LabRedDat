import streamlit as st

st.caption("Integrantes: Saúl Nájera 202107506 - Diego Chew 202103317")

st.header("Practica 3 - Decaimiento de Cesio-137")

text = '''La practica consiste en medir la radiación de un elemento radiactivo, y encontrar un fit el cual se ajuste a los datos obtenidos.
Del mismo modo medir la radiación ambiente y encontrar un fit en el cual este ajuste de una manera optima.

Para esta practica el material radiactivo que se medirá es Cesio-137 el cual es un isotopo radiactivo producido principalmente por fisión 
nuclear, este tiene un periodo de semidesintegración de 30.23 años. El isotopo hemite principalmente partículas beta y decae a Bario-137. 

Para la medición usaremos un Contador Geiger, este nos permite medir la radiactividad de un objeto o lugar. El Contador es en sí un 
detector de partículas el cual no nos permite identificar la clase de partícula que detecta pero si un mínimo energético de estas. 
Este mínimo depende del tipo de medidor que utilizamos, estos están cubiertos por un metal fino que dependiendo del grosor del mismo 
nos permite "filtrar" que clase de partículas queremos detectar.  

Para comprobar si nuestro  fit fue exitoso en ambos casos se usará la pueba de "chi-cuadrado", la cual nos dice que tan cercana
es nuestra aproximación teorica encontrada por el fit, a los valores medidos.
'''

st.markdown(text)

on=st.toggle("Más infomación")

if on:
    st.markdown(":o: [Contador Geiger](https://es.wikipedia.org/wiki/Contador_Geiger)")
    st.markdown(":o: [Partícula beta](https://es.wikipedia.org/wiki/Part%C3%ADcula_beta)")
    st.markdown(":o: [Cesio-137](https://es.wikipedia.org/wiki/Cesio-137)")
    st.markdown(":o: [Prueba Chi-cuadrado](https://datatab.es/tutorial/chi-square-test)")