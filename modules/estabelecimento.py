# Árvore Rubro-negra - AED
# Projeto AED - BSI 2017.1 - UFRPE
###################################

from tree import *
from geradorId import *

#Formato do horario: HH:MM-HH:MM
class Estabelecimento:
    def __init__(self, nome, horario):
        self.__id = geraId(nome)
        self.__nome = nome
        self.__horario = horario
        self.__valor = 0
        self.__montante = BinaryTree()

    ''' get area '''
    
    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome
    
    def getHorario(self):
        return self.__horario
    
    def getValor(self):
        return self.__valor

    ''' set area '''
    
    def setNome(self,novoNome):
        self.__nome = novoNome
    
    def setHorario(self,novoHorario):
        self.__horario = horario

    
    '''extras'''

    def AddValor(self, novoValor):
        self.__valor += novoValor

    def AddMontante(self, novoValor):
        self.__montante.Insert(novoValor, None)

    def ImprimeMontante(self):
        return self.__montante.TreeWalk()