
library(plotrix)
t = seq(-2*pi,2*2*pi,0.01)

r_1 = function(t) ( 2 + cos(3*t) ) 

r_2 = function(t) ( (2 - exp(t)) )


r = function(t) (t)

png('intersecion.png')

radial.plot(sapply(t,r_1),t,rp.type='s',radial.lim=c(0,5),point.symbols='.')
par(new=TRUE)
radial.plot(sapply(t,r_2),t,rp.type='s',radial.lim=c(0,5),point.symbols='.',point.col='red',add=TRUE)


#polar.plot(c(0,1,1),c(0,10,20),rp.type='s')


dev.off()