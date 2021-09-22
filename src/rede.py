import matplotlib.pyplot as plt

from sklearn import metrics, svm, neural_network, naive_bayes, tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np

dados = np.loadtxt('base.csv', delimiter=';', dtype=str)

dadosMfcc = dados[:, :-1]
pessoa = dados[:, 52]

qtde_tuplas = len(dadosMfcc)


classificador = neural_network.MLPClassifier(hidden_layer_sizes=(100, 200, 50), max_iter=500)
# classificador = naive_bayes.()

X_treino, X_teste, y_treino, y_teste = train_test_split(dadosMfcc, pessoa, test_size=0.3, shuffle=True, random_state=1)

classificador.fit(X_treino, y_treino)

predicao = classificador.predict(X_teste)


f1u = metrics.f1_score(y_teste, predicao, average='micro')
f1m = metrics.f1_score(y_teste, predicao, average='macro')
f1 = metrics.f1_score(y_teste, predicao, average=None)

print(f'f1u = {f1u}')
print(f'f1m = {f1m}')
print(f'f1 = {f1}')

disp = metrics.plot_confusion_matrix(classificador, dadosMfcc, pessoa)
plt.show()


