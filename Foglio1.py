# Esercizi foglio 1
"""
Realizzare un programma con le seguenti funzioni per la manipolazione delle liste:
1. stampa -> stampa contenuto di una lista
2. statistiche -> riceve una lista => se numeri: calcola somma, media, minimo e max.
3. somma_vettoriale -> riceve due liste, se sono interi e hanno stessa dimensione, calcola somma; alt. ritorna lista vuota
"""

def stampa(lista):
    for oggetto in lista:
        print(oggetto)

def statistiche(lista):
    somma = 0
    media = 0

    for oggetto in lista:
        if type(oggetto) != int:
            return "Non hai dato una lista di interi"
        
        else:
            somma += oggetto
    
    media = somma/len(lista)
    minimo = min(lista)
    massimo = max(lista)

    return somma, media, minimo, massimo

def somma_vettoriale(V1, V2):
    V = []

    if len(V1) != len(V2):
        return []

    # Soluzione non pythonica
    for i in range(len(V1)):
        if type(V1[i]) != int or type(V2[i]) != int:
            return []

        V.append(V1[i]+V2[i])

    # Soluzione pythonica -> ???

    return V



        