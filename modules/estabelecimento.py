# Árvore Rubro-negra - AED
# Projeto AED - BSI 2017.1 - UFRPE
###################################

from tree import *
from geradorId import *

class Estabelecimento:
    def __init__(self, nome, horario):
        self.__id = geraId(nome)
        self.__nome = nome
        self.__horario = horario
        self.__montante = 0
        self.__valor = 0
        self.__montante = BinaryTree()

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

    def AddMontante(self, novoValor):
        self.__montante.Insert(novoValor)

    def ImprimeMontante(self):
        return self.__montante.TreeWalk()