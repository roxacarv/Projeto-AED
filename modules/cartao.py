# Árvore Rubro-negra - AED
# Projeto AED - BSI 2017.1 - UFRPE
###################################

from tree import *

class Card:
    def __init__(self, numero, titular, limiteTotal):
        self.__numero = numero
        self.__titular = titular
        self.__limiteTotal = limiteTotal 
        self.__limiteAtual = limiteTotal 
        self.__montante = BinaryTree()

    ''' get area '''
    def getNumero(self):
        return self.__numero
    
    def getTitular(self):
        return self.__titular
    
    def getLimiteTotal(self):
        return self.__limiteTotal
    
    def getLimiteAtual(self):
        return self.__limiteAtual
    
    '''set area'''
    def setNumero(self, novoNumero):
        self.__numero = novoNumero
    
    def setTitular(self, novoTitular):
        self.__titular = novoTitular
    
    def setLimiteTotal(self, novoLimiteTotal):
        self.__limiteTotal = novoLimiteTotal

    ''' extras '''

    def desconto(self, valorDebitar):
        self.__limiteAtual -= valorDebitar 
    
    def AddMontante(self, novoValor):
        self.__montante.Insert(novoValor)

    def ImprimeMontante(self):
        return self.__montante.TreeWalk()
