# Árvore Rubro-negra - AED
# Projeto AED - BSI 2017.1 - UFRPE
###################################

from node import *

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

	
	def Insert(self, key, data): # invoca o RBInsert passando o novo elemento como um objeto do tipo nó
		self.RBInsert(Node(key, data))

	def RBInsert(self, data):
    	# definindo duas variáveis, y como nulo e x como a raiz
		y = self.nulo
		x = self.__root
		# verificanção do x -- procura saber se vai o novo nó vai pro lado esquerdo ou direito
		while x != self.nulo:
    	#se o x não for nulo, y = x, para se ter mais uma varíavel, pois vamos ter que fazer o x apontar para os filhos nas verificações
			y = x
			if data.GetKey() < x.GetKey():
				x = x.GetLeft()
			else:
				x = x.GetRight() 
		data.SetParent(y)
		# se o y for nulo, então sabemos que a raiz é nula, logo:
		if y == self.nulo:
			self.__root = data
		# senão for nulo temos que verificar onde o dado vai estar, se é direito ou esquerdo:
		elif data.GetKey() < y.GetKey():
			y.SetLeft(data)
		else:
			y.SetRight(data)
		# por fim, criamos os filhos, nulos e setamos como vermelho, após damos um fix para balancear a árvore
		data.SetLeft(self.nulo)
		data.SetRight(self.nulo)
		data.SetIsRed(True)
		self.RBFixup(data) # não esquecer de chamar o RBFixup para balanceamento da árvore

	def RBFixup(self, n):
		while n.GetParent().GetIsRed():
			if n.GetParent() == n.GetParent().GetParent().GetLeft():
				y = n.GetParent().GetParent().GetRight()
				if y.GetIsRed():
					n.GetParent().SetIsRed(False)
					y.SetIsRed(False)
					n.GetParent().GetParent().SetIsRed(True)
					n = n.GetParent().GetParent()
				else:
					if n == n.GetParent().GetRight():
						n = n.GetParent()
						self.LeftRotation(n)
					n.GetParent().SetIsRed(False)
					n.GetParent().GetParent().SetIsRed(True)
					self.RightRotation(n.GetParent().GetParent())
			else:
				y = n.GetParent().GetParent().GetLeft()
				if y.GetIsRed():
					n.GetParent().SetIsRed(False)
					y.SetIsRed(False)
					n.GetParent().GetParent().SetIsRed(True)
					n = n.GetParent().GetParent()
				else:
					if n == n.GetParent().GetLeft():
						n = n.GetParent()
						self.RightRotation(n)
					n.GetParent().SetIsRed(False)
					n.GetParent().GetParent().SetIsRed(True)
					self.LeftRotation(n.GetParent().GetParent())
		self.__root.SetIsRed(False)

	def RBRemoveFixUp(self, n):
		while n != self.__root and not n.GetIsRed():
			if n == n.GetParent().GetLeft():
				w = n.GetParent().GetRight() 
				if w.GetIsRed(): # ----------------------------------------------------> caso 1: o irmão (w) de n é vermelho
					w.SetIsRed(False) # -----------------------------------------------> caso 1
					n.GetParent().SetIsRed(True) # ------------------------------------> caso 1
					self.LeftRotation(n.GetParent()) # --------------------------------> caso 1
					w = n.GetParent().GetRight() # ------------------------------------> caso 1
				if not w.GetLeft().GetIsRed() and not w.GetRight().GetIsRed(): # ------> caso 2: o irmão (w) de n é preto e ambos os filhos de w também
					w.SetIsRed(False)  # ----------------------------------------------> caso 2
					n = n.GetParent() # -----------------------------------------------> caso 2
				else: # ---------------------------------------------------------------> caso 3: o irmão (w) de n é preto, seu filho esquerdo é vermelho e o direito preto
					if not w.GetRight().GetIsRed(): # ---------------------------------> caso 3
						w.GetLeft().SetIsRed(False) # ---------------------------------> caso 3
						w.SetIsRed(True) # --------------------------------------------> caso 3
						self.RightRotation(w) # ---------------------------------------> caso 3
						w = n.GetParent().GetRight() # --------------------------------> caso 3
					w.SetIsRed(n.GetParent().GetIsRed()) # ----------------------------> caso 4: o irmão (w) de n é preto e seu filho da direita é vermelho
					n.GetParent().SetIsRed(False) # -----------------------------------> caso 4
					w.GetRight().SetIsRed(False) # ------------------------------------> caso 4
					self.LeftRotation(n.GetParent()) # --------------------------------> caso 4
					n = self.__root # -------------------------------------------------> caso 4
			else: # caso o filho deletado seja o direito do pai de n, repete o mesmo código porém trocando LEFT por RIGHT e vice-versa
				w = n.GetParent().GetLeft()
				print("cor right: %s cor left: %s" % (w.GetRight().GetIsRed(), w.GetLeft().GetIsRed()))
				if w.GetIsRed():
					w.SetIsRed(False)
					n.GetParent().SetIsRed(True)
					self.RightRotation(n.GetParent())
					w = n.GetParent().GetLeft()
				if not w.GetRight().GetIsRed() and not w.GetLeft().GetIsRed():
					w.SetIsRed(False)
					n = n.GetParent()
				else:
					if not w.GetLeft().GetIsRed():
						w.GetRight().SetIsRed(False)
						w.SetIsRed(True)
						self.LeftRotation(w)
						w = n.GetParent().GetLeft()
					w.SetIsRed(n.GetParent().GetIsRed())
					n.GetParent().SetIsRed(False)
					w.GetLeft().SetIsRed(False)
					self.RightRotation(n.GetParent())
					n = self.__root
		n.SetIsRed(False)
	
	#função que retorna True se a árvore estiver vazia (raiz é igual a nulo)
	#e False caso contrário
	def isEmpty(self):
		return self.GetRoot() == self.nulo
	
	#a funcao search só deve ser chamada quando a raiz não for nula (usar o método isEmpty() para verificação
	def Search(self, data):
		x = self.__root # nomeia x como a raiz
		while x != self.nulo: # procura o elemento desejado
			if data == x.GetKey(): # se achar, retorna ele
				return x
			else:
				if data < x.GetKey(): # procura pelo lado esquerdo pra elementos menores
					x = x.GetLeft()
				else: # lado direito pros maiores
					x = x.GetRight()
		else:
			return None #retorna None caso nó buscado não esteja na árvore

	def Remove(self, data): # chama o RBRemove passando o elemento que se quer deletar, usando o Search
		self.RBRemove(self.Search(data))

	def RBRemove(self, n):
		if n.GetLeft() == self.nulo or n.GetRight() == self.nulo: # se n tiver apenas um filho e o outro for nulo
			y = n # y recebe n
		else: # caso contrário, n possui dois filhos
			y = self.Predecessor(n) # procura o maior nó que é menor que n
		if n.GetLeft() != self.nulo: # se n possuir um filho esquerdo
			x = y.GetLeft() # faz x receber ele
		else: # se possuir um direito
			x = y.GetRight() # faz x receber ele
		x.SetParent(y.GetParent()) # transforma o pai de x no pai de y
		if y.GetParent() == self.nulo: # se o pai de y for nulo, então a raiz será x
			self.__root = x
		elif y == y.GetParent().GetLeft(): # se y for o filho esquerdo
			y.GetParent().SetLeft(x) # o filho esquerdo do pai de y será x
		else: # caso contrário o filho direito do pai de y será x
			y.GetParent().SetRight(x)
		if y != n: # verifica se y é diferente de n (o nó que queremos deletar)
			n.SetKey(y.GetKey()) # copia as informações de y pra n
			n.SetData(y.GetData())
			if y.GetRight() != self.nulo:
				n.SetRight(y.GetRight())
			if y.GetLeft() != self.nulo:
				n.SetLeft(y.GetLeft())	
		if not y.GetIsRed(): # verifica se y é vermelho ou preto, se for preto chama o RBRemoveFixup pra rebalancear a árvore
			self.RBRemoveFixUp(x)
		return y
		# é necessário notar que y é o elemento que está sendo excluído, n por sua vez vai receber as informações do seu antecessor 
		# já x faz o papel de ocupar o lugar que antes era de n

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
		if noh.GetParent() == self.nulo:
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
		if noh.GetParent() == self.nulo:
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
		
	def TreeWalk(self):
		self.InOrderTreeWalk(self.__root)

	def InOrderTreeWalk(self, root):
		#percorre a árvore em ordem (menor para maior)
		if root != self.nulo:
			self.InOrderTreeWalk(root.GetLeft())
			print(root)
			self.InOrderTreeWalk(root.GetRight())

		
	def Maximum(self, noh):
    	# retorna o número máximo
		while noh.GetRight() != self.nulo:
			noh = noh.GetRight()
		return noh
		
	
	def Minimum(self, noh):
		# retorna o número mínimo
		while noh.GetLeft() != self.nulo:
			noh = noh.GetLeft()
		return noh
	
	def Successor(self, noh):
		# retorna o número sucessor à entrada
		if noh.GetRight() != self.nulo:
			return self.Minimum(noh.GetRight())
		y = noh.GetParent()
		while y != self.nulo and noh == y.GetRight():
			noh = y
			y = y.GetParent()
		return y

	def Predecessor(self, noh):
		# retorna o número antecessor à entrada
		print(noh)
		if noh == self.nulo:
			return 0
		elif noh.GetLeft() != self.nulo:
			return self.Maximum(noh.GetLeft())
		y = noh.GetParent()
		while y != self.nulo and noh == y.GetLeft():
			noh = y
			y = y.GetParent()
		return y

'''Arvore = BinaryTree()
Arvore.Insert(10)
Arvore.Insert(11)
Arvore.Insert(20)
Arvore.Insert(78)
Arvore.Insert(100)
Arvore.Insert(111)
Arvore.TreeWalk()
print("reset..")
Arvore.ResetTree()
Arvore.TreeWalk()'''