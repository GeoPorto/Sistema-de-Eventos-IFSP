from DAOGenerico import ControleDAO
from modelo.Matricula import Matricula


class MatriculaController:

    def __init__(self):
        self.__dao = ControleDAO()

    def insert(self, matricula: Matricula):
        sql = matricula.insertSql()
        self.__dao.insert(sql)

    def pesquisarMatricula(self, matricula: Matricula):
        sql = matricula.selectSql(matricula.getIdMatricula())
        return self.__dao.procura_registro(sql)

    def pesquisarMatriculaPorId(self, id):
        sql = Matricula.selectSql(Matricula, id)
        return self.__dao.procura_registro(sql)

    def findAllMatriculas(self):
        sql = Matricula.selectAllSql(self)
        resultados = self.__dao.procura_registro(sql)
        matriculas = []
        for resultado in resultados:
            matricula = Matricula(resultado[0], resultado[1], resultado[2])
            matriculas.append(matricula)
        return matriculas

    def verificarInscricaoExistente(self, idParticipante, idEvento):
        sql = f"SELECT * FROM matricula WHERE idParticipante = {idParticipante} AND idEvento = {idEvento}"
        resultado = self.__dao.procura_registro(sql)
        return len(resultado) > 0

    def pesquisarMatriculaPorIdEvento(self, idParticipante, idEvento):
        sql = f"SELECT * FROM matricula WHERE idParticipante = {idParticipante} AND idEvento = {idEvento};"
        resultado = self.__dao.procura_registro(sql)
        resultado = resultado[0]
        print(resultado)
        if resultado:
            matricula = Matricula(resultado[0], resultado[1], resultado[2])
            print(matricula)
            return matricula
        return None
