# Error de precisión

Calcule la propagación del error dado por las operaciones aritmétricas, para el siguiente problema:
La velocidad de una particula es constante e igual a `4m/s`, medida con un error de `0.1m/s` durante un tiempo de recorrido de `5s`, medido con un error de `0.1s`. Determine el error absoluto y error relativo en el valor de la distancia recorrida.

## Desarrollo

El **error absoluto** de una multiplicación, sabiendo que `a'` y `b'` son aproximaciones a `a` y `b`, y el error de la medida se denota por `e_a` y `e_b` esta dado por: 

```
| E | = | a'*b' - a*b | = | (a' - a) * ( b' - b)| <= | e_a*e_b | 

| E | <= | 0.1*0.1 | = 0.1*10^-1

```

Para el **error relativo** se tiene que: 

```
| e | = | E |/| a*b | = 0.1*10^-1/( 5 * 4) = 0.5*10^-3
```