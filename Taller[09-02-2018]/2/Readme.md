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

    plot(f,(x,0,20))

    r=solve(f)

    r[0].evalf(5)

    r[2].evalf(5)

    r[2].evalf(5)
```



## Analisis 
