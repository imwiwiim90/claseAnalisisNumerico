# Método Horner

Evaluar el polinomio en cada valor indicado y el número de operaciones mínimo para hacerlo, para los siguientes polinomios junto con sus derivadas:

```
x = -2
P(x) = 2x^4 - 3x^2 + 3x - 4

x = 3
P(X) = 7x^5 + 6x^4 - 6x^3 + 3x - 4

x = -1
P(X) = -5x^6 + 3x^4 + 2x^2 - 4x
```

## Resultados esperados

El número de operaciones requeridas para la evaluación de un monomio de grado n de manera directa es:
```
(n^2 + n)/2
```
Si se tiene en cuenta los coeficientes de los monomios las operaciones requeridas serán:
```
(n^2 + 3n)/2
```

El algoritmo de Horner solo requiere `n` sumas y `n` productos, por lo que se requieran `2n` operaciones
## Código

A continuación describimos las clases y algoritmos implementados para la resolución del problema

### Contador de operaciones

Para el conteo de operaciones se utiliza una clase con métodos estaticos que lleve el conteo de operaciones realizadas

```python
class OperationCounter:
	count = 0

	@staticmethod
	def init():
		OperationCounter.count = 0

	@staticmethod
	def number(n):
		return OperationCounterNumber(n)

	@staticmethod
	def inc_count(n = 1):
		OperationCounter.count += n
```

El contador debe inicializarse para dar inicio al conteo de operaciones `OperationCounter.init()`. Cada vez que se realize una operación se debe llamar al incrementador del contador `OperationCounter.inc_count()`. 

Para realizar el conteo de operaciones sin necesidad de llamar a la clase cada vez que se realize una operación, `OperationCounter.number(n)` devuelve una clase con el comportamiento de una variable numérica, la cual cada vez que se realize una operacion aritmetica sobre esta, incrementará el contador

### Algoritmo Horner

La implementacion del algoritmo horner `horner(poly,x)`, asi como el algoritmo horner que evalua un punto sobre la derivada del polinomio `horner_diff(poly,x)` es la siguiente: 

```python
def horner(poly,x): 
	b = poly[0]
	for a in poly[1:]:
		b = a + b*x
	return b

def horner_diff(poly,x):
	b = poly[0]
	Q = []
	for a in poly[1:-1]:
		b = a + b*x
		Q.append(b)
	return horner(Q,x)
```