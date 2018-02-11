# Método de Newton

Utilice el método de Newton para resolver el problema, muestre gráficamente cómo se comporta la convergencia a la solución:

Una partícula se mueve en el espacio con el vector de posición `R(t)  = ( 2cos(t),sen(t),O )`. Se requiere conocer el tiempo en el que el objeto se encuentra más cerca del punto `P(2,1,O)`. Utilice el método de Newton con cuatro decimales de precisión.

## Entradas

El algoritmo de Newton encuentra las raíces de una función `f(x)` si dentro de un intervalo [a,b], esta es continua en segundo grado, la derivada no es igual a `0` y el valor inicial de entrada es cercano a la respuesta.

Se debe transformar el problema inicial a un equivalente problema de raíz, de este modo se sabe que la distancia entre dos puntos `(x1,y1,z1)` y `(x2,y2,z2)` es `[(x1 - x2)^2 + (y1 - y2)^2 + (z1 - z2)^2]^(1/2)`, de modo que la distancia del punto `P` y la función `R(t)` está determinada por `[ (2cos(t) - 2)^2 + (sen(t) - 1)^2 ]^(1/2)`, sin embargo por facilidad y una función equivalente tal que tiene la misma respuesta está dada por:

```
d(t) = (2cos(t) - 2)^2 + (sen(t) - 1)^2
```

Dado que es una función periódica con periodo `2π` basta con evaluar la función en el intervalo [0,2π].

El mínimo de la función `d(t)` según el *Teorema de los valores extremos* está en `0`,`2π` o cuando `d'(t) = 0`. Es aquí donde se aplica el *algoritmo de Newton* para encontrar `t` tal que `d'(t) = 0`.

Se utiliza `R` para calcular la derivada de la función `d(t)`  en [sol.R](sol.R) teniendo:

```
2 * (cos(t) * (sin(t) - 1)) - 2 * (2 * sin(t) * (2 * cos(t) - 2))
```

Está a simple vista se sabe que es continua, si embargo su derivada `d''(t)` puede tomar valores en `0` como se puede ver a continuación `d'(t)`:

![d'(t)](d'%28t%29.png)

Además, se puede observar que tiene 2 raíces. Por lo que se deben evaluar 4 puntos.

## Algoritmo

El *algoritmo de Newton* implementado es el siguiente:

```r
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
```

El programa arroja que las dos raíces se encuentran en `t1 = 0.5872`, `t2 = 0.3284*10^1`. Entonces el mínimo de `d(t)` se encuentran en una de estas raíces o en los extremos del intervalo trabajado. De este modo: 

```
d(t1) =  0.3111
d(t2) =  17.14
d(0) =  1
d(2π) =  1
```

Así que la gráfica `R(t)` se acerca mas al punto `P` cuando `t = 0.5872`.

## Ilustración

A continuación, se muestra la gráfica que muestra los pasos y convergencia del *algoritmo de Newton* sobre `d'(t)` con un valor inicial de `1`. Los números en rojo sobre la gráfica indican el número de iteración.

![d'(t)](d'%28t%29_converge.png)

Como se puede ver el algoritmo solo necesita de 3 iteraciones para llegar al resultado esperado


