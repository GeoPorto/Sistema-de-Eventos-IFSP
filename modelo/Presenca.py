class Presenca:

    def __init__(self,idPresenca, idMatricula, presente):
        self.__idPresenca = idPresenca
        self.__idMatricula = idMatricula
        self.__presente = presente

    def getIdPresenca(self):
        return self.__idPresenca

    def setIdPresenca(self, idPresenca):
        self.__idPresenca = idPresenca

    def getIdMatricula(self):
        return self.__idMatricula

    def setIdMatricula(self, idMatricula):
        self.__idMatricula = idMatricula

    def getPresente(self):
        return self.__presente

    def setPresente(self, presente):
        self.__presente = presente

    def getPresenca(self):
        dados = {}
        dados['idPresenca'] = self.__idPresenca
        dados['idMatricula'] = self.__idMatricula
        dados['presente'] = self.__presente
        return dados

    def insertSql(self):
        sql = ("INSERT INTO presenca (idMatricula, presente) VALUES('{}', '{}')".format(
            self.__idMatricula, self.__presente))
        return sql

    def selectSql(self, idPresenca):
        sql = ("SELECT * FROM presenca WHERE idPresenca = {}".format(idPresenca))
        return sql

    def selectAllSql(self):
        sql = ("SELECT * FROM presenca")
        return sql

    def updateSql(self):
        sql = ("UPDATE presenca SET idMatricula = '{}', presente = '{}' WHERE (idPresenca = {})".format(
            self.__idMatricula, self.__presente, self.__idPresenca))
        return sql

    def deleteSql(self):
        sql = ("DELETE FROM presenca WHERE (idPresenca = {})".format(self.__idPresenca))
        return sql