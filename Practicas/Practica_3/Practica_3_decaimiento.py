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

on=st.toggle("Funciones a tomar en consideranción para los fit")

if on:
    st.markdown('Para una distribución Gaussiana se utilizará:')
    st.latex('A*[\exp{(-{(x-U)}/{R})^2}]/2')
    st.markdown('Para una distribución de Poisson se utilizará:')
    st.latex('A*[(u^x\exp(-u))/\Gamma(x+1)]')

    # st.markdown("Encontrar la función adecuada para las dos tipos de radiaciones mediante la comprobación del chi-cuadrado.")
st.divider()
st.subheader("Objetivo")
st.markdown("Encontrar la función que se ajuste a los datos recolectados y comprobar cual de estas se ajusta mejor con la herramienta de chi-cuadrado.")
st.divider()
option=st.selectbox(
    "Graficas ajustadas encontradas",
    ("Radiación del aire (Poisson)", "Radiación del aire (Gaussiana)", "Radiación Cesio-137 (Gaussiana)")
)

if option == "Radiación del aire (Poisson)":
    col1, col2 = st.columns(2)
    col1.metric("Parametros de la función", "U=2.46674", " ")
    col2.metric(" ", "A=248.233", " ")
    col1.metric("Chi-cuadrado 1", "115875954952561.1", " ")
    col1.metric("Chi-cuadrado 2", "6.5193", " ")
    st.image("https://imgur.com/cky8vqE.png", width=700)

    
if option == "Radiación del aire (Gaussiana)":
    col1, col2, col3 = st.columns(3)
    col1.metric("Parametros de la función", "U=2.18871", " ")
    col2.metric(" ", "A=63.5732", " ")
    col3.metric(" ", "R=1.59884", " ")
    col1.metric("Chi-cuadrado 1", "2.5057e+42", " ")
    col1.metric("Chi-cuadrado 2", "51.9177", " ")
    imgur_url = "https://imgur.com/XrtRfU4.jpg"
    st.image(imgur_url, width=700)

if option == "Radiación Cesio-137 (Gaussiana)":
    col1, col2, col3 = st.columns(3)
    col1.metric("Parametros de la función", "U=442.628", " ")
    col2.metric(" ", "A=4.9925", " ")
    col3.metric(" ", "R=23.0569", " ")
    col1.metric("Chi-cuadrado", "589.920", " ")
    st.image("https://imgur.com/iAyjfoj.png", width=700)

on=st.toggle("Discusión de resultados")

if on:
    st.markdown(''':o: Al hacer el fit para la distribución de Poisson para el Cesio-137 se vio que no tiene correlación alguna con los datos
                obtenidos por lo que al no dar información relevante se decidió no incluir en los resultados de la practica.''')
    st.markdown(''':o: Dada la función que se utilizó para la distribución de Poisson se necesitó incluir una constante A que nos ayudara
                a escalar la función.''')
    st.markdown(''':o: Se consideró la función gamma en lugar de la exponencial por practicidad del investigador.''')

on=st.toggle("Conclusiones")

if on:
    st.markdown(''':o: Para la medición en el ambiente podemos concluir que la función que más se acerca es una de Poisson y para la del cesio-137 una Gaussiana.''')
    st.markdown(''':o: Para la medición de radiación ambiente se tuvo que omitir el primer termino medido para el chi-cuadrado ya que este tomaba valores anomalos,
                que se pueden apreciar en la diferencia entre el chi-cuadrado 1 y el chi-cuadrado 2. La justificación para este recorte es que se consideró 
                el primer termino como una perturbación externa causada por nuestro medidor, considerando picos de voltaje al encenderse, comunes en electronicos. 
                Esto no seria necesario para la medición del cesio ya que al tener valores muy superiores esta perturbación no tendría tanta relevancia.''')
    st.markdown(''':o: Para obtener un valor de chi-cuadrado más optimo para la distribución Gaussiana en el cesio es necesario tomar más datos, que hallamos obtenido 
                un valor alejado de 1 no quiere decir que sea una mala función para llegar a esa conclusión es necesario tomar mas datos.''')
on=st.toggle("Más infomación")

if on:
    st.markdown(":o: [Contador Geiger](https://es.wikipedia.org/wiki/Contador_Geiger)")
    st.markdown(":o: [Partícula beta](https://es.wikipedia.org/wiki/Part%C3%ADcula_beta)")
    st.markdown(":o: [Cesio-137](https://es.wikipedia.org/wiki/Cesio-137)")
    st.markdown(":o: [Prueba Chi-cuadrado](https://datatab.es/tutorial/chi-square-test)")

