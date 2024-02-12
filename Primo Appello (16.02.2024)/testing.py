import esame as exm

print("Testando...")
# TEST 1. INPUT CORRETTO, O SENZA CAUSARE ECCEZIONI
test_1 = exm.CSVTimeSeriesFile(name="data_test_no_eccez.csv")
data_1 = test_1.get_data()
res_1 = exm.compute_increments(data_1, "1949", "1951")
# Controllo se i risultati sono corretti o meno
expected_values = {"1949-1950": -88, "1950-1951": 48} # da vedere con russo
for x in res_1:
    if x not in expected_values:
        raise Exception("Errore in 1.1. : Calcoli mancanti")
    
    if x in expected_values and (expected_values[x] != res_1[x]):
        raise Exception("Errore in 1.2. : Calcoli errati")

print("Primo test passato!")
print("====================")

# TEST 2. INPUT SCORRETTO, CAUSANDO ECCEZIONI
# 1. File non esistente
try:
    test_2 = exm.CSVTimeSeriesFile(name="bingobungosbungo.csv")

except:
    pass

else:
    raise Exception("Errore in 2.1. : Il tentativo di aprire file non esistenti è andato a buon fine")

# 2. Ordine CSV sbagliato
test_2 = exm.CSVTimeSeriesFile(name="data_test_eccez1.csv")
try:
    test_2.get_data()
except:
    pass
else:
    raise Exception("Errore in 2.2. : Il tentativo di leggere il file è andato a buon fine")

# 3. Duplicati misurazioni
test_3 = exm.CSVTimeSeriesFile(name="data_test_eccez2.csv")
try:
    test_3.get_data()
except:
    pass
else:
    raise Exception("Errore in 2.3. : Il tentativo di leggere il file è andato a buon fine")

# 4. Chiamata funzione sbagliata
test_4 = exm.CSVTimeSeriesFile(name="data_test_no_eccez.csv")
data_4 = test_4.get_data()
try:
    exm.compute_increments(data_4, 1952, 1953)
    exm.compute_increments(data_4, "ciao", "1952")
    exm.compute_increments(data_4, "1953", "1952") 
except:
    pass
else:
    raise Exception("Errore in 2.4. : Il tentativo di calcolare la media degli incremendi è andato a buon fine")

print("Secondo test passato!")
# TEST 3. EDGE CASES (DATI VUOTI, ECCETERA)
test_5 = exm.CSVTimeSeriesFile(name="data_test_vuoti.csv")
data_5 = test_5.get_data()
res_5a = exm.compute_increments(data_5, "1951", "1952")
res_5b = exm.compute_increments(data_5, "1950", "1952")
res_5c = exm.compute_increments(data_5, "1949, 1951")

if res_5a != []:
    raise Exception("Errore in 3.1. : L'output dev'essere una lista vuota")

if res_5b != {"1950-1952": -44}:
    raise Exception("Errore in 3.2. : Calcolo errato")

if res_5c != {"1949-1950": -20}:
    raise Exception("Errore in 3.3. : Calcolo errato")

print("Ultimo test passato! Sei a posto!")
