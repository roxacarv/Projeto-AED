# Árvore Rubro-negra - AED
# Projeto AED - BSI 2017.1 - UFRPE
###################################

from administradora import *

def CadastrarCartao(titular, numero, limiteTotal):
    if VerificarCartao(titular, numero, limiteTotal):
        return 
    else:
        return  "O cartão foi cadastrado com sucesso"

'''def CadastrarEstabelecimento(nome, horario):
    # cadastrar estabelecimento'''