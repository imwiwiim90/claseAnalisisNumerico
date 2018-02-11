
def nroot(k,n,E,a=0,b=None):
	b = (k if b == None else b)
	y = (a + b)/2
	if abs(y**n - k) > E:
		if y**n > k:
			b = y
		else:
			a = y
		return nroot(k,n,E,a=a,b=b)
	return y


print nroot(4.0,2.0,1e-5)
print nroot(8.0,3.0,1e-5)
print nroot(16.0,4.0,1e-5)
print nroot(32.0,5.0,1e-5)
print nroot(27.0,3.0,1e-5)
print nroot(1000.0,3.0,1e-5)
print nroot(50.0,4.0,1e-5)