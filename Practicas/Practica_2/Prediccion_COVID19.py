import streamlit as st
# imagenes
img1_url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Binomial_distribution_pmf.svg/325px-Binomial_distribution_pmf.svg.png"
img2_url= " https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSa0U_bvskSESz5CBAvgvxanovdF7jY4g9zKX3haiP6Aw&s"
st.title('Práctica 2 - Predicción de COVID19')
st.write("<span style = 'font-size= small;'> Intergrantes: Diego Chew, Saúl Nájera", unsafe_allow_html= True )
st.markdown('La práctica consistió en utilizar los datos de los registros de casos de COVID19, tomados por el Ministerio de Salud. De los datos presentes, tomamos un intervalo de estos para hacer una predicción sobre la evolución de los contagios en Guatemala, por fortuna, al tener presente todos los datos, podemos verifcar si en efecto, nuestrea predicción fue relativamente certera o en caso contrario, completamente errónea.')
st.write('A rasgos generales, el problema que queremos abordar e insepccionar es el de establecer una predicción efectiva de un modelo probabilístico que nos permita arrojar un poco de luz acerca de la tendencia del sistema a medida que el tiempo transcurre. Se hace énfasis en que lo que buscamos es comparar el ajuste dado con los datos que luego eventualmente se recopilaron, para así poder concluir la efectividad de nuestro modelo.')
def txt_marco_teorico():
    st.title('Sobre la distribución Binomial y los Fits')
    st.write('Una distribución Binomial es un tipo de distribución probabilística la cual describe la probabilidad de un número fijo de eventos exitosos en un número fijo de ensayos (casos) independientes. Es de tener presente que (esto es muy importante) cada ensayo tiene solo dos posibles resultados, éxito o fracaso. Examinando esta definición en la práctica, los eventos son " Estar enfermo o estar Sano", note que tenemos únicamente dos posibles casos! De ello que es factible que esperaramos tener una distribución del tipo binomial. ')
    st.image(img1_url, use_column_width=True)
    st.title('Breve descripción de Gnuplot:')
    st.write('Es una herramienta de trazado gráfico (al parecer de código abierto) con una amplia aplicabilidad en los ámbitos científicos. En suma, permite visualizar datos y generar gráficos en una amplia variedad de formatos. Es de tener presente que Gnuplot es bastante bueno para hcaer ajustes/fits, tanto para ajustes lineales, no lineales, etc. ')
    st.image(img2_url, use_column_width=True)
if st.button('Hago click para saber acerca de la teória de la práctica.'):
    txt_marco_teorico()

    # Datos fit para 1 de junio de 2020
    # Final set of parameters            Asymptotic Standard Error
# =======================            ==========================
# A               = 298.164          +/- 14.24        (4.775%)
# u               = 90.5441          +/- 0.8669       (0.9575%)
# r               = 9.0499           +/- 0.863        (9.536%)
    
    # Datos fit para 15 de marzo de 2021
#     Final set of parameters            Asymptotic Standard Error
# =======================            ==========================
# A               = 682.927          +/- 27.36        (4.006%)
# u               = 247.195          +/- 8.098        (3.276%)
# r               = 135.612          +/- 10.01        (7.379%)