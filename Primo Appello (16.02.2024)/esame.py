# Svolgimento

class ExamException(Exception):
    pass

def check_int(numero):
    try:
        int(numero)
    except:
        return False
    
    if float(numero) == int(numero):
        return True
    else:
        return False
    
    # controllo se una data stringa (o anche numero) è ESCLUSIVAMENTE int (quindi no float)

class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name

        try:
            open(self.name, "r")

        except:
            raise ExamException("File non leggibile")
        
    def get_data(self):
        file = open(self.name, "r")
        data = []

        ultimo_anno = -1
        ultimo_mese = -1
        next(file)
        for riga in file:
            elementi = riga.split(",")

            # controllo se la riga ha almeno due elementi su cui basarsi (data e coso)
            try:
                elementi[0]
                elementi[1]

            except:
                continue # ignoro e vado avanti (capita se ho qualcosa d.t. una riga vuota, ...)

            # controllo se i dati sono corretti (altrimenti vado avanti e lo scarto via)
            if not check_int(elementi[1]):
                continue # non è int oppure è float

            passeggeri = int(elementi[1])
            if passeggeri < 0:
                continue # minore di zero
            # controllo se la data va bene o meno (tipo dati)
            anno, mese = elementi[0].split("-")
            if not (check_int(mese) and check_int(anno)):
                continue # uno dei numeri non è int
            
            anno = int(anno)
            mese = int(mese)
            # controllo se la data va bene (ordinamento)
            if ultimo_anno > anno:
                raise ExamException("I dati non sono ordinati (anno)")

            if ultimo_anno == anno and ultimo_mese >= mese:
                raise ExamException("I dati non sono ordinati (mese) o ci sono duplicati di anno e mese") 
            
            ultimo_anno = anno
            ultimo_mese = mese
            # ¿ va tutto bene ? Allora re-imposto l'ultimo anno e l'ultimo mese come quello attuale, per preparare alla prox. iter.
            
            # tutto va bene, quindi inserisco l'elemento in data
            data.append([elementi[0], passeggeri])

        file.close()
        return data

def compute_increments(time_series, first_year, last_year):
    if not(type(first_year)== str and type(last_year==str)):
        return ExamException("Le date date non sono date in forma stringa")
    
    increments = {}

    if not (check_int(first_year) and check_int(last_year)):
        return ExamException("Le date date non sono interi")
    
    if first_year == last_year:
        return ExamException("Le date date sono uguali")
    
    # trasformo tutto in int per comodità, assumendo che sono esclusivamente int (già controllato)
    first_year_num = int(first_year)
    last_year_num = int(last_year)

    # vedo se numericamente le date siano accettabili o meno
    if first_year_num >= last_year_num:
        raise ExamException("Le date non sono accettabili")
    
    calcolando = False
    ultimo_elemento = 0
    mesi = 0
    medie = {i: None for i in range(first_year_num, last_year_num+1)} # genera un dizionario temporaneo di medie per ogni anno (None default, in caso di casi eccezionali)
        
    for serie in time_series:
        data = serie[0].split("-")
        passeggeri = serie[1]
        anno = int(data[0])
        # controllo "dove sono messo con la data attuale"
        if first_year_num < anno:
            # o ho finito i calcoli o i dati non ci sono mai stati, faccio i conti e ricomincio
            if mesi != 0:
                medie[first_year_num] = medie[first_year_num]/mesi

            first_year_num = anno 
            ultimo_elemento = first_year_num
            calcolando = False
            mesi = 0

        if first_year_num > anno:
            continue # sono troppo avanti, vado avanti finchè ho la data giusta

        if last_year_num < anno:
            ultimo_elemento = first_year_num
            break # sono troppo avanti, termino l'iterazione

        if first_year_num == anno: # bingo, inizio i calcoli (o li proseguo)
            if not calcolando:
                medie[first_year_num] = passeggeri
                mesi = 1
                calcolando = True

            else:
                medie[first_year_num] += passeggeri
                mesi += 1

    # ultimo calcolo per la media dell'utimo anno
    if mesi != 0:
        medie[ultimo_elemento] = medie[ultimo_elemento]/mesi

    for anno in medie: # ora faccio i conti per ottenere gli increments
        if medie[anno] is None:
            continue # se l'anno non ha avuto nessun dato, vado al prossimo anno

        else:
            for prossimo_anno in medie: # ora cerco il prossimo anno con media non-vuota
                if prossimo_anno <= anno:
                    continue # vado avanti, sto guardando ancora indietro
                
                else:
                    if medie[prossimo_anno] is None:
                        continue # vado avanti

                    else:
                        increments[f"{anno}-{prossimo_anno}"] = medie[prossimo_anno]-medie[anno] # inserisco l'incremento (o decremento)
                        break # termino ciclo e vado al prox.

    if increments == {}: 
        increments = [] # caso del vuoto nietzscheiano

    return increments