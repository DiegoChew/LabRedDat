set terminal pdfcairo
set output 'plot_cesio_poisson.pdf'

set datafile separator ','

d=0


f(x)= A*(((u**x)*(exp(-u)))/(gamma(x+1)))

A=100
u=10

fit f(x) 'resultado_cesio.csv' using 1:2 every :::0::d via A,u

set yrange [1:10]
set xrange [0:500]
# plot 'resultado_cesio.csv' using 1:2, f(x)
plot 'resultado_cesio.csv' using 1:2, 'resultado_cesio.csv' every :::0::d using 1:2, f(x)
plot f(x)

# unset terminal