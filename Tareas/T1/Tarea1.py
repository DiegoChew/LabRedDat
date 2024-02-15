import numpy as np 

#datos
time = [6.29, 6.37, 6.35, 6.62, 6.23, 6.39, 6.4, 6.29]
dis = [10.06, 10.02, 10.09, 10.05, 9.78, 9.99, 9.69, 9.85]

#varianza con N-1
desviacion_t = np.std(time, ddof=1)
desviacion_d = np.std(dis, ddof=1)

#promedio
prom_t = np.mean(time)
prom_d = np.mean(dis)

print("Varianza de tiempo:", desviacion_t)
print("Varianza de distancia:", desviacion_d)
print("Promedio de tiempo:", prom_t)
print("Promedio de distancia:", prom_d)

#diferencia de cada elemento de la lista time
sum_t = []

for element_t in time:
    diff_t = element_t - prom_t  
    sum_t.append(diff_t)  

#diferencia de cada elemento de la lista dis

sum_d = []

for element_d in dis:
    diff_d = element_d - prom_d  
    sum_d.append(diff_d)

#multiplicacion de cada diferencia de terminos

array_t=np.array(sum_t)
array_d=np.array(sum_d)

t_d=array_d*array_t

#suma de la multiplicacion de sus diferencias

sum_t_d=np.sum(t_d)

print("Suma de la multiplicacion de sus diferencias",sum_t_d)

N_1=len(time)-1

result_td=(sum_t_d/N_1)

print("Resultado de S_td^2:", result_td)

#parciales de v=d/t

partial_t=-(prom_d / prom_t**2)

partial_d=1 / prom_t

print("parcial sobre t:", (partial_t*desviacion_t))
print("parcial sobre d:", (partial_d*desviacion_d))


S_v = np.sqrt(np.abs((partial_t * desviacion_t)**2 + (partial_d * desviacion_d)**2 + (2 *result_td * partial_d * partial_t)/N_1))
S_v2 = np.sqrt(np.abs((partial_t * desviacion_t)**2 + (partial_d * desviacion_d)**2))
print("Varianza de la velocidad:", S_v)
print("Varianza de la velocidad aprox:", S_v2)
# Resultados finales

print("Resultados:\n tiempo:",np.around(prom_t,1), "±", np.around(desviacion_t,1), "s\n distnacia:", np.around(prom_d,1), "±", np.around(desviacion_d,1) , "m\n velocidad:", np.around(prom_d/prom_t,2), "±", np.around(S_v,2), "m/s^2" )
