# Non c'è la entry su autograding
# Introduco autograding per i miei modelli

# modello -> test data
# uso il costrutto try-except

from Esercizio6 import CSVFile

# Test 1: apro file non esistente
try:
    CSVFile("null.csv")
except:
    print("Ok!")
else:
    raise Exception("Errore")

# Test 2: apro file esistente
try:
    File = CSVFile("test_data.csv")
except Exception:
    raise Exception("Errore in 2")
else:
    print("Ok 2!")

# Test 3: faccio get_data valido

try:
    File.get_data(1, 3)
except Exception as E:
    print(E)
    raise Exception("Errore in 3")
else:
    print("Ok 3!")

# Test 4: faccio get_data INVALIDO
try:
    File.get_data(5, 2)
except Exception as E:
    print("Ok 4!")
else:
    raise Exception("Errore in 4")
