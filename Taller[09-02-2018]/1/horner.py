

"""
caculates the polynomial at a given x

Args:
        poly (array): array of numbers representing the polynomial
        ex: 2x^2 + 5x + 3 should be [2 5 3]

        x (number): number where the polynomial is being evaluated
Returns:
        the polynomial evaluated at the given value x
"""
def horner(poly,x): 
	b = poly[0]
	for a in poly[1:]:
		b = a + b*x
	return b
