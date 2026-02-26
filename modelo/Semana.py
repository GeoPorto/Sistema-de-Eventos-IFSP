class Semana:

    def __init__(self, idSemana, nome, sigla, finalizado, inicio, termino):
      self.__idSemana = idSemana
      self.__nome = nome
      self.__sigla = sigla
      self.__finalizado = finalizado
      self.__inicio = inicio
      self.__termino = termino

    def getIdSemana(self):
      return self.__idSemana

    def setIdSemana(self, semana):
      self.__idSemana = semana

    def getNome(self):
      return self.__nome

    def setNome(self, nome):
      self.__nome = nome

    def getSigla(self):
      return self.__sigla

    def setSigla(self, sigla):
      self.__sigla = sigla

    def getFinalizado(self):
      return self.__finalizado

    def setFinalizado(self, finalizado):
      self.__finalizado = finalizado

    def getInicio(self):
      return self.__inicio

    def setInicio(self, inicio):
      self.__inicio = inicio

    def getTermino(self):
      return self.__termino

    def setTermino(self, termino):
      self.__termino = termino

    def getSemana(self):
        dados = {}
        dados['idSemana'] = self.__idSemana
        dados['nome'] = self.__nome
        dados['sigla'] = self.__sigla
        dados['finalizado'] = self.__finalizado
        dados['inicio'] = self.__inicio
        dados['termino'] = self.__termino
        return dados

    def insertSql(self):
        sql = ("INSERT INTO semana (nome, sigla, finalizado, inicio, termino) VALUES('{}', '{}', '{}', '{}', '{}')".format(
            self.__nome, self.__sigla, self.__finalizado, self.__inicio, self.__termino))
        return sql

    def selectSql(self, idSemana):
        sql = ("SELECT idSemana, finalizado, inicio, nome, sigla, termino FROM semana WHERE idSemana = {}".format(idSemana))
        return sql

    def selectAllSql(self):
        sql = ("SELECT * FROM semana")
        return sql

    def updateSql(self):
        sql = ("UPDATE semana SET nome = '{}', sigla = '{}', finalizado = '{}', inicio = '{}', termino = '{}' WHERE (idSemana = {})".format(
            self.__nome, self.__sigla, self.__finalizado, self.__inicio, self.__termino, self.__idSemana))
        return sql

    def deleteSql(self):
        sql = ("DELETE FROM semana WHERE (idSemana = {})".format(self.__idSemana))
        return sql

