import streamlit as st
import pandas as pd
# Agregar el link de la pag de gob.
#Tabla de parámetros-------------
latex_table = r'''
\begin{array}{|c|c|}
\hline
\text{Columna 2} & \text{Columna 3} \\
\hline
A & 298.164 \\
u & 90.54 \\
r & 9.05  \\
\hline
\end{array}
'''
latex_table2 = r'''
\begin{array}{|c|c|}
\hline
\text{Columna 2} & \text{Columna 3} \\
\hline
A & 682.927 \\
u & 247.195 \\
r & 135.612 \\
\hline
\end{array}
'''
#--------------------------------

# imagenes------------------------------------
ecuacion_latex = r'f(x) = A e^{-\frac{(x - \mu)^2}{2r^2}}'
imgfit1= "/home/saul/Desktop/LabRedDat/Practicas/Practica_2/Fit 1.png"
imgfit1_1= "/home/saul/Desktop/LabRedDat/Practicas/Practica_2/Fit 1 Comparacion.png"
imgfit2= "/home/saul/Desktop/LabRedDat/Practicas/Practica_2/Fit 2.png"
#---------------------------------------------
img1_url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Binomial_distribution_pmf.svg/325px-Binomial_distribution_pmf.svg.png"
img2_url= " https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSa0U_bvskSESz5CBAvgvxanovdF7jY4g9zKX3haiP6Aw&s"
st.title('Práctica 2 - Predicción de COVID19')
st.write("<span style = 'font-size= small;'> Intergrantes: Diego Chew, Saúl Nájera", unsafe_allow_html= True )
st.markdown('La práctica consiste en evaluar los datos recolectados por el ministerio de Salud durante el COVID19, consideramos dos intervalos de tiempo para nuestro análisis, los elegimos bajo el criterio de estudiar los casos confirmados, ya que estamos manejando datos ya verificados; note que estudiar una etapa en la que se los registran síntomas del paciente no necesariamente implicaría una confirmación del hecho, creando así la posibilidad de tener un modelo aun más impreciso, por ello resulta apropiado manejar datos ya verificados. Al tomar un intervalo dado como muestra, tenemos limitada información sobre el comportamiento del sistema, sin embargo, podriamos conjeturar modelos matemáticos que puedan aproximadamente replicar, cuanto menos, la tendencia y/o comportamiento general del sistema. Motivados por esa idea, al tener en el caso del COVID19, una distribución de datos que, de cierta forma, tienen una densidad de probabilidad asociada, es natural sugerir modelos que arrojen luz sobre la cuestión. Notemos de que existe únicamente entre los posibles resultados el estar enfermo de COVID19 y el no estar enfermo; tenemos todo el derecho de poder conjeturar una distribución del tipo binomial, justificados por la misma idea previamente elaborada, se tienen únicamente el "éxito" o el "fallo".')
st.write('A rasgos generales, el problema que queremos abordar es el de establecer una predicción efectiva de un modelo probabilístico que nos permita arrojar un poco de luz acerca de la tendencia del sistema a medida que el tiempo transcurre. Se hace énfasis en que lo que buscamos es comparar el ajuste dado con los datos que luego eventualmente se recopilaron, para así poder concluir la efectividad de nuestro modelo.')
def txt_marco_teorico():
    st.title('Sobre la distribución Binomial y los Fits')
    st.write('Una distribución Binomial es un tipo de distribución probabilística la cual describe la probabilidad de un número fijo de eventos exitosos en un número fijo de ensayos (casos) independientes. Es de tener presente que (esto es muy importante) cada ensayo tiene solo dos posibles resultados, éxito o fracaso. Examinando esta definición en la práctica, los eventos son " Estar enfermo o estar Sano", note que tenemos únicamente dos posibles casos! De ello que es factible que esperaramos tener una distribución del tipo binomial. ')
    st.image(img1_url, use_column_width=False)
    st.title('Breve descripción de Gnuplot:')
    st.write('Es una herramienta de trazado gráfico (al parecer de código abierto) con una amplia aplicabilidad en los ámbitos científicos. En suma, permite visualizar datos y generar gráficos en una amplia variedad de formatos. Es de tener presente que Gnuplot es bastante bueno para hcaer ajustes/fits, tanto para ajustes lineales, no lineales, etc. En esta práctica en particular, utilizamos a Gnuplot como herramienta para hacer el ajuste de la binomial sobre la distribuición de datos empleada.')
    st.image(img2_url, use_column_width=False)
    st.write('La ecuación que buscamos ajustar viene dada por:')
    st.latex(ecuacion_latex)
    st.write('Los parámetros fueron encontrados mediante las herramientas de gnuplot.')
if st.button('Haga click para saber acerca de la teória de la práctica.'):
    txt_marco_teorico()
def txt_Discusión_Resul():
    st.title('Resultados generales y su discusión.')
    st.write('En los intervalos de tiempo que empleamos se empezó en ambos el 13 de marzo de 2020, siendo esa la fecha del primer confirmado de COVID19 en Guatemala. El primer intervalo termina el 1 de Junio de 2020 y el segundo intervalo termina el 15 de marzo de 2021')
    st.markdown('<p style="font-size: 23px;">Para el primer intervalo se tuvo lo siguiente:</p>', unsafe_allow_html=True)
    st.image(imgfit1, caption= 'Del 13 de marzo de 2020 a 1 de junio de 2020')
    st.write('Es de notable interés que la tendencia general del cuerpo de datos sigue la forma propuesta. Si desplazamos este mismo intervalo unos días más, se presenta la siguiente nueva gráfica, note que se incluyó el ajuste hecho durante el primer intervalo.')
    st.write('Los parámetros que se obtuvieron para este ajuste fueron:')
    st.latex(latex_table)
    st.image(imgfit1_1, caption= 'Del 13 de marzo de 2020 a unos días después de 1 de junio de 2020')
    st.write('Evidentemente el intervalo empleado es insuficiente para proponer una predicción cercana a la realidad, sin embargo, puede ser observado que estudiando la distribución de datos hasta ese punto, la tendencia de la gráfica parece se del tipo Poisson ! .')
    st.markdown('<p style="font-size: 23px;">Para el segundo intervalo se tuvo lo siguiente:</p>', unsafe_allow_html=True)
    st.image(imgfit2, caption='Del 13 de marzo de 2020 a 15 de marzo de 2021')
    st.write('A inspección directa, es concluyente que el ajuste con la binomial no parece ser eficiente, la distribución de datos parace caracterizarse por dos picos en la cantidad de contagios. Es concluyente que para intervalos grandes, un ajuste mediante un modelo binomial es impreciso.')
    st.write('Los parámetros que se determinaron para el ajuste fueron: (Note que este ajuste es mucho más impreciso que el del primer intervalo))')
    st.latex(latex_table2)
    st.title('Conclusiones ')
    st.write(' 1. Es concluyente que una predicción a largo y mediano plazo es incompatible con un modelo de distribución binomial, una razón bastante específica es que la binomial se caracteriza por un máximo solo, impide la posibilidad de un comportamiento en los datos como los evaluados en la práctica. Es preciso emplear otro modelo. Una razón por la cual este modelo falla, es que se asume una probabilidad constante asociada al evento, no toma en cuenta que los factores sociales, econónmicos, entre otros, pueden inducir un cambio en la probabilidad de contagio !.')
    st.write(' 2. Puede ser extraido de estos resultados la siguiente observación: La distribución binomial parece mejorar cuando se consideran intervalos "pequeños" de tiempo, es de hecho una conclusión que podemos deducir de la previa conclusión, ya que en intervalos "suficientemente cortos" podemos albergar en nuestra distribución un único máximo, de ello que un modelo de distribución binomial puede llegar a ser efectivo.')

if st.button('Haga click para saber acerca de los resultados generales y su discusión.'):
    txt_Discusión_Resul()







# Datos fit para 1 de junio de 2020; gráfica: Fit 1 
# Final set of parameters            Asymptotic Standard Error
# =======================            ==========================
# A               = 298.164          +/- 14.24        (4.775%)
# u               = 90.5441          +/- 0.8669       (0.9575%)
# r               = 9.0499           +/- 0.863        (9.536%)
    
    # Datos fit para 15 de marzo de 2021, Gráfica: Fit 2
#     Final set of parameters            Asymptotic Standard Error
# =======================            ==========================
# A               = 682.927          +/- 27.36        (4.006%)
# u               = 247.195          +/- 8.098        (3.276%)
# r               = 135.612          +/- 10.01        (7.379%)