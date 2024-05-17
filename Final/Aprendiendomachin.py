#aprendiendomachin.py

import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt
import re 

def get_y_prediction(W, phi):
    score = np.dot(W, phi)
    if score > 0:
        y_predict = 1
    elif score == 0:
        y_predict = np.nan
    elif score < 0:
        y_predict = -1

    return y_predict

def loss_sq(W, phi, y):

    score = np.dot(W, phi)
    pepi2 = score - y

    return pepi2**2

def grad_loss_sq(W, phi, y):
    # Se realiza el calculo algebraico del gradiente para llegar a esta funcion:
    score = np.dot(W, phi)
    pepi2 = score - y

    return 2*pepi2*phi

