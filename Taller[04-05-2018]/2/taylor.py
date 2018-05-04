import matplotlib.pyplot as plt
import math

xi = 0
wi = 1.0
h = 0.1

x = [xi]
y = [wi]
for i in range(20):
	T = (1 - xi**2 + xi + wi) + h/2*(1 - xi**2 + wi) + h/6*(1 - xi - xi**2 + wi)
	wi = wi + h*T
	xi += h
	y.append(wi)
	x.append(xi)

plt.plot(x,y)

x_anal = [xi*0.1 for xi in range(0,21)]
y_anal = [(xi*(xi + 1)*math.exp(-xi) + 1)*math.exp(xi) for xi in x_anal]

plt.plot(x_anal,y_anal)
plt.show()

err = [abs(x_a-xi) for (x_a,xi) in zip(x_anal,x)]
i = 0
for t in zip(x,err):
	if i % 2 == 0:
		print "{0} | {1:.18f} |".format(t[0],t[1])
	i += 1