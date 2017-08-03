# Árvore Rubro-negra - AED
# Projeto AED - BSI 2017.1 - UFRPE
###################################

class BinaryTree:

	def __init__(self):
		# construtor da árvore
		self.__root = self.nulo = Node(None, None)
		# cor de nulo deve ser preta (Todo nó criado tem cor vermelha - por padrão)
		self.nulo.SetIsRed(False)

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
	def LeftRotation(self, noh):
		# método de rotacionar pra esquerda
		#filho direito de noh ocupará pos de noh
		y = noh.GetRight()
		# filho esquerdo de y será filho direito de noh
		noh.SetRight(y.GetLeft())
		# se o filho esquerdo de y nao for nulo, noh será pai dele
		if y.GetLeft() != self.nulo
		
	
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