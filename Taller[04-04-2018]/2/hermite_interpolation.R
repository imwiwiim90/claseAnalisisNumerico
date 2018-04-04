library('Ryacas')

hermite_interpolation <- function(x,y,dy) {
	n <- length(x)
	D <- matrix(0,2*n,2*n)

	for (i in 1:n) {
		D[1,i*2-1] <- y[i]
		D[1,i*2] <- y[i]
		D[2,i*2-1] <- dy[i]
	}
	for (i in 1:(n-1)) {
		D[2,i*2] <- (D[1,i*2+1] - D[1,i*2])/(x[i+1] - x[i])
	}

	for (i in 3:(n*2)) {
		for (j in 1:(n*2-i+1)) {
			D[i,j] <- (D[i-1,j+1] - D[i-1,j])/( x[ceiling((i+j-1)/2)] - x[ceiling(j/2)] )
		}
	}
	x_ <- Sym('x')
	hermite_poly = y[1]
	mult_exp = expression(1)
	for (i in 2:(n*2)) {
		mult_exp = mult_exp*(x_ - x[ceiling((i-1)/2)])
		hermite_poly = hermite_poly + D[i,1]*mult_exp
	} 
	hermite_poly = Simplify(hermite_poly)
}


x_ <- Sym('x')
f <- log(x_)
df <- deriv(f)

x <- c(1,2) # puntos de referencia
y <- Eval(f, list(x = x))
dy <- Eval(df, list(x = x))

h_poly = hermite_interpolation(x,y,dy)
print(h_poly)

points_x <- seq(0.5, 4, 0.05)
points_y <- Eval(f,list(x = points_x))

h_points_y <- Eval(h_poly,list(x = points_x))
png('interpolacion.png')
plot(points_x,points_y,type='l',xlab='x',ylab='y')
lines(points_x,h_points_y,col='red')
points(x,y)
legend('topleft',legend=c('ln(x)','P(x)'),col=c('blue','red'), lty=c(1,1), cex=0.8)



