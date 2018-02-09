from operation_counter import *
from horner import *

def eval_poly(poly,x):
	n = len(poly) - 1
	ans = poly[0]*x**n
	for a in poly[1:-1]:
		n -= 1
		ans = ans + a*x**n
	ans = ans + poly[-1]
	return ans



poly_1 = [OperationCounter.number(i) for i in [2,0,-3,3,-4]]
xo_1 = OperationCounter.number(-2)

poly_2 = [OperationCounter.number(i) for i in [7,6,-6,0,3,-4]]
xo_2 = OperationCounter.number(3)

poly_3 = [OperationCounter.number(i) for i in [-5,0,3,0,2,-4,0]]
xo_3 = OperationCounter.number(-1)

print "Directa"
OperationCounter.init()
print "x = -2 \n2x^4 - 3x^2 + 3x - 4 = {0}".format(eval_poly(poly_1,xo_1))
print "# de operaciones: {0}".format(OperationCounter.count)
print
OperationCounter.init()
print "x = 3\n7x^5 + 6x^4 - 6x^3 + 3x - 4 = {0}".format(eval_poly(poly_2,xo_2))
print "# de operaciones: {0}".format(OperationCounter.count)
print
OperationCounter.init()
print "x= -1\n-5x^6 + 3x^4 + 2x^2 - 4x = {0}".format(eval_poly(poly_3,xo_3))
print "# de operaciones: {0}".format(OperationCounter.count)
print

print "Horner"
OperationCounter.init()
print "x = -2 \n2x^4 - 3x^2 + 3x - 4 = {0}".format(horner(poly_1,xo_1))
print "# de operaciones: {0}".format(OperationCounter.count)
print
OperationCounter.init()
print "x = 3\n7x^5 + 6x^4 - 6x^3 + 3x - 4 = {0}".format(horner(poly_2,xo_2))
print "# de operaciones: {0}".format(OperationCounter.count)
print
OperationCounter.init()
print "x= -1\n-5x^6 + 3x^4 + 2x^2 - 4x = {0}".format(horner(poly_3,xo_3))
print "# de operaciones: {0}".format(OperationCounter.count)
print