# Argomento: programmazione OOP (Oggetti; TUTTO è un oggetto) -> persino stringhe, ...
# Oggetti -> stato entità e strutturare gerarchie

# Esempi di gerarchie:
# Appunti
# Supermercato -> preferibilmente entro / entro => applico politiche diverse
# Automobili 
# Stati del mondo -> ...
# Trovo caratteristiche su cui DIVIDERE le cose (non attributi!) e su cui appligo leggi

# Oggetti = classi
# funzioni di classi => metodi (ex: prodotto.CalcolaGuadagno() )
# variabili di classi => attributi (ex: prodotto.prezzo )
# istanziazione/inizializzazione = dichiarazione oggetti

""" pseudocodice x oggetto persona
- nome

- saluta
    print 'Ciao!'
"""

# Convenzione
# minuscoli, underscore per le VARIABILI e ISTANZE degli oggetti (anche in generale per variabili e funzioni)
# CamelCase per il nome delle classi (ex ProdottoDeperibileCaserarioDOC)

# metodi magici __...__
# uso apici singoli per str (superflua)

# Esercizio improvvisato: data una stringa, trovo la lunghezza della stringa in numero di parole (faccio len di split)
def len_parola(stringa):
    return len(stringa.split(" "))

# metodi: ritorna qualcosa o in place
# le in place sono difficili da gestire (sono fatte per performance)
my_list = [1,2,3,4]
print(my_list)
my_list.reverse() # => TORNO NIENTE
print(my_list)
# modo per gestire
my_list = [1,2,3,4]
reverse = my_list
reverse.reverse()
print(reverse)

# sintassi classe
class Persona():
    pass

person = Persona()
print(person)

# come dire a python di stampare un oggetto in un CERTO modo? sovrascrivo il metodo magico __str__

# ...


# con gli oggetti estesi per accedere alle "funzioni originali" uso il buintin super(). ...

# Voglio creare un oggetto testo
class Testo(str): # eredita da str -> è built in

    def __len__ (self):
        return len(self.split(" ")) # la split è DEFINITA in quanto ereditata

print(len(mio_testo := Testo('allora '*100)))
print(mio_testo)