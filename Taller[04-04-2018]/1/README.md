# Construya un polinomio P(x) de grado 3 usando los siguientes puntos, (0,10), (1,15), (2,5) con tangente 1 en x=0, use dos metodos diferentes y responda cual es el mas optimo (diga cual es el criterio para ser mas optimo)

## Metodo 1: Lagrange.

Usando el metodo de lagrange, rapidamente se noto como no seria posible realizar la construccion del polinomio, esto debido a que lagrange obtiene solo los datos de los vectores X y Y  realizando asi las operaciones internamente, de esta manera usandolo de manera base lo maximo que se logro obtener fue un polinomio de grado 2 puesto que no hubo forma de integrar el punto de la derivada de la funcion f'(0)=1, aunque de haber logrado implementar dicha derivada se pudo notar algo en la forma en la que se resuelve este metodo, esto en comparacion al metodo 2 utilizado.



Como visto en el codigo anterior se nota como para realizar las operaciones internas se pasa por un for() anidado, este viendose directamente afectado por el tamaño de nuestro vector de variables x, significando que a razon de mayor cantidad de datos en el vector, cada vez sera mas y mas demorado la resolucion del problema, igualmente notamos como obteniendo el polinomio de grado 2 ya muestra signos de demora al ofrecernos la respuesta.

## Metodos 2: Hermite.


## Metodo mas optimo.

Segun todo lo dicho anteriormente, entre los metodos, se puede decir que el metodo de Hermite es mucho mas optimo, puesto que aunque no se haya logrado solucionar con Lagrange el problema, notamos como un polinomio de grado 2 resulta ser mas demorado en ser definido contra el metodo de Hermite que como fue mencionado nos obtuvo un polinomio de grado 5, esto se noto debido a que el metodo de lagrange hace uso de for() anidados, en cambio hermite tiene 4 for() que no se relacionan entre ellos permitiendolos moverse en secuencia rapidamente.

Por lo tanto se puede afirmar que el metodo de Hermite es el ganador entre estos dos. 
