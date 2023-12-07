# Consegna
# ---------
# 1) ok
# 2) ok
# 3) ogni entrata rappresenta una riga con i valori
# 5a) Gestione eccezioni

class CSVFile():
    def __init__(self, name):
        try:
            x = open(name, "r")
        except Exception:
            print("Errore")
        else:
            self.name = name
        finally:
            x.close()

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


