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

## Resultados esperados
