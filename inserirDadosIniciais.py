from controller.ParticipanteController import ParticipanteController
from controller.SemanaController import SemanaController
from modelo.Participante import Participante
from modelo.Semana import Semana
from datetime import date, timedelta

def inserirDadosIniciais():
    semana = Semana(0,"Semana Nacional de Ciência e Tecnologia", "SNCT", "N", date.today(), date.today() + timedelta(days=10) )
    semanaController = SemanaController()

    semanaController.insert(semana)

    semana = Semana(0, "Semana De Engenharia", "SDE", "N", date.today() + timedelta(days=10), date.today() + timedelta(days=20))
    semanaController = SemanaController()

    semanaController.insert(semana)

    semana = Semana(0, "Semana De Pedagogia", "SDP", "N", date.today() + timedelta(days=20),
                    date.today() + timedelta(days=30))

    semanaController = SemanaController()

    semanaController.insert(semana)

def inserirDadosIniciaisParticipante():
    participante = Participante("1", "111111111-11", "Ciencia da Computacao", "email@email.com", "aluno 1", "aluno 1" )

    participanteController = ParticipanteController()

    participanteController.insert(participante)

for x in range(10):
    inserirDadosIniciais()

