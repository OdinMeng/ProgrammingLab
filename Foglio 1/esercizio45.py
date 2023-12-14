# Esercizi 4 e 5

class Automobile:
    def __init__(self, casa_automo, modello, numero_posti, targa):
        if type(casa_automo) != str or type(modello) != str or type(targa) != str:
            raise TypeError
        if type(numero_posti) != int:
            try:
                self.numero_posti = int(numero_posti)
            except:
                raise TypeError
        
        self.casa_automo = casa_automo
        self.modello = modello
        self.numero_posti = numero_posti
        self.targa = targa

    def __str__(self):
        return f"INFORMAZIONI AUTOMOBILE \n CASA AUTOMOBILISTICA: {self.casa_automo} \n MODELLO: {self.modello} \n NUMERO POSTI: {self.numero_posti} \n TARGA: {self.targa}"

    def parla(self):
        print("Broom broom")

    def confronta(self, other):
        if not isinstance(other, Automobile):
            raise TypeError
        
        if self.casa_automo == other.casa_automo and self.modello == other.modello and self.numero_posti == other.numero_posti:
            print("Le due automobili sono uguali")
            return 1
        else:
            print("Le due automobili sono diverse")
            return 0

class Transformer(Automobile):
    def __init__(self, casa_automo, modello, numero_posti, targa, generazione, grado, reparto):
        self.super(__init__(self, casa_automo, modello, numero_posti, targa))
        self.generazione = generazione
        self.grado = grado
        self.reparto = reparto

    def scheda_militare(self):
        return f"SCHEDA MILITARE TRANSFORMER \n GENERAZIONE {self.generazione}\n GRADO {self.grado}\n REPARTO: {self.reparto}"
