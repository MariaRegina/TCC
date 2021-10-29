import numpy as np
import csv

class primeiraOpcao:
    def __init__(self, n_mfcc):
        self.n_mfcc = n_mfcc

    def escreveArquivo(self, vet):
        writer = csv.writer(self.fileCsv, delimiter=';', lineterminator='\n')
        writer.writerow(vet)

    def getDados(self, mfcc):
        vet = [np.mean(mfcc), np.std(mfcc), np.amin(mfcc), np.amax(mfcc)]
        return vet

    def geraArquivo(self):
        self.fileCsv = open('csv/primeiraOpcao.csv', 'w')
        with open("base.csv", "r") as f:
            reader = csv.reader(f, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
            linha = list(reader)
            vet = []
            contMfcc = 1
            for line in linha:
                opcoes = self.getDados(line[1:])
                vet = np.concatenate((opcoes, vet))
                if int(contMfcc) == int(self.n_mfcc):
                    vet = np.concatenate((vet, [line[0]]))
                    self.escreveArquivo(vet)
                    vet = []
                    contMfcc = 1
                else:
                    contMfcc = contMfcc + 1
        self.fileCsv.close()