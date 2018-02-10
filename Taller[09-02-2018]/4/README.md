### Error de redondeo inferior

Suponga que un dispositivo solo puede almacenar únicamente los cuatro primeros digitos decimales de cada número real, y trunca los restantes (redondeo inferior). Calcule el error de redondeo si se quiere almacenar el número `536.78`. Tenga en cuenta lo siguiente:

En general si `n` es la cantidad de enteros del número normalizado con potencias de `10`, y `m` es la cantidad de cifras decimales que se pueden almacenar en el dispositivo, entonces si se truncan los decimales sin ajustar la cifra anterior, el error de redondeo absoluto esta acotado por <a href='maxref'></a>:

```
| E | < 1*10^(n-m)
```
Mientras que el error relativo:
```
| e | < max(|E|)/min(|X|) = 1*10^(n-m)/0.1*10^n = 10*10^-m
```
Solo depende del almacenamiento.

## Desarrollo

Para facilitar el análisis el número en su representación *normalizada de punto decimal flotante* es la siguiente:
```
0.53678 * 10^3
``` 
Al realizar el acotamiento el número será guardado como:
```
0.5367 * 10^3
```
***El error absoluto*** es la diferencia de estos dos valores:
```
| 0.5367 * 10^3 - 0.52678 * 10^3 |  = 0.8*10^-1
``` 
El cual esta acotado por la expresión [anterior](#maxref), sabiendo que `m = 4` y `n = 3` se tiene que  `| E | <  1*10^-1`. En cuanto al ***error relativo***:
```
| 0.5367 * 10^3 - 0.52678 * 10^3 |/| 0.52678 * 10^3 | = 0.15*10^-3
```
Este error claramente es menor al error de maquina `10*10^-4 = 1*10^-3`.