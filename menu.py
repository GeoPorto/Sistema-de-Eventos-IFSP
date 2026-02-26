from flask import Flask, render_template, request, redirect, url_for

from controller.AdmController import AdmController
from controller.EventoController import EventoController
from controller.MatriculaController import MatriculaController
from controller.PalestranteController import PalestranteController
from controller.ParticipanteController import ParticipanteController
from controller.PresencaController import PresencaController
from controller.SemanaController import SemanaController
from modelo.Matricula import Matricula
from modelo.Palestrante import Palestrante
from modelo.Participante import Participante
from modelo.Presenca import Presenca
from modelo.Semana import Semana
from modelo.Evento import Evento

app = Flask(__name__, static_folder='resources')

semanaController = SemanaController()
participanteController = ParticipanteController()
palestranteController = PalestranteController()
eventoController = EventoController()
admController = AdmController()
matriculaController = MatriculaController()
presencaController = PresencaController()
participanteLogado = Participante("", "","","","","","")
idevento= ""

@app.route('/')
def home():
    listaSemanas = semanaController.findAllSemanas()
    return render_template('paginaInicial.html', listaSemanas=listaSemanas, current_page='paginaInicial')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logar', methods=['POST'])
def logar():
    login = request.form['login']
    senha = request.form['senha']
    global participanteLogado
    if participanteController.pesquisarLogin(login, senha):
        participanteLogado = participanteController.pesquisarLogin(login, senha);
        return redirect(url_for('paginaInicialParticipante'))
    else:
        if admController.pesquisarLogin(login, senha):
            return redirect(url_for('paginaInicialAdm'))
        else:
            return render_template('login.html', error='Login ou Senha incorreto.')
    return render_template('login.html', error='Login ou Senha incorreto.')

@app.route('/cadastro')
def cadastro():
    return render_template('telaCadastro.html')

@app.route('/adm/cadastrosemana')
def cadastrosemana():
    return render_template('telaCadastroSemana.html', current_page='adm/semanas')

@app.route('/adm/cadastropalestrante')
def cadastropalestrante():
    return render_template('telaCadastroPalestrante.html', current_page='adm/palestrantes')

@app.route('/adm/cadastroevento')
def cadastroevento():
    listaSemanas = semanaController.findAllSemanas()
    listaPalestrantes = palestranteController.findAllPalestrantes()
    return render_template('telaCadastroEvento.html', listaSemanas=listaSemanas, listaPalestrantes=listaPalestrantes, current_page='adm/eventos')

@app.route('/participante/paginaInicial')
def paginaInicialParticipante():
    print(participanteLogado)
    listaSemanas = semanaController.findAllSemanas()
    return render_template('paginaInicialParticipante.html', listaSemanas=listaSemanas, current_page='participante/paginaInicial')

@app.route('/adm/paginaInicial')
def paginaInicialAdm():
    listaSemanas = semanaController.findAllSemanas()
    return render_template('paginaInicialAdm.html', listaSemanas=listaSemanas, current_page='adm/paginaInicial')

@app.route('/adm/semanas')
def semanasAdm():
    listaSemanas = semanaController.findAllSemanas()
    return render_template('semanasAdm.html', listaSemanas=listaSemanas,  current_page='adm/semanas')

@app.route('/adm/participantes')
def participantesAdm():
    listaParticipantes = participanteController.findAllParticipantes()
    return render_template('participantesAdm.html', listaParticipantes=listaParticipantes,  current_page='adm/participantes')

@app.route('/adm/palestrantes')
def palestrantesAdm():
    listaPalestrantes = palestranteController.findAllPalestrantes()
    return render_template('palestrantesAdm.html', listaPalestrantes=listaPalestrantes,  current_page='adm/palestrantes')

@app.route('/adm/eventos')
def eventosAdm():
    listaEventos = eventoController.findAllEventos()
    for evento in listaEventos:
        idSemana =evento.getIdSemana()
        semana = semanaController.pesquisarSemanaPorId(idSemana)
        evento.setNomeSemana(semana.getNome())

    return render_template('eventosAdm.html', listaEventos=listaEventos,  current_page='adm/eventos')

@app.route('/participante/eventos')
def eventosParticipante():
    listaEventos = eventoController.findAllEventos()
    for evento in listaEventos:
        idSemana =evento.getIdSemana()
        semana = semanaController.pesquisarSemanaPorId(idSemana)
        evento.setNomeSemana(semana.getNome())

    return render_template('eventosParticipante.html', listaEventos=listaEventos,  current_page='participante/eventos')

@app.route('/participante/inscricoes')
def inscricoesParticipante():
    listaEventos = participanteController.findAllEventos(participanteLogado.getIdParticipante())
    for evento in listaEventos:
        idSemana =evento.getIdSemana()
        semana = semanaController.pesquisarSemanaPorId(idSemana)
        evento.setNomeSemana(semana.getNome())

    return render_template('inscricoesParticipante.html', listaEventos=listaEventos,  current_page='participante/inscricoes')

@app.route('/cadastro/cadastrarparticipante', methods=['POST'])
def cadastrarparticipante():
    participante = Participante(0, request.form['cpf'], request.form['curso'], request.form['email'], request.form['nome'], request.form['login'], request.form['senha'])
    participanteController.insert(participante)
    return render_template('login.html')

@app.route('/participante/inscrever', methods=['POST'])
def inscreverparticipante():
    global participanteLogado

    if matriculaController.verificarInscricaoExistente(participanteLogado.getIdParticipante(), request.form['idEvento']):
        error='Você já está inscrito neste evento.'
        listaEventos = eventoController.findAllEventos()
        return render_template('eventosParticipante.html', error=error, listaEventos=listaEventos,
                               current_page='participante/eventos')
    else:
        matricula = Matricula(0, participanteLogado.getIdParticipante(), request.form['idEvento'])
        matriculaController.insert(matricula)
        mensagem="Matricula realizada com sucesso."
        listaEventos = participanteController.findAllEventos(participanteLogado.getIdParticipante())
        return render_template('inscricoesParticipante.html', mensagem=mensagem, listaEventos=listaEventos,  current_page='participante/inscricoes')

@app.route('/adm/cadastrarsemana', methods=['POST'])
def cadastrarsemana():
    semana = Semana(0, request.form['nome'], request.form['sigla'],"N", request.form['inicio'], request.form['termino'])
    semanaController.insert(semana)
    listaSemanas = semanaController.findAllSemanas()
    return render_template('semanasAdm.html', listaSemanas=listaSemanas,  current_page='adm/semanas')

@app.route('/adm/cadastrarpalestrante', methods=['POST'])
def cadastrarpalestrante():
    palestrante = Palestrante(0, request.form['cpf'], request.form['cargo'], request.form['email'], request.form['nome'])
    palestranteController.insert(palestrante)
    listaPalestrantes = palestranteController.findAllPalestrantes()
    return render_template('palestrantesAdm.html', listaPalestrantes=listaPalestrantes,  current_page='adm/palestrantes')

@app.route('/adm/cadastrarevento', methods=['POST'])
def cadastrarevento():
    evento = Evento(0, request.form['semana'], request.form['palestrante'], request.form['ch'], request.form['nome'], 0, request.form['qtdvagas'], request.form['qtdchamadas'])
    eventoController.insert(evento)
    listaEventos = eventoController.findAllEventos()
    for evento in listaEventos:
        idSemana = evento.getIdSemana()
        semana = semanaController.pesquisarSemanaPorId(idSemana)
        evento.setNomeSemana(semana.getNome())
    return render_template('eventosAdm.html', listaEventos=listaEventos,  current_page='adm/eventos')

@app.route('/adm/realizarchamada', methods=['POST'])
def realizarchamada():
    global idevento
    idevento = request.form['idEvento']
    print(idevento)
    listaParticipantes = eventoController.findAllParticipantes(request.form['idEvento'])
    return render_template('realizarChamada.html', listaParticipantes=listaParticipantes)

@app.route('/adm/finalizar', methods=['POST'])
def finalizarchamada():
    global idevento
    id_evento = idevento
    listaParticipantes = eventoController.findAllParticipantes(id_evento)

    lista_presencas = []

    for participante in listaParticipantes:
        idParticipante = participante.getIdParticipante()
        checkbox_name = f'presenca_{idParticipante}'
        presente = 'P' if request.form.get(checkbox_name) else 'F'
        lista_presencas.append((idParticipante, presente))

    for id_participante, presente in lista_presencas:
        matricula = matriculaController.pesquisarMatriculaPorIdEvento(id_participante, id_evento)
        if matricula:
            id_matricula = matricula.getIdMatricula()
            presenca = Presenca(0, id_matricula, presente)
            presencaController.insert(presenca)

    return redirect(url_for('eventosAdm'))

@app.route('/sair')
def sair():
    global participanteLogado
    participanteLogado = Participante("", "", "", "", "", "", "")
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)