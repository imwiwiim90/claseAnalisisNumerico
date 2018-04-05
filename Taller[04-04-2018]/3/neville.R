library('Ryacas')

neville <- function(polynomials, x, y) {
	x_ <- Sym('x')
	if (is.null(polynomials)) {
		A <- matrix(Sym(0),1,2)
		m <- 0
	} else {
		m <- nrow(polynomials) 
		A <- matrix(Sym(0), m + 1, m + 2)
		A[1:m,1:(m+1)] <- polynomials
	}
	A[m+1,1] <- Sym(x) 
	A[m+1,2] <- Sym(y)
	if (m >= 1)
	for (i in 3:(m+2)) {
		A[m+1,i] <- ((x_ - A[m-i+3, 1])*A[m+1,i-1] - (x_ - A[m+1,1])*A[m,i-1]) / (Sym(A[m+1,1]) - Sym(A[m-i+3, 1]))
	}
	A
}

eval_polynomial_matrix <- function(polynomials,x) {
	m <- nrow(polynomials)
	A <- matrix(0,m,m)
	for (i in 1:m) 
		for (j in (1:i)+1) {
			A[i,j-1] <- Eval(Sym(polynomials[i,j]),list(x=x))
		}
	A
}


x <- c(0 ,0.06,0.12,0.18,0.24,0.30)
y <- c(0,0.0017295,0.0066491,0.0143811,0.0245814,0.0369363)

pol <- NULL
for (i in 1:length(x)) {
	pol <- neville(pol,x[i],y[i])
}
print(eval_polynomial_matrix(pol,0.25))
