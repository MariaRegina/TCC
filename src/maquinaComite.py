import numpy as np
from sklearn import model_selection, neural_network
from sklearn.ensemble import BaggingClassifier

class maquinaComite:

    def __init__(self, opcaoCsv, tamVet):
        self.opcaoCsv = opcaoCsv
        self.tamVet = tamVet
        self.acuracia = 0
        self.fazAcontecer()

    def fazAcontecer(self):

        nome = "primeiraOpcao.csv"

        dados = np.loadtxt("csv/" + nome, delimiter=';', dtype=str)

        dadosMfcc = dados[:, :-1]
        pessoa = dados[:, int(self.tamVet)]
        seed = 13

        kfold = model_selection.KFold(n_splits=15, shuffle=True, random_state=seed)
        classifier = neural_network.MLPClassifier(hidden_layer_sizes=(200, 150, 100), max_iter=250)
        num_trees = 20

        model = BaggingClassifier(base_estimator=classifier, n_estimators=num_trees, random_state=seed)
        results = model_selection.cross_val_score(model, dadosMfcc, pessoa, cv=kfold)
        self.acuracia = results.mean()
        print(results.mean())

# maquinaComite(1, 52)