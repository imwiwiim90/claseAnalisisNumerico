import matplotlib.pyplot as plt
import numpy as np
import sympy

sympy.init_printing(use_latex='mathjax')

x = sympy.Symbol('x')
y = sympy.Function('y')

f = 1 - x**2 + x + y(x)

general_sol = sympy.dsolve(y(x).diff(x) - f)
ics_eq = general_sol.subs([(x,0),(y(0),1)])
ode_sol = general_sol.subs([(ics_eq.rhs,ics_eq.lhs)])

print ode_sol