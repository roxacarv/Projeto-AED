# Árvore Rubro-negra - AED
# Projeto AED - BSI 2017.1 - UFRPE
###################################

class BinaryTree:

	def __init__(self):
		# construtor da árvore
		self.__root = self.nulo = Node(None, None)

	#retorna a raiz da arvore
	def GetRoot(self):
		return self.__root
	
	# seta a raiz da arvore
	def SetRoot(self, newRoot):
		self.__root = newRoot
	
	def RBFixup(self):
		# fix das cores pra o balanceamento

	def RBRemoveFixUp(self):
		# fix das cores durante a remoção de um elemento

	def RBInsert(self):
		# método de inserir um elemento

	def RBRemove(self):
		# método de remover um elemento

	#André modificando...
	def LeftRotation(self):
		# método de rotacionar pra esquerda
	
	#André modificando...
	def RightRotation(self):
		# método de rotacionar pra direita

	def InOrderTreeWalk(self):
		# caminhada

	def Maximum(self):
		# retorna o número máximo

	def Minimum(self):
		# retorna o número mínimo

	def Successor(self):
		# retorna o número sucessor à entrada

	def Predecessor(self)::
		# retorna o número antecessor à entrada