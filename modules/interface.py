# interface

from administradora import *
from geradorId import *

def IniciaInterface():
	print("Bem vindo(a) ao sistema de cartão de crédito")
	print("Escolha uma das opções abaixo:")
	print("1 - Cadastrar Cartão\n2 - Cadastrar Estabelecimento\n3 - Buscar Cartão\n4 - Buscar Estabelecimento\n5 - Realizar Compra\n6 - Sair")
	print("Digite a sua escolha: ", end="")
	escolha = input()
	if escolha == "1":
		CadastraCartao()
		IniciaInterface()
	elif escolha == "2":
		CadastraEstabelecimento()
		IniciaInterface()
	elif escolha == "3":
		BuscarCartao()
		IniciaInterface()
	elif escolha == "4":
		BuscarEstabelecimento()
		IniciaInterface()
	elif escolha == "5":
		RealizarCompra()
		IniciaInterface()

def RealizarCompra():
	print("Digite o valor da compra, o número do cartão e o estabelecimento separados por espaços: ", end="")
	valor, numero, estabelecimento = input().split(" ", 2)
	cartao = VerificarCartao(int(numero))
	if cartao == None:
		print("Esse cartão não existe, a compra não pode ser realizada")
		IniciaInterface()
	else:
		if VerificarLimite(int(numero), int(valor)):
			print("Há limite para realizar a compra")
		else:
			print("Não há limite suficiente para realizar a compra")

def BuscarCartao():
	print("Digite o número do cartão a ser buscado: ", end="")
	numero = int(input())
	cartao = VerificarCartao(numero)
	if cartao == None:
		print("Esse cartão não existe no sistema")
	else:
		print("-"*30)
		print("Nome do Titular: %s\nNúmero do Cartão: %s\nLimite Atual: %s" % (cartao.GetData().getTitular(), cartao.GetData().getNumero(), cartao.GetData().getLimiteAtual()))
		print("-"*30)

def BuscarEstabelecimento():
	print("Digite o nome do estabelecimento a ser buscado: ", end="")
	nome = input()
	estabelecimento = VerificarEstabelecimento(nome)
	if estabelecimento == None:
		print("Esse estabelecimento não existe no sistema")
	else:
		print("-"*30)
		print("Nome do Estabelecimento: %s\nHorário de Funcionamento: %s" % (estabelecimento.GetData().getNome(), estabelecimento.GetData().getHorario()))
		print("-"*30)

def CadastraCartao():
	print("Digite o nome do titular, o numero do cartão e qual será o limite total separado por espaço;")
	titular, numero, limite = input().split(" ", 2)
	if not CadastrarCartao(int(numero), titular, int(limite)):
		print("O cartão já está cadastrado no sistema")
	else:
		print("O cartão foi cadastrado com sucesso!")

def CadastraEstabelecimento():
	print("Digite o nome do estabelecimento e o horário de funcionamento separado por espaço;")
	nome, horario = input().split(" ", 2)
	if not CadastrarEstabelecimento(nome, horario):
		print("O estabelecimento já se encontra cadastrado no sistema")
	else:
		print("O estabelecimento foi cadastrado com sucesso!")


IniciaInterface()