# Svolgimento

class ExamException(Exception):
    pass

def check_int(numero):
    """
    Funzione ausiliaria che accetta un qualsiasi (unico) input e controllo se questo input è convertibile univocamente in int
    (quindi no str, no float, no ..., SOLO int); restituisce un valore booleano True/False
    In particolare accetta le stringhe e controlla se è convertibile univocamente in int. (cosa non presente con isistance!)
    check_int: x -> Bool
    """
    try:
        int(numero)
        float(numero)
    except:
        return False
    
    if float(numero) == int(numero): # controlla se non c'è la parte frazionaria (ovvero dopo la virgola), quindi se è intero
        return True
    else:
        return False

class CSVTimeSeriesFile(): # ricreo la classe da capo
    """
    Classe per leggere file CSV, convertire i dati sul file CSV in una lista nestata del tipo
    [
        [data, numero]
        ...
    ]
    tramite il metodo get_data(). Inoltre controlla se il file esiste o meno, oppure se è leggibile o meno.
    """
    
    def __init__(self, name):
        try:
            file = open(name, "r")
            file.readline()
            file.close()

        except:
            raise ExamException("File non leggibile o inesistente")
        
        # controllo se il file è un file CSV
        elementi = name.split(".")
        if (name == "csv" and elementi[-1] == "csv") or (name != "csv" and elementi[1] != "csv"): # casi speciali per cui si accetta anche "csv.csv" ma non "csv" (e basta)
            print("Warning: il file esibito non è del tipo .csv; metodo get_data() disabilitata")
            self.is_csv = False

        else:
            self.is_csv = True

        self.name = name


    def get_data(self):
        if not self.is_csv:
            raise ExamException("Errore: impossibile ottenere dati da questo file, dato che non è del tipo .csv")
        
        file = open(self.name, "r")
        data = []

        ultimo_anno = -1 
        ultimo_mese = -1 
        # le ultime due var. serviranno per "iniziare" il controllo dell'ordinamento delle date; dato che stiamo parlando di line aeree, è sicuro assumerli come -1 (1 a.C.)
        # OSS. in realtà ultimo_anno = 1948 andrebbe anche bene

        # controllo se il file CSV si riferisce alla tipologia di dati corretto (ovvero di linee aeree)
        instestazione = file.readline().strip()
        try:
            instestazione[0:15]
        except:
            raise ExamException("Input scorretto: il storico non si riferisce al contenuto voluto (linee aeree)") # sicuramente la stringa ha meno di 15 caratteri, ovvero non può avere l'intestazione giusta
        else:
            if instestazione[0:15]!= "date,passengers": # l'intestazione può avere altre colonne aggiuntive
                raise ExamException("Input scorretto: il storico non si riferisce al contenuto voluto (linee aeree)")
        # forse si potrebbe semplicemente dare un avvertimento (warning) ?
        
        # inizio a controllare i dati
        for riga in file:
            elementi = riga.split(",")

            # controllo se la riga ha almeno due elementi su cui basarsi (data e passeggeri)
            try:
                elementi[0]
                elementi[1]
                # altrimenti posso fare un if con ¿ len(elementi) >= 2 ? => ...

            except:
                continue # ignoro e vado avanti (capita se ho qualcosa d.t. una riga vuota, ...)

            # controllo se il dato a dx. è corretto (altrimenti vado avanti e lo scarto via)
            if not check_int(elementi[1]):
                continue # non è int oppure è float (non avrebbe senso...)

            passeggeri = int(elementi[1])
            if passeggeri <= 0:
                continue # minore di zero O nullo; invalido 

            # controllo se l'elemento della colonna a sx è effettivamente una data (ovvero del tipo '([0-9]*)-([0-9]*)' )
            try:
                anno, mese = elementi[0].split("-") 
                # oss. è interessante vedere che questa riga scarta anche i casi in cui l'anno o il mese è negativo
            except:
                continue # ignoro     

            # controllo se la data va bene o meno (se sono int?)
            anno, mese = elementi[0].split("-")
            if not (check_int(mese) and check_int(anno)):
                continue # uno dei numeri non è strettamente int
            
            anno = int(anno)
            mese = int(mese)
            
            # controllo se il mese va bene (che non sia oltre il dicembre... undicembre?... oppure l'antigennaio)
            if mese > 12 or mese <= 0:
                continue

            if anno < 0:
                continue
             # ignora anni negativi (dalla consegna si potrebbe pure ignorare gli anni che non stanno nell'intervallo specificato nel testo)

            # controllo se la data va bene (ordinamento); ultimo e finale controllo dei dati
            if ultimo_anno > anno:
                raise ExamException("I dati non sono ordinati (anno)")

            if ultimo_anno == anno and ultimo_mese >= mese:
                raise ExamException("I dati non sono ordinati (mese) o ci sono duplicati di anno e mese") 
            
            # ---
            ultimo_anno = anno
            ultimo_mese = mese
            # ¿ va tutto bene ? Allora re-imposto l'ultimo anno e l'ultimo mese come quello attuale, per prepararmi alla prox. iter.
            
            # tutto va bene, quindi inserisco l'elemento in data output
            data.append([elementi[0], passeggeri])
            # vado alla prossima riga

        file.close()
        return data

def compute_increments(time_series, first_year, last_year):
    """
    IDEA. Prima creo un dizionario in cui ci sono tutte le medie associate ad ogni anno; di default vengono associale al valore None.
    Dopodichè, facendo opportuni calcolo ri-associo la media dell'anno alla media effettiva dell'anno .
    Infine, itero la lista (o dizionario) delle medie, associando (in una maniera ordinata) due anni con medie non vuote all'incremento tra le medie dei due anni, associandolo poi all'output.
    """

    # NOTA: Non serve controllare time_series, dato dal modo che lo uso (ovvero con ---.get_data()), quest'ultima ha una certa forma garantita.

    # NOTA 1. In caso controllo se time_series sia una lista o meno
    if not isinstance(time_series, list):
        raise ExamException("Input time_series invalido")

    # NOTA 2. Magari controllo se time_series è vuota o meno
    if time_series == []: # oppure len(time_series) == 0
        raise ExamException("La serie temporale è vuota (ergo in ogni caso gli estremi non sono compresi nel CSV)")
    
    # controllo input (anni)
    if not(isinstance(first_year, str) and isinstance(last_year, str)):
        raise ExamException("Le date date non sono date in forma stringa")
        
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

    ultimo_elemento = 0
    mesi = 0
    medie = {i: None for i in range(first_year_num, last_year_num+1)} # genera un dizionario temporaneo di medie per ogni anno (None default, in caso di casi eccezionali)
        
    for serie in time_series:
        data = serie[0].split("-")
        if len(data) != 2:
            continue 
            # ignora i casi anomali; ad esempio se ho il dato [-999--1],[100] (che dovrebbe essere impossibile, a priori), allora salto dato che avrei ['','999','','1']
        
        passeggeri = serie[1]
        anno = int(data[0])
        # controllo "dove sono messo con la data attuale"
        if first_year_num < anno:
            # o ho finito i calcoli o i dati non ci sono mai stati, faccio i conti e ricomincio
            if mesi != 0:
                medie[first_year_num] = medie[first_year_num]/mesi

            first_year_num = anno 
            ultimo_elemento = first_year_num
            mesi = 0

        if first_year_num > anno:
            continue # sono troppo avanti, vado avanti finchè ho la data giusta

        if last_year_num < anno:
            ultimo_elemento = first_year_num
            break # sono troppo avanti, termino l'iterazione

        if first_year_num == anno: # bingo, inizio i calcoli (o li proseguo)
            if mesi == 0: # devo instanziare il primo numero, ri-impostando da None a qualcosa
                medie[first_year_num] = passeggeri
                mesi = 1

            elif mesi > 0:
                medie[first_year_num] += passeggeri
                mesi += 1

    # OSS. Quando termina il ciclo for, non faccio calcolo per l'ultima media. Quindi "la faccio a mano" con le seguenti righe

    # ultimo calcolo per la media dell'ultimo anno
    if mesi != 0:
        medie[ultimo_elemento] = medie[ultimo_elemento]/mesi

    # istanzio il risultato
    increments = {}

    for anno in medie: # ora faccio i conti per ottenere gli increments ed assegnarli all'output finale
        if medie[anno] is None:
            continue # se l'anno non ha avuto nessun dato, vado al prossimo anno

        else:
            for prossimo_anno in medie: # ora cerco il prossimo anno con media non-vuota
                if prossimo_anno <= anno:
                    continue # vado avanti, sto guardando ancora indietro
                    # Oss. migliorabile usando un for + range (?); anzi in generale si poteva farlo già dall'inizio
                
                else:
                    if medie[prossimo_anno] is None:
                        continue # vado avanti

                    else:
                        increments[f"{anno}-{prossimo_anno}"] = medie[prossimo_anno]-medie[anno] # inserisco l'incremento (o decremento)
                        break # termino il for nestato e vado al prox. anno

    if increments == {}: 
        increments = [] # caso del vuoto nietzscheiano; ritorno lista vuota

    return increments