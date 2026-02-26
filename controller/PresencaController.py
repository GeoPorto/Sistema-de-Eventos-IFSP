from DAOGenerico import ControleDAO
from modelo.Presenca import Presenca


class PresencaController:

    def __init__(self):
        self.__dao = ControleDAO()

    def insert(self, presenca: Presenca):
        sql = presenca.insertSql()
        self.__dao.insert(sql)
