# interface

from administradora import *
from geradorId import *
import sys, os
import msvcrt as m

def IniciaInterface():
	print("Bem vindo(a) ao sistema de cartão de crédito")
	print("Escolha uma das opções abaixo:")
	print("1 - Cadastrar Cartão\n2 - Cadastrar Estabelecimento\n3 - Buscar Cartão\n4 - Obter Extrato\n5 - Buscar Estabelecimento\n6 - Montante Negociado\n7 - Realizar Compra\n8 - Sair")
	print("Digite a sua escolha: ", end="")
	escolha = input()
	if escolha == "1":
		LimpaConsole()
		CadastraCartao()
		LimpaConsole()
		IniciaInterface()
	elif escolha == "2":
		LimpaConsole()
		CadastraEstabelecimento()
		LimpaConsole()
		IniciaInterface()
	elif escolha == "3":
		LimpaConsole()
		BuscarCartao()
		IniciaInterface()
	elif escolha == "4":
		LimpaConsole()
		ObterExtrato()
		IniciaInterface()
	elif escolha == "5":
		LimpaConsole()
		BuscarEstabelecimento()
		LimpaConsole()
		IniciaInterface()
	elif escolha == "6":
		LimpaConsole()
		MontanteEstabelecimento()
		IniciaInterface()
	elif escolha == "7":
		LimpaConsole()
		RealizarCompra()
		LimpaConsole()
		IniciaInterface()
	else:
		sys.exit(0)
		print("um valor foi digitado incorretamente")

def RealizarCompra():
	try:
	    #É necessário receber também a hora em que a compra foi efetuada (verificar horario establecimento)
	    print("Digite o valor da compra (com no máximo duas casas decimais), o número do cartão, o estabelecimento e a hora (no formato HH:MM) da compra separados por espaços:\n", end="")
	    valor, numero, estabelecimento, horaCompra = input().split(" ", 3)
	    #ATENÇÃO: cartao é um objeto do tipo no, não do tipo cartao
	    cartao = VerificarCartao(int(numero))
	    #Verifica se o cartao existe
	    if cartao == None:
	        print("Esse cartão não existe, a compra não pode ser realizada")
	        IniciaInterface()
	    else:
	        #Se existir, verifica se o cartao tem limite suficiente para a compra
	        if VerificarLimiteByObj(cartao, float(valor)):
	            print("Há limite para realizar a compra")
	            #Agora deve-se verificar se o estabelecimento esta cadastrado
	            resultBuscaEstabelecimento = VerificarEstabelecimento(estabelecimento.lower())
	            #Se estabelecimento estiver cadastrado
	            if resultBuscaEstabelecimento != None:
	                print("Estabelecimento está cadastrado!")
	                #Agora deve-se verificar se a compra foi efetuada em horário comercial
	                horarioOk = VerificaHorarioComercial(horaCompra, resultBuscaEstabelecimento.GetData())
	                #Se compra for efetuada em horario comercial
	                if horarioOk:
	                    cartao.GetData().desconto(float(valor))
	                    cartao.GetData().AddMontante(float(valor))
	                    resultBuscaEstabelecimento.GetData().AddMontante(float(valor))
	                    resultBuscaEstabelecimento.GetData().AddValor((float(valor)*0.02))
	                    print("Limite atual do cartao: R$ %.2f" % (cartao.GetData().getLimiteAtual()))
	                    print("*"*20)
	                    print("Compra autorizada!")
	                    print("*"*20)
	                    IniciaInterface()
	                else:
	                	print("Estabelecimento fora do horário de funcionamento.")
	                	IniciaInterface()
	            #Se estabelecimento não estiver cadastrado
	            else:
	                print("Estabelecimento não está cadastrado!")
	                IniciaInterface()
	        #Caso cartao não tenha limite para efetuar a compra
	        else:
	            print("Não há limite suficiente para realizar a compra")
	            IniciaInterface()
	except:
		print("Você digitou um valor ou valores incorretos. Por favor, tente novamente.")
		IniciaInterface()

def ObterExtrato():
	print("Digite o número do cartão que deseja ver o extrato: ", end="")
	numero = int(input())
	cartao = VerificarCartao(numero)
	if cartao == None:
		print("Esse cartão não existe no sistema")
	else:
		print("-"*40)
		print("Titular: %s - Número do Cartão: %s" % (cartao.GetData().getTitular(), cartao.GetData().getNumero()))
		print("-"*40)
		cartao.GetData().ImprimeMontante()
		print("-"*40)

def MontanteEstabelecimento():
	print("Digite o nome do estabelecimento que deseja verificar o montante: ", end="")
	nome = input()
	estabelecimento = VerificarEstabelecimento(nome.lower())
	if estabelecimento == None:
		print("Este estabelecimento não existe no sistema")
	else:
		print("-"*40)
		print("Nome do Estabelecimento: %s - Horário de Funcionamento: %s" % (estabelecimento.GetData().getNome(), estabelecimento.GetData().getHorario()))
		print("-"*40)
		estabelecimento.GetData().ImprimeMontante()
		print("-"*40)
		print("Valor mensal a ser pago a administradora: R$ %.2f" % estabelecimento.GetData().getValor())
		print("-"*40)

def BuscarCartao():
	try:
		print("Digite o número do cartão a ser buscado: ", end="")
		numero = int(input())
		cartao = VerificarCartao(numero)
		if cartao == None:
			print("Esse cartão não existe no sistema")
		else:
			print("-"*40)
			print("Nome do Titular: %s\nNúmero do Cartão: %s\nLimite Atual: R$ %.2f" % (cartao.GetData().getTitular(), cartao.GetData().getNumero(), cartao.GetData().getLimiteAtual()))
			print("-"*40)
	except:
		print("Você digitou um valor ou valores incorretos. Por favor, tente novamente.")
		IniciaInterface()

def BuscarEstabelecimento():
	try:
		print("Digite o nome do estabelecimento a ser buscado: ", end="")
		nome = input()
		estabelecimento = VerificarEstabelecimento(nome.lower())
		if estabelecimento == None:
			print("Esse estabelecimento não existe no sistema")
		else:
			print("-"*40)
			print("Nome do Estabelecimento: %s\nHorário de Funcionamento: %s" % (estabelecimento.GetData().getNome(), estabelecimento.GetData().getHorario()))
			print("-"*40)
	except:
		print("Você digitou um valor ou valores incorretos. Por favor, tente novamente.")
		IniciaInterface()

def CadastraCartao():
	try:
		print("Digite o nome do titular, o numero do cartão e qual será o limite total separado por espaço;")
		titular, numero, limite = input().split(" ", 2)
		if not CadastrarCartao(int(numero), titular, int(limite)):
			print("O cartão já está cadastrado no sistema")
		else:
			print("O cartão foi cadastrado com sucesso!")
	except:
		print("Você digitou um valor ou valores incorretos. Por favor, tente novamente.")
		IniciaInterface()

def CadastraEstabelecimento():
	try:
		print("Digite o nome do estabelecimento e o horário de funcionamento separado por espaço;")
		nome, horario = input().split(" ", 2)
		if not CadastrarEstabelecimento(nome, horario):
			print("O estabelecimento já se encontra cadastrado no sistema")
		else:
			print("O estabelecimento foi cadastrado com sucesso!")
	except:
		print("Você digitou um valor ou valores incorretos. Por favor, tente novamente.")
		IniciaInterface()

def LimpaConsole(): # Procura o tipo de SO (Windows, Linux, OS) e limpa o console
	os.system('cls' if os.name == 'nt' else 'clear')


IniciaInterface()
SalvarEstado()