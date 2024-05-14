import streamlit as st
# Titulos, nombre, ref
#Resumen
#Marc. teorico
#   definicion de problema
#   Procedimiento experimental
#Discusión / conclusión

# Links
url_trained='https://i.imgur.com/Cu61u5F.png'
url_test= 'https://i.imgur.com/23a0MNH.png'

st.title('Modelos de Clasificación')
st.write('Diego Chew, 202103317; Saúl Nájera, 202107506')
st.write(' La práctica pretende presentar una explicación del modelo de clasificación desarrollado en clase, presentando los resultados y conclusiones sobre el producto final. Se hace también mención acerca de que es un modelo de clasificación, cuales son sus elementos más importantes y su funcionamiento. ')

def marco_teorico():
    st.title('Contexto Teórico')
    st.write('Es pertienente antes de presentar los resultados del código, hablar un poco acerca de los modelos de clasificación.\n Existen de hecho varios tipos de modelos, la regresión logística, máquina de vectores de soporte (SVM), Arboles de decisión, etc.\n\n Se empleará en lo consecuente a la discusión teórica, la palabra clase/categoría para clasificar las entradas dadas al modelo. En pocas palabras, a cada entrada que se le presente al modelo, se le asigna una clase/categoría. El modelo funciona tomando un conjunto de datos de entrenamiento, los cuales ya tienen una clase ya conocida, con ello, se desarrolla una función que pueda predecir la clase a la que pertenecen los ejemplos que aún no han sido etiquetados.\n\n Sobre los vectores de peso: Se refiere a un conjunto de valores numéricos que se utilizan para la asignación de importancias relativas a diferentes elementos de un sistema dado. Note la relevanción en que cada entrada sea un número real.\n\n Sobre la función característica: En pocas palabras es una función que mapea observaciones de un conjunto de datos (entendidos en su forma general, no necesariamente solo números) a un espacio donde cada dimensión corresponde a una característica específica de datos.  ')

def Resultados_obtenidos():
    st.title('Resultados y conclusiones')
    st.subheader('Algunos comentarios sobre el código')
    st.write('El modelo que se desarrolló fue algo del tipo binario, de lo discutido previamente, se sigue que se manejan dos clases, las cuales son asignadas dependiendo del dato someter al análisis. Para este modelo es importante tanto la elaboración de las función que definirán las clases a asignar, como la elaboración de un vector de peso apropiado. Se buscó hallar pesos que minimizaran las funciones de pérdida, esto es porque las funciones de perdida que se definen son una medidad de que tan bien "funciona" el modelo planteado. Es natural una vez definidas dichas función el concluir que una búsqueda por minimizar las funciones de pérdida es un aspecto favorable para la elaboración de un modelo efectivo. \n\n Se plantaron dos vectores, W_target y W_traini, los cuales cumplen que el primero es el vector al que teniamos que llegar (fué usado de referencia para generar los datos aleatorios del dataset) y W_traini es el vector al que se llegó. Es de notable interés que estos ajustes que se aplican sobre la W_traini, son determinados por las función de pérdida previamente definidas!  ')
    st.subheader('Resultados del modelo')
    st.write('Habiendo hecho bastante énfasis en la importancia de las funciones de pérdida, se emplearon para la determinación del vector de peso adecuado, se "entrenó" por así decirlo. Primero se construyo un vector de peso de manera aleatoria, y se construyó con ayuda de ese vector, todo un dataset que, en teoría, está perfectamente relacionado con el vector de peso propuesto. Entonces, una vez presente los datos a emplear y el resultado al que se aspira llegar, se emplean las funciones previamente mencionadas para hacer que un vector propuesto (suele se escogido el vector 0) se llegue a "ajustar" al vector de peso propuesto. \n\n A continuación se presentan los siguientes gráficos ')
    st.image(url_test, caption='\n\n Este primer gráfico representa el conjunto de datos generados por el vector de peso W_target.')
    st.image(url_trained,caption='Este segundo gráfico representa como se ajustó el vector de peso resultante W_traini')
    st.write('Es de hacer saber que la primera imágen representa los datos generados por el vector de peso target, mientras que la segunda imágen hace referencia a como el vector resultante de W_traini aplicado al conjunto de datos usados en el entrenamiento.')
    st.write('De este resultado se hacen las siguientes discusiones: \n\n Es concluyente que la función de pérdida que se empleará a lo largo de la modelación es de suma importancia, es ella la que a fin de cuentas, permite establecer que tan "acertado" es el modelo planteado. Se sigue de esto que los métodos para minimizar este tipo de funciones son también fundamentales para este estudio. \n\n Se el modelo de clasificación es una clasifición binaria, entonces las funciones y método empleados a lo largo de esta práctica son aplicables, de tener 2 o más posibles clases a clasificar, se tendría que recurrir a un función más delicada, sin embargo, su planteamiento matemático es de la misma naturaleza que el empleado durante de esta práctica, y de ello que su realización es posible.')

if st.button('Sección Teórica'):
    marco_teorico()

if st.button('Resultados y conclusiones generales'):
    Resultados_obtenidos()