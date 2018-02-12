# <a name="head"></a>Problema 2 
Se necesita un recipiente rectangular, sin tapa, de un litro de capacidad. Para construirlo se debe usar una lamina rectangular
de 32 cm de largo y 24 cm de ancho. El procedimiento sera cortar las cuatro esquinas y doblar los bordes de la lámina para 
formar un recipiente.

## Utilice dos metodos.

1. ¿Cuál etapa del proceso de resolucíon de un problema numérico requiere más atención?

2. ¿Qué conocimientos son necesarios para formular un modelo matemático?

3. En el ejemplo de la caja. ¿Cuál seria la desventaja de intentar obtener experimentalmente la solución mediante prueba y
error en lugar de analizar el modelo matemático?

4. ¿Qué es más crítico: el error de truncamiento o el error de redondeo?

5. ¿Cuál es la ventaja de instrumentar computacionalmente un metodo numérico?

6. ¿Por qué es importante validar los resultados obtenidos?

## Solución

El primer método fue realizado en python utilizando la librería sympy, esto con el fin de poder realizar un método que
hiciera uso de variables como la x de una manera más natural, igualmente la solución fue obtenida usando la multiplicación
simplificada de la función que nos fue pedida.

Expresada de la siguiente manera: 

```python
    from sympy import*

    x=Symbol('x')

    f=250-192*x+28*x**2-x**3

```

Luego de usar esta función f, dicha función fue resuelta evaluando la raíz en 3 espacios, brindándonos así 3 posibles 
respuestas las cuales fueron las siguientes respectivamente:

```
    1.6963
    
    8.0932
    
    18.211

```

Con estos datos se definieron las posibilidades reales siendo estas la primera de 1.6963 y la de  8.0932 puesto que 
la última al ser tan grande sobrepasaría el tamaño de uno de los lados.


El segundo método utilizado fue en c++ para este método se decidió multiplicar la función para dejarla en términos de 
ax^3+bx^2+cx, esto con el fin de poder derivar dicha función y hacer así uso de la ecuación cuadrática, para obtener
2 resultados de los cuales uno fue descartado debido a que igual que con el método en python este superaba el
tamaño de los lados.

La solución fue obtenida por las siguientes impresiones:

```c++
    cout<<(28+sqrt(208))/(3);
   
    cout<<(28-sqrt(208))/(3);

```

Con estas soluciones se obtuvo los siguientes resultados:


```
    4.53
    
    14.14

```
Como fue mencionado anteriormente el resultado de 14.14 fue descartado puesto que supera los límites de la caja.


## Análisis 

1. Luego de haber resuelto el problema por dos métodos diferentes, es posible decir que la etapa que requiere mayor
atención es el análisis necesario que se le debe brindar a un problema, esto debido a que al analizar mal o no
analizar se vuelve relativamente imposible el poder solucionar uno de los problemas planteados en este taller.

2. Para formular un modelo matemático es necesario saber las leyes de matemática en general, desde polinomios hasta
funciones avanzadas, además de esto es necesario tener un pensamiento lógico para ver los ejercicios mas allá
de resolver matemáticamente las respuestas.

3. En el ejemplo de la caja el intentar usar prueba y error nos haría perder múltiples cosas, inicialmente
materiales puesto que hablamos de cortar y armar cajas, el hacer prueba y error significa que después de una 
prueba es necesario crear otra caja y gastar cada vez más material hasta encontrar lo deseado, si se realiza
un modelo matemático es posible identificar la solución en un solo intento, para que al efectuarlo sobre el 
objeto real en el primer intento quede perfecto.

4.

5. Instrumentar computacionalmente tiene como ventaja, que nos acerca más al ámbito real en el cual siempre,
o la mayoría de las veces disponemos de tecnología a nuestro alcance para obtener las respuestas, además
el instrumentar computacionalmente nos da la ventaja de evitar partes del desarrollo de ejercicios que 
tienden a ser demasiado complicadas y tienden a tomar mayor tiempo del deseado.

6. Es importante validar los datos puesto que esto nos permite saber si no existen otras respuestas
con un índice menor de error, a las actualmente obtenidas.
