# <a name="head"></a>Problema 2 
Se necesita un recipiente rectangular, sin tapa, de un litro de capacidad. Para construirlo se debe usar una lamina rectangular
de 32 cm de largo y 24 cm de ancho. El procedimiento sera cortar las cuatro esquinas y doblar los bordes de la lámina para 
formar un recipiente.

## Utilice dos metodos.

1. ¿Cual etapa del proceso de resolucíon de un problema numérico requiere más atención?

2. ¿Qué conocimientos son necesarios para formular un modelo matemático?

3. En el ejemplo de la caja. ¿Cual seria la desventaja de intentar obtener experimentalmente la solucion mediante prueba y
error en lugar de analizar el modelo matemático?

4. ¿Que es mas crítico: el error de truncamiento o el error de redondeo?

5. ¿Cual es la ventaja de instrumentar computacionalmente un metodo numérico?

6. ¿Por que es importante validar los resultados obtenidos?

## Solucion

El primer metodo fue realizado en python utilizando la libreria sympy, esto con el fin de poder realizar un metodo que
hiciera uso de variables como la x de una manera mas natural, igualmente la solucion fue obtenida usando la multiplicacion
simplificada de de la funcion que nos fue pedida.

Expresada de la siguiente manera: 

```python
    from sympy import*

    x=Symbol('x')

    f=250-192*x+28*x**2-x**3

```

Luego de usar esta funcion f, dicha funcion fue resuelta evaluando la raiz en 3 espacios, brindadonos así 3 posibles 
respuestas las cuales fueron las siguientes respectivamente:

```
    1.6963
    
    8.0932
    
    18.211

```

Con estos datos se definieron las posibilidades reales siendo estas la primera de 1.6963 y la de  8.0932 puesto que 
la ultima al ser tan grande sobrepasaria el tamaño de uno de los lados.


El segundo metodo utilizado fue en c++ para este metodo se decidio multiplicar la funcion para dejarla en terminos de 
ax^3+bx^2+cx, esto con el fin de poder derivar dicha funcion y hacer asi uso de la ecuacion cuadratica, para obtener
2 resultados de los cuales uno fue descartado debido a que igual que con el metodo en python este superaba el
tamaño de los lados.

La solucion fue obtenida por las siguientes impresiones:

```c++
    cout<<(28+sqrt(208))/(3);
   
    cout<<(28-sqrt(208))/(3);

```

Con estas soluciones se obtuvo los siguientes resultados:


```
    4.53
    
    14.14

```
Como fue mencionado anteriormente el resultado de 14.14 fue descartado puesto que supera los limites de la caja.


## Analisis 

1. Luego de haber resuelto el problema por dos metodos diferentes, es posible decir que la etapa que requiere mayor
atencion es el analisis necesario que se le debe brindar a un problema, esto debido a que al analizar mal o no
analizar se vuelve relativamente imposible el poder solucionar uno de los problemas planteados en este taller.

2. Para formular un modelo matemático es necesario saber las leyes de matemica en general, desde polinomios hasta
funciones avanzadas, ademas de esto es necesario tener un pensamiento logico para ver los ejercicios mas alla
de resolver matematicamente las respuestas.

3. En el ejemplo de la caja el intentar usar prueba y error nos haria perder multiples cosas, inicialmente
materiales puesto que hablamos de cortar y armar cajas, el hacer prueba y error significa que despues de una 
prueba es necesario crear otra caja y gastar cada vez mas material hasta encontrar lo deseado, si se realiza
un modelo matematico es posible identificar la solucion en un solo intento, para que al efectuarlo sobre el 
objeto real en el primer intento quede perfecto.

4.

5. Instrumentar computacionalmente tiene como ventaja, que nos acerca mas al ambito real en el cual siempre,
o la mayoria de las veces disponemos de tecnologia a nuestro alcance para obtener las respuestas, ademas
el instrumentar computacionalmente nos da la ventaja de evitar partes del desarrollo de ejercicios que 
tienden a ser demasiado complicadas y tienden a tomar mayor tiempo del deseado.

6. Es importante validar los datos puesto que esto nos permite saber si no existen otras respuestas
con un indice menor de error, a las actualmente obtenidas.
