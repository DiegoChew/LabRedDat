import math
import numpy as np
import streamlit as st
import plotly.express as px
import pandas as pd
n=st.slider("ingrese la cantidad de valores por intento [n]",1,100)
p=st.slider("ingrese la cantidad de valores deseados entre los posibles casos [p]",1,100)
x=np.arange(n+1)

prob=[]
for x in range (n+1):
    binom=math.comb(n,x)
    p_x=(1/p)**x
    q_nx=(1-(1/p))**(n-x)
    # print(binom)
    # print('esta es p',p_x)
    # print('esta es q',q_nx)
    prob.append(binom*p_x*q_nx*100)
nn=np.arange(n+1)
df=pd.DataFrame({"x":nn,'prob':prob})
print(df)
st.bar_chart(data=df, x="x", y="prob")
