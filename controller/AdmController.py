from DAOGenerico import ControleDAO
from modelo.Administrador import Administrador


class AdmController:

    def __init__(self):
        self.__dao = ControleDAO()

    def insert(self, participante: Administrador):
        sql = participante.insertSql()
        self.__dao.insert(sql)

    def pesquisarAdm(self, adm: Administrador):
        sql = adm.selectSql(adm.getIdAdministrador())
        return self.__dao.procura_registro(sql)

    def pesquisarAdmPorId(self, id):
        sql = Administrador.selectSql(Administrador, id)
        return self.__dao.procura_registro(sql)

    def pesquisarLogin(self, login, senha):
        sql = Administrador.selectLogin(Administrador, login, senha)
        resultado =  self.__dao.procura_registro(sql)
        if resultado and len(resultado) > 0:
            resultado = resultado[0]
            adm = Administrador(resultado[0], resultado[1], resultado[2])
            return adm
        else:
            return None


