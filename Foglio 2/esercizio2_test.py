from esercizio2 import Calcolatrice

Macchinetta = Calcolatrice()

# Lista della spesa:
# fa i conti bene
# Input SOLO numerici
# NO divisione per 0!
# potenza SOLO per base e potenza INTERI
# radice n-esima SOLO per valori STRETTAMENTE positivi di k radice(n, k)
# conversione base SOLO da 10 a 2 e SOLO per valori interi positivi
# sanitizzare

print("Testando la calcolatrice... ")
# -- 1: fare i conti
# ---- 1.1.: 1+2=3
if Macchinetta.somma(1,2) != 3:
    raise Exception("Errore in 1.1")
# ---- 1.2.: 0.5*4=2
if Macchinetta.moltiplica(0.5, 4) != 2:
    raise Exception("Errore in 1.2.")
# ---- 1.3.: 2^3 = 8
if Macchinetta.potenza(2, 3) != 8:
    raise Exception("Errore in 1.3.")
# ---- 1.4.: 5 -> 101
if Macchinetta.converti_base(5) != 101:
    raise Exception("Errore in 1.4.")
# ---- 1.5.: 5-2 = 3
if Macchinetta.sottrazione(5, 2) != 3:
    raise Exception("Errore in 1.5.")
# ---- 1.6.: 7 % 3 = 1
if Macchinetta.modulo(7, 3) != 1:
    raise Exception("Errore in 1.6.")

# -- 2: input SOLO numerici
# ---- 2.1.: input corretti
try:
    Macchinetta.somma(1,2)
    Macchinetta.potenza(10, 2)
except:
    raise Exception("Errore in 2.1.")

# ---- 2.2.: input stringa ma corretti lo stesso (quindi da sanitizzare)
try:
    Macchinetta.radice("6", "2")
    Macchinetta.converti_base("76")
except:
    raise Exception("Errore in 2.2.")

# ---- 2.3.: input scorretti
try:
    Macchinetta.potenza(None)
    Macchinetta.somma("a", "b")
    Macchinetta.converti_base([1,2,"a"], {5: "a"})
    Macchinetta.radice("a", 2)
except:
    pass
else:
    raise Exception("Errore in 2.3.")

# -- 3: No divisione per 0
try:
    Macchinetta.divisione(5, 0)
except:
    pass
else:
    raise Exception("Errore in 3.")

# -- 4: Potenza solo per valori interi
try:
    Macchinetta.potenza(2, 2.1)
    Macchinetta.potenza(2.1, 2)
except:
    pass
else:
    raise Exception("Errore in 4.")

# ---- 4.1.: valori corretti
try:
    Macchinetta.potenza(1, 2)
    Macchinetta.potenza(4, 6)
except:
    raise Exception("Errore in 4.1.")

# -- 5: Radice solo per valori strettamente positivi
try:
    Macchinetta.radice(-1, 2)
    Macchinetta.radice(2, -1)
    Macchinetta.radice(-1, -1)
except:
    pass
else:
    raise Exception("Errore in 5.")

# ---- 5.2. valori corretti
try:
    Macchinetta.radice(2, 8)
    Macchinetta.radice(4, 16)
except:
    raise Exception("Errore in 5.2.")

# -- 6: conversione di base solo dalla base 10 a base 2 e per valori interi positivi
try:
    Macchinetta.converti_base(0.5)
    Macchinetta.converti_base(-1)
except:
    pass
else:
    raise Exception("Errore in 6.1.")

# ---- 6.2. valori corretti
try:
    Macchinetta.converti_base(10)
    Macchinetta.converti_base(20)
except:
    raise Exception("Errore in 6.2.")

print("Tutti test passati!")