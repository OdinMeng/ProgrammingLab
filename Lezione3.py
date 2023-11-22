# I files 

# Esercizio 2: sum_csv;
def sum_csv(file_name):
    sum = 0
    file = open(file_name, "r")
    for entrata in file:
        elementi = entrata.split(",")
        if elementi[0] != "Date":
            sum = sum + float(elementi[1])
            # Per il 10 uso flusso try-except
    file.close()

    if sum==0:
        sum = None

    return sum
