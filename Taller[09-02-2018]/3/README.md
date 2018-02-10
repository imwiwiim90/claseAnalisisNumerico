# Raíz cuadrada

Implemente en R el siguiente algoritmo que sirve para calcular la raíz cuadrada. Aplíquelo para evaluar la raíz cuadrada de 7, analize su precisión, convergencia y validez.

```
Algoritmo: Raíz cuadrada
Entra:	n	Dato
		E 	Error permitido
		x 	Valor inicial
Sale: 	y 	Respuesta con error E
y <- 1/2(x + n/x)
Repetir mientras | x - y | > E
	x <- y
	y <- 1/2*(x + n/x)
Fin
```

## Código

La implementación en R es la siguiente:

```
root <- function(n,E,x) {
	y <- 1/2*(x+n/x)
	while (abs(x - y) > E) {
		x <- y
		y <- 1/2*(x+n/x)
	}
	y
}
```

al evaluar la raíz cuadrada de 7, con un error de 10e-4 y un valor inicial de 1.5 `root(4,1.e-4,1.5)` se tiene que el resultado es `2.645751`

## Análisis

### Validez
En el algoritmo la secuencia `{y_n}` esta dada por `y_n = g(y_(n-1))`, Lo que significa que este es un algoritmo de punto fijo. Para que la serie converja se deben cumplir ciertas propiedades de la función `g(x)`.

1. La funcion es continua en un intervalo [a,b], está dentro del intervalo [a,b], para todo x en el intervalo [a,b].
2. La derivada de la funcion, dígase `g'(x)` existe en el intervalo [a,b]y existe una constante `k` tal que `|g'(x)| < k`


