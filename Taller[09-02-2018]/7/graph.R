d_t <- function(t) ((2*cos(t) - 2)^2 + (sin(t) - 1)^2) 
dd_t <- function(t) {}
body(dd_t) <- D(body(d_t),'t')

png("d'(t).png")
curve(dd_t,0,2*pi)
dev.off()

newton <- function(f,x0,E) {

	# derivative
	df <- function(x) {}
	body(df) <- D(body(f),'x')

	y = x0 - f(x0)/df(x0)
	i <- 0
	while (abs(x0 - y) > E) {
		text(x0,0,i,cex=0.8,col="red")
		x0 <- y
		y = x0 - f(x0)/df(x0)
		i <- i+1
	}
	y
}


d_t <- function(x) ((2*cos(x) - 2)^2 + (sin(x) - 1)^2) 
dd_t <- function(x) {}

body(dd_t) <- D(body(d_t),'x')

png("d'(t)_converge.png")
curve(dd_t,0,2*pi)
newton(dd_t,1,1.e-4)
dev.off()