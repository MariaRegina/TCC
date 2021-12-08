import matplotlib.pyplot as plt
from sklearn import metrics, svm, neural_network, naive_bayes, tree
from sklearn.model_selection import train_test_split
import numpy as np

class mlp:

    def __init__(self, opcaoCsv, tamVet):
        self.opcaoCsv = opcaoCsv
        self.tamVet = tamVet
        self.fazAcontecer()

    def fazAcontecer(self):
        nome = ""
        if int(self.opcaoCsv) == 1:
            nome = "primeiraOpcao.csv"

        dados = np.loadtxt("csv/" + nome, delimiter=';', dtype=str)

        dadosMfcc = dados[:, :-1]
        pessoa = dados[:, int(self.tamVet)]

        classificador = neural_network.MLPClassifier(hidden_layer_sizes=(200, 150, 100), max_iter=250)

        X_treino, X_teste, y_treino, y_teste = train_test_split(dadosMfcc, pessoa, test_size=0.3, shuffle=True,
                                                                random_state=1)

        classificador.fit(X_treino, y_treino)

        predicao = classificador.predict(X_teste)

        f1u = metrics.f1_score(y_teste, predicao, average='micro')
        f1m = metrics.f1_score(y_teste, predicao, average='macro')
        f1 = metrics.f1_score(y_teste, predicao, average=None)

        np.savetxt("saida.txt", f1)

        print(f'f1u = {f1u}')
        print(f'f1m = {f1m}')
        print(f1)

        print("\n\n\n")

        disp = metrics.plot_confusion_matrix(classificador, dadosMfcc, pessoa)
        plt.show()

# mlp(1, 52)