# Testing dell'esercizio 8-9
from Esercizio8 import *

data_storico = [8,19,31,41]
data_window = [50,52,60]

Modello = FitTrendModel()
Modello.fit(data_storico)
risultato = Modello.predict(data_window)

if risultato != 68:
    raise Exception("Errore in 1")

dato_sbagliato = {"a", "b"}
try:
    Modello.predict(dato_sbagliato)
except TypeError:
    pass
else:
    raise Exception("Errore in 2")

dato_da_sanitizzare = ["1", "2", "5"]
try:
    Modello.predict(dato_da_sanitizzare)
except:
    raise Exception("Errore in 3")

dato_non_sanitizzabile = ["a", "x"]
try:
    Modello.predict(dato_non_sanitizzabile)
except TypeError:
    pass
else:
    raise Exception("Errore in 4")

# Finalmente testo su test_data.csv
from Esercizio6 import *
file = NumericalCSVFile("test_data.csv")
n = 3 # la dimensione del window
x = len(file.get_data()) +1 # la dimensione delle righe del csv
storico = [z[1] for z in file.get_data(end=x-n)]
window = [z[1] for z in file.get_data(start=x-n+1, end=x)]
Modello.fit(storico)
risultato2 = Modello.predict(window)
print(risultato2)
if risultato2 != 70:
    raise Exception("Errore in 5")
