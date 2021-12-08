from configDB import configDB
from dadosAudio import dadosAudio
import os

class buscaArquivos:

    def __init__(self):
        self.conexaoBanco = configDB()
        self.vetDadosAudio = []

    def buscaArquivosbyId(self, id, cont, qtdAmostrasPorPessoa):
        sql = " select path from train "
        sql += " where client_id = '" + id + "' and length(sentence) >= 70 "
        sql += " order by 1 desc "
        sql += " limit " + str(qtdAmostrasPorPessoa)

        arquivos = self.conexaoBanco.exeSql(sql)

        for arquivo in arquivos:
            nome = arquivo[0].split(".")[0]
            path = r"C:/Users/maria/Desktop/Faculdade/TCC/Repositoorio/TCC/src/baseValida/" + nome + ".wav";
            filename, file_extension = os.path.splitext(path)
            audio = dadosAudio(cont, id, path, nome)
            self.vetDadosAudio.append(audio)


    def buscaIdValidos(self, qtdAmostrasPorPessoa):
        sql = ' select a.client_id from (select count(client_id) AS QTD, client_id from train where length(sentence) >= 70 '
        sql += ' group by client_id order by 1 desc) A '
        sql += ' inner join train B on a.client_id = b.client_id '
        sql += ' where QTD >= ' + str(qtdAmostrasPorPessoa) + ' '
        sql += ' group by A.client_id; '

        dados = self.conexaoBanco.exeSql(sql)

        cont = 0
        for id in dados:
            cont += 1
            self.buscaArquivosbyId(id[0], cont, qtdAmostrasPorPessoa)
        self.conexaoBanco.fecharConexao()
