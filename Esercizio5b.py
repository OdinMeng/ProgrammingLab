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
            x.readline() # extra
        except Exception:
            print("Errore")
            self.can_read = False
        else:
            self.name = name
            self.can_read = True
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

# Sol. alternativa -> creo una flag is_readable
# ! è insufficiente mettere solo open(); i.q. devo vedere se è pure LEGGIBILE

# Estendo a NumericalCSVFile
class NumericalCSVFile(CSVFile):
    def get_data(self):
        super_l = super().get_data()
        l = []
        for i in super_l:
            try:
                float(i[1])

            except Exception:
                print("Errore")
                l.append([i[0], i[1]])

            else:
                l.append([i[0], float(i[1])])


        return l

# dio_cristo = NumericalCSVFile("shampoo_sales.csv")
# print(dio_cristo.get_data())