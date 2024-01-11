# Esercizi 8,9

class Model:
    def predict(self, data):
        raise NotImplementedError

    def fit(self, data):
        raise NotImplementedError

class TrendModel(Model):
    def predict(self, data):
        # l'input DEVE essere una lsita
        if(not isinstance(data, list)):
            raise TypeError

        # la lista DEVE contenere solo int (o almeno traducibili in int!) -> quindi scrollo e controllo, traduco in caso
        ctr = -1
        for pivot in data:
            ctr += 1
            if(not isinstance(pivot, int)):
                try:
                    data[ctr] = float(pivot)
                except:
                    raise TypeError

        prev_value = None
        flag = True
        incrementi = 0
        ctr = 0

        if len(data) == 0:
            return None

        if len(data) == 1:
            raise Error("Dati insufficienti")

        for item in data:
            if flag:
                flag = False
                prev_value = item
                continue
            
            incrementi += (item - prev_value)
            ctr += 1
            prev_value = item

        prediction = prev_value + incrementi/ctr
        return prediction

class FitTrendModel(TrendModel):
    def fit(self, data):
        self.global_avg_variation = super().predict(data) - data[-1]

    def predict(self, data):
        prediction = super().predict(data) - data[-1]
        result = (prediction+self.global_avg_variation)/2 + data[-1]
        return result
