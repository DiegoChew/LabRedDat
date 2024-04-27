set terminal pdfcairo
set output 'plot_cesio_bino.pdf'

set datafile separator ','

d=1

f(x) = A*exp(-((x-u)/r)**2/2)

A=205
u=25
r=50

fit f(x) 'resultado_cesio.csv' using 1:2 every :::0::d via A,u,r

set yrange [0:10]
set xrange [300:500]
# plot 'resultado_cesio.csv' using 1:2, f(x)
plot 'resultado_cesio.csv' using 1:2, 'resultado_cesio.csv' every :::0::d using 1:2, f(x)
plot f(x)

# unset terminal