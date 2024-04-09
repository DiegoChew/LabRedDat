# file: fit_csv.gnuplot
# set terminal pdfcairo
# set output 'plot.pdf'

set datafile separator ','

<<<<<<< HEAD
<<<<<<< HEAD
d=1

f(x) = A*exp(-((x-u)/r)**2/2)

A=400
u=200
r=100

fit f(x) 'csv_filtrado.csv' using 1:3 every :::0::d via A,u,r

set xrange [0:600]
set yrange [0:2000]
plot 'csv_filtrado.csv' every :::0::d using 1:3, f(x)
<<<<<<< HEAD
=======
d=0
=======
d=1
>>>>>>> 70ca94c (Listones)

f(x) = A*exp(-((x-u)/r)**2/2)

A=400
u=200
r=100

fit f(x) 'csv_filtrado.csv' using 1:3 every :::0::d via A,u,r

set xrange [0:400]

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f187724 (Nuevo csv)
=======
# plot 'csv_filtrado.csv' using 1:3,
>>>>>>> 70ca94c (Listones)
=======
plot 'csv_filtrado.csv' using 1:3, 'csv_filtrado.csv' every :::0::d using 1:3, f(x)
>>>>>>> a75b876 (Ahora si)
=======
>>>>>>> 9608f46 (Imagenes)
