# <a name="head"></a>Método Horner

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
<a name="npoly"></a>Si se tiene en cuenta los coeficientes de los monomios las operaciones requeridas serán:
```
(n^2 + 3n)/2
```

El algoritmo de Horner solo requiere `n` sumas y `n` productos, por lo que se requieren `2n` operaciones

## Código

A continuación describimos las clases y algoritmos implementados para la resolución del problema:

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

Para realizar el conteo de operaciones sin necesidad de llamar a la clase cada vez que se realize una operación, `OperationCounter.number(n)` devuelve una clase con el comportamiento de una variable numérica, la cual cada vez que se realize una operación aritmetica sobre esta, incrementará el contador

### Algoritmo Horner

La implementación del algoritmo Horner `horner(poly,x)`, así como el algoritmo Horner que evalua un punto sobre la derivada del polinomio `horner_diff(poly,x)` es la siguiente: 

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

### Método directo

La implementación del método directo `eval_poly(poly,x)`, así como el método directo sobre la derivada del polinomio `eval_poly_diff(poly,x)` es la siguiente: 

```python
def eval_poly(poly,x):
	n = len(poly) - 1
	ans = poly[0]*x**n
	for a in poly[1:-1]:
		n -= 1
		ans = ans + a*x**n
	ans = ans + poly[-1]
	return ans

def eval_poly_diff(poly,x):
	diff_poly = []
	n = len(poly) - 1
	for a in poly[:-1]:
		diff_poly.push(a*n)
	return eval_poly(diff_poly,x)
```

## Resultados

A continuación se muestran los resultados de los diferentes algoritmos sobre los polinomios presentados al [comienzo](#head). Debe tenerse en cuenta que al evaluar el número de operaciones de un polinomio se calcula como si el polinomio estubiera **completo**. Es decir `x^2` no realiza 1 operación si no que se calcula como `1*x^2 + 1*x + 0` y utilizando ésta [ecuación](#npoly) el número de operaciones será `(2ˆ2 + 3*2)/2 = 5`. Para comprobar los resultados correr [sol.py](https://github.com/imwiwiim90/claseAnalisisNumerico/blob/master/Taller%5B09-02-2018%5D/1/sol.py)

Polinomio | x | Resultado | No. Operaciones (Directo) | No. Operaciones (Horner)
------------ | ------------- | ------------- | ------------- | ------------- 
2x^4 - 3x^2 + 3x - 4        | -2 | 10  | 15 | 8 |
7x^5 + 6x^4 - 6x^3 + 3x - 4 |  3 | 2030| 21 | 10|
-5x^6 + 3x^4 + 2x^2 - 4x    | -1 | 4   | 28 | 12|
2x^4 - 3x^2 + 3x - 4 (derivada)        | -2 | -49 | 13 | 12|
7x^5 + 6x^4 - 6x^3 + 3x - 4 (derivada) |  3 | 3324| 19 | 16|
-5x^6 + 3x^4 + 2x^2 - 4x (derivada)    | -1 | 10  | 26 | 20|


