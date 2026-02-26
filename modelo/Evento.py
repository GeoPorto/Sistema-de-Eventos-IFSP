class Evento:

    def __init__(self, idEvento, idSemana, idPalestrante, ch, nome, qtdematriculados, qtdevagas, qtdChamadas):
      self.__idEvento = idEvento
      self.__idSemana = idSemana
      self.__idPalestrante = idPalestrante
      self.__ch = ch
      self.__nome = nome
      self.__qtdematriculados = qtdematriculados
      self.__qtdevagas = qtdevagas
      self.__qtdChamadas = qtdChamadas
      self.__nomeSemana = ""

    def getIdEvento(self):
        return self.__idEvento

    def setIdEvento(self, idEvento):
        self.__idEvento = idEvento

    def getIdSemana(self):
        return self.__idSemana

    def setIdSemana(self, idSemana):
        self.__idSemana = idSemana

    def getIdPalestrante(self):
        return self.__idPalestrante

    def setIdPalestrante(self, idPalestrante):
        self.__idPalestrante = idPalestrante

    def getCh(self):
        return self.__ch

    def setCh(self, ch):
        self.__ch = ch

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getQtdematriculados(self):
        return self.__qtdematriculados

    def setQtdematriculados(self, qtdematriculados):
        self.__qtdematriculados = qtdematriculados

    def getQtdevagas(self):
        return self.__qtdevagas

    def setQtdevagas(self, qtdevagas):
        self.__qtdevagas = qtdevagas

    def getQtdechamadas(self):
        return self.__qtdChamadas

    def setQtdechamadas(self, qtdChamadas):
        self.__qtdChamadas = qtdChamadas

    def getNomeSemana(self):
        return self.__nomeSemana

    def setNomeSemana(self, nomeSemana):
        self.__nomeSemana = nomeSemana

    def insertSql(self):
        sql = ("INSERT INTO evento (idSemana, idPalestrante, ch, nome, qtdematriculados, qtdevagas, qtdChamadas) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            self.__idSemana, self.__idPalestrante, self.__ch, self.__nome, self.__qtdematriculados, self.__qtdevagas, self.__qtdChamadas))
        return sql

    def selectSql(self, idEvento):
        sql = ("SELECT * FROM evento WHERE idEvento = {}".format(idEvento))
        return sql

    def selectAllSql(self):
        sql = ("SELECT * FROM evento")
        return sql

    def updateSql(self):
        sql = ("UPDATE evento SET idSemana = '{}', idPalestrante = '{}', ch = '{}', nome = '{}', qtdematriculados = '{}', qtdevagas = '{}', qtdChamadas = '{}' WHERE (idEvento = {})".format(
            self.__idSemana, self.__idPalestrante, self.__ch, self.__nome, self.__qtdematriculados, self.__qtdevagas, self.__qtdechamadas, self.__idEvento))
        return sql

    def deleteSql(self):
        sql = ("DELETE FROM evento WHERE (idEvento = {})".format(self.__idEvento))
        return sql
