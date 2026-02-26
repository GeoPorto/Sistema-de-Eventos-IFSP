class Administrador:

    def __init__(self, idAdministrador, login, senha):
        self.__idAdministrador = idAdministrador
        self.__login = login
        self.__senha = senha

    def getIdAdministrador(self):
        return self.__idAdministrador

    def setIdAdministrador(self, idAdministrador):
        self.__idAdministrador = idAdministrador

    def getLogin(self):
        return self.__login

    def setLogin(self, login):
        self.__login = login

    def getSenha(self):
        return self.__senha

    def setSenha(self, senha):
        self.__senha = senha

    def mostrar(self):
        print('IdAdministrador: ', self.getIdAdministrador() ,' senha: ', self.getSenha() , ' login : ', self.__login)

    def getAdministrador(self):
        dados = {}
        dados['IdAdministrador'] = self.__idAdministrador
        dados['login'] = self.__login
        dados['senha'] = self.__senha
        return dados

    def insertSql(self):
        sql = ("INSERT INTO administrador (login, senha) VALUES('{}', '{}')".format(
                self.__login, self.__senha))
        return sql

    def selectSql(self, idAdministrador):
        sql = ("SELECT * FROM administrador WHERE idAdministrador = {}".format(idAdministrador))
        return sql

    def selectAllSql(self):
        sql = ("SELECT * FROM administrador")
        return sql

    def selectLogin(self, login1, senha1):
        sql = ("SELECT * FROM administrador WHERE login = '{}' AND senha = '{}'".format(login1, senha1))
        return sql

    def updateSql(self):
        sql = ("UPDATE administrador SET login = '{}', senha = '{}' WHERE (idAdministrador = {})".format(
            self.__login, self.__senha, self.__idAdministrador))
        return sql

    def deleteSql(self):
        sql = ("DELETE FROM administrador WHERE (idAdministrador = {})".format(self.__idAdministrador))
        return sql
