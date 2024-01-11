import random

class Automa:
    def __init__(self):
        self.biancheria = None
        self.calzini = None
        self.maglia = None
        self.pantaloni = None
        self.calzatura = None

    def biancheria(self):
        pass

    def calzini(self):
        pass

    def maglia(self):
        pass

    def pantaloni(self):
        pass

    def calzatura(self):
        pass

# ordine: biancheria > pantaloni; calzini > calzatura

def esegui(automa, capo):
    if capo == "biancheria":
        return automa.biancheria()

    elif capo == "calzini":
        return automa.calzini()

    elif capo == "maglia":
        return automa.maglia()

    elif capo == "pantaloni":
        return automa.pantaloni()

    elif capo == "calzatura":
        return automa.calzatura()

# main block
Boris = Automa()
capi_vestiario = []
vestito = True

while(vestito):
    capo = random.choice(capi_vestiario)
    # G1
    
    # G2
    try:
        esegui(Boris, capo)
    except:
        raise Exception("Boris è un fallito")

print("Automa vestito correttamente")