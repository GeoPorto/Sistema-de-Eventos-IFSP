class Matricula:

    def __init__(self, idMatricula, idParticipante, idEvento):
        self.__idMatricula = idMatricula
        self.__idParticipante = idParticipante
        self.__idEvento = idEvento

    def getIdMatricula(self):
        return self.__idMatricula

    def setIdMatricula(self, idMatricula):
        self.__idMatricula = idMatricula

    def getIdEvento(self):
        return self.__idEvento

    def setIdEvento(self, idEvento):
        self.__idEvento = idEvento

    def getIdParticipante(self):
        return self.__idParticipante

    def setIdParticipante(self, idParticipante):
        self.__idParticipante = idParticipante

    def getMatricula(self):
        dados = {}
        dados['idMatricula'] = self.__idMatricula
        dados['idEvento'] = self.__idEvento
        dados['idParticipante'] = self.__idParticipante
        return dados

    def insertSql(self):
        sql = ("INSERT INTO matricula (idEvento, idParticipante) VALUES('{}', '{}')".format(
            self.__idEvento, self.__idParticipante))
        return sql

    def selectSql(self, idMatricula):
        sql = ("SELECT * FROM matricula WHERE idMatricula = {}".format(idMatricula))
        return sql

    def selectAllSql(self):
        sql = ("SELECT * FROM matricula")
        return sql

    def updateSql(self):
        sql = ("UPDATE matricula SET idEvento = '{}', idParticipante = '{}' WHERE (idMatricula = {})".format(
            self.__idEvento, self.__idParticipante, self.__idMatricula))
        return sql

    def deleteSql(self):
        sql = ("DELETE FROM matricula WHERE (idMatricula = {})".format(self.__idMatricula))
        return sql


