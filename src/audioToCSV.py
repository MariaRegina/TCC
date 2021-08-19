#Processo não finaliza????????

import glob
import numpy as np
import librosa
import csv

def getDados(mfcc):
    vet = [np.mean(mfcc), np.std(mfcc), np.amin(mfcc), np.amax(mfcc)]
    return vet

def vai(fileName):
    hop_length = 512
    y, sr = librosa.load(fileName)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop_length, n_mfcc=13)
    vet = []
    for i in range(12):
        vet = np.concatenate((vet, getDados(mfcc[i])))
    return vet

pastas = glob.glob(r'..\base\*')
cont = 1

f = open('base.csv', 'w')

for pasta in pastas:
    arquivos = glob.glob(pasta + '\*')
    cont = [1];
    for fileName in arquivos:
        ciencia, sr = librosa.load(fileName)
        mfccPessoa = vai(fileName)
        writer = csv.writer(f, delimiter=';', lineterminator='\n')
        writer.writerow(mfccPessoa)
    break

f.close()