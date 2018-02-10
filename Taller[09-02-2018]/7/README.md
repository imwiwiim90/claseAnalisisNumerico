# Método de Newton

Utilize el método de Newton para resolver el problema, muestre gráficamente como se comporta la convergencia a la solución:

Una particula se mueve en el espacio con el vector de posición `R(t)  = ( 2cos(t),sen(t),O )`. Se requiere conocer el tiempo en el que el objeto se encuentra más cerca del punto `P(2,1,O)`. Utilice el método de Newton con cuatro decimales de precisión.

## Entradas

El algoritmo de Newton encuentra las raices de una función `f(x)` si dentro de un intervalo [a,b], esta es continua en segundo grado, la derivada no es igual a `0` y el valor inicial de entrada es cercano a la respuesta.

Se debe transformar el problema inicial a un equivalente problema de raíz, de este modo se sabe que la distancia entre dos puntos `(x1,y1,z1)` y `(x2,y2,z2)` es `[(x1 - x2)^2 + (y1 - y2)^2 + (z1 - z2)^2]^(1/2)`, de modo que la distancia de el punto `P` y la función `R(t)` esta determinada por `[ (2cos(t) - 2)^2 + (sen(t) - 1)^2 ]^(1/2)`, sin embargo por facilidad y una función equivalente tal que tiene la misma respuesta está dada por:

```
d(t) = (2cos(t) - 2)^2 + (sen(t) - 1)^2
```

Dado que es una funcion periódica con periodo `2π` basta con evaluar la función en el intervalo [0,2π].

El mínimo de la función `d(t)` según el *Teorema de los valores extremos* está en `0`,`2π` o cuando `d'(t) = 0`. Es aquí donde se aplica el *algoritmo de Newton* para encontrar `t` tal que `d'(t) = 0`.

Se utiliza `R` para calcular la derivada de la función `d(t)`  en [sol.R](sol.R) teniendo:

```
2 * (cos(t) * (sin(t) - 1)) - 2 * (2 * sin(t) * (2 * cos(t) - 2))
```

Esta a simple vista se sabe que es continua, si embargo su derivada puede tomar valores en `0` como se puede ver a continuación:
![d'(t)](d'%28t%29.png)
## Algoritmo

