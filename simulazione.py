class ExamException(Exception):
    pass

class MovingAverage:
    def __init__(self, window):
        # Trovo se window è input accettabile
        if isinstance(window, float):
            raise ExamException("Input non accettabile (float)")

        if not isinstance(window, int):
            raise ExamException("Input non accettabile (non è un numero intero)")

        if window <= 0:
            raise ExamException("Input non accettabile (il numero dato comporta in sè degli assurdi)")

        else:
            self.window = window

    def evaluate(self, data):
        # 1. Controllo tipo dati
        if not isinstance(data, list):
            raise ExamException("Input data non accettabile (non è lista)")

        for elemento in data:
            if not (isinstance(elemento, float) or isinstance(elemento, int)):
                raise ExamException("Input data non accettabile (contiene non numerici)")

        # 2. Controllo che window e len(data) siano compatibili
        if not self.window <= len(data):
            raise ExamException("Input data non accettabile (la finestra è troppo larga per data o è un numero che non ha senso)")

        # 3. Controllo che la lista non sia vuota


    def compute(self, data):
        # Controlla se il dato input è accettabile
        self.evaluate(data)

        # Fa i calcoli, "simulando" una specie di iteratore
        i = 0
        end = False
        result = []
        while(True):
            s = 0
            try: 
                for j in range(i, self.window+i):
                    try:
                        data[j]
                        s += data[j]

                    except IndexError:
                        raise StopIteration

            except StopIteration:
                break

            result.append(s/self.window)

            i += 1
        return result        