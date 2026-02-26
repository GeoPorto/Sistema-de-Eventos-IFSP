from DAOGenerico import ControleDAO
from modelo.Evento import Evento
from modelo.Participante import Participante


class EventoController:

    def __init__(self):
        self.__dao = ControleDAO()
    
    def insert(self, evento: Evento):
        sql = evento.insertSql()
        self.__dao.insert(sql)

    def pesquisarSemana(self, evento: Evento):
        sql = evento.selectSql(evento.getIdEvento())
        return self.__dao.procura_registro(sql)
    
    def pesquisarEventoPorId(self, id):
        sql = Evento.selectSql(Evento, id)
        return self.__dao.procura_registro(sql)

    def findAllEventos(self):
        sql = Evento.selectAllSql(self)
        resultados = self.__dao.procura_registro(sql)
        eventos = []
        for resultado in resultados:
            evento = Evento(resultado[0], resultado[5], resultado[7], resultado[1], resultado[2], resultado[3], resultado[4], resultado[6])
            eventos.append(evento)
        return eventos

    def findAllParticipantes(self, idEvento):
        sql = f"SELECT p.* FROM participante p INNER JOIN matricula m ON p.idParticipante = m.idParticipante WHERE m.idEvento = {idEvento};"
        resultados = self.__dao.procura_registro(sql)
        participantes = []
        for resultado in resultados:
            participante = Participante(resultado[0], resultado[1], resultado[2], resultado[3], resultado[5], resultado[4], resultado[6])
            participantes.append(participante)
        return participantes


