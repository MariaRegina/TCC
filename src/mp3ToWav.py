import os
from pydub import AudioSegment
from buscaArquivos import buscaArquivos

arquivosValidos = buscaArquivos()

arquivosValidos.buscaIdValidos()
arquivos = arquivosValidos.vetDadosAudio

for x in arquivos:
    sound = AudioSegment.from_mp3(x.path)
    filename, file_extension = os.path.splitext(x.nameFile)
    sound.export("baseValida/" + filename + ".wav", format="wav")
