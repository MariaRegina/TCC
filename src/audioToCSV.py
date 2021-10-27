from buscaArquivos import buscaArquivos
import numpy as np
import librosa
import csv

class audioToCSV:
    def __init__(self, hop_length, n_mfcc):
        self.buscaDados = buscaArquivos()
        self.hop_length = hop_length
        self.n_mfcc = n_mfcc
        self.inicio()

    def geraVetorMFCC(self, caminho, cont, fileCsv):
        y, sr = librosa.load(caminho)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=self.hop_length, n_mfcc=self.n_mfcc)
        vet = []
        for i in range(self.n_mfcc):
            vet = np.concatenate(([cont], mfcc[i]))
            writer = csv.writer(fileCsv, delimiter=';', lineterminator='\n')
            writer.writerow(vet)

    def gerarBase(self, fileCsv):
        arquivos = buscaArquivos()
        arquivos.buscaIdValidos()
        vetFiles = arquivos.vetDadosAudio

        cont = 1
        for file in vetFiles:
            print(str(cont) + " / " + str(len(vetFiles)))
            self.geraVetorMFCC(file.path, file.numPessoa, fileCsv)
            cont = cont + 1

    def inicio(self):
        print("Gerando base...")
        print("Extraindo MFCC dos arquivos...")
        fileCsv = open('base.csv', 'w')
        self.gerarBase(fileCsv)
        fileCsv.close()
