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

## Desarrollo

A continuación describimos las clases y algoritmos implementados para la resolución del problema

### Contador de operaciones

Para el conteo de operaciones se utiliza una clase estatica que lleve el conteo de operaciones realizadas

```
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

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```