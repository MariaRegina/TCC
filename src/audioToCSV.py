#Processo não finaliza????????

import glob
import numpy as np
import librosa
import csv

def getDados(mfcc):
    n = 4
    # s = len(mfcc)//n
    # vet = [np.mean(mfcc[0:s]), np.std(mfcc[0:s]), np.amin(mfcc[0:s]), np.amax(mfcc[0:s])]
    # vet = [np.mean(mfcc[s:s*2]), np.std(mfcc[s:s*2]), np.amin(mfcc[s:s*2]), np.amax(mfcc[s:s*2])]
    # vet = [np.mean(mfcc[s:s*2]), np.std(mfcc[s:s*2]), np.amin(mfcc[s:s*2]), np.amax(mfcc[s:s*2])]
    vet = [np.mean(mfcc), np.std(mfcc), np.amin(mfcc), np.amax(mfcc)]
    # vet = [np.amin(mfcc), np.amax(mfcc)]
    # vet = [np.amax(mfcc)]
    return vet

def vai(fileName, cont):
    hop_length = 512
    y, sr = librosa.load(fileName)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop_length, n_mfcc=13)
    vet = []
    for i in range(13):
        vet = np.concatenate((vet, getDados(mfcc[i])))
    return np.concatenate((vet, [cont]))

opcao = input('1 - Base de treinamento\n2 - Base de teste\n')

pastaAudio = ['..\base\*', '..\BaseTeste\*']
escolhaArquivo = ['base.csv', 'teste.csv']

if int(opcao) == 1:
    pastas = glob.glob(r'..\base\*')
else:
    pastas = glob.glob(r'..\BaseTeste\*')

cont = 1

f = open(escolhaArquivo[int(opcao) - 1], 'w')

cont = 0;
for pasta in pastas:
    arquivos = glob.glob(pasta + '\*')
    cont = cont + 1
    for fileName in arquivos:
        ciencia, sr = librosa.load(fileName)
        mfccPessoa = vai(fileName, cont)
        writer = csv.writer(f, delimiter=';', lineterminator='\n')
        writer.writerow(mfccPessoa)

f.close()