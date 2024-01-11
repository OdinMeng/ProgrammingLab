# Laboratorio di Programmazione
## Esercitazione di esame 1

La  media mobile è un’operazione che data una serie di valori calcola la media di una finestra che si “sposta” sulla serie, fino a calcolarla per tutti i valori. Il parametro fondamentale (e unico) di tale operazione è la lunghezza della finestra.

Per esempio, con lunghezza della finestra pari a “2”, e data la serie di valori 2, 4, 8, 16, la media mobile calcola al primo giro il risultato “3” (ovvero la media tra il valore 2 e 4, per il secondo il risultato “6” (ovvero la media tra i valori 4 e 8), e per il terzo il valore “12”, per poi tornare i valori 3, 6 e 12.

Visivamente:

    valori da mediare per il giro n°1:  [2,4,8,16]  →  3
    valori da mediare per il giro n°2:  [2,4,8,16]  →  6
    valori da mediare per il giro n°3:  [2,4,8,16]  →  12

Create quindi la classe MovingAverage, che venga inizializzata con la lunghezza delle finestra, e che abbia un metodo compute che prenda in input la lista di valori della serie e che ritorni la lista di valori corrispondente alla media mobile.

Esempio di come deve poter essere utilizzata la classe:

    moving_average = MovingAverage(2)

    result = moving_average.compute([2,4,8,16])

    print(result) # Deve stampare a schermo [3.0,6.0,12.0]

Scrivete tale oggetto nel file “esame.py”, e ricordatevi di effettuare i vari controlli relativi agli input e ai casi limite.

Le eccezioni che devono essere alzate in caso di input non corretti o casi limite devono essere istanze di una specifica classe, ovvero “ExamException”, che dovete definire nel codice in esame.py come segue:

    class ExamException(Exception):

        pass

...e che poi userete come una normale eccezione, ad esempio:

    raise ExamException(‘Errore, lista valori vuota’)

Attenzione: se il file non si chiama “esame.py”, se le eccezioni alzate in caso di errori non sono di tipo “ExamException” o se la classe non si chiama “MovingAverage”, l’esame non potrà essere valutato!