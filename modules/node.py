# Árvore Rubro-negra - AED
# Projeto AED - BSI 2017.1 - UFRPE
###################################

class Node:

	def __init__(self, key, data):
		self.__key = key
		self.__data = data
		self.__color = True
		self.__parent = None
		self.__left = None
		self.__right = None
		# construtor do nó

	# retorna o pai do nó
	def GetParent(self):
		return self.__parent

	# retorna o filho esquerdo do nó
	def GetLeft(self):
		return self.__left
	
	# retorna o filho direito do nó
	def GetRight(self):
		return self.__right
	
	# retorna os dados do no
	def GetData(self):
		return self.__data

	# retorna a chave do nó // usada para identificar a posição na árvore
	def GetKey(self):
		return self.__key
		
	# retorna a cor do nó // preto = False e vermelho = True
	def GetIsRed(self):
		return self.__color
	
	# seta o pai do no
	def SetParent(self, newParent):
		self.__parent = newParent

	# seta o filho direito do nó
	def SetRight(self, newRight):
		self.__right = newRight
	
	# seta o filho esquerdo do nó
	def SetLeft(self, newLeft):
		self.__left = newLeft

	# seta a cor do no
	def SetIsRed(self, newBooleanValue):
		self.__color = newBooleanValue