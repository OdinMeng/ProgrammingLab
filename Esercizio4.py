# Consegna
# ---------
# 1) ok
# 2) ok
# 3) ogni entrata rappresenta una riga con i valori

class CSVFile():
    def __init__(self, name):
        self.name = name

    def get_data(self):
        l = []
        file = open(self.name, "r")
        for entrata in file:
            el = entrata.split(",")
            if el[0] != "Date":
                a = [el[0], el[1][:-1]]
                l.append(a)

        file.close()

        return l

# In realtà una cosa non andrebbe bene (toglie l'ultimo carattere dell'ultima riga ma shh)