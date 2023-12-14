# Modifico oggetto CSV file t.c.
# 1 - Controllo se input è STRINGA
# 2 - modifico get_data() in modo tale da aggiungere argomenti start, end che sono un intervallo di righe da file

class CSVFile():
    def __init__(self, name):
        if type(name) != str:
            raise ValueError

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

    def get_data(self, start=1, end=None):
        # sanitizzo il tipi: prima controllo se end è None (ovvero fino alla fine, rappresento end=0 come end=infinito)
        no_end = 0
        if end == None:
            no_end = 1
            end = 0

        if type(start) != int or (type(end) != int and end != None):
            try:
                start = int(start)
                end = int(end)
            except:    
                raise ValueError

        # controllo se gli input di start ed end, in quanto interi, siano corretti o meno
        if (end > 1 and start > end) or (start <= 0 or end < 0):
            raise ValueError

        if not self.can_read:
            print("Errore")
            return None

        ctr = 1
        l = []
        file = open(self.name, "r")
        for entrata in file:
            el = entrata.split(",")
            if el[0] != "Date" and ctr >= start and (ctr <= end or no_end):
                el[1] = el[1].strip()
                l.append(el)
            ctr += 1

        if start > ctr-1 or end > ctr-1: # decremento di 1 perchè il contatore parte da 1
            raise ValueError
            
        file.close()

        return l

# dio_cristo = CSVFile("shampoo_sales.csv")
# print(dio_cristo.get_data(1, 70)) # Come controllo se il "start" non è troppo "grande" per il file? E l'end?