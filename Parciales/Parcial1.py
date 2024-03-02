import math
import numpy as np
import streamlit as st

def prob(x,n,p):
    comb=math.comb(n,x)
    p_x=p**x
    q_nx=(1-p)**(n-x)

    return comb*p_x*q_nx

print('hola siiii')