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
    #É necessário receber também a hora em que a compra foi efetuada (verificar horario establecimento)
    print("Digite o valor da compra, o número do cartão, o estabelecimento e a hora da compra separados por espaços:\n", end="")
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
            resultBuscaEstabelecimento = VerificarEstabelecimento(estabelecimento)
            #Se estabelecimento estiver cadastrado
            if resultBuscaEstabelecimento != None:
                print("Estabelecimento está cadastrado!")
                #Agora deve-se verificar se a compra foi efetuada em horário comercial
                horarioOk = VerificaHorarioComercial(horaCompra, resultBuscaEstabelecimento.GetData())
                #Se compra for efetuada em horario comercial
                if horarioOk:
                    
                    cartao.GetData().desconto(float(valor))
                    print("Limite atual do cartao: R$ %.2f" %(cartao.GetData().getLimiteAtual()))
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