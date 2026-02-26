class Palestrante:

    def __init__(self, idPalestrante, cpf, cargo, email, nome):
        self.__idPalestrante = idPalestrante
        self.__cpf = cpf
        self.__cargo = cargo
        self.__email = email
        self.__nome = nome

    def getIdPalestrante(self):
        return self.__idPalestrante

    def setIdPalestrante(self, idPalestrante):
        self.__idPalestrante = idPalestrante

    def getCpf(self):
        return self.__cpf

    def setCpf(self, cpf):
        self.__cpf = cpf

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getCargo(self):
        return self.__cargo

    def setCargo(self, cargo):
        self.__cargo = cargo

    def getPalestrante(self):
        dados = {}
        dados['idPalestrante'] = self.__idPalestrante
        dados['cpf'] = self.__cpf
        dados['cargo'] = self.__cargo
        dados['email'] = self.__email
        dados['nome'] = self.__nome
        return dados

    def insertSql(self):
        sql = ("INSERT INTO palestrante (cpf, cargo, email, nome) VALUES('{}', '{}', '{}', '{}')".format(
            self.__cpf, self.__cargo, self.__email, self.__nome))
        return sql

    def selectSql(self, idPalestrante):
        sql = ("SELECT * FROM palestrante WHERE idPalestrante = {}".format(idPalestrante))
        return sql

    def selectAllSql(self):
        sql = ("SELECT * FROM palestrante")
        return sql

    def updateSql(self):
        sql = ("UPDATE palestrante SET cpf = '{}', cargo = '{}', email = '{}', nome = '{}' WHERE (idPalestrante = {})".format(
            self.__cpf, self.__cargo, self.__email, self.__nome, self.__idPalestrante))
        return sql

    def deleteSql(self):
        sql = ("DELETE FROM palestrante WHERE (idPalestrante = {})".format(self.__idPalestrante))
        return sql
