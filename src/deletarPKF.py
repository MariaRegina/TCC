import glob
import os

arquivos = glob.glob(r"C:/Users/maria/Desktop/Faculdade/TCC/Repositoorio/TCC/src/baseValida/*")
for fileName in arquivos:
    filename, file_extension = os.path.splitext(fileName)
    print(filename)
    if file_extension == '.pkf':
        os.remove(fileName)
