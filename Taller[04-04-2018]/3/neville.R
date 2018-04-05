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

pol1 <- neville(NULL,1,0.7651977)
pol2 <- neville(pol1,1.3,0.6200860)
pol3 <- neville(pol2,1.6,0.4554022)

print(pol3)
print(eval_polynomial_matrix(pol3,1.5))