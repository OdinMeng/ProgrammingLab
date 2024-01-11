import simulazione

# Input accettabile
L1 = [2, 4, 8, 16]
# -> k=1 => [2.0, 4.0, 8.0, 16.0]
# -> k=2 => [3.0, 6.0, 12.0]
# -> k=3 => [4.666666666666667, 9.333333333333334]
# -> k=4 => [7.5]

LUnico = [1]
# -> k=1 => [1.0]

# Input non accettabili
L2 = ["a", "b", "c"]
L3 = "ciao"
L4 = 12
L5 = {1, 2, 3}
Lx = [L2, L3, L4, L5]

# Input NON accettabili
k_x = ["a", [1, 2], -1, 0, "2"]

# Creo oggetto per testing
try:
    k_1 = simulazione.MovingAverage(1)
    k_2 = simulazione.MovingAverage(2)
    k_3 = simulazione.MovingAverage(3)
    k_4 = simulazione.MovingAverage(4)
except Exception:
    raise Exception("Eccezione inaspettata durante l'inizializzazione dei MovingAverage")

# Testing
# 1. Input non accettabili (liste)
for L in Lx:
    try:
        k_2.compute(L)
    except Exception as e:
        if isinstance(e, simulazione.ExamException):
            pass

        else:
            raise Exception("Errore in 1. Eccezione inaspettata")

    else:
        raise Exception("Errore in 1. Errore non rilevato")

# 2. Input non accettabili (k)
for k in k_x:
    try:
        simulazione.MovingAverage(k)
    except Exception as e:
        if isinstance(e, simulazione.ExamException):
            pass
        
        else:
            raise Exception("Errore in 2. Eccezione inaspettata")
    else:
        raise Exception("Errore in 2. Eccezione non rilevata")

# 3. Caso generale accettabile
if k_2.compute(L1) != [3.0, 6.0, 12.0]:
    raise Exception("Errore in 3.1. Output sbagliato per L1, k=2")

if k_3.compute(L1) != [4.666666666666667, 9.333333333333334]:
    raise Exception("Errore in 3.2. Output sbagliato per L1, k=3")


# 4. Edge cases
if k_1.compute(L1) != [2.0, 4.0, 8.0, 16.0]:
    raise Exception("Errore in 4.1. Output sbagliato per L1, k=1 (edge case)")

if k_4.compute(L1) != [7.5]: 
    raise Exception("Errore in 4.2. Output sbagliato per L1, k=4 (edge case)")

if k_1.compute(LUnico) != [1.0]:
    raise Exception("Errore in 4.2. Output sbagliato per LUnico, k=1 (doppio edge case)")

# 5. Casi particolari inaccettabili (k > n)
k_5 = simulazione.MovingAverage(5)
try:
    k_5.compute(L1)

except Exception as e:
    if isinstance(e, simulazione.ExamException):
        pass
    
    else:
        raise Exception("Errore in 5.1. Eccezione inaspettata")
    
else:
    raise Exception("Errore in 5.1. Eccezione non rilevata")

print("Tutto ok!")