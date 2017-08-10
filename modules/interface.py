# interface

from administradora import *
from geradorId import *
import sys, os
import msvcrt as m

def IniciaInterface():
	print("--------------------------------------------")
	print("Bem vindo(a) ao sistema de cartão de crédito")
	print("--------------------------------------------")
	print("Escolha uma das opções abaixo:")
	print("1 - Cadastrar Cartão\n2 - Cadastrar Estabelecimento\n3 - Buscar Cartão\n4 - Obter Extrato\n5 - Buscar Estabelecimento\n6 - Montante Negociado\n7 - Realizar Compra\n8 - Listar Cartões\n9 - Listar Estabelecimentos\n0 - Sair (ou Enter)")
	print("--------------------------------------------")
	print("Digite a sua escolha: ", end="")
	escolha = input()
	if escolha == "1":
		LimpaConsole()
		CadastraCartao()
		IniciaInterface()
	elif escolha == "2":
		LimpaConsole()
		CadastraEstabelecimento()
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
		IniciaInterface()
	elif escolha == "6":
		LimpaConsole()
		MontanteEstabelecimento()
		IniciaInterface()
	elif escolha == "7":
		LimpaConsole()
		RealizarCompra()
		IniciaInterface()
	elif escolha == "8":
		LimpaConsole()
		ListarCartao()
		print("Pressione qualquer tecla pra voltar ao menu principal")
		m.getch()
		LimpaConsole()
		IniciaInterface()
	elif escolha == "9":
		LimpaConsole()
		ListaEstabelecimentos()
		print("Pressione qualquer tecla pra voltar ao menu principal")
		m.getch()
		LimpaConsole()
		IniciaInterface()
	else:
		sys.exit(0)

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
	        print("Pressione qualquer tecla para voltar ao menu inicial")
	        m.getch()
	        LimpaConsole()
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
	                    print("-"*25)
	                    print("Compra autorizada!")
	                    print("-"*25)
	                    print("Compra efetuada!")
	                    print("Pressione qualquer tecla para voltar ao menu inicial")
	                    m.getch()
	                    LimpaConsole()
	                    IniciaInterface()
	                else:
	                	print("Estabelecimento fora do horário de funcionamento.")
	                	print("Pressione qualquer tecla para voltar ao menu inicial")
	                	m.getch()
	                	LimpaConsole()
	                	IniciaInterface()
	            #Se estabelecimento não estiver cadastrado
	            else:
	                print("Estabelecimento não está cadastrado!")
	                print("Pressione qualquer tecla para voltar ao menu inicial")
	                m.getch()
	                LimpaConsole()
	                IniciaInterface()
	        #Caso cartao não tenha limite para efetuar a compra
	        else:
	            print("Não há limite suficiente para realizar a compra")
	            print("Pressione qualquer tecla para voltar ao menu inicial")
	            m.getch()
	            LimpaConsole()
	            IniciaInterface()
	except:
		print("Você digitou um valor ou valores incorretos. Por favor, tente novamente.")
		print("Pressione qualquer tecla para voltar ao menu inicial")
		m.getch()
		LimpaConsole()
		IniciaInterface()

def ObterExtrato():
	try:
		print("Digite o número do cartão que deseja ver o extrato: ", end="")
		numero = int(input())
		cartao = VerificarCartao(numero)
		if cartao == None:
			print("Esse cartão não existe no sistema")
			print("Pressione qualquer tecla para voltar ao menu inicial")
			m.getch()
			LimpaConsole()
		else:
			print("-"*40)
			print("Titular: %s - Número do Cartão: %s" % (cartao.GetData().getTitular(), cartao.GetData().getNumero()))
			print("-"*40)
			cartao.GetData().ImprimeMontante()
			print("-"*40)
			print("Pressione qualquer tecla para voltar ao menu inicial")
			m.getch()
			LimpaConsole()
	except:
		print("Você digitou um valor ou valores incorretos. Por favor, tente novamente.")
		print("Pressione qualquer tecla para voltar ao menu inicial")
		m.getch()
		LimpaConsole()

def MontanteEstabelecimento():
	print("Digite o nome do estabelecimento que deseja verificar o montante: ", end="")
	nome = input()
	estabelecimento = VerificarEstabelecimento(nome)
	if estabelecimento == None:
		print("Este estabelecimento não existe no sistema")
		print("Pressione qualquer tecla para voltar ao menu inicial")
		m.getch()
		LimpaConsole()
	else:
		print("-"*40)
		print("Nome do Estabelecimento: %s - Horário de Funcionamento: %s" % (estabelecimento.GetData().getNome(), estabelecimento.GetData().getHorario()))
		print("-"*40)
		estabelecimento.GetData().ImprimeMontante()
		print("-"*40)
		print("Valor mensal a ser pago a administradora: R$ %.2f" % estabelecimento.GetData().getValor())
		print("-"*40)
		print("Pressione qualquer tecla para voltar ao menu inicial")
		m.getch()
		LimpaConsole()

def BuscarCartao():
	try:
		print("Digite o número do cartão a ser buscado: ", end="")
		numero = int(input())
		cartao = VerificarCartao(numero)
		if cartao == None:
			print("Esse cartão não existe no sistema")
			print("Pressione qualquer tecla para voltar ao menu inicial")
			m.getch()
			LimpaConsole()
		else:
			print("-"*40)
			print("Nome do Titular: %s\nNúmero do Cartão: %s\nLimite Atual: R$ %.2f" % (cartao.GetData().getTitular(), cartao.GetData().getNumero(), cartao.GetData().getLimiteAtual()))
			print("-"*40)
			print("Pressione qualquer tecla para voltar ao menu inicial")
			m.getch()
			LimpaConsole()
	except:
		print("Você digitou um valor ou valores incorretos. Por favor, tente novamente. Pressione qualquer tecla pra continuar.")
		m.getch()
		LimpaConsole()
		IniciaInterface()

def BuscarEstabelecimento():
	print("Digite o nome do estabelecimento a ser buscado: ", end="")
	nome = input()
	estabelecimento = VerificarEstabelecimento(nome)
	if estabelecimento == None:
		print("Esse estabelecimento não existe no sistema")
		m.getch()
		LimpaConsole()
	else:
		print("-"*40)
		print("Nome do Estabelecimento: %s\nHorário de Funcionamento: %s" % (estabelecimento.GetData().getNome(), estabelecimento.GetData().getHorario()))
		print("-"*40)

def CadastraCartao():
	try:
		print("Digite o nome do titular, o numero do cartão e qual será o limite total separado por espaço;")
		titular, numero, limite = input().split(" ", 2)
		if not CadastrarCartao(int(numero), titular, int(limite)):
			print("O cartão já está cadastrado no sistema - Pressione qualquer tecla para voltar ao menu principal.")
			m.getch()
			LimpaConsole()
		else:
			print("O cartão foi cadastrado com sucesso! - Pressione qualquer tecla para voltar ao menu principal.")
			m.getch()
			LimpaConsole()
	except:
		print("Você digitou um valor ou valores incorretos. Por favor, tente novamente. Pressione qualquer teclado para voltar ao menu inicial.")
		m.getch()
		LimpaConsole()

def CadastraEstabelecimento():
	try:
		print("Digite o nome do estabelecimento e o horário de funcionamento separado por espaço;")
		nome, horario = input().split(" ", 2)
		if not CadastrarEstabelecimento(nome, horario):
			print("O estabelecimento já se encontra cadastrado no sistema - Pressione qualquer tecla para voltar ao menu principal.")
			m.getch()
			LimpaConsole()
		else:
			print("O estabelecimento foi cadastrado com sucesso! - Pressione qualquer tecla para voltar ao menu principal.")
			m.getch()
			LimpaConsole()
	except:
		print("Você digitou um valor ou valores incorretos. Por favor, tente novamente. - Pressione qualquer tecla para voltar ao menu principal.")
		m.getch()
		LimpaConsole()
		IniciaInterface()

def LimpaConsole(): # Procura o tipo de SO (Windows, Linux, OS) e limpa o console
	os.system('cls' if os.name == 'nt' else 'clear')


IniciaInterface()
SalvarEstado()