class Calcolatrice:
    def escludi_float(self, x):
        try:
            z = float(x)
        except:
            pass
        else:
            if z != int(x):
                raise Exception("Input non accettabile")

    def sanitizza(self, x, tipo):
        try:
            tipo(x)
        except Exception:
            raise Exception("Input non accettabile")
        else:
            return tipo(x)

    # metodi: somma, moltiplica, potenza, converti_base, radice, modulo, sottrazione.
    def somma(self, x, y):
        x = self.sanitizza(x, float)
        y = self.sanitizza(y, float)
        return x+y

    def moltiplica(self, x, y):
        x = self.sanitizza(x, float)
        y = self.sanitizza(y, float)
        return x*y

    def sottrazione(self, x, y):
        x = self.sanitizza(x, float)
        y = self.sanitizza(y, float)
        return x-y

    def potenza(self, x, y):
        self.sanitizza(x, int)
        self.sanitizza(y, int)
        self.escludi_float(x)
        self.escludi_float(y)
        x = self.sanitizza(x, int)
        y = self.sanitizza(y, int)
        return x**y

    def converti_base(self, x):
        self.sanitizza(x, int)
        self.escludi_float(x)
        x = self.sanitizza(x, int)
        if x < 0:
            raise Exception("Input tipo non accettabile")

        return int(bin(x)[2:])

    def radice(self, x, y):
        x = self.sanitizza(x, int)
        y = self.sanitizza(y, int)

        if x<=0 or y<=0:
            raise Exception("Valori per la radice NON accettabili")

        return x**(1/y)

    def modulo(self, x, y):
        x = self.sanitizza(x, int)
        y = self.sanitizza(y, int)
        return x % y