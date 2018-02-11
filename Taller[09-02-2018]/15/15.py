//Metodo Punto Fijo

from math import *
def g(x):

    y=0.5*sqrt(10-x**3)

    return y

p0=0

tol=0.001

n0=50

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
