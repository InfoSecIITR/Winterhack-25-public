# https://en.wikipedia.org/wiki/Gaussian_integer
class GaussianInteger:
	def __init__(self, a=0, b=0):
		self.r = int(a)
		self.i = int(b)

	def __repr__(self):
		return '(' + str(self.r) + ((' + ' + str(self.i) if self.i >= 0 else ' - ' + str(-self.i))) + 'j)'

	def __eq__(self, other):
		return self.r == other.r and self.i == other.i

	def conjugate(self):
		return GaussianInteger(self.r, -self.i)

	def norm(self):
		return self.r * self.r + self.i * self.i

	def add(self, other):
		sum_r = self.r + other.r
		sum_i = self.i + other.i
		return GaussianInteger(sum_r, sum_i)

	def __add__(self, other):
		if type(other) is int:
			return GaussianInteger(self.r + other, self.i)
		else:
			return self.add(other)

	def __radd__(self, other):
		if type(other) is int:
			return GaussianInteger(self.r + other, self.i)
		else:
			return self.add(other)

	def __iadd__(self, other):
		self = self + other
		return self

	def __neg__(self):
		return GaussianInteger(-self.r, -self.i)

	def __sub__(self, other):
		return self.__add__(-other)

	def __rsub__(self, other):
		if type(other) is int:
			return GaussianInteger(other - self.r, -self.i)
		else:
			return other - self

	def __isub__(self, other):
		self = self - other
		return self

	def mult(self, other):
		prod_r = self.r * other.r - self.i * other.i
		prod_i = self.i * other.r + self.r * other.i
		return GaussianInteger(prod_r, prod_i)

	def __mul__(self, other):
		if type(other) is int:
			return GaussianInteger(self.r * other, self.i * other)
		else:
			return self.mult(other)

	def __rmul__(self, other):
		if type(other) is int:
			return GaussianInteger(self.r * other, self.i * other)
		else:
			return self.mult(other)

	def __imul__(self, other):
		self = self * other
		return self

	def floordiv(self, divisor):
		if type(divisor) is int:
			numerator = (-self if divisor < 0 else self)
			denominator = (-divisor if divisor < 0 else divisor)
			if denominator == 0:
				raise ZeroDivisionError('{0:s} is null!'.format(divisor))
		else:
			numerator = self * divisor.conjugate()
			denominator = divisor.norm()
			if denominator == 0:
				raise ZeroDivisionError('{0:s} is null!'.format(divisor))
		candidate_r = numerator.r // denominator
		candidate_i = numerator.i // denominator
		if (2 * candidate_r + 1) * denominator < 2 * numerator.r:
			candidate_r += 1
		if (2 * candidate_i + 1) * denominator < 2 * numerator.i:
			candidate_i += 1

		return GaussianInteger(candidate_r, candidate_i)

	def __floordiv__(self, divisor):
		return self.floordiv(divisor)

	def __ifloordiv__(self, divisor):
		self = self // divisor
		return self

	def mod(self, divisor):
		return self - divisor * (self // divisor)

	def __mod__(self, divisor):
		return self.mod(divisor)

	def __imod__(self, divisor):
		self = self % divisor
		return self

	def divmod(self, divisor):
		q = self // divisor
		return (q, self - divisor * q)

	@staticmethod
	def gcd(a, b):
		if a.norm() < b.norm():
			return GaussianInteger.gcd(b, a)
		while b.norm() > 0:
			(q, r) = a.divmod(b)
			(a, b) = (b, r)
		return a

	def __pow__(self, e, m=0):
		result = GaussianInteger(1)
		a = GaussianInteger(self.r, self.i)
		while e:
			if e & 1:
				if m:
					result = result * a % m
				else:
					result = result * a
			e >>= 1
			if m:
				a = a * a % m
			else:
				a = a * a
		return result
	
	@staticmethod
	def sqrt(a):
		def isqrt(n):
			x = n
			y = (x + 1) // 2
			while y < x:
				x = y
				y = (x + n // x) // 2
			return x
		x, y = a.r, a.i
		l = isqrt(a.norm())
		u = isqrt((l + x) // 2)
		v = isqrt((l - x) // 2)

		if y < 0:
			v = -v
		return GaussianInteger(u, v)