library('Ryacas')
#install.packages('rootSolve',repos = "http://cran.us.r-project.org")
library('rootSolve')

options(warn=-1)
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

x <- c(0, 1, 2)
y <- c(10, 15, 5)
dy <- c(1,0,0)

h_poly = hermite_interpolation(x,y,dy)
print(h_poly)
