# Raíz n-ésima

Encuentre una fórmula iterativa de convergencia cuadrática y defina un intervalo de convergencia apropiado para calcular la raíz n-énesima de un número real. El algoritmo sólamente debe incluir operaciones aritmétricas elementales.

## Algoritmo

Sea `k` el número real el cual se quiere hallar su raíz, `n` al orden de la raíz. Se quiere halla un número `y` tal que `y = k^(1/n)`.

El algoritmo propuesto como solución es una variación del algoritmo *bisección*. 

Sea `f(x) = x^n`. Supongase que se tiene un intervalo inicial [a,b] en donde `y^n` pertenece a `[f(a),f(b)]`. Y sabiendo que `f(x)` es continua, según el *teorema del valor intermedio* existe un `x` entre `[a,b]` tal que `x = y`.

La idea es acotar el intervalo de trabajo `[a,b]` por un nuevo `[a_n,b_n]` tal que ese nuevo intervalo contenga a `y` tal que `y^n = k`, siendo `y_n` la respuesta en la n-ésima iteración como `y_n = (a_n + b_n)/2`, es decir la respuesta n-ésima es el valor medio del n-ésimo intervalo, el n-ésimo intervalo viene dado de la siguiente manera:

- Sí `(y_n)^n` es igual `k` entonces `y = y_n`. Y esa es la respuesta.
- Sí `(y_n)^n` es mayor a `k` entonces `b_(n+1) = y_n`
- Sí `(y_n)^n` es menor a `k` entonces `a_(n+1) = y_n`

Y de esta forma nos aseguramos que el intervalo `[a_n,b_n]` siempre contenga la respuesta.

Como intervalo inicial se propone el intervalo `[0,k]` ya que la raíz estará dentro de este intervalo.

## Convergencia

Para hallar la razón de convergencia. Sea la serie `{y_n}` que converge a un numero `y`, y para una serie `{B_n}` que se sabe que converge a `0`, la serie `{y_n}` converge a `y` con una razón de `O(B_n)` es verdad si:

```
| y_n - y | <= | K*B_n | , para un n grande.
```

Para nuestro caso `| y_n - y |` el cual es equivalente a `|(a_n + b_n)/2 - y|` y este a su vez es menor que `1/2| ( a_(n-1) + b_(n-1) )/2 - y |`. Iterando se tiene que:

```
| y_n - y | = |(a_n + b_n)/2 - y| < 1/2| ( a_(n-1) + b_(n-1) )/2 - y | < ... < (1/2)^n| ( a_0 + b_0 )/2 - y | < (1/2)^n | (a_0 + b+0)/2 |
```

Si asumimos `B_n = (1/2)^n` entonces:
```
| y_n - y | <= K | B_n |
```
para un `K` suficientemente grande. Se puede decir que el algoritmo tiene una **razón de convergencia cuadrática**.

## Código

A continuacíon se muestra la implementación del algoritmo en python:

```python
def nroot(k,n,E,a=0,b=None):
	b = (k if b == None else b)
	y = (a + b)/2
	if abs(y**n - k) > E:
		if y**n > k:
			b = y
		else:
			a = y
		return nroot(k,n,E,a=a,b=b)
	return y
```

En este algoritmo `k` hace referencia al número real el cual se quiere hallar su raíz, `n` hace referencia al orden de la raíz. `E` es el error permitido tal que si `y = k^(1/n)` entonces `| y^n - k |  < E`. Y `a` y `b` pueden entenderse como el intervalo n-ésimo de la iteración.

A continuación se muestra una tabla con algunos datos de entrada de prueba, con redondeo a 10^-5:

k 	 |		n |		 E |	y
---- | ------ | ------ | ------
4	 | 		2 | 10^-5  |  2
8	 | 		3 | 10^-5  |  2
16   | 		4 | 10^-5  |  2
32	 | 		5 | 10^-5  |  2
27	 | 		3 | 10^-5  |  3
1000 | 		3 | 10^-5  |  10
50	 | 		4 | 10^-5  |  2.65915

