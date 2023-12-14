# Unit testing - esercizio 4
from esercizio45 import Automobile
auto_di_maso = Automobile("Wolkswagen", "Golf II", 5, "C0GL10N3-S0RD0")
auto_di_alex = Automobile("Ford", "Fiesta", 200, "R4ZZ1S4-B4S4T0")
auto_di_coglione = Automobile("Wolkswagen", "Golf II", 5, "P0V3R0")

# Printo le informazioni
print(auto_di_maso)
print(auto_di_alex)

# Confronto le auto; maso -> alex e maso -> coglione
x = auto_di_maso.confronta(auto_di_coglione)
if x != 1:
    raise Error("Errore in 1")

y = auto_di_alex.confronta(auto_di_maso)
if y != 0:
    raise Error("Errore in 2")

# Confronto tra tipi invalidi
try:
    auto_di_maso.confronta("Ciao")
except TypeError:
    pass
else:
    raise Error("Errore in 3")

# Faccio parlare le auto
auto_di_maso.parla()
auto_di_alex.parla()