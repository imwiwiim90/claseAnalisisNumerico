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

En el algoritmo la secuencia `{y_n}` esta dada por `y_n = g(y_(n-1))`, Lo que significa que este es un **algoritmo de punto fijo**. Para que la serie converja se deben cumplir ciertas propiedades de la función `g(x)`.

1. La función es continua en un intervalo [a,b], su imágen está dentro del intervalo [a,b], para todo x en el intervalo [a,b].
2. La derivada de la función, dígase `g'(x)` existe en el intervalo [a,b] y existe una constante `k` tal que `|g'(x)| < k`

Para este caso en especial `g(x) = 1/2*(x + k/x)` (siendo `k` el número el cual quiere ser evaluado). Dado que `g(x)` no puede ser evaluado en `0` tomaremos un intervalo `[1,b]` para verificar que `g(x)` cumpla las condiciones descritas.

1. Teniendo en cuenta el teorema del valor máximo, `g(x)`  en el intervalo [1,b] tiene máximos en `g(1)`,`g(b)` o donde su derivada sea cero. La derivada no toma valores nulos, por lo que tiene un minimo en `g(1) = 1/2*(1 + k)` y un máximo en `g(b) = 1/2*(b + k/b)`. Para que la función `g(x)` tenga una imagen dentro del intervalo [1,b] se debe cumplir que:

```
k > 1

k < b^2 
```


