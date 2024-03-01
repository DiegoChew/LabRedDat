import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
import streamlit as st
def binomial(x,n,p,q):
    comb=math.comb(n,x)
    p_x=p**x
    q_nx=q**(n-x)

    return comb*p_x*q_nx


n=50
p=1/2
q=1/2

lista=np.arange(n+1,step=0.1)
print(lista)

# diccionario
# a={'pc1':67,'pc2':80}
# print(a["pc1"])

data_table=pd.DataFrame({"x":lista})

# f=lambda x:x+1
# print('lamda:',f(7))

# def f(x):
#     return x+1

# data_table['Nueva'] =data_table["x"]-50
data_table['Pb']=data_table.apply(lambda row:binomial(row['x'],n,p,q),axis=1)

print(data_table)

bonimial_plot,axis=plt.subplots()
axis.bar(data_table['x'],data_table['Pb'])
axis.plot(data_table['x'],data_table['Pb'],color='C2')
# plt.show()

binomial_plot.savefig("imagen.png")
###########################################################

st.title('graficos binomiales')
st.pyplot(binomial_plot)