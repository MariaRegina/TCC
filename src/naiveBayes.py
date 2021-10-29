import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

class naiveBayes:
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

        X_train, X_test, y_train, y_test = train_test_split(dadosMfcc, pessoa, test_size = 0.3, random_state = 0)


        classifier = GaussianNB()
        classifier.fit(X_train, y_train)

        y_pred = classifier.predict(X_test)

        f1u = metrics.f1_score(y_test, y_pred, average='micro')
        f1m = metrics.f1_score(y_test, y_pred, average='macro')
        f1 = metrics.f1_score(y_test, y_pred, average=None)

        print(f'f1u = {f1u}')
        print(f'f1m = {f1m}')
        print(f'f1 = {f1}')

        disp = metrics.plot_confusion_matrix(classifier, dadosMfcc, pessoa)
        plt.show()

naiveBayes(1, 52)