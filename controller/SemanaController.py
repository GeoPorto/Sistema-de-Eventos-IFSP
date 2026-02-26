from DAOGenerico import ControleDAO
from modelo.Semana import Semana

class SemanaController:

    def __init__(self):
        self.__dao = ControleDAO()
    
    def insert(self, semana: Semana):
        sql = semana.insertSql()
        self.__dao.insert(sql)

    def pesquisarSemana(self, semana: Semana):
        sql = semana.selectSql(semana.getIdSemana())
        return self.__dao.procura_registro(sql)
    
    def pesquisarSemanaPorId(self, id):
        sql = Semana.selectSql(Semana, id)
        resultado =  self.__dao.procura_registro(sql)
        resultado = resultado[0]
        if resultado:
            print(resultado)
            semana = Semana(resultado[0], resultado[3], resultado[4], resultado[1], resultado[5], resultado[2])
            return semana
        else:
            return None

    def findAllSemanas(self):
        sql = Semana.selectAllSql(self)
        resultados = self.__dao.procura_registro(sql)
        semanas = []
        for resultado in resultados:
            semana = Semana(resultado[0], resultado[3], resultado[4], resultado[1], resultado[5], resultado[2])
            semanas.append(semana)
        return semanas
    
    def formataTuplaEmDicionario(self, dado):
        semanaFormatada = {}
        if len(dado) >= 1:
            semanaFormatada['idSemana'] = dado[0][0]
            semanaFormatada['nome'] = dado[0][1]
            semanaFormatada['sigla'] = dado[0][2]
            semanaFormatada['finalizado'] = dado[0][3]
            semanaFormatada['inicio'] = dado[0][4]
            semanaFormatada['termino'] = dado[0][5]
        return semanaFormatada

    def formataTuplaEmListaDeDicionarios(self, dados):
        listaSemanasFormatadas = []
        for dado in dados:
            semanaFormatada = {
                'idSemana': dado[0],
                'nome': dado[1],
                'sigla': dado[2],
                'finalizado': dado[3],
                'inicio': dado[4],
                'termino': dado[5]
            }
            listaSemanasFormatadas.append(semanaFormatada)
        return listaSemanasFormatadas

    def setSemanaDicionario(self, semanaDicionario, semana: Semana):
        semana.setIdSemana(semanaDicionario['idSemana'])
        semana.setNome(semanaDicionario['nome'])
        semana.setSigla(semanaDicionario['sigla'])
        semana.setFinalizado(semanaDicionario['finalizado'])
        semana.setInicio(semanaDicionario['inicio'])
        semana.setTermino(semanaDicionario['termino'])