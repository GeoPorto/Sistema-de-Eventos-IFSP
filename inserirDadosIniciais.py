from controller.ParticipanteController import ParticipanteController
from controller.SemanaController import SemanaController
from modelo.Participante import Participante
from modelo.Semana import Semana
from datetime import date, timedelta


def inserirDadosIniciaisSemana():
    semanaController = SemanaController()

    semanas = [
        Semana(0, "Semana Nacional de Ciência e Tecnologia", "SNCT", "N",
               date.today(), date.today() + timedelta(days=10)),

        Semana(0, "Semana De Engenharia", "SDE", "N",
               date.today() + timedelta(days=10),
               date.today() + timedelta(days=20)),

        Semana(0, "Semana De Pedagogia", "SDP", "N",
               date.today() + timedelta(days=20),
               date.today() + timedelta(days=30))
    ]

    for semana in semanas:
        semanaController.insert(semana)



# Executar apenas uma vez
if __name__ == "__main__":
    inserirDadosIniciaisSemana()
