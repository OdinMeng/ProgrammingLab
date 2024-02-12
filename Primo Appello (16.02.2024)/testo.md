# Laboratorio di Programmazione
Compito d’esame per l’appello del 16/3/2024

Una time series (univariata) è una sequenza di valori ordinati nel tempo, ed esprime la variazione di un certo fenomeno nel tempo. Per ogni coppia di punti, il primo elemento corrisponde a un istante o intervallo di tempo, mentre il secondo è il valore di una qualche quantità relativa a quell’istante o intervallo.

Il file “data.csv” contiene la time series del numero totale mensile in migliaia di passeggeri su linee aeree internazionali, da Gennaio 1949 a Dicembre 1960. Il primo elemento di ogni riga rappresenta la data ed è in formato Anno-Mese. Il dato si presenta così:

date,passengers

1949-01,112

1949-02,118

1949-03,132

...

ovvero, messa sotto forma di tabella per comodità:

date
	

passengers

1949-01
	

112

1949-02
	

118

1949-03
	

132

...
	

...

Vogliamo leggere questo tipo di dati e calcolare, dato un intervallo di anni, la differenza tra il numero medio di passeggeri in un anno rispetto all’anno precedente. Dobbiamo quindi prima calcolare, per ogni anno, il numero medio di passeggeri, poi confrontare questo valore tra ogni coppia di anni nell’intervallo, ed infine ritornare le differenze per ogni coppia di anni.

Prendiamo in considerazione i primi tre anni (1949, 1950, 1951). Possiamo considerare una lista di 12 elementi per ogni anno, dove l’elemento all’indice i corrisponde al numero di passeggeri per il mese i+1 in quell’anno (all’indice 0 avremo il valore per il mese 1, Gennaio):

1949: [112,118,132,…]

1950: [115,126,141,…]

1951: [145,150,178,…]

Bisognerà calcolare quindi, per ogni anno, il numero medio di passeggeri (per l’esempio consideriamo solo i primi tre mesi, ma la media andrà calcolata su tutti i mesi ovviamente):

1949:  = 120.7

1950:  = 127.3

1951:  = 157.7

…ed infine sottrarre il valore dell’anno corrente e quello precedente, tornando in questo caso i valori 127.3 - 120.7  e 157.7 - 127.3, che dovranno essere opportunamente strutturati come da specifiche nella sezione seguente “informazioni sullo svolgimento”.

Informazioni sullo svolgimento

Dovete tenere in considerazione che possono esserci dei dati mancanti! Nelle misurazioni di un anno, può mancare il numero di passeggeri per uno o più mesi. Possono mancare anche le misurazioni per un intero anno.

Alla luce di tutto questo, create la classe CSVTimeSeriesFile, modificando o estendendo la classe CSVFile vista a lezione (oppure scrivendola da zero). La classe deve essere istanziata sul nome del file tramite la variabile name e deve avere un metodo get_data() che torni una lista di liste, dove il primo elemento delle liste annidate è la data ed il secondo il numero mensile di passeggeri.

Questa classe si dovrà quindi poter usare così:

        time_series_file = CSVTimeSeriesFile(name='data.csv')

    time_series = time_series_file.get_data()

...ed il contenuto della variabile time_series tornato dal metodo get_data() dovrà essere così strutturato (come lista di liste):

    [

      [“1949-01”, 112],

      [“1949-02”, 118],

      [“1949-03”, 132],

      ...

    ]

Per rilevare gli anni con un incremento nel numero medio di passeggeri, dovete creare una funzione a sé stante (definita NON nella classe CSVTimeSeriesFile ma direttamente nel corpo principale del programma), di nome compute_increments, che avrà come input la time series e che verrà usata così:

    compute_increments(time_series, first_year, last_year)

dove first_year e last_year corrispondono rispettivamente agli estremi dell’intervallo di anni che vogliamo considerare (entrambi gli estremi devono essere inclusi). La funzione dovrà ritornare (tramite un return) in output un dizionario, dove le chiavi saranno gli intervalli dei due anni presi in considerazione e i valori l’incremento del numero medio di passeggeri rispetto all’anno precedente.

   

    {

        “1949-1950”: 6.6,

        “1950-1951”: 30.4,

        ...
   }

   

Il file in cui scrivere il vostro codice deve chiamarsi "esame.py" e le eccezioni da alzare in caso di input non corretti o casi limite devono essere istanze di una specifica classe ExamException, che dovete definire nel codice come segue, senza modifica alcuna (copia-incollate le due righe):

    class ExamException(Exception):

        pass

...e che poi userete come una normale eccezione, ad esempio:

    raise ExamException('Errore, lista valori vuota')

Qualche informazione in più sulle specifiche e qualche e suggerimento:

    Nel file CSV possono mancare delle misurazioni. Per un anno è possibile che non venga registrato il numero dei passeggeri per NESSUN mese. In tal caso, se l’anno è compreso nell’intervallo di anni dato come input, l’anno senza misurazioni andrà ignorato. Per cui, se l’intervallo considerato è 1949, 1950, 1951 e per l’anno 1950 non abbiamo misurazioni, l’incremento nel numero di passeggeri per anni verrà calcolato tra l’anno 1951 e l’anno 1949. Se invece l’intervallo considerato è di soli due anni e per uno dei due anni non abbiamo misurazioni, l’output sarà una lista vuota.
    Attenzione che gli estremi dell’intervallo di tempo dati come input alla funzione devono essere validi valori: per esempio se vogliamo considerare un intervallo di tempo dal 1950 al 1952 chiameremo la funzione compute_increments(time_series, “1950”, “1952”), dove first_year e last_year devono essere passati alla funzione come stringhe e devono essere presenti nel file CSV, altrimenti va alzata un’eccezione.
    Se invece mancano misurazioni per uno o più mesi, chiaramente il numero medio di passeggeri andrà calcolato sul numero di mesi per cui abbiamo le misurazioni.

    I valori di che leggete dal file CSV sono da aspettarsi di tipo intero, un valore non numerico, oppure vuoto o nullo o negativo non deve essere accettato, ma tutto deve procedere comunque senza alzare eccezioni.

    La serie temporale nel file CSV è da considerare sempre ordinata, se per caso ci dovesse essere un timestamp fuori ordine va alzata un'eccezione (dentro la funzione get_data()) senza cercare di riordinare la serie. Stesso discorso se c’è un timestamp duplicato: si alza un'eccezione.

    Il file CSV può contenere letteralmente di tutto. Da linee incomplete a pezzi di testo che non c’entrano niente, e ogni errore salvo quello di un timestamp fuori ordine o duplicato va ignorato (ovvero, ignoro la riga contenente l’errore e vado a quella dopo). Nota: se riuscite a leggere due valori (data e numero di passeggeri) ma c’è un campo di troppo sulla stessa riga, questo non è da considerarsi un’errore e non bisogna ignorare quella riga.

    La classe CSVTimeSeriesFile controlla l’esistenza del file solo quando viene chiamato il metodo get_data() e, nel caso il file non esista o non sia leggibile, alza un'eccezione.

Informazioni sulla consegna

La consegna dell'esame deve avvenire tassativamente entro l'ora di inizio dell'appello orale, e può avvenire in due modi: allegando lo script esame.py, oppure indicando il commit hash da valutare su un repository GitHub, entrambi mandati via mail a stefanoalberto.russo@phd.units.it, come descritto più in dettaglio sul repository del corso: https://github.com/sarusso/ProgrammingLab   

Attenzione: se il file non si chiama “esame.py”, se le eccezioni alzate in caso di errori non sono di tipo “ExamException” o se le classi ed i metodi non si chiamano come indicato da specifiche, l’esame non potrà essere valutato!

Nota benissimo: il vostro file deve includere SOLO una classe, una funzione ed una eccezione, non deve includere nessun codice “main” o tantomeno chiedere input all’utente.

Se non vi ricordate bene come si usa Git, potete fare riferimento al tutorial dei tutor che è disponibile qui: https://github.com/drpOpZ/proglab2021-tutors/blob/master/git_quickstart.md.