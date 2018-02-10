
newton <- function(f,x0,E) {

	# derivative
	df <- function(x) {}
	body(df) <- D(body(f),'x')

	y = x0 - f(x0)/df(x0)
	while (abs(x0 - y) > E) {
		x0 <- y
		y = x0 - f(x0)/df(x0)
	}
	y
}


d_t <- function(x) ((2*cos(x) - 2)^2 + (sin(x) - 1)^2) 
dd_t <- function(x) {}
body(dd_t) <- D(body(d_t),'x')

x1 <- newton(dd_t,1,1.e-4)
x2 <- newton(dd_t,3,1.e-4)

print(x1)
print(x2)



print(paste('d(x1) = ', toString(d_t(x1))))
print(paste('d(x2) = ', toString(d_t(x2))))
print(paste('d(0) = ', toString(d_t(0))))
print(paste('d(2π) = ', toString(d_t(2*pi))))
