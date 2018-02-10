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

al evaluar la raíz cuadrada de 7, con un error de **10e-4** y un valor inicial de 1.5 `root(4,1.e-4,1.5)` se tiene que el resultado es `2.645751`