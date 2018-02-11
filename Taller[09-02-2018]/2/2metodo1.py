from sympy import*

x=Symbol('x')

f=250-192*x+28*x**2-x**3

plot(f,(x,0,20))

r=solve(f)

r[0].evalf(5)

r[2].evalf(5)

r[2].evalf(5)

