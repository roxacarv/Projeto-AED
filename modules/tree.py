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

	def LeftRotation(self, noh):
		# método de rotacionar pra esquerda
		#filho direito de noh ocupará pos de noh
		y = noh.GetRight()
		# filho esquerdo de y será filho direito de noh
		noh.SetRight(y.GetLeft())
		# se o filho esquerdo de y nao for nulo, noh será pai dele
		if y.GetLeft() != self.nulo:
			y.GetLeft().SetParent(noh)
		#pai de noh agora se torna pai de y (também)
		y.SetParent(noh.GetParent())
		# se pai de noh for nulo, quer dizer que noh era a raiz da árvore
		#portanto, y passa a ser a raiz da árvore
		if noh.getParent() == self.nulo:
			self.SetRoot(y)
		# se pai de noh não for nulo, quer dizer que noh é filho direito ou esquerdo (óbvio)
		#precisamos disso para colocar y como novo filho do pai de noh (esquerdo ou direito)
		elif noh == noh.GetParent().GetLeft():
			# ao inves de noh, também poderiamos usar y no comando abaixo
			noh.GetParent().SetLeft(y)
		#se noh for filho direito, então y será filho direito do pai de nó
		else:
			noh.GetParent().SetRight(y)
		#só falta definir o pai de noh como y e o filho esquerdo de y como nó
		y.SetLeft(noh)
		noh.SetParent(y)
		
	
	#RightRotation é o contrário de LeftRotation (trocamos right por left - ATENÇÃO)
	def RightRotation(self, noh):
		# método de rotacionar pra direita
		#filho esquerdo de noh ocupará pos de noh
		y = noh.GetLeft()
		# filho direito de y será filho esquerdo de noh
		noh.SetLeft(y.GetRight())
		# se o filho direito de y nao for nulo, noh será pai dele
		if y.GetRight() != self.nulo:
			y.GetRight().SetParent(noh)
		#pai de noh agora se torna pai de y (também)
		y.SetParent(noh.GetParent())
		# se pai de noh for nulo, quer dizer que noh era a raiz da árvore
		#portanto, y passa a ser a raiz da árvore
		if noh.getParent() == self.nulo:
			self.SetRoot(y)
		# se pai de noh não for nulo, quer dizer que noh é filho direito ou esquerdo (óbvio)
		#precisamos disso para colocar y como novo filho do pai de noh (esquerdo ou direito)
		elif noh == noh.GetParent().GetLeft():
			# ao inves de noh, também poderiamos usar y no comando abaixo
			noh.GetParent().SetLeft(y)
		#se noh for filho direito, então y será filho direito do pai de nó
		else:
			noh.GetParent().SetRight(y)
		#só falta definir o pai de noh como y e o filho direito de y como nó
		y.SetRight(noh)
		noh.SetParent(y)
		
	def InOrderTreeWalk(self):
		#percorre a árvore em ordem (menor para maior)
		
	def Maximum(self):
		# retorna o número máximo
	
	def Minimum(self):
		# retorna o número mínimo
	
	def Successor(self):
		# retorna o número sucessor à entrada

	def Predecessor(self)::
		# retorna o número antecessor à entrada