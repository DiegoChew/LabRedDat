set terminal pdfcairo
set output 'plot_aire_poisson.pdf'

set datafile separator ','

d=1


f(x)= A*(((u**x)*(exp(-u)))/(gamma(x+1)))

A=50
u=10

fit f(x) 'resultado_aire.csv' using 1:2 every :::0::d via u,A

set yrange [0:60]
set xrange [0:30]
# plot 'resultado_aire.csv' using 1:2, f(x)
plot 'resultado_aire.csv' using 1:2, 'resultado_aire.csv' every :::0::d using 1:2, f(x)
plot f(x)

# unset terminal