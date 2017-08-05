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

	def Insert(self,data):
    	#definindo duas variáveis, 1 como nulo e outra como a raiz
		y = self.nulo
		x = self.__root
		# verificanção do x
		while x !=self.nulo:
    	#se o X não for nulo, poem o y = x, para se ter mais uma varíavel, pois vamos ter que fazer o x apontar para os filhos nas verificações
			y = x
			if data.GetData() < x.GetData():
				x = x.GetLeft()
			else:
    			x = x.GetRight() 

		data.SetParent(y)
		#se o y for nulo, então sabemos que a raiz é nula, logo:
		if y == self.nulo:
			self.__root = data
		#senão for nulo temos que verificar onde o dado vai estar, se é direito ou esquerdo:

		elif data.GetData() < y.GetData():
			y.setLeft(data)
		else:
    		y.SetRight(data)
		#por fim, criamos os filhos, nulos e setamos como vermelho, após damos um fix para balancear a árvore
		data.SetLeft(self.nulo)
		data.SetRight(self.nulo)
		data.SetIsRed(True)
		data.RBFixup()
		#RBFixup(data) não esquecer de chamar o RBFixup para balanceamento da árvore

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
		
	def InOrderTreeWalk(self,root):
		#percorre a árvore em ordem (menor para maior)
		if root != self.nulo:
    		self.InOrderTreeWalk(root.GetLeft())
			print(str(root), end="")
			self.InOrderTreeWalk(root.GetRight())

		
	def Maximum(self,noh):
    	# retorna o número máximo
		while noh.GetRight() != self.nulo:
			noh = noh.GetRight()
		return noh
		
	
	def Minimum(self,noh):
		# retorna o número mínimo
		while noh.GetLeft() != self.nulo:
    		noh = noh.GetLeft()
		return noh
	
	def Successor(self,noh):
		# retorna o número sucessor à entrada
		if noh.GetRight() != self.nulo:
			return self.Minimum(noh.GetRight())
		y = noh.GetParent()
		while y != self.nulo and noh == y.GetRight():
    		noh = y
			y = y.GetParent()
		return y

	def Predecessor(self)::
		# retorna o número antecessor à entrada
		if noh == self.nulo:
    		return 0
		elif noh.GetLeft() != self.nulo:
    		return self.Maximum(noh.GetRight())
		y = noh.GetParent()
		while y != self.nulo and noh == y.GetLeft():
    		noh = y
			y = y.GetParent()
		return y