from operation_counter import *
from horner import *

def eval_poly(poly,x):
	n = len(poly) - 1
	ans = poly[0]*x**n
	for a in poly[1:]:
		n -= 1
		ans = ans + a*x**n
	return ans

OperationCounter.init()
poly_1 = [OperationCounter.number(i) for i in [2,0,-3,3,-4]]
xo_1 = OperationCounter.number(-2)

print "2x^4 - 3x^2 + 3x - 4 = {0}".format(horner(poly_1,xo_1))
print "# de operaciones: {0}".format(OperationCounter.count)
print eval_poly(poly_1,xo_1)

OperationCounter.init()
poly_2 = [OperationCounter.number(i) for i in [7,6,-6,0,3,-4]]
xo_2 = OperationCounter.number(3)

print "7x^5 + 6x^4 - 6x^3 + 3x - 4 = {0}".format(horner(poly_2,xo_2))
print "# de operaciones: {0}".format(OperationCounter.count)
print