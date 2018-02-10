### Eficiencia de un algoritmo

Dado el siguiente algoritmo:

```
Leer n
Mientras n > 0 repita
	d <- mod(n,2)
	n <- fix(n/2)
	Mostrar d
Fin
```

1. Recorra el algoritmo con `n = 73`.
2. Suponga que T(n) representa la cantidad de operaciones aritmétricas de división que se realizan para resolver el problema de tamaño `n`. Encuentre `T(n)` y expresela con notación `O()`. Para obtener `T(n)` observe el hecho de que cada ciclo el valor de `n` se reduce aproximadamente a la mitad.

## Desarrollo

1. Al correr el algoritmo con `n = 73` se tiene:

```
1
0
0
1
0
0
1
```

2. Dado que el algoritmo divide recurrentemente `n` en `2` el número requerido de operaciones es `T( n ) = floor(log_2(n))` donde `floor` es el operador de parte entera, dado que `T(n) <= log_2(n)` es equivalente a `O(log(n)`.