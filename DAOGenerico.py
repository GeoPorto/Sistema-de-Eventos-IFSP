import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

class ControleDAO:

    def __init__(self):
        self.servidor = os.getenv("DB_HOST")
        self.usuario = os.getenv("DB_USER")
        self.senha = os.getenv("DB_PASSWORD")
        self.banco = os.getenv("DB_NAME")
        self.con = None
        self.cursor = None

    def abrirConexao(self):
        self.con = pymysql.connect(
            host=self.servidor,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )
        self.cursor = self.con.cursor()

    def fecharConexao(self):
        if self.cursor:
            self.cursor.close()
        if self.con:
            self.con.close()

    def insert(self, sql):
        self.abrirConexao()
        self.cursor.execute(sql)
        self.con.commit()
        self.fecharConexao()

    def procura_registro(self, sql):
        self.abrirConexao()
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.fecharConexao()
        return resultado

    def update(self, sql):
        self.abrirConexao()
        self.cursor.execute(sql)
        self.con.commit()
        self.fecharConexao()

    def delete(self, sql):
        self.abrirConexao()
        self.cursor.execute(sql)
        self.con.commit()
        self.fecharConexao()