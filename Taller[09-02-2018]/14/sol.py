import math


def root_10section(f,a,b,E):
	d = (b - a)/10.0
	x = a
	sgn = f(x)
	while abs(f(x)) > E:
		while f(x)*sgn > 0:
			x += d
		x -= d
		d = d/10.0
	return x


print "x^3"
print root_10section(lambda x: x**3,-1.0,1.0,1e-3)
print

print "cos(x)"
print root_10section(math.cos,0.0,2.0*math.pi,1e-3)
print

print "1 - x"
print root_10section(lambda x: 1-x,-1.0,5.0,1e-3)
print