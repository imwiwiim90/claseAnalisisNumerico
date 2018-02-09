class OperationCounterNumber:
	def __init__(self,n):
		self.n = n

	def __str__(self):
		return str(self.n)

	def __add__(self,b):
		OperationCounter.inc_count()
		return OperationCounterNumber(self.n + b.n)

	def __sub__(self,b):
		OperationCounter.inc_count()
		return OperationCounterNumber(self.n - b.n)

	def __mul__(self,b):
		OperationCounter.inc_count()
		return OperationCounterNumber(self.n * b.n)

	def __div__(self,b):
		OperationCounter.inc_count()
		return OperationCounterNumber(self.n / b.n)
		
	def __pow__(self,b):
		if (isinstance(b, OperationCounterNumber)):
			b = b.n
		if (b > 1):
			OperationCounter.inc_count(b-1)
		return OperationCounterNumber(self.n ** b)


class OperationCounter:
	count = 0

	@staticmethod
	def init():
		OperationCounter.count = 0

	@staticmethod
	def number(n):
		return OperationCounterNumber(n)

	@staticmethod
	def inc_count(n = 1):
		OperationCounter.count += n

