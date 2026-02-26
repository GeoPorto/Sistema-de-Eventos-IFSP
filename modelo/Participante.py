class Participante:

    def __init__(self,idParticipante, cpf, curso, email, nome, login, senha):
        self.__idParticipante = idParticipante
        self.__cpf = cpf
        self.__curso = curso
        self.__email = email
        self.__nome = nome
        self.__login = login
        self.__senha = senha

    def getIdParticipante(self):
        return self.__idParticipante

    def setIdParticipante(self, idParticipante):
        self.__idParticipante = idParticipante

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

    def getSenha(self):
        return self.__senha

    def setSenha(self, senha):
        self.__senha = senha

    def getCurso(self):
        return self.__curso

    def setCurso(self, curso):
        self.__curso = curso

    def getLogin(self):
        return self.__login

    def setLogin(self, login):
        self.__login = login

    def getParticipante(self):
        dados = {}
        dados['idParticipante'] = self.__idParticipante
        dados['cpf'] = self.__cpf
        dados['curso'] = self.__curso
        dados['email'] = self.__email
        dados['nome'] = self.__nome
        dados['login'] = self.__login
        dados['senha'] = self.__senha
        return dados

    def insertSql(self):
        sql = ("INSERT INTO participante (cpf, curso, email, nome, login, senha) VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(
            self.__cpf, self.__curso, self.__email, self.__nome, self.__login, self.__senha))
        return sql

    def selectSql(self, idParticipante):
        sql = ("SELECT * FROM participante WHERE idParticipante = {}".format(idParticipante))
        return sql

    def selectLogin(self, login1, senha1):
        sql = ("SELECT * FROM participante WHERE login = '{}' AND senha = '{}'".format(login1, senha1))
        return sql

    def selectLogin(self, login1, senha1):
        sql = ("SELECT * FROM participante WHERE login = '{}' AND senha = '{}'".format(login1, senha1))
        return sql

    def selectEventos(self, id):
        sql = ("SELECT * FROM evento INNER JOIN matricula ON evento.idEvento = matricula.idEvento WHERE matricula.idParticipante = {}".format(id))
        return sql

    def selectAllSql(self):
        sql = ("SELECT * FROM participante")
        return sql

    def updateSql(self):
        sql = ("UPDATE participante SET cpf = '{}', curso = '{}', email = '{}', nome = '{}', login = '{}', senha = '{}' WHERE (idAdministrador = {})".format(
            self.__cpf, self.__curso, self.__email, self.__nome, self.__login, self.__senha, self.__idParticipante))
        return sql

    def deleteSql(self):
        sql = ("DELETE FROM participante WHERE (idParticipante = {})".format(self.__idParticipante))
        return sql