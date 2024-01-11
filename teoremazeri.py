class Intervallo:
	def __init__(self, a, b, f, epsilon):
		self.a=a
		self.b=b
		self.f=f
		self.epsilon=epsilon

	def __iter__(self):
		return TrovaZeri(self.a, self.b, self.f, self.epsilon)

class TrovaZeri:
	def __init__(self, a, b, f, e):
		self.a = a
		self.b = b
		self.f = f
		self.c = (a+b)/2
		self.e = e

	def __next__(self):
		if self.f(self.c) == 0 or (self.f(self.c)<self.e and self.f(self.c) > -1*self.e):
			raise StopIteration

		if self.f(self.c) > 0:
			self.a = self.a
			self.b = self.c
			self.c = (self.a+self.b)/2
			return self.b

		if self.f(self.c) < 0:
			self.a = self.c
			self.b = self.b
			self.c = (self.a+self.b)/2
			return self.a
