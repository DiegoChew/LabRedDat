set terminal pdfcairo
set output 'plot_aire_bino.pdf'

set datafile separator ','

d=1

f(x) = A*exp(-((x-u)/r)**2/2)

A=100
u=50
r=25

fit f(x) 'resultado_aire.csv' using 1:2 every :::0::d via A,u,r

set yrange [0:60]
set xrange [0:30]
# plot 'resultado_aire.csv' using 1:2, f(x)
plot 'resultado_aire.csv' using 1:2, 'resultado_aire.csv' every :::0::d using 1:2, f(x)
plot f(x)

# unset terminal