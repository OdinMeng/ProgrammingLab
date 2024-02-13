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
    
    # controllo se una data stringa (o anche numero) è ESCLUSIVAMENTE int (quindi no float) (roba ausiliaria)

class CSVTimeSeriesFile():
    """
    Classe per leggere file CSV convertire i dati sul file CSV in lista nestata del tipo
    [
        [data, numero]
        ...
    ]
    tramite il metodo get_data(). Inoltre controlla se il file esiste o meno, oppure se è leggibile o meno.
    """
    
    def __init__(self, name):
        self.name = name
        try:
            file = open(self.name, "r")
            file.readline()
            file.close()

        except:
            raise ExamException("File non leggibile o inesistente")
        
    def get_data(self):
        file = open(self.name, "r")
        data = []

        ultimo_anno = -1
        ultimo_mese = -1 
        # le ultime due var. serviranno per "iniziare" il controllo dell'ordinamento delle date; dato che stiamo parlando di line aeree, è sicuro assumerli come -1 (1 a.C.)
        
        if file.readline().strip() != "date,passengers":
            raise ExamException("Input scorretto: la tabella data non riferisce allo storico voluto")
            # forse si potrebbe semplicemente dare un avvertimento
        
        # inizio a controllare i dati
        for riga in file:
            elementi = riga.split(",")

            # controllo se la riga ha almeno due elementi su cui basarsi (data e passeggere)
            try:
                elementi[0]
                elementi[1]
                # altrimenti posso fare un if con ¿ len(elementi) >= 2 ? => ...

            except:
                continue # ignoro e vado avanti (capita se ho qualcosa d.t. una riga vuota, ...)

            # controllo se il dato a dx. è corretto (altrimenti vado avanti e lo scarto via)
            if not check_int(elementi[1]):
                continue # non è int oppure è float

            passeggeri = int(elementi[1])
            if passeggeri < 0:
                continue # minore di zero; invalido

            # controllo se l'elemento della colonna a sx è effettivamente una data (ovvero del tipo '([0-9]*)-([0-9]*)' )
            try:
                anno, mese = elementi[0].split("-")
            except:
                continue # ignoro     

            # controllo se la data va bene o meno (tipo)
            anno, mese = elementi[0].split("-")
            if not (check_int(mese) and check_int(anno)):
                continue # uno dei numeri non è strettamente int
            
            anno = int(anno)
            mese = int(mese)
            
            # controllo se il mese va bene (che non sia oltre il dicembre... undicembre?)
            if mese > 12:
                continue

            # controllo se la data va bene (ordinamento); ultimo e finale controllo dei dati
            if ultimo_anno > anno:
                raise ExamException("I dati non sono ordinati (anno)")

            if ultimo_anno == anno and ultimo_mese >= mese:
                raise ExamException("I dati non sono ordinati (mese) o ci sono duplicati di anno e mese") 
            
            ultimo_anno = anno
            ultimo_mese = mese
            # ¿ va tutto bene ? Allora re-imposto l'ultimo anno e l'ultimo mese come quello attuale, per prepararmi alla prox. iter.
            
            # tutto va bene, quindi inserisco l'elemento in data output
            data.append([elementi[0], passeggeri])

        file.close()
        return data

def compute_increments(time_series, first_year, last_year):
    """
    IDEA. Prima creo un dizionario in cui ci sono tutte le medie associate ad ogni anno; di default vengono associale al valore None.
    Dopodichè, facendo opportuni calcolo ri-associo la media dell'anno alla media effettiva dell'anno .
    Infine, itero la lista (o dizionario) delle medie, associando (in una maniera ordinata) due anni con medie non vuote all'incremento tra le medie dei due anni, associandolo poi all'output.
    """

    # NOTA: Non serve controllare time_series, dato dal modo che lo uso (ovvero con ---.get_data()), quest'ultima ha una certa forma garantita.

    # controllo input
    if not(type(first_year)== str and type(last_year==str)):
        raise ExamException("Le date date non sono date in forma stringa")
        
    increments = {}

    if not (check_int(first_year) and check_int(last_year)):
        raise ExamException("Le date date non sono interi")
    
    if first_year == last_year:
        raise ExamException("Le date date sono uguali")
    
    # trasformo tutto in int per comodità, assumendo che sono esclusivamente int (già controllato a priori)
    first_year_num = int(first_year)
    last_year_num = int(last_year)

    # vedo se numericamente le date siano accettabili o meno
    if first_year_num >= last_year_num:
        raise ExamException("Le date non sono accettabili (il primo anno è più grande o uguale dell'ultimo anno)")
    
    # vedo se gli estremi (input) sono presenti nel file CSV, in caso di esito negativo alzo eccez. (come previsto dalla consgn.)
    # IDEA. Itero la liste delle serie temporali (time_series), settando un flag; se uno degli estremi è presente, termino il ciclo e altero il flag
    # Altrimenti se termino il ciclo senza alterare il flag, allora ciò vuol dire che non sono stati trovati gli estremi.
    estremo_presente = 0

    for serie in time_series:
        data = serie[0].split("-")
        anno = data[0]
        if first_year == anno or last_year == anno:
            estremo_presente = 1
            break

    if not estremo_presente:
        raise ExamException("Input non valido; gli estremi degli anni non presenti nel CSV")

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
            if not calcolando: # devo instanziare il primo numero, ri-impostando da None a qualcosa
                medie[first_year_num] = passeggeri
                mesi = 1
                calcolando = True

            else:
                medie[first_year_num] += passeggeri
                mesi += 1

    # OSS. Quando termina il ciclo for, non faccio calcolo per l'ultima media. Quindi "la faccio a mano" con le seguenti righe

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
                        break # termino il for nestato e vado al prox. anno

    if increments == {}: 
        increments = [] # caso del vuoto nietzscheiano; ritorno lista vuota

    return increments