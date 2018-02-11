# Método de Newton vs Secante

Resolver por dos métodos diferentes, grafique las soluciones y comparar sus soluciones.

Encuentre una intersección de las siguientes ecuaciones en coordenadas polares:

```
r = 2 + cos(3*t)
r = 2 - e^t
```

## Análisis

Graficaremos las ecuaciones para tener una idea de con lo que se está trabajando:


Si se quiere hallar la itersección de ambas gráficas la imagen debe ser la misma para un `t` dado, dicho de otra manera, ambas ecuaciones se igualan y se debe cumplir que:

```
cos(3*t) + e^t = 0
```

De este modo es un problema de raíces, así que con `f(x) = cos(3*t) + e^t` podemos aplicar los algoritmos de *Newton* y el algoritmo de *secante* para hallar `t` para que la imagen sea `0`.