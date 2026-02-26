from DAOGenerico import ControleDAO
from modelo.Palestrante import Palestrante

class PalestranteController:

    def __init__(self):
        self.__dao = ControleDAO()
    
    def insert(self, palestrante: Palestrante):
        sql = palestrante.insertSql()
        self.__dao.insert(sql)

    def pesquisarPalestrante(self, palestrante: Palestrante):
        sql = palestrante.selectSql(palestrante.getIdPalestrante())
        return self.__dao.procura_registro(sql)
    
    def pesquisarPalestrantePorId(self, id):
        sql = Palestrante.selectSql(Palestrante, id)
        return self.__dao.procura_registro(sql)

    def findAllPalestrantes(self):
        sql = Palestrante.selectAllSql(self)
        resultados = self.__dao.procura_registro(sql)
        palestrantes = []
        for resultado in resultados:
            palestrante = Palestrante(resultado[0], resultado[2], resultado[1], resultado[3], resultado[4])
            palestrantes.append(palestrante)
        return palestrantes
    
    def formataTuplaEmDicionario(self, dado):
        palestranteFormatada = {}
        if len(dado) >= 1:
            palestranteFormatada['idPalestrante'] = dado[0][0]
            palestranteFormatada['cpf'] = dado[0][1]
            palestranteFormatada['cargo'] = dado[0][2]
            palestranteFormatada['email'] = dado[0][3]
            palestranteFormatada['nome'] = dado[0][4]
        return palestranteFormatada

    def formataTuplaEmListaDeDicionarios(self, dados):
        listaPalestrantesFormatados = []
        for dado in dados:
            palestranteFormatado = {
                'idPalestrante': dado[0],
                'cpf': dado[1],
                'cargo': dado[2],
                'email': dado[3],
                'nome': dado[4]
            }
            listaPalestrantesFormatados.append(palestranteFormatado)
        return listaPalestrantesFormatados

    def setSemanaDicionario(self, palestranteDicionario, palestrante: Palestrante):
        palestrante.setIdPalestrante(palestranteDicionario['idPalestrante'])
        palestrante.setCpf(palestranteDicionario['cpf'])
        palestrante.setCargo(palestranteDicionario['cargo'])
        palestrante.setEmail(palestranteDicionario['email'])
        palestrante.setNome(palestranteDicionario['nome'])
