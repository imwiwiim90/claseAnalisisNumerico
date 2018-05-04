# Construya un polinomio P(x) de grado 3 usando los siguientes puntos, (0,10), (1,15), (2,5) con tangente 1 en x=0, use dos metodos diferentes y responda cual es el mas optimo (diga cual es el criterio para ser mas optimo)

## Metodo 1: Lagrange.

Usando el metodo de lagrange, rapidamente se noto como no seria posible realizar la construccion del polinomio, esto debido a que lagrange obtiene solo los datos de los vectores X y Y  realizando asi las operaciones internamente, de esta manera usandolo de manera base lo maximo que se logro obtener fue un polinomio de grado 2 puesto que no hubo forma de integrar el punto de la derivada de la funcion f'(0)=1, aunque de haber logrado implementar dicha derivada se pudo notar algo en la forma en la que se resuelve este metodo, esto en comparacion al metodo 2 utilizado.

```R
lagrange.poly <- function(x, y) {
  
  l <- list() # List to store Lagrangian polynomials L_{1,2,3,4}
  k <- 1
  
  for (i in x) {
   num <- 1
   denom <- 1
   
   p <- x[! x %in% i]
   for (j in p) {
     num <- paste(num, "*", "(", 'x', " - ", as.character(j), ")", sep = "", collapse = "")
     denom <- paste(denom, "*", "(", as.character(i)," - ", as.character(j), ")", sep = "", collapse = "")
   }
    
   l[k] <- paste("(", num, ")", "/", "(", denom, ")", sep = "", collapse = "")
   k <- k + 1
  }

  eq <- 0
  
  for (i in 1:length(y)) {
    eq <- paste(eq, '+', as.character(y[i]), "*", l[[i]], sep = "", collapse = "")
  }

  x <- Var('x')

  return(sympy(paste("simplify(", eq, ")")))
}
```

Como visto en el codigo anterior se nota como para realizar las operaciones internas se pasa por un for() anidado, este viendose directamente afectado por el tamaño de nuestro vector de variables x, significando que a razon de mayor cantidad de datos en el vector, cada vez sera mas y mas demorado la resolucion del problema, igualmente notamos como obteniendo el polinomio de grado 2 ya muestra signos de demora al ofrecernos la respuesta.

## Metodos 2: Hermite.

Usando el metodo de Hermite, usado en el punto 2, se pudo obtener un resultado mayor a un polinomio de tercer grado, esto debido a que para poder hacer uso de este metodo fue necesario utilizar dos puntos adicionales de derivadas de la funcion para f'(1)=0 y f'(2)=0, esto debido a la manera en la que el programa obtiene las derivadas y las reemplaza en la funcion para obtener el polinomio.

```R

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

```
Como se pudo evidenciar en el codigo anterior, para realizar las operaciones se hace uso de 4 for(), ninguno de estos superando el numero de datos en el vector x, al no estar anidados, realiza cada for secuencialmente, y con esto al correrlo obtenemos un valor casi inmediato, este valor como dicho anteriormente no es de grado 3, en vez de esto es de grado 5, como se muestra a continuacion.

```
expression(4 * x^5 - 12.75 * x^4 + 4.5 * x^3 + 8.25 * x^2 + x + 
    10)
```

## Metodo mas optimo.

Segun todo lo dicho anteriormente, entre los metodos, se puede decir que el metodo de Hermite es mucho mas optimo, puesto que aunque no se haya logrado solucionar con Lagrange el problema, notamos como un polinomio de grado 2 resulta ser mas demorado en ser definido contra el metodo de Hermite que como fue mencionado nos obtuvo un polinomio de grado 5, esto se noto debido a que el metodo de lagrange hace uso de for() anidados, en cambio hermite tiene 4 for() que no se relacionan entre ellos permitiendolos moverse en secuencia rapidamente.

Por lo tanto se puede afirmar que el metodo de Hermite es el ganador entre estos dos. 
