# 16.11.2023: Lezione II
# Sito importante: https://autograding.online/ per AUTOVALUTAZIONI di esercizi

# Esercizio 1: Scrivere funzione sum_list(my list)

def sum_list(my_list):
    if my_list == []:
        return None
    return sum(my_list)

# I files 

# Esercizio 2: sum_csv; per il 10 assumo i casi particolari
def sum_csv(file_name):
    sum = 0
    file = open(file_name)
    for entrata in file:
        elementi = entrata.split(",")
        if elementi[0] != "Date":
            sum += float(elementi[1])
    return sum