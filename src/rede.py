from audioToCSV import audioToCSV
from primeiraOpcao import primeiraOpcao
# from naiveBayes import naiveBayes
from mlp import mlp

class fazAcontecer:

    def __init__(self):
        self.n_mfcc = 0
        self.hop_length = 0

    def configurarBase(self):
        #13-512
        opcao = input("Alterar base\n1- Sim\n2 - Não")
        if int(opcao) == 1:
            audioToCSV(self.hop_length, self.n_mfcc)

    def configuraRede(self):
        opcao = input("Informe a rede:\n1 - MLP\n2 - Naive Bayes\n")
        if int(opcao) == 1:
            mlp(self.opcaoDeDados, 4 * int(self.n_mfcc))
        # else:
        #     if int(opcao) == 2:
        #         naiveBayes(self.opcaoDeDados, 4 * int(self.n_mfcc))


    def opcoes(self):
        self.n_mfcc = input("Número de filtros MFCC: ")
        self.hop_length = input("Tamanho do salto: ")
        configurarBase = input('1 - Alterar base\n2 - Continuar\n')
        if int(configurarBase) == 1:
            self.configurarBase()
        self.opcaoDeDados = input("Escolha os dados que serão utilizados na rede\n"
                                + "1 - Média - Desvio Padrão - Mínimo - Máximo\n"
                                + "2 - Em construção\n")
        if int(self.opcaoDeDados) == 1:
            self.opcaoBase = primeiraOpcao(self.n_mfcc)

        self.opcaoBase.geraArquivo()

        self.configuraRede()

vai = fazAcontecer()
vai.opcoes()
# vai = audioToCSV(512, 13)
# vai.inicio()



