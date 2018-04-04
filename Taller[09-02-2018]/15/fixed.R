
fixed <- function (g,x0,E) {
	x <- g(x0)
	while ( abs( g(x) - x ) > E ) {
		x <- g(x)
	}
	x
}


f1 <- function(x) (1/10*(5*x - exp(x) - 1))
g1 <- function(x) (x - f1(x))

fixed(g1,0,1e-2)
fixed(g1,2,1e-2)