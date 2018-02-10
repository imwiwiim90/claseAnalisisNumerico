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

```r
root <- function(n,E,x) {
	y <- 1/2*(x+n/x)
	while (abs(x - y) > E) {
		x <- y
		y <- 1/2*(x+n/x)
	}
	y
}
```

al evaluar la raíz cuadrada de `7`, con un error de `10e-4` y un valor inicial de `4` <a name="example"></a> se evalua `root(4,1.e-4,4)`  y se tiene que el resultado es `2.645751`

## Análisis

### Válidez

En el algoritmo la secuencia `{y_n}` esta dada por `y_n = g(y_(n-1))`, Lo que significa que este es un **algoritmo de punto fijo**. Para que la serie converja se deben cumplir ciertas propiedades de la función `g(x)`.

1. Si la función es continua en un intervalo [a,b], su imágen está dentro del intervalo [a,b], para todo x en el intervalo [a,b]. Entonces existe una solucion para `g(x) = x`.
2. La derivada de la función, dígase `g'(x)` existe en el intervalo [a,b] y existe una constante `c` tal que `|g'(x)| < c` y `0 < |c| < 1`

Para este caso en especial `g(x) = 1/2*(x + k/x)` (siendo `k` el número el cual quiere ser evaluado). Dado que `g(x)` no puede ser evaluado en `0` tomaremos un intervalo `[a,b]` con `a > 0` para verificar que `g(x)` cumpla las condiciones descritas.

1. Teniendo en cuenta el teorema del valor máximo, `g(x)`  en el intervalo [a,b] tiene máximos en `g(a)`,`g(b)` o donde su derivada sea cero. La derivada es nula exactamente cuando `x = k^(1/2)`, en el lado izquierdo del intervalo `g(a) = 1/2*(a + k/a)` y en el lado derecho del intervalo `g(b) = 1/2*(b + k/b)`. Para que la función `g(x)` tenga una imagen dentro del intervalo [a,b] se debe cumplir que:

```
a < k^(1/2)
b > k^(1/2)
b > 1/2*(a + k/a)
```

Esto quiere decir que la función tiene una solucion a `g(x) = x` si el intervalo tomado contiene a `k^(1/2)`.

2. La derivada de la función es `g'(x) = 1/2*(1 - k/x^2)`, debido a que la magnitud de la derivada debe ser menor a 1 en el intervalo se debe cumplir que para todo `x` se tiene que `x > (k/3)^1/2`.

Esto significa que si el intervalo a considerar es de la forma `a = (k/3)^1/2` y `b` lo suficientemente grande, la serie convergerá. Sabiendo que el algoritmo busca `g(x) = x` cuando esto sucede se tiene que `x = k^(1/2)`.

### Convergencia 

El algoritmo de punto fijo tiene una razón de convergencia de `O(c^n)` donde c es menor a `1` el cual limita la derivada de `g(x)`. Pero los límites de la derivada de `g(x)` dependen del intervalo en el que se trabaje [a,b], y el valor que se quiera evaluar `k`. Más precisos para un `x_0` y `k` dado. Analizando el [ejemplo](#example) trabajado al inicio se tiene que `x_0 = 1.5` y `k = 7`, `c` esta dado por `1/2*(1-7/(4)^2) = 0.28125` dando una razón de convergencia de `O(0.28^n)`. 

### Presición

Se sabe que el algoritmo de punto fijo tiene un error absoluto de la forma:

```
| y_n - y | < c^n/(1-c)*| y_1 - x_0 |
```

por lo que el error depende de las variables de entrada, para este caso en particular:

```
| y_n - y | < c^n/(1-c)*| 1/2*(k/x_0 - x_0) |
```