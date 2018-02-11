# Algoritmo para encontrar raíces

El siguiente es un procedimiento intuitivo para calcular una raíz positiva de la ecuación `f(x) = 0` en un intervalo `[a,b]` con presición `E`.

A partir de `x = a` evalúe `f(x)` incrementando `x` en un valor `d`. inicialmente `d = (b - a)/10` Cuando `f` cambie de signo, retroceda x al punto anterior `x - d`, reduzca `d` al valor `d/10` y evalúe nuevamente `f` hasta que cambie de signo Repita este procedimiento hasta que `d` sea menor que E. 

1. De manera formal escriba las condiciones necesarias para que la raiz exista, sea única y pueda ser calculada 
2. Indique el orden de convergencia y estime el factor de convergencia del método. 
3. Describa el procedimiento anterior en notación algoritmica, o en MAMAD o en Python 

## Válidez

Para comprobar que el algoritmo sea válido, se parte de que `f(x)` esta definida y es continua en el intervalo `[a,b]`. Además que `f(a)*f(b) < 0`, esto significa según el valor intermedio que existe un `c` tal que `f(c) = 0` y por lo tanto la raíz *existe*.

El n-ésimo intervalo `[a_n,b_n]` se asegura que es menor al anterior por un factor de `10` ya que `d` en la n-ésima iteración es `d_n = d_(n-1)/(10^n)` lo que significa que el intervalo es más pequeño en cada iteración. Y al asegurar que el intervalo contiene signos opuestos es decir `f(a_n)*f(b_n) < 0` se asegura que siempre el intervalo contendrá a la raíz, y al ser cada vez mas pequeño convergerá a esta y por lo tanto *puede ser calculada*.

Si se quiere asegurar que la raíz dentro del intervalo `[a,b]` sea única, se debe satisfacer que `f'(x)` en este intervalo seá diferente de `0`, además de estar definida y ser continua. Ya que si nunca toma el valor de `0` dentro del intervalo `f(x) < 0` ó `f(x) > 0`, por lo tanto siempre será decreciente o creciente. Y por lo tanto la intersección con `y = 0` sólo ocurrirá una sola vez. Así aseguramos que la raíz sea *única* dentro del intervalo `[a,b]`.

## Convergencia

Sea `y` la raíz que se quiere encontrar y `y_n` la aproximación. Se sabe que el intervalo en la n-ésima iteración tiene la siguiente relación:

```
b_n - a_n = (b - a)/10^n 
```

Si se sabe que `y_n = (a_n-b_n)/10` se tiene que:

```
| y_n - y | <= 1/10(b_n - a_n) = (b - a)/10^n
```

Por lo tanto el factor de convergencia es `O(1/10ˆn)`.

## Código

A continuación se muestra una implementación en python:

```python
def root_10section(f,a,b,E):
	d = (b - a)/10.0
	x = a
	sgn = f(x)
	while abs(f(x)) > E:
		while f(x)*sgn > 0:
			x += d
		x -= d
		d = d/10.0
	return x
```

Probando con algunos datos de entrada como se muestra en [sol.py](sol.py) se tubieron los siguientes resultados, redondeando el resultado a 3 decimales:

f 		|a 		|b 		|E 	 	|Resultado 	
------- | ----- | ----- | ----- | ---- 
x^3     | -1 	| 1 	| 10^-3 | 0 	 
cos(x)  | 0 	| 2π 	| 10^-3 | 1.571 	 
1 - x   | -1 	| 5 	| 10^-3 | 1 	 
