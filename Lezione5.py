# Lezione 5 23.11.2023
# Eccezioni, flusso try-except

# Le eccezioni non sono SOLO errori
# sono oggetti!!!

# except Exception as e:
# e è un istanza di Exception -> CLASSE BASE

# except è gerarchico, come if

# try -> except -> else ( -> finally ) 
# la finally non è necessaria 

# penso alle eccezioni come "mani alzate"; except un modo per dire "ok abbassale"
# le eccezioni salgono fino all'interprete

# |-----------------------------------|

# controllo input, sanitizzazione
# type(...) == ...
# => è molto meglio fare isinstance(..., ...)
# ==> esempio del testo
# MAI usare il system exit!

# classe di errore
class Errore(Exception):
    pass

raise Errore("mona!")

# utile da fare per catturare CERTI errori

# quanto sanitizzare? quanto voglio.

# da fare l'ultiso es sul csvfile