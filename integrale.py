import math

class CalcoloIntegrale:
    def __init__(self, a, b, f, l):
        self.a = a
        self.b = b
        self.f = f 
        self.l = l

    def __iter__(self):
        self.delta = [self.a, self.b]
        self.j = 0
        return self

    def __next__(self):
        # prima calcola l'integrale col delta scelto
        if self.j > self.l:
            raise StopIteration

        S = 0
        for i in range(1, len(self.delta)):
            a_i = self.delta[i]
            a_i1 = self.delta[i-1]
            S += (a_i-a_i1)*(self.f(a_i))

        # calcola nuovo delta e riordina
        for i in range(1, len(self.delta)):
            a_i = self.delta[i]
            a_i1 = self.delta[i-1]
            self.delta.append((a_i+a_i1)*0.5)
        self.delta.sort()
        self.j += 1

        return S

def f(x):
    return math.exp(x)/math.sin(x)

bingo = CalcoloIntegrale(1, 2, f, 25)
for i in bingo:
    print(i)
