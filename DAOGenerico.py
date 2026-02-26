import os
import pymysql
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

class ConfiguracaoBD:

    def __init__(self):
        self.servidor = os.getenv("DB_HOST")
        self.usuario = os.getenv("DB_USER")
        self.senha = os.getenv("DB_PASSWORD")
        self.banco = os.getenv("DB_NAME")
        self.ponteiro = None
        self.con = None

    def abrirConexao(self):
        self.con = pymysql.connect(
            host=self.servidor,
            db=self.banco,
            user=self.usuario,
            passwd=self.senha
        )
        self.ponteiro = self.con.cursor()

    def selectQuery(self, entrada):
        self.ponteiro.execute(entrada)
        return self.ponteiro.fetchall()

    def executeQuery(self, entrada, dados):
        self.ponteiro.execute(entrada, dados)

    def execute(self, entrada):
        self.ponteiro.execute(entrada)

    def gravar(self):
        self.con.commit()

    def descarte(self):
        self.con.rollback()

    def mostraResultado(self, entrada):
        for i in entrada:
            print(i)