import time
from audioToCSV import audioToCSV
from primeiraOpcao import primeiraOpcao
from maquinaComite import maquinaComite

class fazAcontecer:

    def __init__(self):
        self.n_mfcc = 0
        self.hop_length = 0
        self.n_fft = 0
        self.opcaoRede = 0
        self.opcaoAlterarBase = 0
        self.qtdAmostrasPorPessoa = 0
        self.maquinaComite = 0
        self.inicio = 0
        self.fim = 0
        self.tempoExecucao = 0

    def configurarBase(self):
        #13-512
        # input("Quantidade de amostras por pessoa: ")
        audioToCSV(self.hop_length, self.n_fft, self.n_mfcc, self.qtdAmostrasPorPessoa)

    def configuraRede(self):
        # self.opcaoRede = input("Informe a rede:\n1 - MLP\n2 - Naive Bayes\n")
        # if int(self.opcaoRede) == 1:
        #     mlp(self.opcaoDeDados, 4 * int(self.n_mfcc))
        self.maquinaComite = maquinaComite(1, 4 * int(self.n_mfcc))
        self.escreveSaida(self.n_mfcc, self.maquinaComite.acuracia)
        # else:
        #     if int(opcao) == 2:
        #         naiveBayes(self.opcaoDeDados, 4 * int(self.n_mfcc))

    def escreveSaida(self, n, acuracia):
        self.fim = time.time()
        with open("saida.txt", "a") as f:
            f.write("Quantidade de filtros MFCC:" + str(self.n_mfcc) + " \n")
            f.write("Tamanho do salto: " + str(self.hop_length) + "\n")
            f.write("Quantidade de amostras por pessoa: " + str(self.qtdAmostrasPorPessoa) + "\n")
            f.write("Tamanho do janelamento: " + str(self.n_fft) + "\n")
            f.write("Acuracia: " + str(acuracia) + "\n")
            f.write("Tempo de execucaoo: " + str(self.fim - self.inicio) + "\n")
            f.write("\n\n\n")
            f.close()

    def opcoes(self):
        # self.n_mfcc = input("Número de filtros MFCC: ")
        self.n_fft = 2048
        #input("Tamanho do janelamento: ")
        # self.hop_length = input("Tamanho do salto: ")


        self.qtdAmostrasPorPessoa = 10
        self.hop_length = 512

        vet = [10, 15, 20, 25, 30, 35]

        for i in range(1, 51):
            self.inicio = time.time()
            self.n_mfcc = i

            # configurarBase = input('1 - Alterar base\n2 - Continuar\n')
            # if int(configurarBase) == 1:
            self.configurarBase()
            # self.opcaoDeDados = input("Escolha os dados que serão utilizados na rede\n"
            #                         + "1 - Média - Desvio Padrão - Mínimo - Máximo\n"
            #                         + "2 - Em construção\n")
            # if int(self.opcaoDeDados) == 1:

            self.opcaoBase = primeiraOpcao(self.n_mfcc)

            self.opcaoBase.geraArquivo()

            self.configuraRede()


vai = fazAcontecer()
vai.opcoes()






