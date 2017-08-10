# Árvore Rubro-negra - AED
# Projeto AED - BSI 2017.1 - UFRPE
###################################

from armazenar import *
from tree import *
from cartao import *
from estabelecimento import *
from geradorId import *
from pathlib import Path

'''Métodos dos Cartões'''

# cadastra um cartão na árvore caso ele ainda não exista, se não ele retorna uma mensagem de erro
def CadastrarCartao(numero, titular, limiteTotal):
    if CarTree.Search(numero) != None:
        return False
    else:
        CarTree.Insert(numero, Card(numero, titular, limiteTotal))
        return True

# busca o cartão e retorna o objeto, pra ser usado no desconto caso o limite atual tenha quantidade suficiente pra a compra ser feita
# caso o cartão não existe, ele retorna uma mensagem de erro
def VerificarCartao(numero):
    cartao = CarTree.Search(numero)
    if cartao != None:
        return cartao
    else:
        return None

def VerificarLimite(numero, valorCompra):
    cartao = CarTree.Search(numero)
    if cartao.GetData().getLimiteAtual() >= valorCompra:
        return True
    else:
        return False

#Função que verifica se o objetoCartao possui limite para compra
#Retorna True se tiver limite, False se não
def VerificarLimiteByObj(objetoCartao, valorCompra):
    if objetoCartao.GetData().getLimiteAtual() >= valorCompra:
        return True
    else:
        return False
    
'''Métodos dos Estabelecimentos'''

# cadastra um estabelecimento caso ele ainda não exista no árvore, caso contrário retorna uma mensagem de erro
def CadastrarEstabelecimento(nome, horario):
    if EstTree.Search(geraId(nome)) != None:
        return False
    else:
        EstTree.Insert(geraId(nome), Estabelecimento(nome, horario))
        return True

# busca o estabelecimento e retorna o horário de funcionamento e se o estabelecimento existe. Se o estabelecimento não existir
# ele retorna uma mensagem de erro
def VerificarEstabelecimento(nome):
    estabelecimento = EstTree.Search(geraId(nome))
    if estabelecimento != None:
        return estabelecimento
    else:
        return None
    
#Retorna True caso compra tenha sido realizada em horario comercial
#Formato horario estabelecimento: HH:MM-HH:MM
def VerificaHorarioComercial(horaCompra, objEstabelecimento):
    horaInicial, horaFinal = objEstabelecimento.getHorario().split("-")
    horarioInicial = HoraParaMinutos(horaInicial)
    horarioFinal = HoraParaMinutos(horaFinal)
    horarioCompra = HoraParaMinutos(horaCompra)
    if horarioCompra >= horarioInicial and horarioCompra <= horarioFinal:
        return True
    else:
        return False

#Transforma horario (formato string -> HH:MM) em minutos
def HoraParaMinutos(horario):
    qtdHoras, qtdMinutos = horario.split(":")
    qtdTotalMinutos = int(qtdMinutos) + (int(qtdHoras) * 60)
    return qtdTotalMinutos

def SalvarEstado():
    Salvar(CarTree, EstTree)

if Path("infoe.ar").is_file() and Path("infoc.ar").is_file():
    i = Load()
    CarTree = i[0]
    EstTree = i[1]
else:
    CarTree = BinaryTree()
    EstTree = BinaryTree()