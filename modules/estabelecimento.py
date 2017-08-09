# Árvore Rubro-negra - AED
# Projeto AED - BSI 2017.1 - UFRPE
###################################

class Estabelecimento:
    def __init__(self, id, nome, horario, montante, valor):
        self.__id = self.geraId(nome)
        self.__nome = nome
        self.__horario = horario
        self.__montante = montante 
        self.__valor = valor

    ''' get area '''
    
    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome
    
    def getHorario(self):
        return self.__horario
    
    def getMontante(self):
        return self.__montante
    
    def getValor(self):
        return self.__valor

    ''' set area '''
    
    def setNome(self,novoNome):
        self.__nome = novoNome
    
    def setHorario(self,novoHorario):
        self.__horario = horario
        
    def setMontante(self,novoMontante):
        self.__montante = montante
        
    def setValor(self,novoValor):
        self.__valor = valor

    
    '''extras'''
    def geraId(self, nome):
        newKey = 0
        weight = 1
        for s in nome:
            newKey += ord(s) * weight
            weight += 1
        return newKey
