import psycopg2

class configDB:

    def __init__(self):
        self.host = "localhost"
        self.dbname = "tcc"
        self.user = "postgres"
        self.password = "123456"
        conn_string = "host={0} user={1} dbname={2} password={3}".format(self.host, self.user, self.dbname, self.password)
        self.conn = psycopg2.connect(conn_string)

    def exeSql(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        dados = cursor.fetchall()
        return dados

    def fecharConexao(self):
        self.conn.close()



# print("Connection established")
#
# cursor = conn.cursor()
#
# cursor.execute("select client_id, PATH, sentence from dev LIMIT 1;")
#
# dados = cursor.fetchall()
#
#
# print(dados)
#
# # Clean up
# conn.commit()
# cursor.close()
