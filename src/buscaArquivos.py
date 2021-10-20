from configDB import configDB
from dadosAudio import dadosAudio

class buscaArquivos:

    def __init__(self):
        self.conexaoBanco = configDB()
        self.vetDadosAudio = []

    def buscaArquivosbyId(self, id, cont):
        sql = " select path from train "
        sql += " where client_id = '" + id + "' and length(sentence) >= 70 "
        sql += " order by 1 desc; "

        arquivos = self.conexaoBanco.exeSql(sql)

        for arquivo in arquivos:
            path = r"C:/Users/Public/BaseTCC/cv-corpus-7.0-2021-07-21/pt/clips/" + arquivo[0]
            audio = dadosAudio(cont, id, path)
            self.vetDadosAudio.append(audio)


    def buscaIdValidos(self):
        sql = " select a.client_id from (select count(client_id) AS QTD, client_id from train where length(sentence) >= 70 "
        sql += " group by client_id order by 1 desc) A "
        sql += " inner join train B on a.client_id = b.client_id "
        sql += " where QTD >= 10 "
        sql += " group by A.client_id; "

        dados = self.conexaoBanco.exeSql(sql)

        cont = 0
        for id in dados:
            cont += 1
            self.buscaArquivosbyId(id[0], cont)
            break

        self.conexaoBanco.fecharConexao()