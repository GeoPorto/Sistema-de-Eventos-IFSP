from DAOGenerico import ControleDAO
from modelo.Evento import Evento
from modelo.Participante import Participante


class ParticipanteController:

    def __init__(self):
        self.__dao = ControleDAO()

    def insert(self, participante: Participante):
        sql = participante.insertSql()
        self.__dao.insert(sql)

    def pesquisarParticipante(self, participante: Participante):
        sql = participante.selectSql(participante.getIdParticipante())
        return self.__dao.procura_registro(sql)

    def pesquisarParticipantePorId(self, id):
        sql = Participante.selectSql(Participante, id)
        return self.__dao.procura_registro(sql)

    def pesquisarLogin(self, login, senha):
        sql = Participante.selectLogin(Participante, login, senha)
        resultado =  self.__dao.procura_registro(sql)
        if resultado and len(resultado) > 0:
            resultado = resultado[0]
            participante = Participante(resultado[0], resultado[1], resultado[2], resultado[3], resultado[5], resultado[4], resultado[6])
            return participante
        else:
            return None

    def findAllEventos(self, id):
        sql = Participante.selectEventos(Participante, id)
        resultados = self.__dao.procura_registro(sql)
        eventos = []
        for resultado in resultados:
            evento = Evento(resultado[0], resultado[5], resultado[7], resultado[1], resultado[2], resultado[3], resultado[4], resultado[6])
            eventos.append(evento)
        return eventos
    def findAllParticipantes(self):
        sql = Participante.selectAllSql(self)
        resultados = self.__dao.procura_registro(sql)
        participantes = []
        for resultado in resultados:
            participante = Participante(resultado[0], resultado[1], resultado[2], resultado[3], resultado[5], resultado[4], resultado[6])
            participantes.append(participante)
        return participantes

    def formataTuplaEmDicionario(self, dado):
        participanteFormatado = {}
        if len(dado) >= 1:
            participanteFormatado['idParticipante'] = dado[0][0]
            participanteFormatado['cpf'] = dado[0][1]
            participanteFormatado['curso'] = dado[0][2]
            participanteFormatado['email'] = dado[0][3]
            participanteFormatado['login'] = dado[0][4]
            participanteFormatado['nome'] = dado[0][5]
            participanteFormatado['senha'] = dado[0][6]
        return participanteFormatado

    def formataTuplaEmListaDeDicionarios(self, dados):
        listaParticipantesFormatados = []
        for dado in dados:
            participanteFormatado = {
                'idParticipante': dado[0],
                'cpf': dado[1],
                'curso': dado[2],
                'email': dado[3],
                'login': dado[4],
                'nome': dado[5],
                'senha': dado[6]
            }
            listaParticipantesFormatados.append(participanteFormatado)
        return listaParticipantesFormatados

    def setParticipanteDicionario(self, participanteDicionario, participante: Participante):
        participante.setIdParticipante(participanteDicionario['idParticipante'])
        participante.setCpf(participanteDicionario['cpf'])
        participante.setCuro(participanteDicionario['curso'])
        participante.setEmail(participanteDicionario['email'])
        participante.setLogin(participanteDicionario['login'])
        participante.setNome(participanteDicionario['nome'])
        participante.setSenha(participanteDicionario['senha'])