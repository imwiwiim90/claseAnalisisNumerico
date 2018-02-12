Se propone resolver la ecuación integral entre 0 y x de: (5-e^u)du = 2 con el
# Método del punto fijo.

a.) Mediante un gráfico aproximado, o evaluando directamente, localice las raíces
reales.

b.) Mediante un gráfico aproximado, evaluando directamente, localice las raíces 
reales.

c.) Proponga una ecuación equivalente x= g(x) y determine el intervalo de
convergencia para calcular una de las dos raíces.

d.) Del intervalo anterior, elija un valor inicial y realice 5 iteraciones. En
cada iteración verifique que se cumpla la condición de convergencial del punto fijo
y estime el error de truncamiento en el último resultado.

## Análisis 


a.) Luego de resolver la integral se obtiene que f(x) = 5x + e^x - 1, con este 
valor es posible trabajar en los puntos siguientes.

b.) Usando la función f(x) obtenida previamente se optó por graficar para 
obtener las raíces reales de la función, la gráfica obtenida fue la siguiente:

![d_t](d_t.png)

Esta grafica fue obtenida utilizando R en el archivo graph.R.

Luego de analizar la gráfica, es posible decir que las raíces reales se encuentran en
aproximadamente 2,66 y 0.

c.) Para obtener el intervalo y las respectivas iteraciones fue utilizado el método
del punto fijo expresado de la siguiente manera:

```
from math import *
def g(x):

    y=5*x+e^x-1

    return y

p0=0

tol=0.001

n0=5

i=1

while i<=n0:

    p=g(p0)

    if abs(p-p0)<tol:

        print("El punto fijo es ",p," despues de ",i," iteraciones")

        break

    i=i+1

    p0=p

if i>n0:

    
    print("El metodo no converge ")
    
```

Con este intervalo con la ecuación correcta en y=(ecuación) obtendríamos el valor del 
punto fijo después de una cantidad n de iteraciones.
